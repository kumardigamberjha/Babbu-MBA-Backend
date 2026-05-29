from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from .models import Course, Chapter, Topic, UserTopicProgress
from .serializers import (
    CourseSerializer,
    CourseDetailSerializer,
    ChapterSerializer,
    ChapterDetailSerializer,
    TopicSerializer,
    UserSerializer,
    RegisterSerializer,
)

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Courses to be viewed or edited.
    """
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Chapters to be viewed or edited.
    Filter by course using: ?course=<course_id>
    """
    def get_queryset(self):
        queryset = Chapter.objects.all()
        course_id = self.request.query_params.get('course')
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ChapterDetailSerializer
        return ChapterSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Topics to be viewed or edited.
    Filter by chapter using: ?chapter=<chapter_id>
    """
    def get_queryset(self):
        queryset = Topic.objects.all()
        chapter_id = self.request.query_params.get('chapter')
        if chapter_id is not None:
            queryset = queryset.filter(chapter_id=chapter_id)
        return queryset

    def get_serializer_class(self):
        return TopicSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def toggle_progress(self, request, pk=None):
        topic = self.get_object()
        user = request.user
        
        progress, created = UserTopicProgress.objects.get_or_create(
            user=user,
            topic=topic
        )
        
        if not created:
            progress.is_completed = not progress.is_completed
            progress.save()
            
        return Response({
            "is_completed": progress.is_completed,
            "topic_id": topic.id
        }, status=status.HTTP_200_OK)



class RegisterView(APIView):
    """
    API endpoint that allows new users to register.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    API endpoint that logs in a user and returns their token and profile.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response(
                {"error": "Please provide both username and password."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user": UserSerializer(user).data
            }, status=status.HTTP_200_OK)
            
        return Response(
            {"error": "Invalid username or password."},
            status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    """
    API endpoint to log out the user by deleting their token.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Delete token
            request.user.auth_token.delete()
            return Response(
                {"message": "Logged out successfully."},
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"error": "Token not found or already deleted."},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserProfileView(APIView):
    """
    API endpoint that returns the authenticated user's profile.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


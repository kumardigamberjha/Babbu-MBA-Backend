from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission, SAFE_METHODS
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

import os
from groq import Groq

class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Chapters to be viewed or edited.
    Filter by course using: ?course=<course_id>
    """
    permission_classes = [IsAdminOrReadOnly]
    
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
    permission_classes = [IsAdminOrReadOnly]

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


class ChatbotView(APIView):
    """
    API endpoint to handle Chatbot queries about MBA topics using the Groq API.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        messages = request.data.get('messages', [])
        
        if not messages:
            return Response(
                {"error": "Please provide a 'messages' list."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        groq_api_key = os.environ.get('GROQ_API_KEY')
        if not groq_api_key or groq_api_key == 'your_groq_api_key_here':
            return Response(
                {"error": "Groq API key not configured on the server."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        try:
            client = Groq(api_key=groq_api_key)
            
            system_prompt = {
                "role": "system",
                "content": "You are a highly knowledgeable and professional MBA tutor and assistant. Your goal is to help users understand complex business, finance, marketing, and management concepts. Use clear, concise language and provide examples where helpful. If a user asks something completely unrelated to business/MBA topics, politely redirect them back to MBA subjects."
            }
            
            # Prepend system prompt
            api_messages = [system_prompt] + messages
            
            chat_completion = client.chat.completions.create(
                messages=api_messages,
                model="llama-3.3-70b-versatile", # Strong model for knowledge tasks
                temperature=0.7,
                max_tokens=1024,
            )
            
            response_content = chat_completion.choices[0].message.content
            
            return Response(
                {
                    "response": response_content
                }, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course, Chapter, Topic, UserTopicProgress

class TopicSerializer(serializers.ModelSerializer):
    is_completed = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'chapter', 'title', 'slug', 'content', 'order', 'is_published', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def get_is_completed(self, obj):
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            return UserTopicProgress.objects.filter(
                user=request.user,
                topic=obj,
                is_completed=True
            ).exists()
        return False


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'course', 'title', 'slug', 'order', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']


class ChapterDetailSerializer(serializers.ModelSerializer):
    topics = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = ['id', 'course', 'title', 'slug', 'order', 'topics', 'created_at', 'updated_at']

    def get_topics(self, obj):
        # Only return published topics, ordered by order
        published_topics = obj.topics.filter(is_published=True).order_by('order')
        # Pass context to serializer to enable user progress queries inside child serializer
        return TopicSerializer(published_topics, many=True, context=self.context).data


class ChapterSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'slug', 'order']


class CourseSerializer(serializers.ModelSerializer):
    chapters_count = serializers.IntegerField(source='chapters.count', read_only=True)
    modules = serializers.SerializerMethodField()
    progress_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'icon', 'description', 'chapters_count', 'modules', 'progress_percentage', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def get_modules(self, obj):
        ordered_chapters = obj.chapters.all().order_by('order')
        return ChapterSummarySerializer(ordered_chapters, many=True).data

    def get_progress_percentage(self, obj):
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            total_topics = Topic.objects.filter(chapter__course=obj, is_published=True).count()
            if total_topics == 0:
                return 0
            completed_topics = UserTopicProgress.objects.filter(
                user=request.user,
                topic__chapter__course=obj,
                is_completed=True
            ).count()
            return int((completed_topics / total_topics) * 100)
        return 0


class CourseDetailSerializer(serializers.ModelSerializer):
    chapters = serializers.SerializerMethodField()
    progress_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'icon', 'description', 'chapters', 'progress_percentage', 'created_at', 'updated_at']

    def get_chapters(self, obj):
        # Return chapters ordered by order
        ordered_chapters = obj.chapters.all().order_by('order')
        return ChapterDetailSerializer(ordered_chapters, many=True, context=self.context).data

    def get_progress_percentage(self, obj):
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            total_topics = Topic.objects.filter(chapter__course=obj, is_published=True).count()
            if total_topics == 0:
                return 0
            completed_topics = UserTopicProgress.objects.filter(
                user=request.user,
                topic__chapter__course=obj,
                is_completed=True
            ).count()
            return int((completed_topics / total_topics) * 100)
        return 0



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

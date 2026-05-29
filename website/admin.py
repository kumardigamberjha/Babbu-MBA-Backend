from django.contrib import admin
from .models import Course, Chapter, Topic, UserTopicProgress

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'icon', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'slug', 'order', 'created_at')
    list_filter = ('course',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('course', 'order')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'slug', 'order', 'is_published', 'created_at')
    list_filter = ('chapter__course', 'chapter', 'is_published')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('chapter', 'order')


@admin.register(UserTopicProgress)
class UserTopicProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'is_completed', 'completed_at')
    list_filter = ('is_completed', 'user')
    search_fields = ('user__username', 'topic__title')


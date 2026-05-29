from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    icon = models.CharField(max_length=100, default='building-2', help_text="Lucide icon name (e.g. building-2, wallet, megaphone)")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Chapter(models.Model):
    course = models.ForeignKey(Course, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Order position of this chapter in the course")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        unique_together = ('course', 'slug')

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Topic(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, blank=True)
    content = HTMLField(help_text="Rich text content of the topic")
    order = models.PositiveIntegerField(default=0, help_text="Order position of this topic in the chapter")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        unique_together = ('chapter', 'slug')

    def __str__(self):
        return f"{self.chapter.title} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class UserTopicProgress(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='topic_progress')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='user_progress')
    is_completed = models.BooleanField(default=True)
    completed_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Topic Progress"
        verbose_name_plural = "User Topic Progresses"
        unique_together = ('user', 'topic')

    def __str__(self):
        return f"{self.user.username} - {self.topic.title} ({'Completed' if self.is_completed else 'Incomplete'})"


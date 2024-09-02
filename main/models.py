from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    pfp = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, default="IDk")
    auto_slug = AutoSlugField(populate_from='name', unique=True, blank=True, max_length=255)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    auto_slug = AutoSlugField(populate_from='name', unique=True, blank=True, max_length=255)

    def __str__(self):
        return self.name

class Note(models.Model):
    topics = models.ManyToManyField(Topic, related_name='notes')
    title = models.CharField(max_length=255)
    content = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_notes')
    created_at = models.DateTimeField(auto_now_add=True)
    auto_slug = AutoSlugField(populate_from='title', unique=True, blank=True, max_length=255)

    def __str__(self):
        return self.title

class Question(models.Model):
    topics = models.ManyToManyField(Topic, related_name='questions')
    question_text = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_questions')
    created_at = models.DateTimeField(auto_now_add=True)
    auto_slug = AutoSlugField(populate_from='question_text', unique=True, blank=True, max_length=255)

    def __str__(self):
        return self.question_text[:50]  # Show a snippet of the question

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Make this a generic relation (to be used for both notes and questions)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')

    def __str__(self):
        return f"Comment by {self.commented_by} on {self.created_at}"

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # Show a snippet of the message

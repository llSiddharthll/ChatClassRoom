from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

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
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    content = models.TextField()
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # Show a snippet of the comment

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # Show a snippet of the message

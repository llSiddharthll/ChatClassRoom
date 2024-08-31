from django import forms
from .models import Note, Question, Topic, Comment, ChatMessage

class NoteForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        label="Select Topics",
        required=True
    )

    class Meta:
        model = Note
        fields = ['topics', 'title', 'content']

class QuestionForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        label="Select Topics",
        required=True
    )

    class Meta:
        model = Question
        fields = ['topics', 'question_text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['receiver', 'content']

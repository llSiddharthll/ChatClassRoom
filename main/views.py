from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject, Topic, Note, Question, Comment, UserProfile
from .forms import NoteForm, QuestionForm, CommentForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return JsonResponse({'success': False, 'error': 'Passwords do not match.'}, status=400)

        form = UserCreationForm({
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Form is not valid.'}, status=400)

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid username or password.'}, status=400)
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

def home(request):
    return render(request, "home.html")

# List all subjects
def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})

# Detail view of a subject including its topics
def topics(request, slug):
    subject = get_object_or_404(Subject, auto_slug=slug)
    topics = subject.topics.all()
    return render(request, 'topics.html', {'subject': subject, 'topics': topics})

# Detail view of a topic including notes and questions
def topic_detail(request, subject_slug, topic_slug):
    topic = get_object_or_404(Topic, auto_slug=topic_slug)
    subject = get_object_or_404(Subject, auto_slug=subject_slug)
    notes = Note.objects.filter(topics=topic)
    questions = Question.objects.filter(topics=topic)

    # Fetch all comments related to the notes and questions
    notes_comments = Comment.objects.filter(note__in=notes)
    questions_comments = Comment.objects.filter(question__in=questions)

    # Create dictionaries to store comments for each note and question
    notes_comments_dict = {note.id: [] for note in notes}
    questions_comments_dict = {question.id: [] for question in questions}

    # Populate dictionaries with comments
    for comment in notes_comments:
        notes_comments_dict[comment.note.id].append(comment)
    
    for comment in questions_comments:
        questions_comments_dict[comment.question.id].append(comment)

    context = {
        'topic': topic,
        'subject': subject,
        'notes': notes,
        'questions': questions,
        'notes_comments': notes_comments_dict,
        'questions_comments': questions_comments_dict,
    }

    return render(request, 'topic_detail.html', context)

# Detail view of a note
def note_detail(request, subject_slug, topic_slug, note_slug):
    note = get_object_or_404(Note, auto_slug=note_slug)

    # Get the topic associated with the note
    topic = get_object_or_404(Topic, auto_slug=topic_slug)

    # Get the subject associated with the topic
    subject = get_object_or_404(Subject, auto_slug=subject_slug)

    # Get the previous note
    previous_note = Note.objects.filter(id__lt=note.id).order_by('-id').first()

    # Get the next note
    next_note = Note.objects.filter(id__gt=note.id).order_by('id').first()

    context = {
        'topic': topic,
        'subject': subject,
        'note': note,
        'previous_note': previous_note,
        'next_note': next_note,
    }
    return render(request, 'note_detail.html', context)

def chat(request):
    return render(request, 'chat.html')

@login_required
def add_note_comment(request, topic_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        note_id = request.POST.get('note_id')
        note = get_object_or_404(Note, id=note_id)
        comment = Comment(content=content, commented_by=request.user, note=note)
        comment.save()
        return redirect('topic_detail', topic_id=topic_id)
    return redirect('topic_detail', topic_id=topic_id)

@login_required
def add_question_comment(request, topic_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        question_id = request.POST.get('question_id')
        question = get_object_or_404(Question, id=question_id)
        comment = Comment(content=content, commented_by=request.user, question=question)
        comment.save()
        return redirect('topic_detail', topic_id=topic_id)
    return redirect('topic_detail', topic_id=topic_id)

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            # Retrieve selected topics from form data
            topics_ids = request.POST.getlist('topics')
            note.uploaded_by = request.user
            note.save()
            note.topics.set(topics_ids)  # Set many-to-many relationships
            return redirect('dashboard')  # Redirect to dashboard or appropriate page
    else:
        form = NoteForm()
    topics = Topic.objects.all()
    return render(request, 'note_form.html', {'form': form, 'topics': topics})

@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            # Retrieve selected topics from form data
            topics_ids = request.POST.getlist('topics')
            question.added_by = request.user
            question.save()
            question.topics.set(topics_ids)  # Set many-to-many relationships
            return redirect('dashboard')  # Redirect to dashboard or appropriate page
    else:
        form = QuestionForm()
    topics = Topic.objects.all()
    return render(request, 'question_form.html', {'form': form, 'topics': topics})

# Create a new comment on a note
@login_required
def create_comment_note(request, note_pk):
    """
    Creates a comment for a specific note.

    Args:
        request (HttpRequest): The HTTP request object.
        note_pk (int): The primary key of the note.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        Http404: If the note with the given primary key does not exist.

    """
    note = get_object_or_404(Note, pk=note_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.note = note
            comment.commented_by = request.user
            comment.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

# Create a new comment on a question
@login_required
def create_comment_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = question
            comment.commented_by = request.user
            comment.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def edit_profile(request):
    # Get the user's profile or create one if it doesn't exist
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('dashboard')  # Redirect to the profile page or any other page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserProfileForm(instance=profile)
    
    context = {
        'form': form,
    }
    return render(request, 'edit_profile.html', context)
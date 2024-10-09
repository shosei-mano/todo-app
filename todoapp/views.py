from django.shortcuts import render, redirect, get_object_or_404
from .models import Task  # Taskモデルをインポート
from .forms import TaskForm  # TaskFormをインポート
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


@login_required
def profile(request):
    return render(request, 'todoapp/profile.html')

@login_required
def task_list(request):
    tasks = Task.objects.all()  # すべてのタスクを取得
    return render(request, 'todoapp/index.html', {'tasks': tasks})

def index(request):
    return render(request, 'todoapp/index.html')

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority', 1)  # フォームに優先度があれば取得、なければデフォルトは1
        Task.objects.create(title=title, priority=priority)
        return redirect('task_list')
    return render(request, 'todoapp/index.html')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # タスク追加後にリストにリダイレクト
    else:
        form = TaskForm()
    
    return render(request, 'todoapp/create_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todoapp/delete_task.html', {'task': task})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.title = request.POST.get('title', task.title)
        task.priority = request.POST['priority'] # タイトルを更新
        task.save()
        return redirect('task_list')  # 一貫して'task_list'にリダイレクト

    return render(request, 'todoapp/edit_task.html', {'task': task})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'todoapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')  # 認証後にリダイレクト
    else:
        form = AuthenticationForm()
    return render(request, 'todoapp/registration/login.html', {'form': form})

@login_required
def task_search(request):
    query = request.GET.get('q', '')
    if query:
        search_results = Task.objects.filter(title__icontains=query)
    else:
        search_results = Task.objects.none()  # クエリが空の場合、結果なしに設定

    return render(request, 'todoapp/task_list.html', {
        'search_results': search_results,
        'query': query,
        'tasks': Task.objects.all(),  # すべてのタスクリストを表示
    })


@login_required
def profile(request):
    user = request.user  # ログイン中のユーザー情報を取得
    context = {
        'username': user.username,
        'email': user.email,
        'full_name': f"{user.first_name} {user.last_name}",  # フルネーム（姓と名）
    }
    return render(request, 'todoapp/profile.html', context)

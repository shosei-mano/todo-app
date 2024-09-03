from django.shortcuts import render, redirect
from .models import Task  # Taskモデルをインポート

def create_task(request):
    if request.method == 'POST':
        # フォームからのデータを保存する処理をここに書く
        task_name = request.POST.get('task_name')
        if task_name:
            Task.objects.create(name=task_name)
        return redirect('index')  # タスク作成後にインデックスページにリダイレクト

    return render(request, 'todoapp/create_task.html')

def index(request):
    # タスクのリストを取得してコンテキストに渡す
    tasks = Task.objects.all()  # タスクがまだなければこの行は削除してもOKです
    return render(request, 'todoapp/index.html')
from django import forms
from .models import Task 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 # Taskモデルをインポート

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'completed']  # タスクのタイトルをフォームに表示するフィールドとして指定
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # '/' でアクセスしたときにindexビューを呼び出す
    path('create/', views.create_task, name='create_task'), 
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),


] # タスク作成のパス



from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # '/' でアクセスしたときにindexビューを呼び出す
    path('create/', views.create_task, name='create_task'),  # タスク作成のパス
]


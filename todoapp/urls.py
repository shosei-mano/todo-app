from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # ルートURLをタスクリストに設定
    path('create_task/', views.create_task, name='create_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='task_delete'),
    path('edit_task/<int:task_id>/', views.edit_task, name='task_edit'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todoapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='todoapp/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # パスワードリセット用のURL
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='todoapp/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='todoapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='todoapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='todoapp/password_reset_complete.html'), name='password_reset_complete'),

    # タスク検索用のURL
    path('search/', views.task_search, name='task_search'),

    # インデックスページへのURL
    path('index/', views.index, name='index'),
]

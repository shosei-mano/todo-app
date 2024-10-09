from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    PRIORITY_CHOICES = [
        ('low', '低'),
        ('medium', '中'),
        ('high', '高'),
    ]
    priority = models.CharField(max_length=7, choices=PRIORITY_CHOICES, default='medium')

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ユーザーと一対一の関係
    bio = models.TextField(max_length=500, blank=True)  # 自己紹介フィールド
    location = models.CharField(max_length=30, blank=True)  # 居住地フィールド
    birth_date = models.DateField(null=True, blank=True)  # 誕生日フィールド

    def __str__(self):
        return self.user.username
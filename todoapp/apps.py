# todoapp/apps.py
from django.apps import AppConfig

class TodoappConfig(AppConfig):
    name = 'todoapp'

    def ready(self):
        # readyメソッドの中でシグナルをインポート
        from . import signals

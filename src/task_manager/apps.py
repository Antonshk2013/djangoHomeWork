from django.apps import AppConfig


class TaskManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.task_manager'

    def ready(self):
        import src.task_manager.signals

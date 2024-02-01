from django.apps import AppConfig


class SimpleformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpleForm'
    def ready(self):
        import simpleForm.signals
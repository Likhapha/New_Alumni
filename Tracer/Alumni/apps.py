from django.apps import AppConfig


class AlumniConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Alumni'

    # In Alumni/apps.py or Alumni/__init__.py
    def ready(self):
        import Alumni.signals






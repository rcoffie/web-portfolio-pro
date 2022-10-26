from django.apps import AppConfig


class AccountEngineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "account_engine"

    def ready(self):
        import account_engine.signals

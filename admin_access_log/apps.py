from django.apps import AppConfig


class AdminAccessLogConfig(AppConfig):
    name = 'admin_access_log'
    verbose_name = "Django Admin Access Log"

    def ready(self):
        from . import receivers

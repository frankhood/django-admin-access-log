from django.apps import AppConfig


class DjangoAdminAccessLogConfig(AppConfig):
    name = 'django_admin_access_log'
    verbose_name = "Django Admin Access Log"

    def ready(self):
        from . import receivers

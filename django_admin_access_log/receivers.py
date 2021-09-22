import logging

from django.contrib.auth import user_logged_in, user_login_failed
from django.dispatch import receiver

login_logger_error = logging.getLogger("login_logger_error")
login_logger_success = logging.getLogger("login_logger_success")


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = get_client_ip(request)
    login_logger_success.info(f"{ip} {user.username}")


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, request, **kwargs):
    ip = get_client_ip(request)
    login_logger_error.error(f"{ip} {credentials}")


def get_client_ip(request):
    if request:
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
    return None

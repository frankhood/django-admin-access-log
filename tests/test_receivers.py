"""
test_django-admin-access-log.
------------

Tests for `django-admin-access-log` models module.
"""

from django.contrib.auth.models import User
from django.test import Client, TestCase
from freezegun.api import freeze_time


class TestDjangoAdminAccessLog(TestCase):
    def setUp(self):
        self.client = Client()

    @freeze_time("2021-09-22 12:00:00")
    def test_successful_login(self):
        username = "success_username"
        password = "success_password"
        self.user = User.objects.create_user(
            username=username, password=password, is_active=True, is_staff=True
        )
        with self.assertLogs(logger="login_logger_success", level="INFO") as cm:
            self.client.post(
                "/admin/login/", {"username": username, "password": password}
            )
            self.assertIn(
                "INFO:login_logger_success:127.0.0.1 success_username", cm.output
            )

    @freeze_time("2021-09-22 10:00:00")
    def test_failed_login(self):
        username = "failed_username"
        password = "failed_password"
        self.assertEqual(
            len(User.objects.filter(username=username, password=password)), 0
        )
        with self.assertLogs(logger="login_logger_error", level="ERROR") as cm:
            self.client.post(
                "/admin/login/", {"username": username, "password": password}
            )
            self.assertIn(
                "ERROR:login_logger_error:127.0.0.1 {'username': 'failed_username', 'password': '********************'}",
                cm.output,
            )

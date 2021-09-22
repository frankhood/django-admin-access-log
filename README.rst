=============================
Django Admin Access Log
=============================

.. image:: https://badge.fury.io/py/django-admin-access-log.svg
    :target: https://badge.fury.io/py/django-admin-access-log

.. image:: https://travis-ci.org/frankhood/django-admin-access-log.svg?branch=master
    :target: https://travis-ci.org/frankhood/django-admin-access-log

.. image:: https://codecov.io/gh/frankhood/django-admin-access-log/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/frankhood/django-admin-access-log

This package allows you to log successful and failed login attempts on your django admin.

========================
Documentation
========================

The full documentation is at https://django-admin-access-log.readthedocs.io.

========================
Quickstart
========================

Install Django Admin Access Log::

    pip install django-admin-access-log

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_admin_access_log',
        ...
    )


Add in your logging settings "login_logger_error" and "login_logger_success", with the handler of your choice, like this:

.. code-block:: python

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose_login": {
                "format": "%(asctime)s :: %(message)s",
            },
        },
        "handlers": {
            "login_handler_error": {
                "level": "ERROR",
                "class": "logging.handlers.MemoryHandler",
                "capacity": 200
            },
            "login_handler_success": {
                "level": "INFO",
                "class": "logging.handlers.MemoryHandler",
                "capacity": 200
            },
        },
        "loggers": {
            "login_logger_error": {
                "handlers": ["login_handler_error"],
                "level": "ERROR",
                "propagate": True,
            },
            "login_logger_success": {
                "handlers": ["login_handler_success"],
                "level": "INFO",
                "propagate": True,
            },
        },
    }

========================
Features
========================

* Receiver for user_login_failed signal send by django when failed login attempt is tried.
* Receiver for user_logged_in signal send by django when login attempt is successful.
* get_client_ip function.

========================
Running Tests
========================

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

========================
Development commands
========================

::

    pip install -r requirements_dev.txt
    invoke -l

========================
Credits
========================

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

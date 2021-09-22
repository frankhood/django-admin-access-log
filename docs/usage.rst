=====
Usage
=====

To use Django Admin Access Log in a project, add it to your `INSTALLED_APPS`:

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

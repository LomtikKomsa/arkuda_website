from .base import *

DEBUG = True

SECRET_KEY = "django-insecure-9&*a=kc2m0c0u9hgcth(^@6u-^m(314i(-8j0bb3^3am-zfzud"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass

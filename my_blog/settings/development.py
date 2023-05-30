from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "PORT": env("PG_PORT"),
        "HOST": env("PG_HOST"),
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

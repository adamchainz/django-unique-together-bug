import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "not-secret-key"
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "testproj.testapp",
]

ROOT_URLCONF = "testproj.urls"

WSGI_APPLICATION = "testproj.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
        # "ENGINE": "django.db.backends.postgresql",
        # "NAME": "testproj",
    }
}

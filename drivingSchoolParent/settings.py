"""
Django settings for drivingSchoolParent project.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-)oplcn_m=#3!5&%w8ld(b3(x8yh=4k$ql#jkb3m+p4m962xon-"  # fallback for dev
)
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

# allow both your custom domains + DO preview host
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "budgetdrivingschoolreading.com",
    "www.budgetdrivingschoolreading.com",
    "budgetdrivingschool-cnyxh.ondigitalocean.app",
]

# Django 4+: CSRF_TRUSTED_ORIGINS must include scheme
CSRF_TRUSTED_ORIGINS = [
    "https://budgetdrivingschoolreading.com",
    "https://www.budgetdrivingschoolreading.com",
    "https://budgetdrivingschool-cnyxh.ondigitalocean.app",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]



# APPLICATIONS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "main",
    "appointment",
    "django_q",
]

# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # <-- Added here
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "drivingSchoolParent.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # optional, if you use project-wide templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "drivingSchoolParent.wsgi.application"

# DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# PASSWORDS
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/London"
USE_TZ = True
USE_I18N = True


# STATIC FILES
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]  # for app-level static assets

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# MEDIA (for uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# DEFAULTS
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Appointment settings
APPOINTMENT_BASE_TEMPLATE = "base_templates/base.html"
APPOINTMENT_ADMIN_BASE_TEMPLATE = "base_templates/base.html"
APPOINTMENT_WEBSITE_NAME = "Chocolates"
APPOINTMENT_PAYMENT_URL = None
APPOINTMENT_THANK_YOU_URL = None
APPOINTMENT_BUFFER_TIME = 0
APPOINTMENT_SLOT_DURATION = 30
APPOINTMENT_LEAD_TIME = (9, 0)
APPOINTMENT_FINISH_TIME = (16, 30)

# AUTH
AUTH_USER_MODEL = "auth.User"

# Django Q config
Q_CLUSTER = {
    "name": "DjangORM",
    "workers": 4,
    "timeout": 90,
    "retry": 120,
    "queue_limit": 50,
    "bulk": 10,
    "orm": "default",
}

# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "apikey"  # literally "apikey"
EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_API_KEY")  # set this in DO/locally
DEFAULT_FROM_EMAIL = "Budget Driving School <noreply@budgetdrivingschoolreading.com>"

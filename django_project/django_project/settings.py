"""
Django settings for django_project project.

I could not make the global variables in this file prefixed with "g_"
because it would obstruct the functionality of certain components of
of this Django web application.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# import json

# with open('/etc/config.json') as config_file:
#     config = json.load(config_file)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n_=%7q&8r7fx6b$783qwwf%el-%a^122%dw&5_@gkh+6b9czg2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '198.74.49.223',
    '127.0.0.1',
    '*'
]

# Application definition
# Anytime a new application is created, include it under "INSTALLED_APPS".
INSTALLED_APPS = [
    # Here the blog application is added to the list of installed apps,
    # so that django knows to look here when it searches for each template.
    'blog.apps.BlogConfig',
    # There will be a class named "UsersConfig" inside the apps.py
    # file inside the "users" directory.
    'users.apps.UsersConfig',
    # "crispy_forms" is example of an external application, that needs to
    # be included in this list because it is utilised in the Django app.
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'weather',
    'map_app.apps.MapAppConfig',
    'Exams.apps.ExamsConfig',
    'ExamQuestions.apps.ExamQuestionsConfig',
    'ExamResults.apps.ExamResultsConfig',
    'base',
    'embed_video',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(str(BASE_DIR), 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Configure the Django project, so that it read the 'static' folder inside
# the first "django_project" directory.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    BASE_DIR / 'static',
    # BASE_DIR / 'Exam' / 'static',
]

# "MEDIA_ROOT" is the directory where the uploaded files will be saved and uploaded on
# the file system. The directory will be called 'media'.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Since "MEDIA_ROOT" is set to 'media', when an image is uploaded, a 'profile_pics' directory
# will be created inside of the '/media/' directory and the image will be put in there.
MEDIA_URL = '/media/'  # This will be used to access the image in a browser.

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
# 'login' was the same name given to the URL pattern for the login route.
# If a user attempts to access '/profile' without signing in, they
# will be re-directed to the url pattern for the login route.
LOGIN_URL = 'login'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# If a user uploads a file that has the same name as an existing file,
# do not overwrite the existing file.
AWS_S3_FILE_OVERWRITE = False

# Set to 'None' so the file will be private and to avoid issues.
AWS_DEFAULT_ACL = None

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

X_FRAME_OPTIONS = 'ALLOWALL'

CSRF_USE_SESSIONS = True

# 121

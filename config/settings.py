import os
from pathlib import Path
from datetime import timedelta



# Base Directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key for production (make sure to keep this secret in real production environments)
SECRET_KEY = 'ZOgcTLTzEZE59SAd_0zJAURmfLUkLqLp8sESDFFeK6zA0lBybGWnxKEeJcPN64gpjKk'  # Replace with your actual secret key

# Debug mode
DEBUG = os.environ.get('DEBUG', 'True') == 'True'  # Set to True for local development, False for production

# Allowed Hosts
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Applications Installed
INSTALLED_APPS = [
    # Custom apps
    'apps.custom_user.apps.CustomUserConfig',
    # Other custom apps
    'apps.room.apps.RoomConfig',
    'apps.category.apps.CategoryConfig',
    'apps.comment.apps.CommentConfig',
    'apps.bookmark.apps.BookmarkConfig',
    'apps.city.apps.CityConfig',
    
    # Django defaults
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
]

AUTH_USER_MODEL = 'custom_user.User'

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]



# Allow all origins (for development purposes)
CORS_ALLOW_ALL_ORIGINS = True

# Allow specific origins (for production)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React App
]

# Allow credentials if needed
CORS_ALLOW_CREDENTIALS = True

# Allow specific headers and methods
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    "accept",
    "origin",
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# JWT Settings


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kakdepatil333@gmail.com'
EMAIL_HOST_PASSWORD = 'santosh.patil@333'





# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Directories where you want to store your templates
            BASE_DIR / 'templates',  # or any other path where templates are located
        ],
        'APP_DIRS': True,  # This allows Django to automatically look for templates in each app's 'templates' directory
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


# Root URL Configuration
ROOT_URLCONF = 'config.urls'

# WSGI application
WSGI_APPLICATION = 'config.wsgi.application'

# Database Configuration (Replace with your actual database connection string)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'roomapp'),  # Replace with actual DB name
        'USER': os.environ.get('DB_USER', 'postgres'),  # Replace with DB user
        'PASSWORD': os.environ.get('DB_PASSWORD', 'baimanus2024'),  # Replace with DB password
        'HOST': os.environ.get('DB_HOST', 'localhost'),  # Replace with DB host if needed
        'PORT': os.environ.get('DB_PORT', '5432'),  # Replace with DB port if needed
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files settings
MEDIA_URL = '/media/'

# Media files storage

MEDIA_ROOT = BASE_DIR /'media'


# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery Configuration (optional, if you are using Celery)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'



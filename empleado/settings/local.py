from .base import *
import os
import environ



env = environ.Env()
# reading .env file
environ.Env.read_env()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR.child('db.sqlite3'),
#     }
# }



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = os.getenv('AWS_QUERYSTRING_AUTH')





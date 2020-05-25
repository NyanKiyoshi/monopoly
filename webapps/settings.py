"""
Django settings for webapps project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from configparser import ConfigParser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7d#m%i!ed32ei5v(i2da*#w9od=_m9u&*6&-6jla1fqdb=66_('

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ['localhost',
#                  '127.0.0.1',
#                  'ec2-18-188-96-54.us-east-2.compute.amazonaws.com',
#                  '18.188.96.54']

ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1',
                 '192.0.2.143']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'monopoly'
]

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "monopoly.routing.channel_routing",
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webapps.urls'

LOGIN_URL = '/monopoly/login'
LOGIN_REDIRECT_URL = '/monopoly/'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'webapps.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django', 'USER': 'root', 'PASSWORD': 'team16',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# config = ConfigParser()
# config.read(os.path.join(BASE_DIR, 'config.ini'))

# If you use TLS the EMAIL_PORT value is 587 but if you use SSL the port value will have to be 465
# TODO - use config.ini file later once we verify email sending is working

# EMAIL_HOST = config.get('Email', 'Host')
# EMAIL_PORT = int(config.get('Email', 'Port'))
# EMAIL_HOST_USER = config.get('Email', 'User')
# EMAIL_HOST_PASSWORD = config.get('Email', 'Password')
# EMAIL_USE_SSL = True

# TODO - allow less secure app
# see https://myaccount.google.com/u/1/security?pageId=none&nlr=1
# https://medium.com/@_christopher/how-to-send-emails-with-python-django-through-google-smtp-server-for-free-22ea6ea0fb8e

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "noreply.mymonopoly@gmail.com"
EMAIL_HOST_PASSWORD = "E!Yyek=yH{N9V3AFc3?5jt(UckF>K`\"Q"  #escaped char
# EMAIL_HOST_PASSWORD = r'E!Yyek=yH{N9V3AFc3?5jt(UckF>K`"Q'  #escaped char


print('Email host:port = {host}:{port}, user={user}'.format(
    host=EMAIL_HOST, port=EMAIL_PORT, user=EMAIL_HOST_USER))

MEDIA_ROOT = os.path.join(BASE_DIR, 'userdata')
MEDIA_URL = '/userdata/'

# Test email generation from shell
# 1. Run interactive mode: 
#   python manage.py shell
# 2. Import the EmailMessage module:
#   from django.core.mail import EmailMessage
# 3. Send test email
#   email = EmailMessage('TestMyMonopoly', 'This is a test from django app interactive shell', to=['ocanasherrera@gmail.com'])
#   email.send()


"""
sample test output (05/17/20) : success

    (forked_monopoly) Davids-MBP:monopoly david$ python manage.py shell
    Email host:port = smtp.gmail.com:587, user=noreply.mymonopoly@gmail.com
    Python 2.7.17 (default, May  8 2020, 20:08:12)
    [GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.32.59)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from django.core.mail import EmailMessage
    >>> email = EmailMessage('TestMyMonopoly', 'This is a test from django app interactive shell', to=['ocanasherrera@gmail.com'])
    >>> email.send()
    1

"""



# DEPLOYMENT

# Maybe through digitalocean
# https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04

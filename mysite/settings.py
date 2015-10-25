#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from djangae.settings_base import *  # Set up some AppEngine specific stuff
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

from .boot import get_app_config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_app_config().secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'djangae',  # Djangae needs to come before django apps in django 1.7 and above
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'djangosecure',
    # 'csp',
    # 'cspreports',
    'djangae.contrib.gauth.datastore',
    'djangae.contrib.security',
    'blog',
    # 'djangae.contrib.uniquetool',
)

MIDDLEWARE_CLASSES = (
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'djangae.contrib.gauth.middleware.AuthenticationMiddleware',
    # 'mysite.auto_auth.Middleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'csp.middleware.CSPMiddleware',
    # 'session_csrf.CsrfMiddleware',
    # 'djangosecure.middleware.SecurityMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    # "session_csrf.context_processor"
)

SECURE_CHECKS = [
    "djangosecure.check.sessions.check_session_cookie_secure",
    "djangosecure.check.sessions.check_session_cookie_httponly",
    "djangosecure.check.djangosecure.check_security_middleware",
    "djangosecure.check.djangosecure.check_sts",
    "djangosecure.check.djangosecure.check_frame_deny",
    "djangosecure.check.djangosecure.check_ssl_redirect",
    "mysite.checks.check_session_csrf_enabled",
    "mysite.checks.check_csp_is_not_report_only"
]

CSP_REPORT_URI = reverse_lazy('report_csp')
CSP_REPORTS_LOG = True
CSP_REPORTS_LOG_LEVEL = 'warning'
CSP_REPORTS_SAVE = True
CSP_REPORTS_EMAIL_ADMINS = False

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")

# sensible default CPS settings, feel free to modify them
CSP_DEFAULT_SRC = ("'self'", "*.gstatic.com")
CSP_STYLE_SRC = ("'self'", "fonts.googleapis.com", "*.gstatic.com")
CSP_FONT_SRC = ("'self'", "themes.googleusercontent.com", "*.gstatic.com")
CSP_FRAME_SRC = ("'self'", "www.google.com", "www.youtube.com", "accounts.google.com", "apis.google.com", "plus.google.com")
CSP_SCRIPT_SRC = ("'self'", "*.googleanalytics.com", "*.google-analytics.com", "ajax.googleapis.com")
CSP_IMG_SRC = ("'self'", "data:", "s.ytimg.com", "*.googleusercontent.com", "*.gstatic.com")
CSP_CONNECT_SRC = ("'self'", "plus.google.com", "www.google-analytics.com")

from djangae.contrib.gauth.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'djangae.db.backends.appengine'
    }
}

BLOG_TITLE = u"LIANTIAN'S LOG"
BLOG_DESCRIPTION = [
    "\xe8\x99\x9b\xe5\x81\xbd\xe8\xa1\x97\xe8\xa7\x92\xef\xbc\x8c\xe6\x9c\x89\xe4\xbd\xa0\xe5\xbe\xae\xe7\xac\x91\xe2\x80\xa6",
    "\xe6\xb0\xb4\xe5\xba\x95\xe6\xbc\xb8\xe4\xb9\xbe\xef\xbc\x8c\xe6\x9c\x88\xe6\xbc\xb8\xe6\xbb\xbf\xe2\x80\xa6",
    "\xe9\xab\x98\xe7\x89\x86\xe4\xb9\x8b\xe5\x85\xa7\xef\xbc\x8c\xe5\xa4\xb1\xe8\x80\x8c\xe8\xa4\x87\xe5\xbe\x97\xe2\x80\xa6",
    "\xe6\xb7\xba\xe7\x9c\xa0\xe4\xb8\x80\xe5\xa4\xa2\xef\xbc\x8c\xe4\xb8\x8d\xe6\x9b\xbe\xe9\x86\x89\xe9\x85\x92\xe2\x80\xa6",
    "\xe4\xba\x94\xe6\x9c\x88\xe9\x9b\xa8\xe4\xb8\xad\xef\xbc\x8c\xe6\xa2\x94\xe5\xad\x90\xe8\x8a\xb1\xe9\xa6\x99\xe2\x80\xa6",
    "\xe8\x83\x8c\xe5\x8f\x9b\xe7\x9a\x84\xe8\xa8\x98\xe6\x86\xb6\xef\xbc\x8c\xe6\x98\xaf\xe7\x90\xa5\xe7\x8f\x80\xe8\x89\xb2\xe7\x9a\x84\xe5\xbe\xae\xe7\xac\x91\xe2\x80\xa6",
]

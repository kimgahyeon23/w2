"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 현재 디렉토리를 패키지 찾는데 포함시키겠다.
# 파이썬이 패키지 찾는순서 workingderectory->

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kuil5hbs9o=gceu7ym^ku%5n&stdoio75e^(_%lv&earfn%vx_'
# 나중에 보안관련 사용한다함
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.0.15','127.0.0.1','localhost']
# 웹서버의 호스트트
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',#관리
    'django.contrib.auth',#로그인 관련
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',

    'taggit.apps.TaggitAppConfig', ##
    'taggit_templatetags2', ##

    'widget_tweaks', #로그인 관련 form여러가지있음

    'bookmark.apps.BookmarkConfig',
    'blog.apps.BlogConfig',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',#토큰 넣어서 보안활동하는것
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates') # 둘을 결합시켜라
        ],#BASE_DIR = 프로젝트 디렉토리 장고가 제일먼저 찾는곳
        'APP_DIRS': True, # 그다움 없으면 각 app의 templates들을 뒤짐
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_ex_db', # 데이터베이스 명
        'HOST': 'localhost', # 서버 IP
        'PORT': '3306', # 포트번호
        'USER': 'webuser', # 사용자 ID
        'PASSWORD': '1234' # 비밀번호
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'
USE_TZ = False

USE_I18N = True

USE_L10N = True

#로그인 관련 URL 디폴트값
#LOGIN_URL = 'account/login/' #로그인 페이지 URL
#LOGIN_REDIRECT_URL '/accounts/profile' #로그인 성공시 리다이텔그할 URL
#LOGOUT_REDIRECT_RUL '/' #로그 아웃시 리다이렉트할 URL

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TAGGIT_CASE_INSENSITIVE = True ## 대소문자 구분 여부 (안하겠다)
TAGGIT_LIMIT = 50 #(한포스트당 태그 제한)
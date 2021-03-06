"""
Django settings for class427s project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jtwv*_t#hswn32%*#6br+2p#9wrys@k8vy=r&++hv!5^)(b^(i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stu',
    'uauth',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'utils.UserAuthMiddleware.AuthMiddleware',
    'utils.VisitTimesMiddleware.VisitTimes',

]

ROOT_URLCONF = 'class427s.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'class427s.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'class427s',
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': '3306',
        'HOST': 'localhost'
    }
}


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

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


# 配置静态文件
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# 配置上传文件路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 在没有登录时要跳转的地址
LOGIN_URL = '/u/dj_login/'


# 自动创建日志的路径
LOG_PATH = os.path.join(BASE_DIR, 'log')
# 如果地址不存在，则自动创建log文件夹
if not os.path.isdir(LOG_PATH):
    os.mkdir(LOG_PATH)

# 日志信息的相关设置
LOGGING = {
    # version 只能为 1
    'version': 1,
    # True 表示禁用loggers
    'disable_existing_loggers': False,
    # 格式化
    'formatters': {
        'default': {
            'format': '%(levelname)s %(pathname)s %(funcName)s %(module)s %(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(funcName)s %(asctime)s %(message)s'
        }
    },
    # 处理
    'handlers': {
        'stu_handlers': {
            'level': 'DEBUG',
            # 日志文件指定为 5m，超过5m重新备份，然后写入新的日志文件
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 5 * 1024 * 1024,
            # 存放日志文件地址
            'filename': '%s/log.txt' % LOG_PATH,
            'formatter': 'default'
        },

        'u_handlers': {
            'level': 'DEBUG',
            # 日志文件指定为 5m，超过5m重新备份，然后写入新的日志文件
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 5 * 1024 * 1024,
            # 存放日志文件地址
            'filename': '%s/u_log.txt' % LOG_PATH,
            'formatter': 'simple'
        },
    },
    # 需要写入日志的内容
    'loggers': {
        'stu': {
            'handlers': ['stu_handlers'],
            'level': 'INFO',
        },
        'auth': {
            'handlers': ['u_handlers'],
            'level': 'INFO'
        }
    },
    # 过滤部分内容
    'filters': {},
}

# 配置restful api的返回结果
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'utils.RenderResponse.CustomJsonRenderer',
    )
}
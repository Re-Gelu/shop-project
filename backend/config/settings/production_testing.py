from .production import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME":  BASE_DIR / "db.sqlite3",
        "USER": "user",
        "PASSWORD": "SQL_PASSWORD",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': REDIS_URL,
    },
}

CACHING_TIME = 1

EXTRA_SETTINGS_CACHE_NAME = 'default'

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

CELERY_TASK_ALWAYS_EAGER = True

CELERY_TASK_EAGER_PROPAGATES = True

from .development import *

EXTRA_SETTINGS_CACHE_NAME = 'default'

CACHES = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}

CACHING_TIME = 1

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

CELERY_BROKER_URL = 'memory://'

RESULT_BACKEND = 'db+sqlite:///results.sqlite'

CELERY_TASK_ALWAYS_EAGER = True

CELERY_TASK_EAGER_PROPAGATES = True

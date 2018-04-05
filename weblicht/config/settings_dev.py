"""Development configuration"""
from .settings import *

DEBUG = True

ALLOWED_HOSTS += ['localhost', '127.0.0.1']
INTERNAL_IPS = ['127.0.0.1', 'localhost']

STATIC_ROOT = "C:/Users/distorti/projects/ut/webservices/static/"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)-8s [%(name)s:%(lineno)s] %(message)s',
        },
    },
    'loggers': {
        'mysite': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

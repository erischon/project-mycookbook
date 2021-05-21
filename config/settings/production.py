from . import *

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = os.getenv('167.71.39.195')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'), 
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'), 
        'PORT': '',
    }
}


sentry_sdk.init(
    dsn="https://17e5b37213464b05a42d9f2171116080@o570822.ingest.sentry.io/5741629",
    integrations=[DjangoIntegration()],

    traces_sample_rate=1.0,

    send_default_pii=True
)
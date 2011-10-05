from settings import *

INSTALLED_APPS += (
    'basic',
    'namespaced',
)

ROOT_URLCONF = 'namespaced.api.urls'

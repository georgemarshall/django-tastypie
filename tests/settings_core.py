from settings import *

INSTALLED_APPS += (
    'core',
)

from tastypie.authentication import oauth2, oauth_provider
if oauth2 and oauth_provider:
    INSTALLED_APPS += (
        'oauth_provider',
    )

ROOT_URLCONF = 'core.tests.api_urls'
MEDIA_URL = 'http://localhost:8080/media/'




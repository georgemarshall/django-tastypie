from django.conf import settings


def trailing_slash():
    if getattr(settings, 'TASTYPIE_ALLOW_MISSING_SLASH', False):
        return r'/?'
    return r'/'

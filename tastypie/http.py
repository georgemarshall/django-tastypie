"""
The various HTTP responses for use in returning proper HTTP codes.
"""
from django.http import (
    HttpResponse, HttpResponseNotModified, HttpResponseBadRequest,
    HttpResponseNotFound, HttpResponseForbidden, HttpResponseNotAllowed,
    HttpResponseGone, HttpResponseServerError
)


class HttpResponseCreated(HttpResponse):
    status_code = 201
    
    def __init__(self, *args, **kwargs):
        location = ''

        if 'location' in kwargs:
            location = kwargs['location']
            del(kwargs['location'])
        
        super(HttpCreated, self).__init__(*args, **kwargs)
        self['Location'] = location


class HttpResponseAccepted(HttpResponse):
    status_code = 202


class HttpResponseNoContent(HttpResponse):
    status_code = 204


class HttpResponseMultipleChoices(HttpResponse):
    status_code = 300


class HttpResponseSeeOther(HttpResponse):
    status_code = 303


class HttpResponseUnauthorized(HttpResponse):
    status_code = 401


class HttpResponseConflict(HttpResponse):
    status_code = 409


class HttpResponseNotImplemented(HttpResponse):
    status_code = 501


HttpCreated = HttpResponseCreated
HttpAccepted = HttpResponseAccepted
HttpNoContent = HttpResponseNoContent
HttpMultipleChoices = HttpResponseMultipleChoices
HttpSeeOther = HttpResponseSeeOther
HttpNotModified = HttpResponseNotModified
HttpBadRequest = HttpResponseBadRequest
HttpUnauthorized = HttpResponseUnauthorized
HttpForbidden = HttpResponseForbidden
HttpNotFound = HttpResponseNotFound
HttpMethodNotAllowed = HttpResponseNotAllowed
HttpConflict = HttpResponseConflict
HttpGone = HttpResponseGone
HttpApplicationError = HttpResponseServerError
HttpNotImplemented = HttpResponseNotImplemented

from __future__ import absolute_import

from tastypie.api import Api

from .resources import ProductResource


api = Api(api_name='v1')
api.register(ProductResource(), canonical=True)

urlpatterns = api.urls

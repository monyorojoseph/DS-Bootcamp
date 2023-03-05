from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter(trailing_slash=False)
router.register('endpoints', EndpointViewset, basename='endpoints')
router.register('mlalgorithms', MLAlgorithmViewset, basename='mlalgorithms')
router.register('mlalgorithmstatus', MLAlgorithmStatusViewset, basename='mlalgorithmstatus')
router.register('mlrequests', MLRequestViewset, basename='mlrequests')

urlpatterns = [
    path('api/v1/', include(router.urls))
]

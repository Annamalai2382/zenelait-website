from django.urls import path, include
from rest_framework.routers import DefaultRouter
from services.api import ServiceViewSet
from blog.api import PostViewSet
from careers.api import JobListingViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='api-service')
router.register(r'posts', PostViewSet, basename='api-post')
router.register(r'jobs', JobListingViewSet, basename='api-jobs')

urlpatterns = [
    path('', include(router.urls)),
]

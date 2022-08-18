from django.urls import path, include
from .views import ImageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ImageViewSet)

urlpatterns = [
     path('',include(router.urls))
     ]
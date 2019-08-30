from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClimaViewSet


router = DefaultRouter()
router.register('clima', ClimaViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
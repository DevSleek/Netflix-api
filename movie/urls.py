from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActorViewSet, MovieViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

urlpatterns = [
   path('', include(router.urls))
]
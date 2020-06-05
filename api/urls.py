from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers

from api.views import NoteViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('notes', NoteViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

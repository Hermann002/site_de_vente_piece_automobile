from django.conf.urls import url
from django.urls import path, include
from manage_user.views import *
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
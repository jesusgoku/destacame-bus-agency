from django.conf.urls import url, include
from rest_framework import routers

from . import views
from . import views_api

router = routers.DefaultRouter()
router.register(r'buses', views_api.BusVieSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

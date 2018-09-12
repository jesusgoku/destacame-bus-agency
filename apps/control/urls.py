from django.conf.urls import url, include
from rest_framework import routers

from . import views
from . import views_api

router = routers.DefaultRouter()
router.register(r'buses', views_api.BusViewSet)
router.register(r'drivers', views_api.DriverViewSet)
router.register(r'routes', views_api.RouteViewSet)
router.register(r'itineraries', views_api.ItineraryViewSet)
router.register(r'passengers', views_api.PassengerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

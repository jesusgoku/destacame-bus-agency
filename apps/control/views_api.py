from rest_framework import viewsets

from . import models
from . import serializers


class BusViewSet(viewsets.ModelViewSet):
    queryset = models.Bus.objects.all()
    serializer_class = serializers.BusSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer


class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = models.Itinerary.objects.all()
    serializer_class = serializers.ItinerarySerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = models.Passenger.objects.all()
    serializer_class = serializers.PassengerSerializer

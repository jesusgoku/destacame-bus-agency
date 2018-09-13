from rest_framework import viewsets

from . import models
from . import serializers


class BusViewSet(viewsets.ModelViewSet):
    queryset = models.Bus.objects.all()
    serializer_class = serializers.BusSerializer
    filter_fields = ('id', 'capacity', 'identifier',)
    search_fields = ('identifier',)


class DriverViewSet(viewsets.ModelViewSet):
    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    filter_fields = ('id', 'name', 'phone', 'email',)
    search_fields = ('name', 'phone', 'email',)


class RouteViewSet(viewsets.ModelViewSet):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
    filter_fields = ('id', 'name', 'duration',)
    search_fields = ('name',)


class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = models.Itinerary.objects.all()
    serializer_class = serializers.ItinerarySerializer
    filter_fields = ('id', 'start_time', 'end_time',)
    search_fields = ('route__name', 'driver__name', 'bus__identifier',)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = models.Passenger.objects.all()
    serializer_class = serializers.PassengerSerializer
    filter_fields = ('id', 'position', 'name', 'phone', 'emergency_name', 'emergency_phone')
    search_fields = ('name', 'phone', 'emergency_name', 'emergency_phone', )

from rest_framework import viewsets

from . import models
from . import serializers
from . import filters


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
    # filterset_fields = ('id', 'start_time', 'end_time',)
    filter_class = filters.ItineraryFilter
    search_fields = ('route__name', 'driver__name', 'bus__identifier',)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = models.Passenger.objects.all()
    serializer_class = serializers.PassengerSerializer
    filter_fields = ('id', 'position', 'name', 'phone', 'emergency_name', 'emergency_phone', 'itinerary',)
    search_fields = ('name', 'phone', 'emergency_name', 'emergency_phone',)

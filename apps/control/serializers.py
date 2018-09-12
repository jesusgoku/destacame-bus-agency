from rest_framework import serializers

from . import models


class BusSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Bus
        fields = ('id', 'capacity', 'identifier',)


class DriverSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Driver
        fields = ('id', 'name', 'phone', 'email',)

class RouteSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Route
        fields = ('id', 'name', 'duration',)


class ItinerarySerializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Itinerary
        fields = ('id', 'route', 'bus', 'driver', 'start_time', 'end_time', 'capacity', 'capacity_sold', 'duration')


class PassengerSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Passanger
        fields = ('id', 'itinerary', 'position', 'name', 'phone', 'emergency_name', 'emergency_phone',)

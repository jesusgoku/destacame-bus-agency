from rest_framework import serializers
from django.core.exceptions import ValidationError

from . import models


class ModelCleanValidateSerializer(serializers.ModelSerializer):
    def validate(self, data):
        instance = self.Meta.model(**data)

        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.args[0])

        return data


class BusSerializer(ModelCleanValidateSerializer):
    class Meta(object):
        model = models.Bus
        fields = ('id', 'capacity', 'identifier',)


class DriverSerializer(ModelCleanValidateSerializer):
    class Meta(object):
        model = models.Driver
        fields = ('id', 'name', 'phone', 'email',)

class RouteSerializer(ModelCleanValidateSerializer):
    class Meta(object):
        model = models.Route
        fields = ('id', 'name', 'duration',)


class ItinerarySerializer(ModelCleanValidateSerializer):
    class Meta(object):
        model = models.Itinerary
        fields = ('id', 'route', 'bus', 'driver', 'start_time', 'end_time', 'capacity', 'capacity_sold', 'duration')


class PassengerSerializer(ModelCleanValidateSerializer):
    class Meta(object):
        model = models.Passanger
        fields = ('id', 'itinerary', 'position', 'name', 'phone', 'emergency_name', 'emergency_phone',)

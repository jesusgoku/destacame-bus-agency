from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from datetime import datetime

from . import models
from . import serializers
from . import filters


class BusViewSet(viewsets.ModelViewSet):
    queryset = models.Bus.objects.all()
    serializer_class = serializers.BusSerializer
    filter_fields = ('id', 'capacity', 'identifier',)
    search_fields = ('identifier',)

    @action(detail=False)
    def available(self, request):
        serializer = serializers.AvailableOnSerializer(data=request.query_params)

        if not serializer.is_valid():
            raise ParseError('Query param "start_time" or "end_time" not present or is malformed')

        start_time = serializer.validated_data['start_time']
        end_time = serializer.validated_data['end_time']

        buses = models.Bus.objects.availables_on(start_time, end_time)
        page = self.paginate_queryset(buses)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(buses, many=True)
        return Response(serializer.data)


class DriverViewSet(viewsets.ModelViewSet):
    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    filter_fields = ('id', 'name', 'phone', 'email',)
    search_fields = ('name', 'phone', 'email',)

    @action(detail=False)
    def available(self, request):
        serializer = serializers.AvailableOnSerializer(data=request.query_params)

        if not serializer.is_valid():
            raise ParseError('Query param "start_time" or "end_time" not present or is malformed')

        start_time = serializer.validated_data['start_time']
        end_time = serializer.validated_data['end_time']

        buses = models.Driver.objects.availables_on(start_time, end_time)
        page = self.paginate_queryset(buses)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(buses, many=True)
        return Response(serializer.data)


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

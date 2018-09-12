# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models


@admin.register(models.Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('id', 'identifier', 'capacity')


@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')


@admin.register(models.Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration')


@admin.register(models.Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'route', 'bus', 'driver', 'start_time', 'end_time', 'capacity', 'capacity_sold', 'duration')


@admin.register(models.Passanger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id', 'itinerary', 'position', 'name', 'phone', 'emergency_name', 'emergency_phone')

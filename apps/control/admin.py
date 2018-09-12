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
    list_display = ('id', 'name', 'duration', 'average_passengers')


class PassengerInline(admin.TabularInline):
    model = models.Passenger

@admin.register(models.Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    # inlines = (PassengerInline,)
    list_display = ('id', 'route', 'bus', 'driver', 'start_time', 'end_time', 'capacity', 'capacity_sold', 'duration')
    list_filter = ('route', 'bus', 'driver', 'start_time', 'bus__capacity')


@admin.register(models.Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id', 'itinerary', 'position', 'name', 'phone', 'emergency_name', 'emergency_phone')
    list_filter = ('itinerary',)

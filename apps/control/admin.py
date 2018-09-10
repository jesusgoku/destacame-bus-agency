# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models

# admin.site.register(models.Bus)
admin.site.register(models.Driver)
admin.site.register(models.Route)
admin.site.register(models.Itinerary)
admin.site.register(models.Passanger)

@admin.register(models.Bus)
class BusAdmin(admin.ModelAdmin):
    pass

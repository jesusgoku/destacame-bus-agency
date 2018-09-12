# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.dateformat import format
from django.utils.translation import gettext_lazy as _

@python_2_unicode_compatible
class Bus(models.Model):
    capacity = models.IntegerField(_('Capacity'), default=10)

    identifier = models.CharField(_('Identifier'), max_length=255, unique=True)

    def __str__(self):
        return self.identifier

    class Meta(object):
        verbose_name = _('Bus')
        verbose_name_plural = _('Buses')


@python_2_unicode_compatible
class Driver(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    phone = models.CharField(_('Phone'), max_length=50, null=True, blank=True)
    email = models.CharField(_('Email'), max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = _('Driver')
        verbose_name_plural = _('Drivers')


@python_2_unicode_compatible
class Route(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    duration = models.FloatField(_('Duration'), null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = _('Route')
        verbose_name_plural = _('Routes')


@python_2_unicode_compatible
class Itinerary(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name=_('Route'))
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, verbose_name=_('Bus'))
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name=_('Driver'))

    start_time = models.DateTimeField(_('Start time'))
    end_time = models.DateTimeField(_('End time'))

    def __str__(self):
        return "{} / {} ({} / {})".format(
            self.route,
            format(self.start_time, 'l, d b, H:i'),
            self.bus,
            self.driver)

    class Meta(object):
        verbose_name = _('Itinerary')
        verbose_name_plural = _('Itineraries')


@python_2_unicode_compatible
class Passanger(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, verbose_name=_('Itinerary'))

    position = models.IntegerField(_('Position'))

    name = models.CharField(_('Name'), max_length=255, null=True, blank=True)
    phone = models.CharField(_('Phone'), max_length=50, null=True, blank=True)

    emergency_name = models.CharField(_('Emergency name'), max_length=255, null=True, blank=True)
    emergency_phone = models.CharField(_('Emergency phone'), max_length=50, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.itinerary, self.position)

    class Meta(object):
        verbose_name = _('Passenger')
        verbose_name_plural = _('Passengers')

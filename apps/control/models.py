# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils.encoding import python_2_unicode_compatible
from django.utils.dateformat import format
from django.utils.translation import gettext_lazy as _

@python_2_unicode_compatible
class Bus(models.Model):
    capacity = models.IntegerField(_('Capacity'), default=10)

    identifier = models.CharField(_('Identifier'), max_length=255, unique=True)

    def available_on(self, start_time, end_time):
        return self.itinerary_set.filter(start_time__lte=end_time, end_time__gte=start_time).count() == 0

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

    def available_on(self, start_time, end_time):
        return self.itinerary_set.filter(start_time__lte=end_time, end_time__gte=start_time).count() == 0

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = _('Driver')
        verbose_name_plural = _('Drivers')


@python_2_unicode_compatible
class Route(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    duration = models.FloatField(_('Duration'), null=True, blank=True)

    @property
    def average_passengers(self):
        itineraries = float(self.itinerary_set.count())
        passengers = self.itinerary_set.aggregate(models.Count('passanger')).values()[0]
        return passengers / itineraries if itineraries != 0 else float(0)

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

    @property
    def capacity(self):
        return self.bus.capacity

    capacity.fget.short_description = _('Capacity')

    @property
    def capacity_sold(self):
        return self.passanger_set.count()

    @property
    def duration(self):
        return (self.end_time - self.start_time).seconds / float(3600)

    capacity_sold.fget.short_description = _('Capacity sold')

    def position_available(self, position):
        return self.passanger_set.filter(position=position).count() == 0

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError(_('End time is before start time'))

        if self.duration < self.route.duration:
            raise ValidationError(_('Duration of itinerary is less than of route duration'))

        if not self.bus.available_on(self.start_time, self.end_time):
            raise ValidationError(_('Bus not available'))

        if not self.driver.available_on(self.start_time, self.end_time):
            raise ValidationError(_('Driver not available'))

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

    position = models.IntegerField(_('Position'), validators=[MinValueValidator(1)])

    name = models.CharField(_('Name'), max_length=255, null=True, blank=True)
    phone = models.CharField(_('Phone'), max_length=50, null=True, blank=True)

    emergency_name = models.CharField(_('Emergency name'), max_length=255, null=True, blank=True)
    emergency_phone = models.CharField(_('Emergency phone'), max_length=50, null=True, blank=True)

    def clean(self):
        if self.position > self.itinerary.capacity:
            raise ValidationError(_('Position out of range'))

        if self.itinerary.capacity_sold >= self.itinerary.capacity:
            raise ValidationError(_('Itinerary capacity completed'))

        if not self.itinerary.position_available(self.position):
            raise ValidationError(_('Position not available'))

    def __str__(self):
        return '{} {}'.format(self.itinerary, self.position)

    class Meta(object):
        verbose_name = _('Passenger')
        verbose_name_plural = _('Passengers')

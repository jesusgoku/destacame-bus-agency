from django.db import models


class BusManager(models.Manager):
    def availables_on(self, start_time, end_time):
        overlaped = (self
            .get_queryset()
            .filter(itinerary__start_time__lte=end_time, itinerary__end_time__gte=start_time)
            .values_list('id', flat=True))

        return (self
            .get_queryset()
            .exclude(id__in=overlaped))


class DriverManager(models.Manager):
    def availables_on(self, start_time, end_time):
        overlaped = (self
            .get_queryset()
            .filter(itinerary__start_time__lte=end_time, itinerary__end_time__gte=start_time)
            .values_list('id', flat=True))

        return (self
            .get_queryset()
            .exclude(id__in=overlaped))

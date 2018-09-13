from django_filters import rest_framework as filters
from django.db.models import Count

from . import models


class ItineraryFilter(filters.FilterSet):
    capacity_sold__gt = filters.NumberFilter(field_name='passenger__count__gt', lookup_expr='gt', method='capacity_sold_filter')
    capacity_sold__gte = filters.NumberFilter(field_name='passenger__count__gte', lookup_expr='gte', method='capacity_sold_filter')
    capacity_sold__lt = filters.NumberFilter(field_name='passenger__count__lt', lookup_expr='lt', method='capacity_sold_filter')
    capacity_sold__lte = filters.NumberFilter(field_name='passenger__count__lte', lookup_expr='lte', method='capacity_sold_filter')

    def capacity_sold_filter(self, queryset, name, value):
        return queryset.annotate(Count('passenger')).filter(**{ name: value })

    class Meta(object):
        model = models.Itinerary
        fields = {
            'route__id': ['exact',],
            'route__name': ['exact', 'iexact', 'contains', 'icontains', 'startswith', 'istartswith', 'endswith', 'iendswith',],
            'start_time': ['exact', 'gt', 'gte', 'lt', 'lte', 'day', 'month', 'range',],
            'end_time': ['exact', 'gt', 'gte', 'lt', 'lte', 'day', 'month', 'range',],
            'bus__capacity': ['exact', 'gt', 'gte', 'lt', 'lte',],
        }

from rest_framework import serializers

from . import models

class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = models.Bus
        fields = ('id', 'capacity', 'idetifier',)

from rest_framework import viewsets

from . import models
from . import serializers

class BusVieSet(viewsets.ModelViewSet):
    queryset = models.Bus.objects.all()
    serializer_class = serializers.BusSerializer

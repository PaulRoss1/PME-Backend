from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'event_type',
            'name',
            'get_absolute_url',
            'venue',
            'address',
            'date',
            'lat_long',
            'image'
        )




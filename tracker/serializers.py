from rest_framework import serializers

from tracker.models import Track, Record


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'name', 'unit', 'description']


class RecordSerializer(serializers.ModelSerializer):
    track = TrackSerializer()
    date = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = Record
        fields = ['id', 'value', 'date', 'track']

from rest_framework import serializers


class TrackSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    unit = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=300)


class RecordSerializer(serializers.Serializer):
    value = serializers.FloatField(default=0.0)
    date = serializers.DateTimeField(format='%Y-%m-%d')
    track = TrackSerializer()

from rest_framework import serializers


class TrackSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    unit = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=300)
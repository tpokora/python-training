from rest_framework import serializers

from tracker.models import Track, Record


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'name', 'unit', 'description']


class RecordSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])

    class Meta:
        model = Record
        fields = ['id', 'value', 'date', 'track']

    def to_representation(self, instance):
        self.fields['track'] = TrackSerializer(read_only=True)
        return super(RecordSerializer, self).to_representation(instance)

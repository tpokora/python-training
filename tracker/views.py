# Create your views here.
from rest_framework import generics

from tracker.models import Track, Record
from tracker.serializers import TrackSerializer, RecordSerializer


class TrackerList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

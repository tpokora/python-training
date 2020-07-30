# Create your views here.
from rest_framework import generics, viewsets

from tracker.models import Track, Record
from tracker.serializers import TrackSerializer, RecordSerializer


class TrackerList(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class RecordList(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer



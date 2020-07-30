# Create your views here.
from rest_framework import generics

from tracker.models import Track, Record
from tracker.serializers import TrackSerializer, RecordSerializer


class TrackerList(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class RecordList(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordListByTrackerName(generics.ListAPIView):
    serializer_class = RecordSerializer

    def get_queryset(self):
        name = self.kwargs['tracker_name']
        return Record.objects.filter(track__name=name)


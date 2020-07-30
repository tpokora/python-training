# Create your views here.
from rest_framework import generics

from tracker.models import Track
from tracker.serializers import TrackSerializer


class TrackerList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

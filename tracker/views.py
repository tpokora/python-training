# Create your views here.
from rest_framework import viewsets

from tracker.models import Track
from tracker.serializers import TrackSerializer


class TrackerList(viewsets.ModelViewSet):

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


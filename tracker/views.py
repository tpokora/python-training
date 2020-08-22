# Create your views here.
from django.views import generic
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from tracker.models import Track, Record
from tracker.serializers import TrackSerializer, RecordSerializer


class TrackersView(generic.ListView):
    model = Track
    template_name = 'tracker/trackers.html'
    context_object_name = 'trackers_list'

    def get_queryset(self):
        return Track.objects.all()


class TrackerDetailView(generic.DetailView):
    model = Track
    template_name = 'tracker/tracker.html'

    def get_context_data(self, **kwargs):
        context = super(TrackerDetailView, self).get_context_data(**kwargs)
        records = Record.objects.filter(track__id=context['track'].id)
        context['records'] = records
        return context


@permission_classes((AllowAny, ))
class TrackerList(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


@permission_classes((AllowAny, ))
class RecordList(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer



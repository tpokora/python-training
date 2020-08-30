# Create your views here.
from django.db import IntegrityError, transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from tracker.forms import TrackerForm
from tracker.models import Track, Record
from tracker.serializers import TrackSerializer, RecordSerializer


class TrackersView(generic.ListView):
    model = Track
    template_name = 'tracker/trackers.html'
    context_object_name = 'trackers_list'

    def get_queryset(self):
        return Track.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TrackersView, self).get_context_data()
        context['form'] = TrackerForm()
        return context


def create_tracker(request):
    tracker = Track()
    tracker.name = request.POST['name']
    tracker.unit = request.POST['unit']
    tracker.description = request.POST['description']
    try:
        with transaction.atomic():
            tracker.save()
    except IntegrityError:
        return render(request, 'tracker/trackers.html', {
            'trackers_list': Track.objects.all(),
            'form': TrackerForm(),
            'form_error': "Tracking with name '%s' already exists" % (request.POST['name']),
        })
    return HttpResponseRedirect(reverse('tracker:trackers'))


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



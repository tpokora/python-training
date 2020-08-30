# Create your views here.
from datetime import datetime

from django.db import IntegrityError, transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from tracker.forms import TrackerForm, RecordForm
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
    if request.method == 'POST':
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
    else:
        form = TrackerForm()
        return render(request, 'tracker/trackers.html', {
            'trackers_list': Track.objects.all(),
            'form': form,
        })


class TrackerDetailView(generic.DetailView):
    model = Track
    template_name = 'tracker/tracker.html'

    def get_context_data(self, **kwargs):
        context = super(TrackerDetailView, self).get_context_data(**kwargs)
        records = Record.objects.filter(track__id=context['track'].id)
        context['records'] = records
        context['record_form'] = RecordForm()
        return context


def add_record(request, tracker_id):
    track = Track.objects.get(pk=tracker_id)
    if request.method == 'POST':
        try:
            record = Record()
            record.track = track
            record.value = request.POST['value']
            record.date = datetime.strptime(request.POST['datetime'], '%Y-%m-%d %H:%M')
            record.save()
        except ValueError:
            return render(request, 'tracker/tracker.html', {
                'track': track,
                'record_form': RecordForm(),
                'form_error': "Error adding record"
            })

        return HttpResponseRedirect(reverse('tracker:tracker_detail', args=(tracker_id,)))
    else:
        records = Record.objects.filter(track__id=track.id)
        return render(request, 'tracker/tracker.html', {
            'track': track,
            'record_form': RecordForm(),
            'records': records
        })

###############
# REST APIs
###############


@permission_classes((AllowAny, ))
class TrackerList(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


@permission_classes((AllowAny, ))
class RecordList(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer



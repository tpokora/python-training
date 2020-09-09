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
    new_track_form = TrackerForm(request.POST)
    if request.method == 'POST' and new_track_form.is_valid():
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
        fields = {
            'trackers_list': Track.objects.all(),
            'form': new_track_form,
        }

        if new_track_form.errors.get('name'):
            fields['name_error'] = new_track_form.errors.get('name')[0]
        if new_track_form.errors.get('unit'):
            fields['unit_error'] = new_track_form.errors.get('unit')[0]
        if new_track_form.errors.get('description'):
            fields['description_error'] = new_track_form.errors.get('description')[0]

        return render(request, 'tracker/trackers.html', fields)


class TrackerDetailView(generic.DetailView):
    model = Track
    template_name = 'tracker/tracker.html'

    def get_context_data(self, **kwargs):
        labels = []
        data = []
        context = super(TrackerDetailView, self).get_context_data(**kwargs)
        records = Record.objects.filter(track__id=context['track'].id)

        for record in records:
            labels.append(record.date.strftime("%Y-%m-%d"))
            data.append(record.value)

        context['chart_labels'] = labels
        context['chart_data'] = data
        context['records'] = records
        context['record_form'] = RecordForm()
        return context


def add_record(request, tracker_id):
    new_record_form = RecordForm(request.POST)
    track = Track.objects.get(pk=tracker_id)
    if request.method == 'POST' and new_record_form.is_valid():
        try:
            record = Record()
            record.track = track
            record.value = request.POST['value']
            record.date = request.POST['datetime']
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
        fields = {
            'track': track,
            'record_form': new_record_form,
            'records': records,
        }
        if new_record_form.errors.get('value'):
            fields['value_error'] = new_record_form.errors['value'][0]
        if new_record_form.errors.get('datetime'):
            fields['datetime_error'] = new_record_form.errors['datetime'][0]
        return render(request, 'tracker/tracker.html', fields)

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



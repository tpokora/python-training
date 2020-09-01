import datetime

from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse

from tracker.models import Track, Record


class TrackModelTests(TestCase):

    def test_create_track(self):
        name = 'Test name'
        unit = 'Test unit'
        description = 'Test description'
        track = Track(name=name, unit=unit, description=description)

        self.assertEqual(name, track.name)
        self.assertEqual(unit, track.unit)
        self.assertEqual(description, track.description)

        expected_string = "Track{name='%s', unit='%s', description='%s'}" % (name, unit, description)
        self.assertEqual(expected_string, str(track))
        expected_repr = "<Track: Track{name='%s', unit='%s', description='%s'}>" % (name, unit, description)
        self.assertEqual(expected_repr, repr(track))


class RecordModelTests(TestCase):

    def test_create_record(self):
        track = Track(name='name', unit='unit', description='description')
        value = 11.1
        date = datetime.datetime.now()
        record = Record(track=track, value=value, date=date)

        self.assertEqual(str(track), str(record.track))
        self.assertEqual(value, record.value)
        self.assertEqual(date, record.date)

        expected_string = "Record{value='%s', date='%s'}" % (value, date.strftime('%Y-%m-%d'))
        self.assertEqual(expected_string, str(record))
        expected_repr = "<Record: Record{value='%s', date='%s'}>" % (value, date.strftime('%Y-%m-%d'))
        self.assertEqual(expected_repr, repr(record))


####################################
# Views tests
####################################

class TrackersViewTests(TestCase):

    def test_trackers(self):
        client = Client()

        response = client.get('/tracker/')
        content = str(response.content)
        trackers_header = "<h1>Trackers</h1>"
        trackers_list = '<ul id="trackers-list" class="list-group">'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(trackers_header in content, True)
        self.assertEqual(trackers_list in content, True)

    def test_create_tracker(self):
        client = Client()

        data = {'name': 'testName', 'unit': 'g', 'description': 'testDescription'}
        response = client.post(reverse('tracker:create_tracker'), data=data, follow=True)
        content = str(response.content)
        trackers_header = "<h1>Trackers</h1>"
        trackers_list = '<ul id="trackers-list" class="list-group">'

        self.assertEqual(response.status_code, 200)
        self.assertEqual(trackers_header in content, True)
        self.assertEqual(trackers_list in content, True)
        self.assertEqual(data['name'] in content, True)

    def test_create_tracker_error(self):
        client = Client()

        data = {'name': 'testName', 'unit': 'g', 'description': 'testDescription'}
        tracker = Track(name=data['name'], unit=data['unit'], description=data['description'])
        tracker.save()

        response = client.post(reverse('tracker:create_tracker'), data=data)
        content = str(response.content)
        trackers_header = "<h1>Trackers</h1>"
        trackers_list = '<ul id="trackers-list" class="list-group">'
        error_msg = "Tracking with name &#39;%s&#39; already exists" % (data['name'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(trackers_header in content, True)
        self.assertEqual(trackers_list in content, True)
        self.assertEqual(error_msg in content, True)

    def test_create_tracker_get(self):
        client = Client()

        response = client.get(reverse('tracker:create_tracker'))
        content = str(response.content)
        trackers_header = "<h1>Trackers</h1>"
        trackers_list = '<ul id="trackers-list" class="list-group">'

        self.assertEqual(response.status_code, 200)
        self.assertEqual(trackers_header in content, True)
        self.assertEqual(trackers_list in content, True)


class TrackerDetailViewTests(TestCase):

    def test_tracker_detail(self):
        tracker = Track(name='testName', unit='g', description='testDescription')
        tracker.save()

        client = Client()
        response = client.get('/tracker/%s/' % tracker.id)
        content = str(response.content)
        trackers_header = "<h2>%s</h2>" % tracker.name
        self.assertEqual(response.status_code, 200)
        self.assertEqual(trackers_header in content, True)

    def test_tracker_create_record(self):
        tracker = Track(name='testName', unit='g', description='testDescription')
        tracker.save()

        client = Client()
        data = {'value': 15, 'datetime': '2050-01-01 12:30'}
        response = client.post('/tracker/%s/create_record' % tracker.id, data, follow=True)
        content = str(response.content)
        trackers_header = "<h2>%s</h2>" % tracker.name
        self.assertEqual(response.status_code, 200)
        self.assertEqual(trackers_header in content, True)
        self.assertEqual(str(data['value']) in content, True)
        self.assertEqual(data['datetime'] in content, True)

    def test_tracker_create_record_get(self):
        tracker = Track(name='testName', unit='g', description='testDescription')
        tracker.save()

        client = Client()
        response = client.get('/tracker/%s/create_record' % tracker.id)
        content = str(response.content)
        trackers_header = "<h2>%s</h2>" % tracker.name
        self.assertEqual(response.status_code, 200)
        self.assertEqual(trackers_header in content, True)

    def test_tracker_create_record_error(self):
        tracker = Track(name='testName', unit='g', description='testDescription')
        tracker.save()

        client = Client()
        data = {'value': 15, 'datetime': '2050'}
        response = client.post('/tracker/%s/create_record' % tracker.id, data, follow=True)
        content = str(response.content)
        trackers_header = "<h2>%s</h2>" % tracker.name
        error_msg = "Enter a valid date/time."
        self.assertEqual(response.status_code, 200)
        self.assertEqual(trackers_header in content, True)
        self.assertEqual(error_msg in content, True)


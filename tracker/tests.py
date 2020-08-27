import datetime

from django.test import TestCase, Client

# Create your tests here.
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

    def test_tracker_detail(self):
        client = Client()

        response = client.get('/tracker/1/')
        content = str(response.content)
        trackers_header = "<h2>Romek</h2>"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(trackers_header in content, True)



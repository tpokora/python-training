import datetime

from django.test import TestCase

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




from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from datetime import datetime
import pytz

from temperature.models import TempReading

class TestTempReading(TestCase):
    def test_can_save_temp_reading(self):
        """
        Save a new entry to the database
        """

        value = 12.5
        d = datetime(2012, 1, 11, 2, 30, tzinfo=pytz.UTC)

        post_data = {'value': value, 'date': d}

        response = self.client.post(reverse('temperature.views.save_temp_reading'), post_data)
        self.assertEqual(response.status_code, 200)

        entries = TempReading.objects.all()
        self.assertEqual(len(entries), 1)

        entry = entries[0]
        self.assertEqual(entry.value, value)
        self.assertEqual(entry.date, d)

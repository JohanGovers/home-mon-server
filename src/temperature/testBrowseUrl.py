from django.test import TestCase#, Client
from django.core.urlresolvers import reverse
from temperature import urls

class BrowseUrlTests(TestCase):
    def test_get_all_urls(self):
        """
        Loop through all urls and make sure they return status code 200.
        """

        accepted_codes = [200, 302]

        # print(urls.urlpatterns)
        for url in urls.urlpatterns:
            response = self.client.get(reverse(url.name))
            self.assertTrue(response.status_code in accepted_codes)

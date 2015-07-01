from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_resolves_root_to_home_page_view(self):
        found=resolve("/") #gives us which view does a Url maps, returns ResolverMatch() object
        print(found.url_name)#home, it is mapping to name of urls.py pattern
        self.assertEqual(found.func,home_page)
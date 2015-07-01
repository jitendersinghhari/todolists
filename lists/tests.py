from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_resolves_root_to_home_page_view(self):
        found=resolve("/") #gives us which view does a Url maps
        #print(found)
        self.assertEqual(found.func,home_page)
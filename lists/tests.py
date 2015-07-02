from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.
class HomePageTest(TestCase):

    def test_resolves_root_to_home_page_view(self):
        found=resolve("/") #gives us which view does a Url maps, returns ResolverMatch() object
        #print(found.url_name)#home, it is mapping to name of urls.py pattern
        self.assertEqual(found.func,home_page)
    
    def test_home_page_returns_correct_html(self):
        request=HttpRequest()
        #print(request) #scheme :http or https, POST:QueryDict:{},path:,method,resolver_match,''' get_host()'''

        response=home_page(request)#home_page view returns HttpResponse
        print (response.content.decode())# returns byte object
        
        expected_html=render_to_string('home.html')
        #print(expected_html,' \n',response.content.decode())
        self.assertEqual(response.content.decode(),expected_html)
        
        '''self.assertTrue(response.content.strip( ).startswith(b'<html>'))# content:html send to user
        self.assertIn(b'<title>To-do lists</title>',response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))# content:html send to user'''



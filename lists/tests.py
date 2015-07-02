from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item

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
        #print (response.content.decode())# returns byte object

    def test_home_page_can_save_a_POST_request(self):



        request=HttpRequest()
        request.method="POST"
        request.POST["item_text"]='A new list item'
        response= home_page(request)
        self.assertIn('A new list item',response.content.decode())      
        #print (response.content.decode())# returns byte object
        expected_html=render_to_string('home.html',
            {'new_item_text':'A new list item'}
        )
        self.assertEqual(response.content.decode(),expected_html)
class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item=Item()
        first_item.text='The first (ever) item'
        first_item.save()

        second_item=Item()
        second_item.text='Item the second'
        second_item.save()

        saved_items=Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item=saved_items[0]
        second_saved_item=saved_items[1]
        self.assertEqual(first_saved_item.text,"The first (ever) item")
        self.assertEqual(second_saved_item.text,"Item the second")


  
        



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    #return HttpResponse('<html><title>Django</title></html>')
    return render(request,'home.html',{
        'new_item_text':request.POST.get('item_text',''),
    })#request used to genrate response,template to show, it returns Httpresponse
    



    ''' django will search folder templates inside your app directory and it will 
    build response based on content ot template'''
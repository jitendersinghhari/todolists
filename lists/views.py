from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
# request used to genrate response,template to show, it returns Httpresponse
''' django will search folder templates inside your app directory and it will
    build response based on content ot template'''


def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items':items})

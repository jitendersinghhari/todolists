from django.shortcuts import render, redirect
# from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
# request used to genrate response,template to show, it returns Httpresponse
''' django will search folder templates inside your app directory and it will
    build response based on content ot template'''


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')

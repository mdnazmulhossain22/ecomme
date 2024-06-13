from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import Http404

# Create your views here.
def home(request):

# List of dictionaries
    people = [
        {
            "name": "Nazmul",
            "age": 30,
            "phone": "123-456-7890"
        },
        {
            "name": "Oakil vai",
            "age": 25,
            "phone": "987-654-3210"
        },
        {
            "name": "Sumon vai",
            "age": 35,
            "phone": "555-555-5555"
        }
    ]
    my_list = ['apple', 'mango', 'banana']

    context = {
        'p':people,
        'my_list':my_list,
        'name':155456
    }

    return render(request, 'management/home.html',context)

def contact(request):
    contacts = Contact.objects.all()

    context = {
        'contacts':contacts
    }

    return render(request, 'management/contacts.html',context)
 
def detail(request, id):
    contact = None
    try:
        contact = Contact.objects.get(id=id)
    except Contact.DoesNotExist:
        pass

    context = {
        'contact':contact
    }
    return render(request, 'management/detail.html',context)


def about(request):
    return HttpResponse("About us page ")
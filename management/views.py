from django.shortcuts import render
from django.http import HttpResponse

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

    context = {
        ''
    }

    return render(request, 'management/contact.html')

def about(request):
    return HttpResponse("About us page ")
from django.shortcuts import render
from .models import Hotel

# Create your views here.
def homepage(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels':hotels,
    }
    
    return render(request, 'templates/homepage.html', context)


def contact(request):
    return render(request, 'templates/contact.html')


def about(request):
    return render(request, 'templates/about.html')


def tours(request):
    return render(request, 'templates/tours.html')


def seemore(request, id):
    hotels_seemore = Hotel.objects.get(id=id)
    context = {
        'hotels_seemore':hotels_seemore,
    }
    return render(request, 'seemore.html', context)
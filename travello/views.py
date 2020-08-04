from django.shortcuts import render, redirect
from .models import Destination

# Create your views here.


def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})


def destinations(request):
    dests = Destination.objects.all()

    return render(request, 'destinations.html', {'dests': dests})

from django.shortcuts import render
from .models import Ride

def index(request):
    
    return render(request,'girodm/index.html', context)
from django.shortcuts import render, reverse, get_object_or_404, Http404
from django.http import HttpResponse, HttpResponseRedirect
import string
import random
from datetime import datetime
from django.urls import reverse
from .models import Ride
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
def index(request):
    context = {}
    return render(request,'girodm/index.html', context)

def loginPage(request):
    context = {}
    return render(request, 'girodm/login.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    
    return render(request, 'girodm/register.html', context)

def host(request):
    context = {}
    return render (request, 'girodm/hostaride.html', context)

def createride(request):
    # creates a random string, 10 chars long to use as the ride URL
    letters_to_make_string = string.ascii_letters+string.digits
    random_string = ""
    for i in range(10):
        random_string += random.choice(letters_to_make_string)
    code = random_string
    
    # acquiring data from from
    ride_name = request.POST['rideName']
    host_name = request.POST['hostName']
    pace = request.POST['pace']
    start_location = request.POST['startLocation']
    start_time = request.POST['startTime']
    end_location = request.POST['endLocation']
    end_time = request.POST['endTime']
    private = 'private' in request.POST
    comments = request.POST['comments']
    print(pace)
    ride = Ride(
        ride_name = ride_name, 
        host_name = host_name, 
        start_location = start_location, 
        start_time = start_time, 
        end_location = end_location, 
        end_time = end_time, 
        private = private, 
        comments = comments,
        pace = pace, 
        code = code)

    ride.save()

    return HttpResponseRedirect(reverse('girodm:detail',kwargs={"code":code}))

def detail(request, code):
    # must reference a variable outside of the try/except first when created a local variable 
    ride = None
    try:
        ride = Ride.objects.get(code=code)
    except Ride.DoesNotExist:
        raise Http404("Ride does not exist")    
    
    
    context = {'ride': ride}
    
    return render(request, 'girodm/ride.html',context)


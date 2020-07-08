from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.http import HttpResponse, HttpResponseRedirect
import string
import random
from datetime import datetime
from django.urls import reverse
from .models import Ride
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from . import secrets
from django.contrib.auth.decorators import login_required

def index(request):
    context = {'google_maps_api_key': secrets.google_maps_api_key}
    return render(request,'girodm/index.html', context)

@login_required(login_url='login')
def user(request):
    rides = Ride.objects.filter(created_by=request.user)
   
    context = {'rides': rides}

    return render(request, 'girodm/user.html',context )

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('girodm:user')
        else:
            messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'girodm/login.html', context)


def logOutUser(request):
    logout(request)
    return redirect('girodm:login')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('girodm:login')

    context = {'form':form}
    
    return render(request, 'girodm/register.html', context)

def host(request):
    context = {'google_maps_api_key': secrets.google_maps_api_key}
    return render (request, 'girodm/hostaride.html', context)

def createride(request):
    # creates a random string, 10 chars long to use as the ride URL
    letters_to_make_string = string.ascii_letters+string.digits
    random_string = ""
    for i in range(10):
        random_string += random.choice(letters_to_make_string)
    code = random_string
    
    # acquiring data from from\

    created_by = request.user
    ride_name = request.POST['rideName']
    host_name = request.POST['hostName']
    ride_pace = request.POST['pace']
    ride_type = request.POST['type']
    start_location = request.POST['startLocation']
    start_lat = request.POST['']
    start_lng = request.POST['']
    start_date = request.POST['startDate']
    start_time = request.POST['startTime']
    display_start_time = datetime.strptime(start_date + start_time, '%Y-%m-%d%H:%M')
    end_location = request.POST['endLocation']
    end_lat = request.POST['']
    end_lng = request.POST['']
    end_date = request.POST['endDate']
    end_time = request.POST['endTime']
    display_end_time = datetime.strptime(end_date + end_time, '%Y-%m-%d%H:%M')
    # print(f'\n\n\n startdate {start_time} \n {start_date} \n enddate {end_date} \n {end_time}')
    private = request.POST['privacy']
    comments = request.POST['comments']
    ride = Ride(
        created_by = created_by,
        ride_name = ride_name, 
        host_name = host_name, 
        start_location = start_location, 
        start_time = display_start_time, 
        end_location = end_location, 
        end_time = display_end_time, 
        private = private, 
        comments = comments,
        ride_type = ride_type,
        ride_pace = ride_pace, 
        code = code)

    ride.save()

    return HttpResponseRedirect(reverse('girodm:detail',kwargs={"code":code}))

# def ride(request, code):
def detail(request, code):
    # must reference a variable outside of the try/except first when created a local variable 
    ride = None
    try:
        ride = Ride.objects.get(code=code)
    except Ride.DoesNotExist:
        raise Http404("Ride does not exist")    
    
    
    context = {'ride': ride}
    
    return render(request, 'girodm/ride.html',context)

def editRidePage(request, code):
    ride = Ride.objects.get(code=code)
   
    context = {'ride': ride}

    return render(request, 'girodm/editride.html', context)

def editRide(request, code):
    
    ride = Ride.objects.get(code=code)
    created_by = request.user
    ride_name = request.POST['rideName']
    host_name = request.POST['hostName']
    ride_pace = request.POST['pace']
    ride_type = request.POST['type']
    start_location = request.POST['startLocation']
    start_date = request.POST['startDate']
    start_time = request.POST['startTime']
    display_start_time = datetime.strptime(start_date + start_time, '%Y-%m-%d%H:%M')
    end_location = request.POST['endLocation']
    end_date = request.POST['endDate']
    end_time = request.POST['endTime']
    display_end_time = datetime.strptime(end_date + end_time, '%Y-%m-%d%H:%M')
    private = request.POST['']
    comments = request.POST['comments']
    
    ride.ride_name = ride_name 
    ride.host_name = host_name
    ride.start_location = start_location 
    ride.start_time = display_start_time 
    ride.end_location = end_location 
    ride.end_time = display_end_time 
    ride.private = private
    ride.comments = comments
    ride.ride_pace = ride_pace
    ride.ride_type = ride_type

    ride.save()

    return HttpResponseRedirect(reverse('girodm:detail',kwargs={"code":code}))
    
def viewrides(request):
    rides = None
    try:
        rides = Ride.objects.filter(private=False)
    except Ride.DoesNotExist:
        raise Http404("Ride does not exist")

    context = {'rides': rides}

    return render(request, 'girodm/viewrides.html',context )
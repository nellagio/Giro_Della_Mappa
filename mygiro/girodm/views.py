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

from django.contrib.auth.decorators import login_required

def index(request):
    context = {}
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
    context = {}
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
    pace = request.POST['pace']
    start_location = request.POST['startLocation']
    start_time = request.POST['startTime']
    end_location = request.POST['endLocation']
    end_time = request.POST['endTime']
    private = 'private' in request.POST
    comments = request.POST['comments']
    print(pace)
    ride = Ride(
        created_by = created_by,
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

def viewrides(request):
    rides = None
    try:
        rides = Ride.objects.all()
    except Ride.DoesNotExist:
        raise Http404("Ride does not exist")

    context = {'rides': rides}

    return render(request, 'girodm/viewrides.html',context )
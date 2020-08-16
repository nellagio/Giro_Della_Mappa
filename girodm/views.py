from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import string
import random
from datetime import date, datetime, timedelta
from django.urls import reverse
from .models import Ride
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings

def handler404(request, exception):
    return render(request,'girodm/404.html', status=404)

    
def handler500(request):

    print('hello world')
    return render(request,'girodm/500.html', status=500)

def index(request):
    today = datetime.today().date()
    rides = Ride.objects.filter(private=False,start_time__date=today)
    context = {'rides': rides,'google_maps_api_key': settings.GOOGLE_API_KEY, 'weather_api_key':settings.WEATHER_API_KEY}
    return render(request,'girodm/index.html', context)

def about(request):
    context = {'google_maps_api_key': settings.GOOGLE_API_KEY}
    return render(request,'girodm/about.html', context)

@login_required
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
    context = {'google_maps_api_key': settings.GOOGLE_API_KEY}
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
    start_lat = request.POST['startLat']
    start_lng = request.POST['startLng']
    start_date = request.POST['startDate']
    start_time = request.POST['startTime']
    display_start_time = datetime.strptime(start_date + start_time, '%Y-%m-%d%H:%M')
    end_location = request.POST['endLocation']
    end_lat = request.POST['endLat']
    end_lng = request.POST['endLng']
    end_date = request.POST['endDate']
    end_time = request.POST['endTime']
    display_end_time = datetime.strptime(end_date + end_time, '%Y-%m-%d%H:%M')
    private = request.POST['privacy']
    comments = request.POST['comments']
    ride = Ride(
        created_by = created_by,
        ride_name = ride_name, 
        host_name = host_name, 
        start_location = start_location,
        start_lat = start_lat,
        start_long = start_lng, 
        start_time = display_start_time, 
        end_location = end_location,
        end_lat = end_lat,
        end_long = end_lng,
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
        ride.times_clicked += 1
        ride.save()
    except Ride.DoesNotExist:
        raise Http404("Ride does not exist")    
    
    context = {'ride': ride, 'google_maps_api_key': settings.GOOGLE_API_KEY,}
    
    return render(request, 'girodm/ride.html',context)

def editRidePage(request, code):

    ride = Ride.objects.get(code=code)

    context = {'ride': ride, 'google_maps_api_key': settings.GOOGLE_API_KEY}
    
    return render(request, 'girodm/editride.html', context)

def editRide(request, code):
    
    ride = Ride.objects.get(code=code)
    created_by = request.user
    ride_name = request.POST['rideName']
    host_name = request.POST['hostName']
    ride_pace = request.POST['pace']
    ride_type = request.POST['type']

    start_location = request.POST['startLocation']
    start_lat = request.POST['startLat']
    start_lng = request.POST['startLng']
    start_date = request.POST['startDate']
    start_time = request.POST['startTime']
    display_start_time = datetime.strptime(start_date + start_time, '%Y-%m-%d%H:%M')

    end_location = request.POST['endLocation']
    end_lat = request.POST['endLat']
    end_lng = request.POST['endLng']
    end_date = request.POST['endDate']
    end_time = request.POST['endTime']
    display_end_time = datetime.strptime(end_date + end_time, '%Y-%m-%d%H:%M')

    private = request.POST['private']
    comments = request.POST['comments']
    
    ride.created_by = request.user
    ride.ride_name = ride_name 
    ride.host_name = host_name
    ride.ride_pace = ride_pace
    ride.ride_type = ride_type

    ride.start_location = start_location
    ride.start_lat = start_lat
    ride.start_long = start_lng 
    ride.start_date = start_date
    ride.start_time = display_start_time 

    ride.end_location = end_location
    ride.end_lat = end_lat
    ride.end_long = end_lng
    ride.end_Date = end_date
    ride.end_time = display_end_time

    ride.private = private
    ride.comments = comments
    

    ride.save()

    return HttpResponseRedirect(reverse('girodm:detail',kwargs={"code":code}))

def calendarPage(request):
    rides = None
    try:
        rides = Ride.objects.filter(private=False)
        print(rides)
    except Ride.DoesNotExist:
        raise Http404("Ride does not exist")
    context = {'rides': rides, 'google_maps_api_key': settings.GOOGLE_API_KEY,}

    return render(request, 'girodm/calendar.html',context )

def viewrides(request):
    today = date.today()
    rides = None
    try:
        rides = Ride.objects.filter(private=False,start_time__date__gte=today)
        print(rides)
    except Ride.DoesNotExist:
        raise Http404("Ride does not exist")
    context = {'rides': rides, 'google_maps_api_key': settings.GOOGLE_API_KEY,}

    return render(request, 'girodm/viewrides.html',context )

def getLatLng(request):
    start_location_list = []
    end_location_list = []
    rides = Ride.objects.filter(private=False)
 
    for ride in rides:
        start_location = {
            'label': ride.ride_name + ' start location',
            'lat': ride.start_lat,
            'lng': ride.start_long,
            'url': reverse('girodm:detail',kwargs={"code":ride.code}),
            'date': ride.start_time,
        }

        start_location_list.append(start_location)
        end_location = {
            'label': ride.ride_name + ' end location',
            'lat': ride.end_lat,
            'lng': ride.end_long,
        }
        end_location_list.append(end_location)
    print(f'start_location = {start_location_list} \n {end_location_list}')
    return JsonResponse({'start_location_list': start_location_list, 'end_location_list': end_location_list})

def delete_ride(request, code):
    ride = Ride.objects.get(code=code)
    ride.delete()
    return HttpResponseRedirect(reverse('girodm:user'))
from django.shortcuts import render, reverse, get_object_or_404, Http404
from django.http import HttpResponse, HttpResponseRedirect
import string
from datetime import datetime
from django.urls import reverse
from .models import Ride

def index(request):
    
    return render(request,'girodm/index.html')

def host(request):
    
    return render (request, 'girodm/hostaride.html')

def detail(request, code):
    try:
        ride = Ride.objects.get(code=code)
    except Ride.DoesNotExist:
        raise Http404("Ride does not exist")    
    
    
    context = {'ride': ride}
    
    return render(request, 'girodm/ride.html',context)

def createride(request):
    # creates a random string, 10 chars long to use as the ride URL
    letters_to_make_string = string.ascii_letters+string.digits
    random_string = ""
    for i in range(10):
        random_string += random.choice(letters_to_make_string)
    code = random_string
    
    # acquiring data from from
    ride_name = request.POST['ridename']
    host_name = request.POST['hostname']
    pace = request.POST['pace']
    start_location = request.POST['startlocation']
    start_time = request.POST['starttime']
    end_location = request.POST['endlocation']
    end_time = request.POST['endtime']
    private = 'private' in request.POST
    comments = request.POST['comments']

    ride = Ride(ride_name = ride_name, host_name = host_name, start_location = start_location, start_time = start_time, end_location = end_location, end_time = end_time, private = private, comments = comments, code = code)

    ride.save()

    return HttpResponseRedirect(reverse('girodm:detail',kwargs={"code":code}))
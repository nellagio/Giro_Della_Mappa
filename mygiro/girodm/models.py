from django.db import models

class Pace(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name
        
class Ride(models.Model):

    host_name = models.CharField(max_length=30)
    start_location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    waypoint = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    end_time = models.DateTimeField()
    private = models.BooleanField(default=False)
    comments = models.CharField(max_length=400)
    pace = models.ManyToManyField(Pace)

    def __str__(self):
        return self.name
    
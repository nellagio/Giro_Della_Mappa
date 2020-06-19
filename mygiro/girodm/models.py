from django.db import models

RIDE_TYPE = (
    ("ff","Family Friendly"),
    ("ep","Social (Eighteen +)"),
    ("tp","Training Pace"),
)

class Ride(models.Model):

    host_name = models.CharField(max_length=30)
    start_location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    waypoint = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    end_time = models.DateTimeField()
    private = models.BooleanField(default=False)
    comments = models.CharField(max_length=400)
    pace = models.CharField(
        max_length=200,
        choices=RIDE_TYPE,
        default = 'fam'
    )
    
    def __str__(self):
        return self.name
    
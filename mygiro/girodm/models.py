from django.db import models

RIDE_TYPE = (
    ("ff","Family Friendly"),
    ("ep","Social (Eighteen +)"),
    ("tp","Training Pace"),
)

class Ride(models.Model):
    
    ride_name = models.CharField(max_length=30)
    host_name = models.CharField(max_length=30)
    start_location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_location = models.CharField(max_length=200)
    end_time = models.DateTimeField()
    private = models.BooleanField(default=False)
    code = models.CharField(max_length=10) 
    comments = models.TextField()
    pace = models.CharField(
        max_length=200,
        choices=RIDE_TYPE,
        default = 'fam'
    )
    # forgeign key to user model for users
    # ride paceModel foreign key
    def __str__(self):
        return self.ride_name
    
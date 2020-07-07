from django.db import models
from django.contrib.auth import get_user_model


RIDE_TYPE = (
    ("ff","Family Friendly"),
    ("ep","Social (18/21+) Ride"),
    ("tp","Training Ride"),
    ("sp", "Special Event"),
)

RIDE_PACE = (
    ("sl", "3-8 mph"),
    ("md", "9-12 mph"),
    ("fs", "13-17 mph"),
    ("tf", "18+ mph"),
)

class Ride(models.Model):

    created_by = models.ForeignKey(get_user_model(),null=True, blank=True, on_delete=models.CASCADE)
    ride_name = models.CharField(max_length=30)
    host_name = models.CharField(max_length=30)
    start_location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    start_long = models.FloatField(null=True)
    start_lat  = models.FloatField(null=True)
    end_location = models.CharField(max_length=200)
    end_time = models.DateTimeField()
    end_long = models.FloatField(null=True)
    end_lat  = models.FloatField(null=True)
    private = models.BooleanField(default=False)
    code = models.CharField(max_length=10) 
    comments = models.TextField()
    ride_type = models.CharField(
        max_length=200,
        choices=RIDE_TYPE,
        default = 'ff'
    )
    ride_pace = models.CharField(
        max_length=200,
        choices=RIDE_PACE,
        default = 'md'
    )

    def __str__(self):
        return self.ride_name

# class Profile(models.Model):
#     user = models.ForeignKey("", verbose_name=_(""), on_delete=models.CASCADE)
#     def __str__(self):
#         return self.user
    
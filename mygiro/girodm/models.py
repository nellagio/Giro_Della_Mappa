from django.db import models
from django.contrib.auth import get_user_model

RIDE_TYPE = (
    ("ff","Family Friendly"),
    ("ep","Social (18/21+)"),
    ("tp","Training Pace"),
)

class Ride(models.Model):

    created_by = models.ForeignKey(get_user_model(),null=True, blank=True, on_delete=models.CASCADE)
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
        default = 'ff'
    )

    def __str__(self):
        return self.ride_name

# class Profile(models.Model):
#     user = models.ForeignKey("", verbose_name=_(""), on_delete=models.CASCADE)
#     def __str__(self):
#         return self.user
    
from django.urls import path
from . import views


app_name = 'girodm'
urlpatterns = [
    path('', views.index, name='index'),
]
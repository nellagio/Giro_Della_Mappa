from django.urls import path
from . import views


app_name = 'girodm'
urlpatterns = [
    path('', views.index, name='index'),
    path('host/', views.host, name='host'),
    path('<str:code>/', views.detail, name="detail"),
    path('create_a_ride/', views.createride, name="createride"),
]
from django.urls import path
from . import views

app_name = 'girodm'
urlpatterns = [
    path('', views.index, name='index'),
    path('mission/', views.about, name="about"),
    path('user/', views.user, name='user'),
    path('host/', views.host, name='host'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('calendar/', views.calendarPage, name="calendar"),
    path('marketplace/', views.marketplace, name="marketplace"),
    path('viewrides/', views.viewrides ,name="viewrides"),
    path('ride/<str:code>/', views.detail, name="detail"),
    path('ride/<str:code>/edit/', views.editRidePage, name="editridepage"),
    path('ride/<str:code>/delete', views.delete_ride, name="deleteride"),
    path('create_a_ride/', views.createride, name="createride"),
    path('ride/<str:code>/edit_a_ride/', views.editRide, name="editride"),
    path('getlatlng/', views.getLatLng, name="getlatlng"),
]
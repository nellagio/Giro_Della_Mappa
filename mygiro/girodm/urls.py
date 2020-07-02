from django.urls import path
from . import views

app_name = 'girodm'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('host/', views.host, name='host'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('viewrides/', views.viewrides ,name="viewrides"),
    path('ride/<str:code>/', views.detail, name="detail"),
    path('create_a_ride/', views.createride, name="createride"),
]
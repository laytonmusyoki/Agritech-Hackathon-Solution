from django.urls import path
from .views import register,signin,Logout,home

urlpatterns=[
    path('',signin,name='signin'),
    path('register/',register,name='register'),
    path('logout/',Logout,name='Logout'),
    path('home/',home,name='home')
]
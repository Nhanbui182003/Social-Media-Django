from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signup, name='signin'),
]

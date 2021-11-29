from django.urls import path
from . import views
urlpatterns=[
    path('home/', views.sample, name='home'),
    path('hi/', views.sample1, name='hi'),
    path('hello/', views.sample2, name='hello'),
    path('sample/', views.fnsample, name='sample'),


]
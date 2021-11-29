from django.urls import path
from . import views
urlpatterns=[
    
    path('how/', views.fnsample, name='how/'),
    path('hello/', views.fnsample1, name='hello/')

]
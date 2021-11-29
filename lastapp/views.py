from django.shortcuts import render
from django. http import HttpResponse

# Create your views here.
def fnsample(request):
    return HttpResponse("this is last")

def fnsample1(request):
    return HttpResponse("FINAL OVER")    
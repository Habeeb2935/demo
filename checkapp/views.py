from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
    return HttpResponse("HI GUYS...")



def sample1(request):
    return HttpResponse("hii")


def sample2(request):
      return HttpResponse("WELCOME TO OOTY NICE TO MEET YOU")

def fnsample(request):
    return render(request,'sample.html')      



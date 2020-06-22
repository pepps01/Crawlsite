from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def grab(request):
    return HttpResponse("Welcome Home")
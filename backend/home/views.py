from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeScreen(request):
    return HttpResponse('home screen')

def homeTest(request):
    return HttpResponse('homeTest')
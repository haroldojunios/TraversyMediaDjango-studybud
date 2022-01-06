from django.shortcuts import render
from django.http.response import HttpResponse

def home(req):
    return HttpResponse('Home page')

def room(req):
    return HttpResponse('ROOM')

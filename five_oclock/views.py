from django.shortcuts import render
from django.http import HttpResponse
import datetime

def isItFive(requests):
    now = datetime.datetime.now()
    if now.hour == 17:
        return HttpResponse("it's 5 o'clock there")
    else:
        return HttpResponse("it's 5 o'clock somewhere")
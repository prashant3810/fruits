from django.http import HttpResponse
from django.shortcuts import render

def types(request):
    return HttpResponse("malgoba rasal benesa nuziveedu")
# Create your views here.
def apple_types(request):
    return HttpResponse("kashmir,telamgana,rayalaseema")
def apple_colour(request):
    return HttpResponse("red,green,blue,orange")
def apple_grade(request):
    return HttpResponse("excellent good above avreage average bad")
def apple_state(request):
    return HttpResponse("excellent bad and size good")
def apple_district(request):
    return HttpResponse("bad and size good")

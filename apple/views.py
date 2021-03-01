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


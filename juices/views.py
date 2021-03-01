from django.http import HttpResponse
from django.shortcuts import render


def varaities(request):
    return HttpResponse("fruity maaza slice mangoes")
def varaities_names(request):
    return HttpResponse("fruity maaza names slice mangoes")
def varaities_types(request):
    return HttpResponse("fruity maaza  types slice mangoes")
def varieties_sizes(request):
    return HttpResponse("fruits are in different sizes")


# Create your views here.

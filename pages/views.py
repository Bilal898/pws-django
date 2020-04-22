from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


def home(request):
    return HttpResponse("<h1>Welcome to homepage </h1>")


def contact(request):
    return HttpResponse("<h1>Contact Us </h1>")


def about(request):
    return HttpResponse("<h1>About Us </h1>")


def member(request, cat_id, mem_id):
    return HttpResponse("<h1>Team Member ID: {} from Category ID: {}</h1>".format(mem_id, cat_id))


def team(request):
    if request.method == 'GET' and 'cat_id' in request.GET and 'mem_id' in request.GET:
        return HttpResponse("<h1>Team Member ID: {} from Category ID: {}</h1>".format(request.GET.get('mem_id'), request.GET.get('cat_id')))
    else:
        return HttpResponse("<h1>Team Members List:</h1>")


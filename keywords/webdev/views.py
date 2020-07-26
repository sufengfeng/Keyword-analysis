from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.from webdev.models import BlogPostz


def test(request):
    return HttpResponse("Hello world2!")

def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def userOptions(request):
    return render(request, 'login.html')


def userPanel(request):
    return render(request, 'login.html')




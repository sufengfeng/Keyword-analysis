from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from webdev.models import BlogPost


def hello(request):
    return HttpResponse("Hello world2!")


def archive(request):
    posts = BlogPost.objects.all()
    return render(request, 'archive.html', {'posts': posts})

def index(request):
    return render(request, 'index.html')
def signup(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')
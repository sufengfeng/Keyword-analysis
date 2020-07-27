from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.from webdev.models import BlogPostz
from webdev.models import User


def test(request):
    return HttpResponse("Hello world2!")

def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')



@csrf_exempt
def login(request):
    if request.method=="POST" and request.POST:
        email=request.POST["email"]
        password=request.POST.get("password")
        users=User.objects.filter(email=email,password=password)
        #print(users.count())
        if users.count()>0:
            #return render(request, 'login.html')
            return HttpResponseRedirect('/')
            #/?message=error
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')



def userOptions(request):
    return render(request, 'login.html')


def userPanel(request):
    return render(request, 'login.html')




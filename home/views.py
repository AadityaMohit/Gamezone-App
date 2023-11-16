from django.shortcuts import render,redirect
from home.models import Signin
# after migrating import model and make contact model save
# Create your views here.
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,"contact.html")

def signin(request):
    if request.method == "POST":
        name = request.POST.get("name")  # Use request.POST.get() to safely access POST data
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        print(name, email, phone)
        ins = Signin(name=name, email=email)
        ins.save()
        print("Data has been saved")

    return render(request, "signin.html")


def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')


def redirect(request):
    return render(request,'redirect.html')
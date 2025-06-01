from django.shortcuts import render
from django.template import loader
from .models import User
from .forms import RegisterForm

# Create your views here.
def login(request):
    template = loader.get_template("user/login.html")
    return render(request, "user/login.html")

def register(request):
    form = RegisterForm()
    return render(request, "user/register.html", {"form": form})
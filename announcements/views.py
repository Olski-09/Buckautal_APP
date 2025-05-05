from Scripts.bottle import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template import loader
# Create your views here.
def index(request):
    template = loader.get_template("announcements/index.html")
    return render(request, "announcements/index.html")
from Scripts.bottle import response
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from django.template import loader
from django import forms
from django.utils import timezone
# Create your views here.
def index(request):
    template = loader.get_template("announcements/index.html")
    return render(request, "announcements/index.html")


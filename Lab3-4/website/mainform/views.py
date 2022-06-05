from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainform/index.html')

def about(request):
    return render(request, 'mainform/about.html')

def register(request):
    return render(request, 'mainform/register.html')

def login(request):
    return render(request, 'mainform/login.html')


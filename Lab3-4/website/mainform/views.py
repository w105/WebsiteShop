from django.shortcuts import redirect, render
from .models import PlantModel
from django.views.generic import TemplateView
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.contrib.auth import authenticate, login


class About(TemplateView):
    template_name = 'mainform/about.html'


class RegisterView(TemplateView):
    template_name = "main/Register.html"


class Login(TemplateView):
    template_name = 'mainform/login.html'


def index(request):
    plants = PlantModel.objects.order_by('-id')
    return render(request, 'mainform/index.html', {'PlantModel': plants})


# def dispatch(self, request, *args, **kwargs):
#     if request.method == 'POST':


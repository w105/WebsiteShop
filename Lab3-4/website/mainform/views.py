from django.shortcuts import render
from .models import PlantModel
from django.views.generic import TemplateView


class About(TemplateView):
    template_name = 'mainform/about.html'


class Register(TemplateView):
    template_name = 'mainform/register.html'


class Login(TemplateView):
    template_name = 'mainform/login.html'


def index(request):
    plants = PlantModel.objects.order_by('-id')
    return render(request, 'mainform/index.html', {'PlantModel': plants})



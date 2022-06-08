from django.shortcuts import render
from .models import PlantModel


# class AboutView(TemplateView):
#  template_name = "about.html"


# def about(request):
#     return render(request, 'mainform/about.html')


def register(request):
    return render(request, 'mainform/register.html')


def login(request):
    return render(request, 'mainform/login.html')


def index(request):
    plants = PlantModel.objects.order_by('-id')
    return render(request, 'mainform/index.html', {'PlantModel': plants})



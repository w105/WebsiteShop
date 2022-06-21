from django.shortcuts import redirect, render
from django.urls import reverse
from .models import PlantModel
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def logout_user(self):
    logout(self)
    return redirect('index')


class About(TemplateView):
    template_name = 'mainform/about.html'


class Addproduct(TemplateView):
    template_name = 'mainform/addproduct.html'


class Login(TemplateView):
    template_name = 'mainform/login.html'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context['error'] = "Неверный логин или пароль"
        return render(request, self.template_name, context)


def index(request):
    plants = PlantModel.objects.order_by('-id')
    return render(request, 'mainform/index.html', {'title': 'Главная', 'PlantModel': plants})


class Register(TemplateView):
    template_name = "mainform/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse('index'))

        return render(request, self.template_name)


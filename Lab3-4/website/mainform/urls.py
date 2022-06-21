from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', About.as_view()),
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('logout', views.logout_user),
    path('add', Addproduct.as_view()),
]

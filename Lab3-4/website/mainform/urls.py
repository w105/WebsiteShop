from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.index),
    path('about', About.as_view()),
    path('register', Register.as_view()),
    path('login', Login.as_view()),
]
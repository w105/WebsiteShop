from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    # path('about/', TemplateViews.as_view(template_name="about.html")),
    path('register', views.register),
    path('login', views.login),
]
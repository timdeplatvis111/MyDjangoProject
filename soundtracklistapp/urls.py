from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name="soundtracklistapp-home"),
    path ('about', views.about, name="soundtracklistapp-about"),
]

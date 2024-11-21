from django.contrib import admin
from django.urls import path
from .views import (home, about, feedback)

urlpatterns = [
    path('', home),
    path('about', about),
    path('feedback', feedback)
]
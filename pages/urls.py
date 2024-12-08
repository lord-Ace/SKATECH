from django.contrib import admin
from django.urls import path
from .views import (about, feedback)
from news.views import (home, featured, latest, tech, entertainment, finance)
#from multimedia
from adverts.views import (advertise, place)

urlpatterns = [
    path('', home),
    path('about', about),
    path('feedback', feedback),
    path('advert', advertise),
    path('place-advert', place),
    path('featured', featured),
    path('latest', latest),
    path('tech', tech),
    path('entertainment', entertainment),
    path('finance', finance)
]
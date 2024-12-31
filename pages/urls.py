from django.contrib import admin
from django.urls import path
from .views import (about, feedback)
from news.views import (home, featured, latest, tech, entertainment, finance)
#from multimedia
from adverts.views import (advertise, place)

urlpatterns = [
    path('', home),
    path('About', about, name='about'),
    path('feedback', feedback, name='feedback'),
    path('adverts/advert', advertise, name='advertise'),
    path('adverts/place-advert', place, name='place'),
    path('stories/featured', featured, name='featured'),
    path('stories/latest', latest, name='latest'),
    path('stories/tech', tech, name='tech'),
    path('stories/entertainment', entertainment, name='entertainment'),
    path('stories/finance', finance, name='finance')
]
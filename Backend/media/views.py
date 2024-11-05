from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Media

def media_list(request):
    media_files = Media.objects.all()
    return render(request, 'media/media_list.html', {'media_files': media_files})

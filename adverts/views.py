from django.shortcuts import render

# Create your views here.
def advertise(request):
  return render(request, 'Html/adverts.html')
def place(request):
  return render(request, 'Html/place_adverts.html')
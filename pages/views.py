from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def about(request):
  return render(request, 'Html/About_Us.html')
def feedback(request):
  return render(request, 'Html/R&F.html')
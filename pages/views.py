from django.shortcuts import render

# Create your views here.
def about(request):
  return render(request, 'Html/About_Us.html')
def feedback(request):
  return render(request, 'Html/R&F.html')
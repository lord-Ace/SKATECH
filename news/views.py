from django.shortcuts import render
from .models import Article

article = Article.objects.all()
articles = {'articles': article}
# Create your views here.
def home(request):
  return render(request, 'index.html', articles)
def featured(request):
  return render(request, 'Html/featured.Html', articles)
def latest(request):
  return render(request, 'Html/latest.html', articles)
def tech(request):
  return render(request, 'Html/tech.html', articles)
def entertainment(request):
  return render(request, 'Html/entertainment.html', articles)
def finance(request):
  return render(request, 'Html/finance.html', articles)

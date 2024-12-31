from django.shortcuts import render, get_object_or_404
from .models import Article, Comment

# Create your views here.
def home(request):
  all_articles = Article.objects.all()
  articles = {'articles': all_articles}
  return render(request, 'index.html', articles)
def featured(request):
  all_articles = Article.objects.filter(Featured=True)
  articles = {'articles': all_articles}
  return render(request, 'Html/featured.html', articles)
def latest(request):
  all_articles = Article.objects.filter(Trending=True, HappeningToday=True)
  articles = {'articles': all_articles}
  return render(request, 'Html/latest.html', articles)
def tech(request):
  all_articles = Article.objects.filter(Category='TECH')
  articles = {'articles': all_articles}
  return render(request, 'Html/tech.html', articles)
def entertainment(request):
  all_articles = Article.objects.filter(Category='ENTERTAINMENT')
  articles = {'articles': all_articles}
  return render(request, 'Html/entertainment.html', articles)
def finance(request):
  all_articles = Article.objects.filter(Category='FINANCE')
  articles = {'articles': all_articles}
  return render(request, 'Html/finance.html', articles)
#def search_and_detail(request, Title):
  

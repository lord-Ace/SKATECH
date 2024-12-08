from django.db import models

# Create your models here.
categories = {
    'TECH': 'TECH',
    'ENTERTAINMENT': 'ENTERTAINMENT',
    'FINANCE': 'FINANCE'
}
class Article(models.Model):
    Title = models.CharField(max_length =100, unique=True )
    Category = models.CharField(max_length = 50, choices=categories, default='TECH')
    Date_published = models.DateField(auto_now_add=True)
    Views = models.IntegerField(default=0)
    Content = models.TextField(default='hello')
    Is_Featured = models.BooleanField(default=False)

class Comment(models.Model):
    related_article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    commenter_name = models.CharField(max_length=30, null=True)
    email=models.EmailField(null=True)
    comment = models.TextField(null=True)

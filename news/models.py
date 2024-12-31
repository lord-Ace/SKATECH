from django.db import models
from multiselectfield import MultiSelectField
from itertools import chain

# Create your models here.
category_choices = {
    'TECH': 'TECH',
    'ENTERTAINMENT': 'ENTERTAINMENT',
    'FINANCE': 'FINANCE'
}
sub_category_choices = {
    'Tech': {
        'TECH FOR GOOD': 'TECH FOR GOOD',
        'EMERGING TECH': 'EMERGING TECH',
        'CYBERSECURITY': 'CYBERSECURITY',
        'TECH EMPOWERMENT': 'TECH EMPOWERMENT',
        'TECH FOR GOOD': 'TECH FOR GOOD'
    }
}
label_choices = {
    'FEATURED': 'FEATURED',
    'BREAKING NEWS': 'BREAKING NEWS',
    'TRENDING': 'TRENDING',
    'HAPPENING TODAY': 'HAPPENING TODAY',
    'TOP TODAY': 'TOP TODAY'
}
flatened_subC = []
class Article(models.Model):
    Title = models.CharField(max_length =100, unique=True )
    Category = models.CharField(max_length = 50, choices=category_choices, default='TECH')
    DatePublished = models.DateField(auto_now_add=True)
    Views = models.IntegerField(default=0)
    Content = models.TextField(default='hello')
    Featured = models.BooleanField(blank=True, default=False)
    BreakingNews = models.BooleanField(blank=True, default=False)
    Trending = models.BooleanField(blank=True, default=False)
    HappeningToday = models.BooleanField(blank=True, default=False)
    TopToday = models.BooleanField(blank=True, default=False)
    def __str__(self):
        return self.Title

class Comment(models.Model):
    related_article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    commenter_name = models.CharField(max_length=30, null=True, unique=True)
    email=models.EmailField(null=True, unique=True)
    comment = models.TextField(null=True)
    def __str__(self):
        return self.commenter_name
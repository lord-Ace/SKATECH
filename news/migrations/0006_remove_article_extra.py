# Generated by Django 5.1.2 on 2024-12-28 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_extra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Extra',
        ),
    ]
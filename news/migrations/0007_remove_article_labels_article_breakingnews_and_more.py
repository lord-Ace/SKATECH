# Generated by Django 5.1.2 on 2024-12-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_article_extra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Labels',
        ),
        migrations.AddField(
            model_name='article',
            name='BreakingNews',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='Featured',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='HappeningToday',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='TopToday',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='Trending',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

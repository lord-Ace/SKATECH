# Generated by Django 5.1.3 on 2024-11-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_article_date_published_alter_article_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Date_published',
            new_name='Date_publishd',
        ),
        migrations.AddField(
            model_name='article',
            name='Views',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-07 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_rename_comments_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Date_publishd',
            new_name='Date_published',
        ),
    ]

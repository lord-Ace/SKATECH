# Generated by Django 5.1.3 on 2024-11-25 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_structure_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='structure',
            name='Is_Featured',
        ),
    ]

# Generated by Django 5.1.4 on 2025-01-06 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="category",
            name="description",
        ),
        migrations.RemoveField(
            model_name="category",
            name="updated_at",
        ),
    ]

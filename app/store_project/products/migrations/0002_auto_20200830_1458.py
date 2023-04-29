# Generated by Django 3.1 on 2020-08-30 14:58

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="slug",
            field=models.SlugField(
                blank=True, default="", max_length=80, verbose_name="Slug for product"
            ),
        ),
    ]

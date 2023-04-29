# Generated by Django 3.1.2 on 2020-12-04 16:19

import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Exercise ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="Exercise name"),
                ),
                (
                    "slug",
                    models.SlugField(
                        default="", unique=True, verbose_name="Slug for exercise"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Time created"
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Time last modified"
                    ),
                ),
            ],
        ),
    ]

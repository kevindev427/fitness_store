# Generated by Django 3.1.2 on 2020-12-04 17:14

import uuid

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("exercises", "0003_auto_20201204_1700"),
    ]

    operations = [
        migrations.CreateModel(
            name="Alternative",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Alternative ID",
                    ),
                ),
                (
                    "problem",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=200,
                        verbose_name="Problem with original exercise",
                    ),
                ),
                (
                    "alternate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="alternate",
                        to="exercises.exercise",
                        verbose_name="Alternative exercise",
                    ),
                ),
                (
                    "original",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="original",
                        to="exercises.exercise",
                        verbose_name="Original exercise",
                    ),
                ),
            ],
        ),
    ]

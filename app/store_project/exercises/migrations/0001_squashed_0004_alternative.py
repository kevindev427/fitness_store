# Generated by Django 3.1.2 on 2020-12-04 17:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    replaces = [
        ("exercises", "0001_initial"),
        ("exercises", "0002_auto_20201204_1648"),
        ("exercises", "0003_auto_20201204_1700"),
        ("exercises", "0004_alternative"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Category ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Category name")),
                (
                    "slug",
                    models.SlugField(
                        default="", unique=True, verbose_name="Slug for category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
                "ordering": ["name"],
            },
        ),
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
                (
                    "demonstration",
                    models.URLField(
                        blank=True, default="", verbose_name="Demonstration link"
                    ),
                ),
                (
                    "explanation",
                    models.URLField(
                        blank=True, default="", verbose_name="Explanation link"
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        blank=True,
                        to="exercises.Category",
                        verbose_name="Exercise category",
                    ),
                ),
            ],
        ),
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

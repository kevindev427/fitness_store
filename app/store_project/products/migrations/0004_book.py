# Generated by Django 3.1.2 on 2021-01-26 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_lifecycle.mixins
import markdownx.models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0003_auto_20201220_0055"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "status",
                    models.CharField(
                        choices=[("pb", "Public"), ("pr", "Private"), ("dr", "Draft")],
                        default="dr",
                        max_length=2,
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=80, verbose_name="Name of product"),
                ),
                (
                    "slug",
                    models.SlugField(
                        default="",
                        max_length=80,
                        unique=True,
                        verbose_name="Slug for product",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name="Short description of product",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10, verbose_name="Price"
                    ),
                ),
                (
                    "stripe_price_id",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Stripe Price ID"
                    ),
                ),
                (
                    "views",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Number of times viewed"
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
                    "featured_image",
                    models.ImageField(
                        blank=True,
                        upload_to="products/images/",
                        verbose_name="Featured product image",
                    ),
                ),
                (
                    "page_content",
                    markdownx.models.MarkdownxField(
                        blank=True, default="", verbose_name="Page content, in markdown"
                    ),
                ),
                (
                    "pdf",
                    models.FileField(
                        blank=True, upload_to="products/books/pdf/", verbose_name="PDF"
                    ),
                ),
                (
                    "epub",
                    models.FileField(
                        blank=True,
                        upload_to="products/books/epub/",
                        verbose_name="EPUB",
                    ),
                ),
                (
                    "mobi",
                    models.FileField(
                        blank=True,
                        upload_to="products/books/mobi/",
                        verbose_name="MOBI",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author of product",
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
                "abstract": False,
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
    ]

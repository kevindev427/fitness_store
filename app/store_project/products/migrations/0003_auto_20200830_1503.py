# Generated by Django 3.1 on 2020-08-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_auto_20200830_1458"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="slug",
            field=models.SlugField(
                default="", max_length=80, unique=True, verbose_name="Slug for product"
            ),
        ),
    ]

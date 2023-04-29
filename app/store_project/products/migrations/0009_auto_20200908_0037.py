# Generated by Django 3.1 on 2020-09-08 00:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0008_auto_20200907_1955"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.AlterModelOptions(
            name="program",
            options={"ordering": ["-created"]},
        ),
        migrations.AlterField(
            model_name="program",
            name="duration",
            field=models.IntegerField(
                blank=True,
                default=None,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Number of weeks",
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="frequency",
            field=models.IntegerField(
                blank=True,
                default=None,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Training sessions per week",
            ),
        ),
        migrations.AddField(
            model_name="program",
            name="categories",
            field=models.ManyToManyField(to="products.Category"),
        ),
    ]

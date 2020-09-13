# Generated by Django 3.1 on 2020-09-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200907_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='duration',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Number of weeks'),
        ),
        migrations.AddField(
            model_name='program',
            name='frequency',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Training frequency'),
        ),
    ]
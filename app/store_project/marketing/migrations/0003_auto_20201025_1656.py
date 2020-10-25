# Generated by Django 3.1.2 on 2020-10-25 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketing', '0002_auto_20201023_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='recipient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emails_received', to=settings.AUTH_USER_MODEL, verbose_name='To'),
        ),
        migrations.AlterField(
            model_name='email',
            name='sender',
            field=models.CharField(default='Lance Goyke <lance@lancegoyke.com>', max_length=150, verbose_name='From'),
        ),
    ]

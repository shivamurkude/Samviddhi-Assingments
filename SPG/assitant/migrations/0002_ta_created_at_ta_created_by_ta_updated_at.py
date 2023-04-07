# Generated by Django 4.2 on 2023-04-07 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assitant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ta',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ta',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ta_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ta',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
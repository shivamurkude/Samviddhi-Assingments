# Generated by Django 4.2 on 2023-04-05 12:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TA',
            fields=[
                ('ta_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('native_english_speaker', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=50)),
                ('course_instructor', models.IntegerField()),
                ('course', models.CharField(max_length=100)),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=50)),
                ('class_size', models.IntegerField()),
                ('performance_score', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=50)),
            ],
        ),
    ]

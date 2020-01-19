# Generated by Django 3.0 on 2020-01-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='number_in_queue',
        ),
        migrations.AddField(
            model_name='appointment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
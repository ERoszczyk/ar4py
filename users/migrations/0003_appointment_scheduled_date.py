# Generated by Django 3.0 on 2020-01-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200119_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='scheduled_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-13 09:27

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0006_auto_20190613_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='planning',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]

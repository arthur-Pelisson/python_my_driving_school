# Generated by Django 2.2.2 on 2019-06-14 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0028_auto_20190613_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planning', to=settings.AUTH_USER_MODEL),
        ),
    ]

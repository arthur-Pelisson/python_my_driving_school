# Generated by Django 2.2.2 on 2019-06-14 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0031_auto_20190614_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor_planning', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='planning',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_planning', to=settings.AUTH_USER_MODEL),
        ),
    ]
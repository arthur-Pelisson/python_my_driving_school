# Generated by Django 2.2.2 on 2019-06-13 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0021_auto_20190613_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='instructor',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planning.Student'),
        ),
    ]

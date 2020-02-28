# Generated by Django 3.0.3 on 2020-02-26 13:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200226_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tut',
            name='tut_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 16, 0, 1, 975602), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tut',
            name='tut_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutSeries', verbose_name='Series'),
        ),
    ]
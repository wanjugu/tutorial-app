# Generated by Django 3.0.3 on 2020-02-26 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200226_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tut',
            name='tut_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 15, 37, 17, 114855), verbose_name='date published'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-26 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200226_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tut',
            name='tut_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 16, 21, 9, 426750), verbose_name='date published'),
        ),
    ]

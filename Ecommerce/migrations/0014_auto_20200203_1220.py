# Generated by Django 2.2.7 on 2020-02-03 06:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0013_auto_20200203_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 3, 6, 50, 34, 377379, tzinfo=utc)),
        ),
    ]

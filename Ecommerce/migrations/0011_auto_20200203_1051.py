# Generated by Django 2.2.7 on 2020-02-03 05:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0010_auto_20200203_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 3, 5, 21, 42, 201921, tzinfo=utc)),
        ),
    ]

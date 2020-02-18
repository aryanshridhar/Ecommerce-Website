# Generated by Django 2.2.7 on 2020-02-14 09:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0018_auto_20200214_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 9, 57, 34, 86406, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-25 16:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0024_auto_20200215_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 25, 16, 37, 49, 551882, tzinfo=utc)),
        ),
    ]

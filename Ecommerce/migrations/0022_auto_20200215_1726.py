# Generated by Django 2.2.7 on 2020-02-15 11:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0021_auto_20200215_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 15, 11, 56, 30, 165554, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.2 on 2022-08-22 01:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 1, 21, 0, 120588, tzinfo=utc), verbose_name='created time'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 1, 21, 0, 120588, tzinfo=utc), verbose_name='created time'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 1, 21, 0, 120588, tzinfo=utc), verbose_name='created time'),
        ),
    ]
# Generated by Django 2.2 on 2022-08-22 01:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_auto_20220822_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomments',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 1, 21, 0, 120588, tzinfo=utc), verbose_name='created time'),
        ),
        migrations.AlterField(
            model_name='userask',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 1, 21, 0, 120588, tzinfo=utc), verbose_name='created time'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 1, 21, 0, 120588, tzinfo=utc), verbose_name='created time'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 1, 21, 0, 120588, tzinfo=utc), verbose_name='created time'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 1, 21, 0, 120588, tzinfo=utc), verbose_name='created time'),
        ),
    ]

# Generated by Django 2.2 on 2022-08-13 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='avatar/%Y/%m', verbose_name='avatar'),
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-23 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20200423_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='admin_profile_images'),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='registrated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='customer_profile_images'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registrated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='mybug',
            name='buy_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
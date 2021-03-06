# Generated by Django 3.0.4 on 2020-04-23 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_administrator_customer_mybug_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mybug',
            name='name',
        ),
        migrations.AddField(
            model_name='mybug',
            name='buy_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='registrated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registrated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='quanity',
            field=models.IntegerField(default=0),
        ),
    ]

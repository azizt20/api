# Generated by Django 3.2.4 on 2021-07-23 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='count_day',
        ),
        migrations.RemoveField(
            model_name='order_waiting',
            name='count_day',
        ),
    ]

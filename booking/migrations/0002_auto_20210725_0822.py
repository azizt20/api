# Generated by Django 3.2.4 on 2021-07-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_waiting',
            name='finish_date',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='order_waiting',
            name='start_date',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

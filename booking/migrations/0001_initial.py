# Generated by Django 3.2.4 on 2021-07-13 07:09

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(verbose_name=models.CharField(blank=True, max_length=50))),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('slug', models.SlugField(verbose_name=models.IntegerField())),
                ('description', models.CharField(max_length=200)),
                ('bed_count', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('cost_per_day', models.IntegerField()),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name=builtins.id)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('count_day', models.IntegerField()),
                ('order_cost', models.IntegerField()),
                ('user_name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busy', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.order')),
            ],
        ),
    ]

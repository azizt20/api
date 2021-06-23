# Generated by Django 3.2.4 on 2021-06-23 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('bed_count', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('cost_per_day', models.IntegerField()),
                ('typeroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.typeroom')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('count_day', models.IntegerField()),
                ('order_cost', models.IntegerField()),
                ('user_name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.date')),
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
        migrations.AddField(
            model_name='date',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room'),
        ),
    ]
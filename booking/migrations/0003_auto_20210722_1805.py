# Generated by Django 3.2.4 on 2021-07-22 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20210713_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='booking.room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='booking.roomtype'),
        ),
    ]
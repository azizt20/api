# Generated by Django 3.2.4 on 2021-06-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_typeroom_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
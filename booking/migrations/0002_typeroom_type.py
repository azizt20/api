# Generated by Django 3.2.4 on 2021-06-23 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeroom',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
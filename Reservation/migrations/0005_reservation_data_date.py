# Generated by Django 2.2.1 on 2019-06-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0004_auto_20190611_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation_data',
            name='Date',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0002_auto_20190607_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation_data',
            name='Time',
            field=models.IntegerField(blank=True, choices=[(1, '점심'), (2, '저녁')], default=1),
        ),
    ]

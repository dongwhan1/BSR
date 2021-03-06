# Generated by Django 2.2.1 on 2019-06-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0003_auto_20190611_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation_data',
            name='Place',
            field=models.IntegerField(choices=[(1, '농구(왼)'), (2, '농구(오)'), (3, '축구'), (4, '풋살'), (5, '배구(왼)'), (6, '배구(오)')], default=1),
        ),
        migrations.AlterField(
            model_name='reservation_data',
            name='Time',
            field=models.IntegerField(choices=[(1, '점심'), (2, '저녁')], default=1),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-06 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation_data',
            old_name='Reason',
            new_name='Time',
        ),
    ]
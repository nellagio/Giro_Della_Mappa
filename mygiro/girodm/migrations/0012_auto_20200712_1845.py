# Generated by Django 3.0.6 on 2020-07-13 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('girodm', '0011_ride_times_click'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='times_click',
            new_name='times_clicked',
        ),
    ]

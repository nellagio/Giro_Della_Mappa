# Generated by Django 3.0.6 on 2020-07-07 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girodm', '0007_auto_20200704_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='pace',
        ),
        migrations.AddField(
            model_name='ride',
            name='end_lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='end_long',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='ride_pace',
            field=models.CharField(choices=[('sl', '3-8 mph'), ('md', '9-12 mph'), ('fs', '13-17 mph'), ('tf', '18+ mph')], default='md', max_length=200),
        ),
        migrations.AddField(
            model_name='ride',
            name='ride_type',
            field=models.CharField(choices=[('ff', 'Family Friendly'), ('ep', 'Social (18/21+)'), ('tp', 'Training Pace'), ('sp', 'Special Event')], default='ff', max_length=200),
        ),
        migrations.AddField(
            model_name='ride',
            name='start_lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='start_long',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]
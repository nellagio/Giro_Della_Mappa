# Generated by Django 3.0.6 on 2020-07-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girodm', '0009_auto_20200706_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='end_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='end_long',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='start_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='start_long',
            field=models.FloatField(null=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='time_on_zillow',
            field=models.CharField(max_length=255),
        ),
    ]

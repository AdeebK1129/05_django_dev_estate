# Generated by Django 5.0.1 on 2024-01-20 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_property_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='image_url',
            new_name='imgSrc',
        ),
    ]

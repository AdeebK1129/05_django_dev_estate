# Generated by Django 5.0.1 on 2024-01-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_remove_nearbyhomes_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearbyhomes',
            name='street_address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

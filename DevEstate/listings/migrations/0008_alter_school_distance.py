# Generated by Django 5.0.1 on 2024-01-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_alter_school_distance_alter_school_grades_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='distance',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

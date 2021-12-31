# Generated by Django 4.0 on 2021-12-30 08:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_vehicle_data_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle_data',
            name='Date',
        ),
        migrations.AddField(
            model_name='vehicle_data',
            name='vehicle_arrived_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

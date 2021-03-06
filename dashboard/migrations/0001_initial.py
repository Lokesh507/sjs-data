# Generated by Django 4.0 on 2021-12-30 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='total_income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodywash_income', models.IntegerField(default=0)),
                ('fullwash_income', models.IntegerField(default=0)),
                ('jcb_income', models.IntegerField(default=0)),
                ('crane_income', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_counts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodywash_count', models.IntegerField(default=0)),
                ('fullwash_count', models.IntegerField(default=0)),
                ('jcb_count', models.IntegerField(default=0)),
                ('crane_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100)),
                ('vehicle_wash', models.CharField(max_length=50)),
                ('vehicle_amount', models.CharField(max_length=50)),
                ('payment_type', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0011_booking_table_checked_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_table',
            name='data',
            field=models.CharField(max_length=10),
        ),
    ]

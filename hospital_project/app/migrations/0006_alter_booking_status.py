# Generated by Django 3.2.23 on 2024-11-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approve', 'Approve'), ('Reject', 'Reject')], default='pending', max_length=100, null=True),
        ),
    ]

# Generated by Django 3.2.25 on 2024-07-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_booking_departments_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

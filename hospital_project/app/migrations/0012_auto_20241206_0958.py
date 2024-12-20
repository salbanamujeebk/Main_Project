# Generated by Django 3.2.23 on 2024-12-06 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientconsultation',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='patientconsultation',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

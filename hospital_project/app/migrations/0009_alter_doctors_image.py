# Generated by Django 3.2.23 on 2024-11-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_patientconsultation_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

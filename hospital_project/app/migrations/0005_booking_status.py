# Generated by Django 3.2.23 on 2024-11-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_patientconsultation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

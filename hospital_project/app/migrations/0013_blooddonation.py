# Generated by Django 3.2.23 on 2024-12-12 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20241206_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField()),
                ('blood_group', models.CharField(max_length=5)),
                ('weight', models.FloatField()),
                ('medication', models.CharField(max_length=10)),
                ('donated_before', models.CharField(max_length=10)),
                ('medical_condition', models.CharField(max_length=10)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

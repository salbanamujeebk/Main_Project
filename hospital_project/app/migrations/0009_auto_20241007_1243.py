# Generated by Django 3.2.23 on 2024-10-07 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_doctors_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='PatientConsultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=100)),
                ('condition', models.TextField()),
                ('medicine', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

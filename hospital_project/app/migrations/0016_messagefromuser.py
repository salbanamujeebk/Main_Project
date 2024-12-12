# Generated by Django 3.2.23 on 2024-12-12 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_delete_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messagefromuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

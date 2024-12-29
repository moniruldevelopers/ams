# Generated by Django 5.1.4 on 2024-12-29 16:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0002_facebookpage_remove_programinfo_max_participants_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='invalid_phone', message='Enter a valid Bangladesh phone number (e.g., 01712345678).', regex='^01[3-9]\\d{8}$')])),
                ('email', models.EmailField(max_length=254)),
                ('institute_name', models.CharField(max_length=100)),
                ('class_level', models.CharField(choices=[('Class 5', 'Class 5'), ('Class 6', 'Class 6'), ('Class 7', 'Class 7'), ('Class 8', 'Class 8'), ('Class 9', 'Class 9'), ('Class 10', 'Class 10'), ('Class 11', 'Class 11'), ('Class 12', 'Class 12'), ('University', 'University')], max_length=20)),
            ],
        ),
    ]

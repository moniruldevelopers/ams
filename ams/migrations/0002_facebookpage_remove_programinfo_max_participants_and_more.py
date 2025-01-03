# Generated by Django 5.1.4 on 2024-12-29 16:13

import ckeditor.fields
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='programinfo',
            name='max_participants',
        ),
        migrations.RemoveField(
            model_name='programinfo',
            name='program_date',
        ),
        migrations.RemoveField(
            model_name='programinfo',
            name='program_end_date',
        ),
        migrations.AddField(
            model_name='participansinfo',
            name='class_level',
            field=models.CharField(choices=[('Class 5', 'Class 5'), ('Class 6', 'Class 6'), ('Class 7', 'Class 7'), ('Class 8', 'Class 8'), ('Class 9', 'Class 9'), ('Class 10', 'Class 10'), ('Class 11', 'Class 11'), ('Class 12', 'Class 12'), ('University', 'University')], default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programinfo',
            name='program_datetime',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participansinfo',
            name='whatsapp',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='invalid_phone', message='Enter a valid Bangladesh phone number (e.g., 01712345678).', regex='^01[3-9]\\d{8}$')]),
        ),
        migrations.AlterField(
            model_name='programinfo',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.CreateModel(
            name='ExportLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('export_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='export_logs', to='ams.programinfo')),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0006_delete_trashbin'),
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
    ]

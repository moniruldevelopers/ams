# Generated by Django 5.1.4 on 2024-12-24 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0005_trashbin_exportlog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrashBin',
        ),
    ]
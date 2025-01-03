# Generated by Django 5.1.4 on 2024-12-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0003_intereststudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=20)),
                ('site_logo', models.ImageField(upload_to='logo/')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('address', models.CharField(max_length=100)),
                ('site_facebook', models.URLField(max_length=100)),
                ('site_x', models.URLField(max_length=100)),
                ('site_instagram', models.URLField(max_length=100)),
                ('site_pinterest', models.URLField(max_length=100)),
            ],
        ),
    ]

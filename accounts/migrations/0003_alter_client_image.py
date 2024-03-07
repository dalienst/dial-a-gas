# Generated by Django 5.0.1 on 2024-03-07 10:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_vendor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Buyer Image'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_shop_image_category_delivery_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='delivery',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='a nice product for sale'),
            preserve_default=False,
        ),
    ]

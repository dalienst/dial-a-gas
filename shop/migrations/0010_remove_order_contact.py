# Generated by Django 5.0.1 on 2024-03-07 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_order_location_alter_order_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='contact',
        ),
    ]

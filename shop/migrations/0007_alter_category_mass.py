# Generated by Django 5.0.1 on 2024-03-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_category_mass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='mass',
            field=models.CharField(blank=True, choices=[('6kg', 'Small - 6kg'), ('13kg', 'Medium - 13kg'), ('26kg', 'Large - 26kg')], max_length=100, null=True),
        ),
    ]
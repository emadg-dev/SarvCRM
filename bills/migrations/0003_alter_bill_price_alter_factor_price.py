# Generated by Django 4.2 on 2024-10-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_rename_number_factor_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=16),
        ),
        migrations.AlterField(
            model_name='factor',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=16),
        ),
    ]
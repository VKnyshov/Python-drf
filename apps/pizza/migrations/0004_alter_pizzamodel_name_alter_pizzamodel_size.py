# Generated by Django 5.1.4 on 2024-12-19 06:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_pizzamodel_day_alter_pizzamodel_pizza_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzamodel',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z][a-z]{,19}$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='pizzamodel',
            name='size',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]

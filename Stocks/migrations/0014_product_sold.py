# Generated by Django 5.0.1 on 2024-03-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0013_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

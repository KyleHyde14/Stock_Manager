# Generated by Django 4.2.3 on 2023-10-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0004_store_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-28 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0010_rename_owner_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='total',
        ),
    ]

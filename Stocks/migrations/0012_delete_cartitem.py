# Generated by Django 5.0.1 on 2024-02-29 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0011_remove_cartitem_total'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
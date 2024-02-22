# Generated by Django 5.0.1 on 2024-02-14 21:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0008_alter_product_description_alter_product_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stocks.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stocks.product')),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-10-07 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Stocks', '0003_alter_amount_of_product_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
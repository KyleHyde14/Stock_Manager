# Generated by Django 4.2.3 on 2023-08-12 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='amount_of_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(through='Stocks.amount_of_product', to='Stocks.product')),
                ('store', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Stocks.store')),
            ],
        ),
        migrations.AddField(
            model_name='amount_of_product',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stocks.product'),
        ),
        migrations.AddField(
            model_name='amount_of_product',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stocks.stock'),
        ),
    ]

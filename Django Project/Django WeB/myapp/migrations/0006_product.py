# Generated by Django 4.0.3 on 2022-04-19 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.PositiveIntegerField()),
                ('product_image', models.ImageField(default='images/default.jpg', upload_to='images/products/')),
                ('desc', models.TextField(blank=True, null=True)),
                ('stock', models.PositiveIntegerField(default=1)),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.seller')),
            ],
        ),
    ]

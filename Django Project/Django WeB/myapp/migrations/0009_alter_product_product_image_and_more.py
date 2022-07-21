# Generated by Django 4.0.3 on 2022-04-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='images/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]
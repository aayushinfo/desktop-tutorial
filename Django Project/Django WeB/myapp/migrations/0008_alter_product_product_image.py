# Generated by Django 4.0.3 on 2022-04-26 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='https://tse2.mm.bing.net/th?id=OIP.jtzLV8nbTiaPVkbonKgPJAHaDk&pid=Api&P=0&w=336&h=162', upload_to='images/products/'),
        ),
    ]

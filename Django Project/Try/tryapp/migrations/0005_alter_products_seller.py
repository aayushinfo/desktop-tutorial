# Generated by Django 4.0.6 on 2022-07-12 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tryapp', '0004_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tryapp.seller'),
        ),
    ]
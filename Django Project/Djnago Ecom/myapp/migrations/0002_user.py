# Generated by Django 4.0.3 on 2022-05-18 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField(max_length=100)),
                ('lname', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.TextField(max_length=100)),
                ('password', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
            ],
        ),
    ]
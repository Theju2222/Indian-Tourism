# Generated by Django 4.0.3 on 2022-05-18 09:03

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Image')),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]

# Generated by Django 3.2 on 2022-03-29 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_reviewrating_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]

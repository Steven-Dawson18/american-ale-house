# Generated by Django 3.2 on 2022-03-30 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_rating',
            field=models.FloatField(default=5),
        ),
    ]
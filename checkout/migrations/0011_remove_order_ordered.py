# Generated by Django 3.2 on 2022-04-03 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_order_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
    ]
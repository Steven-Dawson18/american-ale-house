# Generated by Django 3.2 on 2022-05-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_reviewrating_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
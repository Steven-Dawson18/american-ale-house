# Generated by Django 3.2 on 2022-03-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_reviewrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.0.2 on 2022-05-18 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('womenwear', '0021_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='customer',
        ),
    ]

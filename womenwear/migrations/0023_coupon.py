# Generated by Django 4.0.2 on 2022-05-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenwear', '0022_remove_wishlist_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.CharField(max_length=15)),
                ('discount', models.IntegerField(default=0)),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2022-05-05 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenwear', '0013_product_table_img8'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_table',
            name='print',
            field=models.CharField(default='', max_length=200),
        ),
    ]

# Generated by Django 4.0.2 on 2022-06-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenwear', '0027_rename_payment_id_orderplaced_razorpay_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_table',
            name='img8',
            field=models.ImageField(blank=True, default='', upload_to='img'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-06-02 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('womenwear', '0025_remove_orderplaced_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='amount',
            new_name='Total_price',
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='payment_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='payment_mode',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='tracking_no',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='oderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='womenwear.orderplaced')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='womenwear.product_table')),
            ],
        ),
    ]

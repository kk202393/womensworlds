# Generated by Django 4.0.2 on 2022-04-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenwear', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dest',
            name='actual_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dest',
            name='disscunt',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dest',
            name='sell_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

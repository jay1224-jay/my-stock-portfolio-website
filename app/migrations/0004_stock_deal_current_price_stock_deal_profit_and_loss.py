# Generated by Django 4.1 on 2022-08-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_stock_deal_current_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_deal',
            name='current_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock_deal',
            name='profit_and_loss',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 4.1 on 2022-08-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_deal',
            name='company_name',
            field=models.CharField(default='null', max_length=6),
        ),
        migrations.AlterField(
            model_name='stock_deal',
            name='company_code',
            field=models.CharField(default='null', max_length=15),
        ),
    ]

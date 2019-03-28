# Generated by Django 2.1.7 on 2019-03-28 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_monitor', '0002_auto_20190327_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock_status',
        ),
        migrations.AddField(
            model_name='product',
            name='instock',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_customer_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]

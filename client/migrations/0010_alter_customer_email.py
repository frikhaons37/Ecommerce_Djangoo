# Generated by Django 5.0.2 on 2024-04-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-14 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0010_produit_imgh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('clothes', 'Clothes'), ('footwear', 'Footwear'), ('jewerly', 'Jewerly'), ('perfume', 'Perfume'), ('cosmetics', 'Cosmetics'), ('glasses', 'Glasses'), ('bags', 'Bags')], default='clothes', max_length=50),
        ),
    ]

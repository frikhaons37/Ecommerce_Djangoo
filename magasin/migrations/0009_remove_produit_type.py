# Generated by Django 5.0.2 on 2024-03-07 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0008_alter_categorie_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='type',
        ),
    ]

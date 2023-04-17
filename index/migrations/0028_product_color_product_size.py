# Generated by Django 4.1.7 on 2023-04-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0027_alter_carrinho_car_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='Cor', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('pp', 'pp'), ('p', 'p'), ('m', 'm'), ('g', 'g'), ('gg', 'gg'), ('xgg', 'xgg')], default='Tamanho', max_length=3),
        ),
    ]
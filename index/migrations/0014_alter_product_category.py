# Generated by Django 4.1.5 on 2023-03-10 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_review_person_product_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Eletrodoméstico', 'Eletrodoméstico'), ('Beleza', 'Beleza'), ('Acessórios', 'Acessórios'), ('Roupas', 'Roupas'), ('Fantasias', 'Fantasias'), ('Computador', 'Computador')], default='Categoria', max_length=20),
        ),
    ]

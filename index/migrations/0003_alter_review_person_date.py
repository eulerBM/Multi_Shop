# Generated by Django 4.1.5 on 2023-03-09 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_product_review_alter_review_person_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_person',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 3, 8, 23, 13, 19, 12590)),
        ),
    ]

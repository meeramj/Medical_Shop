# Generated by Django 3.2.13 on 2022-06-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medshop', '0002_remove_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-02 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
    ]

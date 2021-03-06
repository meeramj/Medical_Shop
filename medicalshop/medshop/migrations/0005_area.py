# Generated by Django 3.2.13 on 2022-06-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medshop', '0004_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]

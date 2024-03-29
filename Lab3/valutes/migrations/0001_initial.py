# Generated by Django 5.0.2 on 2024-03-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parse_code', models.CharField(max_length=10, verbose_name='ParseCode')),
                ('num_code', models.CharField(max_length=10, verbose_name='NumCode')),
                ('char_code', models.CharField(max_length=10, verbose_name='Код валюты')),
                ('nominal', models.IntegerField(default=1, verbose_name='Номинал')),
                ('сurrency_name', models.CharField(max_length=20, verbose_name='Название')),
            ],
        ),
    ]

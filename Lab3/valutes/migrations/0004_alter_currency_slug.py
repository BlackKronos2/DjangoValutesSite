# Generated by Django 5.0.2 on 2024-03-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valutes', '0003_alter_currency_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='slug',
            field=models.SlugField(verbose_name='URL'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valutes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
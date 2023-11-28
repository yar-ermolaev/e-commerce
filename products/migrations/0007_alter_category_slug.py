# Generated by Django 4.2.7 on 2023-11-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='URL'),
        ),
    ]
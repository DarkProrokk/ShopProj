# Generated by Django 4.1.7 on 2023-06-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0003_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]

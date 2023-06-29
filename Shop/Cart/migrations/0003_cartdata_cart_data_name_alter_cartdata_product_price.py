# Generated by Django 4.1.7 on 2023-06-29 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_alter_cart_cart_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdata',
            name='cart_data_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartdata',
            name='product_price',
            field=models.FloatField(blank=True, default=0),
        ),
    ]

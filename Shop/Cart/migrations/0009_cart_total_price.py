# Generated by Django 4.1.7 on 2023-06-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0008_alter_order_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

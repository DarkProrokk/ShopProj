# Generated by Django 4.1.7 on 2023-06-29 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
        ('Person', '0006_customuser_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_cart',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='Cart.cart'),
            preserve_default=False,
        ),
    ]

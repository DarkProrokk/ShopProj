# Generated by Django 4.1.7 on 2023-06-28 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0009_alter_maincategory_childcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maincategory',
            name='childCategory',
        ),
        migrations.AddField(
            model_name='childcategory',
            name='mainCat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Catalog.maincategory'),
        ),
    ]

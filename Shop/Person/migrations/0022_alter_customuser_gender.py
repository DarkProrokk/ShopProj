# Generated by Django 4.1.7 on 2023-06-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0021_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('F', 'Женщина'), ('M', 'Мужчина')], default='', max_length=20),
        ),
    ]

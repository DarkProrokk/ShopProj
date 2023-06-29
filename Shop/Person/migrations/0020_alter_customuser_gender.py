# Generated by Django 4.1.7 on 2023-06-29 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0019_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('F', 'Женщина'), ('M', 'Мужчина')], default='', max_length=20),
        ),
    ]

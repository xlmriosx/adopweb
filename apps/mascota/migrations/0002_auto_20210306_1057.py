# Generated by Django 3.1 on 2021-03-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(choices=[('hembra', 'Hembra'), ('macho', 'Macho')], default='macho', max_length=6),
        ),
    ]
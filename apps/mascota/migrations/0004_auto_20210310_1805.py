# Generated by Django 3.1 on 2021-03-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_mascota_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(choices=[('Hembra', 'Hembra'), ('Macho', 'Macho')], default='Macho', max_length=6),
        ),
    ]

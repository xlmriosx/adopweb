# Generated by Django 3.1 on 2021-03-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_denuncia_caratula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='numero',
            field=models.IntegerField(default=3624),
        ),
    ]

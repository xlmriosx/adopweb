# Generated by Django 3.1 on 2021-03-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0002_auto_20210306_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='adopcion',
            name='fechaPub',
            field=models.DateField(auto_now=True, verbose_name='Fecha del día de hoy'),
        ),
    ]

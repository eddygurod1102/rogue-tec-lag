# Generated by Django 4.2.1 on 2023-06-06 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaproducto',
            name='cantidad',
            field=models.SmallIntegerField(default=0, verbose_name='Cantidad'),
        ),
    ]

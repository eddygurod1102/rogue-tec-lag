# Generated by Django 4.2.1 on 2023-06-04 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gimnasio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fotografia',
            field=models.FileField(upload_to='categorias'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fotografia',
            field=models.FileField(upload_to='productos'),
        ),
    ]
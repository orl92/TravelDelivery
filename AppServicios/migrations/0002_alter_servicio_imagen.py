# Generated by Django 3.2.10 on 2021-12-19 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppServicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='AppServicios'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-10-30 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_oferta_nombre_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='Nombre_empresa',
            field=models.CharField(max_length=45, null=True),
        ),
    ]

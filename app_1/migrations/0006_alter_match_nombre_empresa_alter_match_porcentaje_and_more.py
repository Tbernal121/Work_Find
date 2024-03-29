# Generated by Django 4.0.6 on 2022-11-24 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_alter_empresa_id_empresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='Nombre_empresa',
            field=models.CharField(default='Coca-Cola', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='porcentaje',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='match',
            name='tipo_match',
            field=models.CharField(choices=[('Perfecto', 'Perfecto'), ('Muy bueno', 'Muy bueno'), ('Bueno', 'Bueno'), ('Medio', 'Medio')], default='Perfecto', max_length=45, null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-23 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0012_habilidad1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='archivos/')),
            ],
        ),
        migrations.DeleteModel(
            name='Habilidad',
        ),
    ]

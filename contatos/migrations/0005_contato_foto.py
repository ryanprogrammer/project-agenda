# Generated by Django 4.0.1 on 2022-01-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_contato_ocultar_alter_contato_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='Fotos/%Y/%M/'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-21 19:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_alter_contato_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='ocultar',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 5.0.6 on 2024-09-01 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filiados', '0003_alter_filiado_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filiado',
            name='genero',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

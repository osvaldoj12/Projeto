# Generated by Django 2.2.6 on 2019-11-26 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ouvidoria', '0002_auto_20191126_1426'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RelatorioFuncionario',
        ),
        migrations.DeleteModel(
            name='RelatorioOuvidoria',
        ),
    ]

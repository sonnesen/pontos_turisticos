# Generated by Django 2.0.5 on 2018-05-16 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='longitute',
            new_name='longitude',
        ),
    ]

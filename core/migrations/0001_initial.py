# Generated by Django 2.0.5 on 2018-05-16 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comentarios', '0001_initial'),
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('aprovado', models.BooleanField(default=False)),
                ('atracoes', models.ManyToManyField(to='atracoes.Atracao')),
                ('comentarios', models.ManyToManyField(to='comentarios.Comentario')),
            ],
        ),
    ]
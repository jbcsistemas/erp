# Generated by Django 3.2.11 on 2022-01-27 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('descricao', models.TextField(max_length=90, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barras', models.CharField(max_length=14, unique=True, verbose_name='Código de barras')),
                ('nome', models.CharField(max_length=40)),
                ('descricacao', models.TextField(blank=True, max_length=100, null=True)),
                ('custo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('fabricante', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=20)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('disponivel', models.BooleanField(default=True, verbose_name='Disponível')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.categoria')),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
    ]

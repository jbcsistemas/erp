# Generated by Django 3.2.11 on 2022-03-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0003_auto_20220323_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='rg',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
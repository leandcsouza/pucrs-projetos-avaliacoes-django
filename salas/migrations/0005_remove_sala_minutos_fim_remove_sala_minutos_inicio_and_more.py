# Generated by Django 4.1.9 on 2024-01-16 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0004_rename_ativo_sala_ativa_sala_hora_fim_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sala',
            name='minutos_fim',
        ),
        migrations.RemoveField(
            model_name='sala',
            name='minutos_inicio',
        ),
        migrations.AddField(
            model_name='sala',
            name='minutos_disponiveis',
            field=models.PositiveIntegerField(default=60),
        ),
        migrations.AddField(
            model_name='sala',
            name='reservada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sala',
            name='hora_inicio',
            field=models.TimeField(default='09:00'),
        ),
    ]

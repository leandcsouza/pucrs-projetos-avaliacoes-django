# Generated by Django 4.1.9 on 2024-01-16 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0006_horariodisponivel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sala',
            old_name='minutos_disponiveis',
            new_name='duracao_reserva',
        ),
    ]

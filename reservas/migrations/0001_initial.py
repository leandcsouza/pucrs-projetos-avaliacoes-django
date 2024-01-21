# Generated by Django 4.1.9 on 2024-01-16 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinicas', '0003_rename_status_clinica_ativo'),
        ('salas', '0005_remove_sala_minutos_fim_remove_sala_minutos_inicio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profissional_nome', models.CharField(max_length=255)),
                ('status_pagamento', models.BooleanField(default=False)),
                ('clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicas.clinica')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salas.sala')),
            ],
        ),
    ]

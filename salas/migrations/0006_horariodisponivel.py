# Generated by Django 4.1.9 on 2024-01-16 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0005_remove_sala_minutos_fim_remove_sala_minutos_inicio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorarioDisponivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fim', models.TimeField()),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salas.sala')),
            ],
        ),
    ]


from django.db import models
from salas.models import Sala
from clinicas.models import Clinica


class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    horario_disponivel = models.ForeignKey(
        'salas.HorarioDisponivel', on_delete=models.CASCADE, default=0)
    profissional_nome = models.CharField(max_length=255)
    status_pagamento = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if (self.horario_disponivel.hora_fim.hour * 60 + self.horario_disponivel.hora_fim.minute) - \
                (self.horario_disponivel.hora_inicio.hour * 60 + self.horario_disponivel.hora_inicio.minute) < 60:
            raise ValueError(
                "A sala deve ter pelo menos 60 minutos disponíveis para reserva.")

        if self.horario_disponivel.sala.minutos_disponiveis < 60:
            raise ValueError(
                "A sala não tem minutos suficientes disponíveis para uma reserva de 60 minutos.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.profissional_nome} - {self.sala} - {self.horario_disponivel.data} {self.horario_disponivel.hora_inicio}-{self.horario_disponivel.hora_fim}'

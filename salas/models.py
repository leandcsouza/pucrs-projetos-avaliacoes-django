from django.db import models

from datetime import timedelta
from clinicas.models import Clinica
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import timedelta


class Sala(models.Model):
    nome = models.CharField(max_length=255)
    capacidade = models.IntegerField()
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    ativa = models.BooleanField(default=True)

    hora_inicio = models.TimeField(default='09:00')
    hora_fim = models.TimeField(default='18:00')

    duracao_reserva = models.PositiveIntegerField(default=60)

    reservada = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nome} - {self.clinica.nome} - {self.hora_inicio} to {self.hora_fim} ({self.duracao_reserva} duração do periodo)'


class HorarioDisponivel(models.Model):
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def clean(self):
        # Verifica se a diferença entre hora_inicio e hora_fim é no mínimo igual a duracao_reserva
        diferenca_em_minutos = (self.hora_fim.hour * 60 + self.hora_fim.minute) - \
                               (self.hora_inicio.hour *
                                60 + self.hora_inicio.minute)

        if diferenca_em_minutos < self.sala.duracao_reserva:
            raise ValidationError(
                _('A diferença entre hora_inicio e hora_fim deve ser no mínimo igual a duracao_reserva da Sala '
                  f'({self.sala.duracao_reserva} minutos). Atualmente, a diferença é de {diferenca_em_minutos} minutos.')
            )

        # Verifica se a quantidade de minutos está dentro do período compatível da Sala
        if diferenca_em_minutos > self.sala.duracao_reserva:
            raise ValidationError(
                _('A quantidade de minutos no HorarioDisponivel deve estar dentro do período compatível da Sala.')
            )

        # Verifica se não existe outro HorarioDisponivel na mesma hora solicitada
        conflitos = HorarioDisponivel.objects.filter(
            sala=self.sala,
            data=self.data,
            hora_inicio__lt=self.hora_fim,
            hora_fim__gt=self.hora_inicio,
        )

        if conflitos.exists():
            raise ValidationError(
                _('Já existe um HorarioDisponivel para esta Sala nesta hora solicitada.')
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.sala} - {self.data} {self.hora_inicio}-{self.hora_fim}'

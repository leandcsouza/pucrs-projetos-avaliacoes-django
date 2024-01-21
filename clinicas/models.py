# gerenciamento_clinicas/models.py

from django.db import models


class Clinica(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.TextField()
    contato = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

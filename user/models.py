from django.db import models
from django import forms

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class PersonDetail(models.Model):
    Parto = (
        ('Simples','Simples'),
        ('Duplo','Duplo'),
        ('Triplo','Triplo')
    )
    Habilidade = (
        ('Bom','Bom'),
        ('Regular','Regular'),
        ('Ruim','Ruim')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="new_spending", null=True)
    matriz = models.CharField(max_length=20, help_text = "Informe o nome da matriz")
    reprodutor = models.CharField(max_length=20, help_text = "Informe o nome do reprodutor")
    parto = models.CharField(max_length=10,choices=Parto)
    data_de_nascimento = models.DateField(verbose_name = "Data de parição", help_text = "Por favor use o formato: <em>DD/MM/AAAA</em>.")
    habilidade_materna = models.CharField(max_length=10,choices=Habilidade)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.user)
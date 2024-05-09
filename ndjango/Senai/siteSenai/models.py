from django.db import models
from datetime import datetime

# Create your models here.

class Trabalhadores(models.Model):
    nome_trab = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    fone = models.CharField(max_length=12)
    data_nasc = models.DateTimeField(blank=True)
    endereco = models.TextField()
    email = models.EmailField(max_length=70)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    

    


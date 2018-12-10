from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=128)


class Modelo(models.Model):
    nome = models.CharField(max_length=128)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)


class Configuracao(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cor = models.CharField(max_length=128)
    cordas = models.IntegerField()
    ano = models.IntegerField()


class Guitarra(models.Model):
    configuracao = models.ForeignKey(Configuracao, on_delete=models.CASCADE)
    dono = models.CharField(max_length=128)

from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import *

    

class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    numero_sus = models.CharField(max_length=15, unique=True, blank=False, null=False)
    data_nascimento = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.username}'
    
class Posto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do posto")
    endereco = models.CharField(max_length=100, verbose_name="Endereço do posto")
    telefone = models.CharField(max_length=100, verbose_name="Telefone do posto")

    class Meta:
        verbose_name_plural = "Postos de Saúde"

    def __str__(self):
        return f'{self.nome} {self.endereco} {self.telefone}'

class Area(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da area")

    class Meta:
        verbose_name_plural = "Areas de Atuação"

    def __str__(self):
        return f'{self.nome}'
    
class Medico(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do medico")
    area = models.ForeignKey('Area', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Medicos"

    def __str__(self):
        return f'{self.nome} {self.area}'

class Consulta(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    posto = models.ForeignKey('Posto', on_delete=models.CASCADE)
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    observacao = models.TextField()

    class Meta:
        verbose_name_plural = "Consultas"
    
    def __str__(self):
        return f'{self.user}'












class Sobre(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Index(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo
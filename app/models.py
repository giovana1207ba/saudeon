from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import *



# class Register(models.Model):

#     nome = models.CharField(max_length=+100, verbose_name="Nome da register")
#     cpf = models.CharField(max_length=+100, verbose_name="CPF")
#     num_sus = models.CharField(max_length=+100, verbose_name="Númro do SUS")
#     telefone = models.CharField(max_length=+100, verbose_name="Númro de telefone")
#     email = models.CharField(max_length=+100, verbose_name="Crie um email")
#     senha= models.CharField(max_length=+100, verbose_name="Crie uma senha")
    
#     class Meta:
#         verbose_name_plural = "Register"

#     def __str__(self):
#         return f'{self.nome} {self.cpf} {self.num_sus} {self.telefone} {self.email} {self.senha}'
    

class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    numero_sus = models.CharField(max_length=15, unique=True, blank=False, null=False)
    data_nascimento = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.username}'


class Consulta(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user


class Sobre(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo






# class Login(models.Model):
#     usuario = models.CharField(max_length=150)
#     senha = models.CharField(max_length=128)  # Para segurança, você pode usar hashing
#     email = models.EmailField()

#     def __str__(self):
#         return self.usuario







class Index(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo


class Posto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do posto")
    endereco = models.CharField(max_length=100, verbose_name="Endereço do posto")
    telefone = models.CharField(max_length=100, verbose_name="Telefone do posto")

    class Meta:
        verbose_name_plural = "Posto"

    def __str__(self):
        return f'{self.nome} {self.endereco} {self.telefone}' 
    

class Area(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da area")

    class Meta:
        verbose_name_plural = "Area"

    def __str__(self):
        return f'{self.nome}'
    

class Medico(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do medico")
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Medico"

    def __str__(self):
        return f'{self.nome} {self.area} '

    
    

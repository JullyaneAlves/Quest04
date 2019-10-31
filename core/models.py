from django.db import models
from django.core.validators import RegexValidator

from django.contrib import admin

class Colecao(models.Model):
        class Meta:
                verbose_name_plural = "Coleções"

        nome = models.CharField('Nome', max_length=30)

        def __str__(self):
            return self.nome

class Caixa(models.Model):
        class Meta:
              verbose_name_plural = "Caixas"

        numero = models.IntegerField('Número')
        etiqueta = models.CharField('Etiqueta', max_length=20)
        cor = models.CharField('Cor', max_length=12)
        ano = models.IntegerField('Ano')

class Revista(models.Model):
        class Meta:
              verbose_name_plural = "Revistas"

        numero = models.IntegerField('Número de Edição')
        ano = models.IntegerField('Ano')
        colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
        caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)

class GrupoAmigo(models.Model):
        class Meta:
                verbose_name_plural = "Grupo de Amigos"

        nome = models.CharField('Nome', max_length=10)

        def __str__(self):
            return self.nome

class Amigo(models.Model):
        class Meta:
                verbose_name_plural = "Amigo"

        nome = models.CharField('Nome', max_length=20)
        nome_mae = models.CharField('Nome da Mãe', max_length=30)
        fone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        fone = models.CharField(validators=[fone_regex], max_length=17, blank=True) # validators should be a list
        grupo_amigo = models.ForeignKey(GrupoAmigo, on_delete=models.CASCADE)

        def __str__(self):
            return self.nome


class Emprestimo(models.Model):

        dataemp = models.DateField('Data do emprestimo')
        datadev = models.DateField('Data de devolução')
        amigo = models.ForeignKey(Amigo, on_delete=models.CASCADE)
        revista = models.ForeignKey(Revista, on_delete=models.CASCADE)


        class Meta:
                verbose_name_plural = "Emprestimos"
                ordering = ('-dataemp', 'revista')

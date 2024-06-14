from django.db import models
from django.utils import timezone

class Filiado(models.Model):
    tituloEleitor = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    dataFiliacao = models.DateTimeField()
    uf = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    zona = models.IntegerField()
    situacao = models.CharField(max_length=30)
    pendenciaComunicacao = models.BooleanField(default=False)
    nome_completo = models.CharField(max_length=300)
    nome_social = models.CharField(max_length=300)
    data_nascimento = models.DateTimeField(null=True, blank=True)
    sexualidade = models.CharField(max_length=50, null=True, blank=True)
    raca = models.CharField(max_length=50, null=True, blank=True)
    pcd = models.BooleanField(default=False)
    local_residencia = models.CharField(max_length=50, null=True, blank=True)
    local_exercicio = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome_completo

class SituacaoFiliacao(models.TextChoices):
    REGULAR = 'REGULAR', 'Regular'
    NAO_REGULAR = 'NAO_REGULAR', 'Não Regular'

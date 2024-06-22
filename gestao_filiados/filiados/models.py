from django.db import models
from django.utils import timezone
from tse_importador.up.entidades.filiados import filiado_up as filiado_up
from paprika import to_string

@to_string
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


    def instanciar(self, filiado: filiado_up) :
        self.tituloEleitor = filiado.tituloEleitor
        self.nome = filiado.nome_completo
        self.genero = filiado.genero
        self.dataFiliacao = filiado.dataFiliacao
        self.uf = filiado.uf
        self.municipio = filiado.local_residencia
        self.zona = filiado.zona
        self.situacao = filiado.situacao
        self.pendenciaComunicacao = filiado.pendenciaComunicacao
        self.nome_completo = filiado.nome_completo
        self.nome_social = filiado.nome_social
        self.data_nascimento = filiado.data_nascimento
        self.sexo = filiado.genero
        self.raca = filiado.raca
        self.sexualidade = filiado.sexualidade
        self.pcd = filiado.pcd
        self.local_residencia = filiado.local_residencia
        self.local_exercicio = filiado.local_exercicio
        return self
    
    def retornar_entidade_negocio(self) -> filiado_up:
        return filiado_up(
            tituloEleitor=self.tituloEleitor,
            nome_completo=self.nome_completo,
            nome_social=self.nome_social,
            data_nascimento=self.data_nascimento,
            genero=self.genero,
            sexualidade=self.sexualidade,
            raca=self.raca,
            pcd=self.pcd,
            local_residencia=self.local_residencia,
            local_exercicio=self.local_exercicio,
            dataFiliacao=self.dataFiliacao,
            uf=self.uf,
            zona=self.zona,
            situacao=self.situacao,
            pendenciaComunicacao=self.pendenciaComunicacao
        )

class SituacaoFiliacao(models.TextChoices):
    REGULAR = 'REGULAR', 'Regular'
    NAO_REGULAR = 'NAO_REGULAR', 'Não Regular'

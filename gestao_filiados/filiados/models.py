from django.db import models
from django.utils import timezone
from tse_importador.up.entidades.filiado_up import filiado_up as filiado_up
from paprika import to_string

@to_string
class Filiado(models.Model):
    tituloEleitor = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    dataFiliacao = models.DateTimeField()
    uf = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50, null=True,default='Desconhecido')
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

    # Dados extras vindo da planilha central da UP
    secao = models.IntegerField(null=True, blank=True)
    cpf = models.CharField(null= True, max_length=50)
    cep = models.CharField(null= True, max_length=50)
    rg = models.CharField(null= True, max_length=50)
    genero = models.CharField(null= True, max_length=50)
    endereco_residencial = models.CharField(null= True, max_length=50)
    nome_mae = models.CharField(null= True, max_length=50)
    ocupacao = models.CharField(null= True, max_length=50)
    telefoneComDDD= models.CharField(null= True, max_length=50)
    whatsAppComDDD= models.CharField(null= True, max_length=50)
    email= models.CharField(null= True, max_length=50)
    data_inscricao= models.DateTimeField(null=True, blank=True)
    data_atualizacao= models.DateTimeField(null=True, blank=True)
    municipio_onde_vota= models.CharField(null= True, max_length=50)
    reponsavelFiliacao= models.CharField(null= True, max_length=50)

    def setarCampos(self, filiado: filiado_up):
        self.tituloEleitor = getattr(filiado, 'tituloEleitor', None)
        self.nome = getattr(filiado, 'nome_completo', None)
        self.genero = getattr(filiado, 'genero', None)
        self.dataFiliacao = getattr(filiado, 'dataFiliacao', None)
        self.uf = getattr(filiado, 'uf', None)
        self.municipio = getattr(filiado, 'local_residencia', None)
        self.zona = getattr(filiado, 'zona', None)
        self.situacao = getattr(filiado, 'situacao', SituacaoFiliacao.NAO_REGULAR)
        self.pendenciaComunicacao = getattr(filiado, 'pendenciaComunicacao', True)
        self.nome_completo = getattr(filiado, 'nome_completo', self.nome)
        self.nome_social = getattr(filiado, 'nome_social', self.nome)
        self.data_nascimento = getattr(filiado, 'data_nascimento', None)
        self.sexo = getattr(filiado, 'genero', None)
        self.raca = getattr(filiado, 'raca', None)
        self.sexualidade = getattr(filiado, 'sexualidade', None)
        self.pcd = getattr(filiado, 'pcd', False)
        self.local_residencia = getattr(filiado, 'local_residencia', None)
        self.local_exercicio = getattr(filiado, 'local_exercicio', None)
        # Dados extras vindo da planilha central da UP
        self.secao = getattr(filiado, 'secao', None)
        self.cpf = getattr(filiado, 'cpf', None)
        self.cep = getattr(filiado, 'cep', None)
        self.rg = getattr(filiado, 'rg', None)
        self.endereco_residencial = getattr(filiado, 'endereco_residencial', None)
        self.nome_mae = getattr(filiado, 'nome_mae', None)
        self.ocupacao = getattr(filiado, 'ocupacao', None)
        self.telefoneComDDD = getattr(filiado, 'telefoneComDDD', None)
        self.whatsAppComDDD = getattr(filiado, 'whatsAppComDDD', None)
        self.email = getattr(filiado, 'email', None)
        self.data_inscricao = getattr(filiado, 'data_inscricao', None)
        self.genero = getattr(filiado, 'genero', None)
        self.data_atualizacao = getattr(filiado, 'data_atualizacao', None)
        self.municipio_onde_vota = getattr(filiado, 'municipio_onde_vota', None)
        self.reponsavelFiliacao = getattr(filiado, 'reponsavelFiliacao', None)
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

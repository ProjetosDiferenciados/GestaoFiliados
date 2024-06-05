from datetime import datetime
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from tse_importador.persistencia.entidades.ent_filiado_up import ent_filiado_up
from paprika import to_string

@to_string
class ent_filiado_up_expectativa:
    def __init__(self, id):
        self.id = id
        self.nome = "nome"
        self.nome_completo = "nome_completo"
        self.nome_social=  'nome_social'
        self.data_nascimento= datetime(1, 1, 1)
        self.genero = 'genero'
        self.sexualidade = 'sexualidade'
        self.raca = 'raca'
        self.pcd = False
        self.municipio = 'municipio'
        self.tituloEleitor = 'tituloEleitor'
        self.dataFiliacao = datetime(1, 1, 1)
        self.uf = 'uf'   
        self.zona = 0
        self.situacao = situacao_filiacao.REGULAR.name
        self.pendenciaComunicacao = False
        self.local_residencia= "municipio"
        self.local_exercicio = 'local_exercicio'
        pass
    pass
    def gerar_entidade_pai(self) -> ent_filiado_up:
        entidade = ent_filiado_up()
        entidade.id = self.id
        entidade.nome = self.nome
        entidade.nome_completo = self.nome_completo
        entidade.nome_social = self.nome_social
        entidade.data_nascimento = self.data_nascimento
        entidade.genero = self.genero
        entidade.sexualidade = self.sexualidade
        entidade.raca = self.raca
        entidade.pcd = self.pcd
        entidade.municipio = self.municipio
        entidade.tituloEleitor = self.tituloEleitor
        entidade.dataFiliacao = self.dataFiliacao
        entidade.uf = self.uf
        entidade.zona = self.zona
        entidade.situacao = self.situacao
        entidade.pendenciaComunicacao = self.pendenciaComunicacao
        entidade.local_residencia = self.local_residencia
        entidade.local_exercicio = self.local_exercicio
        return entidade
    
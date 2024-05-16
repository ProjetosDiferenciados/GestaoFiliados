from tse_importador.up.entidades.filiados import filiado_up
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from tse_importador.up.entidades.regiao_administrativa import regiao_administrativa
from datetime import datetime
from dataclasses import dataclass

@dataclass()
class filiado_up_expectativa(filiado_up):
    def __init__(self, id):
        self.id = id
        self.nome_completo = "nome"
        self.nome_social=  'Desconhecido'
        self.data_nascimento= None
        self.genero= 'genero'
        self.tituloEleitor= "tituloEleitor"
        self.sexualidade= "Desconhecido"
        self.raca= 'Desconhecido'
        self.pcd= 'Desconhecido'
        self.dataFiliacao = datetime(1, 1, 1)
        self.uf = "uf"
        self.pcd = 'Desconhecido'
        self.zona = 0
        self.pendenciaComunicacao = False
        self.situacao = situacao_filiacao.REGULAR
        self.local_residencia= "municipio"
        self.local_exercicio = 'Desconhecido'
        pass
    pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
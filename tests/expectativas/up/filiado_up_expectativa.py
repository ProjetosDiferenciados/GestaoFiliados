from tse_importador.up.entidades.filiado_up import filiado_up
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from tse_importador.up.entidades.regiao_administrativa import regiao_administrativa
from tse_importador.up.entidades.profissao_enum import *
from datetime import datetime
from paprika import to_string

@to_string
class filiado_up_expectativa(filiado_up):
    def __init__(self):
        self.id = None
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
        self.pcd = False
        self.zona = 0
        self.pendenciaComunicacao = False
        self.situacao = situacao_filiacao.REGULAR
        self.local_residencia= "municipio"
        self.local_exercicio = 'Desconhecido'
        self.etnia = 'Desconhecido'
        self.profissao = profissao_enum.DESCONHECIDO
        pass
    pass
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
        self.pcd = False
        self.zona = 0
        self.pendenciaComunicacao = False
        self.situacao = situacao_filiacao.REGULAR
        self.local_residencia= "municipio"
        self.local_exercicio = 'Desconhecido'
        self.profissao = profissao_enum.DESCONHECIDO
        self.etnia = 'Desconhecido'
        pass
    pass

    def __eq__(self, other):
        if (other is None or not isinstance(other,filiado_up)  ):
            return False
        return (self.id == other.id and 
                self.nome_completo == other.nome_completo and 
                self.nome_social == other.nome_social and 
                self.data_nascimento == other.data_nascimento and 
                self.genero == other.genero and 
                self.tituloEleitor == other.tituloEleitor and
                self.sexualidade == other.sexualidade and
                self.raca == other.raca and
                self.pcd == other.pcd and
                self.dataFiliacao == other.dataFiliacao and
                self.uf == other.uf and
                self.zona == other.zona and
                self.situacao == other.situacao and
                self.pendenciaComunicacao == other.pendenciaComunicacao and
                self.local_residencia == other.local_residencia and
                self.local_exercicio == other.local_exercicio and
                self.profissao.value == other.profissao.value and 
                self.etnia == other.etnia
                )
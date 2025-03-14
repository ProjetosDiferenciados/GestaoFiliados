from tse_importador.up.entidades.filiado_up import filiado_up
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from tse_importador.up.entidades.regiao_administrativa import regiao_administrativa
from tse_importador.up.entidades.profissao_enum import *
from datetime import datetime
from paprika import *

@to_string
class filiado_up_banco_expectativa(filiado_up):
    def __init__(self, id:int):
        self.id = id
        self.nome_completo = "nome_completo"
        self.nome_social=  'nome_social'
        self.data_nascimento= datetime(1, 1, 1, 0, 0)
        self.genero= 'genero'
        self.tituloEleitor= "tituloEleitor"
        self.sexualidade= "sexualidade"
        self.raca= 'raca'
        self.pcd= False
        self.dataFiliacao = datetime(1, 1, 1)
        self.uf = "uf"
        self.zona = 0
        self.pendenciaComunicacao = False
        self.situacao = situacao_filiacao.REGULAR
        self.local_residencia= "municipio"
        self.local_exercicio = 'local_exercicio'
        self.profissao = profissao_enum.DESCONHECIDO
        self.etnia = "Desconhecido"
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
                self.local_exercicio == other.local_exercicio
                )

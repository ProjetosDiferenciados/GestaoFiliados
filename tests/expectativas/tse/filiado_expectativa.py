from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from tse_importador.tse.entidades.filiado import Tse_Filiado
from datetime import datetime

class Filiado_expectativa(Tse_Filiado):
    def __init__(self):
        self.tituloEleitor = "tituloEleitor"
        self.nome = "nome"
        self.genero = "genero"
        self.dataFiliacao = datetime(1,1,1)
        self.uf = "uf"
        self.municipio = "municipio"
        self.zona = 0
        self.partido = "partido"
        self.situacao = situacao_filiacao.REGULAR
        self.pendenciaComunicacao = False
        pass
    pass
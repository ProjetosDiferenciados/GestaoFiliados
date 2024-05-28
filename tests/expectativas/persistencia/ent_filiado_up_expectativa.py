from datetime import datetime
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from tse_importador.persistencia.entidades.ent_filiado_up import ent_filiado_up

class ent_filiado_up_expectativa:
    def __init__(self, id):
        print("##### ent_filiado_up_expectativa #####")
        print(self)
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
        self.situacaoid = situacao_filiacao.REGULAR.value
        self.pendenciaComunicacao = False
        self.local_residencia= "municipio"
        self.local_exercicio = 'local_exercicio'
        
        pass
    pass
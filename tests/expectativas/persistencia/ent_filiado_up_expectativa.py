
from tse_importador.persistencia.entidades.ent_filiado_up import ent_filiado_up

class ent_filiado_up_expectativa(ent_filiado_up):
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
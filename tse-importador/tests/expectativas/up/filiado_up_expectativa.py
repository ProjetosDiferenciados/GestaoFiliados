from tse_importador.up.entidades.filiados import filiado_up
from tse_importador.up.entidades.regiao_administrativa import regiao_administrativa
from datetime import date

class filiado_up_expectativa(filiado_up):

    def __init__(self, id):
        self.id = id
        self.nome_completo = "set_nome_completo"
        self.nome_social= "set_nome_social"
        self.data_nascimento= date(2021, 1, 1)
        self.genero= "set_genero"
        self.sexualidade= "set_sexualidade"
        self.raca= "set_raca"
        self.pcd= True
        self.local_residencia= "set_local_residencia"
        self.local_exercicio = regiao_administrativa.SIA
        pass
    pass


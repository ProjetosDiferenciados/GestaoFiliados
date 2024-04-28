from tse_importador.up.entidades.filiados import Filiado
from tse_importador.up.entidades.regiao_administrativa import regiao_administrativa

class filiado_up_expectativa(Filiado):

    def __init__(self, id):
        self.id = id
        self.set_nome_completo("set_nome_completo")
        self.set_nome_social("set_nome_social")
        self.set_data_nascimento(date(2021, 1, 1))
        self.set_genero("set_genero")
        self.set_sexualidade("set_sexualidade")
        self.set_raca("set_raca")
        self.set_pcd(True)
        self.set_local_residencia("set_local_residencia")
        self.set_local_exercicio(regiao_administrativa.SIA)
        pass
    pass


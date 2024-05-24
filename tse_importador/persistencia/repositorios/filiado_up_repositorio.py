from sqlalchemy import select
from tse_importador.persistencia.entidades.ent_filiado_up import ent_filiado_up

class filiado_up_repositorio:
    def __init__(self):
        pass
    def salvar(self, filiado):
        pass
    def buscar(self, id):
        print("##### buscar #####")
        sQuery = select(ent_filiado_up)
        print(sQuery)
        pass
    def deletar(self, id):
        pass
    pass
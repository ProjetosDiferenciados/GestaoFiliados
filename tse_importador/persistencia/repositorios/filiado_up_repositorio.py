from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tse_importador.persistencia.entidades.ent_filiado_up import ent_filiado_up


engine = create_engine("sqlite:///:memory:")

# an Engine, which the Session will use for connection
# resources
class filiado_up_repositorio:
    def __init__(self):
        pass
    def salvar(self, filiado):
        pass
    def buscar(self, id):
        print("##### buscar #####")
        session = self.useSession(self)
        with session() as sessionManaged:
            sQuery = select(ent_filiado_up).where(ent_filiado_up.id == id)
            print(sQuery)
            return sessionManaged.execute(sQuery) 
        pass
    def deletar(self, id):
        pass
    def useSession(self):
        Session = sessionmaker(bind=engine)
        return  Session
        pass
    

    pass
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tse_importador.up.entidades.filiados import filiado_up
from tse_importador.persistencia.entidades.converter_ent_filiado_up import converter_filiado_ent_up
from tse_importador.persistencia.entidades.ent_filiado_up import ent_filiado_up
import json


# an Engine, which the Session will use for connection
# resources
class filiado_up_repositorio:
    def __init__(self, engine):
        self.engine = engine
        pass
    def salvar(self, filiado):
        session = self.useSession()
        useConverter = self.useConverter(self)
        with session() as sessionManaged:
            sQuery = select(ent_filiado_up).where(ent_filiado_up.tituloEleitor == filiado.tituloEleitor)
            entNova = useConverter.converter_filiacao_up_ent_filiacao_up(filiado)
            ent = sessionManaged.execute(sQuery)
            if ent:
                ent.update(entNova)
                return
            else:
                sessionManaged.add(entNova)
            sessionManaged.commit()
        pass
    def buscar(self, id) -> filiado_up:
        session = self.useSession()
        useConverter = self.useConverter(self)
        with session() as sessionManaged:
            sQuery = select(ent_filiado_up).where(ent_filiado_up.id == id)
            ent = sessionManaged.execute(sQuery)
            result = useConverter.converter_ent_filiacao_up_filiacao_up(ent);
            return result 
        pass
    def buscarPorTituloEleitor(self, tituloEleitor:str) -> filiado_up:
        session = self.useSession()
        useConverter = self.useConverter(self)
        with session() as sessionManaged:
            sQuery = select(ent_filiado_up).where(ent_filiado_up.tituloEleitor == tituloEleitor)
            ent = sessionManaged.execute(sQuery)
            result = useConverter.converter_ent_filiacao_up_filiacao_up(ent);
            return result 
        pass
    def useSession(self):
        Session = sessionmaker(bind=self.engine)
        return  Session
        pass
    def useConverter(self):
        return converter_filiado_ent_up()

    pass
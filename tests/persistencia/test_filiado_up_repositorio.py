from mockito import when, mock, unstub, spy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tse_importador.persistencia.entidades.ent_filiado_up import ent_filiado_up
from tse_importador.persistencia.repositorios.filiado_up_repositorio import filiado_up_repositorio
from tests.expectativas.persistencia.ent_filiado_up_expectativa import ent_filiado_up_expectativa

repo = spy(filiado_up_repositorio)
sessionSpy = spy(Session)
createEngineMock = mock(create_engine)


#Mockagem inicial
when(repo).useSession().thenReturn(sessionSpy)

def test_buscar_filiado_up_sucesso():
    #Mockagem
    print("##### test_buscar_filiado_up_sucesso #####")
    print(ent_filiado_up_expectativa(1))
    when(sessionSpy).execute(...).thenReturn(ent_filiado_up_expectativa(1))
    repo.buscar(repo,1)
    assert False
    pass

unstub()
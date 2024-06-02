from mockito import when, mock, unstub, spy, spy2
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from mockito.matchers import any as ANY
from tests.expectativas.up.filiado_up_banco_expectativa import filiado_up_banco_expectativa
from tse_importador.persistencia.entidades.ent_filiado_up import ent_filiado_up
from tse_importador.persistencia.repositorios.filiado_up_repositorio import filiado_up_repositorio
from tests.expectativas.persistencia.ent_filiado_up_expectativa import ent_filiado_up_expectativa


def test_buscar_filiado_up_sucesso():
    expectativa = ent_filiado_up_expectativa(1)

    repo:filiado_up_repositorio = spy(filiado_up_repositorio)
    sessionMaker = mock()
    engineMock = mock()
    sessionSpy = mock()

    #Mockagem inicial
    repo.engine = engineMock
    when(repo).useSession(...).thenReturn(sessionMaker)
    when(sessionMaker).__call__(...).thenReturn(sessionSpy);
    when(sessionSpy).__enter__(...).thenReturn(sessionSpy)
    when(sessionSpy).__exit__(...).thenReturn(sessionSpy)
    when(sessionSpy).execute(...).thenReturn(expectativa.gerar_entidade_pai())

    #Mockagem
    print("##### test_buscar_filiado_up_sucesso #####") 
    result = repo.buscar(repo,1)
    assert filiado_up_banco_expectativa(1) == result  
    pass

unstub()
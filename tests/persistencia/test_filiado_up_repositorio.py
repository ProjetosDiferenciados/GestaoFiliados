from mockito import when, mock, unstub, spy, verify
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from mockito.matchers import any as ANY
from tests.expectativas.up.filiado_up_expectativa import filiado_up_expectativa
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


def test_buscar_tituloEleitor_filiado_up_sucesso():
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
    result = repo.buscarPorTituloEleitor(repo,"3131231241231")
    assert filiado_up_banco_expectativa(1) == result  
    pass

def test_salvar_filiado_up_sucesso():
    expectativa = ent_filiado_up_expectativa(1)
    argumento = filiado_up_expectativa(1)

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
    when(sessionSpy).execute(...).thenReturn(None)

    #Mockagem
    print("##### test_buscar_filiado_up_sucesso #####") 
    result = repo.salvar(repo,argumento)
    verify(sessionSpy).add(ANY(ent_filiado_up))  
    pass

def test_atualizar_filiado_up_sucesso():
    expectativa = ent_filiado_up_expectativa(1)
    argumento = filiado_up_expectativa(1)

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
    result = repo.salvar(repo,argumento)
    verify(sessionSpy,times=0).add(ANY(ent_filiado_up))  
    pass
unstub()
from mockito import when, mock, unstub, spy
from tse_importador.persistencia.entidades.ent_filiado_up import ent_filiado_up
from tse_importador.persistencia.repositorios.filiado_up_repositorio import filiado_up_repositorio

repo = spy(filiado_up_repositorio)

def test_buscar_filiado_up_sucesso():
    repo.buscar(repo,1)
    assert False
    pass
from mockito import when, mock, unstub, spy2
from tse_importador.tse.entidades.conversor.conversor_filiado import upload_filiado
from ...expectativas.up.filiado_up_expectativa import filiado_up_expectativa
from ...expectativas.tse.filiado_expectativa import Filiado_expectativa 
from pytest import raises

upload_filiado = upload_filiado()


def test_converter_filiacao_tse_filiacao_cadastro_sucesso():
    print("test_converter_filiacao_tse_filiacao_cadastro_sucesso")
    expectativa: filiado_up_expectativa = filiado_up_expectativa(None)
    result: filiado_up_expectativa = upload_filiado.converter_filiacao_tse_filiacao_cadastro(Filiado_expectativa())
    assert expectativa == result
    pass


def test_converter_filiacao_tse_filiacao_cadastro_falha():
    print("test_converter_filiacao_tse_filiacao_cadastro_falha")
    expectativa: filiado_up_expectativa = filiado_up_expectativa(None)
    with raises(ValueError):
        upload_filiado.converter_filiacao_tse_filiacao_cadastro(None);
    pass
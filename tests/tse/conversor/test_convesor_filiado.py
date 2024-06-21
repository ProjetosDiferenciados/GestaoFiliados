from mockito import when, mock, unstub, spy2
from tse_importador.tse.entidades.conversor.conversor_filiado import conversor_filiado
from ...expectativas.up.filiado_up_expectativa import filiado_up_expectativa
from ...expectativas.tse.filiado_expectativa import Filiado_expectativa 
from pytest import raises

conversor_filiado = conversor_filiado()


def test_converter_filiacao_tse_filiacao_cadastro_sucesso():
    print("test_converter_filiacao_tse_filiacao_cadastro_sucesso")
    expectativa: filiado_up_expectativa = filiado_up_expectativa(None)
    result: filiado_up_expectativa = conversor_filiado.converter_filiacao_tse_filiacao_cadastro(Filiado_expectativa())
    assert expectativa == result
    pass


def test_converter_filiacao_tse_filiacao_cadastro_falha():
    print("test_converter_filiacao_tse_filiacao_cadastro_falha")
    expectativa: filiado_up_expectativa = filiado_up_expectativa(None)
    with raises(ValueError):
        conversor_filiado.converter_filiacao_tse_filiacao_cadastro(None);
    pass
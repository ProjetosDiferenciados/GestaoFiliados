from mockito import when, mock, unstub, spy2
from tse_importador.tse.entidades.conversor.conversor_filiado import conversor_filiacao
from ...expectativas.up.filiado_up_expectativa import filiado_up_expectativa

conversor_filiacao = conversor_filiacao()


def test_converter_filiacao_tse_filiacao_cadastro_sucesso():
    result = conversor_filiacao.converter_filiacao_tse_filiacao_cadastro(None)
    assert result == filiado_up_expectativa(1)
    pass
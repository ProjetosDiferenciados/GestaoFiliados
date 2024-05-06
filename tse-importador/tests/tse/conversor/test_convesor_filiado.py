from mockito import when, mock, unstub, spy2
from tse_importador.tse.entidades.conversor.conversor_filiado import conversor_filiacao
from ...expectativas.up.filiado_up_expectativa import filiado_up_expectativa
from ...expectativas.tse.filiado_expectativa import Filiado_expectativa 
conversor_filiacao = conversor_filiacao()


def test_converter_filiacao_tse_filiacao_cadastro_sucesso():
    expectativa: filiado_up_expectativa = filiado_up_expectativa(1)
    result: filiado_up_expectativa = conversor_filiacao.converter_filiacao_tse_filiacao_cadastro(Filiado_expectativa())
    print("EXPECTATIVA = {}".format(filiado_up_expectativa(1).__str__()))
    print("RESULT = {}".format(result.__str__()))
    print(" IGUALDADE = {}".format(result.__eq__(filiado_up_expectativa(1))))
    assert result.__eq__(expectativa)
    pass
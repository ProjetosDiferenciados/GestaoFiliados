from mockito import when, mock, unstub, spy2
from tse_importador.up.entidades.conversor.upload_filiado_up import upload_filiado_up
from tests.expectativas.up.filiado_up_importado_expectativa import filiado_up_importado_expectativa
from tse_importador.up.entidades.filiado_up import filiado_up
from pytest import raises

upload_filiado_up = upload_filiado_up()


def test_upload_filiado_tse_sucesso():
    print("test_uploado_filiado_up_sucesso")
    result:list = upload_filiado_up.converter_excel_to_filiado_up_list("tests/Modelo-filiacao-up.xlsx")
    assert len(result) == 1
    for r in result:
        print(r)
        assert(filiado_up_importado_expectativa() == r)

    print(list)

    # Caso triste
    try:
        upload_filiado_up.converter_excel_to_filiado_up_list("falha")
        assert False
    except FileNotFoundError as e:
        print(e)
        assert True
    pass


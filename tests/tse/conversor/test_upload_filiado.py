from mockito import when, mock, unstub, spy2
from tse_importador.tse.entidades.conversor.upload_filiado import upload_filiado
from tse_importador.tse.entidades.filiado import Tse_Filiado
from tse_importador.up.entidades.filiados import filiado_up
from pytest import raises

upload_filiado = upload_filiado()


def test_upload_filiado_tse_sucesso():
    print("test_uploado_filiado_tse_sucesso")
    result:list = upload_filiado.converter_excel_to_tse_filiado_list("tests/Modelo-tse-extendido.xlsx")
    assert len(result) == 28
    for r in result:
        isinstance(r, Tse_Filiado)

    # Caso triste
    try:
        upload_filiado.converter_excel_to_tse_filiado_list("falha")
        assert False
    except FileNotFoundError as e:
        print(e)
        assert True
    pass


def test_upload_filiado_up_sucesso():
    print("test_uploado_filiado_tse_sucesso")
    result:list = upload_filiado.converter_excel_to_filiado_list("tests/Modelo-tse-extendido.xlsx")
    assert len(result) == 28
    for r in result:
        isinstance(r, filiado_up)

    # Caso triste
    try:
        upload_filiado.converter_excel_to_filiado_list("falha")
        assert False
    except FileNotFoundError as e:
        print(e)
        assert True
    pass


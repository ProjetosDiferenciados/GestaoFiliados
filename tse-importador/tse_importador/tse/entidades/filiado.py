import datetime
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao

class Filiado:
    tituloEleitor: str
    nome: str
    genero: str
    dataFiliacao : datetime 
    uf : str
    municipio : str
    zona : int
    partido : str 
    situacao : situacao_filiacao
    pendenciaComunicacao = False


    pass






from datetime import date 
from tse_importador.up.entidades.regiao_administrativa import regiao_administrativa
import datetime
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from dataclasses import dataclass

@dataclass()
class filiado_up:

    nome_completo: str
    nome_social: str
    data_nascimento: date
    genero: str
    sexualidade: str
    raca: str
    pcd: bool
    local_residencia: str
    local_exercicio: regiao_administrativa

    # Dados extras vindo do TSE
    tituloEleitor: str
    dataFiliacao : datetime 
    uf : str
    zona : int 
    situacao : situacao_filiacao
    pendenciaComunicacao: bool


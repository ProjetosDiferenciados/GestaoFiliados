from datetime import date 
from regiao_administrativa import regiao_administrativa
from paprika import *

@data
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
    pass
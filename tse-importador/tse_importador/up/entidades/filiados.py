from datetime import date 
from tse_importador.up.entidades.regiao_administrativa import regiao_administrativa
from paprika import *

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
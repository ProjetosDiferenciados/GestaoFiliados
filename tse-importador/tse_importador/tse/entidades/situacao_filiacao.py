from tse_importador.tse.entidades import *
from enum import Enum

def get_situacao_filiacao_por_nome(name):
    if name == situacao_filiacao.REGULAR._name_:
        return situacao_filiacao.REGULAR
    elif name == situacao_filiacao.NAO_REGULAR._name_:
        return situacao_filiacao.NAO_REGULAR
    else:
        return None

class situacao_filiacao(Enum):
    REGULAR = 1,
    NAO_REGULAR = 2
    pass


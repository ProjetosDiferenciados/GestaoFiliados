from datetime import date 
from tse_importador.up.entidades.regiao_administrativa import regiao_administrativa
import datetime
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from paprika import *

@data
class filiado_up:
    id: int
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
    # todo verificar todos os campos 
    # municipio falta
    tituloEleitor: str
    uf : str
    zona : int
    secao : int 
    situacao : situacao_filiacao
    pendenciaComunicacao: bool
    cienciaContribuicao: bool

    cpf: str
    cep: str
    rg: str
    endereco_residencial: str
    nome_mae: str
    ocupacao: str
    municipio: str
    telefoneComDDD: str
    whatsAppComDDD: str
    email: str

    data_inscricao: datetime
    data_atualizacao: datetime
    dataFiliacao : datetime 

    municipio_onde_vota: str
    reponsavelFiliacao: str

    def verificar_titulo_eleitor_igual(self, outro_filiado:any) -> bool:
        if not isinstance(outro_filiado, filiado_up):
            return False
        return self.tituloEleitor == outro_filiado.tituloEleitor
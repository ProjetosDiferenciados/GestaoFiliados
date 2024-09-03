from tse_importador.up.entidades.filiado_up import filiado_up
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from tse_importador.up.entidades.regiao_administrativa import regiao_administrativa
from datetime import datetime
from paprika import to_string

@to_string
class filiado_up_importado_expectativa(filiado_up):
    def __init__(self):
        self.data_inscricao  = datetime(2023, 11, 2, 12, 12, 23)
        self.cep = "73015418"
        self.dataFiliacao = datetime(2022, 11, 29)
        self.email = "victorhs@gmail.com"
        self.endereco_residencial = "Quadra 2 conjunto"
        self.municipio = "Sobradinho"
        self.municipio_onde_vota = "Brasília"
        self.nome_completo = "Victor Henrique "
        self.nome_mae = "NOME DA MÃE"
        self.ocupacao = "-"
        self.reponsavelFiliacao = "Alexandre"
        self.rg = "3123123"
        self.secao = "123"
        self.telefoneComDDD = "619927123"
        self.tituloEleitor = "132412341234"
        self.uf = "DF"
        self.whatsAppComDDD = "6199123123"
        self.zona = 2

    def __eq__(self, valor: object) -> bool:
        return self.data_inscricao == valor.data_inscricao and \
            self.cep == valor.cep and \
            self.dataFiliacao == valor.dataFiliacao and \
            self.email == valor.email and \
            self.endereco_residencial == valor.endereco_residencial and \
            self.municipio == valor.municipio and \
            self.municipio_onde_vota == valor.municipio_onde_vota and \
            self.nome_completo == valor.nome_completo and \
            self.nome_mae == valor.nome_mae and \
            self.ocupacao == valor.ocupacao and \
            self.reponsavelFiliacao == valor.reponsavelFiliacao and \
            self.rg == valor.rg and \
            self.secao == valor.secao and \
            self.telefoneComDDD == valor.telefoneComDDD and \
            self.tituloEleitor == valor.tituloEleitor and \
            self.uf == valor.uf and \
            self.whatsAppComDDD == valor.whatsAppComDDD and \
            self.zona == valor.zona
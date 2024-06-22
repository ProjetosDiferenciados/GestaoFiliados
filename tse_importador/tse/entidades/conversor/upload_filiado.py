from pandas import pandas as pd
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from tse_importador.tse.entidades.situacao_filiacao import get_situacao_filiacao_por_nome
from tse_importador.tse.entidades.conversor.conversor_filiado import conversor_filiado
from tse_importador.tse.entidades.filiado import Tse_Filiado


class upload_filiado:
    conversor :conversor_filiado = conversor_filiado()
    def converter_excel_to_tse_filiado_list(self, file) -> list:
        df = pd.read_excel(file)
        df = df.dropna()
        lista_filiados = []
        for i, r in df.iterrows():
            novo_filiado_tse: Tse_Filiado = Tse_Filiado()
            novo_filiado_tse.nome = r['NOME']
            novo_filiado_tse.genero = r['GENERO']
            novo_filiado_tse.dataFiliacao = datetime.strptime(r['DATA FILIACAO'], '%d/%m/%Y')
            novo_filiado_tse.uf = r['UF']
            novo_filiado_tse.zona = r['ZONA']
            novo_filiado_tse.partido = r['PARTIDO']
            novo_filiado_tse.situacao = get_situacao_filiacao_por_nome(r['SITUACAO'])
            novo_filiado_tse.tituloEleitor = r['TITULO ELEITOR']
            novo_filiado_tse.municipio = r['MUNICIPIO']
            novo_filiado_tse.pendenciaComunicacao = True if r['PENDENCIA DE COMUNICACAO'] == 'SIM' else False
            lista_filiados.append(novo_filiado_tse)
            print("########## TSE FILIADO ############## :",r['SITUACAO'])
        return lista_filiados
        pass

    def converter_excel_to_filiado_list(self, file) -> list:
        tse_list: list = self.converter_excel_to_tse_filiado_list(file)
        filiado_list = []
        for tse in tse_list:
            filiado_list.append(self.conversor.converter_filiacao_tse_filiacao_cadastro(tse))
        return filiado_list
        pass
    pass
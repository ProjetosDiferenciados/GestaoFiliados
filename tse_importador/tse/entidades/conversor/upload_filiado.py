from pandas import pandas as pd
from tse_importador.tse.entidades.filiado import Filiado


class upload_filiado:
    def converter_excel_dataframe(self, file):
        df = pd.read_excel(file)
        df = df.dropna()
        for i, r in df.iterrows():
            print("######## INDICE ########")
            novo_filiado_tse: Filiado = Filiado()
            novo_filiado_tse.nome = r['NOME']
            novo_filiado_tse.genero = r['GENERO']
            novo_filiado_tse.dataFiliacao = r['DATA FILIACAO']
            novo_filiado_tse.uf = r['UF']
            novo_filiado_tse.zona = r['ZONA']
            novo_filiado_tse.partido = r['PARTIDO']
            novo_filiado_tse.situacao = r['SITUACAO']
            novo_filiado_tse.tituloEleitor = r['TITULO ELEITOR']
            novo_filiado_tse.municipio = r['MUNICIPIO']
            novo_filiado_tse.pendenciaComunicacao = True if r['PENDENCIA DE COMUNICACAO'] == 'SIM' else False
            print(novo_filiado_tse.json_converter_filiado_up())
        return 
        pass
from pandas import pandas as pd
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from tse_importador.tse.entidades.situacao_filiacao import get_situacao_filiacao_por_nome
from tse_importador.tse.entidades.conversor.conversor_filiado import conversor_filiado
from tse_importador.up.entidades.filiado_up import filiado_up



class upload_filiado_up:
    conversor :conversor_filiado = conversor_filiado()
    def converter_excel_to_filiado_up_list(self, file) -> list:
        df = pd.read_excel(file)
        lista_filiados = []
        for i, r in df.iterrows():
            novo_filiado_up: filiado_up = filiado_up()
            novo_filiado_up.data_inscricao = (r['Carimbo de data/hora']).to_pydatetime()
            novo_filiado_up.nome_completo = r['NOME COMPLETO']
            novo_filiado_up.rg = str(r['RG'])
            novo_filiado_up.nome_mae = r['NOME DA MÃE']
            novo_filiado_up.ocupacao = r['OCUPAÇÃO/PROFISSÃO']
            novo_filiado_up.tituloEleitor = str(r['TÍTULO DE ELEITOR'])
            novo_filiado_up.zona = r['ZONA']
            novo_filiado_up.secao = str(r['SEÇÃO'])
            novo_filiado_up.municipio_onde_vota = r['MUNICÍPIO ONDE VOTA']
            novo_filiado_up.uf = r['UF']
            novo_filiado_up.endereco_residencial = r['ENDEREÇO RESIDENCIAL']
            novo_filiado_up.cep = str(r['CEP'])
            novo_filiado_up.municipio = r['CIDADE']
            novo_filiado_up.uf = r['UF']
            novo_filiado_up.email = r['E-MAIL']
            novo_filiado_up.telefoneComDDD = str(r['TELEFONE COM DDD'])
            novo_filiado_up.whatsAppComDDD = str(r['WHATSAPP COM DDD'])
            novo_filiado_up.dataFiliacao = r['DATA DA FILIAÇÃO'].to_pydatetime()
            novo_filiado_up.reponsavelFiliacao = r['RESPONSÁVEL POR SUA FILIAÇÃO']
            print(novo_filiado_up)
            lista_filiados.append(novo_filiado_up)
        return lista_filiados
        pass



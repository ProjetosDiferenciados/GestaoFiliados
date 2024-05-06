from tse_importador.tse.entidades.filiado import Filiado
from tse_importador.up.entidades.filiados import filiado_up
from tse_importador.tse.entidades.situacao_filiacao import get_situacao_filiacao_por_nome
from datetime import datetime
import json 


class conversor_filiacao:
    def converter_filiacao_tse_filiacao_cadastro(self, tse_filiado:Filiado ) -> filiado_up: 
        jsontexto = json.loads(tse_filiado.json_converter_filiado_up())
        ent:filiado_up = filiado_up(**jsontexto)
        # Pequenas correcoes
        ent.situacao = get_situacao_filiacao_por_nome(ent.situacao)
        ent.pendenciaComunicacao = {True: True, False: False}[ent.pendenciaComunicacao == "true"]
        ent.dataFiliacao = datetime.strptime(ent.dataFiliacao, '%Y-%m-%d %H:%M:%S')
        # Fim das correcoes
        return ent
        pass
    

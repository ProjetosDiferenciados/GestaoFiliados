from tse_importador.tse.entidades.filiado import Filiado
from tse_importador.up.entidades.filiados import filiado_up
from tse_importador.tse.entidades.situacao_filiacao import get_situacao_filiacao_por_nome
from datetime import datetime
import json 


class upload_filiado:
    def converter_filiacao_tse_filiacao_cadastro(self, tse_filiado:Filiado ) -> filiado_up: 
        self.valida_tse_filiado_valido(tse_filiado);
        jsontexto = json.loads(tse_filiado.json_converter_filiado_up());
        ent:filiado_up = filiado_up(**jsontexto);
        # Pequenas correcoes
        ent.situacao = get_situacao_filiacao_por_nome(ent.situacao)
        ent.pendenciaComunicacao = {True: True, False: False}[ent.pendenciaComunicacao == "true"]
        ent.dataFiliacao = datetime.strptime(ent.dataFiliacao, '%Y-%m-%d %H:%M:%S')
        # Fim das correcoes
        return ent
        pass

    def tse_filiado_valido(self, tse_filiado:Filiado) -> bool:
        return tse_filiado != None and isinstance(tse_filiado, Filiado)
        pass

    def valida_tse_filiado_valido(self, tse_filiado:Filiado) -> bool:
        if not self.tse_filiado_valido(tse_filiado):
            raise ValueError("Filiado invalido")
        pass
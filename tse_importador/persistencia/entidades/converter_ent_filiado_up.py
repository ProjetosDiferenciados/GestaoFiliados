from tse_importador.persistencia.entidades.ent_filiado_up import ent_filiado_up
from tse_importador.up.entidades.filiado_up import filiado_up
from tse_importador.tse.entidades.situacao_filiacao import get_situacao_filiacao_por_nome
from datetime import datetime
import json

class converter_filiado_ent_up:
    def converter_ent_filiacao_up_filiacao_up(self, ent:ent_filiado_up ) -> filiado_up:
        texto =  self.json_converter_filiado_up(ent)
        jsontexto = json.loads(texto);
        filiado:filiado_up = filiado_up(**jsontexto);
        # Pequenas correcoes
        filiado.situacao = get_situacao_filiacao_por_nome(ent.situacao)
        filiado.dataFiliacao = ent.dataFiliacao
        filiado.data_nascimento = ent.data_nascimento
        # Fim das correcoes
        return filiado
        pass

    def converter_filiacao_up_ent_filiacao_up(self, filiado:filiado_up ) -> ent_filiado_up:
        texto =  self.json_converter_filiado_up(filiado)
        jsontexto = json.loads(texto);
        ent:ent_filiado_up = ent_filiado_up(**jsontexto);
        # Pequenas correcoes
        ent.situacao = get_situacao_filiacao_por_nome(filiado.situacao)
        ent.dataFiliacao = filiado.dataFiliacao
        ent.data_nascimento = filiado.data_nascimento
        # Fim das correcoes
        return ent
        pass

    def json_converter_filiado_up (self, entidade:ent_filiado_up) -> str:
        return """
                {{
                    \"id\": {},
                    \"nome_completo\": \"{}\",
                    \"nome_social\": \"{}\",
                    \"data_nascimento\":null,
                    \"genero\": \"{}\",
                    \"sexualidade\": \"{}\" ,
                    \"raca\": \"{}\",
                    \"pcd\": {},
                    \"local_residencia\": \"{}\",
                    \"local_exercicio\": \"{}\",
                    \"tituloEleitor\": \"{}\",
                    \"dataFiliacao\" : null ,
                    \"uf\" : \"{}\",
                    \"zona\" : {},
                    \"situacao\" : null,
                    \"pendenciaComunicacao\" : {}
                }}""".format(
                    entidade.id,
                    entidade.nome_completo,
                    entidade.nome_social,
                    entidade.genero,
                    entidade.sexualidade,
                    entidade.raca,
                    "true" if entidade.pcd else "false",
                    entidade.local_residencia,
                    entidade.local_exercicio,
                    entidade.tituloEleitor ,
                    entidade.uf ,   
                    entidade.zona ,
                    "true" if entidade.pendenciaComunicacao else "false"
                )
        pass
    
    def json_converter_ent_filiado_up (self, entidade:filiado_up) -> str:
        return """
                {{
                    \"id\": {},
                    \"nome_completo\": \"{}\",
                    \"nome_social\": \"{}\",
                    \"data_nascimento\": null ,
                    \"genero\": \"{}\",
                    \"sexualidade\": \"{}\" ,
                    \"raca\": \"{}\",
                    \"pcd\": {},
                    \"local_residencia\": \"{}\",
                    \"local_exercicio\": \"{}\",
                    \"tituloEleitor\": \"{}\",
                    \"dataFiliacao\" : null ,
                    \"uf\" : \"{}\",
                    \"zona\" : {},
                    \"situacao\" : null,
                    \"pendenciaComunicacao\" : {}
                }}""".format(
                    entidade.id,
                    entidade.nome_completo,
                    entidade.nome_social,
                    entidade.genero,
                    entidade.sexualidade,
                    entidade.raca,
                    "true" if entidade.pcd else "false",
                    entidade.local_residencia,
                    entidade.local_exercicio,
                    entidade.tituloEleitor ,
                    entidade.uf ,   
                    entidade.zona ,
                    "true" if entidade.pendenciaComunicacao else "false"
                )
        pass
    pass
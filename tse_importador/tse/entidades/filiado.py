import datetime
from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao

class Filiado:
    tituloEleitor: str
    nome: str
    genero: str
    dataFiliacao : datetime 
    uf : str
    municipio : str
    zona : int
    partido : str 
    situacao : situacao_filiacao
    pendenciaComunicacao = False
    def json_converter_filiado_up (self):
        return """
                {{
                    \"nome_completo\": \"{}\",
                    \"nome_social\": \"Desconhecido\",
                    \"data_nascimento\": null,
                    \"genero\": \"{}\",
                    \"sexualidade\": \"Desconhecido\" ,
                    \"raca\": \"Desconhecido\",
                    \"pcd\": \"Desconhecido\",
                    \"local_residencia\": \"{}\",
                    \"local_exercicio\": \"Desconhecido\",
                    \"tituloEleitor\": \"{}\",
                    \"dataFiliacao\" : \"{}\" ,
                    \"uf\" : \"{}\",
                    \"zona\" : {},
                    \"situacao\" : \"{}\",
                    \"pendenciaComunicacao\" : \"{}\"
                }}
                """.format(
                    self.nome,
                    self.genero,
                    self.municipio,
                    self.tituloEleitor,
                    self.dataFiliacao,
                    self.uf,
                    self.zona,
                    self.situacao._name_,
                    {True: "true", False: "false"} [self.pendenciaComunicacao])
    pass





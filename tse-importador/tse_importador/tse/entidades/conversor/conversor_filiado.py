from tse_importador.tse.entidades.filiado import Filiado
from tse_importador.up.entidades.filiados import filiado_up 
from objectmapper import ObjectMapper   

mapper = ObjectMapper()
mapper.create_map(Filiado, filiado_up)
'''
mapper.create_map(Filiado, filiado_up, 
    {
        'nome_completo': lambda a : a.nome,
        'nome_social': lambda a : 'Desconhecido',
        'data_nascimento': lambda a : None,
        'genero': lambda a : a.genero,
        'sexualidade': lambda a : 'Desconhecido',
        'raca': lambda a : None,
        'pcd': lambda a : None,
        'local_residencia': lambda a : None,
        'local_exercicio': lambda a : None     
     })

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



    nome_completo: str
    nome_social: str
    data_nascimento: date
    genero: str
    sexualidade: str
    raca: str
    pcd: bool
    local_residencia: str
    local_exercicio: regiao_administrativa
'''

class conversor_filiacao:
    def converter_filiacao_tse_filiacao_cadastro(self, tse_filiado):
        return mapper.map(tse_filiado, filiado_up)
        pass
    

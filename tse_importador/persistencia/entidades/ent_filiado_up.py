from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from tse_importador.up.entidades.filiados import filiado_up
from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import registry
from paprika import data

mapper_registry = registry()


filiado_mapeamento = Table('filiados_up',
            mapper_registry.metadata,
            Column('id', Integer, primary_key=True),
            Column('nome', String(50)),
            Column('nome_completo', String(300)),
            Column('nome_social', String(300)),
            Column('data_nascimento', DateTime),
            Column('genero', String(50)),
            Column('sexualidade', String(50)),
            Column('raca', String(50)),
            Column('pcd', Boolean),
            Column('municipio', String(50)),
            Column('tituloEleitor', String(50)),
            Column('dataFiliacao', DateTime),
            Column('uf', String(50)),
            Column('zona', Integer),
            Column('situacao', String(30)),
            Column('pendenciaComunicacao', Boolean),
            Column('local_residencia', String(50)),
            Column('local_exercicio', String(50))
            )

@data
class ent_filiado_up(filiado_up):
    # Campos extras da entidade
    id: int
    pass
    def __init__(self):
        pass

    def update(self, other):
        self.id = other.id
        self.nome = other.nome
        self.nome_completo = other.nome_completo
        self.nome_social = other.nome_social
        self.data_nascimento = other.data_nascimento
        self.genero = other.genero
        self.sexualidade = other.sexualidade
        self.raca = other.raca
        self.pcd = other.pcd
        self.municipio = other.municipio
        self.tituloEleitor = other.tituloEleitor
        self.dataFiliacao = other.dataFiliacao
        self.uf = other.uf
        self.zona = other.zona
        self.situacao = other.situacao
        self.pendenciaComunicacao = other.pendenciaComunicacao
        self.local_residencia = other.local_residencia
        self.local_exercicio = other.local_exercicio
        pass
        



mapper_registry.map_imperatively(ent_filiado_up,filiado_mapeamento)

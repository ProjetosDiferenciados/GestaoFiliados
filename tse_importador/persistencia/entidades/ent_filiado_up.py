from tse_importador.tse.entidades.situacao_filiacao import situacao_filiacao
from tse_importador.up.entidades.filiados import filiado_up
from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import registry

mapper_registry = registry()


filiado_mapeamento = Table('filiados_up',
            mapper_registry.metadata,
            Column('id', Integer, primary_key=True),
            Column('tituloEleitor', String(50)),
            Column('nome', String(50)),
            Column('genero', String(50)),
            Column('dataFiliacao', DateTime),
            Column('uf', String(50)),
            Column('municipio', String(50)),
            Column('zona', Integer),
            Column('partido', String(50)),
            Column('situacaoid', Integer),
            Column('pendenciaComunicacao', Boolean)
        )


class ent_filiado_up(filiado_up):
    id: int
    situacaoid: int

    """ 
    id: Mapped[int] = mapped_column(primary_key=True)
    tituloEleitor: Mapped[str] = mapped_column(String(30))
    nome: Mapped[str] = mapped_column(String(30))
    genero: Mapped[str] = mapped_column(String(30))
    dataFiliacao : Mapped[datetime] = mapped_column(DateTime) 
    uf : Mapped[str] = mapped_column(String(2))
    municipio : Mapped[str] = mapped_column(String(30))
    zona : Mapped[int] = mapped_column(Integer)
    partido : Mapped[str] = mapped_column(String(30))
    situacao : Mapped[situacao_filiacao] = mapped_column(Enum(situacao_filiacao)) 
    pendenciaComunicacao = Mapped[bool] = mapped_column(Boolean)
    pass """

    pass


mapper_registry.map_imperatively(ent_filiado_up,filiado_mapeamento)

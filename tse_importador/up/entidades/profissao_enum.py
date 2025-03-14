from enum import Enum



class profissao_enum(Enum):
    DESCONHECIDO = {"numero": -1, "nome": "Desconhecido"}
    DESENVOLVEDOR_WEB = {"numero": 1, "nome": "Desenvolvedor Web"}
    ENGENHEIRO_CIVIL = {"numero": 2, "nome": "Engenheiro Civil"}
    MÉDICO = {"numero": 3, "nome": "Médico"}
    ADVOGADO = {"numero": 4, "nome": "Advogado"}
    CONTADOR = {"numero": 5, "nome": "Contador"}
    ARQUITETO = {"numero": 6, "nome": "Arquiteto"}
    ENFERMEIRO = {"numero": 7, "nome": "Enfermeiro"}
    DENTISTA = {"numero": 8, "nome": "Dentista"}
    PSICÓLOGO = {"numero": 9, "nome": "Psicólogo"}
    PROFESSOR = {"numero": 10, "nome": "Professor"}
    DESENVOLVEDOR_MOBILE = {"numero": 11, "nome": "Desenvolvedor Mobile"}
    GERENTE_PROJETO = {"numero": 12, "nome": "Gerente de Projetos"}
    FISIOTERAPEUTA = {"numero": 13, "nome": "Fisioterapeuta"}
    BANCÁRIO = {"numero": 14, "nome": "Bancário"}
    TÉCNICO_INFORMÁTICA = {"numero": 15, "nome": "Técnico em Informática"}
    SOLDADOR = {"numero": 16, "nome": "Soldador"}
    MECÂNICO = {"numero": 17, "nome": "Mecânico"}
    QUÍMICO = {"numero": 18, "nome": "Químico"}
    PUBLICITÁRIO = {"numero": 19, "nome": "Publicitário"}
    ENFERMEIRO_OBSTETRA = {"numero": 20, "nome": "Enfermeiro Obstetra"}
    BIOLOGISTA = {"numero": 21, "nome": "Biólogo"}
    ADMINISTRADOR = {"numero": 22, "nome": "Administrador"}
    ESTATÍSTICO = {"numero": 23, "nome": "Estatístico"}
    TÉCNICO_ENFERMAGEM = {"numero": 24, "nome": "Técnico em Enfermagem"}
    ENGENHEIRO_ELETRICISTA = {"numero": 25, "nome": "Engenheiro Eletricista"}
    SOCIOLOGISTA = {"numero": 26, "nome": "Sociólogo"}
    JORNALISTA = {"numero": 27, "nome": "Jornalista"}
    TÉCNICO_EM_SEGURANÇA_DO_TRABALHO = {"numero": 28, "nome": "Técnico em Segurança do Trabalho"}
    ATENDENTE = {"numero": 29, "nome": "Atendente"}
    GESTOR_DE_COMPRAS = {"numero": 30, "nome": "Gestor de Compras"}
    ENGENHEIRO_AMBIENTAL = {"numero": 31, "nome": "Engenheiro Ambiental"}
    DESIGNER_GRÁFICO = {"numero": 32, "nome": "Designer Gráfico"}
    AGENTE_DE_VIGILÂNCIA_SANITÁRIA = {"numero": 33, "nome": "Agente de Vigilância Sanitária"}
    TÉCNICO_DE_EDUCAÇÃO_FÍSICA = {"numero": 34, "nome": "Técnico de Educação Física"}
    TRANSPORTADOR = {"numero": 35, "nome": "Transportador"}
    ARTESÃO = {"numero": 36, "nome": "Artesão"}
    OPERADOR_DE_MÁQUINAS = {"numero": 37, "nome": "Operador de Máquinas"}
    ENCANADOR = {"numero": 38, "nome": "Encanador"}
    FOTÓGRAFO = {"numero": 39, "nome": "Fotógrafo"}
    AUXILIAR_DE_BABÁ = {"numero": 40, "nome": "Auxiliar de Babá"}
    AUDITOR = {"numero": 41, "nome": "Auditor"}
    TÉCNICO_DE_EDUCAÇÃO = {"numero": 42, "nome": "Técnico de Educação"}
    POLICIAL = {"numero": 43, "nome": "Policial"}
    GUARDIÃO_DE_PATRIMÔNIO = {"numero": 44, "nome": "Guardião de Patrimônio"}
    AGENTE_PRISIONAL = {"numero": 45, "nome": "Agente Prisional"}
    ANALISTA_DE_TI = {"numero": 46, "nome": "Analista de TI"}
    VENDEDOR_EXTERNO = {"numero": 47, "nome": "Vendedor Externo"}
    CORRETOR_DE_IMÓVEIS = {"numero": 48, "nome": "Corretor de Imóveis"}
    ESCRITURÁRIO = {"numero": 49, "nome": "Escriturário"}
    PODÓLOGO = {"numero": 50, "nome": "Podólogo"}



def get_profissao_enum_por_id(profissao: profissao_enum):
    profissao_aux = profissao if (profissao != None and isinstance(profissao, profissao_enum) ) else profissao_enum.DESCONHECIDO
    return profissao_aux

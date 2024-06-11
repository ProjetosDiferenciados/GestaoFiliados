CREATE TABLE IF NOT EXISTS filiados_up (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(50),
    nome_completo VARCHAR(300),
    nome_social VARCHAR(300),
    data_nascimento DATETIME,
    genero VARCHAR(50),
    sexualidade VARCHAR(50),
    raca VARCHAR(50),
    pcd BOOLEAN,
    municipio VARCHAR(50),
    tituloEleitor VARCHAR(50),
    dataFiliacao DATETIME,
    uf VARCHAR(50),
    zona INTEGER,
    situacao VARCHAR(30),
    pendenciaComunicacao BOOLEAN,
    local_residencia VARCHAR(50),
    local_exercicio VARCHAR(50)
);


-- DADOS TESTE:
INSERT INTO dados_pessoais(ID,nome) VALUES (1,'teste'); 
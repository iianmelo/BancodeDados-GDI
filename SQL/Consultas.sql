-- SUBCONSULTA DO TIPO TABELA
-- NOME DE EMPRESAS QUE TEM PARTICIPAÇÃO EM CLUBES
SELECT NOME
FROM EMPRESA 
WHERE CNPJ IN (SELECT CNPJ
               FROM PAT_CLUBE);

--INNER JOIN:
-- Nome das Empresas que patrocinam clubes e seu respectivo clube patrocinado:
SELECT E.NOME, C.NOME
FROM CLUBE C INNER JOIN PAT_CLUBE PC ON (C.CODIGO = PC.CODIGO) INNER JOIN EMPRESA E ON (PC.CNPJ = E.CNPJ);

--SUBCONSULTA DO TIPO ESCALAR
-- Codigo dos clubes que a empresa de nome 'Crefisa' patrocina:
SELECT PC.COD
FROM PAT_CLUBE PC
WHERE PC.CNPJ = (SELECT E.CNPJ
                 FROM EMPRESA E
                 WHERE E.NOME = 'CREFISA');

--SUBCONSULTA DO TIPO LINHA
-- Projetar o nome dos funcionários que nasceram na mesmo ano e tem a mesma nacionalidade do funcionário de id '001'
SELECT F.NOME
FROM FUNCIONARIO F
WHERE (YEAR(F.DT_NASCIMENTO), F.NACIONALIDADE) = (SELECT YEAR(F2.DT_NASCIMENTO), F2.NACIONALIDADE
                                                  FROM FUNCIONARIO F2
                                                  WHERE F2.ID_FUNC = '001');

--
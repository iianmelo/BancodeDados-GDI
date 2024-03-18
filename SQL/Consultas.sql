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
WHERE (TO_CHAR(F.DT_NASCIMENTO, 'YYYY'), F.NACIONALIDADE) = (SELECT TO_CHAR(F2.DT_NASCIMENTO, 'YYYY'), F2.NACIONALIDADE
                                                  FROM FUNCIONARIO F2
                                                  WHERE F2.ID_FUNC = '001');

--ANTIJOIN 
-- Projetar as ids das federações que não tem presidente
SELECT F.ID_FED
FROM FEDERACAO F
WHERE NOT EXISTS 
            (SELECT *
             FROM PRESIDENTE_DA_FEDERACAO PF
             WHERE PF.ID_FED = F.ID_FED);

--GROUP BY/HAVING
-- Projetar as médias dos salários dos jogadores por clube
SELECT L.COD, AVG(F.SALARIO) AS MEDIA_SALARIO
FROM LIGADO L INNER JOIN FUNCIONARIO F ON (L.ID_FUNC = F.ID_FUNC)
GROUP BY L.COD
HAVING L.FUNCAO = 'JOGADOR';

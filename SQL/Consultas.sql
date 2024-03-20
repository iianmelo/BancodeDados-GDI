-- CONSULTAS --
-------------------------------------------------------------------

-- OUTER JOIN (ok)
-- Nome das Empresas que não patrocinam competições
SELECT E.NOME
FROM EMPRESA E LEFT OUTER JOIN PAT_COMP PC 
ON (E.CNPJ = PC.CNPJ_EMPRESA)
WHERE PC.CNPJ_EMPRESA IS NULL;

-- SUBCONSULTA DO TIPO TABELA (ok)
-- NOME DE EMPRESAS QUE PATROCINAM CLUBES
SELECT NOME
FROM EMPRESA 
WHERE CNPJ IN (SELECT CNPJ_EMPRESA
               FROM PAT_CLUBE);

--INNER JOIN: (ok)
-- Nome das Empresas que patrocinam clubes e seu respectivo clube patrocinado:
SELECT E.NOME, C.NOME
FROM CLUBE C INNER JOIN PAT_CLUBE PC 
ON (C.CODIGO = PC.CODIGO_CLUBE) INNER JOIN EMPRESA E 
ON (PC.CNPJ_EMPRESA = E.CNPJ);

--SUBCONSULTA DO TIPO ESCALAR (ok)
-- Codigo dos clubes que a empresa de nome 'Emirates' patrocina:
SELECT PC.CODIGO_CLUBE
FROM PAT_CLUBE PC
WHERE PC.CNPJ_EMPRESA = (SELECT E.CNPJ
                 FROM EMPRESA E
                 WHERE E.NOME = 'EMIRATES');

--SUBCONSULTA DO TIPO LINHA (ok)
-- Projetar o nome dos funcionários que nasceram na mesmo ano e tem a mesma nacionalidade do funcionário de id '001'
SELECT F.NOME
FROM FUNCIONARIO F
WHERE (TO_CHAR(F.DT_NASCIMENTO, 'YYYY'), F.NACIONALIDADE) = (SELECT TO_CHAR(F2.DT_NASCIMENTO, 'YYYY'), F2.NACIONALIDADE
                                                             FROM FUNCIONARIO F2
                                                             WHERE F2.ID_FUNC = '001');

--ANTIJOIN (ok)
-- Projetar as ids das federações que não tem presidente
SELECT F.ID_FED
FROM FEDERACAO F
WHERE NOT EXISTS 
            (SELECT *
             FROM PRESIDENTE_DA_FEDERACAO PF
             WHERE PF.ID_FED = F.ID_FED);

-- SEMIJOIN (ok)
-- Projetar os nomes dos funcionários que já jogaram jogos
SELECT F.NOME
FROM FUNCIONARIO F
WHERE EXISTS
            (SELECT *
            FROM JOGO_PARTICIPA JP
            WHERE JP.ID_FUNC = F.ID_FUNC);
  
--GROUP BY/HAVING (ok)
-- Projetar as médias dos salários dos funcionários por clube
SELECT C.NOME, TRUNC(AVG(F.SALARIO),2) AS MEDIA_SALARIO
FROM LIGADO L INNER JOIN FUNCIONARIO F 
ON (L.ID_FUNC = F.ID_FUNC) INNER JOIN CLUBE C
ON (L.CODIGO_CLUBE = C.CODIGO)
GROUP BY C.NOME;

-- CONJUNTOS (ok)
-- Selecionar todas as empresas que já patrocinaram ou patrocinam um clube ou competicao
SELECT E.NOME
FROM EMPRESA E INNER JOIN PAT_CLUBE PCLUBE
ON PCLUBE.CNPJ_EMPRESA = E.CNPJ  
UNION
SELECT E.NOME
FROM EMPRESA E INNER JOIN PAT_COMP PCOMP
ON PCOMP.CNPJ_EMPRESA = E.CNPJ;

-- GATILHOS --
-------------------------------------------------------------------

-- printando o nome do novo funcionário ao ser alterado a coluna 'Id_Func' de um funcionario ja existente
CREATE OR REPLACE TRIGGER SejaBemVindoAoClube
BEFORE UPDATE OF ID_FUNC ON FUNCIONARIO
FOR EACH ROW
BEGIN
    IF(:NEW.ID_FUNC<>:OLD.ID_FUNC)THEN
        DBMS_OUTPUT.PUT_LINE('FUNCIONARIO NOVO:' ||:NEW.ID_FUNC || ' ' || :NEW.NOME);
    END IF;
END;

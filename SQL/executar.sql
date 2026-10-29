-- Executa o esquema, o povoamento e as consultas/PL-SQL na ordem.
-- Pensado para o SQL*Plus (Oracle). Rode a partir de qualquer diretório
-- com o caminho deste arquivo, por exemplo:
--   sqlplus system/<senha>@//localhost/FREEPDB1 @SQL/executar.sql

SET ECHO ON
SET FEEDBACK ON
SET SERVEROUTPUT ON SIZE UNLIMITED
SET SQLBLANKLINES ON
SET LINESIZE 220
SET PAGESIZE 100
SET TRIMSPOOL ON
SET VERIFY OFF
WHENEVER SQLERROR EXIT SQL.SQLCODE

PROMPT ===== CREATE =====
@@create.sql

PROMPT ===== POVOAMENTO =====
@@povoamento.sql

PROMPT ===== CONSULTAS E PL/SQL =====
@@Consultas.sql

PROMPT ===== FIM =====
EXIT

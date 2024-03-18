----------------------
-- POVOAMENTO DO BD --
----------------------

--Federacoes:
INSERT INTO FEDERACAO VALUES ('CBF', 1010); 
-- Brasil
INSERT INTO FEDERACAO VALUES ('AFA', 0420); 
-- Argentina
INSERT INTO FEDERACAO VALUES ('FPF', 0001); 
-- Pernambuco
INSERT INTO FEDERACAO VALUES ('CONMEBOL', 0002); 
-- America do Sul
INSERT INTO FEDERACAO VALUES ('UEFA', 0003); 
-- Europa
INSERT INTO FEDERACAO VALUES ('RFEF', 0004); 
-- Espanha
INSERT INTO FEDERACAO VALUES ('FA', 0005); 
-- Inglaterra
INSERT INTO FEDERACAO VALUES ('FFF', 1919); 
-- França
INSERT INTO FEDERACAO VALUES ('DFB', 2121); 
-- Alemanha
INSERT INTO FEDERACAO VALUES ('FIGC', 1111); 
-- Italia
INSERT INTO FEDERACAO VALUES ('FIFA', 0000); 
-- Mundo


--Presidente da Federacao:
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Ednaldo Rodrigues', 0001, 1010); 
-- Brasil
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Claudio "Chiqui" Fabián Tapia', 0002, 0420); 
-- Argentina
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Evandro Barros', 0003, 0001); 
-- Pernambuco
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Alejandro Domínguez', 0004, 0002); 
-- America do Sul
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Aleksander Ceferin', 0005, 0003); 
-- Europa
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Luis Rubiales', 0006, 0004); 
-- Espanha
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Debbie Hewitt', 0007, 0005); 
-- Inglaterra
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Philippe Diallo', 0008, 1919); 
-- Franca
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Bernd Neuendorf', 0009, 2121); 
-- Alemanha
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Gabriele Gravina', 0010, 1111); 
-- Italia
INSERT INTO PRESIDENTE_DA_FEDERACAO VALUES ('Gianni Infantino', 0011, 0000); 
-- Mundo

--Estadio:
INSERT INTO ESTADIO VALUES ('CAMP NOU', 0000, 99355, 'Espanha', 'Barcelona', 09078789, 45);
INSERT INTO ESTADIO VALUES ('ILHA DO RETIRO', 0001, 26418, 'Brasil', 'Recife', 0000000, 10);
INSERT INTO ESTADIO VALUES ('ARRUDA', 0002, 60044, 'Brasil', 'Recife', 87612955, 35);
INSERT INTO ESTADIO VALUES ('AFLITOS', 0003, 22856, 'Brasil', 'Recife', 897239, 09);
INSERT INTO ESTADIO VALUES ('MARACANÃ', 0004, 78838, 'Brasil', 'Rio de Janeiro', 97563255, 72);
INSERT INTO ESTADIO VALUES ('SANTIAGO BERNABEU', 0005, 81044, 'Espanha', 'Madrid', 825335, 83);
INSERT INTO ESTADIO VALUES ('LA BOMBONERA', 0006, 55000, 'Argentina', 'Buenos Aires', 8723478, 94);
INSERT INTO ESTADIO VALUES ('OLD TRAFORD', 0007, 74310, 'Inglaterra', 'Manchester', 78923, 011);
INSERT INTO ESTADIO VALUES ('WEMBLEY', 0008, 90000, 'Inglaterra', 'Londres', 8931245, 101);
INSERT INTO ESTADIO VALUES ('STANFORD BRIDGE', 0009, 40341, 'Inglaterra', 'Londres', 9727865, 345);
INSERT INTO ESTADIO VALUES ('SAN SIRO', 0010, 75817, 'Italia', 'Milão', 385345678, 78);
INSERT INTO ESTADIO VALUES ('ARENA PERNAMBUCO', 0011, 44300, 'Brasil', 'Recife', 72558395, 99);
INSERT INTO ESTADIO VALUES ('ALLIANZ ARENA', 0012, 75024, 'Alemanha', 'Munique', 38573863, 74);
INSERT INTO ESTADIO VALUES ('SIGNAL IDUNA PARK', 0013, 81365, 'Alemanha', 'Dortmund', 3465863, 97);
INSERT INTO ESTADIO VALUES ('PARC DES PRINCES', 0014, 48583, 'França', 'Paris', 876385628, 56);
INSERT INTO ESTADIO VALUES ('BAY ARENA', 0015, 30210, 'Alemanha', 'Leverkusen', 863856195, 35);
INSERT INTO ESTADIO VALUES ('MONUMENTAL', 0016, 84567, 'Argentina', 'Buenos Aires', 78232415, 97);
INSERT INTO ESTADIO VALUES ('MORUMBIS', 0017, 66795, 'Brasil', 'São Paulo', 171365112, 102);
INSERT INTO ESTADIO VALUES ('ALLIANZ PARQUE', 0018, 43713, 'Brasil', 'São Paulo', 11516189, 06);
INSERT INTO ESTADIO VALUES ('NEOQUIMICA ARENA', 0019, 49205, 'Brasil', 'São Paulo', 18121532, 04);
INSERT INTO ESTADIO VALUES ('VILA BELMIRO', 0020, 30108, 'Brasil', 'Santos',718619132, 45);
INSERT INTO ESTADIO VALUES ('SAO JANUARIO', 0021, 21880, 'Brasil', 'Rio de Janeiro', 11418292, 27);
INSERT INTO ESTADIO VALUES ('ARENA MRV', 0022, 46000, 'Brasil', 'Belo Horizonte', 61419352, 49);
INSERT INTO ESTADIO VALUES ('ARENA DO GREMIO', 0023, 55396, 'Brasil', 'Porto Alegre', 81114152, 39);
INSERT INTO ESTADIO VALUES ('BEIRA RIO', 0024, 50842, 'Brasil', 'Porto Alegre', 96114122, 39);
INSERT INTO ESTADIO VALUES ('ARENA FONTE NOVA', 0025, 48902, 'Brasil', 'Salvador', 11251112,67);
INSERT INTO ESTADIO VALUES ('LEONIDAS CASTRO', 0026, 16200, 'Brasil', 'Belem', 11111112, 87);
INSERT INTO ESTADIO VALUES ('ANFIELD', 0027, 61276, 'Inglaterra', 'Liverpool', 67765675, 06);
INSERT INTO ESTADIO VALUES ('CASTELAO', 0028, 64000, 'Brasil', 'Fortaleza', 6567989024, 39);

--Competicao:
INSERT INTO COMPETICAO VALUES ('Campeonato Pernambucano 2023', 1, 0001, 2023); 
-- 3 Jogos
INSERT INTO COMPETICAO VALUES ('Campeonato Pernambucano 2024', 2, 0001, 2024); 
-- 1 jogo
INSERT INTO COMPETICAO VALUES ('Champions League 2022', 2, 0003, 2022); 
-- 1 jogo 
INSERT INTO COMPETICAO VALUES ('Champions League 2015', 1, 0003, 2015); 
-- 1 jogo 
INSERT INTO COMPETICAO VALUES ('Europa League 2023', 3, 0003, 2023); 
-- 1 jogo 
INSERT INTO COMPETICAO VALUES ('Campeonato Argentino 2023', 1, 0420, 2023); 
-- 1 jogo
INSERT INTO COMPETICAO VALUES ('La Liga 2023', 1, 0004, 2023); 
-- 3 jogos 
INSERT INTO COMPETICAO VALUES ('Premier League 2023', 3, 0005, 2023); 
-- 3 jogos 
INSERT INTO COMPETICAO VALUES ('Premier League 2019', 1, 0005, 2019); 
-- 1 jogo
INSERT INTO COMPETICAO VALUES ('Premier League 2020', 2, 0005, 2020); 
-- 1 jogo
INSERT INTO COMPETICAO VALUES ('Ligue 1 2022', 1, 1919, 2022); 
-- 1 jogo
INSERT INTO COMPETICAO VALUES ('Serie A 2024', 1, 1111, 2024); 
-- 1 jogo
INSERT INTO COMPETICAO VALUES ('Brasileirao 2023', 4, 1010, 2023); 
-- 1 jogo
INSERT INTO COMPETICAO VALUES ('Copa do Brasil 2023', 3, 1010, 2023); 
-- 1 jogo
INSERT INTO COMPETICAO VALUES ('Brasileirao 2019', 2, 1010, 2019); 
-- 1 jogo
INSERT INTO COMPETICAO VALUES ('Copa do Nordeste 2016', 1, 1010, 2016); 
-- 1 jogo
INSERT INTO COMPETICAO VALUES ('Bundesliga 2023', 1, 2121, 2023);
 -- 1 jogo
INSERT INTO COMPETICAO VALUES ('Libertadores 2019', 2, 0002, 2019);
 -- 1 jogo
INSERT INTO COMPETICAO VALUES ('Libertadores 2017', 1, 0002, 2017);
 -- 1 jogo
INSERT INTO COMPETICAO VALUES ('Mundial de Clubes 2021', 1, 0000, 2021);
 -- 1 jogo

--Clubes:
INSERT INTO CLUBES VALUES ('SPORT CLUB DO RECIFE', 0000, 'Leao da Ilha', 'ILHA DO RETIRO');
INSERT INTO CLUBES VALUES ('SANTA CRUZ', 0001, 'Cobra Coral', 'ARRUDA');
INSERT INTO CLUBES VALUES ('NAUTICO', 0024, 'Timbu', 'AFLITOS');
INSERT INTO CLUBES VALUES ('CHELSEA', 0003, 'Lion', 'STANFORD BRIDGE');
INSERT INTO CLUBES VALUES ('BARCELONA', 0004, 'Cachorro Cobi', 'CAMP NOU');
INSERT INTO CLUBES VALUES ('REAL MADRID', 0005, 'Cachorro Violin', 'SANTIAGO BERNABEU');
INSERT INTO CLUBES VALUES ('MANCHESTER UNITED', 0006, 'Fred The Red Devil', 'OLD TRAFFORD');
INSERT INTO CLUBES VALUES ('MANCHESTER CITY', 0007, 'Moonchester', 'ETIHAD STADIUM');
INSERT INTO CLUBES VALUES ('BAYERN MUNCHEN', 0008, 'Bear Berni', 'ALLIANZ ARENA');
INSERT INTO CLUBES VALUES ('BORUSSIA DORTMUND', 0009, 'Junter Bee', 'SIGNAL IDUNA PARK');
INSERT INTO CLUBES VALUES ('BAYER LEVERKUSEN', 0010, 'Brian The Lion', 'BAY ARENA');
INSERT INTO CLUBES VALUES ('LIVERPOOL', 0011, 'Mighty Red Bird', 'ANFIELD');
INSERT INTO CLUBES VALUES ('MILAN', 0012, 'Milanello Devil', 'SAN SIRO');
INSERT INTO CLUBES VALUES ('ROMA', 0013, 'Romolo Wolf', 'ESTADIO OLIMPICO DE ROMA');
INSERT INTO CLUBES VALUES ('INTER MILAN', 0014, 'Biscione Snake', 'SAN SIRO');
INSERT INTO CLUBES VALUES ('PSG', 0015, 'Gervais Fox', 'PARC DES PRINCES');
INSERT INTO CLUBES VALUES ('LYON', 0016, 'Lyou Lion', 'GROUPAMA STADIUM');
INSERT INTO CLUBES VALUES ('BOCA JUNIORS', 0017, 'Chanxeneize', 'LA BOMBONERA');
INSERT INTO CLUBES VALUES ('RIVER PLATE', 0018, 'Gallo', 'ESTADIO MONUMENTAL');
INSERT INTO CLUBES VALUES ('FLAMENGO', 0019, 'Urubu', 'MARACANA');
INSERT INTO CLUBES VALUES ('PALMEIRAS', 0020, 'Porco', 'ALLIANZ PARQUE');
INSERT INTO CLUBES VALUES ('VASCO DA GAMA', 0021, 'Pedro Alvares Cabral', 'SAO JANUARIO');
INSERT INTO CLUBES VALUES ('ATLETICO MINEIRO', 0022, 'Galo', 'ARENA MRV');
INSERT INTO CLUBES VALUES ('INTERNACIONAL', 0023, 'Saci Perere', 'BEIRA RIO');
INSERT INTO CLUBES VALUES ('GREMIO', 0002, 'Mosqueteiro Tarcisio', 'ARENA DO GREMIO');
INSERT INTO CLUBES VALUES ('VITORIA', 0025, 'Leao da Barra', 'BARRADAO');
INSERT INTO CLUBES VALUES ('BAHIA', 0026, 'Superman', 'ARENA FONTE NOVA');
INSERT INTO CLUBES VALUES ('FORTALEZA', 0027, 'Eh o Lion', 'CASTELAO');
INSERT INTO CLUBES VALUES ('CORINTHIANS', 0028, 'Mosqueteiro', 'NEOQUIMICA ARENA');
INSERT INTO CLUBES VALUES ('SAO PAULO FC', 0042, 'Santo Paulo', 'MORUMBIS');
INSERT INTO CLUBES VALUES ('BOTAFOGO', 0030, 'Cachorro', 'ENGENHAO');
INSERT INTO CLUBES VALUES ('SANTOS', 0031, 'Peixao da Vila', 'VILA BELMIRO');
INSERT INTO CLUBES VALUES ('ARSENAL', 0032, 'Gunnersaurus', 'EMIRATES STADIUM');
INSERT INTO CLUBES VALUES ('JUVENTUS', 0033, 'Zebra', 'JUVENTUS STADIUM');
INSERT INTO CLUBES VALUES ('SEVILLA', 0034, 'Gunnersaurus', 'RAMON SANCHEZ PIZJUAN');

--Jogo:
INSERT INTO JOGO VALUES (0001 , TO_DATE('06/06/2015','DD/MM/YYYY'), 'FINAL', 1, 0003, 0033,0004);
 --Champions League 15
INSERT INTO JOGO VALUES (0002 , TO_DATE('28/05/2022','DD/MM/YYYY'), 'FINAL', 2, 0003, 0005,0011); 
-- Champions League 22
INSERT INTO JOGO VALUES (0003 , TO_DATE('31/05/2023','DD/MM/YYYY'), 'FINAL', 1, 0003, 0034, 0013);
 --EUROPA LEAGUE 23
INSERT INTO JOGO VALUES (0004 , TO_DATE('11/03/2023','DD/MM/YYYY'), 'PRIMEIRA FASE', 1, 0001, 0001, 0000); 
--Pernambucano 23
INSERT INTO JOGO VALUES (0005 , TO_DATE('06/06/2023','DD/MM/YYYY'), 'PRIMEIRA FASE', 1, 0001, 0000, 0024);
 --Pernambucano 23
INSERT INTO JOGO VALUES (0006 , TO_DATE('15/01/2023','DD/MM/YYYY'), 'PRIMEIRA FASE', 1, 0001, 0024, 0001); 
--Pernambucano 23
INSERT INTO JOGO VALUES (0007 , TO_DATE('05/02/2023','DD/MM/YYYY'), '20ª RODADA', 1, 0004, 0034, 0004);
 --la liga 23
-- INSERT INTO JOGO VALUES (0008 ,'01X02', TO_DATE('19/03/2023','DD/MM/YYYY'), '26ª RODADA', 1, 0004, 0005, 0005);
--  --la liga 23
-- INSERT INTO JOGO VALUES (0009 ,'02X01', TO_DATE('27/05/2023','DD/MM/YYYY'), '37ª RODADA', 1, 0004, 0005, 0034); 
-- --la liga 23
-- INSERT INTO JOGO VALUES (0010 ,'03X01', TO_DATE('15/02/2023','DD/MM/YYYY'), '12ª RODADA', 3, 0005, 0007, 0032); 
-- --Premier League 23
-- INSERT INTO JOGO VALUES (0011 ,'00X00', TO_DATE('21/01/2023','DD/MM/YYYY'), '21ª RODADA', 3, 0005, 0007, 0006); 
-- --Premier League 23
-- INSERT INTO JOGO VALUES (0012 ,'01X03', TO_DATE('22/01/2023','DD/MM/YYYY'), '21ª RODADA', 3, 0005, 0006, 0032); 
-- --Premier League 23
-- INSERT INTO JOGO VALUES (0013 ,'02X00', TO_DATE('24/04/2019','DD/MM/YYYY'), '31ª RODADA', 1, 0005, 0004, 0033); 
-- --Premier League 19
-- INSERT INTO JOGO VALUES (0014 ,'01X03', TO_DATE('10/03/2019','DD/MM/YYYY'), '31ª RODADA', 1, 0005, 0006, 0032); 
-- --Premier League 19
-- INSERT INTO JOGO VALUES (0015 ,'01X03', TO_DATE('29/09/2018','DD/MM/YYYY'), '7ª RODADA', 1, 0005, 00011, 0003); 
-- --Premier League 19
-- INSERT INTO JOGO VALUES (0016 ,'01X02', TO_DATE('12/02/2022','DD/MM/YYYY'), 'FINAL', 1, 0000, 0020, 0003); 
-- --Mundial de clubes 21 
-- INSERT INTO JOGO VALUES (0017 ,'00X01', TO_DATE('04/02/2024','DD/MM/YYYY'), '23ª RODADA', 1, 1111, 0033, 0014); 
-- --Serie A 2024
-- INSERT INTO JOGO VALUES (0018 ,'01X01', TO_DATE('09/01/2022','DD/MM/YYYY'), '20ª RODADA', 1, 1919, 0015, 0016); 
-- --Ligue 1 2022
-- INSERT INTO JOGO VALUES (0019 ,'00X02', TO_DATE('19/01/2020','DD/MM/YYYY'), '23ª RODADA', 2, 0005, 0006, 0011); 
-- --Premier League 2020
-- INSERT INTO JOGO VALUES (0020 ,'00X01', TO_DATE('07/05/2023','DD/MM/YYYY'), '15ª RODADA', 1, 0420, 0017, 0018); 
-- --Campeonato Argentino 2023
-- INSERT INTO JOGO VALUES (0021 ,'04X03', TO_DATE('01/11/2023','DD/MM/YYYY'), '31ª RODADA', 4, 1010, 0020, 0030); 
-- --Brasileirão 2023
-- INSERT INTO JOGO VALUES (0022 ,'00X04', TO_DATE('06/06/2015','DD/MM/YYYY'), '38ª RODADA', 2, 1010, 0019, 0031); 
-- --Brasileirão 2019
-- INSERT INTO JOGO VALUES (0023 ,'00X01', TO_DATE('20/09/2017','DD/MM/YYYY'), 'QUARTAS DE FINAL(JOGO DE VOLTA)', 1, 0002, 0030, 0002); 
-- --Libertadores 2017
-- INSERT INTO JOGO VALUES (0024 ,'00X01', TO_DATE('24/02/2024','DD/MM/YYYY'), '9ª RODADA', 2, 0001, 0000, 0024); 
-- --Pernambucano 2024
-- INSERT INTO JOGO VALUES (0025 ,'01X00', TO_DATE('17/09/2023','DD/MM/YYYY'), 'FINAL(JOGO DE IDA)', 3, 1010, 0042, 0019); 
-- --Copa do Brasil 2023
-- INSERT INTO JOGO VALUES (0026 ,'02X04', TO_DATE('01/04/2023','DD/MM/YYYY'), '26ª RODADA', 1, 2121, 0009, 0008); 
-- --Bundesliga 2023
-- INSERT INTO JOGO VALUES (0027 ,'01X00', TO_DATE('17/04/2016','DD/MM/YYYY'), 'SEMIFINAL(JOGO DE VOLTA)', 1, 1010, 0001, 0026); 
-- --Copa do Nordeste 2016
-- INSERT INTO JOGO VALUES (0028 ,'01X02', TO_DATE('23/11/2019','DD/MM/YYYY'), 'FINAL', 2, 0002, 0018, 0019); 
-- --Libertadores 2019

--Arbitro:
INSERT INTO ARBITRO VALUES('WILTON PEREIRA SAMPAIO', 00, TO_DATE('08/01/1980','DD/MM/YYYY'),'BRASILEIRO');
INSERT INTO ARBITRO VALUES('ANDERSON DARONCO', 01, TO_DATE('14/07/1983','DD/MM/YYYY'),'BRASILEIRO');
INSERT INTO ARBITRO VALUES('RAPHAEL CLAUS', 02, TO_DATE('27/10/1981','DD/MM/YYYY'),'BRASILEIRO');
INSERT INTO ARBITRO VALUES('VINCIC S.', 03, TO_DATE('19/04/1999','DD/MM/YYYY'),'ESLOVAQUIO');
INSERT INTO ARBITRO VALUES('VUADEN', 04, TO_DATE('05/08/1988','DD/MM/YYYY'),'BRASILEIRO');
INSERT INTO ARBITRO VALUES('ANTONY TAYLOR', 05, TO_DATE('02/06/1970','DD/MM/YYYY'),'INGLES');
INSERT INTO ARBITRO VALUES('OLIVER M.', 06, TO_DATE('04/07/1984','DD/MM/YYYY') ,'FRANCES');
INSERT INTO ARBITRO VALUES('GUSTTAVO LIMA', 07, TO_DATE('18/08/1979','DD/MM/YYYY') ,'BRASILEIRO');
INSERT INTO ARBITRO VALUES('ESKAS E.', 08, TO_DATE('12/11/1975','DD/MM/YYYY') ,'NORUEGUES');
INSERT INTO ARBITRO VALUES('MASSA D', 09, TO_DATE('01/03/1992','DD/MM/YYYY'),'ITALIANO');
INSERT INTO ARBITRO VALUES('TEJERA G.', 10, TO_DATE('11/04/1985','DD/MM/YYYY') ,'URUGUAIO');
INSERT INTO ARBITRO VALUES('HERRERA A.', 11, TO_DATE('30/01/1999','DD/MM/YYYY') ,'VENEZUELANO');
INSERT INTO ARBITRO VALUES('ZWAYER F.', 12, TO_DATE('27/05/1993','DD/MM/YYYY') ,'ALEMAO');
INSERT INTO ARBITRO VALUES('STEFAN B.', 13, TO_DATE('22/04/1976','DD/MM/YYYY') ,'ALEMAO');
INSERT INTO ARBITRO VALUES('GOZUBUYUK S.', 14, TO_DATE('20/07/1986','DD/MM/YYYY') , 'HOLANDES');
INSERT INTO ARBITRO VALUES('ROBSON F.', 15, TO_DATE('10/03/1988','DD/MM/YYYY') , 'ESPANHOL');

--Empresas:
INSERT INTO EMPRESA VALUES('SPOTIFY', 306412);
INSERT INTO EMPRESA VALUES('PUMA', 203693);
INSERT INTO EMPRESA VALUES('CREFISA',756940);
INSERT INTO EMPRESA VALUES('PIXBET', 8515);
INSERT INTO EMPRESA VALUES('BETVIP', 841480);
INSERT INTO EMPRESA VALUES('SANTANDER', 576060);
INSERT INTO EMPRESA VALUES('UMBRO', 543086);
INSERT INTO EMPRESA VALUES('ADIDAS', 628934);
INSERT INTO EMPRESA VALUES('KAPPA', 501203);
INSERT INTO EMPRESA VALUES('NIKE', 739040);
INSERT INTO EMPRESA VALUES('UNIMED', 406363);
INSERT INTO EMPRESA VALUES('CIMENTO NASSAU', 780224);
INSERT INTO EMPRESA VALUES('NOVIBET', 550468);
INSERT INTO EMPRESA VALUES('GAV RESORTS', 225766);
INSERT INTO EMPRESA VALUES('TIM', 499969);
INSERT INTO EMPRESA VALUES('BANRISUL', 24741);
INSERT INTO EMPRESA VALUES('BETANO', 396686);
INSERT INTO EMPRESA VALUES('BMG', 200224);
INSERT INTO EMPRESA VALUES('BRASILIT', 418335);
INSERT INTO EMPRESA VALUES('CIMED', 622758);
INSERT INTO EMPRESA VALUES('ESPORTES DA SORTE', 499827);
INSERT INTO EMPRESA VALUES('SUPERMERCADOS BH', 105919);
INSERT INTO EMPRESA VALUES('QATAR AIRWAYS', 119268);
INSERT INTO EMPRESA VALUES('ETIHAD AIRWAYS', 149253);
INSERT INTO EMPRESA VALUES('TEAMVIEWER', 737062);
INSERT INTO EMPRESA VALUES('STANDARD CHARTERED', 802234);
INSERT INTO EMPRESA VALUES('JEEP', 970076);
INSERT INTO EMPRESA VALUES('T-MOBILE', 916183);
INSERT INTO EMPRESA VALUES('EMIRATES', 740819);
INSERT INTO EMPRESA VALUES('HEINEKEN', 158122);
INSERT INTO EMPRESA VALUES('PLAYSTATION', 693212);
INSERT INTO EMPRESA VALUES('LAY`S', 350016);
INSERT INTO EMPRESA VALUES('MASTERCARD', 504127);
INSERT INTO EMPRESA VALUES('FEDEX', 99434);
INSERT INTO EMPRESA VALUES('TURKISH AIRLINES', 327879);
INSERT INTO EMPRESA VALUES('EA', 353546);

--funcionarios
INSERT INTO FUNCIONARIO VALUES('NOME', id_func , salario , TO_DATE('06/06/2015','DD/MM/YYYY'), 'NACIONALIDADE');
INSERT INTO FUNCIONARIO VALUES('Ze da Silva', 001 ,500, TO_DATE('11/03/1999','DD/MM/YYYY'), 'BRASILEIRO' );
INSERT INTO FUNCIONARIO VALUES('Almir', 002 , 800, TO_DATE('23/02/1990','DD/MM/YYYY'), 'BRASILEIRO');
INSERT INTO FUNCIONARIO VALUES('Ancelotti', 003, 150000 , TO_DATE('25/02/1960','DD/MM/YYYY'), 'FRANCES');
INSERT INTO FUNCIONARIO VALUES('Seu Zeca', 004 , 300, TO_DATE('22/01/1989','DD/MM/YYYY'), 'BRASILEIRO');
INSERT INTO FUNCIONARIO VALUES('Francisco da Limpeza', 005 , 100, TO_DATE('01/05/1999','DD/MM/YYYY'), 'BRASILEIRO');
INSERT INTO FUNCIONARIO VALUES('Neymar', 006 , 100000, TO_DATE('02/05/1994','DD/MM/YYYY'), 'BRASILEIRO');
INSERT INTO FUNCIONARIO VALUES('Messi', 007 , 500000 , TO_DATE('21/06/1992','DD/MM/YYYY'), 'ARGETINO');
INSERT INTO FUNCIONARIO VALUES('Romarinho', 008 , 80000 , TO_DATE('06/09/2000','DD/MM/YYYY'), 'BRASILEIRO');
INSERT INTO FUNCIONARIO VALUES('Ze Roberto', 009 , 100000 , TO_DATE('11/07/1998','DD/MM/YYYY'), 'BRASILEIRO');
INSERT INTO FUNCIONARIO VALUES('Caíque França', 010 , 450000 , TO_DATE('12/06/1990','DD/MM/YYYY'), 'BRASILEIRO');
INSERT INTO FUNCIONARIO VALUES('Pulisic', 011 , 150000 , TO_DATE('11/06/1986','DD/MM/YYYY'), 'AMERICANO');
INSERT INTO FUNCIONARIO VALUES('Mbappe', 012 , 800000 , TO_DATE('12/02/1989','DD/MM/YYYY'), 'FRANCES');
INSERT INTO FUNCIONARIO VALUES('Palmer', 013  , 95000 , TO_DATE('14/07/1977','DD/MM/YYYY'), 'INGLES');
INSERT INTO FUNCIONARIO VALUES('Lukaku', 014 , 105000 , TO_DATE('14/05/1975','DD/MM/YYYY'), 'BELGA');
INSERT INTO FUNCIONARIO VALUES('Haaland', 015 , 900000, TO_DATE('17/01/2015','DD/MM/YYYY'), 'NORUEGUES');
INSERT INTO FUNCIONARIO VALUES('Cristiano Ronaldo', 016 , 1000000 , TO_DATE('18/02/1998','DD/MM/YYYY'), 'PORTUGUES');

INSERT INTO TEM VALUES (00, 0001, 'A_Campo','01X03', 0008);
INSERT INTO TEM VALUES (01, 0001, 'Bandeirinha','01X03', 0008);
INSERT INTO TEM VALUES (01, 0004, 'A_Campo','00x02', 0001);
INSERT INTO TEM VALUES (02, 0005, 'A_Campo','02X02', 0001);
INSERT INTO TEM VALUES (02, 0006, 'A_Campo','01X03', 0004);


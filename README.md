# GDI - Mini-Mundo Futebol
Repositório referente ao projeto da disciplina de Gerenciamento de Dados e Informação do Centro de Informática da UFPE. O objetivo do sistema é armazenar alguns dados sobre futebol em geral.
# Mini-Mundo
Um clube é identificado pelo seu ID do clube e contém informações a respeito do seu nome, mascote e sede. 

Um funcionário é identificado pelo seu ID Funcionário e contém informações a respeito de seu salário, nome, data de nascimento e nacionalidade. Um funcionário pode ter sido ligado a vários clubes na mesma temporada e na mesma função. Um funcionário pode permanecer em um clube por várias temporadas na mesma função. Um funcionário pode exercer em um clube várias funções na mesma temporada. Vários funcionários podem atuar em um clube na mesma função em uma temporada. Um funcionário pode ser um jogador.

Um jogo é identificado pelo seu código e contém informações a respeito do placar, data, hora e a fase da competição a qual ele pertence. Um jogador participa de vários jogos, em cada um ele marca um número x de gols, dá um número x de assistências, joga em uma posição, pode receber vários cartões-cada cartão é dado em um minuto do jogo e tem uma cor. Em um jogo, vários jogadores entram em campo. O jogo precisa ter um clube mandante e um clube visitante. O clube pode ser mandante em vários jogos e pode ser visitante em vários jogos. 

Um estádio é identificado pelo código de estádio e contém informações a respeito de seu nome, sua capacidade e seu endereço composto por país, cidade, CEP e o número da rua. 

Um árbitro é identificado pelo seu código e contém informações a respeito de seu nome, sua data de nascimento e sua nacionalidade. Um árbitro terá uma função em um jogo no estádio. Em um jogo no estádio, há vários árbitros exercendo funções. Em um estádio específico, um árbitro pode exercer uma função diferente para cada vez que ele for trabalhar em um jogo lá. 

Um troféu é identificado pelo seu nome e contém informações a respeito de seu valor.

Uma empresa é identificada pelo seu CNPJ e contém informações a respeito de seu nome. Uma empresa pode patrocinar vários clubes a partir de uma mesma data de assinatura do contrato. Um clube pode ser patrocinado por várias empresas a partir de uma mesma data. Uma empresa pode patrocinar o mesmo clube a partir de diferentes datas. Cada patrocínio tem um valor e uma duração.

Uma federação é identificada pelo ID federação. Um árbitro pode fazer parte de várias federações. Uma federação tem vários árbitros no seu quadro. 

Uma competição é identificada pelo ID federação+ID artificial e contém informações a respeito de seu nome e da sua temporada. Uma federação realiza várias competições. Uma competição precisa ser organizada por uma federação. Uma competição menor pode garantir vaga para várias competições maiores. É possível se classificar para uma competição maior via várias competições menores. Um clube participa de várias competições. Em uma competição participam vários clubes, cada qual tem uma colocação. Nessa participação, pode ter um troféu. Um troféu é dado para uma única participação.  
Uma empresa pode patrocinar várias competições a partir de uma mesma data de assinatura do contrato. Uma competição pode ser patrocinada por várias empresas a partir de uma mesma data. Uma empresa pode patrocinar a mesma competição a partir de diferentes datas. Cada patrocínio tem um valor e uma duração.
Uma competição tem vários jogos. Um jogo vale para uma única competição.

Um presidente de federação é identificado pelo seu ID e contém informações a respeito de seu nome. Um presidente precisa presidir uma federação. Uma federação tem apenas um presidente.

# Curso MySQL #07 - Manipulando Linhas (UPDATE, DELETE e TRUNCATE)
# https://youtu.be/wXViczeTr6Q
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/manipulando-linhas-update-delete-e-truncate/

"""
Aula 07 - Curso MySQL #07 - Manipulando Linhas (UPDATE, DELETE e TRUNCATE)

MANIPULANDO REGISTROS (Linhas ou Tuplas, samesame)

- Nas aulas anteriores, aprendemos a adicionar colunas (INSERT INTO) e linhas...

"""
USE cadastro;
SELECT * FROM gafanhotos;
# Observando o "Result Set" vemos que: 
#   - as LINHAS são os registros (ou tuplas)... 
#   - as COLUNAS são os campos (ou atributos)...
#   - ALTER TABLE permite alterar as colunas...
#   Agora, vamos alterar as LINHAS! =) 

SELECT * FROM cursos;
INSERT INTO cursos VALUES
('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
('2', 'Algoritmos', 'Lógica da Programação', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de Photoshop CC', '10', '8', '2014'),
('4', 'PGP', 'Curso de PHP para Iniciantes', '40', '20', '2010'),
('5', 'Jarva', 'Introdução à Linguagem Java', '10', '29', '2000'),
('6', 'MySQL', 'Bancos de Dados MySQL', '30', '15', '2016'),
('7', 'Word', 'Curso Completo de Word', '40', '30', '2016'),
('8', 'Sapateado', 'Danças Rítmicas', '40', '30', '2018'),
('9', 'Cozinha Árabe', 'Aprenda a Fazer Kibe', '40', '30', '2018'),
('10', 'YouTuber', 'Gerar Polêmica e Ganhar Inscritos', '5', '2', '2018');

SELECT * FROM cursos;

# Agora, podemos perceber que nosso BD possui cadastro de duas coisas: "gafanhotos" e "cursos".
# Em 'gafanhotos' temos (id, nome, profissao, nascimento, sexo, peso, altura, nacionalidade) e em 'cursos' temos (idcursos, nome, descricao, carga, totaulas, ano)
# O 'id' de gafanhotos é a PRIMARY KEY. O 'idcurso' também é PRIMARY KEY.

# Ao final, teremos uma tablea, ainda com alguns "erros":
#     - nome HTML4 está errado
#     - nome PGP está errado
#     - nome Jarva está errado
#     - carga 10 do iducrso 5 está errada
#     - ano 2010 e 2000 do idcurso 4 e 5 estão errados

# Vamos começar a MANIPULAR essas linhas. Lembrando que para cada COMANDO eu posso MANIPULAR UMA ÚNICA LINHA. 
# Porém, DENTRO DE UMA LINHA, ou seja, apenas com um COMANDO, eu ainda posso alterar várias COLUNAS ao mesmo tempo.
# MODIFICANDO LINHAS INCORRETAS

UPDATE cursos
SET nome = 'HTML5'
WHERE idcurso = '1';
# 3	13	23:57:09	UPDATE cursos SET nome = 'HTML5' WHERE idcurso = '1'	1 row(s) affected Rows matched: 1  Changed: 1  Warnings: 0	0.062 sec

UPDATE cursos
SET nome = 'PHP', ano = '2015'
WHERE idcurso = '4';
# 3	14	23:58:17	UPDATE cursos  SET nome = 'PHP', ano = '2015'  WHERE idcurso = '4'	1 row(s) affected  Rows matched: 1  Changed: 1  Warnings: 0	0.000 sec

UPDATE cursos
SET nome = 'Java', carga = '40', ano = '2015'
WHERE idcurso = '5'
LIMIT 1; # Esse PARÂMETRO ajuda a aplicar as alterações em APENAS UMA LINHA (ao invés de várias ao mesmo tempo), embora nossa segurança seja o 'idcurso' que é UNIQUE e PRIMARY KEY. 
# 3	15	00:01:16	UPDATE cursos SET nome = 'Java', carga = '40', ano = '2015' WHERE idcurso = '5' LIMIT 1	1 row(s) affected Rows matched: 1  Changed: 1  Warnings: 0	0.000 sec

"""
1	HTML5	Curso de HTML5	40	37	2014
2	Algoritmos	Lógica da Programação	20	15	2014
3	Photoshop	Dicas de Photoshop CC	10	8	2014
4	PHP	Curso de PHP para Iniciantes	40	20	2015
5	Java	Introdução à Linguagem Java	40	29	2015
6	MySQL	Bancos de Dados MySQL	30	15	2016
7	Word	Curso Completo de Word	40	30	2016
8	Sapateado	Danças Rítmicas	40	30	2018
9	Cozinha Árabe	Aprenda a Fazer Kibe	40	30	2018
10	YouTuber	Gerar Polêmica e Ganhar Inscritos	5	2	2018
"""

# Agora vamos escrever um teste para ALTERAR VÁRIAS linhas ao mesmo tempo, mas vamos usar um WHERE genérico ao invés do PRIMARY KEY.
# Edit > Preferences > SQL Editor > UNCHECK Safe Updates > Reconnect to DBMS, pra poder alterar várias linhas ao mesmo tempo.
UPDATE cursos
SET ano = '2050', carga = '800'
WHERE ano = '2018';
# 3	17	00:05:18	UPDATE cursos SET ano = '2050', carga = '800' WHERE ano = '2018'	3 row(s) affected Rows matched: 3  Changed: 3  Warnings: 0	0.047 sec
"""
8	Sapateado	Danças Rítmicas	800	30	2050
9	Cozinha Árabe	Aprenda a Fazer Kibe	800	30	2050
10	YouTuber	Gerar Polêmica e Ganhar Inscritos	800	2	2050
"""

UPDATE cursos
SET ano = '2018', carga = '0'
WHERE ano = '2050'
LIMIT 1; # Usar sempre como batente de segurança! 
"""
8	Sapateado	Danças Rítmicas	0	30	2018
9	Cozinha Árabe	Aprenda a Fazer Kibe	800	30	2050
10	YouTuber	Gerar Polêmica e Ganhar Inscritos	800	2	2050
"""

# Vamos apagar as três últimas linhas, mas não vale APAGAR com vazio.
# UPDATE mexe e altera as linhas existentes, mas MANTÉM elas lá! 

# REMOVENDO UMA LINHA
# Apagar apenas UM registro com chave primária idcurso = '8'
DELETE FROM cursos
WHERE idcurso = '8';
# 3	21	00:10:18	DELETE FROM cursos  WHERE idcurso = '8'	1 row(s) affected	0.031 sec
"""
1	HTML5	Curso de HTML5	40	37	2014
2	Algoritmos	Lógica da Programação	20	15	2014
3	Photoshop	Dicas de Photoshop CC	10	8	2014
4	PHP	Curso de PHP para Iniciantes	40	20	2015
5	Java	Introdução à Linguagem Java	40	29	2015
6	MySQL	Bancos de Dados MySQL	30	15	2016
7	Word	Curso Completo de Word	40	30	2016
9	Cozinha Árabe	Aprenda a Fazer Kibe	800	30	2050
10	YouTuber	Gerar Polêmica e Ganhar Inscritos	800	2	2050
"""

DELETE FROM cursos
WHERE ano = '2050'
LIMIT 2;
# 3	23	00:12:41	DELETE FROM cursos WHERE ano = '2050' LIMIT 2	2 row(s) affected	0.031 sec
"""
1	HTML5	Curso de HTML5	40	37	2014
2	Algoritmos	Lógica da Programação	20	15	2014
3	Photoshop	Dicas de Photoshop CC	10	8	2014
4	PHP	Curso de PHP para Iniciantes	40	20	2015
5	Java	Introdução à Linguagem Java	40	29	2015
6	MySQL	Bancos de Dados MySQL	30	15	2016
7	Word	Curso Completo de Word	40	30	2016
"""


# CUIDADO PEQUENO GAFANHOTO PRA NÃO APAGAR TODOS OS REGISTROS DE UMA TABELA! Vamos sempre fazer o backup! 
TRUNCATE TABLE cursos;

# Atualizando nossos COMANDOS:

# DDL (Data Definition Language)
#     CREATE DATABASE
#     CREATE TABLE
#     ALTER TABLE
#     DROP TABLE (apaga a tabela inteira, tanto dados quanto a estrutura da tabela)


# DML (Data Manipulation Language) - 
#     INSERT INTO
#     UPDATE
#     DELETE
#     TRUNCATE (apaga os dados, mas mantém a estrutura da tabela, por isso não é DDL)


# Agora vamos aprender a EXPORTAR os dados pra fazer um BACKUP! 





"""
Transcrição


0:10
🎵Música da abertura🎵
0:19
Olá, pequeno gafanhoto!
0:20
Seja bem-vindo a mais uma aula do seu Curso em Vídeo de MySQL.
0:24
O meu nome é Gustavo Guanabara, eu sou seu professor!
0:26
E nessa sétima aula de banco de dados
0:29
nós vamos trabalhar um conceito dando continuidade aquilo que a gente viu na aula passada.
0:33
E dessa vez nós vamos aprender a manipular registros.
0:36
E em outros livros ou tutoriais você pode encontrar esse assunto com outros nomes.
0:40
Pode ser também manipulando linhas ou manipulando tuplas.
0:44
Todos esses são sinônimos.
0:46
Você pode ver...
0:47
Assim, registro é o mais comum de aparecer,
0:49
mas se por acaso for citado, linha, o conceito de linha é a mesma coisa que o registro.
0:54
É uma linha, da tabela.
0:55
A gente já, já vai ver e você vai entender, o por quê, que a gente chama de linha
0:58
e o por quê que os campos a gente chama de colunas
1:00
Mas um nome que é bem curioso é o nome "tupla".
1:02
Que também se refere a uma linha de um Banco de Dados.
1:05
ou então um registro do banco de dados, enfim...
1:07
então, se por acaso, em algum lugar aparecer o termo Linha, Registro ou Tupla.
1:11
Você sabe que está se falando da mesma coisa.
1:13
Em um dos vídeos anteriores a gente viu como incluir linhas.
1:16
Você viu o comando "INSERT INTO".
1:18
Que algumas pessoas chamam de "INSERTI INTU"
1:20
Então, você, pequeno gafanhoto, já sabe incluir linha.
1:22
O quê?!
1:23
Você não sabe incluir linhas?!
1:25
Então, o que você está esperando, meu querido?! Aqui, olha, que tem uma playlist.
1:28
Se você caiu nessa aula de manipulação de registros, sei lá o por que.
1:32
Saiba que existe um curso completo.
1:34
E você precisa seguir esse curso.
1:35
Se você não sabe utilizar o comando INSERT INTO, direito ainda...
1:39
Você clica aqui no meio, olha. Você vai ter a playlist.
1:42
E aqui nessa playlist
1:43
você vai ter acesso a essa aula.
1:44
Essa e muitas outras aulas...
1:45
Como eu disse logo no inicio essa é a sétima aula de banco de dados.
1:49
Então, você já pressupõe que existem outras 6.
1:52
Eu acho.
1:53
Então, vamos parar de conversa e vamos trabalhar.
1:57
Já estou, aqui, com meu WAMP aberto.
2:00
Já estou, aqui, com o meu Workbench aberto.
2:02
E se você chegou agora, com certeza está perdido.
2:05
Então, volto a dar dica:
2:07
assiste a playlist, meu querido, você vai entender tudo bonitinho, você vai aprender MySQL da forma correta.
2:12
Então se você perceber, aqui, eu não estou com banco de dados nenhum aberto...
2:15
Eu estou com o banco "test", aqui, que é o que já vem no Mysql e estou com o "cadastro".
2:19
Não existe,
2:20
porque nenhum deles está em negrito.
2:21
Pra abrir, você tem duas maneiras:
2:23
ou você clica duas vezes,
2:24
como a gente está fazendo, se você clicar duas vezes ele abre.
2:27
Ou, então, você bota o comando "use cadastro;"
2:32
Pressiona Ctrl + Enter. Ele já abriu o banco de dados cadastro. Simples assim.
2:37
Aqui você vai dar uma olhada, a gente já tem as tabelas "cursos" e "gafanhotos".
2:41
A tabela "gafanhotos", eu tenho as colunas: id, nome, profissao, nascimento, sexo, peso, altura e nacionalidade.
2:50
E o seu banco de dados tem que estar dessa maneira, e na tabela cursos...
2:54
Eu tenho as colunas:
2:55
id do curso, nome, descrição, a carga horária do curso, o total de aulas que ele tem e o ano, em que ele foi lançado.
3:03
E se a gente vier aqui e der, "select * from gafanhotos".
3:09
Pressione Ctrl + ENTER.
3:11
E ele vai te mostrar aqui, Godofredo, Maria, Creuza, Adalgisa, Claudio, Pedro e Janaina.
3:17
O que é que você tem contra os nomes que eu coloquei aqui?
3:18
Mas dá uma olhada aqui na tela pra você entender direito o que é linha e o que é coluna.
3:22
Se você prestar atenção...
3:24
A nossa lista, né, o nosso "result set".
3:26
Risada
3:27
Gostou do nome, né?!
3:28
O nome disso é "Result set"!
3:30
Que é o resultado de uma instrução.
3:32
No meu caso, aqui, a instrução "select".
3:34
Se você prestar bem atenção, as minhas linhas, são os meus registros, aqui óh, acabei de selecionar o registro da Maria
3:38
acabei de selecionar o registro do Cláudio
3:40
Então, tudo o que estiver em linha é registro
3:43
tudo que estiver em coluna é campo
3:45
está vendo aqui ó, "nascimento", tudo isso aqui é minha coluna "nascimento"
3:49
tudo isso daqui é minha coluna "peso"
3:51
tudo isso aqui é minha coluna "nacionalidade" e assim sucessivamente.
3:54
Então guarda ai na sua cabeça pequeno gafanhoto.
3:56
As linhas são as tuplas ou registros
3:59
As colunas são os meus campos ou meus atributos
4:02
O que eu quero fazer aqui é manipular linhas
4:04
se você quiser manipular colunas eu já te ensinei o comando.
4:07
Vai pra aula de ALTER TABLE que você vai entender.
4:10
O comando ALTER TABLE permite que você altere as colunas.
4:13
Os comandos que você vai aprender aqui, vão permitir que você manipule linhas.
4:17
Viu como a gente está avançando aqui?
4:18
Vamos dar um SELECT aqui em "cursos"
4:21
Ctrl+ENTER
4:23
E já mudou óh! Percebe aqui que a gente não tem nenhuma linha
4:26
tem um asteriscozinho aqui na frente que indica que não tem registro nenhum
4:29
então, o que nós vamos fazer aqui, antes de mais nada é incluir novos registros, vamos incluir novos cursos.
4:35
E ai pequeno gafanhoto, pra facilitar e pra acelerar a aula
4:38
eu já digitei um comando se você prestar atenção aqui óh, dá uma olhadinha aqui na tela.
4:41
Já tem um comando digitado. Eu vou mostrar ele pra você.
4:43
O que eu criei aqui, foi um comando INSERT INTO gigante.
4:47
Óh! Insira na tabela "cursos", os valores e coloquei vários registros com valores.
4:52
Achou dificil?
4:53
É sinal que você não assistiu a aula de INSERT INTO direito
4:55
Dá uma olhada óh, aqui em cima. Eu vou te dar uma moral e vou colocar aqui a aula de INSERT INTO, então
5:01
como quem não quer nada, clique aqui se você sentir dificuldade, clique aqui e assiste
5:05
continue nessa aula, se você sentir alguma dificuldade
5:07
Clique aqui e assiste a aula de INSERT INTO antes.
5:10
Então esse comando aqui vai adicionar vários registros
5:12
se você prestar atenção
5:13
existe alguns erros de digitação aqui óh. "Jarva".
5:16
E se você assistiu o curso em vídeo responde.
5:18
Você sabe do que eu to falando.
5:19
Você não assiste curso em vídeo responde?
5:21
Vai dar uma olhada lá na Play List
5:23
Tem uma Play List exclusiva, só de curso em vídeo responde
5:25
Coloquei aqui também, vou te dar essa moral
5:27
Tem aqui óh, "PGP" no lugar de "PHP"
5:30
Então, tem alguns errinhos, que eu coloquei de propósito.
5:33
Isso porque, nós vamos manipular linhas.
5:35
O que eu te recomendo é o seguinte.
5:37
Pause o vídeo. Quer vê! Vou passar pra tela
5:39
Então óh, nesse momento, pause o vídeo
5:42
e digite no seu MySQL WORKBENCH esse comando
5:45
Isso é de suma importância, porque nós vamos precisar dessas linhas, pra poder manipular
5:49
E você sabe que só se aprende, como? Praticando.
5:53
Então, pare de preguiça. Vou voltar pra lá.
5:55
Você pausa o vídeo.
5:56
Pausa o vídeo!
5:57
Eu vou esperar em! - Vai, pausa o vídeo!
6:01
Pausa!
6:02
✷Esperando.✷ (Mudo)
6:06
Não vai pausar né!
6:08
✷Risos✷
6:08
Eu espero que você tenha pausado.
6:10
Eu espero que você tenha digitado.
6:11
É só assim que você vai aprender em!
6:12
Então, vou colocar aqui óh. Vou dar Ctrl+ENTER
6:17
Pressionando Ctrl+ENTER ele já adicionou.
6:20
E vamos dar um SELECT aqui agora de novo!?
6:23
SELECT * FROM cursos
6:28
Ctrl+ENTER
6:29
Agora óh, eu já tenho os dados incluídos
6:33
✷Beleza?!✷
6:34
Então, vou considerar que a gente já está nesse ponto.
6:36
Então, pra deixar bem claro.
6:38
O nosso Banco de Dados tem o cadastro de duas coisas.
6:41
"gafanhotos" e "cursos"
6:43
Nos "gafanhotos", nós temos a seguinte estrutura.
6:46
Nós temos esses atributos.
6:48
E se você perceber o "id" está sublinhado ali. Isso por que, ele é o que?
6:51
Chave Primária
6:52
E a estrutura de "cursos" é a seguinte
6:54
idcurso, nome, descrição, carga, total de aulas e ano.
6:57
Então, depois de fazer a inclusão.
6:59
Nossa tabela de cursos está com essa estrutura
7:01
Coloquei as colunas ali
7:03
E vou colocar as linhas
7:04
Nós temos várias linha que foram incluídas
7:06
Com aquele comando que agente acabou de usar
7:08
perceba ai que são 10 registros que foram incluídos
7:11
inclusive com os erros de digitação
7:13
Erra na digitação também pra você acompanhar o que a gente tá fazendo aqui
7:16
pra facilitar a sua vida eu vou marcar os erros que eu cometi aqui
7:19
Então eu botei lá, olha lá! O curso de "HTML4", não é "HTML4", é HTML5.
7:23
Botei ali óh, "PGP" que foi feito em "2010", não foi em "2010" né! Foi o curso de PHP que foi feito em 2015,
7:29
e o curso de "Jarva", que tá "Jarva"
7:32
que tá com a carga de "10" Horas, que não são "10" horas, são 40
7:34
e o ano tá "2000", também é 2015.
7:37
Se você perceber tem uns cursos de 2018 que são meio trollagem
7:40
calma que isso vai ser necessário também, digita, digita tudo aquilo do momento em que você pausou
7:45
Então a primeira coisa que a gente tem que fazer, é conseguir manipular essas linhas
7:50
Eu não consigo manipular várias linhas ao mesmo tempo
7:52
um comando, manipula uma linha
7:55
mas, eu consigo mexer dentro de uma linha, em várias colunas ao mesmo tempo.
7:59
Vamos aprender como fazer isso!
8:01
primeira coisa que nós vamos fazer é modificar a linha 1 ali óh, do "HTML4"
8:05
na verdade a única coisa que tem que se mudar, é de "HTML4" para "HTML5"
8:09
O comando para fazer isso é muito simples
8:11
então ali óh, coloquei do lado direito, todas as modificações que a gente tem que fazer
8:15
vamos começar pela linha 1
8:16
e se você percebeu, a coluna do "idcurso" está marcada
8:20
Vou te explicar porque.
8:21
Então olha só, coluna do "idcurso" eu coloquei de verde pra identificar
8:24
Vamos ao comando!
8:26
Pra gente poder modificar uma linha
8:27
a gente vai utilizar o comando UPDATE
8:29
então eu vou colocar UPDATE "cursos"
8:31
"cursos" sendo o nome da tabela
8:33
e vou colocar SET nome = 'HTML5' isso é
8:36
eu vou modificar na tabela "cursos" o nome para 'HTML5'
8:41
ta vendo que o nome ali é nome?
8:42
então estou mudando de HTML4 para HTML5
8:45
Mas beleza. Como eu vou identificar qual linha vai ser modificada?
8:49
Também é fácil, é só você se basear em um dos campos.
8:52
No meu caso aqui eu vou me basear no campo de chave primária, pq ai eu tenho certeza que só existe uma linha.
8:57
Lembra? Que chave primária identifica cada registro... Identifica cada linha.
9:02
Não existem duas linhas com a mesma chave primária.
9:05
Para fazer isso você, complementado o comando, você vai colocar:
9:08
WHERE idcurso = '1'
9:09
Então olha só!
9:10
Vamos à uma pequena aula de inglês rápida.
9:13
UPDATE é atualize,
9:15
SET é configure
9:17
e WHERE é onde.
9:18
Então vamos tentar lê em português.
9:19
Modifique os cursos, configurando o nome para 'HTML5
9:24
onde o "idcurso" é igual a '1'
9:26
Viu como é mais simples quando você simplesmente traduz do inglês pro português!
9:29
Então eu vou modificar a tabela "cursos"
9:31
vou modificar o conteúdo da coluna "nome" para 'HTML5'
9:35
Onde o "id" seja '1'
9:37
Vamos digitar e ver o que vai acontecer
9:39
Então já estou aqui com meu SELECT aberto, e vou digitar o comando óh, eu limpei o comando anterior
9:44
e vou digitar esse agora
9:45
na verdade você não precisa nem limpar né, eu só limpei pra aula ficar mais bonitinha
9:49
Então vamos lá!
9:49
UPDATE, o nome da tabela
9:52
nome da tabela "cursos"
9:54
UPDATE "cursos"
9:56
configurando o nome pra 'HTML5'
10:01
lembrando que isso aqui não é crase nem acento agudo, isso é aspas simples
10:05
onde (WHERE "idcurso" = '1')
10:10
Simples assim!
10:11
Então eu vou modificar, onde o "idcurso" for = '1'
10:14
só existe uma linha que o "idcurso" igual '1'
10:16
pode procurar, não existe outra e nunca vai existir
10:19
porque "idcurso" é chave primária, não se esqueça disso.
10:22
Então ele vai modificar essa linha aqui
10:24
Vou pressionar Ctrl+Enter
10:26
ele sumiu o SELECT óh!
10:27
vou botar aqui em baixo
10:28
SELECT * FROM cursos;
10:33
Ctrl+Enter
10:35
Ala óh, o que era 'HTML4' agora tá 'HTML5'
10:39
Viu como é fácil?
10:40
Acabamos de manipular uma linha
10:43
mas, não para por ai não, vamos dar continuidade
10:45
se você perceber, a linha 4 que está o curso de 'PHP'
10:49
primeiro o nome está 'PGP'
10:51
e o ano está como '2010'
10:53
eu tenho que alterar os dois ao mesmo tempo
10:55
Como é que eu faço isso?
10:56
É fácil também, vamos começar o comando como começamos o anterior
11:00
Ala! UPDATE "cursos"
11:01
só que agora meu o SET vai ser diferente olha só! Considerando a linha 4 ali
11:06
SET nome = 'PHP' , ano = '2015';
11:09
Viu como é fácil?
11:10
Eu simplesmente coloco na mesma linha todas as alterações separadas por virgula
11:15
mas, em qual eu vou alterar?
11:17
Agora eu vou indicar no WHERE qual a linha que eu vou modificar
11:19
WHERE "idcurso" = '4' ;
11:21
Vamos digitar esse comando. Vamos lá óh!
11:23
UPDATE "cursos", modificando "nome" pra 'PHP'
11:28
e o "ano" pra '2015'
11:32
onde o "idcurso" seja '4'
11:35
Então ele vai modificar óh!
11:36
Essa linha aqui óh! Ele vai modificar.
11:38
O "nome" pra 'PHP' e o "ano" pra '2015'
11:42
Clica na linha. Pode ser em qualquer lugar
11:45
Contanto que seja dentro do comando
11:47
Ctrl + Enter
11:48
Ele modificou.
11:49
Pra verificar se realmente modificou
11:51
Vamos selecionar aqui o SELECT
11:53
Ctrl + Enter
11:54
Perceba aqui óh!
11:56
Modifiquei pra 'PHP'
11:57
Modifiquei pra '2015'
11:59
Agora ficou fácil né!
12:00
Vamos dar continuidade, que tem mais uma linha errada.
12:02
Se você perceber ali óh!
12:03
A quinta linha também está errada
12:05
porque o "nome" do curso está 'Jarva'
12:07
a "carga" não está '40'
12:08
e o "ano não está '2015'
12:10
E você pode está pensando. Pra que tu vai gastar tempo falando isso
12:13
é o mesmo comando, é parecido
12:15
mas, eu vou adicionar mais um parâmetro
12:17
pra poder limitar a ação do comando.
12:19
Então vamos começar!
12:20
UPDATE "curso" SET "nome" 'java' e a "carga" '40'
12:25
e o "ano" '2015' WHERE "idcurso" = '5'
12:29
tudo igual, tudo perfeito, sem problema nenhum
12:31
simplesmente eu estou modificando três colunas então separo por virgula
12:34
você é um gafanhoto esperto e já entendeu isso
12:36
o fato é o seguinte,
12:38
com o UPDATE, se você mexe na chave primária, você só mexe numa linha
12:42
mas, existe a possibilidade, existe o "RISCO"
12:46
de você mexer em várias linha ao mesmo tempo
12:48
Se esse for o seu caso. Por exemplo.
12:51
Eu quero modificar todos os
12:53
Eu quero modificar todos os anos para '2020'
12:55
ou todos os cursos que tem '40' horas, eu quero modificar o nome pra ✷sei lá✷ "PAITON"
13:00
Eu consigo fazer isso, e isso é perigoso!
13:02
o que você vai conseguir fazer é
13:04
se você realmente quer limitar a uma linha
13:07
você pode utilizar um parâmetro especial, e fácil de entender
13:11
no final do comando eu vou colocar um LIMIT '1' e vou botar ponto e virgula
13:15
esse LIMIT é pra limitar quantas linhas vão poder ser afetadas
13:19
então presta atenção aqui! eu quero modificar:
13:21
eu quero modificar o nome do curso para JAVA,
13:23
eu quero modificar a carga para 40
13:25
e quero modificar o ano para 2015.
13:27
Más eu não quero que essa alteração afete mais de uma linha caso eu tenha errado o comando.
13:31
claro que se eu utilizar a chave primária só vou afetar uma linha.
13:34
Então o LIMIT, ele vai permitir que eu limite
13:36
a ação do meu comando
13:37
Vamos ver como é que funciona
13:38
Então vou colocar lá ó, UPDATE cursos
13:41
Modificando o nome pra 'Java',
13:43
o ano pra '2015'
13:46
e a carga...
13:47
pra '40'
13:48
Eu não preciso nem colocar na mesma ordem
13:50
Onde o id
13:52
Ó eu quero modificar esse daqui, onde o id seja '5'
13:55
Só que eu vou colocar aqui ó, um...
13:58
limit 1
14:00
pra ele limitar...a um registro apenas
14:04
CTRL + ENTER
14:05
Vamos dar select
14:07
E você percebe aqui que ele já modificou pra 'Java', '40' horas, e '2015'
14:12
Até então, você tá pensando:"O resultado foi o mesmo"
14:14
Olha só como o update pode ser perigoso
14:17
Eu vou mexer diretamente nessas linhas aqui ó
14:19
Vou mexer nessas três linhas, você percebe aqui que uma característica padrão delas
14:23
É que o curso é de 2018
14:25
Que na verdade nem aconteceu ainda
14:26
Eu vou preparar aqui um update cursos
14:29
Modificando o ano
14:31
pra 2050
14:34
E a carga pra 800
14:36
Vamo exagerar, vamo exagerar
14:37
Só que ao invés de mexer no idcurso
14:39
Eu vou mexer...
14:40
onde o ano
14:42
seja igual
14:43
a 2018
14:44
O que que eu to fazendo aqui?
14:45
Esse enquanto
14:47
ele não vai pegar somente uma linha
14:49
Ele vai pegar
14:49
Todas essas três linhas oh, ele vai colocar
14:52
Essas Três linhas
14:53
Pra isso, claro que eu vou tirar o 'limit'
14:55
oh, então
14:56
Se eu der esse update aqui
14:58
Ele vai modificar todos esses registros
15:01
Ok? Vamos provar!
15:02
Opa! ele deu erro aqui oh
15:04
Isso vai acontecer com você também
15:06
Calma que isso não foi erro de digitação não
15:08
Isso é uma Proteção do WorkBench
15:09
Pra Você!
15:10
Vamos Desligar essa Proteção(Por Inquanto).
15:12
Eu recomendo que você mantenha ela ligada!
15:14
Por padrão
15:15
O Workbench só deixa você fazer atualizações
15:17
Em uma linha
15:18
Mechendo aqui na chave primária
15:20
Pra modificar isso
15:21
Você clica em Edit
15:23
Prefences(Preferência).
15:24
E na tela que vai abrir
15:25
Clica em 'Sql Editor'
15:27
Aqui em baixo, Você tem um Check
15:29
Que é o 'Safe Updates'
15:31
Que são Atualizações Seguras.
15:33
Vou desmarcar, porque a gente não quer atualizações seguras
15:36
viu como é perigoso? Até a ferramenta aqui já me bloqueia isso.
15:40
click em "OK"
15:41
clique aqui nesse botão pra reconectar
15:43
pressiona Ctrl + Enter
15:44
Não se esqueça em clicar em conectar e agora vamos dar o select para ver o que aconteceu
15:47
Clicando aqui Ctrl + Enter
15:50
Vamos fechar a janela de baixo aqui oh, é só clicar na parte de cima
15:53
E agora você vai perceber, que olha só... Todos os cursos que eram 2018
16:00
Ficaram com o ano para 2050 e a carga horaria de 800
16:04
Eu não sei se você conseguiu entender o quão perigoso é isso. Por exemplo:
16:08
Imagina que seu Banco de Dados tenha o cadastro do seus 5 mil clientes
16:11
Por exemplo: Eu tenho um Banco de Dados do Curso em Vídeo dos 120 mil alunos incritos
16:16
E eu dou um update errado e ele muda bairro de todo mundo para Madureira por exemplo
16:20
imagina o risco que isso acontece, então por isso que o Workbench tem o Save Update
16:25
Que a gente desligou temporariamente e eu recomendo que depois que você fizer essas aulas você ligue de novo
16:31
Sim enquanto você está com aula mantem ele desligado que você pode brincar com negócio
16:34
Mas é muito importante que você mantenha por exemplo um backup do seu Banco de Dados
16:37
E por isso que a próxima aula vai te ensinar isso
16:40
Como é que você vai criar uma cópia do seu Banco de Dados aqui
16:43
Então pequeno Gafanhoto muito cuidado quando for utilizar o update
16:46
Ele pode acabar com seu Banco de Dados e ai você precisa ter um Backup pra isso
16:50
Então vamos fazer o seguinte, vamos fazer um update agora com a limitação para você poder entender
16:54
Então percebe o seguinte aqui, vou atualizar os cursos onde o ano for 2050. ''Né''?
16:59
Que agora eu tenho 2050 tenho vários cursos
17:02
Eu vou modificar pra 2018 de novo e vou colocar zero horas de carga
17:08
Se eu fizer isso ele vai alterar, quantos registros tem em 2050? Beleza eu venho aqui e aqui
17:16
Então eu tenho essas três linhas aqui 2050, então se eu der esse comando aqui
17:20
Ele vai mudar tudo isso para 2018 e tudo isso para aqui pra zero
17:24
Só que agora vamos vê o limit funcionando, eu colocar aqui em baixo oh: '' limit 1''
17:31
O que vai acontecer é o seguinte, mesmo eu tendo essas três linha com 2050
17:36
Ele vai se limitar á alterar somente a primeira delas
17:39
vamos vê como é que funciona
17:41
Vou dar Ctrl e Enter aqui, logo em seguida o select
17:45
Perceba que eu ainda tenho duas linha, com 2050
17:51
É a alteração que eu mandei fazer para 2018 e 0, só aconteceu na primeira linha.
17:57
É assim que funciona limit, então o limit e uma segurança.
18:01
A dica que eu te dou é,
18:03
tenta evitar utilizar o update.
18:06
Principalmente no seu banco de dados que estar ativo no momento.
18:09
É se você vai utilizar,
18:11
liga o server update lá diretamente nas preferências do seu workbench
18:15
Combinado
18:16
Então, e assim que funciona a atualização de registros
18:19
Então depois de tudo isto que a gente fez , a nossa tabela como você acabou de ver, estar deste jeito.
18:24
Toda "alteratinha", tudo bonitinho,
18:26
quase tudo bonitinho né.
18:29
Isto porque têm 3 registros que eu não quero.
18:31
se você prestar atenção
18:33
, esse 3 registros lá de baixo
18:35
São completamente inúteis,
18:37
Eu não vou fazer curso em vídeo, de sapateado, nem de cozinha árabe e nem um curso para te ensinar a ser "YouTeber".
18:41
Então, eu não quero essas linhas,
18:43
Eu quero apagar essas linhas, aí você pode pensar,
18:45
Dá um update, colocando tudo vazio. Não é assim, pequeno a gafoito
[TRUNCATE]
"""




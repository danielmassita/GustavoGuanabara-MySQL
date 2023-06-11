# Curso MySQL #09 - PHPMyAdmin (Parte 1)
# https://youtu.be/OaPMvrA0cA4
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/phpmyadmin-parte-1/

# USANDO O PHP MY ADMIN! PHPMyAdmin + Console de Comando

SHOW DATABASES;
"""
mysql> show databases
    -> ;
+--------------------+
| Database           |
+--------------------+
| cadastro           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.07 sec)

mysql>
"""

STATUS;
"""
mysql> status
--------------
c:/wamp64/bin/mysql/mysql8.0.31/bin/mysql.exe  Ver 8.0.31 for Win64 on x86_64 (MySQL Community Server - GPL)

Connection id:          28
Current database:
Current user:           root@localhost
SSL:                    Cipher in use is TLS_AES_256_GCM_SHA384
Using delimiter:        ;
Server version:         8.0.31 MySQL Community Server - GPL
Protocol version:       10
Connection:             localhost via TCP/IP
Server characterset:    utf8mb4
Db     characterset:    utf8mb4
Client characterset:    cp850
Conn.  characterset:    cp850
TCP port:               3306
Binary data as:         Hexadecimal
Uptime:                 1 day 2 hours 43 min 17 sec

Threads: 6  Questions: 2053  Slow queries: 0  Opens: 397  Flush tables: 3  Open tables: 284  Queries per second avg: 0.021
--------------
"""

USE cadastro;
"""
mysql> use cadastro;
Database changed
"""

STATUS;
"""
mysql> status
--------------
c:/wamp64/bin/mysql/mysql8.0.31/bin/mysql.exe  Ver 8.0.31 for Win64 on x86_64 (MySQL Community Server - GPL)

Connection id:          28
Current database:       cadastro                               <<<<<<<<<<<<<<<<<<<<<<<<<<<<
Current user:           root@localhost
SSL:                    Cipher in use is TLS_AES_256_GCM_SHA384
Using delimiter:        ;
Server version:         8.0.31 MySQL Community Server - GPL
Protocol version:       10
Connection:             localhost via TCP/IP
Server characterset:    utf8mb4
Db     characterset:    utf8mb3
Client characterset:    cp850
Conn.  characterset:    cp850
TCP port:               3306
Binary data as:         Hexadecimal
Uptime:                 1 day 2 hours 44 min 20 sec

Threads: 6  Questions: 2079  Slow queries: 0  Opens: 397  Flush tables: 3  Open tables: 284  Queries per second avg: 0.021
--------------
"""

SHOW TABLES;
"""
mysql> show tables;
+--------------------+
| Tables_in_cadastro |
+--------------------+
| cursos             |
| gafanhotos         |
+--------------------+
2 rows in set (0.04 sec)

mysql>
"""

DESCRIBE cursos;
"""
mysql> describe cursos;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| idcurso   | int          | NO   | PRI | NULL    |       |
| nome      | varchar(30)  | NO   | UNI | NULL    |       |
| descricao | text         | YES  |     | NULL    |       |
| carga     | int unsigned | YES  |     | NULL    |       |
| totaulas  | int unsigned | YES  |     | NULL    |       |
| ano       | year         | YES  |     | 2016    |       |
+-----------+--------------+------+-----+---------+-------+
6 rows in set (0.03 sec)
"""

DESC gafanhotos;
"""
mysql> DESC gafanhotos;
+---------------+---------------+------+-----+---------+----------------+
| Field         | Type          | Null | Key | Default | Extra          |
+---------------+---------------+------+-----+---------+----------------+
| codigo        | int           | YES  |     | NULL    |                |
| id            | int           | NO   | PRI | NULL    | auto_increment |
| nome          | varchar(30)   | NO   |     | NULL    |                |
| prof          | varchar(20)   | YES  |     | NULL    |                |
| nascimento    | date          | YES  |     | NULL    |                |
| sexo          | enum('M','F') | YES  |     | NULL    |                |
| peso          | decimal(5,2)  | YES  |     | NULL    |                |
| altura        | decimal(3,2)  | YES  |     | NULL    |                |
| nacionalidade | varchar(20)   | YES  |     | Brasil  |                |
+---------------+---------------+------+-----+---------+----------------+
9 rows in set (0.00 sec)
"""

SELECT * FROM gafanhotos;
"""
mysql> select * from gafanhotos;
+--------+----+-----------+------+------------+------+-------+--------+---------------+
| codigo | id | nome      | prof | nascimento | sexo | peso  | altura | nacionalidade |
+--------+----+-----------+------+------------+------+-------+--------+---------------+
|   NULL |  1 | Godofredo |      | 1984-01-02 | M    | 78.50 |   1.83 | Brasil        |
|   NULL |  2 | Maria     |      | 1999-12-30 | F    | 55.20 |   1.65 | Portugal      |
|   NULL |  3 | Creuza    |      | 1920-12-30 | F    | 50.20 |   1.65 | Brasil        |
|   NULL |  4 | Adalgiza  |      | 1930-11-02 | F    | 63.20 |   1.75 | Irlanda       |
|   NULL |  5 | Cláudio   |      | 1975-04-22 | M    | 99.00 |   2.15 | Brasil        |
|   NULL |  6 | Pedro     |      | 1999-12-03 | M    | 87.00 |   2.00 | Brasil        |
|   NULL |  7 | Janaína   |      | 1987-11-12 | F    | 75.40 |   1.66 | EUA           |
+--------+----+-----------+------+------------+------+-------+--------+---------------+
7 rows in set (0.02 sec)
"""

SELECT * FROM cursos;
"""
mysql> select * from cursos;
+---------+------------+------------------------------+-------+----------+------+
| idcurso | nome       | descricao                    | carga | totaulas | ano  |
+---------+------------+------------------------------+-------+----------+------+
|       1 | HTML5      | Curso de HTML5               |    40 |       37 | 2014 |
|       2 | Algoritmos | Lógica da Programação        |    20 |       15 | 2014 |
|       3 | Photoshop  | Dicas de Photoshop CC        |    10 |        8 | 2014 |
|       4 | PHP        | Curso de PHP para Iniciantes |    40 |       20 | 2015 |
|       5 | Java       | Introdução à Linguagem Java  |    40 |       29 | 2015 |
|       6 | MySQL      | Bancos de Dados MySQL        |    30 |       15 | 2016 |
|       7 | Word       | Curso Completo de Word       |    40 |       30 | 2016 |
+---------+------------+------------------------------+-------+----------+------+
7 rows in set (0.02 sec)
"""

mysql> update cursos set nome = 'Ph' where idcurso = '4';
# Query OK, 0 rows affected (0.00 sec) Rows matched: 1  Changed: 0  Warnings: 0

# MyPHPAdmin:
  UPDATE `gafanhotos` SET `peso` = '83.20' WHERE `gafanhotos`.`id` = 4;

"""
mysql> select * from gafanhotos;
+--------+----+-----------+------+------------+------+-------+--------+---------------+
| codigo | id | nome      | prof | nascimento | sexo | peso  | altura | nacionalidade |
+--------+----+-----------+------+------------+------+-------+--------+---------------+
|   NULL |  1 | Godofredo |      | 1984-01-02 | M    | 78.50 |   1.83 | Brasil        |
|   NULL |  2 | Maria     |      | 1999-12-30 | F    | 55.20 |   1.65 | Portugal      |
|   NULL |  3 | Creuza    |      | 1920-12-30 | F    | 50.20 |   1.65 | Brasil        |
|   NULL |  4 | Adalgiza  |      | 1930-11-02 | F    | 83.20 |   1.75 | Irlanda       |        <<<<<< ATUALIZADO DIRETO DO PHP MY ADMIN
|   NULL |  5 | Cláudio   |      | 1975-04-22 | M    | 99.00 |   2.15 | Brasil        |
|   NULL |  6 | Pedro     |      | 1999-12-03 | M    | 87.00 |   2.00 | Brasil        |
|   NULL |  7 | Janaína   |      | 1987-11-12 | F    | 75.40 |   1.66 | EUA           |
+--------+----+-----------+------+------------+------+-------+--------+---------------+
7 rows in set (0.00 sec)"""





"""
Transcrição


Procurar no vídeo
0:00
♫Cantarolando♫
0:05
Tooooim
0:07
uhhh
0:10
♫Música de Introdução ♫
0:20
Olá, pequeno gafanhoto, seja bem vindo à mais uma aula curso em vídeo de banco de dados com MySQL
0:25
O meu nome é Gustavo Guanabara, eu sou seu professor
0:27
e vamos continuar a falar sobre banco de dados
0:30
e dessa vez vamos fazer aquilo que eu prometi antes pra você,
0:33
vamos aprender a utilizar outra ferramenta
0:36
que no meu caso é o PHPMyAdmin
0:38
Na verdade eu vou te ensinar nessa aula o iniciozinho de duas ferramentas
0:42
na verdade não é ferramenta
0:43
agente vai utilizar o PHPMyAdmin, que é uma ferramenta, que é um aplicativozinho, Criado em PHP
0:47
e não falei que aplicativozinho pra menosprezar ele. É um ótimo aplicativo Web.
0:51
e nós vamos também utilizar o console
0:54
Sabe quando o teu professor te ensinou lá na faculdade no colégio aquela tela preta feia para cacete e você achou horroroso aquilo
0:59
Agora que você já sabe os principais comandos
1:02
Fica fácil utilizar o console também.
1:04
Então meu querido!
1:05
Acomoda-se na cadeira,
1:07
fecha seu Facebook,
1:08
bota o celular no modo silencioso, e fecha esse Whatsaap meu filho!
1:12
Sabe esses grupos que ficam mandando as coisa. To de olho em você rapá!
1:15
E vamos começar a trabalhar.
1:19
Então já estou aqui no Workbench
1:20
O nosso conhecido banco de dados que agente exportou na aula passada né?
1:24
Eu te ensinei como é que exporta e importa
1:26
E as minhas tabelas. Curso e gafanhotos.
1:28
Até aí tudo bem.
1:29
E é muito engraçado porque os alunos confudem
1:32
Eles acham que o banco de dados
1:34
tá guardado no workbench
1:36
E nao é!
1:37
Você pode utilizar esse banco de dados porque ele está em um servidor.
1:39
Para o ambiente que criei nessa aula, é claro, que o seu servidor está na sua máquina
1:43
Mas você pode acessar remotamente qualquer servidor MySQL
1:46
contanto que você tenha: o endereço dele, o usuário e a senha.
1:49
Vamos fazer o seguinte.
1:50
Vou minimizar aqui.
1:51
E vou te provar o que estou falando.
1:53
Vai lá no Wampserver
1:54
Lá no iconizinho com W
1:56
clica nele
1:57
Escolhe MySQL
1:58
E escolhe console MySQL
2:00
vai abrir a tão temível tela preta
2:03
calma, respira, bebe água
2:05
segura aqui na minha mão, pega, segura na minha mão
2:07
calma, não tem nada de mais
2:08
a primeira coisa que ele pede é a senha
2:10
e você se lembra que seu usuário é root
2:12
e a sua senha é vazia
2:14
pra esse caso aqui
2:15
se você está utilizando
2:16
outro modelo de servidor
2:18
você tem que saber, qual é o endereço?
2:19
qual é o usuário?
2:20
qual é a senha?
2:21
no meu caso aqui
2:22
se você está seguindo
2:23
o que eu estou falando nas aulas utilizando o WampServer
2:25
é sem senha
2:26
então, vamos precionar enter
2:27
senha vazia
2:28
e eu já estou dentro do ambiente
2:30
a primeira coisa que agente vai fazer
2:32
é ver quais são os bancos de dados que existem neste ambiente
2:34
então, eu vou dar o comando show databases;
2:37
show databases;
2:39
ponto e vírgula
2:40
da enter
2:41
e ele vai te mostrar
2:42
algumas opções
2:44
por padrão
2:44
todo servidor MySql vem com os seguintes bancos de dados:
2:47
information_schema
2:48
MySql
2:50
e performance_schema
2:51
e em alguns casos ainda vem um banco de dados chamado test
2:53
que agente utilizou até na aula passada, agente apagou em uma das aulas anteriores
2:56
e também nesta lista se você olhar
2:58
tem o nosso conhecido banco de dados cadastro
3:01
pra verificar qual banco de dados está aberto no momento
3:03
você vai digitar o comando status;
3:07
digitando status e dando enter
3:09
aqui eu tenho uma linha que é o current_databases
3:11
que é o banco de dados atual
3:13
tá vendo aqui ó...tá vazio
3:14
eu não tenho banco de dados nenhum aberto
3:16
pra abrir o banco de dados
3:17
eu já te ensinei o comando, qual é? qual é? qual é?
3:20
isso aí rapá! use
3:22
então eu vou botar aqui:
3:23
use cadastro;
3:26
ponto e vírgula, dou enter
3:28
tá aqui ó database changed
3:30
agora vamos dar o status de novo
3:33
ala ó, agora o meu current databases é cadastro
3:37
até aí bem parecido com o Workbench né?
3:40
Só não tem aquela interface gráfica
3:41
vamos ver quais são as tabelas do nosso banco de dados aberta no momento
3:44
pra ver as tabelas...
3:45
show tables
3:46
ponto e vírgula
3:48
tá lá ó, eu tenho as tabelas cursos e gafanhotos
3:52
exatamente como a gente viu lá no Workbench
3:54
e como é que eu mostro, por exemplo, a estrutura da tabela gafanhotos?
3:57
o comando, é o describe
3:58
exatamente o mesmo que agente utilizou no Workbench
4:01
então vamos colocar aqui ó
4:02
describe
4:04
cursos, por exemplo
4:07
ele me mostrou a estrutura de cursos ó
4:09
idcurso que é int, nome que é varchar, descrição que é text, carga e totaulas que é int e o ano que é year
4:16
lembra quando agente fazia isso no Workbench
4:18
olha só
4:19
🔨🔨🔨 esse corno martelando na minha cabeça 🔨🔨🔨
4:23
vou voltar aqui no Workbench, mesmo com as marteladas
4:25
e vou colocar aqui ó: describe cursos;
4:31
vou dar ctrl+enter para executar
4:33
tá lá ó
4:34
o que tá aqui
4:36
compara aí, compara aí gafanhoto
4:38
olha só
4:40
o que está aqui, desse lado, está aqui, desse lado
4:44
e qual é o seu trauma com a tela de terminal?
4:46
só porque está preto e branco!
4:47
para de graça meu querido
4:49
é claro que agente vai voltar a utilizar o Workbench, agente vai continuar utilizando ele porque ele facilita nossa vida
4:54
mas, se alguém mandar você entrar no terminal, entrar no console do MySql pra acessar o servidor
4:58
não tem trauma cara! você pode entrar sem problema
5:01
sem medo de ser feliz
5:03
entra lá, estufa o peito, fala assim...vou entrar nesse maldito desse console
5:06
me aqui que eu vou te mostrar os comandos
5:08
o Guanabara me ensinou essa parada toda, eu sou inteligente!
5:11
vai lá e assiste a aula dele, que ele é bem legal
5:14
compartilhe!
5:15
então voltando aqui no terminal
5:17
lembrando que você pode utilizar ao invés de describe, desc, desc.....
5:22
por exemplo gafanhotos
5:26
tá lá
5:27
id, nome, profissão, exatamente a estrutura que você tem mostrado lá
5:30
eu quero ver quais são os gafanhotos cadastrados?
5:32
select * from gafanhotos!
5:36
ponto e vírgula!
5:38
e tá lá! Godofredo, Maria, Creuza, Adalgiza, Cláudio, Pedro e Janaína
5:42
eu quero ver quais são os cursos?
5:44
select * from cursos
5:49
tá lá!
5:50
curso de HTML, de Algorítmo, de Photoshop, de PHP, de Java, de MySql e de Word
5:53
tudo aquilo que foi cadastrado lá
5:55
e eu posso por exemplo, utilizar os comandos que agente viu nas aulas anteriores
5:59
por exemplo! eu quero renomear o curso de PHP pra.....sei lá! P!
6:04
pra fazer isso! eu faço, update
6:08
cursos
6:11
set
6:13
nome igual a 'Ph'
6:17
where, idcurso
6:20
igual =
6:21
PHP é o idcurso 4
6:23
ponto e vírgula
6:25
deu enter, olha lá, query ok
6:27
vamos dar o select
6:28
você percebe aqui ó
6:30
que eu redigitei o comando de forma rápida
6:32
eu estou utilizando seta pra cima ⬆ e seta pra baixo ⬇ no teclado que ele vai voltando no histórico de comandos
6:37
mais uma dica legal
6:38
vou dar select * from cursos
6:40
e você vai ver ó, o curso de PHP agora se chama PH
6:42
vamos voltar aqui no Workbench
6:45
vamos dar um select * from cursos;
6:52
ctrl + enter
6:55
e você vai ver que o curso de PHP
6:57
agora se chama PH
6:58
viu! o seu dado, ele não está num aplicativo expecífico
7:02
o seu dado não está no Workbench
7:04
o seu dado está no seu servidor MySql
7:06
então independente da ferramenta que você utilizar
7:09
você pode utilizar qualquer comando que agente viu até agora
7:12
lembra que agente viu select, insert into, update, delete, create table, create database
7:19
qualquer desses comandos que você viu em todas as aulas anteriores
7:23
o quê!!!
7:23
você não viu a aula anterior?
7:25
aqui meu querido, play list direto
7:27
acessa a playlist e assista as aulas, cara
7:30
esse curso, ele não é composto só dessa aula
7:32
você chegou no meio do curso
7:34
então clicando aqui, você vai direto pra playlist
7:36
e vê todas as aulas que foram lançadas até o momento
7:39
inclusive se você está vendo algum tempo depois do lançamento oficial
7:43
você tem aulas depois dessa também
7:45
por exemplo: essa aula que eu vou apresentar novas ferramentas, eu vou dividir em duas partes
7:48
porque é muita coisa
7:49
nessa eu estou te mostrando o console MySql
7:51
e vou te mostrar o phpMyAdmin o iniciozinho dele
7:53
na outra eu vou dar continuidade ao estudo do PHP
7:56
então meu querido, acredita no tio
7:59
você vai conseguir utilizar o console sem problema nenhum
8:02
a única coisa que você não precisa no Workbench
8:04
é você utilizar os comandos show data bases;
8:07
show tables;
8:08
você já tem a visualização lateral
8:10
então você não precisa dar show tables; show databases;
8:13
mas, são comandos simples, que você consegue aprender rapidinho
8:17
não é meu objetivo aqui ficar te mostrando muito console
8:20
mas, o meu objetivo principal em te mostrar que o console não tem problema nenhum
8:23
é tirar esse trauma que muita gente tem
8:26
tem gente que pensa que console apareceu tela preta e letra branca você não vai conseguir fazer nada na sua vida
8:30
e eu tô trabalhando esse curso de MySql com comandos
8:33
então eu justifiquei no início que eu não ia utilizar ferramenta de clique e arrastro
8:37
que tem várias ferramentas de clique e arrastro
8:39
porque senão você não aprenderia os comandos
8:41
e aí se você não aprender os comandos
8:43
você não consegue programar por exemplo em: PHP em Java
8:47
porque lá na frente você vai precisar aprender Sql
8:49
e aí se você fez arrastando
8:51
você não lembra do comando
8:53
É! cuidado com isso, porque tem gente que vai falar assim, há!! Então ele está dizendo duas coisas diferentes
8:57
porque Java ele ensinou com clicar e arrastar
8:59
porque o comando em Java
9:01
você não tem necessidade de ficar decorando muito de comando
9:04
porque se você clicar e arrastar
9:06
beleza, ele gerou o comando pra você e você nunca vai precisar se preocupar com ele na vida
9:09
no banco de dados não
9:11
se você gerou um comando
9:12
e você vai precisar programar em PHP ou Java, por exemplo
9:15
você vai precisar lembrar do comando em Sql tudo bonitinho
9:17
pra você colocar dentro do comando em PHP
9:19
não sei se eu fiz bem claro
9:21
mas, confia em mim gafanhoto
9:22
eu escolhi a melhor técnica pra você
9:25
pode confiar no tio Guanabara aqui que ele sabe o que faz
9:27
ou pelo menos acha que sabe!
9:29
será???? 😏😏😏
9:30
então ó! Eu vou deixar aberto aqui o Workbench
9:33
vou deixar aberto aqui o meu servidor, o meu console
9:36
e eu vou abrir uma terceira ferramenta
9:38
só pra não zonear, que eu tenho toque
9:40
eu vou minimizar aqui tá?
9:42
tá limpinho, ufa 💨, que alívio 😥
9:43
agora eu vou fazer o seguinte ó
9:45
clica no ícone do Wampserver aqui em baixo
9:48
e no lugar do MySql você vai clicar em phpMyAdmin, respira fundo e confia
9:52
ele vai abrir o navegador
9:54
e vai abrir esse ambiente aqui
9:55
é muita coisa escrita
9:57
mas é fácil de usar
9:58
o phpMyAdmin como eu já expliquei anteriormente
10:00
é uma aplicação web com o objetivo de facilitar
10:03
e automatizar a criação de banco de dados MySql
10:06
ele realmente é muito simples
10:07
e também é muito popuplar
10:08
muitas Empresas de hospedagem
10:10
utilizam o phpMyAdmin
10:12
diretamente nos seus servidores de banco de dados, quando quer criar um site
10:15
advinha qual Empresa que utiliza? Eu não vou falar, eu não sei
10:19
eu vou dar um exemplo aqui
10:21
assim......largado
10:23
a melhor é essa aqui 😄, acessa lá👆, bota seu site lá🏡, que é legal👏
10:29
então o phpMyAdmin ele está me mostrando aqui também, olhem só
10:32
aqui na esquerda, olha que surpresa ele tem o banco de dados cadastro
10:35
olha só, está aqui
10:37
e eu tenho cursos e gafanhotos
10:39
clicando em cursos ele está me mostrando aqui ó
10:41
todos os cursos que estão cadastrados
10:43
quer ver a estrutura dele?
10:45
está aqui ó...a estrutura
10:46
está a estrutura dele aqui
10:49
vamos em gafanhotos, também tem ó, todos os gafanhotos cadastrados
10:52
por exemplo aqui ó
10:54
Adalgiza
10:56
eu coloquei aqui que ela tem 63 quilos e 20
10:58
ele não vai ter mais 63 quilos e 20 (63,20)
11:00
porque eu vou selecionar aqui
11:02
e eu vou editar
11:03
os dados da Adalgiza
11:05
ele vai colocar aqui ó, em vez de 63,20
11:08
ela tem 83,20
11:10
safadinha mentiu o peso
11:12
vou clicar em executar
11:14
ele salvou
11:16
percebe aqui ó... olha o que o phpMyAdmin fez
11:18
ele colocou o comando update que você digitaria caso estivesse no terminal
11:23
então o phpMyAdmin é uma ótima fonte de aprendizado também
11:26
começa a usar ele porque ele constantemente vai te dar qual comando Sql
11:29
e na verdade não ignore esse comando
11:31
olha e analisa, hummm peraí, é aquele comando que o Guanabara me ensinou no curso de MySql
11:36
e tudo mais, que é super legal, o melhor curso de MySql da internet
11:38
e o Guanabara é lindo😠, e o Guanabara é lindo😠 "falando com lentidão kkkkk"
11:44
e eu quero muito dar muito dinheiro 💵 pra ele
11:48
não??!!
11:48
então ele deu update aqui ó
11:50
então agora a Adalgiza
11:50
cadê a Adalgiza? Aqui ó...
11:52
que tinha 63,20, agora está com 83,20
11:56
será que ele atualizou os dados no console?
11:58
vamos lá ver!
11:59
vou minimizar aqui o phpMyAdmin
12:01
vamos voltar ao console
12:03
e vamos dar um select * from gafanhotos;
12:09
lembrando... aqui ó...
12:11
vamos ver aqui em cima
12:13
a Adalgiza aqui em cima ó
12:15
estava com 63,20
12:17
mentiu o peso, que feio dona Adalgiza
12:20
vou dar enter aqui ó...
12:21
não é ctrl + enter aqui não ó. É só enter
12:23
pressionou enter
12:25
a Adalgiza agora está com 83,20
12:28
que é o peso que foi atualizado diretamente do phpMyAdmin
12:31
eu acho que nesse ponto, você já está convencido, de que, aquilo que você faz numa ferramenta
12:36
repercute em todas as outras
12:38
porque na verdade, não é a ferramenta que armazena os dados
12:41
a ferramenta apenas manipula os dados de um servidor
12:44
então, independente da ferramenta que você escolheu
12:46
ah! Eu vou utilizar o Workbench. Não eu prefiro utilizar
12:50
o terminal aqui com o console
12:53
não! Eu prefiro o phpMyAdmin
12:54
independente da ferramenta que você utilizar
12:57
você vai conseguir manter os dados
12:59
porque eles não estão dentro dessa ferramenta
13:01
eles estão dentro do servidor
13:03
e pra você extrair esses dados desse servidor. O quê que você vai fazer?
13:06
você vai gerar o dump
13:07
então agente já acabou de unir o que agente aprendeu nessa aula
13:10
com o que agente aprendeu na aula anterior
13:12
está vendo como a coisa é simples
13:13
as vezes as pessoas se traumatizam
13:16
sei lá! Porque!!!
13:17
eu muito assim: Você está dentro de uma sala de aula
13:19
você é adolescente. O que você mais quer é conversar com seu coleguinha do lado
13:23
e tem um professor falando lá, e tem um professor falando lá
13:25
e eu caguei pro que o professor falou lá, eu só quero conversar com o coleguinha
13:28
a menininha bonita, loirinha, novinha e tudo mais
13:31
está ali do lado e o que você vai fazer?
13:32
Caguei pra ele. Você só vai perceber que a coisa está feia
13:36
quando o professor falar assim:
13:37
hora da prova, vamos lá que vale ponto
13:39
e aí você entra em desespero, porque?
13:41
você estava de olho na menininha
13:42
e é normal, todo adolescente tem isso
13:44
e aí você acaba traumatizando
13:46
porque você não prestou atenção no que o professor estava falando
13:48
porque está muito mais interessante falar com a menina aqui do lado
13:51
e você tem que lembrar daqui a 5 minutos
13:53
um comando que você não prestou atenção
13:55
e isso gera traumas
13:56
então meu querido
13:57
a partir de agora você está correndo atras do conteúdo
14:00
o conteúdo está aqui disponível pra você
14:02
não tem uma menina bonita do seu lado
14:04
se tiver tu se deu bem
14:06
não sei o que você está fazendo aqui assistindo essa aula
14:09
😄😄😄😄😄😄😄😄😄😍😍😍😍😍😜😜😜😜😜😜😜
14:12
mas concentra, concentra aqui, concentra que você vai conseguir
14:16
então o trauma das pessoas é porque as vezes elas não veem necessidade
14:20
e agora você viu necessidade
14:22
e como eu estou trazendo
14:23
efeitos visuais, a coisa bem trabalhada
14:25
eu to conversando contigo olho a olho, tete a tete, professor e gafanhoto
14:30
você está aprendendo, então, acredite em mim
14:32
tanto faz a ferramenta que você vai escolher pra criar seu banco de dados
14:36
o que importa é
14:37
sempre essa ferramenta vai ser trabalhada em comandos
14:40
as vezes automáticos como é o phpMyAdmin
14:42
as vezes manuais como é o console e também o Workbench
14:46
mas o que importa é: Você precisa aprender esses comandos, acredita em mim
14:50
você só vai sentir necessidade desses comandos quando você for por exemplo
14:53
aprender como acessa um banco de dados em PHP
14:55
uma coisa que todo mundo me pede. A Guanabara me ensina a acessar um banco de dados em PHP
14:59
ensino, pra isso você precisa de MySql
15:01
porque se você não prestou atenção em MySql, você vai ter problema lá na frente
15:04
lembra que eu sempre falei
15:05
se você não prestar atenção na aula de algorítimo, você vai ter problema em PHP
15:08
muitos gafanhotos acreditaram em mim e fizeram certinho o curso de algorítimo
15:12
e estão aí, aprendendo PHP, aprendendo Java
15:14
e me dando orgulho pela internet a fora, então
15:16
acredita no tio aqui, aprende essa bagaça
15:19
aprende MySQL, se não você vai ter problema lá na frente em PHP ou Java
15:23
na hora que você quiser acessar um banco de dados
15:25
eu falei pra caramba nessa aula
15:27
e eu vou deixar agora pra dar uma continuidade no phpMyAdmin
15:30
na próxima aula porque essa já acabou
15:32
como final, sempre tem o protocolo né?
15:35
👇 clica aqui e se inscreve
15:37
aqui você assiste todas as aulas 👇
15:39
a inscrição ela é muito importante
15:41
porque eu consigo um volume de alunos
15:43
eu consigo, quando vou buscar patrocinador pro curso
15:45
e não acredite que toda essa estrutura aqui
15:48
não precisa de patrocínio, não precisa de valores
15:50
tenta fazer um tutorial com qualidade
15:52
e você vai ver o quanto vai dar de trabalho e o quanto de dinheiro você vai precisar
15:55
então o que eu te peço é só isso
15:57
se inscreve no canal
15:58
e sempre que você se inscrever, na hora que você se inscrever
16:01
se você já é inscrito
16:02
clica na engrenagenzinha do lado
16:04
essa engrenagem vai ter uma opção pra você receber um e-mail
16:06
diz que quer receber
16:08
confia na gente, agente só te dá conteúdo legal
16:10
então é isso pequeno gafanhoto
16:12
você tem uma semana pra brincar com seu console
16:14
brincar com seu phpMyAdmin
16:16
na próxima aula agente vai criar um banco de dados de teste
16:19
no phpMyAdmin e vai ficar brincando aí em phpMyAdmin
16:23
console e Workbench pra ver como é que tudo funciona
16:25
e você vai aprender dentro de um curso de MySql
16:27
já uma ferramenta nova
16:29
então eu fico por aqui
16:30
até a próxima aula
16:31
um forte abraço
16:33
e até a próxima
16:34
olá pequeno gafanhoto! Seja bem vindo a mais uma aula do seu curso de banco de dados
16:39
>:(>:(>:(>:(>:(>:(>:(>:(>:(>:(>:(
16:40
comecei bem
16:41
ele realmente é muito simples
16:43
💨 💨 💨
16:45
ele realmente é muito simpleeeessss
16:47
caralh...........
16:48
ele realmente é muito $$%#$@#$$%#$%%@#$%¨&¨meu Deus o que eu ia falar?
"""

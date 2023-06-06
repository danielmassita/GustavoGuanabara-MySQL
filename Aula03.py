# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/criando-o-primeiro-banco-de-dados/
# https://youtu.be/m9YPlX0fcJk

"""
Aula 03 - Curso MySQL #03 - Criando o primeiro Banco de Dados

Vamos utilizar uma contação de história. Conheceremos o nosso amigo, Godofredo, para entendermos a ESTRUTURA DO BANCO DE DADOS! 

  Godofredo
  32 anos
  Masc
  78.5 kg
  1.83 m
  Brasil
  
  Dolores
  30 anos
  Fem
  52.3 kg
  1.65 m
  México
  
  Godolores
  3 anos
  Fem
  25.8 kg
  0.89 m
  EUA
  
Características que todos possuem... Pessoas diferentes, com CARACTERÍSTICAS semelhantes e comuns entre eles (nome, idade, sexo, peso, altura, nacionalidade). 
Cada pessoa é uma INSTÂNCIA. São unidades diferentes.
O Banco de Dados tem como OBJETIVO registrar coisas separadas (instâncias) que possuem características semelhantes e afins.
Usando esse padrão, podemos ADICIONAR qualquer tipo de pessoa, com essas CARATERÍSTICAS comuns. Mas os VALORES são diferentes. 
Desse modo, podemos colocar essas personagens em um CONTAINER que será chamado de 'PESSOAS'. 
E todas as INSTÂNCIAS dentro do container terão essas MESMAS CARACTERÍSTICAS (nome, idade, sexo, peso, altura, nacionalidade), algumas opcionais embora, mas sempre existe a possibilidade de CADASTRO.
Podemos criar container's diferentes, como por exemplo em distinção do container de 'pessoas', podemos ter um de 'JOGOS' com todas as características diferentes (de jogos, estilos, etc.).

A idéia é, em um Banco de Dados, ter a capacidade de:
- AGRUPAR coisas com CARACTERÍSTICAS semelhantes, e
- SEPARAR coisas com CARACTERÍSTICAS diferentes, mas que pela diferença, eu vou agrupar elas nas semelhanças entre elas;

Vamos colocar o container dentro de um 'navio'. Esse navio vai ser o nosso Banco de Dados.
- Banco de Dados são COLEÇÕES DE DADOS com características separadas, mas organizados em LOCAIS específicos.
- Os LOCAIS específicos são as TABELAS ('pessoas', 'jogos'), com coisas com CARACTERÍSTICAS semelhantes.
- E os dados dentro das tabelas são os REGISTROS. 

RESUMINDO: Banco de Dados > Conjunto de Tabelas         > Tableas são Conjunto de Registros
RESUMINDO: Local          > Características Semelhantes > Instâncias Distintas  > Registros difeferentes. 

"""
# Vamos começar CRIANDO UM BD (no nosso ambiente do MySQL).
# WAMP Server > MySQL Workbench > 

SHOW databases;

CRAETE DATABASE cadastro; # Run! 1 row affected; - criado no SCHEMAS o BD chamado 'cadastro', dentro tem e.g.: TABELAS, VIEWS, FUNCTIONS, etc.

# Tabela: PESSOAS (contém registros)
# Campos (características): nome, idade, sexo, peso, altura, nacionalidade 

CREATE TABLE pessoas (
  nome,
  idade,
  sexo,
  peso,
  altura,
  nacionalidade,
); # NOT RUN! 

# TIPOS PRIMITIVOS (do MySql): 

#   Numéricos
#     - inteiro (TinyInt, SmallInt, Int, MediumInt, BigInt)
#     - reais (Decimal, Float, Double, Real)
#     - lógicos (Bit, Boolean)

#   Data e Tempo (Date, DateTime, TimeStamp, Time, Year)

#   Literal
#     - caracteres (Char, VarChar - fixo, e depende)
#     - texto (TinyText, Text, MediumText, LongText)
#     - binário (TinyBlob, Blob, MediumBlob, LongBlob)
#     - coleções (Enum, Set)

#   Espacial (Geometry, Point, Polygon, MultiPolygon)

# Colocar os Tipos Primitivos em cada novo campo (vai nos ajudar a dimensionar). 
# PRECISÂO - Como os dados serão armazenados em disco, precisamos saber DIMENSIONAR a ESTRUTURA da TABELA. 
# Cada TIPO vai ter PRECISÃO diferente (pra dimensionar)...

# o símbolo ; indica o fim do COMANDO.

USE cadastro; # Run!

CREATE TABLE pessoas (
  nome VarChar(30),
  idade TinyInt(3),
  sexo Char(1),
  peso Float,
  altura Float,
  nacionalidade VarChar(20)
); # Run! 

DESCRIBE pessoas; # RUN! vai abrir a estrutura do nome, idade, sexo, etc., varchar, tinyint, char...



# Vamos abrir o Wamp Server > MySql > MySQL Console (Terminal)
# Prompt de comando do mysql.exe
mysql> show databases;

"""
mysql> show databases;

+--------------------+
| Database           |
+--------------------+
| cadastro           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
"""

mysql> use cadastro;
"""Database changed"""

mysql> status;
"""
mysql> status
--------------
c:/wamp64/bin/mysql/mysql8.0.31/bin/mysql.exe  Ver 8.0.31 for Win64 on x86_64 (MySQL Community Server - GPL)

Connection id:          12
Current database:       cadastro
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
Uptime:                 39 min 50 sec

Threads: 4  Questions: 206  Slow queries: 0  Opens: 185  Flush tables: 3  Open tables: 101  Queries per second avg: 0.086
--------------
"""

mysql> show tables;
"""
mysql> show tables;
+--------------------+
| Tables_in_cadastro |
+--------------------+
| pessoas            |
+--------------------+
1 row in set (0.01 sec)
"""

mysql> describe pessoas;
"""
mysql> describe pessoas;
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| nome          | varchar(30) | YES  |     | NULL    |       |
| idade         | tinyint     | YES  |     | NULL    |       |
| sexo          | char(1)     | YES  |     | NULL    |       |
| peso          | float       | YES  |     | NULL    |       |
| altura        | float       | YES  |     | NULL    |       |
| nacionalidade | varchar(20) | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
6 rows in set (0.01 sec)
"""

mysql> exit

# APRENDE O COMANDO MANO, sim mesmo em terminal!!!! 

"""
Para cadastrar novos registros, vamos adicionar no Vladmir (mas atenção):

  Vladmir
  65 anos
  Masc
  115.78 kg
  1.85 kg
  Rússia

Se por acaso já existisse o registro do Vladmir, a tabela não iria acusar erro, e iria fazer um novo cadastro do Vladmir... :'( Pois não tem chave primária...
Mas vamos aprimorar a estrutura da tabela na próxima aula...
"""



"""
Transcrição


0:00
♫ Cantarolando uma música ♫
0:19
Olá pequeno gafanhoto
0:21
Seja bem vindo a mais uma aula do seu curso de banco de dados
0:24
O meu nome é Gustavo Guanabara
0:25
Eu sou seu professor
0:27
E chegamos à mais uma do curso de banco de dados
0:30
E dessa vez nós vamos fazer o que tá todo mundo esperando
0:33
Criar o nosso primeiro banco de dados
0:35
Então, olha só
0:36
É muito importante que eu seja chato mais uma vez e diga
0:39
Você não pode pular etapas
0:41
Você vai falar assim: "Ah não, eu quero logo criar o banco de dados"
0:43
"Então vou procurar qual é o vídeo de criar o banco de dados"
0:46
Na primeira aula eu expliquei o que é um banco de dados
0:48
Pra que que ele serve.. como ele funciona
0:51
Na segunda aula a gente viu como instalar e preparar o ambiente
0:54
Então eu já to com o ambiente todo preparadinho
0:56
Se você não viu essa aula, você não está com o ambiente preparado
1:00
Então, meu querido, vai na playlist
1:02
Oh! Clique aqui
1:02
Você vai direto para a playlist
1:04
Ou acessa lá o cursoemvideo.com
1:06
Ou acessa nossa playlist do YouTube
1:08
Você vai saber se virar
1:09
E assiste as primeiras aulas
1:11
É muito valioso
1:12
É muito importante
1:14
Que você saiba
1:15
Aquilo que eu falei nas aulas anteriores
1:17
Então meu querido
1:18
Não pule etapas
1:19
E como todos os cursos do Curso em Video até o momento,
1:22
Esse curso de banco de dados não poderia ser diferente
1:24
E ele é voltado para o público iniciante
1:27
Eu já falei isso anteriomente
1:28
E vou falar várias vezes
1:29
Se você já é um usuário avançado
1:31
Se você já sabe MySQL
1:33
Você não vai aprender muita coisa aqui
1:35
Assiste os videos
1:36
Porque sempre vai ter uma coisa nova
1:38
Mas o foco aqui é para o iniciante
1:41
É para aquele cara que nunca criou um banco de dados
1:43
Ou criou poucos bancos de dados
1:45
Ou não sabe muito MySQL
1:47
Sabe criar em outro banco por exemplo
1:49
Já sabe Access
1:50
Se já sabe Oracle
1:51
Mas ainda não sabe MySQL
1:52
Então vocês vão ver
1:53
Pequenas diferenças
1:55
E mais uma vez explicando
1:56
E foco deste curso é no MySQL
1:58
Na linguagem SQL
2:00
Nas instruções SQL
2:02
A gente vai dar uma passadinha sobre o modelo relacional
2:05
Mas não é nosso foco da teoria de banco de dados
2:08
Nós vamos botar a mão na massa
2:09
Afinal de contas
2:10
O Curso em Vídeo é isso
2:11
E além disso tudo
2:12
E além disso tudo você sabe que
2:13
O Curso em Vídeo a gente dá uma mastigada
2:15
Eu dou aquela explicada
2:16
Daquele jeitinho que você gosta
2:18
Que eu sei fazer né
2:19
Que eu organizo tudo bonitinho
2:20
E eu organizei uma história aqui pra você
2:22
Para você entender
2:24
A estrutura de um banco de dados
2:26
Eu sei que a gente já viu isso
2:27
No iniciozinho lá da primeira aula
2:28
Mas agora vou te explica de uma outra maneira
2:30
Então se você ainda não entendeu
2:32
Se você esqueceu
2:33
Seu você ainda está um pouquinho confuso
2:34
Presta atenção
2:35
Que desta vez vai
2:37
Apresento a vocês o meu pequeno amigo aqui
2:40
O que foi?
2:41
Achou feio?
2:42
Não é nada, é bonitinho
2:43
Se você achou ele feio,
2:44
Imagina o nome dele
2:46
O nome dele é Godofredo
2:47
Ele é meu amigo
2:48
Posso botar o nome que eu quiser?
2:50
Valeu?
2:51
O Godofredo tem 32 anos,
2:52
É do sexo masculino,
2:54
Tem 78,5kg
2:56
Tem 1,83m
2:58
E é Brasileiro.
2:59
São características que o Godofredo tem e que você também tem
3:02
Você também não tem um nome?
3:03
Você não tem uma idade?
3:03
Peso? Altura?
3:04
Uma nacionalidade?
3:06
Todo mundo tem isso.
3:07
E além do Godofredo,
3:08
Eu vou te apresentar a parceira dele
3:10
Há alguns anos atrás
3:11
O Godofredo conheceu essa bela mulher
3:13
O nome dela mais bonito ainda
3:15
Dolores
3:16
A Dolores ela tem 30 anos
3:18
Ela é do sexo feminino
3:19
Tem 52,3 kg
3:22
Tem 1,65m de altura
3:24
E mora no México
3:25
Então o Godofredo conheceu a Dolores
3:27
Numa viagem, sei lá
3:29
Inventa ai na sua cabeça o que você quiser
3:31
Então são duas pessoas
3:32
Com características semelhantes
3:34
Mas eu vou apresentar para você uma terceira pessoa
3:36
Do fruto do amor do Godofredo com a Dolores
3:39
Nasce
3:39
A filhinha do Godofredo e da Dolores
3:41
Que se chama
3:42
Godolores
3:43
Você esperava coisa melhor?
3:45
A Godolores está com 3 aninhos
3:47
É do sexo feminino
3:49
Tem 25,8 kg
3:51
Tem 89 cm
3:53
E nasceu nos Estados Unidos
3:55
Sim
3:56
O Godofredo e a Dolores viajaram para os Estados Unidos
3:58
E tiveram a Godolores
4:00
Não interfere na minha história
4:03
O fato aqui não é o meu bom gosto para a escolha de nomes
4:05
O fato aqui é que essas três pessoas
4:08
Elas tem características semelhantes
4:10
Dá uma olhada
4:11
Qualquer um dos três
4:13
Tem características
4:14
Que são comuns a todos eles
4:16
Eles tem um nome
4:17
Eles tem uma idade
4:19
Eles tem sexo
4:20
Eles tem o peso
4:21
A altura
4:21
E a nacionalidade
4:22
Cada uma das personagens que eu apresentei aqui
4:25
Seu próprio nome, sua própria altura,
4:27
Seu próprio peso, sua própria nacionalidade
4:28
Seu próprio sexo
4:29
E isso os faz instâncias
4:32
E isso os faz pessoas diferentes umas das outras
4:35
E esse é o objetivo do banco de dados
4:37
Registrar instâncias separadas
4:40
De coisas que têm características semelhantes
4:43
Então basicamente utilizando este padrão
4:45
Eu posso cadastrar qualquer tipo de pessoa
4:48
Porque todas elas tem as mesmas características
4:51
E note que são características e não os valores
4:53
As características são as mesmas
4:55
Todos esses tem nomes
4:56
Mas cada um tem seu próprio nome
4:58
Então basicamente eu posso pegar todas essas pessoas
5:01
E colocar, sei lá, num container
5:02
Segue minha linha de raciocínio
5:04
Nesse container eu vou escrever do lado de fora bem grande "Pessoas"
5:07
Isso é
5:07
Esse container
5:09
Todas as vezes que eu tiver uma pessoa
5:11
E que eu quiser guardar esta pessoa
5:13
Eu vou colocar neste container
5:14
E todas as instâncias que estiverem dentro deste container
5:18
Vão ter estas características
5:20
Todas elas vão ter que ter estas características
5:22
Algumas, por exemplo, podem ser opcionais
5:24
Como, por exemplo, nacionalidade
5:25
Pode ser que eu
5:26
Não precise da nacionalidade de todo mundo
5:28
Mas existe...
5:30
@#$%*
5:32
Mas existe a possibilidade de cadastro desta nacionalidade
5:36
Ficou claro ai?
5:37
Então eu posso criar containers diferentes
5:40
Para coisas diferentes
5:42
Por exemplo, eu posso ter um container
5:44
Onde eu coloque todas as características de Jogos
5:47
Pessoas e jogos são coisas diferentes
5:50
E por isso possuem características diferentes
5:52
E por conta disso têm que estar em containers diferentes
5:55
Deu para entender qual é a ideia da coisa?
5:57
Então nesse container jogos
5:59
Eu vou colocar vários jogos
6:01
Que cada um tem suas próprias características, como título
6:04
O fabricante, o gênero
6:06
A plataforma e tudo mais
6:08
Deu para entender mais ou menos a ideia?
6:10
Então no mundo do banco de dados
6:11
Eu vou agrupar coisas
6:12
Que têm características semelhantes
6:14
E separar coisas que têm características diferentes
6:17
E essas coisas que têm características diferentes
6:19
Eu vou agrupar entre elas
6:20
Pra que todas as coisas agrupadas em containers
6:23
Tenham características semelhantes
6:25
Agora eu vou pegar esses dois containers
6:27
E colocar dentro de um Navio
6:29
Eu vou colocar esse container e levar para algum lugar
6:31
Deu para entender esta loucura?
6:34
Acho que ninguém nunca te explicou banco de dados desta maneira
6:36
Essa obra tá difícil
6:38
Vamos lá...
6:39
Mas o que importa é a aula
6:40
Então deu para entender como funciona o negócio?
6:42
Eu primeiro peguei
6:44
Pessoas que têm características semelhantes
6:45
Coloquei num container
6:47
Peguei jogos, que têm outras características
6:49
Coloquei em outro container
6:50
Esses dois containers são importantes para mim
6:52
Eu vou pegar os dois
6:53
E colocar no navio
6:54
Beleza? No mundo do banco de dados isso tudo tem nomes
6:57
O navio é o meu banco de dados
6:59
Então o banco de dados são coleções de dados
7:03
Que são de características separadas
7:06
Mas que estão organizados em locais específicos
7:10
Esses locais específicos são as minha Tabelas
7:13
Tabelas guardam dados de coisas que têm características semelhantes
7:17
E se quiser, eu posso ter várias tabelas dentro de um banco de dados
7:20
Eu acho que essa relação ficou bem clara na sua cabeça agora
7:23
Os dados dentro das tabelas também têm um nome específico, que são registros
7:28
Então resumindo, bancos de dados são conjuntos de tabelas
7:33
E tabelas são conjuntos de registros
7:36
Lembra da primeira aula quando eu falei o exemplo da ficha colocada dentro de uma pastinha?
7:40
E colocada dentro de um arquivo metálico?
7:42
É exatamente a mesma relação
7:44
Só que eu resolvi extrapolar isso e explicar de uma maneira diferente
7:47
Criando uma historinha aqui pra você
7:49
Mas os conceitos são exatamente os mesmos
7:51
Eu só criei uma forma um pouquinho mais divertida e um pouquinho mais maluca
7:55
Então, pra começar, a primeira coisa que eu tenho que criar é o meu banco de dados
7:59
Criar um banco de dados usando o MySQL é muito simples
8:03
Você simplesmente tem que dar o comando
8:05
'create database' e o nome do banco de dados
8:08
no meu caso aqui eu vou chamar de 'cadastro'
8:10
Então, create database cadastro;
8:14
Tá, mas onde eu vou colocar esta linha?
8:16
Exatamente no ambiente que a gente preparou, todo bonitinho, na aula passada
8:20
Você se lembra né?
8:22
Então, vamos partir diretamente para o nosso ambiente
8:24
Então eu estou aqui no Windows, e a primeira coisa que eu vou fazer é abrir o WAMP Server
8:30
Então, o WAMP Server a gente instalou na aula passada
8:33
Então vou abrir ele
8:34
Se você perceber aqui embaixo tem um 'W' vermelho
8:37
Quando ele ficar verde...
8:38
tá amarelo... verde
8:39
Agora sim, já está funcionando meu servidor
8:42
Para acessar o banco de dados eu posso clicar aqui e vou abrir o meu MySQL Workbench
8:49
Em alguns segundos ele vai abrir a aplicação
8:52
Deixa eu maximizar aqui
8:54
E nós vamos abrir a instância do WAMP Server, que foi previamente aberta
9:01
Nunca se esqueça, você tem que abrir o WAMP Server antes e esperar o 'W' ficar verde
9:06
Então, esse é o ambiente do Workbench
9:08
Basicamente, você vai ter que entender o seguinte
9:11
Aqui no cantinho, oh, você percebe que talvez não esteja aparecendo tudo
9:14
Pode ser que a sua tela esteja um pouco mais povoada dessa maneira
9:19
Eu não gosto muito desta bagunça que ele cria
9:21
Então o que eu vou fazer é esconder as barrinhas
9:24
Pra isso eu posso esconder, oh, a barra da esquerda, a barra de baixo e a barra da direita
9:29
Eu fico somente com as Querys, somente com as minhas consultas aqui
9:33
Com as instruções que eu vou colocar
9:35
No caso aqui ainda eu vou abrir a coluna da esquerda
9:39
Para eu poder verificar se o que eu criei está funcionando
9:43
Para isso eu vou aqui em esquemas...
9:46
E vamos ver se a gente vai realmente criar um banco de dados
9:50
Então, vamos colocar a mão na massa e digitar aquele comando lá
9:53
O comando que a gente viu foi o...
9:55
create
9:56
database
9:59
cadastro;
10:00
a gente vai criar um banco de dados chamado 'cadastro'
10:03
Você pode digitar em maiúsculas, em minúsculas, você pode escolher
10:06
Feito isso, vamos executar o comando
10:09
Para executar o comando que está ativo,
10:11
Você vai clicar nesse raiozinho que está aqui que tem um tracinho em pé
10:15
Que é executar o comando que está selecionado
10:18
Clicando nele...
10:19
O comando foi executado com sucesso
10:22
Para verificar se ele foi com sucesso ou não
10:25
Vamos abrir a parte de baixo, aqui oh
10:27
create databade cadastro;
10:29
one row affected (uma linha afetada)
10:30
O conceito de linhas afetadas a gente vai usar bastante
10:34
Então, basicamente, é assim eu não tinha um banco
10:36
Quando eu criei um banco eu afetei uma linha, isso é, eu tenho um banco de dados novo
10:40
Vamos ver realmente se eu tenho um banco de dados novo
10:42
Vem aqui no lado esquerdo, oh
10:44
E vamos atualizar os esquemas, clicando sobre esse botão
10:48
Agora, oh, eu tenho um banco de dados 'cadastro'
10:52
Dentro de banco de dados eu tenho, como eu falei oh, eu tenho tabelas
10:55
Tenho outras coisas, mas eu tenho tabelas
10:58
Por enquanto nós vamos trabalhar somente com tabelas
11:00
Mas você tem outras coisas como por exemplo visões, procedimentos armazenados, funções
11:05
Então, vamos começar passo a passo
11:07
Como eu disse, a gente criou o navio, a gente criou o banco de dados
11:10
Que é o banco de dados cadastro
11:11
O próximo passo é partir para as nossas tabelas
11:14
Para criar a nossa tabela a gente tem que dar uma relembrada
11:16
O meu container de pessoas ele tem características padronizadas para todos eles
11:21
Então todos eles da tabela pessoas vão ter:
11:25
nome, idade, sexo, o peso
11:28
a altura e nacionalidade
11:30
Essas características são chamadas de campos
11:33
Então vai anotando aí, olha só
11:35
Banco de Dados contém Tabelas
11:39
Tabelas contém Registros
11:41
Registros são compostos por Campos
11:44
Viu como ficou bem parecido com a tua aula de banco de dados do colégio ou da faculdade
11:48
Só que de uma maneira um pouco diferente
11:50
Vamos começar a criar essa estrutura aí
11:52
Para criar nós vamos usar um comando bem simples também
11:56
Se para criar o banco de dados foi: create database
11:58
Para criar tabela vai ser: create table
12:00
Então vou criar a tabela 'pessoas'
12:03
Abro, fecho parêntesis, ponto e vírgula
12:05
Vamos voltar aqui ao nosso ambiente
12:07
Esse comando já executei, vou executar outro comando aqui
12:10
create table pessoas
12:13
Abro, fecho parêntesis
12:15
ponto e vírgula
12:17
Vou organizar aqui mais ou menos, vou dar um espacinho
12:20
Não se preocupe com este erro, já já ele vai sumir
12:22
Dentro do comando 'create table' nós vamos colocar os campos:
12:26
nome, idade, sexo, peso, altura e nacionalidade
12:31
Vamos colocar lá
12:32
Nome, idade, sexo
12:34
nacionalidade
12:37
Ah, vou colocar a vírgula aqui depois de cada um deles
12:40
Para a gente poder exemplificar
12:44
Então tenho que separar, o nacionalidade não precisa de vírgulo porque é o último
12:48
Não se preocupe com os erros ainda
12:50
Agora eu tenho que dizer o tipo de cada um destes campos
12:54
Sim, assim como nos algorítimos você tem que colocar as variáveis relacionadas a um tipo primitivo
13:00
*O que? Tu não fez algorítmo ainda?*
13:02
Aqui oh! cursoemvideo.com
13:04
A gente tem o curso de algorítimo, tá na playlist, clique aqui
13:08
Você vai direto para a playlist, assiste isso, algorítimo é a base de tudo
13:12
Quando você aprender o MySQL e precisar usar o PHP
13:16
Para unificar o banco de dados com PHP
13:19
A primeira coisa que você tem que saber é algorítimo
13:21
Então a gente tá caminhando aí no Curso em Vídeo para uma coisa bem maior
13:25
Então, se prepara Gafanhoto
13:27
Então a gente vai ter que conhecer quais são os tipos primitivos antes de colocá-los
13:32
O MySQL tem um monte de tipos primitivos
13:34
Eu vou selecionar alguns aqui para vocês
13:36
Os tipos primitivos do MySQL separa tudo em algumas famílias
13:41
Como a família dos numéricos, data e tempo, literais e epacial
13:46
Então quando você trabalha lá com os algorítimos a gente tem 4 famílias né:
13:50
Números inteiros, números reais, carácteres e lógico
13:53
Aqui também são 4 famílias:
13:55
Números, data e tempo, os literais e os espaciais
13:59
Só que eles têm subdivisões e subtipos
14:01
Os tipos numéricos se subdividem em: Inteiros, Reais e Lógicos
14:07
E aí vem uma das grandes diferenças do MySQL
14:09
Precisão
14:10
Como os dados vão ser armazenados em disco
14:12
Você precisa saber dimensionar muito bem a estrutura da sua tabela
14:16
Nessa primeira aula a gente não vai aprimorar muito, não vai aprofundar muito
14:22
Até porque deixa eu fazer um parênteses aqui
14:24
Quem sabe muito banco de dados já deve estar me execrando aqui, já deve estar me cruxificando
14:29
Poxa, cadastrar idade no banco de dados?
14:31
Calma Gafanhoto! A gente tá começando
14:34
Já já vou desfazer este negócio
14:36
Quem tem experiência em banco de dados sabe que não se cadastra idade em banco de dados
14:40
Até porque idade muda constantemente
14:42
Mas, estamos no passo a passo
14:44
Paciência Gafanhoto! Paciência é muito importante
14:48
Outra família que se subdivide é a família dos literais
14:51
Os literais se subdividem em caracteres, textos, binários e coleções
14:57
Tá dificultando muito?
14:59
Calma a gente nem vai precisar disso tudo agora
15:01
Só vou exemplificar pra isso aqui ficar completinho
15:03
Como eu falei, cada um destes tipos tem precisões diferentes
15:07
Vamos por exemplo ver quais são os tipos inteiros
15:10
Num algorítimo, tipo inteiro é tipo inteiro, no banco de dados não!
15:13
Tipo inteiro num banco de dados MySQL ele se subdivide em vários outros tipos com precisões diferentes
15:18
Como por exemplo: TinyInt, SmallInt, Int, MediumInt e BigInt
15:23
A diferença desses esses tipos é a quantidade de bytes que ele vai utilizar para armazenar este dado
15:29
O TinyInt por exemplo ele usa muito menos dados do que por exemplo o BigInt
15:34
Então o BigInt vai usar muitos bytes em disco e o TinyInt vai usar pouquinho
15:39
Isso vai influenciar diretamente no tamanho do número que você vai guardar
15:43
Por exemplo, idade você não vai precisar utilizar o Int inteiro
15:46
Você usa o TinyInt que utiliza apenas 3 bytes na memória
15:50
O mesmo acontece para os tipos reais que tem o decimal, float, double e real
15:55
O tipo lógico também tem dois, o bit e o boolean
15:58
O tipo lógico ele guarda sim e não, verdadeiro e falso, 0 e 1
16:02
Para data e para tempo nós temos: Date, DateTime, TimeStamp, Time e Year
16:08
Basicamente o Date é uma data, DateTime e TimeStamp vão ser datas, horas e algumas informações a mais
16:15
Time somente hora e Year somente um ano
16:18
Vamos agora para os tipos literais, começando pelo Caractere, que tem os tipos Char e VarChar
16:23
A diferença entre o Char e VarChar tá no próprio nome
16:26
Um é fixo o outro é variante
16:28
Basicamente é o seguinte:
16:29
Se eu digo que o nome tem 30 letras... o nome é um tipo literal, né?
16:34
Se eu digo que um nome tem 30 letras e ele é Char, ele vai armazenar com 30 letras
16:39
Ah mas o nome do cara é Zé, só usou 2 letras. Ele vai ter duas letras guardadas
16:44
e o resto tudo preenchido com espaço, porque no disco você disse que vai ter 30 espaços fixos
16:51
VarChar é diferente, você coloca lá, o nome vai ter até 30 letras, VarChar
16:57
então se tiver Zé, ele vai guardar só dois e vai deixar os outros la disponoveis
17:03
ele não vai colocar espaços, ele não vai ocupar 30. Ficou claro?
17:07
Se ainda não ficou mais pra frente você vai aprender melhor
17:10
então existem dois tipos: Char e Varcha. A maioria a gente vai ultilizar VaChar
17:14
o tipo texto eu tenho: TinyText, Text, MediumText e LongText
17:18
e ai qual é a diferença entre o caractere e o texto?
17:22
textos é pra textos longos você quer a descrição de uma pessoa
17:26
você quer guardar um texto longo no seu banco de dados, usa o tipo Text
17:30
quer guardar um nome, um endereço, um telefone, uma coisa caractere, guarda no tipo Char ou VarChar.
17:37
O tipo Binário são os tipos Blob. Eu tenho TinyBlob, Blob, MediumBlob e LongBlob
17:41
o tipo Blob ele permite guardar qualquer coisa em binário por exemplo, uma imagem
17:46
apesar de não recomendado guardar uma imagem dentro de um banco de dados
17:50
é possível utilizando esse tipo como Blob
17:52
temos também o tipo Coleção que é o Enum e o Set
17:55
Emun e Set são tipos que você pode configurar quais são os valores permitidos
18:00
e na hora do cadastro ele so vai aceitar esses valores
18:04
a gente vai isso mais na próxima aula como funciona mais especificamente os tipos Enum e Set
18:09
e por fim nós temos os tipos Espaciais como Diometry, Point, Polygon, MultiPolygon e muitos outros
18:16
o tipo espacial é um tipo novo do MySql a partir da versão 5 se eu não me engano
18:20
e ele permite guardar informação sobre volumétricos
18:23
nós não vamos tratar esse tipo de dado, essa família espacial no nosso curso
18:28
mas se você precisa fazer o cadastro de algo volumétrico e que precise de informações
18:33
da uma pesquisada nessa família espacial e você vai ter com certeza muita coisa legal pra aprender
18:39
Então esse ai são os tipos primitivos do MySql
18:43
Ficou muito coisa? Você precisa decorar isso tudo, aos poucos você vai utiizando
18:48
É importante você saiba dimensionar bem um banco de dados
18:51
Mais uma vez eu vou deixar claro
18:53
Nessa tabela que a gente ta criando agora essa primeira tabela, eu não estou dimensionando muito bem
18:59
Eu vou dimensionar melhor mais pra frente
19:01
Então vamos voltar para o comando que a gente tinha preparado até o momento
19:04
E vamos começar a dar tipos para cada um dos campos
19:07
O nome, por exemplo, eu vou colocar como varchar (30)
19:10
A idade, como tinyint com 3 espaços
19:14
O tinyint você não tem a obrigatoriedade de colocar o '3' entre parêntesis, pode colocar só tinyiny
19:19
E ele indica que está ocupando 3 bytes
19:22
O tipo Int, como curiosidade, ocupa 11 bytes
19:25
O sexo eu vou definir como char (1)
19:27
Isso é, ele vai sempre guardar uma letra independente se eu coloque ou não o sexo
19:32
Ele vai reservar um espaço ali, porque eu usei char
19:34
O peso vai ser float
19:35
A altura também vai ser float
19:38
E a nacionalidade vai ser varchar (20)
19:40
Vamos colocar em prática, digitando todos esses valores no meu MySQL Workbench
19:46
Então vamos lá, nome
19:48
varchar (30)
19:51
idade vai ser tinyint
19:55
Como eu disse não tem obrigatoriedade em colocar (o valor 3)
19:57
Você percebe que os erros estão sumindo aqui no canto?
20:00
sexo char (1)
20:04
peso float
20:06
altura float
20:09
E nacionalidade varchar (20)
20:12
Lembrando que não tem vírgula no último comando, se você colocar vírgula aqui
20:16
Ele vai dar erro embaixo porque ele está esperando outro
20:18
Então eu não tenho aqui
20:20
Basicamente um comando MySQL não é composto
20:25
Então se eu coloquei aqui 8 linhas eu não tenho 8 comando, eu tenho um comando só
20:28
Porque eu só tenho um ponto e vírgula ';'
20:30
O simbolo de ponto e vírgula indica o fim do comando
20:34
Vamos agora executar este comando
20:36
Pause o video na tela, digite seu código e execute
20:40
Não adianta você assister a aula assim oh...
20:43
Você vai ver eu fazendo e na hora de você fazer você não vai lembrar do comando
20:47
Então, pequeno Gafanhoto, faça!
20:48
Vamos executar o comando que está marcado
20:52
Clicando sobre este botão
20:53
Ele deu um erro aqui porque eu não tenho um banco de dados aberto
20:57
Para eu abrir um banco de dados
20:59
Eu posso usar o comando aqui oh
21:00
Vou colocar aqui em cima
21:02
use cadastro
21:06
Ou então você clica duas vezes aqui em cadastro
21:08
Você está vendo que cadastro está clarinho aqui?
21:11
Você deixar selecionado aqui o comando que está sendo executado
21:15
Vou executar
21:15
Agora 'cadastro' é o banco de dados que está ativo
21:19
Agora vamos executar de novo
21:21
Agora ele deu o comando 'create table' válido
21:23
Eu posso vir aqui em tabelas, vamos atualizar o esquema
21:27
Agora eu tenho a tabela 'pessoas'
21:29
Então a tabela 'pessoas' tem as seguintes colunas:
21:32
nome, idade, sexo, peso, altura e nacionalidade
21:36
Viu como é simples o negócio?
21:38
Você quer ver como funciona, mais ou menos, a estrutura interna de uma tabela?
21:42
Vamos lá. Você pode vir aqui embaixo
21:44
Vou colocar um comando novo
21:45
Vou dar o comando: 'describe table pessoas'
21:50
'Describe' pessoas significa descreva pessoas para mim
21:53
Na hora que eu executar o comando
21:55
Ele vai abrir a estrutura, oh
21:57
Deixa eu esconder a parte de baixo para você conseguir ver
22:00
nome, idade, sexo, peso, altura, nacionalidade
22:04
Tem todas as estruturas, oh
22:05
Float, tal, tem algumas informações que a gente ainda não viu
22:08
Vamos ver isso na próxima aula
22:10
Mas a tabela foi criada
22:12
Viu como é simples quando você usa o MySQL e você usa o Workbench?
22:16
Mas, basicamente, você também pode fazer isso também no modo terminal
22:19
Vamos dar uma olhada aqui
22:20
Se você clicar aqui em baixo no ícone do WAMP Server e clicar em MySQL
22:24
Console MySQL, ele vai abrir, como na aula passada, a tela de terminal
22:29
Não tem senha, lembra? Só dar Enter
22:31
E eu vou colocar aqui oh, por exemplo,
22:34
show databases
22:36
Pra ele ver e mostrar quais são os bancos de dados criados
22:40
Você pode ver aqui que existe o banco de dados 'cadastro' que nós criamos nesta aula
22:45
O ambiente é o mesmo
22:46
Então vamos abrir o banco de dados cadastro
22:48
use cadastro
22:51
Olha lá, já estou utilizando
22:53
Pra você ver o banco de dados que está aberto, o comando 'status'
22:57
No comando 'status' você tem aqui o banco de dados atual é o banco de dados 'cadastro'
23:03
Posso dar o comando 'show tables'
23:06
Para ele me mostrar quais são as tabelas
23:08
No caso aqui do banco de dados cadastro
23:10
Eu só tenho a tabela pessoas
23:11
Vou dar um 'describe pessoas'
23:14
E ele vai descrever tal e qual eu fiz lá no outro ambiente
23:18
Ficou claro?
23:19
Então, eu não estou usando mais aqui o ambiente terminal para a coisa ficar mais bonitinha,
23:24
Para a coisa ficar mais clara
23:26
Mas o objetivo aqui é a gente aprender os comandos
23:29
Aí vem uma coisa que eu gostaria de explicar muito claramente aqui
23:33
Pra gente poder entender um negócio
23:35
Quando você aprendeu Java comigo, eu falei que era melhor utilizar uma IDE
23:39
Que ficar digitando o comando era uma coisa muito trabalhosa
23:42
No SQL é muito importante que você aprenda a linguagem SQL
23:47
Porque são esses comandos que eu estou te dando aqui
23:49
Que você vai utilizar na hora de progrmar em PHP por exemplo
23:53
Então você pode no PHP utilizar os comandos 'create database'
23:57
O comando 'create table'
23:59
Então esse tipo de coisa é muito importante você aprender o comando
24:04
Então, meu pequeno Gafanhoto,
24:05
Aprende do jeito que eu estou te falando
24:07
É a maneira que eu julgo mais importante
24:10
Se você julgar outra forma, beleza!
24:13
"Ah eu já fiz outro curso e ele ensinou clicando o botão e fazendo"
24:18
Beleza, você vai aprender a criar o banco de dados mas você não vai saber o comando para criar
24:23
Que é valioso na hora de você programar em linguagens
24:26
Como Java, PHP
24:27
Então, meu objetivo aqui é ensinar comandos SQL e não utilizar ferramentas de Workbench
24:33
Então vou sair daqui
24:34
Pra sair do MySQL, exit, e ele sai
24:37
Você pode ter maiores informações sobre a tabela clicando sobre esse iconezinho aqui
24:41
com um pequeno 'i'
24:43
Aqui você vai ter as informações de quanto ele está ocupando em disco
24:46
Quais são as colunas, qual é a estrutura do banco de dados
24:50
Quais são os índices
24:51
Os gatilhos
24:53
As chaves estrangeiras, as partições, quem tem permissão
24:57
Então aqui é importante. Para fecha isso, vou fechar aqui a aba
25:00
E você volta para sua área de Query
25:03
Viu a vantagem do Workbench?
25:05
O Workbench vai te facilitar em relação a esse tipo de coisa
25:08
Porém eu tenho um pequeno problema nesta estrutura
25:11
Com a tabela que a gente criou
25:13
A gente deve ser capaz de cadastrar qualquer uma dessas pessoas que está aparecendo ai na tela
25:16
Como por exemplo, o senhor Vladimir
25:18
Que tem 65 anos
25:20
É homem, tem 115,78kg
25:23
1,85 m de altura
25:24
E mora na Rússia
25:25
Para cadastrar novos registros, a gente vai utilizar um outro comando que é o 'insert into'
25:29
Que a gente vai ver em outra aula
25:31
Geralmente as pessoas chamam de "insert intô"
25:33
O problema desta estrutura que a gente criou agora
25:35
Assim, esta estrutura tem vários problemas, como por exemplo,
25:38
Não pode cadastrar idade
25:39
Os dados não estão bem definidos
25:42
E uma coisa muito importante que é um problema que vai acontecer neste banco de dados
25:47
Se por um acaso eu me equivocar, já cadastrar o senhor Vladimir uma vez
25:50
E quiser cadastrar ele de novo, ele vai permitir
25:53
Isso porque a tabela que a gente criou de criar ainda não tem uma chave primária
25:56
Mas isso é assunto para a outra aula
25:59
Sem uma chave primária é possível acontecer isso
26:01
Cadastrar o senhor Vladimir duas vezes
26:03
Não só duas, eu posso cadastrar quantas vezes eu quiser o senhor Vladimir
26:07
E não é isso que eu vou querer no banco de dados
26:09
Mas por enquanto, essa aula para por aqui
26:11
Na próxima aula a gente vai aprimorar a estrutura desta tabela
26:15
Que a gente acabou de criar
26:16
Então, pequeno Gafanhoto, é isso
26:18
A gente se vê na próxima, na 4ª aula do curso de banco de dados
26:22
Eu espero que você tenha gostado
26:23
Eu espero que você tenha entendido
26:25
Eu espero sinceramente que você esteja praticando
26:28
Esteja fazendo junto comigo na aula
26:30
Como de costume, no finalzinho da nossa aula,
26:32
Eu queria te pedir sempre
26:33
Pra se inscrever no canal
26:34
Me dar essa honra
26:36
De ser um dos alunos inscritos
26:37
A gente já está com mais de 120 mil alunos
26:39
Então me dá esta honra? Por favor?
26:41
Se inscreve aqui no canal e seja mais um dos felizes alunos cadastrado no Curso em Video
26:46
Clicando aqui
26:47
Você vai ter acesso a playlist no curso de banco de dados
26:49
Todas as aulas vão estar lá
26:51
Todas organizadas
26:53
Tudo bonitinho, para você poder aprender direito
26:56
Materiais exclusivos, material dos slides disponibilizados
26:59
Qualquer download que você queira fazer
27:01
Do WAMP Server, o download do Workbench
27:05
Tudo aqui, www.cursoemvideo.com
27:08
Se inscreve lá
27:09
Faz o curso de banco de dados por lá
27:11
Por todas as informações extras, todos os arquivos estarão lá
27:15
Se você é professor e quer utilizar os Slides
27:18
Eu disponibilizo eles em pdf lá para você
27:20
Você poder utilizar na aula essa loucura ai que eu estou utilizando aqui durante a aula
27:25
Você pode utilizar, contanto que os direitos sejam mantidos
27:29
Tem que dizer lá, olha, usei do Curso em Vídeo
27:31
Esse aqui é um material criado pelo professor Gustavo Guanabara
27:34
Beleza senhores?
27:35
Um forte abraço pequeno Gafanhoto
27:37
Estude sempre!
27:39
Estude bastante!
27:41
Se você ainda não fez o curso de algoritmo, o curso de PHP
27:43
Faça! Até a próxima aula, dá um tempinho
27:46
Um forte abraço e até a próxima
"""





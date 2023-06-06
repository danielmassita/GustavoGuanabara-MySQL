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










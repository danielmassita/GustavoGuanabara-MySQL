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



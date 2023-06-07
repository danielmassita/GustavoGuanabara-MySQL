# Curso MySQL #04 - Melhorando a Estrutura do Banco de Dados 

# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/melhorando-a-estrutura-do-banco-de-dados/ 
# https://youtu.be/cHLKtALWDos

"""
Aula 04 - Curso MySQL #04 - Melhorando a Estrutura do Banco de Dados 

Hello, world! Vamos melhorar a estrutura do banco de dados. Basicamente, vamos refazer de uma maneira melhor (comandos de alter-table). 
E lembra do bug? Múltiplos cadastros do seu Valdemir? Vamos corrigir!

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

Na aula passada, usamos os seguintes comandos:

MySQL Workbench

      SHOW databases;
      CREATE DATABASE cadastro;
      USE cadastro; 
      CREATE TABLE pessoas (
        nome VarChar(30),
        idade TinyInt(3),
        sexo Char(1),
        peso Float,
        altura Float,
        nacionalidade VarChar(20)
      ); 
      DESCRIBE pessoas; 
"""

# Vamos começar deletando o último BD chamado cadastro.
DROP DATABASE cadastro;

# Vamos criar um novo DB com dois PARÂMETROS (Constraints)
CREATE DATABASE cadastro
DEFAULT CHARACTER SET utf8
DEFAULT COLLATE utf8_general_ci;

# Vamos agora atualizar a ESTRUTURA da tabela, com campos mais inteligentes e tipos primitivos bem dimensionados... Mas já vamos OTIMIZAR a estrutura das tabelas.
# Se um INT usa 11 bytes e TinyInt usa 3 bytes. Mas se falarmos de milhões de dados... ;)
# Por exemplo, ao cadastrar a idade vamos usar o dia que nasceu, assim a tabela será dinâmica e atualizada sempre.

CREATE TABLE pessoas (
    `id` int NOT NULL AUTO_INCREMENT,
    `nome` varchar(30) NOT NULL ,
    `nascimento` date,
    `sexo` enum('M', 'F'),
    `peso` decimal(5,2),
    `altura` decimal(3,2),
    `nacionalidade` varchar(20) DEFAULT 'Brasil', 
    primary key (id)
) default charset = utf8;

DESCRIBE pessoas;

# Usamos duas constraints (not null e default).
# Sempre importante ter um campo tipo CHAVE PRIMÁRIA (únicas).











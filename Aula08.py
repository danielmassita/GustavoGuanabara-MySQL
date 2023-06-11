# Curso MySQL #08 - Gerenciando Cópias de Segurança MySQL
# https://youtu.be/w6OYS_M7hTM
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/gerenciando-copias-de-seguranca-mysql/

# GERENCIANDO CÓPIAS DE SEGURANÇA!

USE cadastro;

DESCRIBE gafanhotos;
DESC cursos;

SELECT * FROM cursos;

# Gerando um DUMP de uma BASE DE DADOS (dump = backup no servidor)
# MySQL Workbench > Server > Data Export > 
"""
(seleciona o schema e os objetos/tabelas)
(cadastro + cursos + gafanhotos ++ Dump Structure and Data)
(objects to export > stored procedures + events + triggers)
(export to self contained file > + include create schema) # SEMPRE MARCAR INCLUIR O SCHEMA! 
(start export)
"""

# Depois de feito o backup, podemos na moral apagar tudo!
DROP DATABASE cadastro;

# MySQL Workbench > Server > Data Import > 
"""
Import Dump from Project Folder 
or
Import from Self-Contained File (C:\...)
Start Import 
"""
USE cadastro;
# 3	4	01:22:22	USE cadastro	0 row(s) affected	0.000 sec

SHOW TABLES;
"""
cursos
gafanhotos
"""

DESCRIBE gafanhotos;
"""
codigo	int	YES			
id	int	NO	PRI		auto_increment
nome	varchar(30)	NO			
prof	varchar(20)	YES			
nascimento	date	YES			
sexo	enum('M','F')	YES			
peso	decimal(5,2)	YES			
altura	decimal(3,2)	YES			
nacionalidade	varchar(20)	YES		Brasil	
"""

DESC cursos;
"""
idcurso	int	NO	PRI		
nome	varchar(30)	NO	UNI		
descricao	text	YES			
carga	int unsigned	YES			
totaulas	int unsigned	YES			
ano	year	YES		2016	
"""

SELECT * FROM gafanhotos;
"""
	1	Godofredo		1984-01-02	M	78.50	1.83	Brasil
	2	Maria		1999-12-30	F	55.20	1.65	Portugal
	3	Creuza		1920-12-30	F	50.20	1.65	Brasil
	4	Adalgiza		1930-11-02	F	63.20	1.75	Irlanda
	5	Cláudio		1975-04-22	M	99.00	2.15	Brasil
	6	Pedro		1999-12-03	M	87.00	2.00	Brasil
	7	Janaína		1987-11-12	F	75.40	1.66	EUA
"""

SELECT * FROM cursos;
"""
1	HTML5	Curso de HTML5	40	37	2014
2	Algoritmos	Lógica da Programação	20	15	2014
3	Photoshop	Dicas de Photoshop CC	10	8	2014
4	PHP	Curso de PHP para Iniciantes	40	20	2015
5	Java	Introdução à Linguagem Java	40	29	2015
6	MySQL	Bancos de Dados MySQL	30	15	2016
7	Word	Curso Completo de Word	40	30	2016
"""


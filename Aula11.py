# Curso MySQL #11 - SELECT (Parte 1)
# https://youtu.be/GaOlyL3Uv9M
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/select-parte-1/

"""
Aula 11 - Curso MySQL #11 - SELECT (Parte 1)
- Vamos finalmente começar a falar do comando mais famoso do SQL, obtendo dados da tabela usando o SELECT. 
- Essa é a aula parte 1, pois vamos trabalhar extensamente o SELECT. 
- Vamos usar o arquivo da aula "Dump-CeV01.zip". 
- MySQL Workbench > Server > Import > From File > ...
"""
USE cadastro;
SHOW TABLES;

DESCRIBE cursos;
"""
idcurso	int	NO	PRI	0	
nome	varchar(30)	NO	UNI		
descricao	text	YES			
carga	int unsigned	YES			
totaulas	int unsigned	YES			
ano	year	YES		2016	
"""

SELECT * FROM cursos;
"""
1	HTML5	Curso de HTML5	40	37	2014
2	Algoritmos	Lógica de Programação	20	15	2014
3	Photoshop5	Dicas de Photoshop CC	10	8	2014
4	PHP	Curso de PHP para iniciantes	40	20	2015
5	Java	Introdução à Linguagem Java	40	29	2015
6	MySQL	Bancos de Dados MySQL	30	15	2016
7	Word	Curso completo de Word	40	30	2016
8	Python	Curso de Python	40	18	2017
9	POO	Curso de Programação Orientada a Objetos	60	35	2016
10	Excel	Curso completo de Excel	40	30	2017
11	Responsividade	Curso de Responsividade	30	15	2018
12	C++	Curso de C++ com Orientação a Objetos	40	25	2017
13	C#	Curso de C#	30	12	2017
14	Android	Curso de Desenvolvimento de Aplicativos para Android	60	30	2018
15	JavaScript	Curso de JavaScript	35	18	2017
16	PowerPoint	Curso completo de PowerPoint	30	12	2018
17	Swift	Curso de Desenvolvimento de Aplicativos para iOS	60	30	2019
18	Hardware	Curso de Montagem e Manutenção de PCs	30	12	2017
19	Redes	Curso de Redes para Iniciantes	40	15	2016
20	Segurança	Curso de Segurança	15	8	2018
21	SEO	Curso de Otimização de Sites	30	12	2017
22	Premiere	Curso de Edição de Vídeos com Premiere	20	10	2017
23	After Effects	Curso de Efeitos em Vídeos com After Effects	20	10	2018
24	WordPress	Curso de Criação de Sites com WordPress	60	30	2019
25	Joomla	Curso de Criação de Sites com Joomla	60	30	2019
26	Magento	Curso de Criação de Lojas Virtuais com Magento	50	25	2019
27	Modelagem de Dados	Curso de Modelagem de Dados	30	12	2020
28	HTML4	Curso Básico de HTML, versão 4.0	20	9	2010
29	PHP7	Curso de PHP, versão 7.0	40	20	2020
30	PHP4	Curso de PHP, versão 4.0	30	11	2010
"""

DESCRIBE gafanhotos;
"""
id	int	NO	PRI		auto_increment
nome	varchar(30)	NO			
profissao	varchar(20)	YES			
nascimento	date	YES			
sexo	enum('M','F')	YES			
peso	decimal(5,2)	YES			
altura	decimal(3,2)	YES			
nacionalidade	varchar(20)	YES		Brasil	
"""

SELECT * FROM gafanhotos;
"""
1	Daniel Morais	Auxiliar Administrat	1984-01-02	M	78.50	1.83	Brasil
2	Talita Nascimento	Farmacêutico	1999-12-30	F	55.20	1.65	Portugal
3	Emerson Gabriel	Programador	1920-12-30	M	50.20	1.65	Moçambique
4	Lucas Damasceno	Auxiliar Administrat	1930-11-02	M	63.20	1.75	Irlanda
5	Leila Martins	Farmacêutico	1975-04-22	F	99.00	2.15	Brasil
6	Letícia Neves	Programador	1999-12-03	F	87.00	2.00	Brasil
7	Janaína Couto	Auxiliar Administrat	1987-11-12	F	75.40	1.66	EUA
8	Carlisson Rosa	Professor	2010-08-01	M	78.22	1.98	Brasil
9	Jackson Telles	Programador	1999-01-23	M	55.75	1.33	Portugal
10	Danilo Araujo	Dentista	1975-12-10	M	99.21	1.87	EUA
11	Andreia Delfino	Auxiliar Administrat	1975-07-01	F	48.64	1.54	Irlanda
12	Valter Vilmerson	Ator	1985-10-12	M	88.55	2.03	Brasil
13	Allan Silva	Programador	1993-11-11	M	76.99	1.55	Brasil
14	Rosana Kunz	Professor	1935-01-16	F	55.24	1.87	Brasil
15	Josiane Dutra	Empreendedor	1950-01-20	F	98.70	1.04	Portugal
16	Elvis Schwarz	Dentista	2011-05-07	M	66.69	1.76	EUA
17	Paulo Narley	Auxiliar Administrat	1997-03-17	M	120.10	2.22	Brasil
18	Joade Assis	Médico	1930-12-01	M	65.88	1.78	França
19	Nara Matos	Programador	1978-03-17	F	65.90	1.33	Brasil
20	Marcos Dissotti	Empreendedor	2010-01-01	M	53.79	1.54	Portugal
21	Ana Carolina Mendes	Ator	2000-12-15	F	88.30	1.54	Brasil
22	Guilherme de Sousa	Dentista	2001-05-18	M	132.70	1.97	Moçambique
23	Bruno Torres	Auxiliar Administrat	2000-01-30	M	44.65	1.65	Brasil
24	Yuji Homa	Empreendedor	1996-12-25	M	33.90	1.22	Japão
25	Raian Porto	Programador	1989-05-05	M	54.89	1.54	Brasil
26	Paulo Batista	Ator	1999-03-15	M	110.12	1.87	Portugal
27	Monique Precivalli	Auxiliar Administrat	2013-12-30	F	48.20	1.22	Brasil
28	Herisson Silva	Auxiliar Administrat	1965-10-10	M	74.65	1.56	EUA
29	Tiago Ulisses	Dentista	1993-04-22	M	150.30	2.35	Brasil
30	Anderson Rafael	Programador	1989-12-01	M	64.22	1.44	Irlanda
31	Karine Ribeiro	Empreendedor	1988-10-01	F	42.10	1.65	Brasil
32	Roberto Luiz Debarba	Ator	2007-01-09	M	77.44	1.56	Brasil
33	Jarismar Andrade	Dentista	2000-06-23	F	63.70	1.33	Brasil
34	Janaina Oliveira	Professor	1955-03-12	F	52.90	1.76	Canadá
35	Márcio Mello	Programador	2011-11-20	M	54.11	1.55	EUA
36	Robson Rodolpho	Auxiliar Administrat	2000-08-08	M	110.10	1.76	Brasil
37	Daniele Moledo	Empreendedor	2006-08-11	F	101.30	1.99	Brasil
38	Neto Sophiate	Ator	1996-05-17	M	59.28	1.65	Portugal
39	Neriton Dias	Auxiliar Administrat	2009-10-30	M	48.99	1.29	Brasil
40	André Schmidt	Programador	1993-07-26	M	55.37	1.22	Angola
41	Isaias Buscarino	Dentista	2001-01-07	M	99.90	1.55	Moçambique
42	Rafael Guimma	Empreendedor	1968-04-11	M	88.88	1.54	Brasil
43	Ana Carolina Hernandes	Ator	1970-10-11	F	65.40	2.08	EUA
44	Luiz Paulo	Professor	1984-11-01	M	75.12	1.38	Portugal
45	Bruna Teles	Programador	1980-11-07	F	55.10	1.86	Brasil
46	Diogo Padilha	Auxiliar Administrat	2000-03-03	M	54.34	1.88	Angola
47	Bruno Miltersteiner	Dentista	1986-02-19	M	77.45	1.65	Alemanha
48	Elaine Nunes	Programador	1998-08-15	F	35.90	2.00	Canadá
49	Silvio Ricardo	Programador	2012-03-12	M	65.99	1.23	EUA
50	Denilson Barbosa da Silva	Empreendedor	2000-01-08	M	97.30	2.00	Brasil
51	Jucinei Teixeira	Professor	1977-11-22	F	44.80	1.76	Portugal
52	Bruna Santos	Auxiliar Administrat	1991-12-01	F	76.30	1.45	Canadá
53	André Vitebo	Médico	1970-07-01	M	44.11	1.55	Brasil
54	Andre Santini	Programador	1991-08-15	M	66.00	1.76	Itália
55	Ruan Valente	Programador	1998-03-19	M	101.90	1.76	Canadá
56	Nailton Mauricio	Médico	1992-04-25	M	86.01	1.43	EUA
57	Rita Pontes	Professor	1999-09-02	F	54.10	1.35	Angola
58	Carlos Camargo	Programador	2005-02-22	M	124.65	1.33	Brasil
59	Philppe Oliveira	Auxiliar Administrat	2000-05-23	M	105.10	2.19	Brasil
60	Dayana Dias	Professor	1993-05-30	F	88.30	1.66	Angola
61	Silvana Albuquerque	Programador	1999-05-22	F	56.00	1.50	Brasil
"""



# REGISTROS DA TABELA 'CURSOS'

SELECT * FROM cursos; # Selecionando * (todas as colunas) da tabela 'cursos'. Resultados aparecem em ORDEM PRIMÁRIA.
"""mysql> SELECT * FROM cursos
    -> LIMIT 5;
+---------+------------+------------------------------+-------+----------+------+
| idcurso | nome       | descricao                    | carga | totaulas | ano  |
+---------+------------+------------------------------+-------+----------+------+
|       1 | HTML5      | Curso de HTML5               |    40 |       37 | 2014 |
|       2 | Algoritmos | Lógica de Programação        |    20 |       15 | 2014 |
|       3 | Photoshop5 | Dicas de Photoshop CC        |    10 |        8 | 2014 |
|       4 | PHP        | Curso de PHP para iniciantes |    40 |       20 | 2015 |
|       5 | Java       | Introdução à Linguagem Java  |    40 |       29 | 2015 |
+---------+------------+------------------------------+-------+----------+------+
5 rows in set (0.00 sec)"""

SELECT * FROM cursos
ORDER BY nome; # Ordenar em sentido alfabético [default], mas poderia ser ao reverso usando DESC, ou em ordem DESCentende ou ASCecndente.
"""
mysql> SELECT * FROM cursos
    -> ORDER BY nome
    -> LIMIT 5;
+---------+---------------+------------------------------------------------------+-------+----------+------+
| idcurso | nome          | descricao                                            | carga | totaulas | ano  |
+---------+---------------+------------------------------------------------------+-------+----------+------+
|      23 | After Effects | Curso de Efeitos em Vídeos com After Effects         |    20 |       10 | 2018 |
|       2 | Algoritmos    | Lógica de Programação                                |    20 |       15 | 2014 |
|      14 | Android       | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      13 | C#            | Curso de C#                                          |    30 |       12 | 2017 |
|      12 | C++           | Curso de C++ com Orientação a Objetos                |    40 |       25 | 2017 |
+---------+---------------+------------------------------------------------------+-------+----------+------+
5 rows in set (0.00 sec)
"""

SELECT * FROM cursos
ORDER BY nome ASC; # Método em ordem ASCENDENTE.
"""
mysql> SELECT * FROM cursos
    -> ORDER BY nome ASC
    -> LIMIT 5;
+---------+---------------+------------------------------------------------------+-------+----------+------+
| idcurso | nome          | descricao                                            | carga | totaulas | ano  |
+---------+---------------+------------------------------------------------------+-------+----------+------+
|      23 | After Effects | Curso de Efeitos em Vídeos com After Effects         |    20 |       10 | 2018 |
|       2 | Algoritmos    | Lógica de Programação                                |    20 |       15 | 2014 |
|      14 | Android       | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      13 | C#            | Curso de C#                                          |    30 |       12 | 2017 |
|      12 | C++           | Curso de C++ com Orientação a Objetos                |    40 |       25 | 2017 |
+---------+---------------+------------------------------------------------------+-------+----------+------+
5 rows in set (0.00 sec)
"""

SELECT * FROM cursos
ORDER BY nome DESC;  # Método em ordem DESCENDENTE.
"""
mysql> SELECT * FROM cursos
    -> ORDER BY nome DESC
    -> LIMIT 5;
+---------+-----------+--------------------------------------------------+-------+----------+------+
| idcurso | nome      | descricao                                        | carga | totaulas | ano  |
+---------+-----------+--------------------------------------------------+-------+----------+------+
|      24 | WordPress | Curso de Criação de Sites com WordPress          |    60 |       30 | 2019 |
|       7 | Word      | Curso completo de Word                           |    40 |       30 | 2016 |
|      17 | Swift     | Curso de Desenvolvimento de Aplicativos para iOS |    60 |       30 | 2019 |
|      21 | SEO       | Curso de Otimização de Sites                     |    30 |       12 | 2017 |
|      20 | Segurança | Curso de Segurança                               |    15 |        8 | 2018 |
+---------+-----------+--------------------------------------------------+-------+----------+------+
5 rows in set (0.00 sec)
"""

SELECT nome, carga, ano FROM cursos # Seleciona apenas as COLUNAS nome, carga, ano e ORDENA por NOME asc
ORDER BY nome; 
"""
mysql> SELECT nome, carga, ano FROM cursos
    -> ORDER BY nome
    -> LIMIT 5;
+---------------+-------+------+
| nome          | carga | ano  |
+---------------+-------+------+
| After Effects |    20 | 2018 |
| Algoritmos    |    20 | 2014 |
| Android       |    60 | 2018 |
| C#            |    30 | 2017 |
| C++           |    40 | 2017 |
+---------------+-------+------+
5 rows in set (0.00 sec)
"""

SELECT ano, nome, carga FROM cursos
ORDER BY nome;
"""mysql> SELECT ano, nome, carga FROM cursos
    -> ORDER BY nome
    -> LIMIT 5;
+------+---------------+-------+
| ano  | nome          | carga |
+------+---------------+-------+
| 2018 | After Effects |    20 |
| 2014 | Algoritmos    |    20 |
| 2018 | Android       |    60 |
| 2017 | C#            |    30 |
| 2017 | C++           |    40 |
+------+---------------+-------+
5 rows in set (0.00 sec)"""

SELECT ano, nome, carga FROM cursos
ORDER BY ano;
"""
mysql> SELECT ano, nome, carga FROM cursos
    -> ORDER BY ano
    -> LIMIT 5;
+------+------------+-------+
| ano  | nome       | carga |
+------+------------+-------+
| 2010 | PHP4       |    30 |
| 2010 | HTML4      |    20 |
| 2014 | HTML5      |    40 |
| 2014 | Algoritmos |    20 |
| 2014 | Photoshop5 |    10 |
+------+------------+-------+
5 rows in set (0.00 sec)
"""

SELECT ano, nome, carga FROM cursos
ORDER BY ano, nome;
"""
mysql> SELECT ano, nome, carga FROM cursos
    -> ORDER BY ano, nome
    -> LIMIT 5;
+------+------------+-------+
| ano  | nome       | carga |
+------+------------+-------+
| 2010 | HTML4      |    20 |
| 2010 | PHP4       |    30 |
| 2014 | Algoritmos |    20 |
| 2014 | HTML5      |    40 |
| 2014 | Photoshop5 |    10 |
+------+------------+-------+
5 rows in set (0.00 sec)
"""



# SELECIONANDO LINHAS (usar a cláusula WHERE!)
SELECT * FROM cursos
ORDER BY nome;
"""
mysql> SELECT * FROM cursos
    -> ORDER BY nome
    -> LIMIT 5;
+---------+---------------+------------------------------------------------------+-------+----------+------+
| idcurso | nome          | descricao                                            | carga | totaulas | ano  |
+---------+---------------+------------------------------------------------------+-------+----------+------+
|      23 | After Effects | Curso de Efeitos em Vídeos com After Effects         |    20 |       10 | 2018 |
|       2 | Algoritmos    | Lógica de Programação                                |    20 |       15 | 2014 |
|      14 | Android       | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      13 | C#            | Curso de C#                                          |    30 |       12 | 2017 |
|      12 | C++           | Curso de C++ com Orientação a Objetos                |    40 |       25 | 2017 |
+---------+---------------+------------------------------------------------------+-------+----------+------+
5 rows in set (0.00 sec)
"""

SELECT * FROM cursos
WHERE ano = '2016'
ORDER BY nome;
"""
mysql> SELECT * FROM cursos WHERE ano = '2016' ORDER BY nome;
+---------+-------+------------------------------------------+-------+----------+------+
| idcurso | nome  | descricao                                | carga | totaulas | ano  |
+---------+-------+------------------------------------------+-------+----------+------+
|       6 | MySQL | Bancos de Dados MySQL                    |    30 |       15 | 2016 |
|       9 | POO   | Curso de Programação Orientada a Objetos |    60 |       35 | 2016 |
|      19 | Redes | Curso de Redes para Iniciantes           |    40 |       15 | 2016 |
|       7 | Word  | Curso completo de Word                   |    40 |       30 | 2016 |
+---------+-------+------------------------------------------+-------+----------+------+
4 rows in set (0.00 sec)
"""

SELECT nome, carga FROM cursos
WHERE ano = '2016'
ORDER BY nome;
"""
mysql> SELECT nome, carga FROM cursos WHERE ano = '2016' ORDER BY nome;
+-------+-------+
| nome  | carga |
+-------+-------+
| MySQL |    30 |
| POO   |    60 |
| Redes |    40 |
| Word  |    40 |
+-------+-------+
4 rows in set (0.00 sec)
"""

# 'RESULT SET' é o resultado de uma consulta ('QUERY')! 
# Guardar a palavra 'result set' e 'query'.

SELECT nome, descricao, carga FROM cursos
WHERE ano = '2016'
ORDER BY nome;
"""
mysql> SELECT nome, descricao, carga FROM cursos WHERE ano = '2016' ORDER BY nome;
+-------+------------------------------------------+-------+
| nome  | descricao                                | carga |
+-------+------------------------------------------+-------+
| MySQL | Bancos de Dados MySQL                    |    30 |
| POO   | Curso de Programação Orientada a Objetos |    60 |
| Redes | Curso de Redes para Iniciantes           |    40 |
| Word  | Curso completo de Word                   |    40 |
+-------+------------------------------------------+-------+
4 rows in set (0.00 sec)
"""

# Uma 'QUERY' é uma pergunta, uma solicitação e que podemos usar o WHERE como uma CONDIÇÃO, com uma EXPRESSÃO RELACIONAL (podemos lembrar dos Operadores Relacionais de Algoritmos).
SELECT nome, descricao FROM cursos
WHERE ano <= '2015'
ORDER BY nome;
"""
mysql> SELECT nome, descricao, ano FROM cursos WHERE ano <= '2015' ORDER BY nome;
+------------+----------------------------------+------+
| nome       | descricao                        | ano  |
+------------+----------------------------------+------+
| Algoritmos | Lógica de Programação            | 2014 |
| HTML4      | Curso Básico de HTML, versão 4.0 | 2010 |
| HTML5      | Curso de HTML5                   | 2014 |
| Java       | Introdução à Linguagem Java      | 2015 |
| Photoshop5 | Dicas de Photoshop CC            | 2014 |
| PHP        | Curso de PHP para iniciantes     | 2015 |
| PHP4       | Curso de PHP, versão 4.0         | 2010 |
+------------+----------------------------------+------+
7 rows in set (0.00 sec)
"""

SELECT nome, descricao, ano FROM cursos
WHERE ano <= 2015
ORDER BY ano, nome;
"""
mysql> SELECT nome, descricao, ano FROM cursos WHERE ano <= '2015' ORDER BY ano, nome;
+------------+----------------------------------+------+
| nome       | descricao                        | ano  |
+------------+----------------------------------+------+
| HTML4      | Curso Básico de HTML, versão 4.0 | 2010 |
| PHP4       | Curso de PHP, versão 4.0         | 2010 |
| Algoritmos | Lógica de Programação            | 2014 |
| HTML5      | Curso de HTML5                   | 2014 |
| Photoshop5 | Dicas de Photoshop CC            | 2014 |
| Java       | Introdução à Linguagem Java      | 2015 |
| PHP        | Curso de PHP para iniciantes     | 2015 |
+------------+----------------------------------+------+
7 rows in set (0.00 sec)
"""

#   OPERADORES RELACIONAIS BÁSICOS PODEM SER:
#       < menor que
#       <= menor ou igual a
#       > maior que
#       >= maior ou igual a
#       = igual a
#       != diferente de (not)
#       <> diferente de (not)

# SELECIONANDO INTERVALOS - OPERADOR BETWEEN
SELECT * FROM cursos
WHERE (____________________)
ORDER BY nome;

SELECT * FROM cursos
WHERE totaulas BETWEEN '20' and '30'
ORDER BY nome;
"""
mysql> SELECT * FROM cursos
    -> WHERE totaulas BETWEEN '20' and '30'
    -> ORDER BY nome;
+---------+-----------+------------------------------------------------------+-------+----------+------+
| idcurso | nome      | descricao                                            | carga | totaulas | ano  |
+---------+-----------+------------------------------------------------------+-------+----------+------+
|      14 | Android   | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      12 | C++       | Curso de C++ com Orientação a Objetos                |    40 |       25 | 2017 |
|      10 | Excel     | Curso completo de Excel                              |    40 |       30 | 2017 |
|       5 | Java      | Introdução à Linguagem Java                          |    40 |       29 | 2015 |
|      25 | Joomla    | Curso de Criação de Sites com Joomla                 |    60 |       30 | 2019 |
|      26 | Magento   | Curso de Criação de Lojas Virtuais com Magento       |    50 |       25 | 2019 |
|       4 | PHP       | Curso de PHP para iniciantes                         |    40 |       20 | 2015 |
|      29 | PHP7      | Curso de PHP, versão 7.0                             |    40 |       20 | 2020 |
|      17 | Swift     | Curso de Desenvolvimento de Aplicativos para iOS     |    60 |       30 | 2019 |
|       7 | Word      | Curso completo de Word                               |    40 |       30 | 2016 |
|      24 | WordPress | Curso de Criação de Sites com WordPress              |    60 |       30 | 2019 |
+---------+-----------+------------------------------------------------------+-------+----------+------+
11 rows in set (0.14 sec)
"""

SELECT nome, ano FROM cursos
WHERE ano BETWEEN '2014' AND '2016'
ORDER BY ano DESC, nome ASC;
"""
mysql> SELECT nome, ano FROM cursos WHERE ano BETWEEN '2014' AND '2016' ORDER BY ano DESC, nome ASC;
+------------+------+
| nome       | ano  |
+------------+------+
| MySQL      | 2016 |
| POO        | 2016 |
| Redes      | 2016 |
| Word       | 2016 |
| Java       | 2015 |
| PHP        | 2015 |
| Algoritmos | 2014 |
| HTML5      | 2014 |
| Photoshop5 | 2014 |
+------------+------+
9 rows in set (0.00 sec)
"""

# SELECIONANDO VALORES ESPECÍFICOS (in != between)

SELECT idcurso, nome FROM cursos
WHERE ano IN ('2014', '2016', '2018') # valores específicos que estão contidos na 'lista' (diferente valores e específicos)
ORDER BY nome;
"""
mysql> SELECT idcurso, nome FROM cursos
    -> WHERE ano IN ('2014', '2016', '2018')
    -> ORDER BY nome;
+---------+----------------+
| idcurso | nome           |
+---------+----------------+
|      23 | After Effects  |
|       2 | Algoritmos     |
|      14 | Android        |
|       1 | HTML5          |
|       6 | MySQL          |
|       3 | Photoshop5     |
|       9 | POO            |
|      16 | PowerPoint     |
|      19 | Redes          |
|      11 | Responsividade |
|      20 | Segurança      |
|       7 | Word           |
+---------+----------------+
12 rows in set (0.02 sec)
"""

SELECT nome, descricao, ano FROM cursos
WHERE ano IN (2014, 2016) # o IN seleciona exclusivamente e individualmente os valores 2014 e 2016, diferente do exemplo a seguir com between.
ORDER BY ano;
"""
mysql> SELECT nome, descricao, ano FROM cursos
    -> WHERE ano IN (2014, 2016)
    -> ORDER BY ano;
+------------+------------------------------------------+------+
| nome       | descricao                                | ano  |
+------------+------------------------------------------+------+
| HTML5      | Curso de HTML5                           | 2014 |
| Algoritmos | Lógica de Programação                    | 2014 |
| Photoshop5 | Dicas de Photoshop CC                    | 2014 |
| MySQL      | Bancos de Dados MySQL                    | 2016 |
| Word       | Curso completo de Word                   | 2016 |
| POO        | Curso de Programação Orientada a Objetos | 2016 |
| Redes      | Curso de Redes para Iniciantes           | 2016 |
+------------+------------------------------------------+------+
7 rows in set (0.00 sec)
"""

SELECT nome, descricao, ano FROM cursos
WHERE ano BETWEEN 2014 AND 2016 # o BETWEEN ele seleciona o RANGE entre os valores 2014 e 2016 (de 2014 até 2016, 2015 incluso), diferente do exemplo anterior com IN.
ORDER BY ano;
"""
mysql> SELECT nome, descricao, ano FROM cursos
    -> WHERE ano BETWEEN 2014 AND 2016
    -> ORDER BY ano;
+------------+------------------------------------------+------+
| nome       | descricao                                | ano  |
+------------+------------------------------------------+------+
| HTML5      | Curso de HTML5                           | 2014 |
| Algoritmos | Lógica de Programação                    | 2014 |
| Photoshop5 | Dicas de Photoshop CC                    | 2014 |
| PHP        | Curso de PHP para iniciantes             | 2015 |
| Java       | Introdução à Linguagem Java              | 2015 |
| MySQL      | Bancos de Dados MySQL                    | 2016 |
| Word       | Curso completo de Word                   | 2016 |
| POO        | Curso de Programação Orientada a Objetos | 2016 |
| Redes      | Curso de Redes para Iniciantes           | 2016 |
+------------+------------------------------------------+------+
9 rows in set (0.00 sec)
"""

# Além dos OPERADORES RELACIONAIS (<, <=, >, >=, =, !=, <>, between, in)
# Temos também os OPERADORES LÓGICOS, assim como nos algoritmos, e nós podemos combinar os Operadores Relacionais criando Expressões Lógicas mais potentes.

# COMBINANDO TESTES

SELECT * FROM cursos
WHERE (carga > 35) AND (totaulas < 30)
ORDER BY nome;
"""
mysql> SELECT * FROM cursos
    -> WHERE carga > 35 and totaulas < 30
    -> ORDER BY nome;
+---------+---------+------------------------------------------------+-------+----------+------+
| idcurso | nome    | descricao                                      | carga | totaulas | ano  |
+---------+---------+------------------------------------------------+-------+----------+------+
|      12 | C++     | Curso de C++ com Orientação a Objetos          |    40 |       25 | 2017 |
|       5 | Java    | Introdução à Linguagem Java                    |    40 |       29 | 2015 |
|      26 | Magento | Curso de Criação de Lojas Virtuais com Magento |    50 |       25 | 2019 |
|       4 | PHP     | Curso de PHP para iniciantes                   |    40 |       20 | 2015 |
|      29 | PHP7    | Curso de PHP, versão 7.0                       |    40 |       20 | 2020 |
|       8 | Python  | Curso de Python                                |    40 |       18 | 2017 |
|      19 | Redes   | Curso de Redes para Iniciantes                 |    40 |       15 | 2016 |
+---------+---------+------------------------------------------------+-------+----------+------+
7 rows in set (0.00 sec)
"""

SELECT nome, carga, totaulas FROM cursos
WHERE carga > 35 and totaulas < 30; # O AND é um excludente, então os resultados devem, AO MESMO TEMPO, ter carga > 35 E totaulas < 30.
"""
mysql> SELECT nome, carga, totaulas FROM cursos
    -> WHERE carga > 35 and totaulas < 30;
+---------+-------+----------+
| nome    | carga | totaulas |
+---------+-------+----------+
| PHP     |    40 |       20 |
| Java    |    40 |       29 |
| Python  |    40 |       18 |
| C++     |    40 |       25 |
| Redes   |    40 |       15 |
| Magento |    50 |       25 |
| PHP7    |    40 |       20 |
+---------+-------+----------+
7 rows in set (0.00 sec)
"""

SELECT nome, carga, totaulas FROM cursos
WHERE carga > 35 OR totaulas < 30; # O operador lógico OR (OU) aceita resultados que cumpram carga > 35, OU totaulas < 30, OU ambas. 
"""
mysql> SELECT nome, carga, totaulas FROM cursos
    -> WHERE carga > 35 OR totaulas < 30;
+--------------------+-------+----------+
| nome               | carga | totaulas |
+--------------------+-------+----------+
| HTML5              |    40 |       37 |
| Algoritmos         |    20 |       15 |
| Photoshop5         |    10 |        8 |
| PHP                |    40 |       20 |
| Java               |    40 |       29 |
| MySQL              |    30 |       15 |
| Word               |    40 |       30 |
| Python             |    40 |       18 |
| POO                |    60 |       35 |
| Excel              |    40 |       30 |
| Responsividade     |    30 |       15 |
| C++                |    40 |       25 |
| C#                 |    30 |       12 |
| Android            |    60 |       30 |
| JavaScript         |    35 |       18 |
| PowerPoint         |    30 |       12 |
| Swift              |    60 |       30 |
| Hardware           |    30 |       12 |
| Redes              |    40 |       15 |
| Segurança          |    15 |        8 |
| SEO                |    30 |       12 |
| Premiere           |    20 |       10 |
| After Effects      |    20 |       10 |
| WordPress          |    60 |       30 |
| Joomla             |    60 |       30 |
| Magento            |    50 |       25 |
| Modelagem de Dados |    30 |       12 |
| HTML4              |    20 |        9 |
| PHP7               |    40 |       20 |
| PHP4               |    30 |       11 |
+--------------------+-------+----------+
30 rows in set (0.00 sec)
"""

# Vamos relembrar o quadro da Paula e Quézia, e queremos saber:

# Quero que Paula E Quézia (AND) estejam felizes:
"""
Paula    |    Quézia    |    Estou feliz por elas?
:)                :)                :)    (ambas felizes, oba!)
:)                :/                :/    (apenas uma feliz, que pena)
:/                :)                :/    (apenas uma feliz, que pena)
:/                :/                :/    (ambas tristes, que pena)
"""

# Quero Paula OU Quézia (OR) estejam felizes:
"""
Paula    |    Quézia    |    Estou feliz por elas?
:)                :)                :)    (ambas felizes, oba!)
:)                :/                :)    (ao menos uma feliz, oba!)
:/                :)                :)    (ao menos uma feliz, oba!)
:/                :/                :/    (ambas tristes, que pena)
"""

# Classificação dos Comandos em SQL
# DDL (Data Definition Language):
#       CREATE DATABASE
#       CREATE TABLE
#       ALTER TABLE
#       DROP TABLE

# DML (Data Manipulation Language):
#       INSERT INTO
#       UPDATE
#       DELETE
#       TRUNCATE

# DQL (Data Query Language - linguagem pra perguntas, qüestionamentos, REQUISIÇÕES - Query!):
#       SELECT
# 



"""
Transcrição


Procurar no vídeo
0:03
hum hum
0:19
olá pequeno gafanhoto seja bem-vinda mais uma aula do seu curso em vídeo de banco de dados como sql o meu nome é
0:26
gustavo guanabara eu sou professor e nessa sua aula de banco de dados a gente vai finalmente começar a falar sobre o
0:33
comando mais famoso do sql eu vou te mostrar como obter dados nas tabelas utilizando o comando select e essa é a
0:40
partir dessa aula sem sombra de dúvidas essa é a aula mais esperada é a ela que todo mundo espera porque vai falar do
0:46
comando mais famoso do comando mais utilizado do comando que tem mais parâmetros maior comando da linguagem
0:51
sql que é o comando select você pode estar perguntando por que você está gravando com esse capacete você chegou agora nessa procura pelo
0:58
comando mais famoso chegou a hora de se retardar daqui com capacete basicamente porque nas aulas anteriores
1:04
alguém falou que meu cabelo tá parecendo um capacete eu só resolvi ajudar a piada se você não viu as outras aulas desse
1:09
aqui ó clique aqui você vai direto pra playlist e lá você vai ver o curso desde o início
1:15
essa é uma aula bem mais na frente essa é a décima primeira aula então claro que se você sabe fazer contas e esta é a 11ª
1:22
tem dez aulas pra frente eu te garanto que esse curso é o curso mais legal de mais quero que você encontra em todo
1:28
lugar porque ele te mostra de uma maneira simples e divertida como utilizar o sql se aquela chatice início
1:34
de falar sobre o modelo relacional não estou falando que o modelo relacional é inútil ele é extremamente útil mas eu não falo ele logo no início
1:41
eu deixo mais pra frente porque lá pra frente você vai conseguir entender melhor do que ficar decorando teoria no
1:46
início do curso mas vamos parar de conversa e vamos preparar nossa base de dados para a gente começar a treinar sql
1:52
porque eu preparei um banco especialmente para você então já estamos aqui com o nosso
1:57
ambiente carregado o amp carregado o servidor mais kelly totalmente ativo e
2:02
nós estamos aqui no rock band o que não sabe que nada disso que é o anc workbench meu querido assistir às aulas
2:08
anteriores lá eu ensino como colocar todo o ambiente para funcionar e tudo bonitinho pra você na sua casa você não
2:15
precisa de servidores e de conexão à internet nem nada você vai conseguir utilizar mais que l sem problema nenhum
2:21
e aqui a gente tem a nossa base cadastro foi a base que a gente utilizou até aula de agora o que eu fiz foi gerar um banco
2:27
de dados que está disponível aqui ó lá no curso em vídeo pontocom está disponível uma base de dados gerado em
2:32
forma de anp para você poder importar na sua casa e acompanhar as aulas então meu querido que está esperando
2:38
para se cadastrar lá no curso de banco de dados vai na área de downloads do curso de banco de dados e baixos eu da
2:43
anp para a gente conseguir acompanhar esse daqui o arquivo de da anp eu já coloquei aqui o número de documentos na pasta dantes não tem
2:50
necessidade de estar lá mas eu coloquei então você vai pegar o arquivo dan picos em vídeo que é o arquivo que eu te dei
2:56
nós vamos importar aqui ó envolverem salva de import aquele vai permite
3:04
importar ele vai perguntar se você quer importar de um folder ou de uma self container de fahel
3:10
bota aqui para importar de um arquivo ou clicar na rede essência e vou procurar o
3:15
meu dunk curso em vídeo que foi o arquivo que você fez o download lá vamos abrir não precisa selecionar mais nada
3:22
aqui mandar importar ele vai pedir a senha do usuário do mais que l no meu caso que estou utilizando um
3:29
servidor com o usuário ruth ea senha vazia então é só clicar em ok ele vai fazer a importação e agora eu
3:35
posso atualizar o esquema aqui e parece que nada aconteceu né atualizando ele manteve a base de cadastros acontece que
3:42
cedeu o comando a gente utilizou várias vezes o select asterisco from gafanhotos
3:47
ponto e vírgula voltar contra o enter e você vai ver aqui ó que o cadastro em vários gafanhotos o cadastro pelo menos
3:53
60 isso aí 60 gafanhoto foram cadastrados aqui isso porque agora a gente vai começar a trabalhar com as
3:58
buscas de sql então preciso de uma base de dados mais cheinho é claro que 60 registra pouca coisa mas é bom pra você
4:04
atualizar isso daqui pode ser que quando você baixar o nosso da anp tenha mais registros no momento em que estou gravando essa aula eu só tive paciência
4:11
de fazer 60 se você vê aqui der o comando select 3 from cursos que a outra tabela que a
4:17
gente encontrou em ter você vai ver que eu tenho 30 cursos cadastrados e eu sei que vai começar o desesperar ele
4:23
escreveu ali que vai ter curso de python calma meu querido eu fui ver dando cursos então não começa a viver a
4:29
era que em 2019 vai ter curso de premier não
4:34
calma eu só fiz registros pode ser verdade mas pode ser mentira mas acho
4:40
que é verdade namit demitir mas pode ser verdade a gente nunca sabe me tira
4:52
verdade ou mentira isso daqui vai estar lá na nossa base de dados que você em português você não quer fazer o cadastro
4:59
no curso em vídeo para geral da anp você vai ter que pegar base de dados que a gente criou até aula passada e começar a alimentar de dados
5:04
isso porque a gente vai precisar fazer seleções específicas dos nossos dados
5:09
então vamos partir para os comandos do sr a primeira coisa que vai considerar é que a tabela cursos têm alguns registros
5:16
então eu coloquei aqui que está aparecendo na tela 10 registros são os registos antigos a gente está trabalhando lá no banco de
5:22
dados com 30 registros para cursos mas eu vou representar aqui os dez primeiros registros que foram aqueles que a gente
5:27
trabalhou até aula passada se utilizar o comando eléctrico foram cursos que a
5:32
gente já utilizou várias vezes basicamente traduzindo fica assim selecione asterisco significa todas as
5:39
colunas nunca se esqueça colunas são os campos então selecione todos os campos
5:45
from que a palavra dá não dá didar de oferecer da didá cursos
5:53
então seria selecione todas as colunas da tabela cursos o que ele vai fazer é
5:59
selecionar todos os registros e todas as colunas a gente utilizou esse comando várias vezes então eu só te ensinei esse
6:05
comando até agora porque a gente precisava ver os dados na por exemplo não incluir a observar um selecto para
6:10
ver se realmente ele selecionou quando eu dei um bilhete quando tive que utilizar o select para ver se realmente apagou então esse foi quando a gente utiliza
6:17
até agora não tem novidade nenhuma eu seleciono todos os cursos mas eu consigo começar filtrar olha só
6:23
além de selecionar todas as colunas e todas as linhas eu posso utilizar o comando eléctrico concursos dizendo
6:29
order by nome se você perceber a ordem que ele aparece é a ordem da chave primária não fazer
6:35
uma prática aqui então eu dei aqui select asterisco from cursos
6:40
contra o inter e ele vai te dar lá ele está em ordem não é hora de a fabet que está em ordem
6:46
de de curso que a minha chave primária ele selecionou aqui essa ordem se utilizar o parâmetro order by e colocar
6:55
o nome de uma coluna por exemplo o nome ele vai ordenar o control inter ele vai colocar os cursos seria querer custa
7:02
tudo bagunçado é porque na verdade ele está se mostrando gerado por nome do after effects algoritmo android fechar e
7:09
c++ excel ai meu deus consegui android ai meu deus custos e sharp a 6 são muito chatos mas
7:17
eu gosto a cada um de vocês vai ser chato então quando você dá o odor by nome ele
7:23
vai ordenar de acordo com aquela coluna ao estágio que estava anteriormente ordenada pelo e do curso agora tá
7:29
ordenada pelo nome e nessa ordenação você ainda consegue configurar o sentido você pode adicionar por exemplo no order
7:36
by dólar em baixa e está ordenado por nome beleza se eu colocar a palavra desk e depois
7:42
ele vai fazer a ordenação de baixo pra cima em ordem alfabética inversa na prática que ós evitar o ordenado de
7:48
after effects para baixo se eu colocar a palavra desk contra o inter ele colocou a wordpress o word
7:56
swift s ou segurança ai meu deus curso de swift uso disso ift
8:07
e aí você pode estar se perguntando mas guanabara você ensinou o comando 10 que o comando 10 que é o describe então bota
8:14
aqui ó describe ou simplesmente desk o nome da tabela cursos e ele vai te dar
8:20
descrição calma gafanhoto desk como comando é descreve desk como parâmetro
8:27
do select não é descreve é descendente que é descendente hamas e se eu quiser ascendente é só você não dizer nada ou
8:34
colocar um parâmetro então se no lugar de desk eu colocar a sic que é ascendente ou ascendente contra o inter
8:42
ele vai colocar ascendente então se eu botar a sic ou não votar nada é ascendente se eu botar desk
8:49
eu vou colocar em forma decrescente e não adianta colocar describe aqui porque se 10
8:54
ele descreve esse desk é de descrever e deste clube contra o inter ele descreveu
9:02
aqui se eu gostar desse clube ele vai dar erro porque o comando é desk beleza
9:10
é só isso que o select faz o que tu tá de brincadeira minha cara o select faz muito mais que isso vamos
9:16
começar que todos que a gente viu até agora e select asteriscos elet3 elet6 serviço é sempre asterístico não
9:21
necessariamente asterisco como já disse é selecionar todas as colunas e você pode filtrar as colunas para filtrar as
9:28
colunas eu vou tirar aquele asterisco dali vou manter o mesmo comandam a select tinha um asterisco from cursos order bom
9:34
nome eu tirei o asterisco e eu vou colocar aqui por exemplo nome carga e ano o que
9:40
está fazendo ali é eu não quero selecionar todas as colunas eu quero selecionar somente as colunas nome carga
9:46
e ano então o resultado disso seria a seleção de todos os registros mas ele não vai mostrar todas as colunas ele vai
9:52
mostrar somente as colunas que ficaram verdes e aí vamos ver se funciona então eu vou tirar aqui ó
9:57
vamos lá celeste há seis concursos ele mostrou todas as colunas mas eu quero mostrar no lugar de todas as colunas
10:03
somente nome carga e ano contra o inter
10:09
a ló ele só me mostrou o nome cargo e ano e mostrou todos os cursos isso porque nem todas as vezes que você
10:16
quer fazer uma busca você precisa da base de dados inteira então você quer filtrar para mostrar somente aquelas
10:21
colunas que eu preciso e aí gostou então para filtrar as colunas você tira o asterisco e coloca
10:28
quais são as colunas que você quer que apareça inclusive na hora que você quiser pode até mudar a ordem por exemplo eu quero colocar o ano antes do
10:36
nome então vou daqui ano nome e carga o encontrou em ter
10:41
ele está lá o ano nome é karga feito isso eu consigo até ordenar em múltiplas colunas por exemplo em vez de ordem by
10:48
nome vou botar o líder baiano encontrou em ter perceba aqui ó ele colocou em 2010 eu tenho um curso de
10:55
php html em 2014 html5 de photoshop de algoritmo de php
11:00
ele ordenou pelo ano mas o nome acabou ficando isolado por exemplo em 2010 eu tive o curso de php html
11:07
em 2014 eu tive html5 photoshop e algoritmos basicamente que eu fiz a
11:14
selecionei aqui então em 2014 eu tive esses cursos e se eu quiser colocar
11:19
dentro de 2014 coordenado por nome basta colocar aqui ó primeiro ordena por
11:24
ano vírgula depois ordena por nome vamos dar contra o inter a prestar
11:30
atenção agora em 2014 eu tive os cursos de algoritmo html5 e photoshop bem legal
11:37
isso né o select é muito poderoso você não faz idéia de quanto poderá select tempo tanto que essa é a primeira aula de
11:43
select já está gostando né então a gente aprendeu anteriormente como fio para a coluna você disse que
11:48
não quer aparecer todas as colunas não quero aparecer as colunas específicas você pode estar pensando tá mas filtrar
11:54
a coluna é útil mas filtrar a linha também é bem legal dá pra fazer e vou te mostrar como para
11:59
filtrar linhas então voltei lá o select asterisco foi um curso ordem vai nome selecionaria todos os cursos e ordenava por nome que
12:06
é exatamente isso que está aparecendo na sua tela e se você quiser filtrar as linhas
12:11
você pode colocar a cláusula oher por exemplo lê se command ió selecione todos
12:17
os campos da tabela cursos onde o ano seja igual 2016 ordenado por nome
12:24
vamos fazer funcionar embora vou criar um novo comando aqui ok só para ficar registrado select asterístico from ursos
12:34
o é ano é igual a 2016 eu quero saber
12:39
quais são os cursos que vão ser lançados em 2016 orbán by nome beleza contra o enter
12:48
ele mostrou lá em 2016 segundo esse daqui vai ter o curso
12:53
demais ql de programação orientada a objetos de redes e de word
12:58
ai meu deus curso de redes a meu deus curso de redes quanto direito de 2016
13:06
dai-me paciência você percebe aqui que eu já fico três linhas eu tinha linha
13:12
pra caramba agora eu só tenho quatro linhas mas que lp ó redes word
13:17
você pode filtrar linhas e colunas por exemplo eu quero mostrar somente o nome ea carga separa por vírgula né
13:25
contra o inter ele mostrou só o nome ea carga dos cursos que vão ser lançados em
13:30
2016 e você pode estar pensando para igual na vara mas o campo não estava lá el filtrem 2016 não está aparecendo 2016
13:38
não você pode filtrar pela linha utilizando o é e essa coluna nem fazer parte do seu
13:43
resultado 7 para que eu vou botar coluna ano aqui se eu sei que todos eles são 2016 viu que inteligente select é que eu falo
13:50
uma palavra estranha neves 17 risoto 7 é o resultado de uma consulta então quando
13:55
eu dou select e o resultado é isso que apareceu na tela a gente chama isso tecnicamente the results sete guarda
14:01
essa palavrinha que quando se tiver aprendendo php a palavra o resultado vai aparecer toda hora então você está vendo na tela esses
14:08
eléctricos eléctrico selecionar aquelas duas linhas a linha mais que l word mas eu posso substituir o asterisco por
14:16
colunas separada só vou selecionar aqui ó e eu vou colocar quais são as colunas que eu quero somente nome e descrição e
14:22
carga dos cursos que fazem parte de 2016 então ele vai eliminar as colunas que
14:27
não fazem parte da quarta e já vem mais uma palavra difícil aí com harry na verdade o certo de falar e curi mas
14:34
dependendo do professor fala kerry quer e é triste então o eco harry que é uma pronúncia
14:41
meio errada ou cury dá uma olhada no dicionário pra conferir aqui só o segundo então eu abrir aqui no
14:47
dicionário online de inglês há uma crise entre o plural é que lhes é uma quest
14:56
one ou é ninja e uma pergunta uma solicitação
15:01
vamos pronunciar aqui eu não sei pra mentir é de novo a gente viu de novo por
15:17
exemplo intitulado que eu utilizo direto pessoal chama de insert into
15:23
não vim aqui ó
15:30
encho significa tudo em sairá dentro de alguma coisa
15:35
ó batia ó não é into é beleza então uma
15:48
curva e é uma pergunta uma solicitação ele é se você perceber aqui você acabou
15:53
de utilizar um dever com uma condição com uma expressão relacional e se você é
15:58
um gafanhoto esperto já fez o curso de algoritmo com a gente sabe que existem vários operadores relacionais
16:03
o que tu não fez o curso de algoritmo tá esperando o quê gafanhoto aqui em cima aqui na parte interativa tal curso de
16:10
algoritmos ou aqui embaixo da playlist algoritmo ou no curso em vídeo ponto contar lhe faça algoritmo ensino
16:16
algoritmo pega um jovem e bota pra assistir algoritmo algoritmo é importante para a vida então a gente
16:22
pode utilizar outros operadores relacionais como por exemplo na cláusula o é eu vou selecionar o nome descrição da
16:28
tabela cursos onde o ano seja menor ou igual a 2015 se você perceber aqui ó esses são os
16:35
registros há ó dólar na direita o ano de 2014 2015 2014/2015 lá então
16:41
menor ou igual é menor do que em 2015 ou igual a ele e você percebe eu selecionei
16:47
somente as colunas nome e descrição que é o que eu coloquei lá em cima mesmo a coluna ano não aparecendo vamos
16:53
fazer um teste ao digitar qualquer o nome e descrição da tabela cursos onde
17:00
ano seja menor ou igual a 2015 exatamente o que eu falei lá essa aqui ela é opcional tá eu posso
17:07
colocar aqui 2015 e numérico diretamente ele vai funcionar a 1 contra o enter
17:12
ele selecionou lá somente algoritmos html 4 html5 java photoshop php php
17:18
quatro foram cursos em 2005 ou antes dele eu vou colocar aqui também para
17:24
aparecer o ano só para você poder ver não é obrigatório mas eu posso colocar aqui
17:29
ah mas eu quero que ele fique em ordem de ano beleza não é indiano agora tem ordem de
17:35
ano ah mas eu quero que dentro do ano por exemplo aqui ó em 2014 eu tive esses
17:41
cursos aqui não está em ordem como a gente já viu você pode colocar aqui ó também por nome contra o enter
17:47
está lá agora em 2014 eu tenho os cursos ordenados por ano primeiro e depois por nome
17:55
isso aqui faz toda a diferença a ordem disso faz toda a diferença e você pode utilizar vários operadores
18:01
relacionais aos operadores relacionais básicos são igual diferente menor maior
18:08
maior igual ou menor ou igual a representação de todos eles não vim aqui ó menor que em 2015 vai
18:14
mostrar os cursos menor que em 2015 a 2010 2014 só se eu colocar maior que
18:20
2015 mottaki maior de 2016 todo mundo que vai ser feito em 2017 2018 19 para ela hoje
18:26
17 18 19 2020 falar se eu quiser maior ou igual a 2016
18:33
o 2016 é incluído também lá os cursos de 2016 foram incluídos aqui na lista
18:39
botei maior igual se eu quiser por exemplo menor do que em 2016 a todo
18:44
mundo que foi abaixo dos 16 se eu quiser concluiu de 2016 na lista menor ou igual a agora 2016 está incluído na lista
18:52
o igual a gente já viu todos os cursos de 2006 a tudo aqui é diferente é só
18:57
botar uma exclamação na frente que é ou não não igual o que não é igual é diferente então a tudo que não for 2016 então a
19:04
lista aqui eu não tenho os cursos 2006 ano de 2015 já pulou para 2017
19:10
e se você quiser ter uma outra forma de representar o diferente além de dizer que é algo que não é igual
19:16
você pode colocar diferente assim a menor maior encontrou entrar deu a mesma coisa não adicionou os de 2016 pulou de
19:23
2015 para 2017 mas se você quiser você pode utilizar outros operadores
19:29
além dos operadores relacionados basicamente acabou de número aqui existem outros vamos ver alguns deles o primeiro que a
19:35
gente vai aprender é bem legal por exemplo aqui ó select as três foram cursos não colocou nenhum era ainda o
19:41
dem vai nome beleza está ordenado por nome eu quero selecionar todas as colunas de curso onde o total de aulas
19:47
esteja bituin 20 entre 30 a palavra bituin ela quer dizer em
19:56
entre entre uma coisa e outra como entender aqui eu posso fazer o seguinte olha só select nome e ano
20:04
from cursos o é ano be turim
20:12
então quero ano entre 2014 e 2016
20:19
eu quero saber quais são os cursos foram lançados entre 2014 e 2016 encontrou a inter
20:25
ele mostrou html aqui eu tenho 2014 2015 2016 que a todos eles a 2014 2015 2016
20:33
foram exibidos então todos os cursos com o nome ano onde o ano esteja entre 2014
20:40
e 2016 aqui ficou em ordem de ano por pura coincidência ou não mandou eu renasci eu
20:46
quiser posso mandar denarc ó ordem by ano em nome sendo que o ano eu quero
20:53
descendente ó desk falar o ano foi decrescente e o nome foi
21:00
crescente é legal também o 2014 foi lançado algoritmo html5 e photoshop
21:06
eu botei o 10 que somente na coluna que eu quero decrescente no nome eu quero crescente por exemplo primeiro eu vou
21:13
selecionar ordenando por ano do maior para o menor de 2016 para 2014
21:19
e dentro da organização do ano por exemplo dentro de 2016 que eu tenho esses cursos eu quero ordenar os nomes de forma
21:26
ascendente belezinho além do operador between eu tenho mais alguns vão ver
21:31
mais um aqui então além do b twin eu posso utilizar outro operador que é o operador ryan então a uea ano em 2014 e
21:40
2016 e 2018 qual a diferença entre o yin e obtinha no fim eu vou poder colocar valores
21:46
específicos no âmbito indo eu posso especificar faixas de valores por exemplo aqui eu vou criar um comando
21:52
novo select nome e descrição yano from
21:59
cursos o é ano em 2014 e 2016
22:09
o voltaço 2014/2016 botão horda by ana
22:16
encontrou em ter lá o que ele fez a ele só me mostrou os cursos de 2014 e de
22:23
2016 o passo de que se utilizar o bi turim ele me mostrou os cursos de 2014 e 2015
22:32
e 2016 porque essa é a faixa entre 2014
22:38
e 2016 se utilizar o hino lugar eu só quero mostrar nome descrição e ano
22:45
dos cursos onde o ano esteja dentro desses valores estão 2014 2016
22:52
ele vai te mostrar somente os cursos que foram dados em 2014 e em 2016 por
22:58
exemplo aqui vou colocar 2020 também então eu coloco aqui ó 2014 2016 e os
23:08
cursos que estão planejados em 2020 planejados ou não né deu pra entender a diferença entre o
23:14
between e o im faça seus testes na sua casa que com certeza você vai entender
23:19
acho que a nossa base maior zinha para você conseguir ter mais resultados e se não bastassem todos esses operadores
23:24
relacionados que a gente viu ainda existem operadores lógicos exatamente como nos algoritmos e você pode combinar
23:31
operadores relacionais formando expressões lógicas cada vez mais potentes vamos ver um exemplo aqui então olha só
23:37
fiz um select três concursos e o meu é vai ser o seguinte ó carga maior que 35
23:42
em ti total de aulas menor do que 30 lembra do e doou que a gente viu lá no
23:47
curso de algoritmo não lembra honda relembrada já nós vamos testar esse tipo de coisa aqui tá olha só um comando novo
23:55
aqui select até is from cursos ué carga
24:01
maior que 35 em anti totti aulas menor
24:07
do que 30 então eu quero mostrar todos os cursos que tenham carga acima de 35 e
24:12
o total de aulas menor do que 30 contra o inter olha só que ele gostou vejas turístico
24:18
eu vou mostrar o nome do curso a carga eo de aula só para facilitar sua
24:24
visualização entrou em ter olha só o curso php tem carga de 40 e total de
24:30
aulas de 20 então ele atende a minha condição que é ter carga acima de 35 ele
24:36
tem 40 e ter total de aulas abaixo de 30 que ele tem aqui percebe que nenhum
24:41
curso tem 30 horas aqui se você colocar o menor ou igual e vai começar a aparecer aqui os cursos de 30 horas como
24:48
por exemplo o curso de excel tirar que o menor era tirar o igual e vai voltar
24:54
porque a gente tinha anteriormente e acompanhe aqui comigo a funcionalidade doente ou marcar o que está aqui na sua
25:00
tela todos os cursos que têm carga acima de 35 aló todos os cursos têm carga acima de 35
25:06
você percebe ó que alguns cursos ficaram de fora de 21 de 30 de 10 eu marquei só de vermelho ea carga que têm acima de 35
25:14
vou marcar também agora todos os que têm aula abaixo de 30 olha lá ó todos esses tons de vermelho
25:20
tem um total de água abaixo de 30 percebe que por exemplo o curso de algoritmos tem carga 20 isso não tá
25:26
acima de 35 mas ele tem o total de aulas abaixo de 30 então ele selecionou eo vermelho e
25:31
qual desses registros vai fazer parte se eu utilizei o ente só onde eu tiver dois
25:37
vermelhos na mesma linha acompanhe aqui percebe ó eu tenho no curso de java 2 vermelhinhos no curso e
25:44
html5 tem um só no curso de cozinha árabe tem um só no curso de php eu tenho
25:49
os dois então basicamente que eu tenho eu só tenho dois valores vermelhos na mesma linha em java e em php
25:55
então esses serão os registros que serão selecionados deu para entender ele só vai selecionar
26:00
se tiver um ou outro vamos dar uma olhada no nosso resultado ali então é que o meu comando é tem que
26:06
ter carga acima de 35 e o total de aulas menor que 30 percebe que todos eles têm
26:13
mais de 35 horas de carga e tem menos de 30 aulas beleza e se você se lembra
26:20
muito bem além do ente a gente tem o órgão então vou colocar aqui no lugar de gente ora se você colocar o war dando contra o
26:28
inter ele te mostrou ela só html5 ele tem 40 horas e ele tem 37 aulas e eu
26:34
queria somente o total de aulas abaixo de 30 mas como eu utilizei o war serve um e
26:40
serve outro você se confunde muito com essa coisa de ordem indy na verdade eu tenho uma técnica que eu
26:45
já mostrei aqui várias vezes mas eu vou te mostrar de novo para não ter nenhuma dúvida nesse seu curso de banco de dados
26:50
o uso de operadores lógicos é muito importante basicamente como se usam os operadores lógicos matematicamente existe a regra
26:58
os operadores and o resultado só será verdadeiro se todas as duas premissas
27:03
forem verdadeiros em todos os outros casos o resultado é falso utilizando o operador org bastando que
27:10
uma das premissas seja verdadeira o resultado será verdadeiro o resultado só será falso quando todas as premissas
27:16
forem falsas www seu professor de matemática professor de algoritmos o
27:21
professor de lógica pode ter explicado assim o seu professor que dá aula de capacete vai explicar de uma
27:26
maneira muito mais legal considere o seguinte vou apagar os resultados aqui eu tenho as premissas pq
27:32
vamos esquecer que são premissas pq eu tenho duas amigas a paula ea kezia e que sacou a paula ea
27:40
queda podem ficar felizes ou tristes vamos colocar todas as combinações aqui a paula está feliz ea queda triste
27:47
a paula está triste a queda está feliz e as duas estão tristes agora se pergunta lembrando que entendi é e e oréal
27:54
imagine o seguinte eu quero que a paula ea késia estejam felizes senão não fico
28:01
feliz vamos ver os resultados da primeira linha ali a paulo está feliz ea queda está feliz eu quero que uma é a outra
28:08
estejam felizes então eu fico feliz porque as duas estão na segunda linha só
28:13
paulo está feliz a queda não tá e como eu quero que as duas estejam felizes e eu quero que uma
28:18
esteja feliz ea outra esteja feliz se uma delas está triste eu fico chateado então eu não fico feliz
28:25
no terceiro caso a paula está triste e a queda está feliz como eu quero que as
28:30
duas estejam felizes eu também fico triste no último caso as duas estão chorando e também chorou junto e viram a novela deu
28:38
pra entender vão fazer o mesmo agora pro ou seguindo a mesma premissa mesma
28:43
história a mesma seqüência se está vendo na tela tudo igual na primeira linha utilizando ou a paula está feliz ea
28:49
queda feliz uma ou a outra então fico feliz ou é uma ou outra as duas são felizes vamos
28:55
aproveitar na segunda linha a paula está feliz ea queda também tristinha mas como
29:01
eu sou egoísta e eu falei que serve uma ou serve outra eu fico feliz ao ver que dão a cada pese as habitam de ponto
29:08
serve uma ou serve outra se uma feliz deixa outra em casa chorando no terceiro caso ali a paula triste a
29:14
queda está feliz dane se a paula eu fico feliz também porque serve uma ou a outra se as duas
29:21
tiverem lucro mas só uma tiver a beleza também serve no último caso aliás duas estão tristes
29:27
eu não vou ter com quem passear eu fico triste também deu pra entender acho que é muito mais fácil assim
29:32
agora que eu vou fazer é trocar todas as carinhas felizes por verdadeiro e todas as carinhas tristes por falso fazendo
29:38
isso a gente tem a nossa famosa tabela verdade doente e do ó então no enter
29:44
eu só vou ficar feliz se as duas ficarem felizes e no órgão eu só vou ficar triste se as duas ficarem tristes
29:50
em todos os outros casos você vê o que está acontecendo na tela e aí gostou dessa forma eu acho que essa maneira de
29:57
utilizar os operadores lógicos é muito mais simples de entender eu nunca vou cansar de explicar dessa maneira é feio é
30:04
mas funciona e você aprendeu todo final de aula a gente classifica os comandos que a gente estuda nessa aula a gente só
30:10
viu um até agora que o select gente viu várias cláusulas o from o é o odor
30:15
bairro os operadores maior menor marca igual melhor igual o ibl ine ainda existem outros a gente vai ver
30:21
mais para frente mas vamos classificar o comando select se você se lembra das aulas anteriores a gente classificou já os comandos cliente
30:28
ser hábeis e create table alter table drop table como ddl que são comandos de definição nos classificamos também 17 o
30:35
update de lithium trocate como comando dml de manipulação e agora chegamos ao
30:41
comando select vamos classificá lo aqui e o select é um caso raro o select em
30:46
alguns autores eles classificam como uma coisa em alguns autores que classificam como outro em alguns livros você vai ver
30:52
essa classificação o select é um comando de dml isso é um comando de manipulação de
30:58
dados vários livros fazem isso então a classificação do select seria como dml alguns outros
31:03
atores fazem uma classificação diferente o que coloca como ddl não para alguns
31:09
autores o select inaugura uma outra classificação que é a de que elle que é
31:15
o day é o elenco tite basicamente o select faria parte de uma classificação diferente que seria uma
31:22
linguagem para perguntas uma linguagem para questionamentos então dependendo do livro você tem uma
31:27
classificação diferente eu particularmente gosto mais da classificação ddl porque o select ele
31:33
não manipula os dados ele simplesmente seleciona eles a manipulação dos dados seria uma inclusão de um novo dado uma
31:40
alteração da existente ou até mesmo apagar um dado que já existe e não vai existir mais select não faz manipulação
31:46
de dados o select faz seleção de dados então para a seleção de dados a
31:51
classificação de keele pra mim é mais clara mas você é totalmente livre para escolher qual delas você vai utilizar
31:58
e aí gostou dessa sua primeira aula de select na próxima aula a gente vai ver mais parte do select que vai se
32:03
aprofundar ainda mais nesse comando que é tão poderoso espero que você tenha gostado dessa aula comigo de capacete não vai rolar de novo
32:10
quer lançar todo suado cá todo suado eu queria pedir aquele jovem é
32:16
caprichado queria pedir para você compartilhar as suas redes sociais e nunca se esqueça que a mãe de jesus
32:23
clicando aqui você vai se inscrever no canal para dar essa moral pra gente me dá essa honra de ter você como aluno
32:28
inscrito são mais de 120 mil alunos no momento em que eu tô gravando esse vídeo com certeza no momento que está assistindo é
32:34
muito mais porque todo mundo escuta depois de se inscrever clica na engrenagem vizinha que tem do lado dos inscreva depois de se inscrever e bota
32:41
lá quero receber um e mail na verdade não sou eu que vou te mandar um e mail muito menos eu vou ter o seu email é a plataforma do google e disse
32:48
já tem cerveja faz tempo se preocupar com isso eles vão te mandar um e-mail sempre que a gente lançar uma vídeo-aula
32:53
nova então a gente tem vários cursos que estão em andamento aqui com certeza tem uma coisa boa pra você tem muitos outros
32:59
cursos que vão se interessar clicando aqui você vai ver a playlist todas as aulas deve seguir uma aula de
33:05
select agora você não viu as outras aulas dessa moral também não tem nada pra fazer agora não vai ficar vendo
33:11
outros vídeos né vai manter no curso em vídeo e tá aqui ó todos os vídeos aquino interativo
33:16
sozinho dizem que tem aqui em cima você vai ver outros cursos que a gente faz então além da playfish de banco de dados contém
33:22
outras playlists aqui em cima de vez em quando eu coloco alguns questionamentos aqui em cima para saber se você gostou não dá algumas
33:29
perguntas que a gente pode fazer às vezes eu coloco aqui em cima também dá uma olhada e participa das nossas enquetes e nunca se esqueça aqui no meio
33:36
a experiência completa esta base de dados aqui que você não achou você tem que baixar diretamente do curso vídeo pontocom e lá você vai ter todos
33:42
os materiais inclusive os slides da aula se você é professor de utilizar o slide fica à vontade contanto que você
33:48
mantenha todos os direitos reservados o curso em vídeo que será um trabalho pra caramba crea então é isso porque é
33:54
um gafanhoto pratique sempre utilizo ambiente brinca bastante com o select dessa aula até a próxima porque na
34:00
próxima a gente vai se aprofundar ainda mais e não adianta você se aprofundar se você não sai não adianta você mergulha fundo se você não sabe nem
34:07
goiás concorda comigo então pratique sempre um forte abraço e até a próxima
34:14
meu deus maldita ideia que eu tive de filmar essa parada
"""

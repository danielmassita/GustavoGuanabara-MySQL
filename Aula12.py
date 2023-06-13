# Curso MySQL #12 - SELECT (Parte 2)
# https://youtu.be/q4hPo83-Buo
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/select-parte-2/

"""
OBTENDO DADOS DAS TABELAS - Parte 2
- Vamos dar continuidade aos estudos do comando SELECT, mais famosos, mais utilizado e com mais PARÂMETROS! 
- Muito embora, seja um comando que também receba mudanças em novas versões de SQL (o que requer uma pesquisa na documentação de acordo com a versão).
- São conhecidas como as SINTAXES MÚLTIPLAS (são escritas de maneiras diferentes no MySQL, MariaDB, Postgree, Oracle, etc.)
"""

# SELEÇÃO POR NOME
SELECT * FROM cursos
WHERE nome = 'PHP'; # todos os valores (dados), vamos usar sempre aspas simples ' ', mas por padrão de documentação os campos vêm entre crases ` `, é normal.
"""
mysql> SELECT * FROM cursos
    -> WHERE nome = 'PHP';
+---------+------+------------------------------+-------+----------+------+
| idcurso | nome | descricao                    | carga | totaulas | ano  |
+---------+------+------------------------------+-------+----------+------+
|       4 | PHP  | Curso de PHP para iniciantes |    40 |       20 | 2015 |
+---------+------+------------------------------+-------+----------+------+
1 row in set (0.00 sec)
"""

# Teremos uma única Linha (ou Registro, ou Tupla)

# USANDO UM OPERADOR ESPECIAL - LIKE (semelhante a...)
SELECT * FROM cursos
WHERE nome LIKE 'P%'; # O % serve como 'wild card', ou seja, uma carta coringa pra substituir alguma coisa... 
# O LIKE é um operador case sensitive (aceita ambos upper and lower case).
# O % substitui 'nenhum' ou 'vários' caracteres.
# Em resumo, o comando será: SELECIONE todos(*) os campos A PARTIR DA tabela cursos ONDE nome contém algo PARECIDO com 'P%' seguido de qualquer coisa, inclusive nada.
# Podemos brincar com a posição dos caracteres coringas.
"""
mysql> SELECT * FROM cursos
    -> WHERE nome LIKE 'P%'; 
+---------+------------+------------------------------------------+-------+----------+------+
| idcurso | nome       | descricao                                | carga | totaulas | ano  |
+---------+------------+------------------------------------------+-------+----------+------+
|       3 | Photoshop5 | Dicas de Photoshop CC                    |    10 |        8 | 2014 |
|       4 | PHP        | Curso de PHP para iniciantes             |    40 |       20 | 2015 |
|      30 | PHP4       | Curso de PHP, versão 4.0                 |    30 |       11 | 2010 |
|      29 | PHP7       | Curso de PHP, versão 7.0                 |    40 |       20 | 2020 |
|       9 | POO        | Curso de Programação Orientada a Objetos |    60 |       35 | 2016 |
|      16 | PowerPoint | Curso completo de PowerPoint             |    30 |       12 | 2018 |
|      22 | Premiere   | Curso de Edição de Vídeos com Premiere   |    20 |       10 | 2017 |
|       8 | Python     | Curso de Python                          |    40 |       18 | 2017 |
+---------+------------+------------------------------------------+-------+----------+------+
8 rows in set (0.03 sec)
"""

SELECT * FROM cursos
WHERE nome LIKE 'a%'; # A requisição vai retornar todos os cursos que começam com a letra 'a'
"""
mysql> SELECT * FROM cursos WHERE nome LIKE 'a%';
+---------+---------------+------------------------------------------------------+-------+----------+------+
| idcurso | nome          | descricao                                            | carga | totaulas | ano  |
+---------+---------------+------------------------------------------------------+-------+----------+------+
|      23 | After Effects | Curso de Efeitos em Vídeos com After Effects         |    20 |       10 | 2018 |
|       2 | Algoritmos    | Lógica de Programação                                |    20 |       15 | 2014 |
|      14 | Android       | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
+---------+---------------+------------------------------------------------------+-------+----------+------+
3 rows in set (0.00 sec)
"""

SELECT * FROM cursos
WHERE nome LIKE '%a';
"""
mysql> SELECT * FROM cursos
    -> WHERE nome LIKE '%a';
+---------+-----------+--------------------------------------+-------+----------+------+
| idcurso | nome      | descricao                            | carga | totaulas | ano  |
+---------+-----------+--------------------------------------+-------+----------+------+
|       5 | Java      | Introdução à Linguagem Java          |    40 |       29 | 2015 |
|      20 | Segurança | Curso de Segurança                   |    15 |        8 | 2018 |
|      25 | Joomla    | Curso de Criação de Sites com Joomla |    60 |       30 | 2019 |
+---------+-----------+--------------------------------------+-------+----------+------+
3 rows in set (0.01 sec)
"""

SELECT * FROM cursos # Selecionar todos os registros onde o 'nome' seja parecido com algo que:
WHERE nome LIKE '%a%'; # Contenha a letra A antes, no meio, ou no final do registro, pois o % pode substituir qualquer valor OU nenhum valor 
# %A% inclusi %Algoritmos, sem nada antes, e também inclui SegurançA%, sem nada depois, e também inclui %Java% pois tem A no final e no meio também.
# Inclusive a pontuação do A será aceita, acento agudo, grave ou afim.
"""
mysql> SELECT * FROM cursos
    -> WHERE nome LIKE '%a%';
+---------+--------------------+------------------------------------------------------+-------+----------+------+
| idcurso | nome               | descricao                                            | carga | totaulas | ano  |
+---------+--------------------+------------------------------------------------------+-------+----------+------+
|       2 | Algoritmos         | Lógica de Programação                                |    20 |       15 | 2014 |
|       5 | Java               | Introdução à Linguagem Java                          |    40 |       29 | 2015 |
|      11 | Responsividade     | Curso de Responsividade                              |    30 |       15 | 2018 |
|      14 | Android            | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      15 | JavaScript         | Curso de JavaScript                                  |    35 |       18 | 2017 |
|      18 | Hardware           | Curso de Montagem e Manutenção de PCs                |    30 |       12 | 2017 |
|      20 | Segurança          | Curso de Segurança                                   |    15 |        8 | 2018 |
|      23 | After Effects      | Curso de Efeitos em Vídeos com After Effects         |    20 |       10 | 2018 |
|      25 | Joomla             | Curso de Criação de Sites com Joomla                 |    60 |       30 | 2019 |
|      26 | Magento            | Curso de Criação de Lojas Virtuais com Magento       |    50 |       25 | 2019 |
|      27 | Modelagem de Dados | Curso de Modelagem de Dados                          |    30 |       12 | 2020 |
+---------+--------------------+------------------------------------------------------+-------+----------+------+
11 rows in set (0.00 sec)
"""

SELECT * FROM cursos
WHERE nome NOT LIKE '%a%'; # Todos as linhas que não possuem uma letra 'a' em lugar algum...
"""
mysql> SELECT * FROM cursos
    -> WHERE nome NOT LIKE '%a%';
+---------+------------+--------------------------------------------------+-------+----------+------+
| idcurso | nome       | descricao                                        | carga | totaulas | ano  |
+---------+------------+--------------------------------------------------+-------+----------+------+
|       1 | HTML5      | Curso de HTML5                                   |    40 |       37 | 2014 |
|       3 | Photoshop5 | Dicas de Photoshop CC                            |    10 |        8 | 2014 |
|       4 | PHP        | Curso de PHP para iniciantes                     |    40 |       20 | 2015 |
|       6 | MySQL      | Bancos de Dados MySQL                            |    30 |       15 | 2016 |
|       7 | Word       | Curso completo de Word                           |    40 |       30 | 2016 |
|       8 | Python     | Curso de Python                                  |    40 |       18 | 2017 |
|       9 | POO        | Curso de Programação Orientada a Objetos         |    60 |       35 | 2016 |
|      10 | Excel      | Curso completo de Excel                          |    40 |       30 | 2017 |
|      12 | C++        | Curso de C++ com Orientação a Objetos            |    40 |       25 | 2017 |
|      13 | C#         | Curso de C#                                      |    30 |       12 | 2017 |
|      16 | PowerPoint | Curso completo de PowerPoint                     |    30 |       12 | 2018 |
|      17 | Swift      | Curso de Desenvolvimento de Aplicativos para iOS |    60 |       30 | 2019 |
|      19 | Redes      | Curso de Redes para Iniciantes                   |    40 |       15 | 2016 |
|      21 | SEO        | Curso de Otimização de Sites                     |    30 |       12 | 2017 |
|      22 | Premiere   | Curso de Edição de Vídeos com Premiere           |    20 |       10 | 2017 |
|      24 | WordPress  | Curso de Criação de Sites com WordPress          |    60 |       30 | 2019 |
|      28 | HTML4      | Curso Básico de HTML, versão 4.0                 |    20 |        9 | 2010 |
|      29 | PHP7       | Curso de PHP, versão 7.0                         |    40 |       20 | 2020 |
|      30 | PHP4       | Curso de PHP, versão 4.0                         |    30 |       11 | 2010 |
+---------+------------+--------------------------------------------------+-------+----------+------+
19 rows in set (0.00 sec)
"""

UPDATE cursos SET nome = 'PáOO'
WHERE idcurso = '9';
"""
mysql> UPDATE cursos
    -> SET nome = 'PáOO'
    -> WHERE idcurso = '9';
Query OK, 1 row affected (0.09 sec)
Rows matched: 1  Changed: 1  Warnings: 0
"""

SELECT * FROM cursos
WHERE nome NOT LIKE '%A%'; # O curso de 'POO' não aparece pois agora em seu registro EXISTE o caracteer 'a' no meio de 'PáOO'.
"""
mysql> SELECT * FROM cursos
    -> WHERE nome NOT LIKE '%a%';
+---------+------------+--------------------------------------------------+-------+----------+------+
| idcurso | nome       | descricao                                        | carga | totaulas | ano  |
+---------+------------+--------------------------------------------------+-------+----------+------+
|       1 | HTML5      | Curso de HTML5                                   |    40 |       37 | 2014 |
|       3 | Photoshop5 | Dicas de Photoshop CC                            |    10 |        8 | 2014 |
|       4 | PHP        | Curso de PHP para iniciantes                     |    40 |       20 | 2015 |
|       6 | MySQL      | Bancos de Dados MySQL                            |    30 |       15 | 2016 |
|       7 | Word       | Curso completo de Word                           |    40 |       30 | 2016 |
|       8 | Python     | Curso de Python                                  |    40 |       18 | 2017 |
|      10 | Excel      | Curso completo de Excel                          |    40 |       30 | 2017 |
|      12 | C++        | Curso de C++ com Orientação a Objetos            |    40 |       25 | 2017 |
|      13 | C#         | Curso de C#                                      |    30 |       12 | 2017 |
|      16 | PowerPoint | Curso completo de PowerPoint                     |    30 |       12 | 2018 |
|      17 | Swift      | Curso de Desenvolvimento de Aplicativos para iOS |    60 |       30 | 2019 |
|      19 | Redes      | Curso de Redes para Iniciantes                   |    40 |       15 | 2016 |
|      21 | SEO        | Curso de Otimização de Sites                     |    30 |       12 | 2017 |
|      22 | Premiere   | Curso de Edição de Vídeos com Premiere           |    20 |       10 | 2017 |
|      24 | WordPress  | Curso de Criação de Sites com WordPress          |    60 |       30 | 2019 |
|      28 | HTML4      | Curso Básico de HTML, versão 4.0                 |    20 |        9 | 2010 |
|      29 | PHP7       | Curso de PHP, versão 7.0                         |    40 |       20 | 2020 |
|      30 | PHP4       | Curso de PHP, versão 4.0                         |    30 |       11 | 2010 |
+---------+------------+--------------------------------------------------+-------+----------+------+
18 rows in set (0.00 sec)
"""

SELECT * FROM cursos
WHERE nome LIKE '%A';
"""
mysql> SELECT * FROM cursos
    -> WHERE nome LIKE '%a%';
+---------+--------------------+------------------------------------------------------+-------+----------+------+
| idcurso | nome               | descricao                                            | carga | totaulas | ano  |
+---------+--------------------+------------------------------------------------------+-------+----------+------+
|       2 | Algoritmos         | Lógica de Programação                                |    20 |       15 | 2014 |
|       5 | Java               | Introdução à Linguagem Java                          |    40 |       29 | 2015 |
|       9 | PáOO               | Curso de Programação Orientada a Objetos             |    60 |       35 | 2016 |
|      11 | Responsividade     | Curso de Responsividade                              |    30 |       15 | 2018 |
|      14 | Android            | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      15 | JavaScript         | Curso de JavaScript                                  |    35 |       18 | 2017 |
|      18 | Hardware           | Curso de Montagem e Manutenção de PCs                |    30 |       12 | 2017 |
|      20 | Segurança          | Curso de Segurança                                   |    15 |        8 | 2018 |
|      23 | After Effects      | Curso de Efeitos em Vídeos com After Effects         |    20 |       10 | 2018 |
|      25 | Joomla             | Curso de Criação de Sites com Joomla                 |    60 |       30 | 2019 |
|      26 | Magento            | Curso de Criação de Lojas Virtuais com Magento       |    50 |       25 | 2019 |
|      27 | Modelagem de Dados | Curso de Modelagem de Dados                          |    30 |       12 | 2020 |
+---------+--------------------+------------------------------------------------------+-------+----------+------+
12 rows in set (0.00 sec)
"""

# Vamos alterar o comando no proprio MySQL, no registro da linha 9, podemos dar duplo clique e alterar, depois APPLY, e veremos o código SQL gerado, com a alteração.
UPDATE `cadastro`.`cursos` SET `nome` = 'POO' WHERE (`idcurso` = '9');

SELECT * FROM cursos
WHERE nome LIKE 'PH%P'; # PHP e Photoshop retornariam como resultado, mas no BD o valor está como Photoshop5, então esse 5 no final impede o resultado de ambos.
"""
mysql> SELECT * FROM cursos
    -> WHERE nome LIKE 'ph%p';
+---------+------+------------------------------+-------+----------+------+
| idcurso | nome | descricao                    | carga | totaulas | ano  |
+---------+------+------------------------------+-------+----------+------+
|       4 | PHP  | Curso de PHP para iniciantes |    40 |       20 | 2015 |
+---------+------+------------------------------+-------+----------+------+
1 row in set (0.00 sec)
"""

SELECT * FROM cursos
WHERE nome LIKE 'ph%p%'; # Agora, tanto o PHP quanto PHotoshoP5, PHP4, PHP7 vão aparecer... 
"""
mysql> SELECT * FROM cursos
    -> WHERE nome LIKE 'ph%p%';
+---------+------------+------------------------------+-------+----------+------+
| idcurso | nome       | descricao                    | carga | totaulas | ano  |
+---------+------------+------------------------------+-------+----------+------+
|       3 | Photoshop5 | Dicas de Photoshop CC        |    10 |        8 | 2014 |
|       4 | PHP        | Curso de PHP para iniciantes |    40 |       20 | 2015 |
|      30 | PHP4       | Curso de PHP, versão 4.0     |    30 |       11 | 2010 |
|      29 | PHP7       | Curso de PHP, versão 7.0     |    40 |       20 | 2020 |
+---------+------------+------------------------------+-------+----------+------+
4 rows in set (0.00 sec)
"""

SELECT * FROM cursos
WHERE nome LIKE 'ph%p_'; # Ou seja, é preciso começar com PH, e no final terminar com P_, onde _ é ALGUM valor que seja válido, não vazio/final.
"""
mysql> SELECT * FROM cursos
    -> WHERE nome LIKE 'ph%p_';
+---------+------------+--------------------------+-------+----------+------+
| idcurso | nome       | descricao                | carga | totaulas | ano  |
+---------+------------+--------------------------+-------+----------+------+
|       3 | Photoshop5 | Dicas de Photoshop CC    |    10 |        8 | 2014 |
|      30 | PHP4       | Curso de PHP, versão 4.0 |    30 |       11 | 2010 |
|      29 | PHP7       | Curso de PHP, versão 7.0 |    40 |       20 | 2020 |
+---------+------------+--------------------------+-------+----------+------+
3 rows in set (0.00 sec)
"""

SELECT * FROM cursos
WHERE nome LIKE 'P%';
"""
mysql> SELECT * FROM cursos
    -> WHERE nome LIKE 'P%';
+---------+------------+------------------------------------------+-------+----------+------+
| idcurso | nome       | descricao                                | carga | totaulas | ano  |
+---------+------------+------------------------------------------+-------+----------+------+
|       3 | Photoshop5 | Dicas de Photoshop CC                    |    10 |        8 | 2014 |
|       4 | PHP        | Curso de PHP para iniciantes             |    40 |       20 | 2015 |
|      30 | PHP4       | Curso de PHP, versão 4.0                 |    30 |       11 | 2010 |
|      29 | PHP7       | Curso de PHP, versão 7.0                 |    40 |       20 | 2020 |
|       9 | POO        | Curso de Programação Orientada a Objetos |    60 |       35 | 2016 |
|      16 | PowerPoint | Curso completo de PowerPoint             |    30 |       12 | 2018 |
|      22 | Premiere   | Curso de Edição de Vídeos com Premiere   |    20 |       10 | 2017 |
|       8 | Python     | Curso de Python                          |    40 |       18 | 2017 |
+---------+------------+------------------------------------------+-------+----------+------+
8 rows in set (0.00 sec)
"""

SELECT * FROM cursos
WHERE nome LIKE 'p_p%';
"""
mysql> SELECT * FROM cursos
    -> WHERE nome LIKE 'p_p%';
+---------+------+------------------------------+-------+----------+------+
| idcurso | nome | descricao                    | carga | totaulas | ano  |
+---------+------+------------------------------+-------+----------+------+
|       4 | PHP  | Curso de PHP para iniciantes |    40 |       20 | 2015 |
|      30 | PHP4 | Curso de PHP, versão 4.0     |    30 |       11 | 2010 |
|      29 | PHP7 | Curso de PHP, versão 7.0     |    40 |       20 | 2020 |
+---------+------+------------------------------+-------+----------+------+
3 rows in set (0.00 sec)
"""

SELECT * FROM cursos
WHERE nome LIKE 'p__t%';
"""
mysql> SELECT * FROM cursos
    -> WHERE nome LIKE 'p__t%';
+---------+------------+-----------------------+-------+----------+------+
| idcurso | nome       | descricao             | carga | totaulas | ano  |
+---------+------------+-----------------------+-------+----------+------+
|       3 | Photoshop5 | Dicas de Photoshop CC |    10 |        8 | 2014 |
+---------+------------+-----------------------+-------+----------+------+
1 row in set (0.00 sec)
"""

SELECT * FROM gafanhotos
WHERE nome LIKE '%silva%';
"""
mysql> SELECT * FROM gafanhotos
    -> WHERE nome LIKE '%silva%';
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
| id | nome                      | profissao            | nascimento | sexo | peso  | altura | nacionalidade |
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
| 13 | Allan Silva               | Programador          | 1993-11-11 | M    | 76.99 |   1.55 | Brasil        |
| 28 | Herisson Silva            | Auxiliar Administrat | 1965-10-10 | M    | 74.65 |   1.56 | EUA           |
| 50 | Denilson Barbosa da Silva | Empreendedor         | 2000-01-08 | M    | 97.30 |   2.00 | Brasil        |
| 61 | Silvana Albuquerque       | Programador          | 1999-05-22 | F    | 56.00 |   1.50 | Brasil        |
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
4 rows in set (0.00 sec)
"""

UPDATE `cadastro`.`gafanhotos` SET `id` = '', `nome` = '', `profissao` = '', `nascimento` = '', `sexo` = '', `peso` = '', `altura` = '', `nacionalidade` = '' WHERE (`id` = '61');
DELETE FROM `cadastro`.`gafanhotos` WHERE (`id` = '61');

SELECT * FROM gafanhotos
WHERE nome LIKE '%silva%';
"""
mysql> SELECT * FROM gafanhotos
    -> WHERE nome LIKE '%silva%';
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
| id | nome                      | profissao            | nascimento | sexo | peso  | altura | nacionalidade |
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
| 13 | Allan Silva               | Programador          | 1993-11-11 | M    | 76.99 |   1.55 | Brasil        |
| 28 | Herisson Silva            | Auxiliar Administrat | 1965-10-10 | M    | 74.65 |   1.56 | EUA           |
| 50 | Denilson Barbosa da Silva | Empreendedor         | 2000-01-08 | M    | 97.30 |   2.00 | Brasil        |
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
3 rows in set (0.00 sec)
"""

INSERT INTO `cadastro`.`gafanhotos` (`id`, `nome`, `profissao`, `nascimento`, `sexo`, `peso`, `altura`, `nacionalidade`) VALUES ('61', 'Silvana Albuquerque', 'Programador', '1999-05-22', 'F', '56', '1.5', 'Brasil');
SELECT * FROM gafanhotos
WHERE nome LIKE '%silva%';
"""
mysql> SELECT * FROM gafanhotos
    -> WHERE nome LIKE '%silva%';
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
| id | nome                      | profissao            | nascimento | sexo | peso  | altura | nacionalidade |
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
| 13 | Allan Silva               | Programador          | 1993-11-11 | M    | 76.99 |   1.55 | Brasil        |
| 28 | Herisson Silva            | Auxiliar Administrat | 1965-10-10 | M    | 74.65 |   1.56 | EUA           |
| 50 | Denilson Barbosa da Silva | Empreendedor         | 2000-01-08 | M    | 97.30 |   2.00 | Brasil        |
| 61 | Silvana Albuquerque       | Programador          | 1999-05-22 | F    | 56.00 |   1.50 | Brasil        |
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
4 rows in set (0.00 sec)
"""

SELECT * FROM gafanhotos
WHERE nome LIKE '%_silva'; # Silva é o último sobrenome, necessário ter algum caractere antes _ iclusive espaço, mas Silvana não aparece.
"""
mysql> SELECT * FROM gafanhotos
    -> WHERE nome LIKE '%_silva';
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
| id | nome                      | profissao            | nascimento | sexo | peso  | altura | nacionalidade |
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
| 13 | Allan Silva               | Programador          | 1993-11-11 | M    | 76.99 |   1.55 | Brasil        |
| 28 | Herisson Silva            | Auxiliar Administrat | 1965-10-10 | M    | 74.65 |   1.56 | EUA           |
| 50 | Denilson Barbosa da Silva | Empreendedor         | 2000-01-08 | M    | 97.30 |   2.00 | Brasil        |
+----+---------------------------+----------------------+------------+------+-------+--------+---------------+
3 rows in set (0.00 sec)
"""

SELECT * FROM gafanhotos
WHERE nome LIKE 'silva%';
"""
mysql> SELECT * FROM gafanhotos
    -> WHERE nome LIKE 'silva%';
+----+---------------------+-------------+------------+------+-------+--------+---------------+
| id | nome                | profissao   | nascimento | sexo | peso  | altura | nacionalidade |
+----+---------------------+-------------+------------+------+-------+--------+---------------+
| 61 | Silvana Albuquerque | Programador | 1999-05-22 | F    | 56.00 |   1.50 | Brasil        |
+----+---------------------+-------------+------------+------+-------+--------+---------------+
1 row in set (0.00 sec)
"""


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



# DISTINGUINDO 
# Se você analisar, vamos procurar por 'carga' vários cursos com 40 horas... 
# O DISTINCT vai pegar todos os registros iguais, e mostrar apenas uma vez. O valor 40, mesmo com várias ocorrências, só será exibido uma vez.
# E assim para todos os registros. O DISTINCT vai exibir 'um de cada' pra os valores/registros existentes.

SELECT DISTINCT carga FROM cursos;
"""mysql> SELECT DISTINCT carga FROM cursos;
+-------+
| carga |
+-------+
|    40 |
|    20 |
|    10 |
|    30 |
|    60 |
|    35 |
|    15 |
|    50 |
+-------+
8 rows in set (0.01 sec)"""


SELECT nacionalidade FROM gafanhotos;
"""mysql> SELECT nacionalidade FROM gafanhotos;
+---------------+
| nacionalidade |
+---------------+
| Brasil        |
| Portugal      |
| Moçambique    |
| Irlanda       |
| Brasil        |
| Brasil        |
| EUA           |
| Brasil        |
| Portugal      |
| EUA           |
| Irlanda       |
| Brasil        |
| Brasil        |
| Brasil        |
| Portugal      |
| EUA           |
| Brasil        |
| França        |
| Brasil        |
| Portugal      |
| Brasil        |
| Moçambique    |
| Brasil        |
| Japão         |
| Brasil        |
| Portugal      |
| Brasil        |
| EUA           |
| Brasil        |
| Irlanda       |
| Brasil        |
| Brasil        |
| Brasil        |
| Canadá        |
| EUA           |
| Brasil        |
| Brasil        |
| Portugal      |
| Brasil        |
| Angola        |
| Moçambique    |
| Brasil        |
| EUA           |
| Portugal      |
| Brasil        |
| Angola        |
| Alemanha      |
| Canadá        |
| EUA           |
| Brasil        |
| Portugal      |
| Canadá        |
| Brasil        |
| Itália        |
| Canadá        |
| EUA           |
| Angola        |
| Brasil        |
| Brasil        |
| Angola        |
| Brasil        |
+---------------+
61 rows in set (0.00 sec)"""


SELECT DISTINCT nacionalidade FROM gafanhotos;
"""mysql> SELECT DISTINCT nacionalidade FROM gafanhotos;
+---------------+
| nacionalidade |
+---------------+
| Brasil        |
| Portugal      |
| Moçambique    |
| Irlanda       |
| EUA           |
| França        |
| Japão         |
| Canadá        |
| Angola        |
| Alemanha      |
| Itália        |
+---------------+
11 rows in set (0.00 sec)"""


SELECT DISTINCT nacionalidade FROM gafanhotos
ORDER BY nacionalidade ASC;
"""mysql> SELECT DISTINCT nacionalidade FROM gafanhotos
    -> ORDER BY nacionalidade ASC;
+---------------+
| nacionalidade |
+---------------+
| Alemanha      |
| Angola        |
| Brasil        |
| Canadá        |
| EUA           |
| França        |
| Irlanda       |
| Itália        |
| Japão         |
| Moçambique    |
| Portugal      |
+---------------+
11 rows in set (0.02 sec)"""


SELECT carga FROM cursos
ORDER BY carga ASC;
"""mysql> SELECT DISTINCT carga FROM cursos
    -> ORDER BY carga ASC;
+-------+
| carga |
+-------+
|    10 |
|    15 |
|    20 |
|    30 |
|    35 |
|    40 |
|    50 |
|    60 |
+-------+
8 rows in set (0.00 sec)"""


# FUNÇÕES DE AGREGAÇÃO 
# Assim como Operadores Relacionais, FUNÇÕES de agregação são amplamente utilizadas, pra poder TOTALIZAR alguma coisa.


SELECT COUNT(nome) FROM cursos;

"""mysql> SELECT COUNT(nome) FROM cursos;
+-------------+
| COUNT(nome) |
+-------------+
|          30 |
+-------------+
1 row in set (0.04 sec)"""


SELECT COUNT(*) FROM cursos;

"""mysql> SELECT COUNT(*) FROM cursos;
+----------+
| COUNT(*) |
+----------+
|       30 |
+----------+
1 row in set (0.01 sec)"""


SELECT * FROM cursos
WHERE carga > 40;

"""mysql> SELECT * FROM cursos
    -> WHERE carga > 40;
+---------+-----------+------------------------------------------------------+-------+----------+------+
| idcurso | nome      | descricao                                            | carga | totaulas | ano  |
+---------+-----------+------------------------------------------------------+-------+----------+------+
|       9 | POO       | Curso de Programação Orientada a Objetos             |    60 |       35 | 2016 |
|      14 | Android   | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      17 | Swift     | Curso de Desenvolvimento de Aplicativos para iOS     |    60 |       30 | 2019 |
|      24 | WordPress | Curso de Criação de Sites com WordPress              |    60 |       30 | 2019 |
|      25 | Joomla    | Curso de Criação de Sites com Joomla                 |    60 |       30 | 2019 |
|      26 | Magento   | Curso de Criação de Lojas Virtuais com Magento       |    50 |       25 | 2019 |
+---------+-----------+------------------------------------------------------+-------+----------+------+
6 rows in set (0.00 sec)"""


SELECT COUNT(*) FROM cursos WHERE carga > 40;

"""mysql> SELECT COUNT(*) FROM cursos WHERE carga > 40;
+----------+
| COUNT(*) |
+----------+
|        6 |
+----------+
1 row in set (0.01 sec)"""


SELECT * FROM cursos ORDER BY carga DESC;

"""mysql> SELECT * FROM cursos ORDER BY carga DESC;
+---------+--------------------+------------------------------------------------------+-------+----------+------+
| idcurso | nome               | descricao                                            | carga | totaulas | ano  |
+---------+--------------------+------------------------------------------------------+-------+----------+------+
|       9 | POO                | Curso de Programação Orientada a Objetos             |    60 |       35 | 2016 |
|      14 | Android            | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      17 | Swift              | Curso de Desenvolvimento de Aplicativos para iOS     |    60 |       30 | 2019 |
|      24 | WordPress          | Curso de Criação de Sites com WordPress              |    60 |       30 | 2019 |
|      25 | Joomla             | Curso de Criação de Sites com Joomla                 |    60 |       30 | 2019 |
|      26 | Magento            | Curso de Criação de Lojas Virtuais com Magento       |    50 |       25 | 2019 |
|       1 | HTML5              | Curso de HTML5                                       |    40 |       37 | 2014 |
|       4 | PHP                | Curso de PHP para iniciantes                         |    40 |       20 | 2015 |
|       5 | Java               | Introdução à Linguagem Java                          |    40 |       29 | 2015 |
|       7 | Word               | Curso completo de Word                               |    40 |       30 | 2016 |
|       8 | Python             | Curso de Python                                      |    40 |       18 | 2017 |
|      10 | Excel              | Curso completo de Excel                              |    40 |       30 | 2017 |
|      12 | C++                | Curso de C++ com Orientação a Objetos                |    40 |       25 | 2017 |
|      19 | Redes              | Curso de Redes para Iniciantes                       |    40 |       15 | 2016 |
|      29 | PHP7               | Curso de PHP, versão 7.0                             |    40 |       20 | 2020 |
|      15 | JavaScript         | Curso de JavaScript                                  |    35 |       18 | 2017 |
|       6 | MySQL              | Bancos de Dados MySQL                                |    30 |       15 | 2016 |
|      11 | Responsividade     | Curso de Responsividade                              |    30 |       15 | 2018 |
|      13 | C#                 | Curso de C#                                          |    30 |       12 | 2017 |
|      16 | PowerPoint         | Curso completo de PowerPoint                         |    30 |       12 | 2018 |
|      18 | Hardware           | Curso de Montagem e Manutenção de PCs                |    30 |       12 | 2017 |
|      21 | SEO                | Curso de Otimização de Sites                         |    30 |       12 | 2017 |
|      27 | Modelagem de Dados | Curso de Modelagem de Dados                          |    30 |       12 | 2020 |
|      30 | PHP4               | Curso de PHP, versão 4.0                             |    30 |       11 | 2010 |
|       2 | Algoritmos         | Lógica de Programação                                |    20 |       15 | 2014 |
|      22 | Premiere           | Curso de Edição de Vídeos com Premiere               |    20 |       10 | 2017 |
|      23 | After Effects      | Curso de Efeitos em Vídeos com After Effects         |    20 |       10 | 2018 |
|      28 | HTML4              | Curso Básico de HTML, versão 4.0                     |    20 |        9 | 2010 |
|      20 | Segurança          | Curso de Segurança                                   |    15 |        8 | 2018 |
|       3 | Photoshop5         | Dicas de Photoshop CC                                |    10 |        8 | 2014 |
+---------+--------------------+------------------------------------------------------+-------+----------+------+
30 rows in set (0.00 sec)"""


SELECT max(carga) FROM cursos; # Seleciona o maior registro de todos os valores existentes em 'carga' dos cursos existentes.

"""mysql> SELECT max(carga) FROM cursos;
+------------+
| max(carga) |
+------------+
|         60 |
+------------+
1 row in set (0.00 sec)"""


SELECT * FROM cursos WHERE ano = '2016'; # Seleciona todos os registros de cursos onde ano = 2016.

"""mysql> SELECT * FROM cursos WHERE ano = '2016';
+---------+-------+------------------------------------------+-------+----------+------+
| idcurso | nome  | descricao                                | carga | totaulas | ano  |
+---------+-------+------------------------------------------+-------+----------+------+
|       6 | MySQL | Bancos de Dados MySQL                    |    30 |       15 | 2016 |
|       7 | Word  | Curso completo de Word                   |    40 |       30 | 2016 |
|       9 | POO   | Curso de Programação Orientada a Objetos |    60 |       35 | 2016 | <<<<<<<<<<<<<<<<<<
|      19 | Redes | Curso de Redes para Iniciantes           |    40 |       15 | 2016 |
+---------+-------+------------------------------------------+-------+----------+------+
4 rows in set (0.00 sec)"""

SELECT max(totaulas) FROM cursos WHERE ano = '2016'; # Seleciona o maior valor do Total_Aulas dos cursos com ano = 2016.

"""mysql> SELECT max(totaulas) FROM cursos WHERE ano = '2016';
+---------------+
| max(totaulas) |
+---------------+
|            35 |
+---------------+
1 row in set (0.00 sec)"""


SELECT min(totaulas) FROM cursos; # Seleciona o menor valor do Total_Aulas dos cursos existentes.

"""mysql> SELECT min(totaulas) FROM cursos;
+---------------+
| min(totaulas) |
+---------------+
|             8 |
+---------------+
1 row in set (0.00 sec)"""


SELECT min(totaulas) FROM cursos WHERE ano = '2016'; # Seleciona o menor valor dos cursos existentes no ano de 2016.

"""mysql> SELECT min(totaulas) FROM cursos WHERE ano = '2016';
+---------------+
| min(totaulas) |
+---------------+
|            15 |
+---------------+
1 row in set (0.00 sec)"""


SELECT nome, MIN(totaulas) FROM cursos WHERE ano = '2016';

"""mysql> SELECT nome, MIN(totaulas) FROM cursos WHERE ano = '2016';
+-------+---------------+
| nome  | MIN(totaulas) |
+-------+---------------+
| MySQL |            15 |
+-------+---------------+
1 row in set (0.00 sec)"""


# Agora vamos para um detalhe da Função de Agregação. Elas retornarão APENAS o primeiro resultado da query, mas não todas.

SELECT * FROM cursos WHERE ano = '2016';

"""mysql> SELECT * FROM cursos WHERE ano = '2016';
+---------+-------+------------------------------------------+-------+----------+------+
| idcurso | nome  | descricao                                | carga | totaulas | ano  |
+---------+-------+------------------------------------------+-------+----------+------+
|       6 | MySQL | Bancos de Dados MySQL                    |    30 |       15 | 2016 |
|       7 | Word  | Curso completo de Word                   |    40 |       30 | 2016 |
|       9 | POO   | Curso de Programação Orientada a Objetos |    60 |       35 | 2016 |
|      19 | Redes | Curso de Redes para Iniciantes           |    40 |       15 | 2016 |
+---------+-------+------------------------------------------+-------+----------+------+
4 rows in set (0.00 sec)"""

# Observe que MySQL tem 15 aulas e Redes também possui 15 aulas. 
# A função de agregação capturou apenas a primeira ocorrência. 
# Se eu quisesse mostrar os dois resultados, aí não seria somente FUNÇÃO DE AGREGAÇÃO, seria necessário também FUNÇÕES DE AGRUPAMENTO (próxima aula).

# Agora vamos utilizar a Função de Agregação pra saber a SOMA (SUM).

SELECT SUM(totaulas) FROM cursos;

"""mysql> SELECT SUM(totaulas) FROM cursos;
+---------------+
| SUM(totaulas) |
+---------------+
|           583 |
+---------------+
1 row in set (0.00 sec)"""


SELECT sum(totaulas) FROM cursos WHERE ano = '2016';

"""mysql> SELECT sum(totaulas) FROM cursos WHERE ano = '2016';
+---------------+
| sum(totaulas) |
+---------------+
|            95 |
+---------------+
1 row in set (0.00 sec)"""


# Agora vamos utilizar a Função de Agregação pra saber a MÉDIA (AVG). 

SELECT AVG(totaulas) FROM cursos;
"""mysql> SELECT AVG(totaulas) FROM cursos;
+---------------+
| AVG(totaulas) |
+---------------+
|       19.4333 |
+---------------+
1 row in set (0.01 sec)"""




# LISTA DE EXERCÍCIOS DAS AULAS 11 e 12 - Exercitando! (importar a dump da aula anterior)

# 1 - Uma lista com o nome de todas as gafanhotas.
# 2 - Uma lista com os dados de todos aqueles que nasceram entre 1-Jan-2000 e 31-Dez-2015.
# 3 - Uma lista com o nome de todos os homens que trabalham como Programador.
# 4 - Uma lista com os dados de todas as mulheres que nasceram no Brasil e que têm seu nome iniciando com a letra J.
# 5 - Uma lista com o nome e a nacionalidade de todos os homens que têm Silva no nome, não nasceram no Brasil e pesam menos de 100 kg.
# 6 - Qual é a maior altura entre gafanhotos homens brasileiros?  
# 7 - Qual é a média de peso dos gafanhotos cadastrados?
# 8 - Qual o menor peso entre as gafanhotas mulheres que nasceram fora do Brasil entre 01-Jan-1990 e 31-Dez-2000?
# 9 - Quantas gafanhotas mulheres tem mais de 1.90 m de altura?

SHOW DATABASES;
USE cadastro;
SHOW TABLES;
DESCRIBE gafanhotos;
"""mysql> describe gafanhotos;
+---------------+---------------+------+-----+---------+----------------+
| Field         | Type          | Null | Key | Default | Extra          |
+---------------+---------------+------+-----+---------+----------------+
| id            | int           | NO   | PRI | NULL    | auto_increment |
| nome          | varchar(30)   | NO   |     | NULL    |                |
| profissao     | varchar(20)   | YES  |     | NULL    |                |
| nascimento    | date          | YES  |     | NULL    |                |
| sexo          | enum('M','F') | YES  |     | NULL    |                |
| peso          | decimal(5,2)  | YES  |     | NULL    |                |
| altura        | decimal(3,2)  | YES  |     | NULL    |                |
| nacionalidade | varchar(20)   | YES  |     | Brasil  |                |
+---------------+---------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)"""


# 1 - Uma lista com o nome de todas as gafanhotas.

SELECT nome FROM gafanhotos WHERE sexo =`F` ORDER BY nome ASC;

"""mysql> SELECT nome FROM gafanhotos WHERE sexo = 'F' ORDER BY nome;
+------------------------+
| nome                   |
+------------------------+
| Ana Carolina Hernandes |
| Ana Carolina Mendes    |
| Andreia Delfino        |
| Bruna Santos           |
| Bruna Teles            |
| Daniele Moledo         |
| Dayana Dias            |
| Elaine Nunes           |
| Janaína Couto          |
| Janaina Oliveira       |
| Jarismar Andrade       |
| Josiane Dutra          |
| Jucinei Teixeira       |
| Karine Ribeiro         |
| Leila Martins          |
| Letícia Neves          |
| Monique Precivalli     |
| Nara Matos             |
| Rita Pontes            |
| Rosana Kunz            |
| Silvana Albuquerque    |
| Talita Nascimento      |
+------------------------+
22 rows in set (0.00 sec)"""


# 2 - Uma lista com os dados de todos aqueles que nasceram entre 1-Jan-2000 e 31-Dez-2015.

SELECT * FROM gafanhotos WHERE nascimento BETWEEN '2000-01-01' AND '2015-12-31'; 

"""mysql> SELECT * FROM gafanhotos WHERE nascimento BETWEEN '2000-01-01' AND '2015-12-31';
+----+---------------------------+----------------------+------------+------+--------+--------+---------------+
| id | nome                      | profissao            | nascimento | sexo | peso   | altura | nacionalidade |
+----+---------------------------+----------------------+------------+------+--------+--------+---------------+
|  8 | Carlisson Rosa            | Professor            | 2010-08-01 | M    |  78.22 |   1.98 | Brasil        |
| 16 | Elvis Schwarz             | Dentista             | 2011-05-07 | M    |  66.69 |   1.76 | EUA           |
| 20 | Marcos Dissotti           | Empreendedor         | 2010-01-01 | M    |  53.79 |   1.54 | Portugal      |
| 21 | Ana Carolina Mendes       | Ator                 | 2000-12-15 | F    |  88.30 |   1.54 | Brasil        |
| 22 | Guilherme de Sousa        | Dentista             | 2001-05-18 | M    | 132.70 |   1.97 | Moçambique    |
| 23 | Bruno Torres              | Auxiliar Administrat | 2000-01-30 | M    |  44.65 |   1.65 | Brasil        |
| 27 | Monique Precivalli        | Auxiliar Administrat | 2013-12-30 | F    |  48.20 |   1.22 | Brasil        |
| 32 | Roberto Luiz Debarba      | Ator                 | 2007-01-09 | M    |  77.44 |   1.56 | Brasil        |
| 33 | Jarismar Andrade          | Dentista             | 2000-06-23 | F    |  63.70 |   1.33 | Brasil        |
| 35 | Márcio Mello              | Programador          | 2011-11-20 | M    |  54.11 |   1.55 | EUA           |
| 36 | Robson Rodolpho           | Auxiliar Administrat | 2000-08-08 | M    | 110.10 |   1.76 | Brasil        |
| 37 | Daniele Moledo            | Empreendedor         | 2006-08-11 | F    | 101.30 |   1.99 | Brasil        |
| 39 | Neriton Dias              | Auxiliar Administrat | 2009-10-30 | M    |  48.99 |   1.29 | Brasil        |
| 41 | Isaias Buscarino          | Dentista             | 2001-01-07 | M    |  99.90 |   1.55 | Moçambique    |
| 46 | Diogo Padilha             | Auxiliar Administrat | 2000-03-03 | M    |  54.34 |   1.88 | Angola        |
| 49 | Silvio Ricardo            | Programador          | 2012-03-12 | M    |  65.99 |   1.23 | EUA           |
| 50 | Denilson Barbosa da Silva | Empreendedor         | 2000-01-08 | M    |  97.30 |   2.00 | Brasil        |
| 58 | Carlos Camargo            | Programador          | 2005-02-22 | M    | 124.65 |   1.33 | Brasil        |
| 59 | Philppe Oliveira          | Auxiliar Administrat | 2000-05-23 | M    | 105.10 |   2.19 | Brasil        |
+----+---------------------------+----------------------+------------+------+--------+--------+---------------+
19 rows in set (0.00 sec)"""


# 3 - Uma lista com o nome de todos os homens que trabalham como Programador.

SELECT nome FROM gafanhotos
WHERE profissao = `Programador` AND sexo = `M` ORDER BY nome;

"""mysql> SELECT nome FROM gafanhotos
    -> WHERE profissao = 'Programador' and sexo = 'M'
    -> ORDER BY nome;
+-----------------+
| nome            |
+-----------------+
| Allan Silva     |
| Anderson Rafael |
| Andre Santini   |
| André Schmidt   |
| Carlos Camargo  |
| Emerson Gabriel |
| Jackson Telles  |
| Márcio Mello    |
| Raian Porto     |
| Ruan Valente    |
| Silvio Ricardo  |
+-----------------+
11 rows in set (0.00 sec)"""


# 4 - Uma lista com os dados de todas as mulheres que nasceram no Brasil e que têm seu nome iniciando com a letra J.

SELECT * FROM gafanhotos WHERE sexo = `F` AND nacionalidade = `Brasil` AND nome LIKE `J%`;

"""mysql> SELECT * FROM gafanhotos
    -> WHERE sexo = 'F'
    -> AND nacionalidade = 'Brasil'
    -> AND nome LIKE 'J%';
+----+------------------+-----------+------------+------+-------+--------+---------------+
| id | nome             | profissao | nascimento | sexo | peso  | altura | nacionalidade |
+----+------------------+-----------+------------+------+-------+--------+---------------+
| 33 | Jarismar Andrade | Dentista  | 2000-06-23 | F    | 63.70 |   1.33 | Brasil        |
+----+------------------+-----------+------------+------+-------+--------+---------------+
1 row in set (0.00 sec)"""


# 5 - Uma lista com o nome e a nacionalidade de todos os homens que têm Silva no nome, não nasceram no Brasil e pesam menos de 100 kg.

SELECT nome, nacionalidade FROM gafanhotos
WHERE sexo = 'M'
AND nome LIKE '%silva%'
AND nacionalidade != 'Brasil'
AND peso < '100';

"""mysql> SELECT nome, nacionalidade FROM gafanhotos
    -> WHERE sexo = 'M'
    -> AND nome LIKE '%silva%'
    -> AND nacionalidade != 'Brasil'
    -> AND peso < '100';
+----------------+---------------+
| nome           | nacionalidade |
+----------------+---------------+
| Herisson Silva | EUA           |
+----------------+---------------+
1 row in set (0.00 sec)"""


# 6 - Qual é a maior altura entre gafanhotos homens brasileiros?

SELECT max(altura) WHERE sexo = 'M' AND nacionalidade = 'Brasil';

"""mysql> SELECT max(altura) FROM gafanhotos
    -> WHERE sexo = 'M'
    -> AND nacionalidade = 'Brasil';
+-------------+
| max(altura) |
+-------------+
|        2.35 |
+-------------+
1 row in set (0.00 sec)"""


# 7 - Qual é a média de peso dos gafanhotos cadastrados?

SELECT AVG(peso) FROM gafanhotos;

"""mysql> SELECT AVG(peso) FROM gafanhotos;
+-----------+
| AVG(peso) |
+-----------+
| 73.967705 |
+-----------+
1 row in set (0.00 sec)"""


# 8 - Qual o menor peso entre as gafanhotas mulheres que nasceram fora do Brasil entre 01-Jan-1990 e 31-Dez-2000?

SELECT min(peso) FROM gafanhotos WHERE sexo = `F` AND nacionalidade <> `Brasil` AND nascimento BETWEEN `1990-01-01` AND `2000-12-31`;

"""mysql> SELECT min(peso) FROM gafanhotos
    -> WHERE sexo = 'F'
    -> AND nacionalidade <> 'Brasil'
    -> AND nascimento BETWEEN '1990-01-01' AND '2000-12-31';
+-----------+
| min(peso) |
+-----------+
|     35.90 |
+-----------+
1 row in set (0.00 sec)"""


# 9 - Quantas gafanhotas mulheres tem mais de 1.90 m de altura?

# Podemos fazer em duas etapas, primeiro: 
SELECT * FROM gafanhotos WHERE sexo = `F` AND altura > `1.90`;

# E depois, podemos filtrar o totalizador desses registros:
SELECT COUNT(*) FROM gafanhotos WHERE sexo = `F` AND altura > `1.90`;

"""mysql> SELECT * FROM gafanhotos
    -> WHERE altura > '1.90'
    -> AND sexo = 'F';
+----+------------------------+--------------+------------+------+--------+--------+---------------+
| id | nome                   | profissao    | nascimento | sexo | peso   | altura | nacionalidade |
+----+------------------------+--------------+------------+------+--------+--------+---------------+
|  5 | Leila Martins          | Farmacêutico | 1975-04-22 | F    |  99.00 |   2.15 | Brasil        |
|  6 | Letícia Neves          | Programador  | 1999-12-03 | F    |  87.00 |   2.00 | Brasil        |
| 37 | Daniele Moledo         | Empreendedor | 2006-08-11 | F    | 101.30 |   1.99 | Brasil        |
| 43 | Ana Carolina Hernandes | Ator         | 1970-10-11 | F    |  65.40 |   2.08 | EUA           |
| 48 | Elaine Nunes           | Programador  | 1998-08-15 | F    |  35.90 |   2.00 | Canadá        |
+----+------------------------+--------------+------------+------+--------+--------+---------------+
5 rows in set (0.00 sec)"""

"""mysql> SELECT COUNT(*) FROM gafanhotos
    -> WHERE altura > '1.90'
    -> AND sexo = 'F';
+----------+
| COUNT(*) |
+----------+
|        5 |
+----------+
1 row in set (0.00 sec)"""





"""
Transcrição


0:00
hum hum hum
0:19
olá pequeno gafanhoto seja bem vindo a mais uma aula de seu curso em vídeo de banco de dados com mais que l
0:26
o meu nome é gustavo guanabara eu sou seu professor chegamos agora a segunda parte da aula que a gente começou na
0:32
aula passada que ensinando como obter dados das tabelas então a gente vai dar continuidade ao
0:37
estudo do comando select e o comando select como eu já falei várias vezes durante esse curso é sim o comando mais
0:44
famoso é o comando mais utilizado e ao comando que tem mais parâmetros dentro da linguagem sql e eu vou te falar
0:51
até por ter mais parâmetros é o comando que mais muda de uma versão de sql para
0:56
a outra não estou dizendo que de uma versão demais querem pra outra versão de my sql vai mudar
1:02
não vai talvez uma mudança assim ou outra mas por exemplo se você tentar utilizar o select do oracle do mais que
1:09
ele serve provavelmente você vai ter várias mudanças a iná sintax então você vai ter que dar uma adaptada
1:16
voltando a dizer esse curso não é completamente inútil para quem utiliza outra ferramenta como por exemplo pulso
1:21
e se parece bastante simplesmente você vai ter que ter um trabalho a mais de filtrar aquilo que eu tô te ensinando
1:27
adaptar sua plataforma então por exemplo se eu te ensinando o select aqui com funções de agregação de funções de
1:33
navegação vão funcionar em todos mas por exemplo se eu te mostrar a função de agregação mais detalhada que não é o
1:38
caso e que não funciona no possuir basta você procurar na comunidade do poço e como isso se adapta a mais que ele está
1:45
cheio de site é que ensinamos sintaxes múltiplas é o cara vai te ensinar o select ele mostra olha eu mais quero é
1:50
assim no pulso e assim no lax é assim na hora qual é assim então você não vai usar isso de desculpa para não estudar
1:56
mais quer com a gente mas vamos dar continuidade aqui porque a lista de comando está grande e no final dessa aula em exercício eu vou deixar
2:03
exercícios e vai fazer os exercícios são nove exercícios e parei pra vocês e vocês vão deixar nos comentários às
2:09
respostas então discutam entre vocês com a resposta melhor de cada um dos exercícios coloquei isso nessa aula e para aumentar
2:15
a interatividade entre a gente então vamos começar com um exemplo que a gente viu na aula passada se você se lembra muito bem na aula
2:21
passado a gente deixou aqui dez registros de exemplo eu coloquei a tabela de cursos estou colocando dez registros aqui como
2:28
base a gente poder trabalhar os nossos comandos e ver quais seriam os resultados possíveis então como é que a gente vai trabalhar
2:34
aqui é o seguinte olha só select asterix concursos se eu botar só esse comando ele vai selecionar todo mundo não é isso mas eu
2:41
vou criar um filtro aqui que é o é nome golpe hp lembrando que por mais que ele
2:46
toda stream todo dado está entre aspas simples então assim é uma sintaxe que é padrão é
2:51
o seguinte a eu quero nome do curso e golpe hp então o nome do curso php
2:56
a quantidade de horas é maior que 30 maior que 30 a data de lançamento foi dia 1º de março
3:03
de 2016 1º de março de 2016 tudo entre aspas
3:08
simples se você aprender assim não tem como errar é claro que você vê assim táxis oficiais o nome dos campos entre
3:15
crases eu não utilizo isso por questão de facilidade de digitação mas se você encontrar um curso que diz
3:21
olha é obrigatório na verdade não é obrigatório mas ficará usa ele está dentro dos padrões e também não
3:27
significa que a gente tá errado porque está fora do padrão eu estou ensinando de uma maneira mais fácil pra você ficar
3:33
digitando se você começar a colocar cras na frente e depois depois de cada um dos campos cada um dos nomes vai ficar de
3:38
saco cheio rapidinho só simplificando pra você mas saiba que por exemplo uma coisa que não é muito recomendável que os campos
3:44
têm um espaço dentro nome do campo é selar nome do curso geralmente bota o nome do design curso você pode botar
3:51
nome espaço curso você pode fazer isso só que se você fizer isso no sql você vai ter que
3:57
colocar casa na hora de representar toda vez nesse campo então não coloca o que eu vou fazer o seguinte
4:03
mandei selecionar todos os dados da tabela cursos onde o nome seja igual a
4:08
php então ele vai selecionar ó php a essa é a linha que ele vai selecionar lembrando
4:14
linha registro outro plan você pode chamar o que você quiser mas aí vem uma dúvida tá beleza você mostrou
4:21
na aula passada que tem o maior menor igual ou maior igual ou menor igual mas
4:26
eu estou tentando fazer por exemplo mostrar os cursos que começam com a letra p e não estou conseguindo isso porque eu
4:32
não te mostrei na água passada de propósito para deixar para essa segunda porque já estava bem cheia de conteúdo aquela anterior
4:38
o operador especial e que muita gente usa o operador que a gente vai trabalhar agora é o operador lic
4:44
vamos ver um exemplo aqui botar lá select as três foram cursos exatamente como eu fiz anteriormente e vou colocar o er nome lalique e por cento
4:53
like pode ser uma palavra que significa gostar né o curtir do facebook mas na
4:58
verdade aquele que é parecido é semelhante esse porcentual em chama de guarda o
5:04
quarto que é a carta curinga e que a gente pode utilizar para substituir alguma coisa assim como colina
5:09
vamos ver funcionando vamos sair agora da nossa apresentação e diretamente para o nosso ambiente com o mais quero
5:14
workbench tentar fazer o seguinte ó select asterisco from cursos
5:21
ele selecionou todos os cursos quero selecionar todos os cursos que têm um p embora o é nome igual a você tem a
5:31
tendência a shark você colocar isso aqui ó o é o nome google app ele vai te mostrar os cursos começa com p
5:37
na verdade não se mostrou nada porque você não tem nenhum curso que se chama p e também não adianta botar por cento
5:43
aqui ó e também não vai mostrar nada isso porque o operador de igualdade assim como o nome sugere ele testa
5:50
igualdades então você não tem nenhum curso chamado p por cento então não vai mostrar mas se
5:55
eu quiser semelhança está a lic semelhante a um por cento o coringa que
6:02
o caracter coringa tem um significado específico a gente vai viajar mas o fato é só apertar contra o inter ele vai
6:09
botar todos os cursos que começam com t photoshop php python pior ponto pra mim
6:14
é pega p7 php 4 e o mais legal é que olic ele é parecido parecido mesmo ele é
6:20
case sensitivity cerca de 7 significa o seguinte se eu colocar o nome lá equipe minúsculo
6:27
seguido da porcentagem rodada contra o inter ele também vai mostrar o mesmo resultado
6:32
beleza então considera o like.com operador assim como o âmbito em que a gente viu na aula passada estar escrito
6:39
lic fica aquele não é um operador tem aluno que faz assim a operadora maior menor
6:45
igual o líquido é operador sim olic é um operador o bi turbina operador o im é um
6:50
operador então é que ele tem operadores literais tem operadores que têm letras na
6:56
composição então se eu quiser aqui por exemplo todo o curso que começa com a ele também faz o after effects
7:02
algoritmos e android sendo assim como eu disse anteriormente à palavra light significa parecido e não
7:09
gostar curtir o pôr cento é um caracter curinga que substitui nenhum ou vários
7:16
caracteres então assim esse por cento substituir nenhum ou vários caracteres por exemplo
7:22
se eu tiver um curso chamado só p ele vai selecionar se tiver php photoshop como você já viu aconteceu ele
7:28
vai selecionar então ele vai trocar esse por cento por qualquer conjunto de caracteres inclusive nenhum caractere ea
7:35
posição do por cento têm toda influência então nesse caso aqui como você viu eu estou dizendo selecione todos os campos
7:42
da tabela cursos onde o nome se pareça com p seguido de qualquer coisa
7:47
inclusive seguido de nada então ele vai selecionar aqui os nossos cursos que começam com o pp e são seguidos de
7:53
qualquer coisa inclusive de nada e aí a gente pode brincar com a posição desse nosso carácter coringa
7:59
então a gente vai começar a trabalhar com as oito cards então vamos ver um exemplo aqui select asterisco foram
8:04
cursos o economic por cento a percebe que eu substituir eu mudei a posição do por
8:12
cento vamos ver o resultado que estudar então olha só eu coloquei será que aqueles com curso é nome li ke ha por cento ele me
8:19
mostrou que os cursos que começam com a se eu trocar o por cento daqui pra cá o
8:26
que vai acontecer vou pressionar contra o enter e ele me mostrou java segurança
8:31
e dilma tá mas onde está o ar no final presta atenção percebe que java
8:37
segurança e de uma terminam com a letra a e eu posso colocar o a minúsculo a
8:43
maiúsculo sem problema nenhum ele vai resultar a mesma coisa então basicamente o que ele fez ele
8:48
selecionou eu estou selecionando todos os campos da tabela cursos onde o nome
8:54
essa com qualquer coisa encerrada com a deu pra entender
8:59
então por exemplo se eu colocar o por cento no final ele substitui e você vai testar o início se eu colocar o por
9:06
cento no início ele substitui e vai testar o final não vê na tela que se você ainda fica um pouco enrolado
9:11
então percebi ali nessa nossa lista quais cursos terminam com a letra a nessa lista eu tenho apenas java se você
9:19
dá uma olhadinha eu tô falando pra você poder dar uma analisada nenhum dos outros nomes termina com a
9:25
letra a então é qualquer coisa seguida da letra tá mas e se eu quiser a letra em
9:31
qualquer lugar eu quero a letra no início eu quero entrar no final cada letra no meio eu quero letrado de
9:36
qualquer jeito dá pra fazer você pode fazer isso daqui ó em vez de colocar a por cento ou por
9:43
cento a colocar o nome like por cento a por cento isso significa que vai ter qualquer
9:48
coisa na frente e qualquer coisa atrás inclusive nada e essa é uma dúvida muito
9:53
comum entre os gafanhotos que estão começando o cara fala assim tá por cento a por cento é a no meio não serve no
10:00
início não serve no final serve porque como a gente viu o árbitro card por cento substituir nada ou várias coisas
10:08
nesse caso então ele vai selecionar todos os registros que tenham lá em qualquer lugar você percebe a algoritmos
10:15
começa com a java termina com a sapateado tem 2 às em posições
10:21
diferentes e cozinha árabe também tem dois as inclusive aquele acentuado também é considerado dentro do select
10:28
isso não acontece em todos os escalões não ainda foi outro cuidado com isso o mais que ele suporta se você colocou lá
10:35
o tf 8 ele vai suportar caracteres acentuados e vai utilizá los na indexação na seleção e tudo mais então
10:42
um assento é considerado um a mais cuidado que nem todo sql considera isso
10:48
aí vamos fazer o teste então vou colocar aqui ó por cento a por cento contra o
10:53
inter ele me deu a vários cursos que tenha em qualquer lugar e se eu quiser que não tenha em lugar nenhum é só botar
11:00
aqui ó not like isso daqui ele vai mostrar os cursos pelo photoshop não tenha lugar nenhum mas que ele não
11:08
tem em lugar nenhum e aí você sabia disso é claro que sabia né então eu mostrei na aula passada que a
11:14
gente tem os operadores não eo utilizados porque a sua inteligência vai permitir que uma coisa vamos colocar
11:21
aqui no registro 9 vamos colocar um acentuado aqui no meio
11:26
vamos colocar aqui ó update cursos 7
11:32
nome igual à p a com acento ó o é e de curso igual a 9
11:45
contra o inter ele modificou vamos dar o mesmo select agora a pior
11:51
não faz parte se eu tirar o note que você vai ver que agora uma de selecionar todo mundo tem a
11:57
pior só tem um acentuado no meio e ele conseguiu pegar gostou da dica eu vou te dar mais uma
12:04
dica para você não precisa ficar lembrando do update é claro você precisa conhecer o comando mas o ocidente de
12:09
ajuda nisso olha só que interessante o que eu posso fazer o seguinte vir aqui no meu horizonte 7 e clicar duas vezes e ditar
12:18
uma vez editado a ele botou a canetinha aqui pressionar enter ele já editou e eu vou ficar aqui
12:25
embaixo apply ele já vai montar o comando olha só também serve de dica pra você e
12:31
aprendendo os comandos na utilização ou orkut como eu falei lá na segunda aula eu falei dá pra usar o orkut sem usar
12:38
comando é pra você e brincando várias coisas dá pra fazer mas o meu objetivo não é ficar mostrando isso porque o meu
12:43
objetivo é que você aprenda hoje comandos que a gente vai utilizar mais à frente o php no java no que você quiser dando apply ele vai aplicar o comando do
12:53
finnish eo pior já não faz mais parte ano ele veio pra cá lá o pior não tenha
12:58
no meio e você pode brincar com assoalho do carro de qualquer forma utilizando antes da maneira que você achar melhor
13:04
vamos dar mais um exemplo aqui select asterisco from cursos mulher nome lalique ph por cento p a senhora falar
13:12
olha só vai selecionar bhp não olha só raciocina comigo ele vai fazer qualquer
13:19
curso cujo nome começa com ph e t o minicom p e aí você tá tá guanabara só
13:25
php atende a isso não senhor dá uma olhada aqui se você prestar atenção
13:31
photoshop também começa com ph e termina com p e aí será que ele vai pegar esse tipo de
13:38
coisa claro que vai ver o querido e sef que l então vamos fazer um teste tirar esse
13:43
update que pode incomodar vou fazer aqui vamos selecionar começando com ph qualquer coisa
13:51
inclusive nada p certo então a simplan php não tem nada aqui no meio por isso
13:57
que o por cento funciona pra nada ou pra qualquer coisa vou tirar aqui o note contra o enter
14:03
agora sim ó photoshop e php você pode estar pensando pô mas você tem um
14:08
negócio do php 4 php5 se criou o curso de php por que ele não pegou isso porque eles
14:15
não terminam com p extermínio com número thp 4h p5 quero te desejar
14:20
se você quiser que ele pegue esses também coloca mais um por cento no final assim ó posso fazer isso só botar 1% no
14:27
final contra o inter agora ele pegou a photoshop thp pega p4p
14:33
hp7 só pode ter nada ou alguma coisa no final tá mas e se você quiser em vez de falar
14:39
nada eu quero exatamente eu quero que pegue os php mas que tenha uma numeração no final tem
14:45
que ter alguma coisa no final como é que eu faço aí você usa outra hora do corte a outra ótica que eu tenho
14:51
para mostrar é o sublinhado então se vocês portal sublinhado você exige que tenha um caractere aqui e ele
14:58
pode ser qualquer um pode ser uma letra para um número mais que exige que tem alguma coisa op pressionando contra o inter ele pegou
15:04
lá só php 4 e php 7 olha só eu peguei todos os cursos que
15:10
têm um nome começados com ph tenham nada ou alguma coisa terminem com pp e que
15:18
tenham alguma coisa que no final quero é o seguinte ó vamos pegar de photoshop e vamos colocar photoshop 5
15:27
perto vou editar aqui aplicar ele vai fazer o update apliquei
15:33
finalizei está lá qualquer coisa que começa com ph termine
15:39
com p seguido de alguma coisa agora eu vou ter ph p4p hp7 photoshop 5 isso
15:46
porque o photoshop começa com ph tem qualquer coisa no meio termina com p
15:52
seguido de alguma coisa beleza então já te ensinei dois caracteres curinga a porcentagem e um
15:58
sublinhado não fazer mais um exemplo aqui e começar selecionando aqui todos os cursos começam a competir aqui ó php
16:04
python premier tá tudo aqui se você quiser você pode selecionar qualquer curso que começa com
16:12
p tenha qualquer letra depois tem a outro p e qualquer coisa após pressionando
16:21
contra o enter e selecionou todos esses cursos começam com p obrigatoriamente
16:26
tem uma letra depois e depois tem outro pé vão fazer outro exemplo o ataque a
16:32
todo mundo que tem te posso fazer p duas letras quaisquer então vou botar dois sublinhados no lugar t seguido de
16:41
qualquer coisa ele seleciona até o photoshop 5 foi esse caso ele tinha p duas coisas
16:48
tom e tem a gaiola e depois a letra t viu então o sublinhado ele obriga que
16:54
tem uma letra pode ser qualquer uma mas não pode ser nem uma letra e obriga que tenha um caractere assim o select com o
17:02
é usando like é uma das coisas que mais se usa dentro de um sistema porque os caras fazem busca por pedaços
17:09
então assim ah eu quero procurar pessoas que têm um silva no nome beleza vão procurar pessoas tenham silva 19
17:14
vou vir aqui fazer uma busca em gafanhotos em gafanhotos qualquer pessoa que tem um nome com
17:22
silva em qualquer lugar
17:27
seleciona aqui ó eu tenho alan silva edson silva e denílson barbosa cadê o silva dele da silva o cadastro a
17:35
pessoa nova que o tac sylvana albuquerque
17:42
vou colocar aquela é programadora também pode cadastrar direto aqui nasceu em
17:47
1999 dia 5 do mês 5 dia 22 é mulher
17:56
pesa 56 quilos e tem um metro e cinquenta nasceu no brasil
18:05
vamos aplicar a lidarem set to aplicando ele aplicou aqui lembrando que eu
18:13
coloquei o id como auto numeração então não precisa digitar deixa ele nulo na hora que ele deu em 7 eo ele já gerou
18:19
um código para mim automaticamente se você não puder ele como alto incremento ele não vai gerar então você percebe aqui ó que silva e
18:26
silvana também pegou por silvana tem silva a palavra silvana tem silva dentro
18:31
até mas eu não quero que pegue silva eu quero que silva seja um sobrenome uma das maneiras se pode fazer o
18:37
seguinte a botar aqui ó anderle na frente ele vai selecionar só quem tem silva com um espaço antes então ele não
18:43
vai pegar silvana nesse meu caso mas se você tivesse por exemplo maria silvana aí sim ele ia te mas por exemplo se
18:50
tivesse maria silvana esse caso ia pegar também a mas se eu quiser que pessoas que só terminem com silva já te ensinei
18:56
é fácil fazer se você quiser pessoas que terminem o nome com silva é só você colocar aqui por cento silva e aí ele
19:05
vai mostrar todo mundo que termina com silva silvano não faz mais parte se eu quiser pessoas que comecem com silva eu
19:11
boto o curioso é que no final e ele vai pegar só sylvana albuquerque acho que deu para você compreender o uso
19:17
do lec é poderosíssimo a gente já fez vários exemplos e ainda vou passar exercício pra você no final de preparar
19:23
a equipe vem bastante lá e aqui pra você utilizar mas vamos parar de falar só de olic porque nessa disse que é feito
19:29
vamos começar a aprender como distinguir coisas vão comando aqui select distinto
19:34
de carga from cursos e o que essa palavra distinct faz né qual o resultado dela presta atenção aqui na tela
19:42
se você analisar procura por carga na coluna carga você tem vários cursos que têm 40 horas
19:48
não tem itália vários deles têm 40 eu tenho um de 2011 de 10 onde 31 de 5 o
19:54
resto é tudo 40 o que diz ti ti ti vai fazer é pegar todos os que são iguais por exemplo era só 40 apareceu várias
20:01
vezes ele mostrar só os que são verdes ou 40 já que ele tem várias ocorrências
20:06
ele só mostra uma vez não entendeu direito vamos ver alguns exemplos não vim aqui ó
20:12
select asterisco honda fan outros simples assim gostei todos os gafanhotos
20:18
se eu quiser saber o país de nacionalidade 2000 já fontes qual ou quais são os países que eu tenho um
20:24
aluno tá beleza então vai pensar assim a inb select aviation foi outro que vai botar select nacionalidade franco foi outros
20:32
eu quero saber onde as pessoas nasceram lá ó brasil portugal moçambique e irlanda brasil brasil estados unidos
20:38
brasil portugal brasil brasil brasil brasil brasil brasil brasil você percebeu que ele apareceu nomes
20:45
repetitivos brasil portugal moçambique apareceu várias vezes mas se eu fizer uma lista só dos nomes eu não quero
20:51
saber é repetidamente eu quero só uma lista de quais locais as pessoas que
20:56
fazem curso comigo nasceram e aí é que vem a palavra distinct basicamente eu não estou interessado em saber onde cada
21:02
um nasceu eu quero saber só onde existem pessoas nascidas então voltar aqui ó distinct as várias ocorrências de brasil
21:11
moçambique e portugal vão virar apenas uma hora eu tenho no meu banco de dados
21:16
pessoas do brasil portugal moçambique e irlanda estados unidos frança japão canadá angola alemanha e itália
21:23
se você quiser ainda pode vir aqui o tribunal order by nacionalidade control
21:31
inter derrotou a alemanha angola brasil e tudo mais então agora eu tenho uma lista de que locais as pessoas nasceram
21:39
na minha base de dados e aí gostou assim não é tão comum você
21:44
utilizar o stint mas se por exemplo no seu sistema você quiser uma listagem por exemplo de
21:50
quais são as cargas horárias dos meus cursos aí usa aquele comando estava na tela antes você botar aqui ó
21:57
quero saber quais são as cargas dos meus
22:02
cursos ordenado por carga
22:08
então eu tenho lá ó eu tenho 10 horas 15 horas 20 horas 20 horas 20 a 20 30 horas
22:14
tentar evitar fazer isso eu faço eu boto distinct então quais são
22:19
as cargas horárias meu discurso eu tenho curso de dez horas de 15 horas de 20 horas de 30 de 35 e 40 e 50 e 60 horas
22:27
beleza e só pode tá falando uma pera aí mas quando os cursos têm 2 horas
22:32
não sei quantos curso tem 40 horas não sei mas dá pra saber da mas isso a gente
22:37
só vai ver na hora que vem a gente vai ver na próxima aula agrupamento seu a grupo o que eu estou fazendo aqui não é
22:43
agrupar somente distinguir não distingue serve pra isso ele pede assim quais foram as minhas ocorrências quais são
22:49
diferentes quais são distintas ai mostra para você beleza em momento nenhum com o
22:55
distintivo eu vou poder dizer olha tanto os cursos têm 40 horas olha os cursos tais tem 40
23:01
horas o desquite não serve pra isso é uma coisa muito específica além de distinção
23:07
eu posso fazer agregações isso é um assunto muito importante na linguagem
23:12
escreve assim como os operadores relacionais assim como por exemplo li que é muito importante funções de
23:17
agregação também são bastante utilizadas elas servem pra selecionar ou totalizar
23:23
alguma coisa vamos ver aqui as principais delas uma coisa que eu posso mostrar seguinte ela só select county
23:30
nome from cursos vamos entender isso melhor se eu colocar aqui select asterisco from cursos
23:37
encontrou em ter você vai ver que eu tenho vários cursos cadastrados eu tenho na verdade 30 cursos
23:44
cadastrados e percebe que o código está indo de 1 até 30 então eu tenho 30 cursos cadastrados
23:50
e agora o que importa aqui não é mostrar os cursos cadastrados eu quero saber quantos são os cursos
23:56
cadastrados uma das maneiras é você fazer isso que eu acabei de fazer da um selecto youtube conta os registros e reza para ter um
24:03
campo que faça isso mas dá pra fazer de maneira mais inteligente essa maneira mais inteligente é o seguinte olha só eu não quero que você
24:09
me mostre tudo eu quero que você ponte tudo então o rosinha aqui ó função de
24:17
agregação contra o inter olha lá o county é 30 vamos a outro exemplo aqui select
24:24
asterístico concursos o é lá carga maior do que 30
24:30
ele vai mostrar aqui quais são os cursos que têm carga acima de 30 o botão acima
24:36
de 40 para mostrar - acima de 40 e não vai mostrar-nos de 40 só tem os cursos de 50 e 60 horas
24:43
se você perceber que eu tenho um dois três quatro cinco seis cursos e aí o que me importa não é quais são os
24:50
cursos eu quero saber quanto os cursos têm mais de 40 horas aí utiliza uma função de agregação então
24:56
no lugar de select asterístico botar o counter asterisco olha só encontrou em
25:03
ter seis que foi exatamente o número que a gente tinha contado antes da piora de novo vou tirar o county enquanto os
25:10
registros têm a carga maior do que 40 123456 time mas eu quero saber se o
25:18
número então eu boto county que ele vai me contar eu tenho seja isso aqui conta pra mim ou
25:25
você conta na mão ou deixa o sql contar pra você gostou dessa né e tem muito mais função de agregação pra
25:31
mim aí então nesse nosso exemplo aqui o select tout nome concursos enquanto os nomes eu tenho ali a eu tenho dez nomes
25:38
então o counter nome é igual a 10 você não precisa contar com asteriscos e
25:43
pode colocar o nome do campo também outra função de agregação muito comum é o max o max ele vai ver qual é o máximo dentro
25:50
de um campo vamos aqui na prática olha só mudar select os três concursos a
25:57
ordem by carga
26:04
lá ele olhando por cargas a 10 é a menor carga e 60 é a maior carga
26:11
então se você quiser saber qual é a maior carga você pode fazer um site de se ordenar e lá no final mas dá pra
26:17
fazer mas quero trabalhar pra você em vez de selecionar tudo eu quero saber qual é a maior carga
26:23
então vou botar aqui em vez de asterisco vou colocar qual é a maior carga entre os cursos não
26:31
preciso do dérbi que só vai mostrar um número qual é a maior carga entre os cursos
26:36
a gente está vendo aqui que 60 certo quando encontrou em ter ao a 60 ele já faz pra você sozinho
26:43
e dá para a gente brincar mais com isso olha só eu quero saber aqui celexa esteves foram cursos
26:50
a uel é um ano igual 2015 colocar entre
26:55
aspas aqui que é o padrão eu quero saber quais são os cursos 2015
27:01
2015 foi pouco notado 2014 também foi pouco para 2016 tem bastante que é o
27:09
suficiente então eu tenho aqui ó quais são os cursos de 2016 se eu quiser
27:15
saber qual o curso teve mais aula em 2016 então bota aqui ó max total de aulas
27:23
então quero saber o seguinte eu não quero saber quais os cursos têm o ano de 2016
27:28
eu quero saber dentro dos cursos do ano de 2016 qual foi o máximo de total de aulas que
27:34
eu tive então se você olhar aqui ó o máximo de total de aulas que eu tive aqui em 2016 foi 35 que foi no curso de
27:41
programação orientada a objeto que nem existe destaque 35 aulas então ou você faz assim na mão você
27:48
manda e selecionar por exemplo selecione dos cursos que têm um ano de 2016 eu quero saber qual foi o maior
27:54
total de aulas deles você está pedindo pra sequer para fazer isso que eu fiz aqui pra você no olho ele vai retornar
28:00
35 a 35 é o máximo de total de aulas dos cursos do ano de 2016 está ficando cada
28:08
vez mais poderosas a linguagem sql né isso é o legal do select você poder saber perguntar para o sistema
28:15
você faz um questionamento faz uma cury para o servidor e ele responde isso sql
28:21
então nesse nosso exemplo aqui o máximo de total de aulas de cursos ali olhando na direita é total de aulas 37 que é o
28:28
maior e você também pode pegar o menor utilizando a função mim funcionamento
28:34
domingo vamos olhar e no canto qual é o menor total de aulas dos cursos eu tenho lá embaixo o último tem duas
28:41
aulas então é esse aí que vai selecionar fio e dá pra fazer um pouquinho mais um treino
28:46
antes então olha só eu quero o mínimo de total de aulas dos cursos de 2016
28:54
você quer 15 se eu quiser saber o nome desse curso eu posso fazer aqui ó nome vírgula
29:00
mim total de aulas vai botar aqui ó mais kelly teve 15 aulas vamos ver se foi realmente mais quer que
29:06
teve 15 aulas botão esteja aqui ó de todos os cursos que tiverem 2016
29:14
o mais kelly teve 15 aulas ele mostrou o nome e você vai falar peraí guanabara o de redes também teve
29:21
15 aulas e não apareceu isso porque ele pegou somente o primeiro a função de agregação ela vai ter um
29:28
número e vai te perguntar mas qual curso teve esse número e vai colocar o curso
29:33
que teve esse número a mas se eu quisesse mostrar os dois aí não é só função de agregação você precisaria de
29:39
funções de agrupamento que é o assunto da nossa próxima aula e tem mais condição de agregação olha só eu posso
29:46
utilizar a função sangue que é pra somar então o que ele vai fazer que é o seguinte olha só ao somatório do total
29:52
de aulas de cursos se você dá uma olhada aí ó quais são os total janelas que a gente tem aí na tela 37 15 8 29 15 30 30 32
30:02
somando isso tudo dá 216 então mostraria o total de aulas de todos esses cursos
30:09
216 horas vamos fazer na prática vão comigo então vamos lá mais uma vez eu quero todos os cursos de
30:16
2016 ali eu tive 15 aula já de sql 30 aulas de word 35 dp ó e 15 de redes vão
30:25
fazer uma conta rápida aqui ó 15 com 15 30 com 30 60 com 35 95
30:34
vamos ver se realmente a 95 então sam somatório de total de aulas dos cursos
30:44
de 2016 lá 95 foi o número que a gente calcula então meu querido tem várias têm vai ter
30:51
mais um homem está mais uma pra você além de somar você também pode tirar a média que é a avg toda foi que o leva a
30:59
vejo assim mas que tem a ver com o antivírus no antivírus meu querido avg vende em média em inglês que é verde
31:07
então basicamente ele vai fazer aqui é o seguinte já vai somar todos os cursos a gente já viu aqui da 216 não foi só
31:13
que ele vai dividir pelo número de cursos quanto os cursos vão aparecendo na tela 10 216 / 10 da 21,6
31:22
essa é a média de total de aulas dentro do curso no nosso exemplo aqui ó
31:27
os cursos com 2016 foram 12 34 cursos 95
31:35
aulas ao total dividido por quatro óperas g de totti aulas
31:41
a média é de 23 75 aulas então o que ele fez foi pegar aquele 95 e dividir pela
31:47
quantidade de cursos que atendiam aquela condição e aí gostou dessa aula então assim viu
31:53
como é que os separar as coisas não vão te encher de conteúdo é claro que se você já conhece as funções a moleza pra você mas fico
32:00
imaginando quando eu estava aprendendo se eu te mostrar a agregação e agrupamento na mesma aula até o nome se
32:05
parece vai confundir então vou deixar uma semana aí pra você dá uma assinada dar uma treinada a gente
32:12
não encerrou ainda não vamos pôr os exercícios separei 9 exercícios aqui ea idéia é a
32:17
seguinte você vai colocar em prática aquilo que eu te ensinei na aula onde sql e na aula 2
32:23
então o que nós vamos fazer o seguinte são nove exercícios que vão treinar o seu select só o select
32:29
então o que eu quero que você faça assistir isso vão dar uma lida nesses exercícios e você vai colocar pelo
32:35
número do exercício de 1 a 9 à sua resposta o ideal é que você faça um comentário com todas as respostas vamos ver quando
32:41
chegar foi outros vão acertar quando chegavam em outros vão errar e vocês por favor me ajudem nos comentários
32:47
só a querido você errou o número quatro i unió dar uma melhorada com certa dessa maneira
32:52
é assim que os gafanhotos aprendendo isso é feito sempre no curso em vídeo do curso de algoritmo tem muita gente
32:58
ajudando então essa é a idéia faz aí coloca a resposta no comentário desse vídeo e vamos colocar aí os comentários
33:05
para funcionar e nunca se esqueça você só aprende praticando não adianta ficar só vendo falar e fazer
33:11
tudo que estou fazendo aqui nas aulas então vamos aos nossos exercícios que eu coloquei aqui vamos exercitar tudo
33:17
aquilo que a gente aprendeu na primeira e na segunda aula de select que é essa daqui primeiro exercício que eu separei
33:23
pra vocês simples vamos selecionar uma lista com o nome de todas as garotas
33:29
na verdade eu sei que gafanhoto fêmea gafanhoto mulher vamos chamar de gafanhoto eu vou chamar de gafanhoto mulher partir de agora
33:36
prometo então sim eu quero uma lista de dos gafanhotos do cadastro a gente já fez
33:41
mas a coisa nos cursos utiliza a base de dados nós aulas anteriores eu ensinei como
33:46
importar nossa base de dados não é importar da anp não viu playlist querido
33:51
você pode ver todos os cursos têm a playlist ato organizado não adianta você caí aqui de paraquedas e acha que vai
33:58
acontecer tudo fácil assim o exercício número 2 eu quero uma lista com os dados de todos aqueles que
34:04
nasceram entre 1º de janeiro o exercício número 2 eu quero uma lista com todos os dados de todos aqueles que
34:10
nasceram entre 1º de janeiro de 2000 e 31 de dezembro de 2015 cuidado com a representação da data
34:16
lembra que a data representação é sempre ano mês e dia e não dia mês e ano como a gente faz por aí
34:22
o exercício 3 uma lista com o nome de todos os homens que trabalham como programador
34:27
então você tem cada pessoa com a sua profissão cadastrado eu quero só os programadores ficou fácil né
34:32
então tem um cadastro de todos os gafanhotos e suas profissões eu quero só os homens que são programadores o
34:38
exercício número quatro é uma lista com todos os dados de todas as mulheres que
34:43
nasceram no brasil e que tem seu nome iniciado com a letra j a nacionalidade e vai pegar o nome
34:50
começando com j e mostrou-lhe quiné o exercício 5 é o seguinte uma lista com o
34:55
nome ea nacionalidade de todos os homens eu não quero todos os dados eu quero só o nome ea nacionalidade cuidado com isso
35:02
que tem silva no nome em qualquer lugar não nasceram no brasil e pesam menos de
35:08
100 quilos isso vai te dar um trabalho só não o é mas é só você utilizar o operador lógico
35:14
não vou ficar te ensinando não faz aí vamos pôr exercício número 6 que é qual é a maior altura entre gafanhotos homens
35:21
que moram no brasil então não quero saber quem é o mais alto eu quero saber qual é a maior altura entre o grupo dos
35:27
gafanhotos que moram no brasil são homens a resposta para esse é o número se vai utilizar a função de agregação para isso
35:33
é óbvio o número 7 também vai utilizar agregação e eu quero qual é média de peso dos gafanhotos cadastrados
35:40
todos os gafanhotos o exercício 8 é o seguinte qual o menor peso entre os gafanhotos mulheres que nasceram fora do
35:47
brasil isso é não nasceram no brasil e entre 1º de janeiro de 1990 e 31 de dezembro de 2000 ea nona e última
35:54
questão é a seguinte quantas gafanhotos mulheres têm mais de 1 90 de altura e aí
35:59
fáceis difíceis você só vai ver se você tentar fazer então paulo o vídeo leva lá no exercício
36:07
do texto enquanto falando pausa vai lá no seu ambiente mas que é lhe faz o teste a nota resposta e coloca no
36:14
comentário aqui e aí eu espero que você tenha gostado dessa aula ela ficou bem grandinha mas mostrou bastante coisa
36:21
nova e select está pensando acabou select abonada meu querido ainda tem
36:26
mais aula de select aí e não vai parar na próxima não ainda vai ter mais então o que eu te peço é sempre a mesma
36:33
coisa bem aqui em cima clique aqui e se inscreve no canal sempre que tiver aula assim que sair
36:39
essa nova aula as aulas saem semanalmente assim que ela sair você vai ser avisada é bem pontual a aula mas por
36:46
acaso a gente atrasar você só fica sabendo se você se inscrever clicar na engrenagem vizinha e dizer quero receber um email assim que
36:52
ela sair do youtube manda um email pra você faça já saiu vai estudar é assim que funciona é quase a sua mãe
36:58
clicando aqui você vai pra playlist então se você assistiu só essa aula gostou da aula gostou da qualidade
37:04
seja bem vindo o curso em vídeo tem um curso completo de sql clicando aqui e tem vários outros cursos depois você viu
37:10
de sql procura nossos playlists tem muita coisa boa lá e aqui no meio o curso em vídeo que a experiência
37:16
completa onde você vai poder baixar inclusive o banco de dados de exemplo que a gente está falando aqui nunca se esqueça
37:21
pequeno gafanhoto mostras aulas com o maior número de pessoas interaja curta compartilhar nas redes
37:27
sociais porque o crescimento do curso em vídeo depende de duas coisas 1 do meu trabalho eu tô fazendo a minha parte e 2
37:34
a sua colaboração o seu compartilhamento é mostrar esse projeto por maior número de pessoas
37:40
a gente não trabalha só com curso avançado não é essa parte é mais avançadinho mas a gente tem curso de word por exemplo você pode mostrar se um
37:46
familiar seu primo de pressionar o canal quem sempre vai lançar a partir de agora a gestão série de curso em vídeo para usuários
37:53
pagar foi outros novos e gafanhotos iniciantes é isso aí meu querido a gente volta na semana que vem com mais uma
38:00
aula de sql caprichada pra você um forte abraço pratique você tem um exercício para fazer até a próxima
"""

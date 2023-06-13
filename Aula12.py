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

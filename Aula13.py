# Curso MySQL #13 - SELECT (Parte 3)
# https://youtu.be/ocyVJ9gRUaE
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/select-parte-2/

""" OBTENDO DADOS DAS TABELAS
- Estamos na 3ª aula sobre SELECT, e mesmo assim não vamos esgotar todos os usos do comando.
- Uma das últimas coisas, foi DISTINGUIR registros.
- Resolvemos explicar com uma outra ótica; E então poderemos trabalhar um novo tema: AGRUPAMENTO."""

# O DISTINCT vai considerar apenas uma ocorrência de cada valor dentro dos registros, ainda que sejam repetidas e múltiplas.

# Vamos AGRUPAR os valores, criando um grupo pra cada tipo de idade, por exemplo (então, quem tem a mesma idade fica no mesmo grupo).
# Na aula passada, nós usamos o DISTINGÜINDO, a saber:

SELECT DISTINCT carga FROM cursos
ORDER BY carga;
"""mysql> SELECT DISTINCT carga FROM cursos ORDER BY carga;
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
8 rows in set (0.88 sec)"""


# AGRUPANDO REGISTROS (Group By) nós poderemos não mais distingüir os valores, mas sim agrupá-los, criando conjuntos com as mesmas características.

SELECT carga FROM cursos
GROUP BY carga;
"""mysql> SELECT carga FROM cursos
    -> GROUP BY carga;
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
8 rows in set (0.00 sec)"""

# AGRUPANDO e AGREGANDO - vamos adicionar um parâmetro ao comando 'Group By' que acabamos de ver.
# Adicionar uma função de agregação (count(), sum(), min(), max(), avg() ) 

# Vamos SELECIONAR a carga, e a contagem dos (nomes) respectivos de cada carga, a partir da tabela cursos, agrupados por carga.
SELECT carga, COUNT(nome) FROM cursos 
GROUP BY carga;
"""mysql> SELECT carga, COUNT(nome) FROM cursos
    -> GROUP BY carga;
+-------+-------------+
| carga | COUNT(nome) |
+-------+-------------+
|    40 |           9 |
|    20 |           4 |
|    10 |           1 |
|    30 |           8 |
|    60 |           5 |
|    35 |           1 |
|    15 |           1 |
|    50 |           1 |
+-------+-------------+
8 rows in set (0.06 sec)"""


# Exemplos do Banco de Dados antigo:

SELECT * FROM cursos;
"""mysql> SELECT * FROM cursos;
+---------+--------------------+------------------------------------------------------+-------+----------+------+
| idcurso | nome               | descricao                                            | carga | totaulas | ano  |
+---------+--------------------+------------------------------------------------------+-------+----------+------+
|       1 | HTML5              | Curso de HTML5                                       |    40 |       37 | 2014 |
|       2 | Algoritmos         | Lógica de Programação                                |    20 |       15 | 2014 |
|       3 | Photoshop5         | Dicas de Photoshop CC                                |    10 |        8 | 2014 |
|       4 | PHP                | Curso de PHP para iniciantes                         |    40 |       20 | 2015 |
|       5 | Java               | Introdução à Linguagem Java                          |    40 |       29 | 2015 |
|       6 | MySQL              | Bancos de Dados MySQL                                |    30 |       15 | 2016 |
|       7 | Word               | Curso completo de Word                               |    40 |       30 | 2016 |
|       8 | Python             | Curso de Python                                      |    40 |       18 | 2017 |
|       9 | POO                | Curso de Programação Orientada a Objetos             |    60 |       35 | 2016 |
|      10 | Excel              | Curso completo de Excel                              |    40 |       30 | 2017 |
|      11 | Responsividade     | Curso de Responsividade                              |    30 |       15 | 2018 |
|      12 | C++                | Curso de C++ com Orientação a Objetos                |    40 |       25 | 2017 |
|      13 | C#                 | Curso de C#                                          |    30 |       12 | 2017 |
|      14 | Android            | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      15 | JavaScript         | Curso de JavaScript                                  |    35 |       18 | 2017 |
|      16 | PowerPoint         | Curso completo de PowerPoint                         |    30 |       12 | 2018 |
|      17 | Swift              | Curso de Desenvolvimento de Aplicativos para iOS     |    60 |       30 | 2019 |
|      18 | Hardware           | Curso de Montagem e Manutenção de PCs                |    30 |       12 | 2017 |
|      19 | Redes              | Curso de Redes para Iniciantes                       |    40 |       15 | 2016 |
|      20 | Segurança          | Curso de Segurança                                   |    15 |        8 | 2018 |
|      21 | SEO                | Curso de Otimização de Sites                         |    30 |       12 | 2017 |
|      22 | Premiere           | Curso de Edição de Vídeos com Premiere               |    20 |       10 | 2017 |
|      23 | After Effects      | Curso de Efeitos em Vídeos com After Effects         |    20 |       10 | 2018 |
|      24 | WordPress          | Curso de Criação de Sites com WordPress              |    60 |       30 | 2019 |
|      25 | Joomla             | Curso de Criação de Sites com Joomla                 |    60 |       30 | 2019 |
|      26 | Magento            | Curso de Criação de Lojas Virtuais com Magento       |    50 |       25 | 2019 |
|      27 | Modelagem de Dados | Curso de Modelagem de Dados                          |    30 |       12 | 2020 |
|      28 | HTML4              | Curso Básico de HTML, versão 4.0                     |    20 |        9 | 2010 |
|      29 | PHP7               | Curso de PHP, versão 7.0                             |    40 |       20 | 2020 |
|      30 | PHP4               | Curso de PHP, versão 4.0                             |    30 |       11 | 2010 |
+---------+--------------------+------------------------------------------------------+-------+----------+------+
30 rows in set (0.04 sec)"""


SELECT totaulas FROM cursos
ORDER BY totaulas;
"""mysql> SELECT totaulas FROM cursos
    -> ORDER BY totaulas;
+----------+
| totaulas |
+----------+
|        8 |
|        8 |
|        9 |
|       10 |
|       10 |
|       11 |
|       12 |
|       12 |
|       12 |
|       12 |
|       12 |
|       15 |
|       15 |
|       15 |
|       15 |
|       18 |
|       18 |
|       20 |
|       20 |
|       25 |
|       25 |
|       29 |
|       30 |
|       30 |
|       30 |
|       30 |
|       30 |
|       30 |
|       35 |
|       37 |
+----------+
30 rows in set (0.04 sec)"""


SELECT DISTINCT totaulas FROM cursos
ORDER BY totaulas;
"""mysql> SELECT DISTINCT totaulas FROM cursos
    -> ORDER BY totaulas;
+----------+
| totaulas |
+----------+
|        8 |
|        9 |
|       10 |
|       11 |
|       12 |
|       15 |
|       18 |
|       20 |
|       25 |
|       29 |
|       30 |
|       35 |
|       37 |
+----------+
13 rows in set (0.00 sec)"""


SELECT totaulas FROM cursos
ORDER BY totaulas
GROUP BY totaulas;
"""mysql> SELECT totaulas FROM cursos
    -> GROUP BY totaulas
    -> ORDER BY totaulas;
+----------+
| totaulas |
+----------+
|        8 |
|        9 |
|       10 |
|       11 |
|       12 |
|       15 |
|       18 |
|       20 |
|       25 |
|       29 |
|       30 |
|       35 |
|       37 |
+----------+
13 rows in set (0.00 sec)"""


SELECT totaulas, count(*) FROM cursos
GROUP BY totaulas
ORDER BY totaulas;
"""mysql> SELECT totaulas, count(*) FROM cursos
    -> GROUP BY totaulas
    -> ORDER BY totaulas;
+----------+----------+
| totaulas | count(*) |
+----------+----------+
|        8 |        2 |
|        9 |        1 |
|       10 |        2 |
|       11 |        1 |
|       12 |        5 |     <<<<<<<<<<<<
|       15 |        4 |
|       18 |        2 |
|       20 |        2 |
|       25 |        2 |
|       29 |        1 |
|       30 |        6 |      <<<<<<<<<<<<
|       35 |        1 |
|       37 |        1 |
+----------+----------+
13 rows in set (0.01 sec)"""


SELECT * FROM cursos
WHERE totaulas = '30';
"""mysql> SELECT * FROM cursos
    -> WHERE totaulas = '30';
+---------+-----------+------------------------------------------------------+-------+----------+------+
| idcurso | nome      | descricao                                            | carga | totaulas | ano  |
+---------+-----------+------------------------------------------------------+-------+----------+------+
|       7 | Word      | Curso completo de Word                               |    40 |       30 | 2016 |
|      10 | Excel     | Curso completo de Excel                              |    40 |       30 | 2017 |
|      14 | Android   | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      17 | Swift     | Curso de Desenvolvimento de Aplicativos para iOS     |    60 |       30 | 2019 |
|      24 | WordPress | Curso de Criação de Sites com WordPress              |    60 |       30 | 2019 |
|      25 | Joomla    | Curso de Criação de Sites com Joomla                 |    60 |       30 | 2019 |
+---------+-----------+------------------------------------------------------+-------+----------+------+
6 rows in set (0.08 sec)"""


SELECT * FROM cursos
WHERE totaulas = '12';
"""mysql> SELECT * FROM cursos
    -> WHERE totaulas = '12';
+---------+--------------------+---------------------------------------+-------+----------+------+
| idcurso | nome               | descricao                             | carga | totaulas | ano  |
+---------+--------------------+---------------------------------------+-------+----------+------+
|      13 | C#                 | Curso de C#                           |    30 |       12 | 2017 |
|      16 | PowerPoint         | Curso completo de PowerPoint          |    30 |       12 | 2018 |
|      18 | Hardware           | Curso de Montagem e Manutenção de PCs |    30 |       12 | 2017 |
|      21 | SEO                | Curso de Otimização de Sites          |    30 |       12 | 2017 |
|      27 | Modelagem de Dados | Curso de Modelagem de Dados           |    30 |       12 | 2020 |
+---------+--------------------+---------------------------------------+-------+----------+------+
5 rows in set (0.00 sec)"""


# Podemos também AGRUPAR utilizando condicionais como WHERE... Por exemplo, selecionar todos os registros dos cursos onde o total de aulas sejam maior que 20 aulas.
SELECT * FROM cursos WHERE totaulas > 20; 
"""mysql> SELECT * FROM cursos WHERE totaulas > 20;
+---------+-----------+------------------------------------------------------+-------+----------+------+
| idcurso | nome      | descricao                                            | carga | totaulas | ano  |
+---------+-----------+------------------------------------------------------+-------+----------+------+
|       1 | HTML5     | Curso de HTML5                                       |    40 |       37 | 2014 |
|       5 | Java      | Introdução à Linguagem Java                          |    40 |       29 | 2015 |
|       7 | Word      | Curso completo de Word                               |    40 |       30 | 2016 |
|       9 | POO       | Curso de Programação Orientada a Objetos             |    60 |       35 | 2016 |
|      10 | Excel     | Curso completo de Excel                              |    40 |       30 | 2017 |
|      12 | C++       | Curso de C++ com Orientação a Objetos                |    40 |       25 | 2017 |
|      14 | Android   | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      17 | Swift     | Curso de Desenvolvimento de Aplicativos para iOS     |    60 |       30 | 2019 |
|      24 | WordPress | Curso de Criação de Sites com WordPress              |    60 |       30 | 2019 |
|      25 | Joomla    | Curso de Criação de Sites com Joomla                 |    60 |       30 | 2019 |
|      26 | Magento   | Curso de Criação de Lojas Virtuais com Magento       |    50 |       25 | 2019 |
+---------+-----------+------------------------------------------------------+-------+----------+------+
11 rows in set (0.00 sec)""" 

# Eu posso querer adicionar somente aqueles resultados dos cursos que tenham 30 aulas.
SELECT * FROM cursos WHERE totaulas = '30';
"""mysql> SELECT * FROM cursos WHERE totaulas = '30';
+---------+-----------+------------------------------------------------------+-------+----------+------+
| idcurso | nome      | descricao                                            | carga | totaulas | ano  |
+---------+-----------+------------------------------------------------------+-------+----------+------+
|       7 | Word      | Curso completo de Word                               |    40 |       30 | 2016 |
|      10 | Excel     | Curso completo de Excel                              |    40 |       30 | 2017 |
|      14 | Android   | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      17 | Swift     | Curso de Desenvolvimento de Aplicativos para iOS     |    60 |       30 | 2019 |
|      24 | WordPress | Curso de Criação de Sites com WordPress              |    60 |       30 | 2019 |
|      25 | Joomla    | Curso de Criação de Sites com Joomla                 |    60 |       30 | 2019 |
+---------+-----------+------------------------------------------------------+-------+----------+------+
6 rows in set (0.00 sec)"""


# Podemos mostrar carga e o total de aulas, pra quem tem aulas = 30, agrupados por carga.
SELECT carga, COUNT(*) FROM cursos WHERE totaulas = '30' GROUP BY carga;
"""mysql> SELECT carga, COUNT(*) FROM cursos WHERE totaulas = '30' GROUP BY carga;
+-------+----------+
| carga | COUNT(*) |
+-------+----------+
|    40 |        2 |
|    60 |        4 |
+-------+----------+
2 rows in set (0.00 sec)"""


# O AGRUPAMENTO é mais que isso. Ele permite usar as Funções de Agregação em conjunto.

# Podemos selecionar quem eu quero agrupar (HAVING). 
# Vou selecionar a contagem (count) de cada valor de carga(40, 20, 30, 60) - agrupados por carga - que contenham mais de 3 registros.
SELECT carga, COUNT(nome) FROM cursos
GROUP BY carga
HAVING count(nome) > 3;
"""mysql> SELECT carga, count(nome) FROM cursos
    -> GROUP BY carga
    -> HAVING count(nome) > 3;
+-------+-------------+
| carga | count(nome) |
+-------+-------------+
|    40 |           9 |
|    20 |           4 |
|    30 |           8 |
|    60 |           5 |
+-------+-------------+
4 rows in set (0.00 sec)"""


# Selecionaremos as linhas dos anos, com as contagens agregadas, agrupados por ano, organizados por contagem, decrescente. 
SELECT ano, count(*) FROM cursos
GROUP BY ano
ORDER BY count(*) DESC;
"""mysql> SELECT ano, count(*) FROM cursos GROUP BY ano ORDER BY count(*) DESC;
+------+----------+
| ano  | count(*) |
+------+----------+
| 2017 |        8 |
| 2018 |        5 |
| 2016 |        4 |
| 2019 |        4 |
| 2014 |        3 |
| 2015 |        2 |
| 2020 |        2 |
| 2010 |        2 |
+------+----------+
8 rows in set (0.00 sec)"""


# Poderíamos agrupar somente aqueles que possuem um contador >= 5.
SELECT ano, count(*) FROM cursos
GROUP BY ano
HAVING count(ano) >= 5
ORDER BY count(*) DESC;
"""mysql> SELECT ano, count(*) FROM cursos GROUP BY ano HAVING count(ano) >= 5 ORDER BY count(*) DESC;
+------+----------+
| ano  | count(*) |
+------+----------+
| 2017 |        8 |
| 2018 |        5 |
+------+----------+
2 rows in set (0.00 sec)"""


# O HAVING está para o GROUP BY assim como, mais ou menos, o WHERE está para o SELECT.
# Dentro do HAVING somente podemos trabalhar com o campo que nós agrupamos. 
SELECT ano, count(*) FROM cursos
GROUP BY ano # Agrupamos por ANO, então... 
HAVING count(ano) >= 5 # Só podemos passar um HAVING que esteja listado, no caso ANO...
ORDER BY count(*) DESC;


SELECT ano, count(*) FROM cursos
GROUP BY ano
HAVING ano > 2013
ORDER BY count(*) DESC;
"""mysql> SELECT ano, count(*) FROM cursos GROUP BY ano HAVING ano > 2013 ORDER BY count(*) DESC;
+------+----------+
| ano  | count(*) |
+------+----------+
| 2017 |        8 |
| 2018 |        5 |
| 2016 |        4 |
| 2019 |        4 |
| 2014 |        3 |
| 2015 |        2 |
| 2020 |        2 |
+------+----------+
7 rows in set (0.00 sec)"""


# Eu estou selecionando os anos da tabela de cursos, onde o total de aulas sejam maior que 30, agrupando a seleção por ano, e só vou mostrar ano acima de 2013, ordenador pelo ano.
SELECT ano, count(*) FROM cursos
WHERE totaulas > 30
GROUP BY ano
HAVING ano > 2013
ORDE BY count(*) DESC;
"""mysql> SELECT ano, count(*) FROM cursos WHERE totaulas > 30 GROUP BY ano HAVING ano > 2013 ORDER BY count(*) DESC;
+------+----------+
| ano  | count(*) |
+------+----------+
| 2014 |        1 |
| 2016 |        1 |
+------+----------+
2 rows in set (0.00 sec)"""


# Vai me mostrar a média de horas dos cursos
SELECT avg(carga) FROM cursos;
"""mysql> SELECT avg(carga) FROM cursos;
+------------+
| avg(carga) |
+------------+
|    36.3333 |
+------------+
1 row in set (0.01 sec)"""


# Vamos selecionar todos os valores da tabela cursos com ano > 2015.
SELECT * FROM cursos
WHERE ano > 2015;
"""mysql> SELECT * FROM cursos
    -> WHERE ano > 2015;
+---------+--------------------+------------------------------------------------------+-------+----------+------+
| idcurso | nome               | descricao                                            | carga | totaulas | ano  |
+---------+--------------------+------------------------------------------------------+-------+----------+------+
|       6 | MySQL              | Bancos de Dados MySQL                                |    30 |       15 | 2016 |
|       7 | Word               | Curso completo de Word                               |    40 |       30 | 2016 |
|       8 | Python             | Curso de Python                                      |    40 |       18 | 2017 |
|       9 | POO                | Curso de Programação Orientada a Objetos             |    60 |       35 | 2016 |
|      10 | Excel              | Curso completo de Excel                              |    40 |       30 | 2017 |
|      11 | Responsividade     | Curso de Responsividade                              |    30 |       15 | 2018 |
|      12 | C++                | Curso de C++ com Orientação a Objetos                |    40 |       25 | 2017 |
|      13 | C#                 | Curso de C#                                          |    30 |       12 | 2017 |
|      14 | Android            | Curso de Desenvolvimento de Aplicativos para Android |    60 |       30 | 2018 |
|      15 | JavaScript         | Curso de JavaScript                                  |    35 |       18 | 2017 |
|      16 | PowerPoint         | Curso completo de PowerPoint                         |    30 |       12 | 2018 |
|      17 | Swift              | Curso de Desenvolvimento de Aplicativos para iOS     |    60 |       30 | 2019 |
|      18 | Hardware           | Curso de Montagem e Manutenção de PCs                |    30 |       12 | 2017 |
|      19 | Redes              | Curso de Redes para Iniciantes                       |    40 |       15 | 2016 |
|      20 | Segurança          | Curso de Segurança                                   |    15 |        8 | 2018 |
|      21 | SEO                | Curso de Otimização de Sites                         |    30 |       12 | 2017 |
|      22 | Premiere           | Curso de Edição de Vídeos com Premiere               |    20 |       10 | 2017 |
|      23 | After Effects      | Curso de Efeitos em Vídeos com After Effects         |    20 |       10 | 2018 |
|      24 | WordPress          | Curso de Criação de Sites com WordPress              |    60 |       30 | 2019 |
|      25 | Joomla             | Curso de Criação de Sites com Joomla                 |    60 |       30 | 2019 |
|      26 | Magento            | Curso de Criação de Lojas Virtuais com Magento       |    50 |       25 | 2019 |
|      27 | Modelagem de Dados | Curso de Modelagem de Dados                          |    30 |       12 | 2020 |
|      29 | PHP7               | Curso de PHP, versão 7.0                             |    40 |       20 | 2020 |
+---------+--------------------+------------------------------------------------------+-------+----------+------+
23 rows in set (0.00 sec)"""


# Posso agrupar por carga, no caso aquelas cargas com maior contagem (repetições).
SELECT carga, count(*) FROM cursos
WHERE ano > 2015
GROUPB BY carga;
"""mysql> SELECT carga, count(*) FROM cursos
    -> WHERE ano > '2015'
    -> GROUP BY carga;
+-------+----------+
| carga | count(*) |
+-------+----------+
|    30 |        7 |
|    40 |        6 |
|    60 |        5 |
|    35 |        1 |
|    15 |        1 |
|    20 |        2 |
|    50 |        1 |
+-------+----------+
7 rows in set (0.00 sec)"""


# E se, por exemplo, eu quiser dessa listagem mostrar apenas os cursos com horas ACIMA do valor médio dos cursos.
# Selecionar todos os cursos com ano > 2015, agrupado por carga, mas mostrar somente quem tem a carga > avg(carga).
SELECT carga, count(*) FROM cursos
WHERE ano > 2015
GROUP BY carga
HAVING carga > (select avg(carga) from cursos);
"""mysql> SELECT carga, count(*) FROM cursos
    -> WHERE ano > 2015
    -> GROUP BY carga
    -> HAVING carga > (select avg(carga) FROM cursos);
+-------+----------+
| carga | count(*) |
+-------+----------+
|    40 |        6 |
|    60 |        5 |
|    50 |        1 |
+-------+----------+
3 rows in set (0.07 sec)"""
# Ou seja, eu selecionei, filtrei e agrupei, e mostrei desse agrupamento, somente quem está acima do resultado de outro select.


# EXERCITANDO (agora com os gafanhotos)... 

# 1 - "Uma lista com as profissões dos gafanhotos e seus respectivos quantitativos."
# 2 - "Quantos gafanhotos homens e mulheres nasceram após 01-Jan-2005?"
# 3 - "Uma lista com os gafanhotos que nasceram fora do Brasil, mostrando o país de origem e o total de pessoas nascidas lá. Só nos interessam os países que tiverem mais de 3 gafanhotos com essa nacionalidade."
# 4 - "Uma lista agrupada pela altura dos gafanhotos, mostrando quantas pessoas pesam mais de 100 kg e que estão acima da média de altura de todos os cadastrados."


# 1 - "Uma lista com as profissões dos gafanhotos e seus respectivos quantitativos."
SELECT DISTINCT profissao, FROM gafanhotos;

SELECT DISTINCT profissao, count(*) FROM gafanhotos
GROUP BY profissao
ORDER BY count(*) DESC;
"""mysql> SELECT DISTINCT profissao, count(*) FROM gafanhotos GROUP BY profissao ORDER BY count(*) DESC;
+----------------------+----------+
| profissao            | count(*) |
+----------------------+----------+
| Programador          |       16 |
| Auxiliar Administrat |       13 |
| Professor            |        7 |
| Dentista             |        7 |
| Empreendedor         |        7 |
| Ator                 |        6 |
| Médico               |        3 |
| Farmacêutico         |        2 |
+----------------------+----------+
8 rows in set (0.00 sec)"""


# 2 - "Quantos gafanhotos homens e mulheres nasceram após 01-Jan-2005?"
SELECT * FROM gafanhotos WHERE nascimento > '2005-01-01';

SELECT DISTINCT sexo, count(*) FROM gafanhotos
WHERE nascimento > '2005-01-01'
GROUP BY sexo
ORDER BY count(*) DESC;
"""mysql> SELECT DISTINCT sexo, count(*) FROM gafanhotos WHERE nascimento > '2005-01-01' GROUP BY sexo ORDER BY count(*) DESC;
+------+----------+
| sexo | count(*) |
+------+----------+
| M    |        8 |
| F    |        2 |
+------+----------+
2 rows in set (0.00 sec)"""


# 3 - "Uma lista com os gafanhotos que nasceram fora do Brasil, mostrando o país de origem e o total de pessoas nascidas lá. Só nos interessam os países que tiverem mais de 3 gafanhotos com essa nacionalidade."
SELECT * FROM gafanhotos WHERE nacionalidade != 'Brasil';
SELECT DISTINCT nacionalidade FROM gafanhotos WHERE nacionalidade <> 'Brasil';    
SELECT DISTINCT nacionalidade, count(*) FROM gafanhotos WHERE nacionalidade != 'Brasil' GROUP BY nacionalidade ORDER BY count(*) DESC;
SELECT DISTINCT nacionalidade, count(*) FROM gafanhotos WHERE nacionalidade <> 'Brasil' GROUP BY nacionalidade HAVING count(nacionalidade) >= 3 ORDER BY count(*) DESC;
"""mysql> SELECT DISTINCT nacionalidade, count(*) FROM gafanhotos
    -> WHERE nacionalidade <> 'Brasil'
    -> GROUP BY nacionalidade
    -> HAVING count(nacionalidade) >= 3
    -> ORDER BY count(*) DESC;
+---------------+----------+
| nacionalidade | count(*) |
+---------------+----------+
| Portugal      |        8 |
| EUA           |        8 |
| Canadá        |        4 |
| Angola        |        4 |
| Moçambique    |        3 |
| Irlanda       |        3 |
+---------------+----------+
6 rows in set (0.00 sec)"""


# 4 - "Uma lista agrupada pela altura dos gafanhotos, mostrando quantas pessoas pesam mais de 100 kg e que estão acima da média de altura de todos os cadastrados."
SELECT avg(altura) FROM gafanhotos;
SELECT * FROM gafanhotos;
SELECT DISTINCT altura FROM gafanhotos GROUP BY altura ORDER BY altura;
SELECT avg(altura) FROM gafanhotos;
"""mysql> SELECT * FROM gafanhotos
    -> WHERE peso > 100
    -> GROUP BY altura
    -> HAVING altura > (SELECT avg(altura) FROM gafanhotos)
    -> ORDER BY altura DESC;
+----+--------------------+----------------------+------------+------+--------+--------+---------------+
| id | nome               | profissao            | nascimento | sexo | peso   | altura | nacionalidade |
+----+--------------------+----------------------+------------+------+--------+--------+---------------+
| 29 | Tiago Ulisses      | Dentista             | 1993-04-22 | M    | 150.30 |   2.35 | Brasil        |
| 17 | Paulo Narley       | Auxiliar Administrat | 1997-03-17 | M    | 120.10 |   2.22 | Brasil        |
| 59 | Philppe Oliveira   | Auxiliar Administrat | 2000-05-23 | M    | 105.10 |   2.19 | Brasil        |
| 37 | Daniele Moledo     | Empreendedor         | 2006-08-11 | F    | 101.30 |   1.99 | Brasil        |
| 22 | Guilherme de Sousa | Dentista             | 2001-05-18 | M    | 132.70 |   1.97 | Moçambique    |
| 26 | Paulo Batista      | Ator                 | 1999-03-15 | M    | 110.12 |   1.87 | Portugal      |
| 36 | Robson Rodolpho    | Auxiliar Administrat | 2000-08-08 | M    | 110.10 |   1.76 | Brasil        |
+----+--------------------+----------------------+------------+------+--------+--------+---------------+
7 rows in set (0.00 sec)"""

"""mysql> SELECT nome, altura, peso FROM gafanhotos
    -> WHERE peso > 100
    -> GROUP BY altura
    -> HAVING altura > (SELECT avg(altura) FROM gafanhotos)
    -> ORDER BY altura DESC;
+--------------------+--------+--------+
| nome               | altura | peso   |
+--------------------+--------+--------+
| Tiago Ulisses      |   2.35 | 150.30 |
| Paulo Narley       |   2.22 | 120.10 |
| Philppe Oliveira   |   2.19 | 105.10 |
| Daniele Moledo     |   1.99 | 101.30 |
| Guilherme de Sousa |   1.97 | 132.70 |
| Paulo Batista      |   1.87 | 110.12 |
| Robson Rodolpho    |   1.76 | 110.10 |
+--------------------+--------+--------+
7 rows in set (0.00 sec)"""





"""

"""

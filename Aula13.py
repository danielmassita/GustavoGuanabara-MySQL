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
Transcrição


Procurar no vídeo
0:19
olá pequeno gafanhoto seja bem vindo a
0:22
mais uma aula do seu curso de banco de
0:24
dados como sql do curso em vídeo o meu
0:26
nome é gustavo guanabara eu sou
0:28
professor e chegamos a mais uma aula de
0:30
banco de dados e vamos dar continuidade
0:32
ao assunto que a gente estava tratando
0:33
na aula anterior de como obter dados das
0:36
tabelas
0:37
utilizando como o select e essa é a
0:39
terceira aula a tratar sobre o comando
0:41
select é meu querido fazia idéia de como
0:44
o select era grande mas não sabia que
0:45
tinha tanta coisa assim né
0:47
e pode acreditar em mim a gente não viu
0:48
tudo e nem vai ver tudo que o select
0:51
pode fazer mas ainda falta um bocadinho
0:52
fica tranquilo relaxa e você que está
0:55
chegando agora e está procurando saber
0:56
um pouco mais sobre select saiba que
0:58
essa é a terceira aula sobre o comando
1:01
ea décima terceira aula de um curso que
1:04
já está em andamento então se você clica
1:06
aqui ó
1:06
você vai diretamente para o curso
1:07
completo então não perca a oportunidade
1:09
de acompanhar o curso de banco de dados
1:11
completo é completa não tem aquela
1:14
historinha de olha assistir quatro aulas
1:15
aqui depois você vai ser desviado por um
1:17
site que você vai ter que pagar para
1:19
poder assistir as outras não meu querido
1:21
aqui todas as aulas são gratuitas e com
1:24
qualidade e se você se lembra da aula
1:26
passada uma das coisas que a gente viu
1:28
no select uma das últimas coisas foi
1:30
distinguir registros
1:32
eu sei que muita gente ficou confuso com
1:33
isso e eu resolvi explicar sobre uma
1:35
outra ótica
1:36
dá uma olhada aqui que com certeza se
1:38
ficou dúvida dá uma passada ela vai
1:40
subir agora e esse conceito é muito
1:41
importante para você poder entender o
1:43
que eu vou falar nessa aula que é sobre
1:45
agrupamentos então na aula passado a
1:47
gente falou sobre distinção ea palavra
1:49
distinct era utilizada para isso vamos
1:52
imaginar a seguinte situação
1:53
nós temos essa fila de pessoas e eu
1:55
pergunto qual é a idade de todas elas
1:57
elas vão responder rapidamente todo
2:02
mundo responde aí
2:05
obrigado criança maldita se você
2:07
perceber na sua tela
2:08
várias pessoas têm idades iguais se eu
2:11
utilizar o comando distinct
2:13
distinguir elas vão vir aqui como
2:15
exemplo por exemplo aqui ó separei em
2:16
dois grupos se você perceber ali o
2:18
primeiro da esquerda tem 65 anos
2:20
então do lado direito eu vou eliminar
2:22
quem tenha 65 anos
2:23
o segundo menino a criança maldita em
2:26
três anos eu vou eliminar também todo
2:28
mundo que tem a idade igual a ele
2:29
o próximo tem 32 anos eu vou eliminar
2:32
todo mundo que também tenha 32 anos
2:34
isso porque eu estou distinguindo-o diz
2:37
ti ti ti é exatamente isso que expliquei
2:38
na aula passada ele vai considerar
2:40
apenas uma ocorrência de cada valor
2:43
dentro do registro isso porque para a
2:45
distinção não importa a quantidade ou o
2:47
tipo de pessoas
2:48
o que importa são apenas os valores
2:50
ficou claro ele vai simplesmente pegar
2:53
olha só
2:54
desse grupo de gente se utilizar um
2:55
distinto lá para selecionar os registros
2:57
por unidade
2:58
ele vai pegar todo mundo que tem a mesma
3:00
idade vai pegar somente uma ocorrência e
3:02
vai jogar o resto tudo fora e eu não vou
3:04
dizendo aqui que o distingue é inútil
3:06
simplesmente estou dizendo me importa
3:08
mais saber quais são as cidades se você
3:11
tem por exemplo um curso e você tem
3:13
muitos alunos cadastrados e você quer
3:15
saber em que bairros os seus alunos
3:16
moram se você é select bairro foram
3:19
alunos
3:19
você vai ver todos os bairros inclusive
3:21
com repetições mas eu quero uma lista de
3:23
bairros guanabara beleza o distingue na
3:26
frente ele vai selecionar somente os
3:28
bairros
3:28
então assim não é que distingue que seja
3:30
inútil é porque às vezes eu preciso
3:32
fazer uma coisa e eu não consigo e essa
3:34
coisa é agrupar essas pessoas
3:37
vamos imaginar a mesma situação todo
3:39
mundo com a sua idade aí até mesmo a
3:41
criança maldita já falou dela o que eu
3:43
vou fazer aqui agora em vez de
3:44
distinguir eu vou agrupá-los perceba aí
3:48
agora eu agrupei eles por idade criando
3:51
um grupo para cada tipo de idade recebem
3:54
ó eu tenho pessoas com 65 anos pessoas
3:57
com três anos pessoas com 32 anos e uma
3:59
pessoa no canto com 30 anos
4:01
então eu estou agrupando não
4:03
distinguindo são duas operações que você
4:06
pode fazer com o select isso vai
4:07
depender do que você queira fazer
4:09
fica claro então vamos voltar para os
4:11
exemplos da aula passada na aula passada
4:13
se você se lembra muito bem a gente
4:15
tinha aquela tabela com 10 registros e
4:17
utiliza o comando select distintos de
4:19
carga foram cursos order by carga
4:21
então ele vai selecionar todas as cargas
4:23
só que ele vai querer as distintas
4:26
e aí eu tenho
4:26
aqui ó eu tenho vários cursos que têm
4:29
carga horária de 40 como você acabou de
4:31
ver aqui ele vai simplesmente pegar só o
4:33
primeiro aquele html5 e vai ignorar
4:36
todos os outros
4:38
você percebe nesses quadradinhos verdes
4:40
quais foram selecionados
4:42
então ele vai gerar uma listagem com
4:44
todas as cargas possíveis
4:46
no meu caso ali ordenado por carga então
4:48
você pode analisar da seguinte maneira
4:50
eu tenho cursos com carga horária de
4:52
cinco dez 20 30 e 40 horas dentro dos
4:56
meus cursos cadastrados e o que importa
4:58
aqui mais uma vez são apenas os números
5:00
não me importa saber quantos cursos têm
5:03
40 horas/aula guanabara e se importar
5:05
saber quantos cursos têm aí você não
5:08
pode distinguir aí você tem que agrupá e
5:10
agrupá é extremamente simples você vai
5:13
fazer o seguinte select carga foram
5:14
cursos e no lugar de utilizar o
5:17
distinguished antes da carga
5:18
você vai utilizar o grupo bae carga
5:20
grupo bairro significa agrupado por
5:23
então vou selecionar as duplas os
5:26
registros agrupados por carga exatamente
5:29
como eu fiz com a idade das pessoas no
5:30
exemplo anterior o que eu vou gerar é o
5:32
seguinte eu tenho aí grupos o grupo
5:34
verde é o que tem mais registros de
5:36
todas as outras cargas tem apenas uma
5:38
ocorrência eu tenho lá sim o azulzinho
5:40
10 o vermelhinho 21 roxo e amarelo com
5:44
30 fazendo esse agrupamento o resultado
5:46
vai ser esse
5:47
as cargas 40 2010 35 tá mas o resultado
5:52
foi exatamente o mesmo
5:53
não exatamente pequeno gafanhoto agora
5:56
os registros eles foram agrupados não
5:58
distinguidos o resultado visual na sua
6:01
tela nesse momento pode até ter sido
6:03
parecido mas ele está longe de ser igual
6:05
distinct vamos ver um outro exemplo aqui
6:07
vamos adicionar um parâmetro aquele
6:09
comando que a gente acabou de ver então
6:10
comandante acabou de ver é select carga
6:12
foram cursos grupo vai carga o que eu
6:14
vou fazer o seguinte eu vou adicionar
6:16
uma função de agregação que a gente viu
6:18
na aula passada lembra dela passada a
6:20
gente viu o cat o sã o avg 1min o max dá
6:25
pra usar tudo isso utilizando
6:27
agrupamento do sql então nós vimos
6:29
anteriormente o resultado desse comando
6:30
é esse daí os arquivos foram poupados e
6:33
selecionados aparecendo na tela apenas
6:35
uma vez
6:35
vamos agora adicionar um parâmetro
6:37
utilizando uma função de agregação co
6:40
por exemplo o counter nome o counter
6:42
como você já viu ele conta quantos
6:44
registros ocorreram se os seus registros
6:46
estão agrupados
6:47
ele permite que você conte quantos
6:49
registros estão agrupados também dá uma
6:51
olhada aqui
6:52
sendo assim ele vai criar mais uma
6:53
coluna com o county e como você vai
6:55
interpretar isso dá uma olhada na tabela
6:57
da esquerda e da direita enquanto os
6:59
quadradinhos verde você encontra seis
7:01
não é mesmo
7:02
olha agora para a tabela da direita eu
7:04
tenho seis cursos de 40 horas
7:07
eu tenho um curso de 20 horas um curso
7:09
de 10 horas um curso de 30 horas e um
7:11
curso de cinco horas
7:13
e aí gostou vamos partir para o nosso
7:15
ambiente do work bent e ver como
7:17
funciona na prática
7:19
então já estou aqui no rock band meu
7:22
servidor já está ativo
7:23
eu vou dar aqui ó select asterístico
7:25
from cursos contra o inter ele já me deu
7:30
aqui todos os cursos selecionados numa
7:33
listagem aqui ó
7:35
eu tenho todos os 30 cursos se eu
7:38
colocar pra mostrar pote aulas
7:40
ele vai mostrar que eu tenho 37 aulas 15
7:43
8 20
7:44
vamos ordenar que também então eu tenho
7:46
dois cursos com oito aulas dos cursos
7:50
com dez aulas um monte de curso com 12
7:53
aulas mais um monte com 15 e assim
7:56
sucessivamente
7:57
se você quiser distingui-los você pode
7:59
colocar distinct agora eu tenho uma
8:02
listagem do total de aulas de cada curso
8:06
o problema é que eu não consigo saber
8:07
quantos cursos têm 8 quando os cursos
8:09
têm nove eu só sei que existem cursos
8:11
com oito existem cursos com 9 para saber
8:13
a quantidade
8:14
eu não posso distinguir los eu tenho que
8:16
agrupá los
8:17
então falei aqui ó vamos agrupar por
8:19
total de aulas
8:20
o resultado vai ser exatamente o mesmo
8:23
serviu como era antigamente como está
8:25
agora é exatamente igual pode voltar o
8:27
vídeo que está exatamente igual
8:28
o que eu vou fazer agora é além de
8:31
agrupar totaliza los por exemplo a um
8:35
cateterismo
8:36
só eu quero contar quantos registros têm
8:39
dentro de cada agrupamento aqui ó
8:42
eu tenho com oito aulas eu tenho dois
8:45
cursos com dez aulas eu tenho dois
8:47
cursos com 11 com 12 aulas eu tenho
8:50
cinco lembra do que a gente tinha muito
8:52
curso com 12 aulas muito
8:54
curso com 15 aulas e eu tenho também
8:56
muito curso com 30 aulas quer ver aqui
8:58
vamos selecionar ó eu quero selecionar
9:02
asterístico from cursos
9:05
o é totti aulas igual a 30
9:11
ele vai ter que mostrar seus registros
9:13
lá exatamente seis registros word excel
9:17
android suíte wordpress e dilma todos
9:20
eles têm 30 aulas e isso se reflete na
9:24
quele comando anterior com 30 aulas
9:27
eu tenho seis cursos vão fazer sua prova
9:29
final vamos ver quantos têm 12 aulas
9:32
ele tem que mostrar cinco cursos vamos
9:34
ver aqui ó select a chevron cursos onde
9:37
aula seja 12 contra o enter
9:40
lá eu tenho seis sharp powerpoint
9:42
hardware s ou e modelagem de dados
9:47
eu tenho cinco cursos aqui exatamente o
9:50
resultado que eu tinha com 12 aulas
9:53
cinco curso eu pra entender pra que
9:56
serve o agrupamento e você pode agrupar
9:58
utilizando o e também por exemplo eu
10:00
quero selecionar todos os registros dos
10:03
cursos onde o total de aulas seja maior
10:06
que 30
10:08
então eu quero somente nos cursos que
10:10
têm mais de 30 aulas
10:11
então eu tenho somente dois cursos com
10:14
mais de 30 aulas vão botar mais que 20
10:16
a primeira mais registros aqui eu tenho
10:18
esses cursos aqui com mais de 20 aulas
10:22
você percebe aqui que vários tem 40
10:24
horas
10:25
então eu falei o seguinte vamos ver aqui
10:27
eu tenho aqui vários cursos com 30 aulas
10:29
aqui ó 30 aulas com 30 aulas 30 30 e 31
10:36
alguns têm 40 horas de carga outras têm
10:39
60 horas de carga eu quero selecionar
10:41
somente aqueles que têm 30 aulas
10:45
não vou colocar aqui onde o curso tenha
10:48
30 aulas ataque somente de 30 aulas e
10:53
você vê que tem alguns que tem 40 e
10:55
alguns que tem 60
10:57
eu posso agrupá-los também por isso não
10:59
posso mandar mostrar aqui ó
11:01
quero mandar mostrar carga e o total de
11:04
aulas
11:06
pra quem tem aulas igual a 30
11:10
agrupados por carga ó
11:16
ele vai mostrar eu tenho 40 horas 60
11:19
horas todos eles têm o total de aulas de
11:21
30 anos estava em mostrar o total de
11:23
aulas aqui né
11:24
não tenho desse grupo que atende eu
11:26
tenho cursos com 40 cursos com 60
11:29
se eu quiser saber quantos vêm aqui ó
11:31
county register isco para o atacar onde
11:35
qualquer campo aqui há um nome quanto os
11:39
nomes de cursos têm essa carga e atende
11:42
todas essas características
11:44
então dá uma olhadinha no comando eu
11:46
estou selecionando quero mostrar a carga
11:48
e quantos cursos têm na tabela cursos
11:52
que tenham total de aula igual a 30 mas
11:55
eu quero agrupar por carga
11:57
então vamos ver eu tenho cursos de 40
11:59
horas de curso de 60 horas
12:01
quantos dois cursos de 44 cursos com 60
12:05
horas
12:06
vamos ver exatamente isso então ou
12:09
select asterisco concursos ou selecionar
12:13
todas as colunas de cursos onde o total
12:17
de aulas seja igual a 30
12:19
então ele tem que mostrar dois cursos de
12:22
44 cursos de 60
12:24
vamos ver eu tenho dois cursos com 40 e
12:29
eu tenho um dois três quatro cursos com
12:33
60 exatamente o resultado que esse
12:36
comando está me dando dois cursos de 44
12:39
cursos com 60 horas
12:41
tranquilo gostou assim o agrupamento é
12:44
mais que isso
12:45
o mais legal do agrupamento é você
12:47
conseguir utilizar as funções de
12:49
agregação em conjunto com ele mas não
12:51
para por aí não
12:52
você pode selecionar quem você pode
12:54
agrupar um exemplo disso vai vir aqui
12:56
agora eu tenho select carga continha o
12:59
nome foi um curso o grupo vai cargo
13:00
exatamente o que tinha antes
13:02
isso vai gerar aquele resultado que a
13:03
gente viu antes ele vai selecionar
13:05
quando as cargas são vai agrupar e vai
13:07
totalizar só que eu quero é o seguinte
13:09
eu não quero mostrar todos
13:11
eu quero mostrar os agrupados somente
13:14
quem tem heaven o counter nome maior que
13:18
3
13:18
então por exemplo ali eu
13:20
tenho um curso com 51 curso com 30 um
13:23
curso com 10 um curso com 20
13:25
mas eu tenho seis cursos com 40 eu quero
13:28
mostrar somente quem tem o contador
13:31
maior que 3
13:32
então só vou mostrar quem tem 40 horas
13:35
eu tenho seis cursos e aí deu pra
13:38
entender
13:39
ficou confuso vamos diretamente com o
13:41
ambiente e esse martelo não me deixa
13:44
vocês perceberam que agora tem uma
13:45
furadeira também eu estou tentando
13:46
ignora
13:47
eu já limpei aqui vamos dar um select
13:50
asterístico from cursos têm todos esses
13:55
cursos vão agrupar por exemplo por ano
13:58
o grupo bae ano a mostrar aqui o ano e o
14:10
county register stico olha só vamos
14:14
ordenar aqui ordem by renault master
14:22
está pra você ordenar também por uma
14:24
coluna que ó então em 2021 tem dois
14:27
cursos em 2010 dois cursos onde tive
14:30
mais curso a 2017 com oito cursos você
14:33
quiser inverso
14:34
você pode botar 10 que aqui ele vai te
14:36
mostrar do maior para o menor então em
14:38
2017 foi onde eu fiz ou farei será que é
14:42
verdade isso não sei mais cursos com
14:45
oito 2018 com 5.016 com 4 e assim
14:50
sucessivamente
14:51
e se eu quiser agrupar somente quem tem
14:54
esse contador acima de 5 por exemplo
14:58
contando 5
14:59
eu quero ver só isso aqui ó eu quero
15:01
saber quais os anos eu tenho maior
15:02
incidência de cursos
15:04
então eu vou fazer o seguinte aqui ó
15:05
heaven o counter ano maior ou igual a 5
15:14
contra o inter
15:16
lá ele me selecionou em vez de mostrar
15:18
todo seu só agrupei quem tem o carro
15:22
deste ano maior ou igual a 5
15:24
o heaven para o grupo bayer é mais ou
15:26
menos semelhante ao é o select e uma
15:29
coisa importante dentro do heaven você
15:31
só pode trabalhar com o cão
15:33
o que você acha grupo ficou confuso ct
15:36
dar um exemplo
15:36
então eu agrupei por ano e eu não posso
15:39
por exemplo mostrar nesse ano todo mundo
15:42
que tem sei lá o total de aulas maior do
15:46
que 30
15:47
se eu pudesse comando ele vai mostrar um
15:49
erro aqui dizendo que ele não conhece o
15:52
ano com volume total las em heavy cross
15:55
então ele não conhece o trote aulas
15:57
porque você não há grupo por eles mas se
15:59
você quiser saber por exemplo eu quero
16:01
agrupar por ano que tenha o ano maior do
16:04
que sei lá 2013
16:08
ele também vai mostrar todo mundo que
16:10
tem um ano somente acima de 2013 e que
16:12
não têm os anos anteriores não tenham
16:14
por exemplo votar 2016 aqui realmente
16:17
que seja maior 2016
16:18
ele me mostrou somente eles não me
16:20
mostram anterior então o heaven ele só
16:22
funciona se aqui eu colocar o campo que
16:26
eu utilizei diretamente no grupo vai mas
16:28
nada impede que você utilizar outro
16:30
campo aqui ó por exemplo com o é
16:32
não quero selecionar ó onde o total de
16:36
aulas foi maior do que 30 por exemplo
16:39
ele vai agrupar aquele não mostrou
16:42
nenhum maior que 2013
16:47
agora eu tenho o que eu estou fazendo
16:48
aqui estou selecionando os anos da
16:51
tabela de cursos onde o total de aulas
16:53
seja acima de 30 só quero selecionar
16:55
esses vou agrupar essa seleção por ano e
16:58
dentro desse agrupamento eu só vou
17:00
mostrar quem tem ano acima de 2013
17:02
ordenado pelo total aqui deu pra
17:04
entender
17:05
você pode selecionar filtrar agrupar e
17:09
dizer dentro desse grupamento qual você
17:11
quer exibir aí você usa o select o é o
17:15
grupo bae e o heaven
17:16
se isso se torna confuso pra você você
17:18
precisa praticar um pouco mais
17:20
eu trouxe quatro exercícios aqui pra
17:22
você fazer no finalzinho da aula
17:24
mas antes eu tenho que mostrar uma coisa
17:25
bem legal você pode juntar tudo aqui
17:27
desse jeito você pode juntar mais ainda
17:30
por exemplo aqui ó responder essa janela
17:32
de baixo
17:33
é só você clicar aqui no cantinho né
17:35
fazer o seguinte aqui ó select avg carga
17:41
from cursos que ele vai fazer aqui ele
17:45
vai mostrar
17:46
média de horas dos cursos então o que eu
17:49
fiz aqui
17:50
o valor que foi exibido foi 36.3 isso
17:53
significa de todos os cursos que eu
17:55
tenho ele somou todas as cargas e
17:57
dividir pelo número de cursos e mostrou
17:59
seu valor
18:00
então em média os meus cursos que eu
18:02
lancei até hoje tem 36 horas de duração
18:05
agora vou fazer outros electric select
18:09
asterisco concursos
18:12
o é lá ano maior do que 2013
18:18
mandei mostrar aqui todos os campos de
18:20
quem dos cursos que foram feitos depois
18:22
de 2003 2013 não não vai dar muito 2015
18:26
não tenho alguns cursos aqui todos eles
18:29
feitos depois de 2015
18:30
posso vir aqui e agrupar por carga por
18:34
exemplo
18:34
então eles vão ficar agrupados por cada
18:37
quero mostrar a carga e o counter isso é
18:42
de cursos acima de 2015
18:45
eu tenho dois cursos com 20 horas sete
18:48
cursos com 30 horas e por aí vai
18:51
mas se por exemplo se eu quiser dessa
18:53
listagem mostrará apenas os cursos que
18:56
têm horas acima da média de horas de
18:58
todos os cursos
18:59
ficou claro que estou falando olha só eu
19:01
tenho a média de horas 36.6 eu quero
19:03
mostrar essa listagem somente os cursos
19:05
que têm a carga acima dessa média
19:08
é claro que eu posso vir calcular 36.6
19:11
vir aqui fazer o meu select utilizando
19:13
36.6 mas seu cadastro de novos cursos ea
19:16
média mudar toda hora vou ter que ir lá
19:18
ficar calculando a média para depois
19:19
mudar o meu select não precisa pequeno
19:21
gafanhoto você pode juntar um selecto no
19:23
outro e é isso que vou te mostrar agora
19:25
então eu quero selecionar todos os
19:27
cursos que tenham ano acima de 2015
19:30
vou agrupar por carga mas eu só quero
19:32
mostrar quem tem a carga percebe o
19:37
heaven está utilizando o mesmo campo do
19:39
grupo vai acima de 36 pontos seis só que
19:44
se eu botar 36 pontos aqui ea média de
19:46
cargas mudar eu vi vou ter que vir aqui
19:49
toda hora e modificar
19:50
então eu vou fazer o seguinte vou botar
19:52
um parêntese aqui dentro vou vir aqui ó
19:54
copiar e select inteiro control c
19:58
eu vim aqui dentro contra o v
20:00
isso é eu estou selecionando a carga eo
20:03
total de horas dos cursos onde o ano
20:06
seja acima de 2015
20:08
vou agrupá los por carga exatamente como
20:10
estou fazendo aqui mas eu não quero
20:12
mostrar quem tem carga baixa eu quero
20:14
mostrar somente quem está acima da carga
20:17
então por exemplo sem a carga 36.5 esses
20:20
caras aqui ó não vão aparecer vai
20:22
aparecer somente esses três aqui de
20:24
baixo
20:25
será que vai acontecer vamos dar contra
20:27
o enter ela
20:28
ele só me mostrou aqueles três de baixo
20:31
isso é eu selecionei phil trey agrupei e
20:38
mostrei desse agrupamento
20:40
somente quem está acima do resultado de
20:43
outros select oi meu querido
20:47
isso é confuso se você não entendeu
20:49
direito a assistir aula de novo essa
20:51
aula não é pra assistir uma vez só essa
20:53
é uma aula daquelas que você tem que
20:55
assistir mais uma vez tem que estar com
20:57
o computador ligado
20:58
não adianta ficar a meu deus eu não
21:01
estou entendendo nada demais que 'ele
21:03
não vai entender meu querido se você não
21:06
botar a mão na massa não tirar essa mãe
21:07
do seu queixo e botar a mão na massa
21:09
você não vai entender isso é complicado
21:12
sim é confuso é mas é legal pra
21:16
então eu tentando demostrar é que o
21:18
comando select é poderosíssimo
21:20
você pode unir um com o outro juntar
21:22
utilizam select dentro de outro ele é
21:25
poderoso e volto a dizer não vou ter
21:27
como ensinar tudo que o select faz até
21:29
porque senão seria o curso em vídeo de
21:31
select mas concorda comigo que eu te
21:33
mostrando é muito mais do que muito
21:35
curso é que você faz inclusive os pagos
21:37
então pra exemplificar para exercitar
21:40
aquilo que você aprendeu nessa aula
21:42
vamos a quatro exercícios que eu separei
21:44
caprichados aqui pra você
21:46
vamos então exercitar como sempre
21:48
estamos fazendo nas últimas aulas e o
21:50
primeiro exercício é o seguinte eu quero
21:52
uma lista com as profissões dos
21:54
gafanhotos e seus respectivos
21:56
quantitativos
21:57
então eu fiz uns elektra tabela de
21:59
cursos agora você vai trabalhar com a
22:01
tabela de gafanhotos
22:02
eu quero uma lista com todas as
22:04
profissões e seus respectivos
22:05
quantitativos então por exemplo eu quero
22:07
saber
22:08
dentro dos gafanhotos cadastrados
22:10
quantos são programadores quantos são
22:12
analistas quanto são professores
22:14
e assim sucessivamente essa é fácil né
22:16
então ó pausa o vídeo abre seu ambiente
22:20
importa base de dados já ensinei a fase
22:22
antes nos nas aulas anteriores e prática
22:25
senão não vai adiantar o que eu sempre
22:28
vou te pedir o seguinte prática faz
22:30
quatro exercícios e coloca a resposta
22:32
aqui nos comentários
22:33
vamos fazer a troca de informações entre
22:35
gafanhotos
22:37
vamos ver quem acerta quem erra quem não
22:39
entendeu o gabarito vai tá aqui embaixo
22:41
não sou eu que vou botar são os próprios
22:42
gafanhotos então não confie 100% você
22:45
ler
22:46
pratique e vez está funcionando o
22:47
segundo exercício é um pouquinho mais
22:49
complexo mas mesmo assim é fácil eu
22:51
quero saber quanto de gafanhotos homens
22:54
e quantos gafanhotos mulheres nasceram
22:56
após 1º de janeiro de 2005 então o
22:59
seguinte eu quero primeiro saber quantas
23:00
pessoas nasceram acima de 1º de janeiro
23:03
de 2005 e select é fácil de fazer
23:06
depois eu quero agrupá los por sexo e
23:09
ver quantos homens enquanto as mulheres
23:11
nasceram
23:12
atendendo a essa expectativa que de ter
23:14
nascido após dia 1º de janeiro de 2005
23:18
essa também é moleza vamos melhorar um
23:20
pouquinho mais mas nunca se esqueça
23:22
pause e faço exercício dois não deixa
23:24
para ouvir três agora não eu tô
23:26
esperando talvez aí e agora que você fez
23:31
eu espero que você tenha feito vamos ao
23:32
terceiro exercício
23:34
o terceiro é um pouco mais complexo eu
23:36
quero uma lista com os gafanhotos que
23:38
nasceram fora do brasil mostrando o país
23:40
de origem eo total de pessoas nascidas
23:42
lá vão parar por aqui
23:44
olha só eu não quero quem mora no brasil
23:46
então eu quero selecionar quem está fora
23:48
do brasil
23:49
eu expliquei isso também nas aulas de
23:51
operadores e aí eu quero uma lista de
23:53
países de origem e quantas pessoas moram
23:56
lá
23:56
eu quero saber quantas pessoas moram no
23:58
canadá quantas pessoas moram nos estados
23:59
unidos quando as pessoas morrem em
24:01
moçambique quantas pessoas moram no
24:02
congo então sim eu quero saber quantas
24:04
pessoas moram em cada um dos países que
24:07
não sejam brasil não quero saber quantas
24:09
pessoas moram no brasil e ainda tem um
24:11
adicional só nos interessam os países
24:13
que tiverem mais de 3 já foi outros com
24:15
essa nacionalidade
24:16
então por exemplo se eu pegar japão
24:19
tiver só dois gafanhotos
24:20
eu não quero mostrar japão eu quero
24:22
mostrar somente os países que tenham
24:24
mais de 3 na ou três ou mais pessoas
24:28
morando lá e aí esse é um pouco mais
24:30
complexa faça o seu exercício paulo o
24:32
vídeo e vamos pro quarto anunciado que
24:34
eu parei pra você
24:35
agora que você já fez o terceiro eu
24:37
espero que sim
24:38
vamos ao quarto exercício que é o mais
24:40
complicado hein
24:41
mas você consegue fazer o que o
24:43
enunciado é o seguinte eu quero uma
24:45
lista agrupado pela altura dos
24:47
gafanhotos mostrando quantas pessoas
24:50
peçam mais de 100 quilos e que estão
24:52
acima da média de altura de todos os
24:54
cadastrados
24:55
calma calma não se joga pela já volto
24:59
aqui não se joga pela janela
25:01
presta atenção em primeiro lugar você
25:03
vai ter que saber qual é a média de
25:05
altura de todos os gafanhotos eu te
25:07
ensinei a calcular esta média 1 salete
25:09
pequeninho reserva desse select
25:12
aí você vai pegar em outros select todas
25:13
as pessoas que pesam mais de 100 quilos
25:16
vai agrupar eles por altura mas eu não
25:19
quero mostrar todo mundo eu quero
25:21
mostrar só quem tem esse peso acima de
25:23
100 e que está acima da média de altura
25:25
que a gente calculou no início deste
25:27
exercício difícil não é
25:30
você vai conseguir eu garanto se você
25:32
não conseguir assistir essa aula de novo
25:35
com calma praticando e aí você vai
25:38
conseguir
25:38
então é isso que quero gafanhoto
25:40
chegamos ao fim de mais uma aula
25:42
falando sobre como o select uma aula
25:44
caprichada convenhamos
25:45
então se você achou a caprichada nunca
25:47
se esqueça de curtir mostrar para as
25:49
pessoas nas suas redes sociais
25:51
olha só eu vou te pedir um favor não
25:52
compartilha só essa aula não se você
25:55
compartilha essa aula
25:56
as pessoas que não conhecem não falar
25:57
tanto esse cara não fala um monte de
25:58
coisa maluca muito difícil não gostei
26:01
desse curso compartilha a playlist do
26:03
curso completo que é muito mais legal
26:04
então dar essa ajuda e procura em vídeo
26:07
a gente está precisando de um atalho que
26:09
ó se você utilizar esse atalho aqui você
26:11
vai diretamente para playlist com todas
26:14
as aulas banco de dados
26:15
então compartilhe essa url aqui se não
26:17
tiver não deve clicar aqui tudo mas você
26:19
vendo na descrição desse vídeo tem uma
26:21
url encurtada para isso
26:24
compartilhe esse link nas redes sociais
26:26
ajuda a gente a gente está precisando e
26:27
o curso de banco de dados está bem
26:29
caprichado com certeza você tá mostrando
26:30
essas aulas para muita gente mas como
26:32
sempre no final da aula eu queria te
26:34
pedir a agora tenha uma furadeira e me
26:36
ajudando a canal clicando aqui ó
26:45
viu que maravilha
26:48
então clique aqui e se inscreva no canal
26:51
seja mais um dos principais garanhões
26:53
desse país
26:54
olha aqui ó essa é a primeira aula que
26:56
eu tô gravando lembro que falei no curso
26:57
em vídeo responde vamos ver quanto tempo
26:59
vai demorar para aparecer aqui ó
27:01
essa é a primeira aula queria agradecer
27:03
aqui ó a todo mundo dos 100 mil
27:05
inscritos do canal essa é a aula que eu
27:08
tô gravando aqui e você pode clicar aqui
27:10
ou se inscrevendo
27:11
você pode fazer parte desse grupo aqui e
27:13
fazer a gente aumentar essa placa é a
27:15
placa de 100.000 eu quero trocar essa
27:16
placa um dia e botar a placa de um
27:18
milhão e você é o único que pode me
27:20
ajudar isso como se inscrevendo e
27:22
trazendo maior número de pessoas para se
27:24
inscrever também no canal
27:25
clicando aqui você se inscreve clicando
27:27
aqui você vê o curso completo é a
27:30
playlist é aquilo que você que eu pedi
27:32
pra você para você compartilhar
27:33
clicando aqui você vê todas as aulas é
27:36
bom de vez em quando você voltar algumas
27:38
aulas e assistir de novo principalmente
27:39
por exemplo você já tá vendo select há
27:41
bastante tempo
27:42
volto aqui na playlist assistir à aula
27:44
de cliente table assistir aula de halter
27:46
table assistir às aulas de drop
27:49
então é muito útil você praticar um
27:51
banco de dados sempre
27:52
e aqui no meio como sempre você vai pra
27:55
experiência completa o curso em vídeo
27:57
que é o site onde você vai poder
27:58
encontrar todas as aulas todos os
28:00
materiais e tudo bonito tudo organizado
28:03
a gente está trabalhando para tentar
28:05
manter o curso em vídeo site totalmente
28:07
disponível às vezes a gente passa por
28:09
alguns problemas mas faz parte da vida
28:11
então é isso pequeno gafanhoto gostaria
28:13
mais uma vez de agradecer a todo mundo
28:15
que nos deu essa baixa placa não é minha
28:17
é essa placa não é da nossa equipe
28:20
essa placa não é de vocês essa placa é
28:22
do conjunto é do nosso select
28:24
asterístico from curso em vídeo então
28:26
todo mundo que faz parte desse projeto
28:28
de alguma maneira seja escrevendo seja
28:30
produzindo seja programando faz parte
28:33
aqui um pedacinho de todos nós
28:36
esse projeto como sempre digo me orgulha
28:38
muito e deixa muito feliz e com isso a
28:40
gente se despede na semana que vem tem
28:42
mais aula na semana que a gente vai dar
28:44
prosseguimento ainda vamos ver um pouco
28:45
mais de salete
28:46
mas a gente vai fazer um negócio bem
28:48
legal que é conseguir juntar uma tabela
28:50
na outra e dar resultados muito mais
28:52
interessantes
28:53
então é isso que nunca foi o tupi
28:55
sempre não pára de estudar não parei de
28:58
compartilhar essas aulas faça nossos
29:00
outros cursos têm muito o curso está
29:02
disponível um forte abraço e até a
29:04
próxima
"""

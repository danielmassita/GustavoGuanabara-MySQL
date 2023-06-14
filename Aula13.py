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


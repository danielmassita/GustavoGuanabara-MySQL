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
(export to self contained file > + include create schema)
(start export)
"""

# Depois de feito o backup, podemos na moral apagar tudo!
DROP DATABASE cadastro;

# Curso MySQL #09 - PHPMyAdmin (Parte 1)
# https://youtu.be/OaPMvrA0cA4
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/phpmyadmin-parte-1/

# USANDO O PHP MY ADMIN! PHPMyAdmin + Console de Comando

SHOW DATABASES;
"""
mysql> show databases
    -> ;
+--------------------+
| Database           |
+--------------------+
| cadastro           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.07 sec)

mysql>
"""

STATUS;
"""
mysql> status
--------------
c:/wamp64/bin/mysql/mysql8.0.31/bin/mysql.exe  Ver 8.0.31 for Win64 on x86_64 (MySQL Community Server - GPL)

Connection id:          28
Current database:
Current user:           root@localhost
SSL:                    Cipher in use is TLS_AES_256_GCM_SHA384
Using delimiter:        ;
Server version:         8.0.31 MySQL Community Server - GPL
Protocol version:       10
Connection:             localhost via TCP/IP
Server characterset:    utf8mb4
Db     characterset:    utf8mb4
Client characterset:    cp850
Conn.  characterset:    cp850
TCP port:               3306
Binary data as:         Hexadecimal
Uptime:                 1 day 2 hours 43 min 17 sec

Threads: 6  Questions: 2053  Slow queries: 0  Opens: 397  Flush tables: 3  Open tables: 284  Queries per second avg: 0.021
--------------
"""

USE cadastro;
"""
mysql> use cadastro;
Database changed
"""

STATUS;
"""
mysql> status
--------------
c:/wamp64/bin/mysql/mysql8.0.31/bin/mysql.exe  Ver 8.0.31 for Win64 on x86_64 (MySQL Community Server - GPL)

Connection id:          28
Current database:       cadastro                               <<<<<<<<<<<<<<<<<<<<<<<<<<<<
Current user:           root@localhost
SSL:                    Cipher in use is TLS_AES_256_GCM_SHA384
Using delimiter:        ;
Server version:         8.0.31 MySQL Community Server - GPL
Protocol version:       10
Connection:             localhost via TCP/IP
Server characterset:    utf8mb4
Db     characterset:    utf8mb3
Client characterset:    cp850
Conn.  characterset:    cp850
TCP port:               3306
Binary data as:         Hexadecimal
Uptime:                 1 day 2 hours 44 min 20 sec

Threads: 6  Questions: 2079  Slow queries: 0  Opens: 397  Flush tables: 3  Open tables: 284  Queries per second avg: 0.021
--------------
"""

SHOW TABLES;
"""
mysql> show tables;
+--------------------+
| Tables_in_cadastro |
+--------------------+
| cursos             |
| gafanhotos         |
+--------------------+
2 rows in set (0.04 sec)

mysql>
"""

DESCRIBE cursos;
"""
mysql> describe cursos;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| idcurso   | int          | NO   | PRI | NULL    |       |
| nome      | varchar(30)  | NO   | UNI | NULL    |       |
| descricao | text         | YES  |     | NULL    |       |
| carga     | int unsigned | YES  |     | NULL    |       |
| totaulas  | int unsigned | YES  |     | NULL    |       |
| ano       | year         | YES  |     | 2016    |       |
+-----------+--------------+------+-----+---------+-------+
6 rows in set (0.03 sec)
"""

DESC gafanhotos;
"""
mysql> DESC gafanhotos;
+---------------+---------------+------+-----+---------+----------------+
| Field         | Type          | Null | Key | Default | Extra          |
+---------------+---------------+------+-----+---------+----------------+
| codigo        | int           | YES  |     | NULL    |                |
| id            | int           | NO   | PRI | NULL    | auto_increment |
| nome          | varchar(30)   | NO   |     | NULL    |                |
| prof          | varchar(20)   | YES  |     | NULL    |                |
| nascimento    | date          | YES  |     | NULL    |                |
| sexo          | enum('M','F') | YES  |     | NULL    |                |
| peso          | decimal(5,2)  | YES  |     | NULL    |                |
| altura        | decimal(3,2)  | YES  |     | NULL    |                |
| nacionalidade | varchar(20)   | YES  |     | Brasil  |                |
+---------------+---------------+------+-----+---------+----------------+
9 rows in set (0.00 sec)
"""

SELECT * FROM gafanhotos;
"""
mysql> select * from gafanhotos;
+--------+----+-----------+------+------------+------+-------+--------+---------------+
| codigo | id | nome      | prof | nascimento | sexo | peso  | altura | nacionalidade |
+--------+----+-----------+------+------------+------+-------+--------+---------------+
|   NULL |  1 | Godofredo |      | 1984-01-02 | M    | 78.50 |   1.83 | Brasil        |
|   NULL |  2 | Maria     |      | 1999-12-30 | F    | 55.20 |   1.65 | Portugal      |
|   NULL |  3 | Creuza    |      | 1920-12-30 | F    | 50.20 |   1.65 | Brasil        |
|   NULL |  4 | Adalgiza  |      | 1930-11-02 | F    | 63.20 |   1.75 | Irlanda       |
|   NULL |  5 | Cláudio   |      | 1975-04-22 | M    | 99.00 |   2.15 | Brasil        |
|   NULL |  6 | Pedro     |      | 1999-12-03 | M    | 87.00 |   2.00 | Brasil        |
|   NULL |  7 | Janaína   |      | 1987-11-12 | F    | 75.40 |   1.66 | EUA           |
+--------+----+-----------+------+------------+------+-------+--------+---------------+
7 rows in set (0.02 sec)
"""

SELECT * FROM cursos;
"""
mysql> select * from cursos;
+---------+------------+------------------------------+-------+----------+------+
| idcurso | nome       | descricao                    | carga | totaulas | ano  |
+---------+------------+------------------------------+-------+----------+------+
|       1 | HTML5      | Curso de HTML5               |    40 |       37 | 2014 |
|       2 | Algoritmos | Lógica da Programação        |    20 |       15 | 2014 |
|       3 | Photoshop  | Dicas de Photoshop CC        |    10 |        8 | 2014 |
|       4 | PHP        | Curso de PHP para Iniciantes |    40 |       20 | 2015 |
|       5 | Java       | Introdução à Linguagem Java  |    40 |       29 | 2015 |
|       6 | MySQL      | Bancos de Dados MySQL        |    30 |       15 | 2016 |
|       7 | Word       | Curso Completo de Word       |    40 |       30 | 2016 |
+---------+------------+------------------------------+-------+----------+------+
7 rows in set (0.02 sec)
"""

mysql> update cursos set nome = 'Ph' where idcurso = '4';
# Query OK, 0 rows affected (0.00 sec) Rows matched: 1  Changed: 0  Warnings: 0

# MyPHPAdmin:
  UPDATE `gafanhotos` SET `peso` = '83.20' WHERE `gafanhotos`.`id` = 4;

"""
mysql> select * from gafanhotos;
+--------+----+-----------+------+------------+------+-------+--------+---------------+
| codigo | id | nome      | prof | nascimento | sexo | peso  | altura | nacionalidade |
+--------+----+-----------+------+------------+------+-------+--------+---------------+
|   NULL |  1 | Godofredo |      | 1984-01-02 | M    | 78.50 |   1.83 | Brasil        |
|   NULL |  2 | Maria     |      | 1999-12-30 | F    | 55.20 |   1.65 | Portugal      |
|   NULL |  3 | Creuza    |      | 1920-12-30 | F    | 50.20 |   1.65 | Brasil        |
|   NULL |  4 | Adalgiza  |      | 1930-11-02 | F    | 83.20 |   1.75 | Irlanda       |        <<<<<< ATUALIZADO DIRETO DO PHP MY ADMIN
|   NULL |  5 | Cláudio   |      | 1975-04-22 | M    | 99.00 |   2.15 | Brasil        |
|   NULL |  6 | Pedro     |      | 1999-12-03 | M    | 87.00 |   2.00 | Brasil        |
|   NULL |  7 | Janaína   |      | 1987-11-12 | F    | 75.40 |   1.66 | EUA           |
+--------+----+-----------+------+------------+------+-------+--------+---------------+
7 rows in set (0.00 sec)"""


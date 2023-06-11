# Curso MySQL #07 - Manipulando Linhas (UPDATE, DELETE e TRUNCATE)
# https://youtu.be/wXViczeTr6Q
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/manipulando-linhas-update-delete-e-truncate/

"""
Aula 07 - Curso MySQL #07 - Manipulando Linhas (UPDATE, DELETE e TRUNCATE)

MANIPULANDO REGISTROS (Linhas ou Tuplas, samesame)

- Nas aulas anteriores, aprendemos a adicionar colunas (INSERT INTO) e linhas...

"""
USE cadastro;
SELECT * FROM gafanhotos;
# Observando o "Result Set" vemos que: 
#   - as LINHAS são os registros (ou tuplas)... 
#   - as COLUNAS são os campos (ou atributos)...
#   - ALTER TABLE permite alterar as colunas...
#   Agora, vamos alterar as LINHAS! =) 

SELECT * FROM cursos;
INSERT INTO cursos VALUES
('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
('2', 'Algoritmos', 'Lógica da Programação', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de Photoshop CC', '10', '8', '2014'),
('4', 'PGP', 'Curso de PHP para Iniciantes', '40', '20', '2010'),
('5', 'Jarva', 'Introdução à Linguagem Java', '10', '29', '2000'),
('6', 'MySQL', 'Bancos de Dados MySQL', '30', '15', '2016'),
('7', 'Word', 'Curso Completo de Word', '40', '30', '2016'),
('8', 'Sapateado', 'Danças Rítmicas', '40', '30', '2018'),
('9', 'Cozinha Árabe', 'Aprenda a Fazer Kibe', '40', '30', '2018'),
('10', 'YouTuber', 'Gerar Polêmica e Ganhar Inscritos', '5', '2', '2018');

SELECT * FROM cursos;

# Agora, podemos perceber que nosso BD possui cadastro de duas coisas: "gafanhotos" e "cursos".
# Em 'gafanhotos' temos (id, nome, profissao, nascimento, sexo, peso, altura, nacionalidade) e em 'cursos' temos (idcursos, nome, descricao, carga, totaulas, ano)
# O 'id' de gafanhotos é a PRIMARY KEY. O 'idcurso' também é PRIMARY KEY.

# Ao final, teremos uma tablea, ainda com alguns "erros":
#     - nome HTML4 está errado
#     - nome PGP está errado
#     - nome Jarva está errado
#     - carga 10 do iducrso 5 está errada
#     - ano 2010 e 2000 do idcurso 4 e 5 estão errados

# Vamos começar a MANIPULAR essas linhas. Lembrando que para cada COMANDO eu posso MANIPULAR UMA ÚNICA LINHA. 
# Porém, DENTRO DE UMA LINHA, ou seja, apenas com um COMANDO, eu ainda posso alterar várias COLUNAS ao mesmo tempo.
# MODIFICANDO LINHAS INCORRETAS

UPDATE cursos
SET nome = 'HTML5'
WHERE idcurso = '1';
# 3	13	23:57:09	UPDATE cursos SET nome = 'HTML5' WHERE idcurso = '1'	1 row(s) affected Rows matched: 1  Changed: 1  Warnings: 0	0.062 sec

UPDATE cursos
SET nome = 'PHP', ano = '2015'
WHERE idcurso = '4';
# 3	14	23:58:17	UPDATE cursos  SET nome = 'PHP', ano = '2015'  WHERE idcurso = '4'	1 row(s) affected  Rows matched: 1  Changed: 1  Warnings: 0	0.000 sec

UPDATE cursos
SET nome = 'Java', carga = '40', ano = '2015'
WHERE idcurso = '5'
LIMIT 1; # Esse PARÂMETRO ajuda a aplicar as alterações em APENAS UMA LINHA (ao invés de várias ao mesmo tempo), embora nossa segurança seja o 'idcurso' que é UNIQUE e PRIMARY KEY. 
# 3	15	00:01:16	UPDATE cursos SET nome = 'Java', carga = '40', ano = '2015' WHERE idcurso = '5' LIMIT 1	1 row(s) affected Rows matched: 1  Changed: 1  Warnings: 0	0.000 sec


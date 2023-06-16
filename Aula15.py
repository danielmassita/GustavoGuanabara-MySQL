# Curso MySQL #15 - Chaves Estrangeiras e JOIN
# https://youtu.be/paZNDJAPT4E
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/chaves-estrangeiras-e-join/

"""
RELACIONANDO TABELAS - Parte 2

Quando criamos uma tabela usando o MySQL, precisamos definir uma ENGINE, uma máquina que será capaz de criar os registros.
InnoDB = uma 'engine', um mecanismo (InnoBase < Oracle) permite criar tabelas com características que vamos precisar. 

A principar característica dessa engine é SUPORTAR CHAVES ESTRANGEIRAS. 
Todas essas são 'engines' que permitem criar BD e Tabelas em MySQL que sejam compatíveis com CHAVES ESTRANGEIRAS.

- MyISAM (não é complacente com as regras transacionais do ACID)
- InnoDB (suportam ACID e Chaves Estrangeiras!!!)
- XtraDB (suportam ACID)

Transação é tudo aquilo que podemos PEDIR pro Banco de Dados e que ele possa EXECUTAR.
ACID = 
- Atomicidade (não pode ser subdividida em sub-tarefas, ou toda é feita ou nada é feito, não há transação). Sua mãe manda arrumar o quarto // arrumar somente o armário.
- Consistência (um BD consistente antes, precisa continuar consistente após a transação). Se antes tava OK, depois da transação está OK, sem falhas/inconsistências, se ocorrer, volta pro estado anterior.
- Isolamento (se existirem duas transações ocorrendo ao mesmo tempo em paralelo, ambas devem acontecer como se sendo executadas isoladas). Se dois usuários requisitarem algo do BD, ambos os pedidos devem ocorrer de forma isoladas, uma sem afetar a outra.
- Durabilidade (uma transação deve ser durável, durar o tempo que for necessário). O dado do cliente fica no DB pelo tempo que quiser (telefone, nome, atributos, etc.), com alteração que vai persistir e ser durável enquanto existir.
"""



"""
Na aula passada, criamos duas entidades:

- Gafanhoto ('id', nome, profissao, nascimento, sexo, peso, altura, nacionalidade)
- Curso ('idcurso', nome, descricao, carga, totaulas, ano)

Relacionamentos do Tipo (N-para-1, muitos para único): 
[gafanhotos] ---------- <prefere> ---------- [cursos]

Menino                                        HTML
Godofredo                                     PHP
Dolores                                       Word

Menino prefere Word.
Godofredo prefere HTML.
Dolores prefere HTML.

Cardinalidade: 
Cada gafanhoto pode preferir um curso (é O mais Preferido!, oras).
Cada curso pode ser preferido por vários gafanhotos.

REGRA RELACIONAMENTO 1-para-Muitos:
- Sempre pegamos o Lado-1 e sua CHAVE PRIMÁRIA e trazemos diretamente pro Lado-Muitos.
- Pegamos o 'idcurso' (pk de cursos) e levamos como 'cursopreferido' para a entidade 'gafanhotos'. 
- A chave estrangeira não precisa do mesmo nome. Mas SIM o mesmo tipo e tamanho (INT, VarChar(10)). 
- Adicionar a 'chave estrangeira' na tabela de 'gafanhotos'.

>>> XAMP
>>> MySQL Workbench
"""
# Inicianlizando o Banco de Dados
SHOW DATABASES;
USE cadastro;
DESCRIBE gafanhotos;

# Adicionando a Foreign Key
ALTER TABLE gafanhotos
ADD COLUMN cursopreferido int; # Vai adicionar 'cursopreferido', do tipo INT, no final padrão...

DESCRIBE gafanhotos;

# Adicionando a Foreign Key
ALTER TABLE gafanhotos
ADD FOREIGN KEY (cursopreferido)
REFERENCES cursos(idcurso);

DESCRIBE gafanhotos;
#cursopreferido	int	YES	MUL <<< MUL = Multiple Keys (Foreign Key)

# Agora, podemos começar a registrar/cadastrar cada curso preferido de cada aluno.
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

# Daniel (id = 1) vai ter MySQL(idcurso = 6) como curso preferido.
UPDATE gafanhotos SET cursopreferido = '6' WHERE id = '1';
SELECT * FROM gafanhotos;

# No MySQL Workbench, podemos adicionar manualmente os cursos preferidos, em lote, adicionando em 'cursopreferido' (foreign key) os números do 'idcurso' (primary key da tabela 'cursos').
# Atualizamos manualmente (mouse+teclado) e depois clicamos em Apply. Temos o código pra revisão.
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '22' WHERE (`id` = '2');
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '12' WHERE (`id` = '3');
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '7' WHERE (`id` = '4');
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '1' WHERE (`id` = '5');
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '8' WHERE (`id` = '6');
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '4' WHERE (`id` = '7');
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '5' WHERE (`id` = '8');
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '3' WHERE (`id` = '9');
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '30' WHERE (`id` = '10');
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '22' WHERE (`id` = '11');


### INTEGRIDADE REFERENCIAL

# Se perceber, agora o aluno Daniel possui o curso 6 como seu preferido.
# E se eu tentasse apagar o curso de MySQL? 

# Vou tentar apagar, da tabela 'cursos' o registro onde 'idcurso' = '6', ou seja, apagar o MySQL. Veja o erro.
DELETE FROM cursos WHERE idcurso = '6';
"""0	21	16:26:08	DELETE FROM cursos WHERE idcurso = '6'	Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`cadastro`.`gafanhotos`, CONSTRAINT `gafanhotos_ibfk_1` FOREIGN KEY (`cursopreferido`) REFERENCES `cursos` (`idcurso`))	0.047 sec"""

# O erro de constraint + foreign key é um ERRO DE INTEGRIDADE REFERENCIAL. 
# Na prática, se eu tentar alterar qualquer estrutura, o BD será negado, pois já existe uma relação gafanhoto-curso.
# No exemplo da linha 29.
# Não podemos apagar HTML5, pois o Godofredo e Dolores já preferem esse curso.
# Porém, o curso de PHP pode ser apagado, pois não tem registro relacional.

# No exemplo, podemos apagar o 'idcurso' = 28 (HTML4).
DELETE FROM cursos WHERE idcurso = '28';
"""
3	22	16:29:56	DELETE FROM cursos WHERE idcurso = '28'	1 row(s) affected	0.031 sec

27	Modelagem de Dados	Curso de Modelagem de Dados	30	12	2020
29	PHP7	Curso de PHP, versão 7.0	40	20	2020
"""

# Se eu der um SELECT na tabela de 'gafanhotos', eu vou ver APENAS o código do seu curso preferido, e não o nome...
SELECT * FROM gafanhotos;
SELECT nome, cursopreferido FROM gafanhotos;

# Quero ver o 'nome do curso' para além do idcurso = '6'. Vamos precisar entender as JUNÇÕES DO SQL.

SELECT * FROM cursos;
SELECT nome, ano FROM cursos;

# Meu objetivo é juntar as tabelas, de (SELECT nome, cursopreferido FROM gafanhotos;) + (SELECT nome, ano FROM cursos;)
SELECT gafanhotos.nome, gafanhotos.cursopreferido, cursos.nome, cursos.ano
FROM gafanhotos
JOIN cursos;
"""
Daniel Morais	6	PHP4	2010
Daniel Morais	6	PHP7	2020
Daniel Morais	6	Modelagem de Dados	2020
Daniel Morais	6	Magento	2019
Daniel Morais	6	Joomla	2019
Daniel Morais	6	WordPress	2019
Daniel Morais	6	After Effects	2018
Daniel Morais	6	Premiere	2017
Daniel Morais	6	SEO	2017
Daniel Morais	6	Segurança	2018
Daniel Morais	6	Redes	2016
Daniel Morais	6	Hardware	2017
Daniel Morais	6	Swift	2019
Daniel Morais	6	PowerPoint	2018
Daniel Morais	6	JavaScript	2017
Daniel Morais	6	Android	2018
Daniel Morais	6	C#	2017
Daniel Morais	6	C++	2017
Daniel Morais	6	Responsividade	2018
Daniel Morais	6	Excel	2017
Daniel Morais	6	POO	2016
Daniel Morais	6	Python	2017
Daniel Morais	6	Word	2016
Daniel Morais	6	MySQL	2016
Daniel Morais	6	Java	2015
Daniel Morais	6	PHP	2015
Daniel Morais	6	Photoshop5	2014
Daniel Morais	6	Algoritmos	2014
Daniel Morais	6	HTML5	2014
Talita Nascimento	22	PHP4	2010
Talita Nascimento	22	PHP7	2020
Talita Nascimento	22	Modelagem de Dados	2020
Talita Nascimento	22	Magento	2019
Talita Nascimento	22	Joomla	2019
Talita Nascimento	22	WordPress	2019
Talita Nascimento	22	After Effects	2018
Talita Nascimento	22	Premiere	2017
[...]
"""

# Eu estou juntando 'gafanhotos' com 'cursos'. ERRO - no exemplo, pra cada aluno, mostrarei todos cursos, embora apareça apenas o cursopreferido = '6'.
# Precisamos FILTRAR, usando uma Cláusula Obrigatória (ON) sempre que usar JOIN.

# Cláusula ON

# Selecionando nome, cursopref., nome curso, ano | da tabela gafanhotos JUNTANDO com cursos
SELECT gafanhotos.nome, gafanhotos.cursopreferido, cursos.nome, cursos.ano
FROM gafanhotos JOIN cursos
ON cursos.idcurso = gafanhotos.cursopreferido;
# ONDE o gafanhoto se liga ao curso através de sua chave estrangeira e primária
# ON cursos.idcurso (chave primária) = gafanhotos.cursopreferido (chave estrangeira)

# Fiz a ligação da chave primária com o relacionamento na chave estrangeira.
"""
Leila Martins	1	HTML5	2014
Jackson Telles	3	Photoshop5	2014
Janaína Couto	4	PHP	2015
Carlisson Rosa	5	Java	2015
Daniel Morais	6	MySQL	2016
Lucas Damasceno	7	Word	2016
Letícia Neves	8	Python	2017
Emerson Gabriel	12	C++	2017
Talita Nascimento	22	Premiere	2017
Andreia Delfino	22	Premiere	2017
Danilo Araujo	30	PHP4	2010
"""

# Podemos melhorar e apagar a coluna 'gafanhotos.cursopreferido' pra evitar poluição numérica.
SELECT gafanhotos.nome, cursos.nome, cursos.ano
FROM gafanhotos JOIN cursos
ON cursos.idcurso = gafanhotos.cursopreferido;
"""
Leila Martins	HTML5	2014
Jackson Telles	Photoshop5	2014
Janaína Couto	PHP	2015
Carlisson Rosa	Java	2015
Daniel Morais	MySQL	2016
Lucas Damasceno	Word	2016
Letícia Neves	Python	2017
Emerson Gabriel	C++	2017
Talita Nascimento	Premiere	2017
Andreia Delfino	Premiere	2017
Danilo Araujo	PHP4	2010
"""

# Eu tinha 60 alunos, e 30 cursos. Mas só aparecem os 10 alunos alterados. Na verdade, fizemos um INNER JOIN, ou seja, somente aqueles COM RELAÇÃO.
UPDATE `cadastro`.`gafanhotos` SET `cursopreferido` = '1' WHERE (`id` = '14');

SELECT gafanhotos.nome, cursos.nome, cursos.ano
FROM gafanhotos JOIN cursos
ON cursos.idcurso = gafanhotos.cursopreferido;
"""
Leila Martins	HTML5	2014
Rosana Kunz	HTML5	2014              <<<<<<<<<
Jackson Telles	Photoshop5	2014
Janaína Couto	PHP	2015
Carlisson Rosa	Java	2015
Daniel Morais	MySQL	2016
Lucas Damasceno	Word	2016
Letícia Neves	Python	2017
Emerson Gabriel	C++	2017
Talita Nascimento	Premiere	2017
Andreia Delfino	Premiere	2017
Danilo Araujo	PHP4	2010
"""

# O INNER JOIN vai ver somente as relações ativas, ou seja, as linhas coloridas do diagrama entre Gafanhoto e Curso Preferido.

SELECT gafanhotos.nome, cursos.nome, cursos.ano
FROM gafanhotos INNER JOIN cursos
ON cursos.idcurso = gafanhotos.cursopreferido
ORDER BY gafanhotos.nome ASC;

# Podemos melhorar mais usando apelidos (alias):

SELECT g.nome, c.nome, c.ano
FROM gafanhotos AS g INNER JOIN cursos AS c
ON c.idcurso = g.cursopreferido
ORDER BY g.nome ASC;

# O INNER JOIN pega somente a ÁREA RELACIONADA (no caso do exemplo, as linhas de quem é aluno e tem curso preferido).
"""
Relacionamentos do Tipo (N-para-1, muitos para único): 
[gafanhotos] ---------- <prefere> ---------- [cursos]

Menino                                        HTML
Godofredo                                     PHP
Dolores                                       Word
Velho                                         Java

Menino prefere Word.
Godofredo prefere HTML5.
Dolores prefere HTML5.
Velho não prefere curso algum.
"""

# O OUTTER JOIN mostra aqueles registros SEM RELAÇÃO.

# Temos uma tabela (gafanhotos) à ESQUERDA do JOIN e a tabela (cursos) à DIREITA do JOIN.
# FROM gafanhotos AS g JOIN cursos AS c
# Precisamos definir 'gafanhotos' como PREFERENCIAL, à 'cursos', quando usamos OUTER JOIN.
SELECT g.nome, c.nome, c.ano
FROM gafanhotos AS g LEFT OUTER JOIN cursos AS c
ON c.idcurso = g.cursopreferido;
"""
Daniel Morais	MySQL	2016
Talita Nascimento	Premiere	2017
Emerson Gabriel	C++	2017
Lucas Damasceno	Word	2016
Leila Martins	HTML5	2014
Letícia Neves	Python	2017
Janaína Couto	PHP	2015
Carlisson Rosa	Java	2015
Jackson Telles	Photoshop5	2014
Danilo Araujo	PHP4	2010
Andreia Delfino	Premiere	2017
Valter Vilmerson		
Allan Silva		
Rosana Kunz	HTML5	2014
Josiane Dutra		
Elvis Schwarz		
Paulo Narley		
Joade Assis		
Nara Matos		
Marcos Dissotti		
Ana Carolina Mendes		
Guilherme de Sousa		
Bruno Torres		
Yuji Homa		
Raian Porto		
Paulo Batista		
Monique Precivalli		
Herisson Silva		
Tiago Ulisses		
Anderson Rafael		
Karine Ribeiro		
Roberto Luiz Debarba		
Jarismar Andrade		
Janaina Oliveira		
Márcio Mello		
Robson Rodolpho		
Daniele Moledo		
Neto Sophiate		
Neriton Dias		
André Schmidt		
Isaias Buscarino		
Rafael Guimma		
Ana Carolina Hernandes		
Luiz Paulo		
Bruna Teles		
Diogo Padilha		
Bruno Miltersteiner		
Elaine Nunes		
Silvio Ricardo		
Denilson Barbosa da Silva		
Jucinei Teixeira		
Bruna Santos		
André Vitebo		
Andre Santini		
Ruan Valente		
Nailton Mauricio		
Rita Pontes		
Carlos Camargo		
Philppe Oliveira		
Dayana Dias		
Silvana Albuquerque		
"""
# A Query vai dar Preferência pra gafanhotos, exibindo a totalidade dos alunos mesmo que sem relação com curso preferido.

# Podemos também definir a PRIORIDADE dos cursos, onde haverá ao menos uma entrada de registro pra cada curso, ou nenhuma entrada. 
SELECT g.nome, c.nome, c.ano
FROM gafanhotos AS g RIGHT OUTER JOIN cursos AS c
ON c.idcurso = g.cursopreferido;
"""
Leila Martins	HTML5	2014
Rosana Kunz	HTML5	2014
	Algoritmos	2014
Jackson Telles	Photoshop5	2014
Janaína Couto	PHP	2015
Carlisson Rosa	Java	2015
Daniel Morais	MySQL	2016
Lucas Damasceno	Word	2016
Letícia Neves	Python	2017
	POO	2016
	Excel	2017
	Responsividade	2018
Emerson Gabriel	C++	2017
	C#	2017
	Android	2018
	JavaScript	2017
	PowerPoint	2018
	Swift	2019
	Hardware	2017
	Redes	2016
	Segurança	2018
	SEO	2017
Talita Nascimento	Premiere	2017
Andreia Delfino	Premiere	2017
	After Effects	2018
	WordPress	2019
	Joomla	2019
	Magento	2019
	Modelagem de Dados	2020
	PHP7	2020
Danilo Araujo	PHP4	2010
"""





"""
Transcrição


Procurar no vídeo
0:00
hum hum hum
0:19
Olá pequeno gafanhoto seja bem-vindo a mais uma aula do seu curso em vídeo de banco de dados que eu mais quero ele o
0:26
meu nome é Gustavo Guanabara eu sou seu professor e chegamos a mais uma aula Onde vamos dar continuidade a banco de
0:32
dados e dessa vez a gente vai continuar falando sobre o modelo racional e vamos começar a relacionar as tabelas
0:39
efetivamente Essa é a parte 2 dessa aula e agora já foi outra gente vai poder
0:45
ligar uma tabela na outra através dos Comandos e você vai ver tudo aquilo que a gente viu na aula passada na teoria
0:51
colocar em prática e como você pode chegar à conclusão de uma maneira bem fácil Se você não entendeu direito aula
0:57
passada ou se você sequer assistiu ao a passar e você vai precisar assistir lá porque a gente viu toda a base teórica
1:04
na aula passada e agora a gente vai colocando em prática então aula 15 que a sala que você está assistindo não faz
1:10
sentido sem o conhecimento prévio da aula 14 então eu vou vim te fazer um convite especial dá uma olhada aqui ó
1:16
tem que aqui embaixo também esse botão aqui embaixo eu tô vendo o botão aqui clica nele e aqui você vai ser enviado diretamente para playlist e você vai
1:24
assistir à aula 14 dessa playlist se você preferir você pode clicar aqui em cima que vai aparecer aqui nesse momento
1:30
também a Playlist diretamente para o curso de banco de dados assistir aula 14 Veja a estrutura que foi idealizada E aí
1:37
você pode vir aqui e assistir aula aqui e antes de dar uma relembrada no que a gente viu na aula passada eu preciso te
1:43
explicar um conteúdo técnico que não é muito complicado O negócio é o seguinte quando a gente cria uma tabela utilizando mais Kelly a gente tem que
1:50
escolher uma coisa chamada índia que a máquina que vai poder criar registro deixa eu abrir o código do nosso damp
1:56
que foi feito nas aulas anteriores para poder explicar isso para você então em ambiente Windows vou abrir
2:03
o explorador de arquivos vou lá em documentos dumpees e eu tenho aqui os dentes que
2:10
foram gerados aqui vou editar um deles aqui no outro pede mais mais e se você perceber aqui se eu achar um Crush aí
2:17
aqui ó o Chris Table no final do comando eu tenho a minha and
2:23
especificada você percebe aqui que por padrão Ela utiliza a Engine innodb então
2:29
podemos chegar à conclusão de que hino de bebê é uma rede né uma máquina de
2:34
criação de tabelas e não beber na verdade é um mecanismo esse mecanismo foi criado por uma empresa chamada hino
2:40
base que hoje pertence a hora o hino de bebê ele é um mecanismo é uma ending que
2:46
pertence Hoje em dia a hora e que vai permitir a criação de tabelas com algumas características que a gente vai
2:51
precisar a principal característica dessa and an é suportar Chaves
2:57
estrangeiras e você deve lembrar da aula passada que eu falei muito sobre chave estrangeira Então para que eu possa Sul
3:02
e a chave estrangeira eu vou utilizar o hino de ver só que existem outros exemplos de máquinas que você pode
3:09
utilizar as mais comuns são um Maísa que é um pouquinho mais antiga e uma outra que é um pouco mais recente que a Extra
3:16
de bebê todas essas três são and essa estão aparecendo aqui na tela são em dias para poder criar banco de dados
3:21
criar tabelas utilizando mais Kelly e que sejam compatíveis com Chaves estrangeiras se você deu uma olhada aí
3:27
pela internet você vai ver que tem muito tutorial que utilizava a Índia antiga que é a Maísa o grande problema da maçã
3:33
é que ela não é complacente com as regras transacionais d'Oeste aquela agora já era mas falou em inglês aqui
3:41
falou alemão entendi nada tá uma porque ela ganhou o Maísa não dava suporte as
3:47
quatro principais regras de uma boa transação E essas regras são conhecidas como s a c e d os dois debaixo o innodb
3:56
electradp suporto esse tipo de coisa mas vem aqui comigo eu vou te dar uma explicada nessas quatro letrinhas aqui
4:02
da tra bom então como eu disse anteriormente as duas em diante de baixo ainda bebê e aqui tá é beber suportam o
4:10
que a gente chama de é ser que são as quatro principais regras de uma boa transação transação sempre lembrando é o
4:16
seguinte tudo aquilo que você possa pedir para um banco de dados e executar e te dar uma resposta é considerada uma
4:23
transação toda ação que o banco de dados possa executar é considerado como sendo uma transação e uma transação para ela
4:30
acontecer ela tem que seguir as quatro principais regras oa dessa sigla significa atomicidade uma transação a
4:37
tem que ser atômica O que significa ser atômica ela não pode ser dividida em
4:43
subir tarefas isso é de uma maneira bem simples atomicidade de seguinte uma eu
4:49
tenho uma tarefa para fazer ou toda a tarefa é feita ou nada vai ser considerado sua mãe chega para você
4:55
falar assim olha só Arruma seu quarto e aí você arruma só metade a sua arrumação não foi atômica você não Me leva que ela
5:03
pediu por completo então sua mãe seguindo as regras toda essa de transação diria para você você não
5:10
arrumou o quarto isso porque você só arrumou metade então atomicidades de uma frase simples ou tudo acontece ou Nada é
5:17
considerado no banco de dados você manda salvar um dado e ele salva só metade ele vai ter que voltar para o estado
5:23
anterior porque a transação não foi completada Deu para entender a segunda regra que é o cê é a consistência
5:30
consistência é o seguinte um banco de dados que estava consistente anteriormente tem que continuar
5:36
consistente após uma transação então é o seguinte Resumindo numa frase se antes de fazer a transação banco de dados
5:42
estava OK depois que terminar a transação ele também tem que estar o que não podem ocorrer falhas não podem
5:48
correr inconsistências e se isso acontecer tudo é desfeito para o estado imediatamente anterior vamos agora a
5:54
terceira letrinha que a ue é de isolamento isolamento trato seguinte
6:00
quando eu tenho duas transações acontecendo em PA e elas devem acontecer como se tivessem sendo executadas de
6:06
forma sou a o mas que era um banco de dados multitarefa você sabe disso ele é multi-usuário também isso é eu posso ter
6:12
duas pessoas acessando o mesmo tempo pedindo transações ao mesmo tempo se eu tenho dois usuários que pedem duas
6:18
transações ao mesmo tempo Duas atividades ao mesmo tempo elas não podem interferir uma na outra então se eu
6:24
tiver coisas paralelas acontecendo Elas têm que acontecer como se elas tivessem isoladas uma não pode afetar a outra
6:29
isso é isolamento vamos agora a quarta e última letra que é o de Poder é de
6:35
durabilidade uma transação ela tem que ser durável isso ela tem que durar o tempo que for necessário por exemplo se
6:43
você salvou dado de um cliente você quer que esse dado do cliente fique lá o tempo necessário que você precise dele
6:49
não tô dizendo que o dado do que a gente tem que ser eterno até porque você pode por exemplo alterar o número do telefone
6:54
dele mudaram o nome dele que você digitou errado adicionar novas características para o cliente ele os
7:00
dados eles não são estáticos eles podem ser de novo em qualquer alteração que eu faça ela tem que persistir Elas têm que
7:07
ser durável o suficiente enquanto eu precisar de cidade você não pode perder dados do nada isso é durabilidade Então
7:14
por uma transação acontecer ela tem que ser atômica consistente isolada e
7:19
durável isso é um princípio fundamental da teoria de banco de dados o Maísa que
7:25
aquele mecânico antigo ele não possui compatibilidade com esses papo conceito de transações mecanismos mais recentes
7:31
como por exemplo Windows bebê e o ex a receber suportam isso então na hora de criar sua tabela você pode explicitar
7:38
que você quer utilizar Onde o bebê da mesma maneira que eu fiz aqui moto and igual ainda o bebê no final do cliente e
7:44
sabão no caso do mais que é essa é a versão que eu tô utilizando caso eu não coloque Qual a Índia Eles já considera
7:51
minha bebê então cuidado ele tem duas funcionalidades primeiro permitir a compatibilidade o uso de Chaves
7:57
estrangeiras que são extremamente importantes porque garantem a integridade referencial eu vou mostrar
8:03
bom para você nessa aula e além de garantir a integridade referencial por uso de Chaves estrangeiras o innodb
8:08
também permite a compatibilidade com os quatro conceitos fundamentais de uma boa
8:14
a transação é um pouco teórico é um pouco conceitual aprofundado mas eu
8:19
preciso passar isso para vocês porque às vezes você vai ver um tutorial que usam mais AM e o mais Ah não é melhor opção
8:25
se você vive um tutorial que tiver tirando mais a provavelmente um pouco mais antigo e mais era a única opção na
8:30
época basta que você no caso aí se você vai digitar no seu sistema Tire o mais Lan coloque-me no db e tudo vai
8:37
funcionar normalmente então agora a gente pode voltar a nossa teoria de banco de dados para gente poder botar em prática se você se lembra na aula
8:44
passada a gente tinha criado uma estrutura com duas tabelas com duas entidades a identidade gafanhoto
8:50
entidade curso cada uma delas tinha seu próprio conjunto de atributos onde o café Sutil identificação nome uma
8:57
profissão Nascimento sexo peso altura nacionalidade e cada curso tinha o seu identificador um nome é uma carga total
9:04
de aula Simone e aí a gente criou uma ligação teórica aqui a gente fez com que um gafanhoto pudesse preferido um
9:10
determinado curso Então eu tinha aqui um relacionamento prefere E aí sempre que
9:15
você tem relacionamentos entre entidades eu sempre proponho aquele exercício mental que você sempre faz sempre que
9:22
você olhar um retângulo expande ele e imagina instâncias dentro dele eu vou expandir aqui ó vamos expandir Rafael de
9:29
curso expandindo eu vou poder botar várias gafanhas aqui dentro e vou imaginar vários cursos aqui dentro esse
9:36
já foi outros eles podem preferir cursos por exemplo o primeiro ali de cima vamos supor que ele prefere curso de Word
9:42
Acabei de fazer um apontamento essa linha é o meu relacionamento entre as duplas que vão comprou a tabela o
9:48
segundo ali Godofredo ele vai preferir o conserto ml por exemplo e a Dolores vai preferir também o curso HTML Então nós
9:54
vamos consertar esse exemplo durante essa aula então eu tenho menininha ali que prefere o Word o Godofredo e a
10:01
Dolores Eles preferem o curso e esse você dá uma olhadinha ali ninguém prefere a considerar então a ali na tela
10:07
o curso de PHP ninguém nesse momento nesse grupo de três pessoas preferir um curso de PHP para a gente poder fazer a
10:14
cartinha nalidade nunca se esqueça a gente tem que considerar o seguinte cada um desse daqui tem quantas gerações ali
10:21
então cada ao gafanhoto pode preferir um curso Então vou fazer cada um desse lado
10:27
prefere um curso agora cada curso desse aqui é preferido por vários gafanhotos e
10:35
pode ser preferido por vários gafanhotos Então esse aqui é um relacionamento de um para muitos E aí entendeu agora que a
10:43
gente já fez essa relação já mostrou essa ligação a gente pode encurtar a gente pode parar de imaginar as coisas
10:50
lá dentro com as relações já que a gente volta nisso a vão dar uma encostada aqui então vou simplificar diminuindo aqui as
10:56
minhas entidades e o que eu vou ter que fazer o seguinte a regra do relacionamento de um Para muitos é
11:01
simples porque a gente tem que fazer vou pegar sempre o lado um pegar a chave primária que no caso aqui aí de curso e
11:08
trazê-la diretamente aqui para o lado muitos Então o que eu vou fazer a pegar o e do curso e colocar desse lado aqui
11:14
como curso preferido a chave estrangeira ela não precisa ter o mesmo nome da
11:19
chave primária de onde ela veio ela só precisa ter o mesmo tipo e tamanho então por exemplo se o ID do curso é inte
11:26
então o curso preferido também tem que ser 20 se por acaso uma chave primária Eva achar de 10 a chave estrangeira
11:32
também tem que ser baixar de 10 ela não precisa ter um mesmo nome ela precisa ter um mesmo tipo e o mesmo tamanho Então vamos ao nosso ambiente Vamos
11:39
abrir o banco de dados e ver como é que tá tudo até o momento Lembrando que o que eu tenho que fazer
11:44
aqui é adicionar uma chave estrangeira na tabela já foi outro Isso é curso preferido vai ser um campo que eu vou
11:51
adicionar na tabela já foi outro então eu estou de volta aqui no meio ambiente meu servidor já tá aberto aqui embaixo
11:56
eu já tô com um servidor aberto tudo ativo está verdinho pode ser o centro também e eu vou abrir o Oi Kelly bom que
12:04
vem abre no ambiente eu vou logar no servidor correspondente aqui e eu tenho
12:09
meu banco de dados de cadastro Primeira coisa eu vou abrir esse banco de os cadastro a controlar a inter já abriu o banco de
12:16
dados vamos fazer o seguinte vamos dar um describe aqui na tabela gafanhoto
12:23
controlar Inter e agora eu tenho responder aqui a parte de baixo eu tenho
12:28
aqui a estrutura da tabela onde eu tenho ideia nome profissão Nascimento sexo peso altura nacionalidade lembrando eu
12:35
tenho que agora adicionar o curso preferido para adicionar a gente já viu mas eu vou mostrar aqui pra vocês de
12:41
novo para adicionar um campo que a primeira coisa que a gente tem que fazer a gente tem que utilizar o alter table Então vou colocar alter table gafanhotos
12:48
e vou colocar é de cólon curso preferido int Lembrando que curso preferido tem
12:53
que ser do mesmo tipo da chave primária que veio lá do curso que é isso no meu caso aqui vamos de para o ambiente e
12:59
digitar Esse comando vamos ver aqui ó o alter table já foi o outro é de cólon
13:07
curso preferido sem espaço nem nada do tipo gente percebe que o seguinte a
13:14
palavra: ela é opcional então eu posso digitar alter table gafanhotos é de cólon com os preferiti ou simplesmente é
13:21
de curso prefiro doente Lembrando que se eu não colocar nada depois do tipo aqui ele vai ser adicionado no final da
13:26
tabela Eu ainda tenho opção de ter first ou After qualquer um dos Campos aqui aí
13:33
no caso aqui eu vou deixar em branco que ele vai adicionar no final contra o Inter ele executou vou dar um outro
13:39
describe e perceber que agora eu tenho curso preferido beleza adicionei um campo e esse campo ele é um curso
13:45
preferido de cada aluno o que nós temos que fazer agora é dizer que esse curso preferido é uma chave estrangeira para
13:51
poder fazer aquela ligação que a gente viu para fazer isso eu vou dar um outro alter table que eu vou dar alter table
13:57
gafanha outro de novo só que agora eu vou adicionar uma chá bom dia para adicionar chave estrangeira é fácil só
14:04
que em vez da é Nicole eu vou usar é diferente eu tô adicionando o curso preferido como uma chave estrangeira E
14:12
aí eu tenho que indicar qual é a referência Então vou utilizar references curso e de curso isso significa o
14:19
seguinte que o curso preferido da tabela de gafanhotos está ligado com o ID curso
14:25
na tabela de cursos E foi exatamente o que eu coloquei naquela imagem lá que a gente acabou de ver eu preciso fazer uma
14:32
ligação entre o curso preferido que a chave estrangeira e o ID cursus a tabela cursos que a chave primária para a gente
14:38
poder fazer aquela ligação entre chave primária chave estrangeira que é extremamente necessária para garantir a integridade referencial digitando aquele
14:45
comando vamos lá alter table e a fã em outras vamos adicionar é uma folha aqui
14:53
que é a curso preferido com a minha referência a
15:00
cursos e de curso o ponto-e-vírgula control enter ele já
15:06
fez a ligação vamos dar o describe apanhou outro de novo para em cima da linha control enter e agora eu percebo
15:12
que o seguinte o meu curso preferido tá com inte que é o mesmo tamanho e aqui ó eu tenho no que Na minha chave Eu tenho
15:19
um esse mundo é a representação aqui que tem uma chave múltipla ou uma chave no
15:24
nosso caso aqui essa chave múltipla seria uma chave estrangeira para você precisa verificar aqui se depois
15:30
executar esses comandos o curso preferido está sendo considerado como uma chave múltipla que nosso caso aqui a
15:36
gente já colocou como forma aqui que é um tipo de chave múltipla mas a gente consegue identificar que que ela é uma
15:41
chave estrangeira agora o que a gente tem que fazer é começar a cadastrar os cursos preferidos de cada aluno então
15:47
vou fazer o seguinte aqui ó vamos dar um select asteristico from gafanhoto
15:53
controlar Inter Agora eu tenho aqui vamos fazer com que por exemplo Daniel Morais prefira o curso de
16:01
eletricista from cursos o control center a vamos supor aqui ó o Daniel vai
16:07
preferir o curso e mais Kelly que é isso nosso curso aqui um curso mais Kelly tem o ID do curso 6 Então nós vamos
16:13
adicionar aqui o Daniel como preferindo o curso de mais Kelly que é o 6 Então
16:18
nós vamos fazer o seguinte update gafanhotos 7 curso preferido igual a sem
16:27
onde Where o ID do aluno seja igual a 1
16:33
isso é o meu aluno um que é o Daniel vai gostar do curso seis que é o mais Kelly
16:41
control enter agora nós podemos dar um Será que triste um gafanhotos e
16:46
verificar que agora o curso preferido do Daniel é o 6 E aí em teoria você vai ter
16:51
que dar um update para cada um dos alunos Eu tenho 60 alunos eu não vou colocar todos aqui mas eu vou mostrar
16:57
uma técnica de você dar o update utilizando o Aqui vende que Vai facilitar sua vida quando a sua base de
17:02
dados ela tá uma e você pode fazer isso de forma manual que é digitando o comando ou de maneira automática que é o
17:08
seguinte lá tá aqui ó Thalita vamos fazer aqui ó os cursos eu tenho meu select do curso eu tenho cursos de 1 até
17:16
o 30 então eu vou fazer o seguinte aqui vamos lá nos gafanhotos e eu vou fazer
17:21
aqui ó vou adicionar alguns preferido de cada um 22
17:27
12718 453
17:32
3.022 vou fazer só esse daqui é importante que se você mexer nessa tabela você perceba no canto inferior
17:39
direito da tela que tem um botão apply se você não clicar nele nenhuma das alterações que eu fiz vai surtir efeito
17:46
então basicamente que o teria que fazer é um update para cada um dos casos e o outro dente Vai facilitar minha vida
17:51
nisso então a vou clicar aqui em baixo no offline ele vai já montar os comandos
17:56
update para mim eu vou clicar em apply ele já aplicou finalizo a partir de
18:01
agora quando eu der um select pagar e ele já tá com os dados do curso preferido já cadastrados e agora nós
18:08
vamos falar sobre uma coisa muito importante que é a integridade referencial você percebeu ali o exemplo
18:14
que a gente criou o aluno Daniel que é o aluno um está preferindo o curso seis
18:19
que é o curso de mais quer às vezes quando você cria uma chave estrangeira você não vi muita utilidade para votar
18:24
que eu queria isso eu vou te mostrar agora na prática o que eu vou tentar fazer aqui é por exemplo tentar apagar o
18:30
curso de mais quer porque eu vou tentar fazer dar um bilhete from cursos Ué e de
18:36
curso igual a 6 isso é eu estou tentando apagar o curso de mais Kelly vamos executar Esse comando lá no nosso
18:42
ambiente e ver como ele se comporta Então já estou aqui no ambiente e fechar o resultado da busca Então vamos lá
18:47
vamos digitar o comando de elite from cursos Where
18:54
mídia curso seja igual a 6 isso é eu estou tentando apagar o curso que tem o
18:59
identificador seis control center e você percebe lá em baixo nem consegui deletar e ele deu um erro de constante funk Ok
19:08
se você perceber que com street for him Então esse erro foi o erro de integridade referencial vou te mostrar
19:15
na prática o que que tá acontecendo aqui você deve se lembra muito bem dessa imagem que a gente gerou alguns minutos
19:21
atrás nessa aula onde eu tinha os gafanhotos e os cursos e eu tinha gafanhotos preferindo determinado os
19:26
cursos o que acontece na prática que é o seguinte se eu tentar alterar qualquer estrutura do curso por exemplo você vê
19:33
ali que o Godofredo e a Dolores preferem o curso de HTML5 Se eu tentar apagar o
19:39
curso HTML5 Isso vai ser legado isso porque e já existe a relação entre nunca
19:45
foi outro e esse curso não sou tentar apagar esse curso eu vou receber uma mensagem de erro eu não vou conseguir
19:51
fazer porque já existem pessoas preferido esse curso segundo os criadores preferem o curso HTML5 eles
19:58
são registrados para isso eu não posso apagar o registro do HTML5 que ele vai perder o relacionamento entre eles Então
20:05
nesse caso se o sistema de banco de dados permite se a seleção se eu pudesse apagar que o HTML 5 o godofreda Dolores
20:12
ficaram com uma inconsistência isso é porque ele diriam olha ele prefere até mais 5 mas ele prefere um curso que nem
20:18
existe porque eu acabei de apagar agora Se eu tentar pagar o curso de PHP por exemplo ele não tem relação nenhuma com
20:25
ninguém então ele vai conseguir ser apagado sem problema algum o curso de
20:31
HTML5 e hoje aqui nesse meu caso não poderiam ser apagados mas hoje pegar tem que estava aqui pode ser apagado porque
20:37
não existe relação nenhuma vamos ver na prática se isso realmente funciona entendeu select dos gafanhotos aqui eu
20:43
tenho alguns preferidos seis 22/12 714853 por exemplo o curso 9 não é
20:50
preferido tipo mim o tanto a pagar ele pagar o curso 9 Então vamos dar um select no curso aqui para eu ver qual é
20:57
o curso 9 o posto 9 é o DP o vamos fazer o seguinte que o curso de html 4 É sério
21:04
que você vai ter medo de quatro vamos Apagar Ele são 28 também não tem relação Vamos tentar pagar Então os 28 então de
21:10
leite from curso mulher e de curso = 28 que seria esse curso que perguntar
21:16
controle a e ele apagou Sem problema nenhum ó vou dar um select nos cursos de novo Eu já não tenho mais o 28 lá 27 e
21:25
já pulou por 29 Deu para entender isso é integridade referencial eu não consigo
21:30
modificar um campo se ele for afetar a minha transação se essa transação começar a Gerar inconsistência que seria
21:37
o caso ele não deixaria acontecer é por isso que a gente usa ainda em um bebê porque ela Vai facilitar o nosso
21:43
trabalho é a sua integridade referencial que eu fiz funciona para qualquer uma das três máquinas inclusive com mais a mais o innodb é mais recente então
21:50
utilize ele ou essa bebê e aí a gente chegou um ponto decisivo se eu dou um
21:56
select em gafanhotos eu vejo os dados do gafanhoto e vejo o curso que ele prefere só que não vejo o nome do curso que ele
22:02
prefere eu o código do curso ele prefere te mostrar essa aqui na prática vou apagar tudo aqui que aqui já não eu não
22:09
tenho mais sentido outra coisa que eu posso fazer é deixar esses comandos aqui e clica aqui ó eu acho que é animaizinho
22:14
e ele vai abrir uma nova aba eu tenho os comandos antigos e os comandos novos aqui eu posso fazer isso sem problema algum fazer o seguinte aqui ó
22:22
select* foram gafanhotos se eu faço isso eu tenho lá os dados do gafanhoto se eu
22:28
quiser filtrar coluna eu tiro as três que significa todas as colunas eu vou mostrar somente a coluna nome e a coluna
22:35
curso preferido tá eu tenho aqui ó Daniel Morais prefere o curso seis que é
22:40
onde mais que era que a gente fez anteriormente mas eu não quero que apareça vocês eu quero que apareça mais que é isso é importante isso é
22:46
interessante para você conseguir esse efeito para que você consiga essa solução essa resposta você precisa
22:53
entender as junções das então que a gente tem que fazer agora começar a trabalhar com junsom presta atenção para
23:00
você poder entender o que eu tô falando vou fazer o seguinte a selection
23:05
o asterisco from cursos são mostrar aqui eu mostro os cursos não
23:11
quero mostrar tudo não era mostrar só o nome do curso e o ano dele
23:17
e também mostrei algo o nome do curso e o ano dele o que eu queria era poder juntar isso daqui com isso daqui
23:26
mostrando cada aluno e os cursos que cada um prefere para isso tem que fazer
23:31
o seguinte ó eu vou juntar os dois select nome curso preferido
23:39
o from gafanhotos Joy em
23:44
concursos Johnny é uma junção então vou fazer assim ó dos gafanhotos eu vou
23:50
mostrar um nome tão gafanhotos. Nome
23:57
gafanhotos. Curso preferido foi um gafanhotos de online curso além de café
24:03
eu vou mostrar o nome do curso curso. O nome e curso Ponto ano
24:10
e eu estou juntando gafanhotos concurso poderá controlar
24:16
Inter de eu ir aqui que nós nome da minha tabela na curta curso né vou botar no por aqui o sushi aqui
24:24
cursos aqui mandar controlar Inter agora ele funcionou e olha o que aconteceu vamos analisar
24:31
Daniel Moraes Daniel Moraes Daniel Moraes Daniel Morais agora ele fez todos os cursos o que tá fazendo o seguinte eu
24:37
pedi um joinha e ele mostrou o Daniel junto com todos os cursos você perceber
24:42
que vão dar os 30 cursos para Daniela dá uma olhada todos os cursos estão com Daniel quando terminar os 30 cursos do
24:49
Daniel vai vir a Talita e a Talita também vai ter a relação com os 30 cursos tá lá tu nem 30 curso da Talita
24:57
depois já virou Emerson com todos os 30 cursos também depois depois do Emerson
25:02
vem Lucas Damasceno com todos os 30 cursos o que ele fez foi dar um joinha eles junto só que ele não juntou de
25:09
forma inteligente a junção foi Beleza você quer juntar gafanhoto e curso tá bom cada aluno vai ser junto com todos
25:16
os cursos O que eu preciso fazer é filtrar essas coisas para que eu queria um filtro tem uma cláusula sempre que eu
25:24
usar um joinha eu tenho uma cláusula que é obrigatória querer obrigatória não porque ela funcionou sem essa causa e
25:29
ela é importante para poder dar sentido esse Johnny que a cláusula humano então
25:34
vou fazer seguinte ó select nome do gafanhoto curso preferido o gafanhoto nome do curso ano do curso juntando
25:40
gafanhoto concurso Uno eu vou colocar aqui quais são as relações o gafanhoto
25:46
se liga o curso através de suas chaves estrangeiras e primária Então vou colocar aqui onde a chave primária
25:53
cursos ponto e de curso é igual a chave estrangeira
25:59
gafanhotos. Curso preferido então Acabei de fazer a ligação da minha chave
26:05
primária no relacionamento lembro que a gente fez anteriormente com a chave estrangeira ainda foi outra isso
26:11
relacionamento tente incrível agora quando eu dou contra o Inter que que ele fez Daniel prefere mais Kelly somente
26:17
Talita prefere Premier Emerson prefere ser mais aqui ficou o código do curso
26:22
preferido eu não quero mais ele então posso tirar aqui ó pega fanhoto tirando o curso preferido dele aqui é o nome do
26:30
gafanhoto o nome do curso e o ano do curso controlar a inter eu tenho Daniel prefere que é Eric foi em 2016 Talita
26:37
prefere Premier Emerson preferência mais mais carlison prefere Java o André EA
26:43
prefere premiar viu como funcionou de forma legal então sempre que utilizar o dia em qualquer um dos jovens a gente
26:49
vai ver vários vilões sempre que você utilizar um Joy você tem que utilizar o homem para dar sentido você percebe aqui
26:56
que eu tenho 61 alunos e 30 cursos agora 29 quando ele tem um curso mas então
27:02
tenho 60 alunos e não apareceram e 60 aqui aonde só apareceu esses alunos aqui isso porque quando eu faço um joia só a
27:09
palavra Joy eu tô fazendo o que a gente chama de Inner John é um joia somente com as relações com uma olhada aquele
27:16
gafanhotos Se eu der um select* from os gafanhotos
27:22
ele vai me mostrar todos os gafanhotos percebe aqui que os que têm curso preferido São só esses aqui ó o Daniel
27:29
Ah tá até aqui até Andreia Daniel Talita Emerson Lucas Leila Letícia né somente
27:36
esses alunos têm curso preferido os demais não tem eu vou botar aqui a Rosana A Rosana vai preferir o curso um
27:43
também vamos dar a praia aqui no final aqui vamos dar apply aplicar as alterações Pode fechar janela
27:51
e agora eu vou fazer de novo aquele comando do Johnny ó eu tenho Daniel
27:56
Talita e agora entrou a Rosana na lista que não estava Ela prefere o curso HTML5 foi criado em 2014 Deu para entender o
28:04
que estou indo Joy ele vai somente fazer quase tem a ligações mas tem aquelas linhas coloridas lá no desenho que a
28:11
gente já vai ver de novo então um herói ele simplesmente vai ver o que que tem relação nas duas tabelas Como eu disse
28:18
Esse é um Inner join então eu posso escrever só o hino Joy é especificar vamos vai dar o
28:25
mesmo resultado aqui se você quiser pois ela não está em ordem de nome de aluno eu quero em nome de aluno que eu posso
28:30
vir aqui botar Order by que a gente já viu os
28:36
gafanhotos. Nome lá nome control enter agora eles estão em ordem alfabética de
28:43
nome eu posso fazer nada também por ordem alfabética licor Deu para entender então isso é o Windows vai só para dar
28:48
uma relembrada você pode trabalhar com apelidos de coluna apelidos de coluna a gente usa a palavra és ou simplesmente
28:55
não usa a palavra vão utilizar o ex aqui então que eu vou fazer que é gafanhotos és G Então sempre que eu vou me referir
29:03
a gafanhoto posso usar o g e cursos é esse Então sempre que eu vou me referir
29:08
a curso eu posso me referir a ser isso vai diminuir bastante meu comando Então posso botar em vez de gafanhoto G em vez
29:14
de curso se em todas as ocorrências a hora que eu tô fazendo tô Apagando tudo aqui ó Então vou apagar aqui também
29:21
deixa a ser Vou apagar aqui também deixa agir Vou apagar aqui também deixa agir a
29:27
única coisa que eu tenho que deixar escrito gafanhotos é depois do fronto e depois do joia Então eu tenho que o
29:33
pedido uma vez né então coloca aqui ó o apelido sempre que fala de gafanhoto é G sempre fala de curso é ser e todos os
29:41
outros eu posso utilizar para votar contou entre aqui você vai ver que o comando funciona da mesma maneira que a
29:46
gente quer nem de onde são muito importantes e muita gente acha que isso é difícil você viu que eu fiz um John
29:52
simples ele diz qual tabela que ele relacionar com qual e utilizei o ônibus para ligar a chave primária chave
29:58
estrangeira dela então você precisa antes planejar Qual é a estrutura da sua tabela para você poder saber o que que a
30:04
chave primária que a chave estrangeira fazer a sua configuração adicionando a forma que e botar para funcionar mais
30:11
uma vez eu quero deixar bem claro não é tão fácil fazer isso então às vezes você tem que assistir essa aula mais uma vez
30:17
sempre colocar em prática não adianta você ficar olhando ou fazendo e fazer ela tá aí ó eu aprendi que legal aonde
30:23
você botar a mão na massa você vai esquecer a abre seu ambiente assistir a sala eu gosto sempre de indicar o
30:29
seguinte assistir aula primeiro da pressa estava toda que é você já vai ter o primeiro contato em volta da Play de novo só que dessa
30:36
vez você usa o pause vai fazendo os paus vai fazendo vai repetindo que eu tô
30:41
fazendo E aí sim você vai ter prática na hora de você poder criar o seu próprio exercício então a minha junção funcionar
30:48
da seguinte maneira eu tenho aqui aquela imagem que a gente viu anteriormente eu tenho os gafanhotos de um lado eu tenho
30:55
os cursos do outro e aqui no meio Eu tenho as ligações então percebe o seguinte aqui nesse exemplo o curso de
31:01
PHP ninguém prefere o curso de Java ninguém prefere e aqui desse lado eu tenho esse cara que não prefere pulso
31:06
nenhum que é o caso lá daquelas linhas que estão com Lulu Então existe em casa aqui na tela curso que eu tenho cursos
31:12
que não são preferidos por ninguém e eu também tenho casos aqui em gafanhotos que tem gafanhoto que não prefere nada o que me interessa no herói são essas
31:19
linhas coloridas então um erjon ele vai pegar essa área e vai fazer a ligação e
31:26
além do Windows onde a gente tem os autores jovens water Johnny ele vai tratar exatamente os conceitos do hino é
31:33
muito com aqueles dados que não tem relação com nenhuma outra tabela então preste atenção aqui nesse caso aqui eu
31:39
tenho gafanhoto ele tá me mostrando seu usar o Whindersson ele vai mostrar só esses três já foi outros que preferem
31:45
esses dois cursos aqui as barbáries se eu quiser mostrar todos os gafanhotos mesmo se não preferem nada aí eu vou
31:51
mostrar um negócio para você então mantendo esse mesmo comando a seguinte seu moto ir no Joy ele tá fazendo
31:57
somente os alunos lá até a Talita que somente esses alunos eles têm relação
32:03
com o outro se eu vem aqui e boto autor eu vou considerar inclusive os campos
32:08
que não fazem parte só que aí eu tenho que perceber o seguinte vamos procurar onde é que tá o joinha aqui deixa eu
32:14
apagar isso aqui vamos identificar onde é que tá o Johnny o Johnny tá aqui a esquerda do Johnny tá tabela gafanhotos
32:21
à direita do Johnny tabela curso Então eu tenho uma tabela a esquerda e uma
32:27
tabela direita do John de ontem gafanhotos a esquerda e cursos à direita
32:32
então eu vou considerar e a tabela da esquerda é a Canhoto e a tabela da direita ecos então vou fazer o seguinte
32:39
se eu quiser mostrar todos os gafanhotos inclusive aqueles que não preferem nada
32:44
eu vou utilizar um autor jovem só que se alterar Eu Tenho duas possibilidades ou
32:50
eu vou considerar gafanhotos como preferencial ou cursos com preferencial os considerar primeiro gafanhotos
32:56
Lembrando que a França está à esquerda do joia Então vou colocar aqui left Out
33:01
Boy quando eu do control center olha só o que ele fez ele botou em ordem Deixa
33:06
eu tirar esse lado e vai aqui para você poder entender que eu tô fazendo controlar a gente você percebe aqui ó
33:13
Daniel para sair mais que ela e Talita até a Rosana Andrea Rosana panela a usando que eu coloquei aqui você percebe
33:19
que ele mostrou todos os alunos isso é ele deu preferência para minha coluna da
33:25
esquerda se ele mostrou os alunos independente de quem prefere ou não Por exemplo eu sei que Daniel prefere mais
33:30
Kelly eu sei que Jackson prefere photoshop e eu o Walter não preferem nada e aí deu para entender os apps Joy
33:38
como gafanhotos tá do lado esquerdo nesse meu comando ele está dando preferência left alterações isso é ele
33:44
vai aparecer dando preferência minha tabela da esquerda que no meu caso aqui é que foi outra eu posso chamar de Leste
33:50
ao ter de uma ou simplesmente Leste o seu supremo a palavra alter ele vai considerar como left join left out já
33:58
estamos a falar da mesma maneira tá vendo ali então ele tá aqui ó eu tô fazendo Joe a esquerda eu tenho
34:04
gafanhoto a direito tenho curso tô dando preferência para gafanhotos EA maneira similar eu posso dar preferência por
34:10
lado direito isso é eu tô dando preferência para cursos eu quero mostrar todos os cursos inclusive aqueles que
34:16
nenhum aluno prefere e dá uma olhada aqui se eu der um right
34:22
out Joy ou simplesmente ri Johnny eu vou controlar entra eu estou mostrando o
34:28
Leila prefere HTML Rosana também prefere HTML claro que eu tenho repetição aqui porque como eu disse anteriormente cada
34:35
gafanhoto só pode preferir um curso mas eu posso ter um curso preferido por vários gafanhoto Você viu como é que a
34:42
teoria se junta na prática agora eu dei preferência agora para lado direito pra tinha tabela que está do lado direito
34:47
aqui no caso é o curso Nossa o seu olhar aqui ó vamos procurar onde é que tá o Johnny tá aqui vai ter o teu Joy do lado
34:53
esquerdo tá gafanhoto do lado direito tá curto então tô dando preferência para curso Ele tá mostrando todos os cursos
34:58
inclusive aqueles que não tem nenhuma coisa pior ninguém gosta Excel ninguém prefere responsabilidade ninguém prefere
35:05
Android e prefere E aí ficou confuso vou te mostrar a forma de imagem para você poder entender como nós vimos
35:11
anteriormente o meu Miller John é a ligação ele vai considerar somente as linhas as ligações vai considerar suas E
35:17
ai outros que preferem determinado curso Deve mostrar só esses três gafanhotos porque eles têm preferências e só esses
35:24
dois cursos aqui porque eles são preferidos se eu quiser dar preferência para gafanhoto aqui A garrafa está em
35:30
qual lado tá do lado esquerdo não tá então eu dou um left Out Boy ou simplesmente leve Joy se eu quiser de
35:36
preferência para cursos eu quero mostrar os cursos inclusive de pegar page Java que ninguém prefere então eu dou um
35:43
reach Out Boy ou simplesmente White J E aí muito difícil então se eu coloco
35:50
somente John eu estou me referindo ao energia se eu quiser referir ao alternion eu posso colocar vai tchau
35:56
desde ontem ou simplesmente White Johnny ou left out on ou simplesmente let Joy é
36:02
assim que funciona o relacionamento entre tabelas mostrando determinados dados de acordo o que que eu preciso na
36:08
minha necessidade achou difícil achou complicado a dica a seguinte se você não entendeu ainda é porque você não tá
36:15
conseguindo ligar a Teoria com a prática bom então vai por mim primeiro o ideal é que você assista a Playlist inteira todo
36:22
o curso porque é cada aula vai te dando um passo Inicial aqui tá não passa na frente do outro se você caiu de
36:28
paraquedas aqui nessa aula paga aula de Jó empurra aula de joia é o que eu quero então assistir E você tá meio perdido é
36:34
porque você não assistiu aula 14 que fala um pouco sobre o modelo relacional e como criar um diagrama entidade-relacionamento definir as
36:41
cardinalidades e definir as chaves primárias e estrangeiras sem esse conceito eu não vai entender dá uma
36:46
olhada primeiro assistir o cônsul todo se por acaso você já assistiu o curso todo você volta só na aula 14 assistir
36:53
ela de novo Faz essa aula 15 e prática se você colocar em prática eu garanto
36:58
que você vai conseguir Então é isso que andar foi outro a gente chegou ao fim dessa 15ª aula e eu tenho uma notícia um
37:04
tanto quanto triste para te dar a próxima aula que a aula 16 é a última aula do nosso curso demais cidades mas
37:11
não precisa ficar triste porque logo em seguida a gente vai fazer outro curso é uma novidade bem legal aqui para vocês
37:16
não conseguir a falar de Joy eu considero ainda como uma coisa bem simples e isso caberia não
37:23
curso de introdução ao banco de dados mas você pode perceber que na sua faculdade no seu colégio o professor não
37:28
teve tanta paciência assim para te explicar se ele teve Parabéns professor se ele não teve você tá aprendendo e
37:34
pode mostrar para seus colegas então nunca se esqueça você pode né Sempre aquela coisa de sempre assinar o canal e
37:41
sempre que tiver uma aula nova você vai conseguir ver se você tiver vendo do celular vai numa aula Marca um Sininho
37:47
né temos um ícone Zinho do Sino marca esse sim você vai ser avisado se você tá usando o computador vai no inscrever no
37:53
canal depois você se inscrever do lado do inscreva-se vai ter uma engrenagem clica nela e Marco opção que era o
38:00
receber e-mail sempre tiver uma aula nova você vai ver faz isso pela gente e faz isso por você porque você vai
38:05
aprender sempre mais desse lado aqui você vai ver a Playlist que eu já falei tantas vezes a ficha playlist assistir o
38:11
vídeo da vida aqui no meu a diferença completa
38:18
você vai acessar o curso em video. Com e lá você vai ter acesso a todos os materiais o daqui do banco de dados os
38:25
slides as aulas tudo organizadinho tudo de forma simples e objetiva e também
38:31
existe a forma de interatividade principalmente o celular se você tá no celular você não tá conseguindo clicar em nada aqui aqui em cima aqui vai ter
38:37
playlist vai ter acesso a aula a outros cursos que a gente está indicando então seguinte você tá aprendendo banco de
38:43
dados está gostando dois cursos que eu indico bastante que tão aqui em cima com certeza Então se algoritmo e o curso de
38:49
PHP porque Vai juntar tudo isso algoritmo therapy Já va vamos se juntar banco de dados mas na frente na vida do
38:56
curso em vídeo e na sua vida profissional então esperando já foi outro me despeço por aqui todas as
39:02
nossas redes sociais estão disponíveis na descrição do vídeo então adiciona a gente o Facebook Instagram e tudo mais
39:07
um sempre bota coisa nova tem conteúdo exclusivo para quem segue a gente no Facebook sempre que eu faço viagem
39:13
sempre que eu participo de alguma coisa eu tô indo lá no Facebook e postar Ah tá moral para gente umas Facebook
39:20
facebook.com/cursos em vídeo não tinha curso em vídeo vou te botar cursos em vídeo é um curso em vídeo tudo junto sem
39:27
espaço nem adiciona a gente a rede social lá a gente sempre vai bater papo de uma maneira mais perto e sempre
39:33
assista o seguinte responde a gente sempre tá lá falando algumas coisas falando besteira respondendo as
39:39
perguntas e tudo mais se você não viu vai lá na associação de playlists do canal e procuro cursivo de responde tem
39:44
muita coisa legal inclusive um vídeo onde eu Visitei o Google e nesse vídeo da visita do Google olha só que eu
39:50
ganhei a alegria até careca do YouTube ele tá com cogumelo dentro para ela
39:55
poder crescer muito obrigado por ficar até aqui no finalzinho tem muito café porque não fica até o final você ficou
40:01
deixe um comentário aqui embaixo eu fiquei até o final Olha que legal persista nisso daí às vezes algumas informações legais como por exemplo que
40:07
essa é a pena última aula do curso Estuda bastante essa coisa do John que na hora que vem a gente vai dar
40:12
continuidade e eu vou mostrar para o finalzinho como é que eu faço um relacionamento como é que eu o que uma
40:18
tabela muitos-para-muitos Aí sim começa a ficar avançado e por isso que a gente interrompe o curso na próxima aula um
40:25
forte abraço pratique trem nessa parada aqui para você vai precisar disso na hora 16 na hora 16 vai vir Guanabara
40:31
chato falando que você precisa assistir aula 14 a 15 forte abraço foi outra até
40:37
a próxima
"""



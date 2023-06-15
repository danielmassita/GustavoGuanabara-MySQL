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






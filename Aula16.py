# Curso MySQL #16 - INNER JOIN com várias tabelas
# https://youtu.be/jx2ne8iZMOA
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/inner-join-com-varias-tabelas/

""" 
[Gafanhoto] n--------- <Assiste a> ---------n [Curso]
- id (pk)                                   - idcurso (pk)
- nome                                      - nome 
- sexo                                      - descricao 
- nascimento                                - aulas 

Classificação de Relacionamento: Cardinalidade de muitos-para-muitos (N-to-N).
Regra de N-para-N, nas extremidades (N), vou trazer pro meio uma NOVA entidade <antiga Relação: Assiste> com novos relacionamentos das extremidades. 

[Gafanhoto] ---1-------n--- [Assiste] ---n-------1--- [Curso]
- id (pk) >>>               - id (pk)             <<<   - idcurso (pk)
- nome                      - data                      - nome 
- sexo                  >>> - idgafanhotos (FK)         - descricao 
- nascimento                - idcurso (FK)  <<<         - aulas 

Entidade 'gafanhotos' possui 'id' como primary key pra cada alunos.
Entidade 'cursos' possui 'idcurso' como primary key pra cada curso.
Entidade 'assiste' possui 'id' como primary key, idgafanhoto e idcurso como Foreign Keys.

Técnica aula passada: Trazer a chave primária do Lado-1 para o Lado-N-muitos, duas vezes.

# CRIANDO A TABELA EXTRA
CREATE TABLE gafanhoto_assiste_curso (
  id int NOT NULL AUTO_INCREMENT,
  data date,
  idgafanhoto int,
  idcurso int,
  
  PRIMARY KEY (id),
  FOREIGN KEY (idgafanhoto) REFERENCES gafanhotos(id)
  FOREIGN KEY (idcurso) REFERENCES cursos(idcurso)
) DEFAULT CHARSET = utf8;

# A chave estrangeira DEVE ser do mesmo TIPO da chave primária.
"""

# XAMP Server + MySQL Workbench
USE cadastro;

CREATE TABLE gafanhoto_assiste_curso (
	id int NOT NULL AUTO_INCREMENT,
    data date,
    idgafanhoto int,
    idcurso int,
    
    PRIMARY KEY (id),
    FOREIGN KEY (idgafanhoto) REFERENCES gafanhotos(id),
    FOREIGN KEY (idcurso) REFERENCES cursos(idcurso)
) DEFAULT CHARSET = utf8;
# 1	2	17:06:00	CREATE TABLE gafanhoto_assiste_curso (3719 'utf8' is currently an alias for the character set UTF8MB3, but will be an alias for UTF8MB4 in a future release. Please consider using UTF8MB4 in order to be unambiguous.	1.672 sec

""" Vamos elaborar o exemplo:

[Gafanhoto] ---1-------n--- [Assiste] ---n-------1--- [Curso]

- Menino                 menino.[  ].hmtl5               - HTML5
                         menino.[  ].word            
                         
- Godofredo           godofredo.[  ].hmtl5               - PHP 
                      godofredo.[  ].php
                      
- Dolores               dolores.[  ].html                - Word
                        dolores.[  ].php                     
                        dolores.[  ].word                     

# Cada pessoa pode assistir a vários cursos.
# Cada curso pode ser visto por várias pessoas. 
"""

# INSERINDO REGISTROS DENTRO DA NOVA TABELA

INSERT INTO gafanhoto_assiste_curso VALUES
(DEFAULT, '2014-03-01', '1', '2');
# 3	3	17:32:41	INSERT INTO gafanhoto_assiste_curso VALUES (DEFAULT, '2014-03-01', '1', '2')	1 row(s) affected	0.203 sec

SELECT * FROM gafanhoto_assiste_curso;

# Vamos usar a tabela do MySQL pra adicionar manualmente novos registros...
INSERT INTO `cadastro`.`gafanhoto_assiste_curso` (`data`, `idgafanhoto`, `idcurso`) VALUES ('2015-12-22', '3', '6');
INSERT INTO `cadastro`.`gafanhoto_assiste_curso` (`data`, `idgafanhoto`, `idcurso`) VALUES ('2014-01-01', '22', '12');
INSERT INTO `cadastro`.`gafanhoto_assiste_curso` (`data`, `idgafanhoto`, `idcurso`) VALUES ('2016-05-12', '1', '19');


"""
JUNÇÕES (INNER JOIN ou apenas JOIN)

[gafanhoto]		[assiste]		[curso]
id (pk)			idgafanhoto (fk)	idcurso (pk)
			idcurso (fk)


SELECT * FROM gafanhotos g
JOIN gafanhoto_assiste_curso a
ON g.id = a.idgafanhoto;

1	Daniel Morais	Auxiliar Administrat	1984-01-02	M	78.50	1.83	Brasil	6	1	2014-03-01	1	2
3	Emerson Gabriel	Programador	1920-12-30	M	50.20	1.65	Moçambique	12	2	2015-12-22	3	6
22	Guilherme de Sousa	Dentista	2001-05-18	M	132.70	1.97	Moçambique		3	2014-01-01	22	12
1	Daniel Morais	Auxiliar Administrat	1984-01-02	M	78.50	1.83	Brasil	6	4	2016-05-12	1	19
"""


# Vamos começar a trabalhar com a tabela, fazendo uma parte primeiro (gafanhotos), depois a outra (cursos).
SELECT g.id, g.nome, a.idgafanhoto, idcurso FROM gafanhotos g
JOIN gafanhoto_assiste_curso a
ON g.id = a.idgafanhoto;
"""
1	Daniel Morais	1	2
3	Emerson Gabriel	3	6
22	Guilherme de Sousa	22	12
1	Daniel Morais	1	19
"""


# Selecionando os nomes e os id's dos cursos.
SELECT g.nome, idcurso FROM gafanhotos g
JOIN gafanhoto_assiste_curso a
ON g.id = a.idgafanhoto
ORDER BY g.nome;
"""
Daniel Morais		2
Daniel Morais		19
Emerson Gabriel		6
Guilherme de Sousa	12"""


# Mas eu não quero o ID do curso, quero os nomes dos cursos...
SELECT * FROM gafanhotos AS g
JOIN gafanhoto_assiste_curso AS a
ON g.id = a.idgafanhoto
JOIN cursos AS c
ON a.idcurso = c.idcurso;

# MySQL Workbench
SELECT g.nome, a.idcurso FROM gafanhotos AS g
JOIN gafanhoto_assiste_curso AS a
ON g.id = a.idgafanhoto
JOIN cursos AS c
ON c.idcurso = a.idcurso
ORDER BY g.nome;
"""
Daniel Morais	2
Daniel Morais	19
Emerson Gabriel	6
Guilherme de Sousa	12
"""


SELECT g.nome, c.nome FROM gafanhotos AS g
JOIN gafanhoto_assiste_curso AS a
ON g.id = a.idgafanhoto
JOIN cursos AS c
ON c.idcurso = a.idcurso
ORDER BY g.nome;
"""
Daniel Morais		Algoritmos
Daniel Morais		Redes
Emerson Gabriel		MySQL
Guilherme de Sousa	C++
"""





"""
Transcrição


0:00
♫ Cantarolando. ♫
0:05
Vinheta de abertura. ♫
0:20
Olá, pequeno gafanhoto! Seja bem vindo a mais uma aula do seu curso de banco de dados com MySQL!
0:25
Infelizmente, a última aula.
0:28
O meu nome é Gustavo Guanabra, eu sou seu professor,
0:30
e nessa última aula do seu curso de banco de dados
0:33
nós vamos terminar um assunto que ficou aberto da última aula.
0:37
Nós vamos voltar a falar sobre o relacionamento entre tabelas,
0:40
e essa é a terceira e última parte sobre o assunto
0:44
Siiiim!
0:45
O que a gente tinha visto na aula passada, foi o relacionamento de uma tabela
0:48
de um para muitos. E ai ficou aquela dúvida: Tá, mas a gente tem o relacionamento de um para um,
0:53
você ensinou como é que faz com a chave.
0:55
A gente tem o relacionamento de um para muitos,
0:56
você também ensinou na aula passada e mostrou até na prática como é que faz.
0:59
Mas ficou aberto aquele assunto do relacionamento de muitos para muitos.
1:04
Eu tenho muitas instâncias de um lado e muitas instâncias do outro, e elas estão se relacionando.
1:09
Como é que eu faço isso na prática?
1:11
Porque é um tipo de relacionamento que acontece constantemente e que
1:14
você vai ter que aprender a utilizar.
1:16
Então, essa última aula, eu reservei para me despedir de vocês e para mostrar
1:20
esse importante recurso que você vai precisar caso você queira criar um banco de dados
1:24
um pouquinho mais parrudo.
1:25
Mais uma vez eu quero informar...
1:26
"Péra ai", mais uma vez eu quero tirar esse óculos porquê eu não consigo olhar com esse negócio aqui
1:31
Vamos lá!
1:31
Então vamos voltar.
1:32
Mais uma vez, eu queria agradecer a você, por todo esse carinho, e eu queria mudar um pouquinho o protocolo
1:38
Eu queria te dizer o seguinte:
1:40
Nunca se esqueça, olha aqui ó:
1:41
Aquele "coisa" de sempre.
1:43
Clicando aqui, você assina o canal. O curso tá acabando, assina o canal, vai vir mais outro curso aí.
1:48
Não vai emendar uma semana na outra não,
1:50
mas o próximo curso ta vindo aí com muita novidade.
1:53
Aqui desse lado, você vai ser desviado diretamente para a Playlist.
1:56
Assista o nosso curso sempre pelas Playlist's.
1:59
Porque assim, é mais fácil para você se organizar,
2:02
você vê o que você já assistiu e o que você não assistiu,
2:04
facilita para a gente, porquê a gente mantém você na sequência, e outra coisa, nunca se esqueça, nunca
2:11
se esqueça, você precisa fazer essas aulas fazendo na prática.
2:16
Não adianta. Tem gente que fala: "Ah, eu não entendi nada de HTML."
2:19
Você praticou? "Ah, não, não. Só assisti a aula."
2:21
Não adianta, meu filho!
2:23
Você precisa praticar, MySQL também, são muitos comandos, são muitos detalhes,
2:28
a gente fez um "funkzinho", né?! Lembra de um funkzinho?" Que tá lá...
2:31
♫ Create table, cria uma tabela, ♫
2:35
♫ Alter table, mexe na tabela... ♫
2:37
Eu tentei fazer de tudo para facilitar o seu aprendizado.
2:40
Eu espero sinceramente, de coração, que eu tenha conseguido.
2:44
Parte do esforço é meu, de construir aula, construir músicas, de construir os slides...
2:49
E parte é sua, de praticar, de treinar, de colocar tudo e...
2:53
de criar um banco de dados que vem da sua cabeça, ou que você ta precisando, da sua necessidade.
2:58
Só desse jeito, só dessa maneira, você vai conseguir aprender banco de dados
3:01
Vamos parar de enrolação, vamos para os nossos slides que eles estão caprichados.
3:05
Vamos dar uma recordada no que a gente fez aula passada antes de começar da nossa necessidade
3:10
daqui pra frente.
3:11
Se você se lembra muito bem, esse foi o diagrama entidade relacionamento que a gente
3:14
construiu na aula passada.
3:16
E que nós fizemos o relacionamento onde o gafanhoto prefere um determinado curso
3:20
E preferir, nós entramos num consenso que você não prefere muitas coisas, você prefere uma coisa.
3:25
É o seu curso preferido, é o seu curso predileto.
3:28
Isso nos gera um relacionamento de uma instância de um lado, com muitas instâncias de outro.
3:33
Sendo assim, o que nós resolvemos é que:
3:35
Cada gafanhoto só pode preferir um curso,
3:38
E cada curso pode ser preferido por vários gafanhotos.
3:41
A técnica que eu utilizava para fazer esse tipo de relacionamento
3:45
era trazer a chave primária do lado um para o lado muitos.
3:48
Então eu trazia o "idcurso" de curso, diretamente para o lado do gafanhoto.
3:53
Então, curso preferido viraria uma chave estrangeira.
3:57
Isso porque ele era uma chave primária em outro lado.
3:59
Até aí, tudo bem, até aí tudo perfeito.
4:02
Mas e os relacionamento muitos para muitos?
4:04
Como é que eu vou fazer a dinâmica das chaves?
4:07
A gente viu isso na primeira parte dessa aula de relacionamentos.
4:10
Então se você não viu ainda, ou se você já viu mas se esqueceu, dá uma revisada sempre, Playlist aqui ó:
4:16
Procura a aula quatorze. Se eu não me engano é a aula quatorze.
4:19
Que é a aula que fala sobre diagrama entidade relacionamento.
4:22
É a aula que fala sobre o modelo relacional.
4:24
Mas vamos ver uma outra situação aqui. Vamos ver um outro tipo de relacionamento que pode existir
4:28
entre gafanhoto e cursos.
4:29
Você não necessariamente tem um tipo de relacionamento entre duas entidades,
4:32
podem ter vários relacionamentos.
4:34
O exemplo que eu separei aqui ó:
4:35
É o gafanhoto assistir um determinado curso.
4:39
Então, gafanhoto - assiste - curso.
4:41
Como é que eu faço aqui? Eu vou fazer com que cada gafanhoto possa assistir vários cursos,
4:46
então ele vai gerar um "n" ali, e que cada curso possa ser assistido por vários gafanhotos também.
4:51
Isso nos gera um relacionamento "assiste" que é da cardinalidade muitos para muitos,
4:57
então, eu classifico esse relacionamento como um relacionamento de cardinalidade muitos para muitos.
5:02
E você deve se lembrar muito bem. Ou então você vai precisar dar uma recordada na aula quatorze.
5:07
Eu não tenho certeza se é quatorze não. Dá uma olhada lá, que é a aula de modelo relacional.
5:11
O que que vai acontecer quando eu tenho um relacionamento de muitos para muitos?
5:13
Segue aqui com o tio. Eu vou fazer o seguinte:
5:16
Esse "n" que era nas extremidades, eu vou trazer ele para o meio,
5:19
vou transformar "assiste" em uma entidade. Olha lá o que aconteceu.
5:23
E vou colocar as cardinalidades 1 do lado de fora, criando novos relacionamentos.
5:28
Então essa é a técnica.
5:29
E a partir daí eu gerei dois relacionamentos de um para muitos, e ai eu vou utilizar as mesmas técnicas
5:35
que eu utilizei anteriormente.
5:36
Eu vou criar novos atributos, por exemplo, quem assiste, eu vou ter um identificador para assistir e vou ter a data
5:42
em que ele começou a assistir um curso, por exemplo, e eu vou ter que trazer as chaves.
5:45
Então eu vou trazer a chave primária de gafanhoto, eu vou trazer o "id" de gafanhoto para dentro de "assiste"
5:50
como uma chave estrangeira. Vou chamar de "idgafanhoto."
5:53
Vou trazer também a chave primária de curso, que é "idcurso" para dentro do "assiste"
5:57
também como chave estrangeira, e eu vou chamar de "idcurso."
6:00
Então eu utilizei aquela técnica da aula passada, que é trazer a chave primária do lado 1 para o lado muitos
6:06
duas, vezes, porque eu tenho dois relacionamentos.
6:08
E ai eu tenho essa essa entidade central, e essa entidade central vai ter os dois atributos normais dela
6:13
que são "id" e "data". E também dois atributos especiais que serão chaves estrangeiras.
6:18
Para fazer isso então, eu vou ter que utilizar o "CREATE TABLE", que é aquele comando que a gente já
6:22
utiliza a algum tempo.
6:23
Então eu vou botar lá, CREATE TABLE, gafanhoto_assiste_curso (.
6:26
O nome dessa tabela pode ser qualquer um. Eu vou utilizar esse daqui por questões de didática,
6:30
mas tem gente que só coloca, por exemplo, "assiste", tem gente que coloca, por exemplo, "gassistec", né....
6:36
Mas eu vou utilizar nomes mais completos, só pra gente poder entender melhor e fixar esses conteúdos.
6:41
E ai eu vou colocar os atributos, como eu disse lá ó, por exemplo, eu vou criar um identificador de "assistir".
6:46
Então eu vou colocar "id int NOT NULL AUTO_INCREMENT, "
6:50
O "NOT NULL" ali é meio opcional, porque quando eu colocar ele como chave primária, automaticamente
6:54
ele vai virar "NOT NULL". Mas eu vou colocar explicitando também, por questões educacionais.
6:59
O segundo atributo é a data. Eu vou colocar "data", que é do tipo "date". Coloco uma vírgula. Vou colocar os dois
7:04
atributos que vão servir de chave estrangeira. Ó, o "idgafanhoto", que é do tipo "int"
7:08
Nunca se esqueça, não é necessariamente do tipo "int". Nem toda chave estrangeira é do tipo "int", mas,
7:14
ela tem que ser do mesmo tipo da chave primária originária. Então, a chave estrangeira tem que ser do
7:19
mesmo tipo da chave primária. Até porque, a chave estrangeira é uma chave primária que está em
7:23
outro lugar.
7:24
Então elas têm que ser do mesmo tipo. Não precisa ser do mesmo nome, mas o tipo tem que ser seguido.
7:28
Também vou criar o "idcurso". E agora nós vamos definir a chave primária.
7:32
Vou colocar "PRIMARY KEY (id)". Esse "id", é o "id" lá de cima.
7:36
É esse "id" daqui. Então eu vou colocar aqui, minha chave primária dessa tabela, vai ser "id", que é esse
7:41
atributo daqui de cima. Agora eu tenho que definir aqui embaixo, as duas chaves estrangeiras.
7:46
Sim, duas chaves estrangeiras, porque a gente viu, que vai vir uma chave primária de cada lado, e vai se juntar
7:51
a essa entidade nova. Para fazer isso, a gente vai usar a mesa técnica da aula passada. Nós vamos colocar lá,
7:56
FOREIGN KEY (idgafanhoto) REFERENCES gafanhotos (id),
8:00
Isso é, eu vou fazer com que esse "idgafanhoto" aqui, se ligue com o "id" da tabela de gafanhotos.
8:07
Caso você tenha dificuldade em entender isso, é porque você não assistiu direito a aula passada.
8:11
Então vai lá na aula quinze e assiste direito, pequeno gafanhoto.
8:14
Essa que é a vantagem da gente ir para a playlist. Eu tô sempre te jogando para um lado e para o outro.
8:18
Dá uma olhada na playlist. Eu não lembro se é desse lado ou desse lado que fica uma lista.
8:23
Em um dos lados está a playslist. Ou então aqui em cima, clica aqui em cima no "i" interativo.
8:27
Clicou, vai aparecer aqui do lado, você clica lá na playlist e vai diretamente para a aula quinze.
8:32
Então na aula quinze eu ensinei o uso do FOREIGN KEY com o REFERENCES.
8:36
Você precisa entender isso porque eu vou fazer isso duas vezes.
8:39
Se você não entender como faz uma vez só, como é que você vai conseguir entender duas?
8:42
E também você vai conseguir compreender a integridade referencial. Como é que funciona
8:47
a integridade referencial. Eu não vou explicar isso de novo. Você cria relações entre as tabelas, onde você não
8:52
permite atualizações, exclusões desnecessárias ou que tenham dados relacionados.
8:57
É muita importante que você entenda isso, até pra você poder justificar o uso das FOREIGN KEYS.
9:02
E vou criar uma segunda FOREIGN KEY, como eu já sugeri aqui, que é a FOREIGN KEY do "idcurso", ondeu eu
9:07
vou fazer com que o "idcurso" que é esse meu atributo daqui se relacione com o "idcurso" da tabela curso.
9:12
Então agora, chegou aquela hora. Estala os dedos, estica as costas, abre o seu ambiente, abre
9:18
todo o seu servidor, abre o Workbench, e vamos trabalhar.
9:21
♫ Efeito de transição.♫
9:23
Então já estou aqui no Workbench, meu banco de dados não está aberto, então eu vou colocar lá
9:26
"use cadastro;"
9:28
Então, já estou lá com o cadastro.
9:30
Eu tenho as tabelas curso e gafanhoto, está tudo lá bonitinho, como na aula passada.
9:34
Vamos fazer aquele "CREATE TABLE" que a gente usou agora.
9:37
vou colocar "create table", vou colocar "gafanhoto_assiste_curso", abro parênteses, fecho
9:44
parênteses. Vou colocar aqui meu "default charset" pro "utf8", só para não esquecer lá no final.
9:51
E agora vamos colocar os atributos aqui. Aqui dentro eu vou ter o "id" da minha tabela,
9:56
vou criar com o "int not null" e "auto_increment". Tem um underline aqui.
10:04
Com o strength ele é bem limitado com relação a isso.
10:07
Ponto e vírgula não, maldito! Vírgula.
10:09
Vou colocar aqui também a data,
10:12
que é "date",
10:14
vou colocar também as minha chaves estrangeiras,
10:18
"Idgafanhoto int",
10:21
e o "idcurso int".
10:23
A chave estrangeira também. Se lá na sua chave primária você tiver alguma com um strength especial
10:28
como por exemplo o default e tal, você também tem que colocar aqui.
10:30
Vamos fazer agora a chave primária.
10:32
Então eu vou colocar aqui "primary key", entre parênteses eu vou colocar "id", referenciando a esse "id"
10:38
"id" daqui de cima.
10:39
também vamos colocar algumas "foreign key".
10:42
Tem gente que pergunta como é que faz para poder aparecer esse simplificado aqui.
10:45
Se você fizer com pressa ele não aparece, mas se você apertar "f" e esperar 1 segundo, 1 segundo e meio,
10:50
ele vai começar a te ajudar.
10:51
"foreign key", entre parênteses "idgafanhoto", que é o campo daqui de cima "references", a minha tabela,
11:00
que é gafanhotos,
11:03
e o campo "id", que é o campo "id" de gafanhotos.
11:06
Se você tiver dúvidas, você vem aqui em tabelas, abre a tabela gafanhotos, abre a tabela columns, né, já que a
11:12
coluna são os atributos da tabela. Eu tenho lá, ó, "id".
11:17
Vou deixar fechado aqui.
11:18
E vou criar a minha segunda "foreign key" que é a "idcurso",
11:23
que vai referenciar,
11:25
na tabela cursos,
11:27
o "idcurso".
11:30
Acabou que ficou com o mesmo nome, né?! "idcurso" aqui, "idcurso" aqui, você pode confundir.
11:33
Esse "idcruso" daqui, é esse "idcurso" aqui de cima.
11:37
Esse "idcurso" daqui, é esse "idcurso" de cursos. Então se eu abrir a tabela cursos de maneira similar, vai ter lá
11:43
"idcursos", que é o meu atributo.
11:45
Colocamos a estrutura aqui. Vamos pressionar Ctrl+Enter. Ele já criou a minha tabela.
11:51
Vamos atualizar aqui e ver se ele já criou a tabela aqui, ó.
11:53
Agora eu tenho cursos, gafanhotos, e eu tenho gafanhoto_assiste_curso.
11:57
A nossa tabela está pronta. Agora a gente tem que entender como é que eu coloco o dado lá dentro,
12:01
que tipo de relação a gente vai fazer. Mais uma vez, eu vou trazer aquele meu exemplo que eu
12:06
sempre faço com vocês.
12:07
Vou dar aquela expandida caprichada aqui nas minhas entidades, então eu tenho gafanhoto assiste curso,
12:11
e então vamos colocar alguns gafanhotos do lado esquerdo e vamos colocar alguns cursos do lado direito.
12:16
Vamos fazer o seguinte: primeiro gafanhoto ali de cima,
12:19
ele vai assistir o curso de HTML 5, por exemplo.
12:22
Então eu vou fazer o gafanhoto, assiste, vou criar uma instância no do meio, e vou fazer ele assistir o curso
12:29
de HTML5.
12:30
Então eu vou colocar nesse quadradinho preto, que você está vendo aí no meio, eu vou colocar o identificador
12:35
do gafanhoto, e vou colocar também o identificador do curso.
12:36
12:39
Acabei de criar uma relação dizendo que esse gafanhoto vai assistir o curso de HTML.
12:43
Também vou fazer ele assistir outro curso, ó.
12:46
Vou criar um outra instância e vou fazer ele assistir por exemplo o curso de Word.
12:50
Então acabei de criar uma outra ligação.
12:52
O primeiro gafanhoto ali está assistindo dois cursos.
12:54
Está assistindo o curso de HTML 5, e o curso de Word, que como eu disse anteriormente, o mesmo gafanhoto
13:00
pode assistir vários cursos.
13:02
Vamos fazer o godofredo ali também assistir um curso.
13:04
Vou fazer o godofredo assistir HTML 5, né, só pra mostrar que um curso pode ser visto por mais
13:09
de uma pessoa. Então eu vou fazer essa relação ali, ó. Faço o godofredo apontar para assiste, e assiste
13:14
apontar para HTML5. Vou fazer também o godofredo assistir um segundo curso, que é curso de PHP.
13:20
Então tá lá o pequenininho lá em cima, tá assistindo dois cursos, e o godofredo também vai assistir
13:24
dois cursos.
13:25
E ai vem a Dolores e vai assistir 3 cursos, vai logo de cara, vou fazer 3 referências pra ela aqui.
13:30
Ela vai assistir o curso de HTML5, o curso de PHP e o curso de Word.
13:34
Ficou meio bagunçado, né?! Mas é só você prestar atenção que dá pra entender bonitinho.
13:37
Presta atenção aqui ó. Cada gafanhoto pode assistir vários cursos. Então tem esse
13:44
cara assistindo dois cursos, tem esse cara assistindo dois, e essa aqui assistindo três.
13:48
E cada curso pode ser assistido por várias pessoas. Aqui por exemplo ó,
13:52
o HTML5 está sendo assistido por três pessoas.
13:55
O PHP está sendo assistido só por duas pessoas, o amarelinho e o verde ó,
13:58
o godofredo e a Dolores.
14:00
E o curso de Word também está sendo assistido por duas pessoas, que são o vermelho, que é menininho
14:04
de cachinhos de ouro, e o verde, que é a Dolores.
14:07
Eu acabei de justificar para vocês como é que funciona um relacionamento de muitos para muitos
14:11
visualizando na prática.
14:13
Agora vamos colocar dados lá dentro. Como é que eu coloco dados dentro dessa tabela?
14:18
A coisa na verdade é bem simples. Eu vou inserir registros como eu te ensinei nas aulas passadas.
14:22
Eu vou utilizar o "insert into" nessa tabela.
14:24
Então eu vou colocar "insert into gafanhoto_assiste_curso", para eu poder inserir
14:28
os dados. E eu vou colocar os dados. Por exemplo, "default, ' 2014-03-01' , '1' , 2' "
14:34
O que que significa isso? Eu estou dizendo: esse "default" identifica que o meu id do gafanhoto
14:39
assiste curso vai ser gerado automaticamente, eu to dizendo que um determinado gafanhoto
14:44
que é o gafanhoto 1, começou a assistir o curso 2, que são os id's de gafanhoto, no dia primeiro de
14:52
de março de 2014.
14:54
Deu para entender? Então vamos adicionar esse dado diretamente no nosso banco.
14:58
Vamos fazer lá, ó, "insert into gafanhoto_assiste_curso values"
15:04
Acho que eu esqueci o "values" lá no negócio.
15:08
O "values" é, vamos colocar aqui, "default", sem aspas, por favor, a data vai ser 2014, março, dia primeiro
15:21
usuário 1 tá fazendo o curso 2, Ctrl+Enter, adicionei e agora a gente pode dar um select aqui pra ver se foi.
15:28
"select * from gafanhoto_assiste_curso", ta vendo?" Tem duas opções, gafanhoto e gafanhoto_assiste_curso.
15:34
Quero ver esse esse daqui. Então eu tenho lá, o gafanhoto 1 , assistiu o curso 2 e começou nessa data aqui.
15:41
Então vamos fazer o seguinte, vamos facilitar?!
15:44
Deixa eu dar uma puxada aqui pra cima.
15:46
Vou cadastrar algumas pessoas, por exemplo, 2015-12-22, dia 22 o aluno 3 começou a assistir o curso 6.
15:57
Tenho 60 alunos e tenho 30 cursos se eu não me engano.
16:02
Vou colocar aqui 2014-01-01, o gafanhoto 22 começou a assistir o curso 12, e também em
16:12
em 2016-05-12. Vou fazer outro aluno, ó, o aluno 1 também tá assistindo o curso 19.
16:26
Então você viu? Criei essa relação. Vamos clicar aqui em baixo em "apply" nunca se esqueça. "Apply" de novo.
16:32
Finish. E agora os dados já estão cadastrados.
16:35
O grande problema é o seguinte, eu dou um "select" nessa tabela do meio, nessa minha tabela relacional,
16:40
e o que aparece é um monte de número, o que eu quero é uma listagem, o nome do cara, o nome do gafanhoto,
16:46
e qual curso que ele tá fazendo. Isso é complicado, porque um tá de um lado, o outro tá de outro e eu tenho
16:53
uma tabela no meio, para meio que, atrapalhar. Na verdade ela vai te ajudar, mas o grande problema é como
16:58
é que eu vou juntar isso tudo.
16:59
A resposta disso tudo são as junções. Lembra a aula passada quando eu ensinei o join?!
17:04
Nós vamos usar nessa aula principalmente o inner join, que é o join tradicional. Se eu coloco só join,
17:09
é um inner join. A gente já viu isso anteriormente. Hoje a gente vai utilizar um conceito que a gente já viu na aula
17:13
passada para juntar um join no outro. Calma, não tem nada muito difícil, vamos por partes.
17:19
Vamos começar com um select simples. Antes de mais nada eu vou colocar o diagrama entidade
17:23
relacionamento para você lembrar. Só que eu coloquei de uma maneira simplificada, só pra você lembrar.
17:24
Só que eu vou colocar ele de uma maneira simplificada, só com as chaves.
17:27
Então você vê ai o gafanhoto só com a sua chave primária, o curso lá do outro lado só com a chave
17:31
primária, e o assiste só com suas chaves estrangeiras.
17:34
Que é o que vai importar pra gente aqui.
17:36
Vamos começar o nosso select. Vou colocar select * from gafanhotos e vou colocar "g" como um apelido,
17:43
e vou juntar essa tabela de gafanhotos com o resultado do assiste.
17:47
Então eu vou colocar join gafanhoto_assiste_curso, e vamos chamar de "a", de assiste.
17:52
Então o "g" vai ser o apelido para gafanhotos, e o vai ser o apelido para gafanhoto-assiste.
17:56
Se eu colocar só assim, a gente já viu na última aula que vai dar uma bagunça tremenda.
18:00
Eu preciso da cláusula "on". O que gafanhoto se junta a assiste? Eu vou juntar a chave primária de gafanhoto
18:06
com a chave estrangeira de assiste.
18:08
Então eu vou utilizar o id do gafanhoto com o id gafanhoto da tabela de assiste.
18:13
Então eu vou fazer o seguinte, ó, on g.id, isso é o id do gafanhoto, igual ao id gafanhoto da tabela "a",
18:20
que é o gafanhoto_assiste_curso.
18:21
Beleza?! Vamos fazer até ai pra gente ver como é que funciona o negócio.
18:25
Então vamos voltar aqui ao normal.
18:28
E eu quero o seguinte aqui,ó.
18:30
Vamos criar um select novo aqui.
18:33
select * from gafanhotos, com apelido "g", vou colocar join, que é o inner join. Ele vai juntar as referências e os
18:43
dois com gafanhoto_assiste_curso.
18:47
Beleza, com o apelido de "a". E eu vou utilizar o "on" aqui pra poder ligar. Vou ligar g.id com o a.idgafanhto
18:57
Coloca ponte e vírgula, Ctrl+Enter. Ele vai me mostrar os dados do gafanhoto, e aqui eu tenho o id do gafanhoto
19:04
e o id do curso e a data.
19:06
Daqui pra lá, é o dado do assiste. Daqui pra cá, são os dados do gafanhoto.
19:17
Vamos dar uma filtrada aqui para mostrar somente o nome do gafanhoto, g.nome. E também quero mostrar
19:25
o código do gafanhoto.
19:29
idgafanhto.
19:31
Da tabela de "a". Eu vou colocar também o g.id, que é o id identificador do gafanhoto.
19:37
Olha aqui. Eu mostrei o id do meu gafanhoto, que é 1, e eu peguei o id gafanhoto lá da tabela de assiste que
19:43
que também veio.
19:44
Vamos adicionar aqui também, o id do curso.
19:47
Ctrl+Enter.
19:48
Então eu tenho essa relação, do idgafanhoto, que é a ligação que eu tô utilizando.
19:54
Aqui é sempre igual a esse. Ele tem que ser sempre igual a esse porque eu usei o inner join.
19:59
Então eu tô dizendo aqui que Daniel Morais tá fazendo o curso 2. Emerson Gabriel, tá fazendo o curso 6.
20:05
Guilherme de Souza, tá fazendo o curso 12. Então eu já posso até tirar o id daqui para ficar mais claro pra gente
20:10
poder entender. Vou tirar aqui. Não precisa aparecer o id do gafanhoto, a gente já viu como é que funciona
20:16
o negócio.
20:17
Então Daniel Morais tá fazendo o curso 2, Emerson Gabriel tá fazendo o curso 6, Guilherme 12,
20:23
e o Daniel Morais tá 2 vezes.
20:26
Vamos colocar isso daqui em ordem. order by g.nome
20:31
O Daniel Morais tá fazendo 2 cursos, o 2 e o 19. O Emerson Gabriel tá fazendo 1 curso e o Guilherme
20:38
Souza tá fazendo 1 curso também.
20:40
Só que aí, Guanabara, eu não quero o código do curso, eu quero o nome do curso,
20:44
e o nome do curso tá em uma terceira tabela. Como é que eu faço pra puxar o
20:47
nome do curso lá da outra tabela?
20:49
Faz mais um join, meu querido! Acompanha aqui com o tio, vamos passo a passo.
20:53
Então nós paramos nesse momento aqui. Eu juntei o id do gafanhoto, o id do gafanhoto que tá lá na
20:58
tabela assiste.
20:59
Agora eu vou ter que pegar os dados lá do curso, lá da direita.
21:02
Então eu vou usar mais um join,
21:04
nesse join eu vou dar um join com cursos, e eu também tenho que dizer o on.
21:09
Como é que eu vou montar esse on? Eu quero que o id do curso se junte com o id do curso de assiste.
21:14
Eu vou relacionar chave primária com chave estrangeira de novo. Então eu vou fazer assim,
21:18
on, o id do curso do assiste vai ser igual ao id do curso do curso.
21:23
Ficou confuso? Vamos na prática que agora você entende.
21:27
Então nesse ponto eu tô mostrando somente o id do curso aqui,
21:30
mas eu quero mostrar o nome do curso.
21:32
Como é que eu faço? Tem que vir aqui depois desse on, e vou fazer um join. Desce o order by, tá!
21:37
Com cursos, vou dar o apelido de c, o on, e aí eu posso escolher qualquer um dos lados.
21:43
Vou fazer aqui c.idcurso = a.idcursos. Fiz a junção aqui.
21:50
Então a ideia é essa, com esse join eu consigo juntar os dois. Vamos ver se isso funciona.
21:54
Então eu coloquei aqui c.idcurso, a.idcurso, Ctrl+Enter...
22:00
Ele deu um erro aqui dizendo que id.curso é ambíguo. Ahh sim!!
22:04
Aqui eu coloquei só id.curso. Vou colocar a.idcurso, porque eu tenho idcurso nas duas
22:10
Dou Ctrl+Enter. Agora funcionou.
22:12
Só dar Ctrl+Enter, ele não mostra o nome do curso. Isso porque você não fez ele mostrar o nome do curso ainda.
22:20
Vou colocar aqui c.nome, e vai mostrar o nome do curso. Aqui é nome do gafanhoto, aqui é nome do curso.
22:27
Ctrl+Enter.
22:28
Agora eu tenho. Daniel Morais tá fazendo Algoritmo e Redes
22:32
Emerson Gabriel tá fazendo MySQL.
22:35
Guilherme de Souza tá fazendo C++.
22:37
♫Efeito de transição.♫
22:38
Viu? Agora eu tô conseguindo puxar dados de 3 tabelas.
22:41
Com isso, eu precise usar os dois join's.
22:44
Esse tipo de conceito já é um pouquinho mias complexo, e já começa a entrar no mais difícil do MySQL
22:51
E é por isso que a gente encerra o curso por aqui. Eu mostrei pra você, a maioria das coisas que o MySQL
22:57
tem de fundamental. A gente viu o início de modelo relacional, isso é, a gente viu quase tudo
23:04
do básico de banco de dados.
23:06
É claro, volto a dizer, com esse curso você consegue criar banco de dados simples e até mesmo
23:12
intermediários, mas se você precisar de banco de dados mais avançados, você vai ter que se aprofundar no
23:17
conceito, vai ter que estudar mais sobre o modelo relacional, mais um pouco sobre tipos de atributo,
23:22
mais relacionamentos, criar relacionamentos ternários... Você tem muito mais coisa para aprender.
23:27
Esse curso é um curso introdutório de banco de dados com MySQL.
23:32
Eu espero sinceramente, de coração, que eu tenha te ajudado, que eu tenha colaborado para o seu
23:37
aprendizado, que eu tenha te mostrado de uma maneira mais divertida, um pouco mais descontraída,
23:42
um pouco diferente daquela que o seu professor utilizou em sala de aula.
23:47
Eu fico muito feliz de receber os relatos, da galera que chega pra mim e fala: "Pô, Guanabara, você me ajudou
23:51
pra caramba, eu não tava entendendo tal conceito e agora eu consigo entender."
23:56
Eu fico muito feliz. E a forma de pedir o seu agradecimento é sempre você se manter aqui
24:01
no Curso em vídeo.
24:02
Se inscrever no canal só por se inscrever não serve de nada para mim. Eu poderia chegar e falar assim:
24:06
Olha só, vamos fazer uma promoção aqui, eu quero inscritos. Chama a sua vó, seu avô, seu tio,
24:10
sua tia. Tá, mas eles não estão interessados no que eu tô falando. Então eu preciso de inscritos ativos,
24:16
eu preciso de inscritos que sempre assistam os nosos vídeos.
24:19
O que faz um canal crescer, não é só se inscrevendo nele, é assistindo os vídeos dele, é valorizando
24:25
as propagandas que estão aparecendo. É dando view.
24:27
"Ah não, esse curso aqui eu não quero fazer agora!"
24:30
Dá um view, vê se você consegue pelo menos dar uma introdução ao conceito.
24:34
A gente tá fazendo agora outros tipos de vídeo. A gente tá fazendo o Curso em vídeo responde,
24:37
a gente tá fazendo aqueles vlog's de viagem, onde você acompanha meu dia-a-dia, as coisas que eu faço...
24:42
Então eu quero muito convidar você a se tornar um frequente visitante do Curso em vídeo,
24:48
do canal do Curso em vídeo do YouTube.
24:50
Você pode ter certeza que você vai fazer com que o curso cresça, com que o canal cresça e a gente consiga
24:55
cada vez mais anunciantes, e conseguindo cada vez mais anunciantes, vai ter cada vez mais cursos
24:59
Mais um vez eu me despeço aqui, mas não fica aquela sensação de tristeza, fica uma sensação de realização,
25:05
aquela sensação de eu ter conseguido fazer um curso com 16 aulas, que você pode ter certeza,
25:10
foi a melhor qualidade que eu consegui proporcionar a você. Eu fiz um esforço tremendo, a gente começou
25:16
a gravação com um monte de barulho, um monte de obra. Graças a Deus essa obra acabou,
25:20
eu to gravando essa 16ª aula, olha o silencio, ouça o silêncio...
25:24
...
25:25
Mas eu me esforcei ao máximo possível. Me desculpa se ficou faltando alguma coisa,
25:29
me desculpa se algum conceito você não conseguiu entender direito. Assiste a aula de novo, consulte o seu
25:34
professor. O seu professor ele não é inútil. Eu nunca disse isso, muito pelo contrário, eu sempre valorizei
25:39
muitos os professores. Professor, quer utilizar esse material? Tá lá no site cursoemvideo.com,
25:44
lá você vai poder baixar os slides, acessar tudo bonitinho. Você pode utilizar o meu conteúdo, você pode
25:51
utilizar a minha aula, os meus vídeos na sua sala de aula, contanto que seja mantido...
25:55
Você não pode baixar a aula e entregar para os seus alunos, mas manda o link pra eles,
26:00
fala pra que assistas, passe como trabalho de casa...
26:03
Gafanhotos, assistam, valorizem, valorize o seu professor, esse cara que mostra o curso para vocês.
26:08
E se você é um gafanhoto que descobriu o curso e seu professor adoravelmente não sabe, mostre para o seu
26:12
professor também. Vamos fazer o caminho duplo aqui, professor mostra pro aluno, aluno mostra pro professor
26:16
e a gente cresce, a gente evolui, e com certeza, eu estou contribuindo pro melhor ensino na a´rea de tecnologia.
26:23
Pelo menos eu estou tentando fazer isso.
26:25
Mais uma vez eu me despeço, dessa vez a gente vai voltar com outros tipos de cursos, com outros tipos
26:31
de conteúdo. Me dá aquela trista no coração de não poder gravar mais nenhuma aula de banco de dados.
26:35
Estamos nos despedindo, infelizmente do godofredo, da Dolores e da Godolores, aquela coisa linda de
26:41
cuti cuti cuti titititi...
26:42
E é assim que eu encerro o Curso em vídeo de banco de dados.
26:46
A gente se vê na próxima, espero que vocês gostem. Tem uma coisa bem legal nesse próximo curso
26:52
que tá saindo. A gente vai começar uma série nova, um novo assunto, as aulas já estão sendo gravadas,
26:57
mas eu vou guardar a surpresa porque vai ser bem legal.
27:00
Queria agradecer aqui todo mundo que com seu esforço, ajuda o Curso em vídeo,
27:05
queria agradecer aqui o Yuri, o Ariel, que faze os cortes nas aulas. Essa aula tá sendo cortada pelo Yury,
27:11
forte abraço, Yuri.
27:13
Queria também agradecer a todas essas coisas visuais que aparecem na tela, queria agradecer o Ramon
27:18
e a Iná, que são os nossos animadores, os nossos finalizadores, os riscos que aparecem na tela...
27:23
tudo isso foi produzido por uma equipe, eu não comprei um pacote de animação, até porque esses pacotes não
27:31
existem com essa qualidade que a gente produz aqui.
27:33
Então valorize, valorize mesmo a produção de conteúdo independente que a gente tá fazendo aqui no
27:38
Curso em vídeo.
27:39
Forte abraço, pequeno gafanhoto! Estude sempre, nunca pare de estudar
27:44
A gente se vê no próximo curso com muita mais informação pra vocês.
27:48
Um forte abraço e até o próximo curso.
27:53
Assista os nossos cursos sempre pela paylist.
27:55
LBRUBRLUBRBLUR
"""

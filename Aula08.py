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
(export to self contained file > + include create schema) # SEMPRE MARCAR INCLUIR O SCHEMA! 
(start export)
"""

# Depois de feito o backup, podemos na moral apagar tudo!
DROP DATABASE cadastro;

# MySQL Workbench > Server > Data Import > 
"""
Import Dump from Project Folder 
or
Import from Self-Contained File (C:\...)
Start Import 
"""
USE cadastro;
# 3	4	01:22:22	USE cadastro	0 row(s) affected	0.000 sec

SHOW TABLES;
"""
cursos
gafanhotos
"""

DESCRIBE gafanhotos;
"""
codigo	int	YES			
id	int	NO	PRI		auto_increment
nome	varchar(30)	NO			
prof	varchar(20)	YES			
nascimento	date	YES			
sexo	enum('M','F')	YES			
peso	decimal(5,2)	YES			
altura	decimal(3,2)	YES			
nacionalidade	varchar(20)	YES		Brasil	
"""

DESC cursos;
"""
idcurso	int	NO	PRI		
nome	varchar(30)	NO	UNI		
descricao	text	YES			
carga	int unsigned	YES			
totaulas	int unsigned	YES			
ano	year	YES		2016	
"""

SELECT * FROM gafanhotos;
"""
	1	Godofredo		1984-01-02	M	78.50	1.83	Brasil
	2	Maria		1999-12-30	F	55.20	1.65	Portugal
	3	Creuza		1920-12-30	F	50.20	1.65	Brasil
	4	Adalgiza		1930-11-02	F	63.20	1.75	Irlanda
	5	Cláudio		1975-04-22	M	99.00	2.15	Brasil
	6	Pedro		1999-12-03	M	87.00	2.00	Brasil
	7	Janaína		1987-11-12	F	75.40	1.66	EUA
"""

SELECT * FROM cursos;
"""
1	HTML5	Curso de HTML5	40	37	2014
2	Algoritmos	Lógica da Programação	20	15	2014
3	Photoshop	Dicas de Photoshop CC	10	8	2014
4	PHP	Curso de PHP para Iniciantes	40	20	2015
5	Java	Introdução à Linguagem Java	40	29	2015
6	MySQL	Bancos de Dados MySQL	30	15	2016
7	Word	Curso Completo de Word	40	30	2016
"""





"""
Transcrição


Procurar no vídeo
0:19
olá pequeno gafanhoto seja bem vindo a
0:22
mais uma aula do seu curso em vídeo de
0:23
banco de dados com mais que l
0:25
o meu nome é gustavo guanabara eu sou
0:27
professor e nessa 8ª aula do seu curso
0:29
de banco de dados nós vamos falar sobre
0:31
uma coisa que eu tinha prometido na aula
0:32
passada e dessa aula eu vou te ensinar
0:34
como gerenciar cópias de segurança da
0:37
sua base de dados
0:38
e se você estava procurando no youtube
0:40
como exportar banco mas kelly como
0:42
exportaram base uma base de dados mas
0:44
kelly e caiu nesse vídeo saiba que essa
0:46
é a oitava aula de um curso completo de
0:49
mais quero é para iniciantes
0:50
então se você quiser me dar essa honra
0:51
de assistir essa aula ou pelo menos a
0:53
aula onde eu configura o ambiente estava
0:55
mais quer instalar mais keliwort bem
0:57
você vai precisar dessa base toda
0:59
instalado se precisa saber como eu estou
1:01
trabalhando esses conceitos mais que l
1:04
então fique à vontade a play visitar
1:06
aqui aqui em cima clicando nesse zinho
1:08
interatividade aqui você também pode ter
1:10
acesso a playlist inclusive vou colocar
1:12
ele na interatividade
1:13
a aula de instalação do ambiente caso
1:15
você já saiba mais quero que você está
1:17
precisando é só entender como é que uma
1:18
estrutura aqui o meu servidor mas vamos
1:21
diretamente por nosso ambiente saber
1:22
como é que tá tudo estruturado a gente
1:24
poder fazer o backup da nossa base de
1:26
dados
1:27
estou aqui no meu ambiente windows já
1:30
estou como eu entenda que é aberto eo
1:32
mais que ele funcionando ele está
1:34
verdinho talento então meus servidores
1:36
estão ativos e eu vou abrir agora ou
1:38
mais quero workbench clicando sobre o
1:41
ícone
1:42
a gente aprendeu a instalar todas essas
1:43
ferramentas abrindo o cliente
1:45
vou abrir a minha instância do meu
1:48
servidor está aberto lá
1:49
caso você não esteja com o wv aqui com
1:53
certeza que vai dar erro
1:54
eu não tenho nenhum banco de dados
1:56
aberto uma coisa que é muito comum sei
1:58
lá eu vou dizer aqui select risco from
2:02
cursos que o que está fazendo quando
2:05
executava está me dizendo aqui eu não
2:08
consigo abrir porque não existe um banco
2:10
de dados selecionado
2:12
então pra
2:13
abrir um banco de dados antes eu posso
2:15
dar e use cadastro
2:18
agora o cadastro aberto eo meu select
2:21
vai funcionar corretamente beleza
2:23
você deve ter visto aqui que dá uma
2:24
passada a gente deu um tom kitt apagou
2:26
todos os dados já coloquei aqui tudo de
2:28
novo para a gente poder exportar e gerar
2:30
um backup com tudo bonitinho na
2:31
recordada como é que a nossa estrutura
2:33
do banco de dados rever alguns comandos
2:35
rapidamente onde você vê aqui ó
2:37
você consegue describe a gente tem a
2:40
tabela gafanhotos contra o inter eu
2:45
tenho e de nome profissão está aqui
2:47
todos os tipos tudo bonitinho eu também
2:49
tenho tabela cursos todo mundo escreve
2:52
nela você pode usar describe ou desk sem
2:56
problema
2:58
ele funciona a então eu tenho a
3:00
estrutura do gafanhoto e até a estrutura
3:02
do curso também tenho cursos cadastrados
3:05
e também tenho gafanhotos cadastrados
3:12
tenho dados na tabela gafanhotos tenho
3:15
dados na tabela cursos têm a estrutura
3:17
da tabela gafanhoto tem a estrutura da
3:20
tabela cursos tudo ok tudo bonito e aí
3:23
na aula passado te ensinei utilizar o
3:25
update o dele tietê disse olha cuidado
3:28
na hora de utilizar esses comandos
3:29
porque eles podem apagar registros que
3:31
você não quer que apague e não existe
3:33
controle sendo mais kelly
3:35
existe aí caramba paguei sem querer não
3:37
é meu querido apagou sem querer refaz o
3:40
backup mas como é que eu vou fazer o
3:42
backup e foi aqui que a gente parou na
3:44
anterior
3:44
eu vou te ensinar como gerar uma cópia
3:46
de segurança e como gerenciar essas
3:48
cópias de segurança diretamente do seu
3:50
ambiente do mais que l utilizando aqui
3:52
como exemplo o worldbench para fazer
3:55
essa exportação nós vamos dentro do
3:57
ambiente workbench nós vamos clicar em
3:59
server e vamos clicar em data export vai
4:04
abrir essa janela onde você vai poder
4:05
selecionar os seus esquemas ou seu banco
4:08
de dados
4:08
então vou selecionar aqui o cadastro
4:11
clicando sobre ele você pode selecionar
4:12
o que tiver de objeto dentro desse
4:15
esquema
4:15
não tenho só duas tabelas curso e
4:17
gafanhotos se por acaso você é um
4:19
programa do mais experiente e está
4:20
gerenciando seu banco de dados ele tiver
4:22
views tudo vai aparecer aqui direto no
4:24
momento a gente só tem duas
4:26
ele vai deixar tudo selecionada que se
4:28
você quiser pode portar só uma tabela
4:29
branco não quero exportar gafanhotos que
4:31
eu vou querer mas você pode desmarcar
4:33
outra coisa que você pode escolher aqui
4:34
você vai gerar o dumping e aí vem um
4:36
termo novo o backup de um banco de dados
4:39
a gente chama de dampier sempre você
4:41
quiser criar uma cópia de seu banco de
4:42
dados você pode fazer a gerar um banco e
4:44
desse banco de dados para mim porque a
4:46
base de dados a lam está numa máquina
4:47
ela está num servidor no seu caso aqui
4:50
o anc já criou o seu servidor na sua
4:52
própria máquina mas não é comum você tem
4:54
acesso ao servidor de acesso diretamente
4:56
ao arquivo então o que você vai fazer é
4:58
você tem acesso ao servidor
4:59
você está vendo o banco de dados você
5:01
tem autorização para gerar um dano pi
5:02
josé neci damp pega ele você vai poder
5:04
levar ele pra outro servidor ao gerar o
5:06
dano você pode escolher exportar a
5:09
estrutura e os dados e aí você vai
5:11
exportar a estrutura da tabela que a
5:13
gente botou aqui com describe e também
5:15
os dados cadastrados
5:16
então se você quiser o banco de dados só
5:18
o banco de dados invasivos em nada só
5:20
estruturas em dado nenhum aí você
5:22
escolhe aqui ó damp strummer
5:26
se você quiser também pode anteceder a 1
5:28
lens e pode só exportar os dados no meu
5:31
caso aqui eu vou exportar o dado ea
5:34
estrutura isso porque eu quero o banco
5:36
de dados inteiro quer um banco de dados
5:37
completo se por acaso você é mais
5:40
avançada provavelmente você já sabe
5:42
utilizar histórias procidades eventos e
5:45
triggers são os gatilhos você marcar que
5:48
ele também vai gerar o da anp desse
5:50
componente no banco de dados aqui como
5:51
eu só tenho duas tabelas não vou marcar
5:53
nenhuma delas logo em seguida você vai
5:55
escolher qual tipo de exportação você
5:57
quer uma exportação do folder inteiro de
6:00
um projeto ou simplesmente num arquivo
6:03
único e você vai fazer testes ver qual é
6:05
a melhor opção para você no meu caso
6:07
aqui o que a gente vai utilizar na aula
6:08
é a exportação para um arquivo único
6:10
então você vai colocar aqui o export
6:12
self container finance e pode dar um
6:14
nome que eu vou deixar que vai gerar que
6:16
ele gerou um golpe em 2016
6:19
02 08 dia 8 de fevereiro de 2016 que é
6:25
quando estou gerando excedente aqui e se
6:27
você é um gafanhoto esperto e fez ponta
6:30
eu estou no meio do carnaval sim se
6:32
assistiu às aulas anteriores estava
6:34
martelando não estava
6:36
hoje é quase feriado tem ninguém
6:38
trabalhando
6:39
a paz não vou deixar aqui ele vai gerar
6:42
um arquivo dentro dos meus documentos na
6:44
pasta dantes se você quiser eu vou fazer
6:48
marque a opção inclui create esquema pra
6:51
que serve isso lembra que nas primeiras
6:52
aulas mas kelly eu te ensinei o comando
6:54
criativo de cada vez
6:55
então se você não marcar essa opção
6:57
dentro do seu banco não vai ver a
6:59
criação do banco de dados
7:00
e aí vai forçar que você digite o
7:02
primeiro crie um banco de dados no
7:03
servidor e só então possa importar um
7:06
tanque
7:06
aqui no meu caso mesmo que esse banco de
7:08
dados não exista ele vai criar marcas
7:10
opção feito isso vamos clicar em start
7:13
export
7:15
cliquei ele vai me pedir a senha do meu
7:18
usuário e aí você está utilizando outros
7:21
servidores você tem que saber qual é o
7:22
usuário e senha do seu servidor sql
7:25
no meu caso aqui como eu utilizando anp
7:26
e já falou isso nos vídeos anteriores o
7:28
nosso usuário é ruth ea nossa senha é
7:31
uma senha vazia é só pressionar enter
7:33
então vamos deixar a caixa de 100 vazia
7:35
vamos continuar aqui deixa vazia
7:38
clique em ok ele vai gerar o da anp em
7:41
alguns segundos e está tudo feito um dá
7:45
uma olhadinha ver como funciona isso
7:46
abre seu windows explorer aí então vamos
7:48
abrir o explorador de arquivos e vamos
7:52
abrir os meus documentos dentro dos meus
7:55
documentos eu tenho a pasta dantes
7:57
abrindo ela tem um arquivo que eu acabei
7:59
de gerar eu vou clicar com o botão
8:00
direito você pode abrir qualquer editor
8:02
de textos em formatação no meu caso eu
8:04
vou utilizar o notepad mas mais mas você
8:06
pode abrir por exemplo com o seu bloco
8:09
de notas sem problema nenhum vou usar
8:11
nos pés mas que eu consiga gerenciar o
8:13
tamanho da minha fonte é aumentar um
8:15
pouquinho só para você entender então
8:17
basicamente que eu fiz aqui ó
8:18
você percebe que ele tem os comandos que
8:20
a gente está aprendendo durante a aula
8:22
basicamente um banco é ou foi o passo a
8:24
passo que quem criou um banco de dados
8:26
fez para poder chegar ao banco de dados
8:28
nesse estado que ele está basicamente
8:30
vai criar uma lista de comandos
8:32
acompanhe aqui o primeiro comando é o
8:34
creative labs e final existe se lembra
8:37
disso a gente fez isso a gente usou
8:39
colete table e flora existentes
8:41
o creative labs também funciona o ignora
8:44
existentes
8:44
então vou criar um banco de dados
8:45
chamado cadastro vou dar uns cadastro
8:49
para ele abrir um banco de dados a gente
8:51
já viu isso várias vezes
8:52
logo
8:53
vida a gente tem a tabela isso tudo é
8:55
comentário aqui na verdade são
8:57
comentários de configuração não entre
8:59
muito nesses detalhes
9:01
ó o drop table existe discurso é se já
9:04
existe uma tabela cursos apague ela e
9:07
cria nova tabela cursos com toda aquela
9:09
estrutura que a gente fez anteriormente
9:10
perceba que o comando é exatamente
9:12
aquele que a gente criou durante a nossa
9:14
aula do coritiba logo em seguida você
9:17
vai ter também o da anp da tabela
9:21
gafanhotos a ele dá um jovem antes se
9:23
existir e dá um cliente table também
9:25
então ele vai criar tabela gafanhotos
9:27
também exatamente com a mesma estrutura
9:29
que a gente viu antes
9:30
então a gente viu o craque da vez eo
9:32
credit tempo para cada uma das tabelas
9:35
viu como quando você segue o curso você
9:37
consegue entender se aqui de uma maneira
9:39
simples é gaga foi o que eu falei que
9:41
você aprendeu fql eu já fiz promessa e
9:44
não cumprir é mais embaixo eu vou ter um
9:46
insight tim aqui ó insert into do
9:48
gafanhoto colocando as pessoas só rolar
9:50
para o lado que você vê todos os
9:53
registros no único e certamente eu vou
9:56
quebrar página aqui vou clicar em
9:58
visualizar quebrar linhas
10:00
automaticamente instalar o seu set to
10:02
você vê lá em cima
10:03
logo depois de cursos você também tem 17
10:06
tio da tabela curta que atendam inteira
10:08
todos gerando da anp dos dados em todos
10:11
os cursos aqui que já existiam
10:13
anteriormente beleza então guardou na
10:16
sua pasta dambi tudo aquilo que você
10:18
precisa para recriar esse banco de dados
10:20
em outro servidor se você precisa e como
10:22
a gente vai testar se isso funciona aqui
10:24
gostoso vai pagar os cuidados e se
10:27
comunicam dor no coração o cérebro então
10:29
agora que eu tenho um dano gerado voltar
10:32
aqui ó e sem cerimônia sem medo de ser
10:35
feliz
10:36
eu vou dar um trope da base o cadastro a
10:42
sério só quem apagou um banco de dados
10:47
em querer saber o que é a alegria
10:53
olha lá ele apaga o banco de dados de
10:56
cadastro para pagar o banco de dados
10:58
teste também que eu não quero ele nem de
11:02
depp apaguei
11:03
agora meu servidor está vazia las em
11:06
banco de dados
11:07
e aí dá controle e aí ver se você
11:10
consegue desfazer pode apertar quantas
11:11
vezes quiser não existe essa
11:13
possibilidade então o que a gente
11:14
garantiu aqui foi um backup antes de
11:16
apagar
11:17
agora eu tenho da anp já verificamos o
11:19
davi está todo bonitinho tudo
11:20
funcionando e agora nós vamos fazer o
11:22
trabalho reverso
11:23
vamos imaginar agora que você mudou de
11:25
servidor então basicamente estou num
11:27
novo servidor ou imaginar que eu tenho
11:28
uma outra máquina num outro servidor que
11:30
eu também tenho acesso ao mais que r eu
11:33
vou abril o cliente é importante dizer
11:35
que a ferramenta workbench é oficial do
11:37
mais que ela então é utilizada em várias
11:39
empresas então é comum você acontecer
11:42
isso eu vou abrir aqui o servidor
11:45
então você pegou aquele dano que foi
11:47
gerada que arquivos em sql que foi
11:49
gerado na sua pasta da anp pega aquele
11:51
arquivos estavam em um pen drive
11:52
nessa conversa o cuidado no fumo gigante
11:54
não se salvou fez um backup levou para
11:57
outra máquina nem vou para um lugar onde
11:59
você tem acesso ao servidor simplesmente
12:01
da sua própria máquina e você pode
12:03
importar isso diretamente para o seu
12:05
novo servidor
12:06
então tá lá estou aqui com servidor
12:07
vazio e eu quero jogar aquele banco de
12:09
dados que eu tinha exportado antes
12:11
como é que eu faço um simples clique em
12:13
cerva e no lugar de dedé export clique
12:16
inteira importe se vai abrir essa janela
12:19
ele vai dizer aqui ó importe um camp do
12:22
seguinte e roldanas seguinte pastas e
12:25
clique aqui e vamos colocar a pasta que
12:28
eu tenho o da anp
12:29
se botar no seu pendrive tudo mais vou
12:31
ter aqui o dantes ok eu vou importar
12:36
na verdade não o projeto vai importar
12:38
diretamente desse arquivo clique aqui
12:43
escolhe seus documentos pasta antes de
12:48
escolher aquele wg anteriormente
12:50
clique em abrir efeito essa escolha já
12:53
que eu exportei marcando que eu queria
12:55
inclusive exportar o esquema só clicar
12:58
em start importe ele vai pedir mais uma
13:02
vez a senha do meu servidor você digita
13:04
a senha do servidor no meu caso aqui é
13:06
vazia
13:09
ele vai importar e depois de importado
13:12
você pode ver aqui ó atualizar e ele já
13:15
está lá
13:16
o banco de dados de novo viu como é
13:18
simples você acabou de importar uma base
13:20
de dados
13:21
levou de um servidor para outro sem
13:23
precisarem pastinha copiar arquivos nada
13:25
disso
13:25
você simplesmente no seu ambiente de
13:27
servidor gera um dom pepe ele gera esse
13:30
da anp completo
13:31
nunca se esqueça de marcar a exportação
13:33
do esquema junto se você vai ter que
13:34
fazer um procedimento um pouco diferente
13:36
e agora o seu serviço está funcionando
13:38
sem problema nenhum não está funcionando
13:40
mesmo vamos fechar essa janela aqui e na
13:44
quarta vamos e use cadastro para abrir
13:47
um banco de dados
13:48
abrir um banco de dados vamos ver a
13:52
descrição da tabela tables tabelas
13:59
tabela cursos e gafanhotos
14:01
eu posso dar describe gafanhotos só
14:10
começar a digitar que ele completa para
14:12
você então vou executar esse primeiro
14:14
click na linha contra o inter já
14:17
descreveu também não tinha nada agora
14:18
tem da fã e outros também está lá ver
14:23
quais são os dados que estão lá posso
14:25
botar select asterisco from gafanhotos
14:29
select 38
14:37
lá todo mundo cadastrado em curso
14:41
lá todo mundo cadastrado e aí tem coisa
14:45
mais simples que isso então você pode
14:47
pegar por exemplo em breve salvar pegar
14:49
aquele arquivo salvar no pen drive e
14:51
depois levar para onde você quiser ou
14:53
mandar por e mail para alguém o dono do
14:54
seu banco de dados você vai poder
14:56
colocar seu banco de dados em qualquer
14:57
servidor que tenha mais que ela e aí
15:00
gostou
15:01
essa obra foi um pouco mais curta mas é
15:03
bastante importante que você entenda
15:05
tudo isso que você saiba exportar
15:08
importar uma base de dados
15:09
isso é de suma importância para todo
15:11
profissional que vai trabalhar com o
15:13
banco de dados
15:13
então meu querido cris e os bancos
15:15
procuram agora bancos é procurar na
15:18
internet lá por dantas de banco de dados
15:19
que existem vários bancos de dados de
15:21
teste que é só você baixar o arquivo
15:23
conta sql da internet jogar diretamente
15:26
no seu oponente mandar importar e ele
15:29
vai estar com a base de dados
15:29
diretamente para você útil pra caramba
15:32
na mesma aula sendo um pouco mais curta
15:34
para agradecer eu queria te pedir que
15:36
você curte se compartilhar com as
15:38
pessoas e que também se inscrevesse no
15:40
canal caso você não seja inscrito chegou
15:42
a hora eu queria faça parte desses
15:44
milhares de gafanhotos inscritos no
15:46
canal
15:46
clicando aqui não se inscrever você vai
15:48
participar esse clube dos gafanhotos
15:51
clicando aqui você vai pra playlist onde
15:53
você vai ter acesso a todas as aulas
15:54
mais que l
15:55
a sala foi curtinha foi bastante útil
15:57
foi curta mas foi ótimo mas você tem uma
15:59
série de aulas
16:00
essa é uma das aulas banco de dados na
16:03
próxima aula eu vou te ensinar opções
16:06
a working band vou te mostrar outras
16:07
maneiras de você manipular os dados vou
16:10
te mostrar a famigerada a tela preta
16:12
o professor de ensino com tela preta
16:13
aquilo dava trauma eu vou te mostrar que
16:15
agora que você já sabe utilizar o outro
16:17
mente aquela preta não é tão feio assim
16:20
não é nenhum um horror você aprender
16:21
mais quer você utilizar o mais quer
16:23
directamente do console
16:25
nós vamos ver uma solução gratuita
16:26
também feito em php para gerenciar o seu
16:28
banco de dados de maneira até mais fácil
16:30
nós vamos continuar com o cliente mas
16:32
nada que vem eu vou te dar opções para
16:35
mexer no seu banco de dados
16:36
vou provar para você que o seu banco de
16:38
dados não é o working band workbench não
16:39
é uma ferramenta para criar um banco de
16:42
dados porque vem de uma ferramenta para
16:43
facilitar o uso do mais kelly a
16:45
estrutura do banco de dados da ce parada
16:47
tá lá no servidor
16:48
e nunca se esqueça aluno cadastrado no
16:50
curso em vídeo tem direito a diploma
16:52
então aqui no meio você vai ter acesso
16:54
diretamente cadastrá-la faz as aulas
16:57
diretamente por lá e no final do curso
16:59
você vai poder imprimir o seu
17:00
certificado meu querido e mais
17:02
importante até que o certificado no
17:04
final do curso você vai saber mais que l
17:07
aquilo que você tanto queria no início
17:08
tá ficando fácil né tá ficando molezinha
17:10
africano chupetinha 2000 querido para ti
17:13
sempre esporte importa são as novidades
17:16
troque banco de dados entre gafanhoto
17:18
troca o banco de dados com seus amigos
17:19
agora você já sabe fazer um forte abraço
17:22
e até a próxima
17:25
você pegou aquele sedã que aquele seu
17:27
arquivo cinco pontas kelly que gerou
"""

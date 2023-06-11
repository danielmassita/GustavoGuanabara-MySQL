# Curso MySQL #10 - PHPMyAdmin (Parte 2)
# https://youtu.be/EC_1ZtXsUtA
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/phpmyadmin-parte-2/

# Vamos usar o PHP My Admin = http://localhost/phpmyadmin/index.php
# >>> +New (ou Base de Dados)
# >>> Criar Base de Dados 'exemplo'
# >>> Collation UTF8 General CI
# >>> CRIAR

# exemplo
# Criar Nova Tabela
# amigos (id, nome, telefone)
# id int Índice 'primary'
# nome varchar 30 'unique'
# tel varchar 11 'nulo'
# colação UTF8 general ci
# motor InnoDB
# Guarda

# PHP My Admin
ALTER TABLE `amigos` CHANGE `id` `id` INT UNSIGNED NOT NULL AUTO_INCREMENT, add PRIMARY KEY (`id`);

# MySQL:
mysql> show databases;
"""
+--------------------+
| Database           |
+--------------------+
| cadastro           |
| exemplo            |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)"""

mysql> use exemplo;
"""Database changed"""

mysql> show tables;
"""
+-------------------+
| Tables_in_exemplo |
+-------------------+
| amigos            |
+-------------------+
1 row in set (0.01 sec)"""

mysql> desc amigos;
"""
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int unsigned | NO   | PRI | NULL    | auto_increment |
| nome  | varchar(30)  | NO   |     | NULL    |                |
| tel   | varchar(11)  | YES  |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)"""

mysql> show create database exemplo;
"""
+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| Database | Create Database                                                                                                                   |
+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| exemplo  | CREATE DATABASE `exemplo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */ |
+----------+-----------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)"""

mysql> show create table amigos;
"""
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table  | Create Table                                                                                                                                                                                                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| amigos | CREATE TABLE `amigos` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `tel` varchar(11) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)"""

# PHP My Admin
ALTER TABLE `amigos` CHANGE `tel` `telefone` VARCHAR(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL;
"""
Exibindo como código PHP
$sql = "ALTER TABLE `amigos` CHANGE `tel` `telefone` VARCHAR(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL;";
"""

# PHP My Admin
# Adicionar nova coluna ou no final da tabela ou depois de nome. 'idade'
ALTER TABLE `amigos` ADD `idade` INT NOT NULL AFTER `nome`;

# Idade está errado no Banco de Dados, vamos salvar a Data de Nascimento!
# Apagar -> Elimina! 
"ALTER TABLE `amigos` DROP `idade`;"?

# Adicionar nova coluna para 'sexo'.
ALTER TABLE `amigos` ADD `sexo` ENUM('M', 'F') NOT NULL AFTER `nome`;

# Adicionar Maria e João como registros...
INSERT INTO `amigos` (`id`, `nome`, `sexo`, `telefone`) VALUES (NULL, 'Maria', 'F', '2222-3333'), (NULL, 'João', 'M', '2222-3333');
INSERT INTO `amigos` (`id`, `nome`, `sexo`, `telefone`) VALUES (NULL, 'José', 'M', '3333-4444'), (NULL, 'Ana', 'F', '1111-2222');
SELECT * FROM `amigos`

# Alterando o João, se separou da Maria e foi morar com Ana.
UPDATE `amigos` SET `telefone` = '1111-2222' WHERE `amigos`.`id` = 2;

# Apagar a Ana pois quer fugir da treta
Realmente deseja executar "DELETE FROM amigos WHERE `amigos`.`id` = 4"?

# MySQL Workbench
use exemplo;
show tables;
desc amigos;
select * from amigos;

# PHP My Admin
# Exportar > Rápido/Persoalizado > 'exemplo' > Formato: SQL > Add Create Database / Use statemente > Executar 




"""
Transcrição


Procurar no vídeo
0:03
van gaal
0:19
o la pequeno gafanhoto seja bem vindo a
0:22
mais uma aula de seu curso em vídeo de
0:23
banco de dados
0:24
o meu nome estava na barreira eu sou
0:26
professor e agora a gente vai dar
0:27
prosseguimento aos seus estudos de banco
0:29
de dados
0:30
aprendendo um pouco mais de como
0:31
utilizar o phpmyadmin e essa é a aula da
0:35
parte 2
0:35
então o vídeo passado eu falei um pouco
0:37
sobre outras ferramentas eu mostrei como
0:39
utilizar o console mais que elle e o php
0:41
mais de mim ea gente aprendeu a entrar
0:43
no ph pena de mim e fazer as
0:45
funcionalidades básicas
0:46
eu também falei na aula passada que
0:48
independe da ferramenta que você utiliza
0:50
a base de dados está sempre um servidor
0:52
e não importa qual a ferramenta você
0:54
utilize o banco de dados vai estar lá e
0:55
vai ser criado não importa a ferramenta
0:57
que você utilize agora eu vou dar um
0:59
pouco mais de foco no ph pé de mim
1:01
porque eu sei que tem gente que utiliza
1:02
bastante principalmente em planos de
1:04
hospedagem então se você vai colocar o
1:06
seu site no ar provavelmente a
1:08
ferramenta que a empresa de hospedagem
1:09
vai direcionar é o phpmyadmin a hostnet
1:12
por exemplo que é patrocinadora deste
1:14
curso disponibiliza phpmyadmin todos os
1:17
seus planos de hospedagem então se você
1:18
quiser criar um banco de dados e colocar
1:20
ele hospedado na hostnet você vai
1:22
utilizar o phpmyadmin então vamos deixar
1:23
uma coisa muito clara aqui você precisa
1:25
ter assistido ao anterior
1:27
caso você não tenha assistido clique
1:29
aqui.o você vai direto pra playlist e
1:31
você vai procurar a aula de ph pé de mim
1:33
parte 1 porque lá eu vou te mostrar como
1:35
você entra como você acesso phpmyadmin e
1:37
algumas funcionalidades básicas
1:39
agora a gente vai aprofundar um pouco
1:40
mais no conhecimento da ferramenta para
1:42
você poder construir o seu banco de
1:44
dados utilizando o phpmyadmin então já
1:48
estou com meu servidor ativo e também
1:51
com phpmyadmin aberto e também deixa
1:53
aberto aqui o work bent e a tela do
1:56
console e se cada vez que você vê a tela
1:58
de consolidar um pequeno arrepio
1:59
provavelmente é porque você ainda não
2:01
assistiu à aula anterior
2:03
lá eu te mostrei que é muito fácil e que
2:05
se você está seguindo as aulas bonitinho
2:06
testando treinando os comandos na tela
2:09
do console não vai te assustar de forma
2:11
alguma
2:12
nós vamos votar pega até mal de mim e
2:13
aprender algumas funcionalidades básicas
2:15
então já estou aqui na tela principal do
2:17
pega pena de mim e você vê que você
2:19
tenha base de dados aqui cadastro que é
2:21
que a gente está utilizando durante a
2:22
aula
2:23
vimos também que a gente tem sempre por
2:25
padrão três bases de dados que já ficam
2:27
aqui se você vê por exemplo aqui no
2:29
terminal é apertar enter que a senha é
2:33
vazia
2:34
vou dar aqui ó show terá bases
2:38
ele vai te mostrar aqui exatamente as
2:40
mesmas bases a information o esquema
2:41
performance esquema e mais que 'ele já
2:44
são por padrão exatamente como você está
2:46
vendo aqui tá vendo as as quatro bases
2:49
se você vier workbench e conectar ao
2:52
servidor
2:53
você vai ver aqui do lado que ele só te
2:56
dá acesso à base o cadastro mostra os
2:58
outros três
2:59
isso porque a ferramenta do ocidente ela
3:01
oculta essas três bases padrões para
3:03
você não precisa mexer nelas
3:05
a gente viu na aula passada que dá pra
3:06
gente manipular dados e acessar dados
3:08
diretamente o phpmyadmin agora eu vou
3:11
criar um banco de dados de teste e nós
3:12
vamos ver quais são os procedimentos
3:14
para você criar um banco de dados uma
3:16
tabela define quais são os campos
3:18
adicionar manipular os registros
3:21
então vem comigo que a sala está
3:22
caprichada uma vez no phpmyadmin vamos
3:25
criar um banco de dados novo para criar
3:26
uma base de dados nova você tem algumas
3:28
possibilidades
3:29
ou você clica aqui no link mil fica do
3:31
lado esquerdo ele vai abrir a tela de
3:33
base de dados
3:34
ou ainda na página principal você vem
3:36
aqui e clica em base de dados que você
3:39
vai abrir exatamente a mesma tela que
3:41
anteriormente
3:42
aqui você vai ver todos os bancos de
3:44
dados que estão criados no momento e tem
3:46
a possibilidade de criar uma base de
3:48
dados nós vamos na caixa de texto logo
3:50
abaixo e digitar o nome do banco eu vou
3:52
usar o banco de dados que vou criar como
3:54
exemplo
3:55
logo em seguida você vai ter que
3:57
escolher qual é o collegium clicando
3:59
sobre ele
3:59
você lembra que a gente utilizou na aula
4:01
de banco de dados utilizando o working
4:03
band
4:04
o tf 8 general sei eu vou procurar aqui
4:07
na lista
4:08
pô o tef 8 a procurar aqui na área
4:13
você vai ter o gênero se existem outros
4:16
tipos de colégio que também aceitam as
4:18
situações a gente escolheu o f8 aqui
4:20
assim como nas aulas anteriores para a
4:22
gente não ter problemas com as situações
4:24
particularmente eu prefiro esse mas tem
4:26
gente que usa formar
4:27
os latinos assim você pode ter
4:29
professores ou até mesmo vídeo aulas no
4:31
youtube que mostra outro padrão de
4:33
colégio
4:34
eu recomendo o tf 8 jersey
4:37
feito isso nós vamos clicar em criar a
4:40
partir daí ó à base de dados exemplo foi
4:42
criada exemplo o nome que eu dei a ela
4:45
isso você olhar aqui ó já tem exemplo
4:47
criado olhando aqui na esquerda
4:50
você também tem o banco de dados exemplo
4:52
pra abrir a base de dados de exemplo
4:54
basta clicar sobre o nome dela e ele
4:56
como não tem nada dentro ele já vai
4:58
sugerir criar uma tabela
5:00
vamos criar uma tabela clicando nessa
5:02
caixa e digitando o nome dela eu digitar
5:04
ou criar trabalho amigos
5:06
em seguida ele vai te perguntar qual é o
5:08
número de colunas e se você é um
5:10
gafanhoto esperto já assistiu às aulas
5:11
anteriores sabe que eu já comentei
5:13
algumas vezes que colunas são os campos
5:16
então por exemplo vamos imaginar que eu
5:19
vou querer que cada amigo meu tenha um
5:21
identificador que vai ser chave primária
5:22
o nome eo telefone de contato
5:25
só isso então eu vou ter três
5:27
identificados por o nome eo telefone de
5:29
contato
5:30
então vem aqui no número de colunas e
5:32
coloco o valor 3
5:34
clique em executar e você vai perceber
5:37
que ele já criou aqui uma estrutura com
5:39
três espaços pra gente poder nomear as
5:42
colunas então meus colegas vão ser e de
5:44
nome e telefone
5:47
então eu tenho as minhas três colunas
5:49
nomeadas o próximo passo é escolher os
5:52
tipos primitivos lembra lá no início de
5:54
uma lista de tipos primitivos estão
5:56
todos aqui olha só o meu e de é inteiro
5:59
mas eu posso escolher qualquer um dos
6:01
tipos primitivos que eu já expliquei pra
6:03
vocês inclusive os tipos espaciais
6:05
lembra de o metrô e point colligan e
6:08
muito mais
6:09
então e de inteiro o nome vai ser achar
6:11
todo já coloca aqui no início e o
6:14
telefone também vou colocar a baixar
6:16
você pode estar pensando no guanabara
6:17
telefone um número não vai achar
6:19
telefone você não coloca o símbolo de
6:21
mais você quiser utilizar o código do
6:23
país
6:23
bota parênteses se você quiser colocar o
6:25
código de área e coloca o iff para
6:27
separar os quatro primeiros dígitos dos
6:29
quatro últimos
6:29
isso depende do lugar do brasil que você
6:31
tá né tem lugar no brasil quem está
6:32
utilizando o formato de três dígitos 1-4
6:35
dígitos nos tipos baixaram também tem
6:37
que indicar o tamanho então vou colocar
6:39
aqui
6:41
então o nome e 11 por telefone se você
6:43
quiser pode colocar algum valor pré
6:45
definido como por exemplo como definido
6:47
no lula é por padrão ou data e hora
6:51
atual
6:53
eu não vou querer nenhum desses deixa
6:55
base aqui eu posso preencher seu quero
6:57
ou não que o valor possa ser nulo por
6:59
padrão phpmyadmin coloca sempre como not
7:02
no pão por exemplo eu vou deixar que o
7:04
telefone seja nulo uma pessoa pode ser
7:06
cadastrado e não ter telefone fax e-mail
7:09
inútil mas sei que é só como exemplo
7:11
aqui eu posso indicar qualquer um como
7:13
índice por exemplo eu vou querer que o
7:16
id seja minha chave primária e você já
7:18
viu que a chave primária é aquele campo
7:20
que identifica cada uma das duplas de
7:21
cada uma das linhas se você não sabe
7:23
disso
7:24
assistir às aulas anteriores eu nunca
7:25
vou cansar de encher o seu saco
7:27
você precisa assistir o curso inteiro
7:28
não adianta você cai de paraquedas e
7:30
querer utilizar que o ph pena de mim sem
7:32
uma base inicial pelo menos um banco de
7:34
dados
7:34
na segunda foto que está chegando nesse
7:36
vídeo nesta série de ph pena de mim você
7:38
saiba que esse curso eu não tô falando
7:39
muito sobre modelo relacional eu não tô
7:42
me aprofundando não tô falando ainda
7:43
sobre a uma parte chata que seu
7:45
professor fala desde as primeiras aulas
7:47
de banco de dados
7:48
então estou começando esse curso de uma
7:49
maneira com uma proposta diferente bem
7:51
mais dinâmica colocando a mão na massa
7:53
então dar um voto de confiança por
7:55
guanabara aqui e assistir esse curso
7:56
pequeno da fã 18 vai por mim você vai
7:58
gostar
7:58
vou colocar aqui por exemplo como nome
8:00
comunique a gente já viu o que é o
8:03
unique que é diferente de chave primária
8:07
esse campo aí aqui seria o alto
8:10
incremento então por exemplo se eu
8:11
marcar aqui eu estou dizendo que o meu i
8:14
d
8:14
ele vai ser gerado automaticamente pelo
8:16
sistema se você quiser também você pode
8:18
colocar algum comentário sobre o campo
8:20
eu não vou colocar nenhum embaixo você
8:22
pode escolher qual vai ser a história de
8:23
end que vai ser utilizada e você pode
8:26
utilizar outras indígenas e pode
8:28
escolher por exemplo o mais rã que
8:30
também é bastante famoso
8:31
se você quiser também pode especificar o
8:33
colégio aqui mas a gente já específico
8:36
no banco de dados ele vai seguir o que
8:37
foi especificado lá mas se você quiser
8:39
aqui ó
8:40
você pode ver e escolher na lista o tf 8
8:44
ac também utilizar a mesma colégio da
8:47
criação do banco de dados
8:49
se você quiser pode também colocar
8:50
comentários sobre a tabela colocar
8:52
definições de partição verdade vou
8:53
deixar tudo vazio
8:54
e vou ficar em guarda como você já viu
8:57
nas aulas anteriores o phpmyadmin vai
9:00
criar a base de dados de maneira bem
9:02
simples e sem precisar que você decore
9:04
comandos
9:05
volto a dizer é claro que na hora de
9:07
criar uma base de dados você pode
9:09
utilizar phpmyadmin mas é bom que você
9:11
conheça o funcionamento dos comandos
9:13
crítica era bes e cleide table pra você
9:15
ter o conhecimento prévio da instrução
9:17
sql e poder classificar essas instruções
9:20
como por exemplo o líder abc o cliente
9:22
table são comandos da classe d l
9:25
então o que foi feito aqui foi criar
9:27
automaticamente a minha tabela e vou te
9:29
mostrar uma setinha aqui para você saber
9:31
qual o comando que foi utilizado então
9:32
vem aqui se o banco de dados exemplo ea
9:35
tabela amigos foi criado corretamente
9:37
vamos abrir o nosso console vou dar o
9:40
show terá bases que o mesmo comando que
9:41
eu acabei de dar aqui você pode usar
9:43
certa pra cima pra isso eu tenho um
9:45
banco de dados exemplo vou abri lo e use
9:48
exemplo o banco de dados foi modificado
9:51
e eu posso vir aqui o show tables ele
9:54
teve aqui amigos claro que eu posso
9:56
utilizar qualquer momento descreve ou
9:57
desk amigos pra ver com a estrutura dela
10:00
e de nome telefone ele colocou int de 11
10:04
baixar de 30 baixa de 11 colocou aqui
10:06
ele pode ser no telefone como o mesmo
10:08
especifiquei a chave primária no id a
10:11
chave unic no nome e ele vai poder for
10:14
colocar os valores no saque nos campos e
10:16
inclusive o ex craque do campo e de
10:19
quetta como alto incremento até aí tudo
10:21
bem é o que você está vendo phpmyadmin
10:23
também só aqui no console você pode usar
10:25
um comando especial dá uma olhadinha
10:27
aqui se você quiser ver as tabelas você
10:29
já viu que é o show tables mas se você
10:32
colocar em vez de show tables show
10:35
create table de amigos você vai ver qual
10:41
foi o comando que foi utilizado para
10:44
criar essa tabela tanto em ter aqui ó
10:47
o comando foi cleide table amigos e
10:49
dentinho 11 9 no alto incremente nome
10:52
baixar de 30 à noite no telefone baixar
10:54
11 de forno pra mim aqui é e de munique
10:57
que nome nome
10:59
esse é o nome do seu índice esse é o
11:00
nome do seu campo seu engine foi o idb o
11:03
de focar 7 é o tef 8 mil que legal então
11:06
mesmo criando no pega
11:08
é de mim você pode aprender comandos
11:10
então isso é bastante interessante e o
11:12
mesmo do chocolate table também serve
11:14
por chocolate de base
11:16
acompanhe aqui comigo então se eu der
11:17
show create da deise não é intemporal no
11:23
singular
11:24
o nome do banco de dados exemplo ele vai
11:28
te mostrar o cliente terá mês o cliente
11:30
terá vez exemplo coloca aqui ó de focar
11:32
7 o f8 e botou até de uma forma
11:34
diferente daquela que eu te ensinei
11:36
durante a aula é as duas funcionam
11:39
perfeitamente até aí tranquilo então
11:41
você pode criar uma base de dados e
11:43
criar uma tabela diretamente no
11:45
phpmyadmin e também descobrir quais
11:47
foram os comandos utilizados para cada
11:49
uma delas diretamente no console do mais
11:51
que l voltando aqui ao ph pena de mim
11:53
você vai ver que a tabela foi criada e
11:55
você pode por exemplo aqui ó também vê a
11:57
estrutura da tabela é menor então e de
12:00
nome telefone com todas as informações
12:02
que foram dadas no console de forma
12:04
textual
12:04
elas estão aqui organizadas uma coisa
12:06
que a gente pode fazer que a gente já
12:07
fez nas aulas utilizando comandos é por
12:09
exemplo em vez de theo eu quero telefone
12:12
para fazer isso basta você vir na linha
12:14
do telefone aqui e clicar em muda
12:17
clicando em buda que eu posso modificar
12:19
simplesmente essa coluna digitando aqui
12:23
telefone
12:24
posso modificar também vou botar 15 por
12:27
exemplo aceitar o código de área possa
12:29
modificar o coletivo específico desse
12:31
campo posso modificar qualquer
12:33
informação aqui
12:34
clique em guarda e você vai ver que ele
12:37
vá alterar a coluna telefone e ele aqui
12:39
em cima já está te dando o comando que
12:42
foi utilizado para isso a gente aprendeu
12:44
o comando ao ter table então alternou
12:47
amigos tinha de theo para telefone
12:49
você lembra que na hora de modificar um
12:51
campo você tem o alter table com xande e
12:53
com o modifique ea gente aprendeu que o
12:55
modifique não permite renomear que para
12:57
renomear teria que ser xande
12:59
então ele já está utilizando aqui pra
13:00
você se você quiser você pode ainda
13:02
evitar o comando e trabalha diretamente
13:04
com sql
13:05
basta você clicar aqui e dita ele vai
13:08
abrir uma nova janela do seu navegador e
13:10
vai permitir que você modifique a
13:12
instrução que foi executado viu o php
13:15
admin e é tão simples quanto o pente e
13:17
ele tem até algumas funcionalidades a
13:19
mais porque eu estou utilizando php
13:21
admiro o curso inteiro então para não
13:23
fazer com que você fica com vontade de
13:25
criar sua base de dados em aprender os
13:27
comandos porque como eu disse você
13:29
quando quiser programar em php por
13:31
exemplo vai precisar entender esses
13:33
comandos e por falar em php
13:35
o phpmyadmin como o próprio nome diz foi
13:37
feito em php e ele é focado
13:39
principalmente para a linguagem e é
13:41
possível até gerar códigos sozinho
13:42
utilizando ela a fechando aqui do lado
13:45
do editor você pode ver aqui o que eu
13:46
tenho criar código php
13:48
aqui ele já vai criar uma linha que
13:51
seria a criação de uma variável sql já
13:54
colocando o alter table tudo bonitinho
13:57
para você pegar isso daqui copiar e
14:00
colar no seu código php e se você quiser
14:02
aprender php é uma ótima dica agora que
14:04
você está fazendo o curso de sql é uma
14:06
ótima dica você seguir seus estudos no
14:08
curso em vídeo é claro porque aqui ó
14:10
clique aqui você vai diretamente para o
14:12
curso de php a gente fez um curso básico
14:14
de php
14:15
você precisa saber se básico por exemplo
14:16
apareceu aqui na tela sul dólares sql um
14:20
cifrão sql não significa que é uma
14:22
variável
14:23
você não sabe disso o curso de php vai
14:25
te ensinar isso tudo você quiser que
14:27
também na interatividade eu coloquei
14:29
alguns cursos inclusive o curso de
14:31
algoritmos você sente dificuldade no ph
14:33
p
14:33
então assim é tudo uma seqüência pedido
14:35
da fã a gente está vendo o banco de
14:37
dados aqui já pensando no futuro em
14:39
fazer um curso de php um banco de dados
14:40
mas para você aprender php você também
14:42
precisa saber algoritmo antes então vai
14:45
aqui em cima na interatividade e dá uma
14:46
olhada no que a gente que já criou no
14:48
curso em vídeo com esse vídeo é feito só
14:49
de banco de dados não você chegou no
14:51
consumo cuidados seja bem vindo mas o
14:53
curso vídeo tem uma história tem cursos
14:55
foram criados antes mesmo do discurso
14:56
que está assistindo agora então sinta se
14:59
à vontade para navegar pelas nossas
15:00
playlists porque é tudo de graça
15:02
vamos voltar à estrutura da tabela
15:04
clicando no nome dela aqui você vai ver
15:06
e depois clicando em estrutura
15:09
outra coisa que você pode fazer é
15:11
adicionar novos campos por exemplo eu
15:13
quero adicionar uma coluna no fim da
15:15
tabela ou quero criar uma coluna depois
15:18
de nome
15:21
então ele vai fazer aqui ó a execução e
15:23
vai criar uma nova linha eu vou criar o
15:25
campo e idade tá errado mas vão criar
15:27
idade inteiro
15:29
clique em guarda eo comando ao ter table
15:32
amigos é de idade
15:35
anote no wef ter nome lembra que você
15:37
tem dois parâmetros o ft e o forte e se
15:40
você não colocar nem a apple nem for se
15:42
ele vai colocar no final eu já te
15:43
ensinei isso numa aula anterior
15:45
então tá aqui ó então você vê que apenas
15:47
com cliques o phpmyadmin permite que
15:50
você manipule cri tabelas que manipule
15:53
dados nem todos os comandos de dl dml
15:56
que você já viu até agora com a
15:57
facilidade do clique do mouse e mesmo
15:59
depois de tudo criado você ainda
16:01
consegue ver o comando visualizar qual
16:04
foi o comando que foi utilizado então é
16:06
uma ferramenta também educacional
16:08
vamos voltar aqui na estrutura e ver que
16:10
ele criou o campo idade
16:13
depois do campo nome exatamente como a
16:15
gente fez mas a idade é uma coisa errada
16:17
nos coloca idade no banco de dados
16:18
eu já expliquei porque disso não se você
16:21
colocar a idade agora ela hoje eu tenho
16:22
37 anos é um cadastro no banco de dados
16:25
e quando eu fizer 38 que falta pouco
16:27
como é que fica no banco de dados fica
16:28
37 então o ideal em vez de salvar a
16:31
idade você salva a data de nascimento
16:33
que não pegará pena você consegue fazer
16:35
o cálculo da idade do cara sem problema
16:37
nenhum
16:38
baseado na data de nascimento dele então
16:39
pequeno gafanhoto sempre que dá vontade
16:41
de você cadastra a idade de alguém não
16:43
cadastra cadastrar data de nascimento e
16:45
o próprio mais que 'ele tem o formato de
16:48
data então vou excluir a idade aqui
16:50
basta você clicar aqui e elimina e ele
16:52
vai te dar o comando a aal terceiro
16:54
amigos drop e dady lembra do drop
16:57
o drop utilizado em duas funcionalidades
16:59
seu uso drop table o drop ter a base eu
17:02
apago banco de dados ou a tabela seu
17:04
usual ter time bom com drop top view um
17:07
parâmetro é um parâmetro daughter table
17:09
também o drop pode ser um comando ou
17:11
pode ser um parâmetro se for utilizado
17:13
como comando ele permite que você apague
17:14
uma tabela
17:15
o banco de dados o índice foi utilizado
17:17
como parâmetro ele permite que você
17:19
apague um campo uma coluna então é
17:22
importante que você saiba essa diferença
17:24
então aqui ó
17:25
você quer realmente executar o alter
17:27
table drop idade quero ok ele apagou a
17:30
coluna ea partir de agora uma estrutura
17:31
voltou a ser e de nome e telefone então
17:34
essas são as funcionalidades principais
17:35
na hora de utilizar os comandos de dl de
17:39
definição agora nós vamos partir para os
17:41
comandos de dml que era a manipulação
17:43
dos dados
17:44
antes como exemplo eu vou criar um campo
17:46
sexo aqui olha que interessante
17:48
então eu vou adicionar uma coluna depois
17:52
do nome
17:53
então quero depois do nome quero criar
17:55
sexo
17:56
vou colocar aqui sexo ele vai ser do
18:00
tipo e num que a gente já viu nas aulas
18:02
anteriores ou 7 e não colocar nenhum
18:05
aqui e eu tenho os valores de num vou
18:08
colocar aqui ele vai aceitar m
18:10
ou então efe não é do tipo num vou
18:14
guardar
18:15
ele vai ao terceiro amigos adicionando
18:17
sexo num e mail efe
18:19
continuo é ter o nome ouvir aqui na
18:21
estrutura e eu tenho o campus accionado
18:24
para adicionar um novo registro para
18:26
cadastrar as pessoas com nome sexo
18:28
telefone
18:29
o eta como o numeração também não vou
18:31
precisar informar basta clicar com a
18:33
tabela aberta clicarem insere clicando
18:37
inserir ele já me dá opção aqui você tá
18:39
vendo que o sexo acaba de criar como num
18:41
ele já criou as bolachinhas aqui
18:43
isso porque o e num só vai aceitar m ou
18:46
efe ele já cria as opções pra você olha
18:48
e simplicidade
18:49
olha que facilidade vão preencher os
18:51
dados de duas pessoas aqui então vou
18:53
adicionar maria que é do sexo feminino e
18:57
tem o telefone 2233 pode ligar a maria
19:01
ela atende eu vou cadastrar que o joão é
19:05
do sexo masculino e têm o telefone 21
19:08
2223 333
19:10
mas o joão e maria têm o mesmo telefone
19:11
ao marido e mulher
19:13
feito isso você clique em executar aqui
19:16
embaixo
19:16
cuidado porque tem dois executar se você
19:18
clicar no executado aqui de cima e vai
19:20
executar só a inserção do registro de
19:22
cima que maria se você clicar aqui e vai
19:24
executar só o joão que o registo de
19:25
baixo
19:26
se você quiser você pode executar os
19:28
dois clicando aqui e aqui você ainda
19:30
pode escolher qual é a próxima ação ele
19:32
vai inserir como novo registro e também
19:34
depois ele vai fazer o que ele volta
19:36
atrás ou insere um novo registro
19:39
eu vou fazer pra ele lá inserir um novo
19:41
registro foi executar
19:43
ele já vai me dar que os comandos aqui ó
19:45
insert into eo na tabela de amigos
19:47
os campos e de nome sexo telefone com os
19:50
valores e já coloca aqui os valores
19:52
diretamente de cada registro
19:54
lembra da aula de 7 mil a primeira coisa
19:56
que tem que lembrar não é certinho junto
19:58
então o comando que a gente aprendeu
19:59
durante a aula fazendo utilizada que
20:01
automaticamente
20:02
você tá ficando com raiva de mim porque
20:04
vai esse maldito fez o digital comando e
20:06
aqui ele faz sozinho tal na gafanha
20:08
outro você está aprendendo e você vai me
20:10
agradecer quando chegar lá na frente no
20:12
curso de php um banco de dados
20:14
e você já sabe utilizar os comandos vai
20:16
por mim eu vou fazer você utilizar uma
20:17
ferramenta e digitar comandos a esmo sem
20:20
necessidade
20:21
tudo tem seu objetivo vai na minha top
20:23
cv que lhe permitiu colocar mais dois
20:25
vou colocar aqui
20:26
josé masculino 3363 4444
20:32
parece que ele é vizinho né eu vou botar
20:34
aqui ana ana quer feminina e mora no 12
20:43
222 é síndica do prédio
20:46
vamos clicar aqui e executar só que em
20:48
vez de ser um novo registro ou clicar em
20:50
volta atrás
20:51
ele vai executar e vai voltar pra última
20:54
estrutura que foi lá a digitação do
20:56
comando você quiser você pode vir aqui
20:58
em estrutura e ele vai te mostrar que
21:00
ele tem a estrutura que a gente viu
21:02
antes
21:02
e se você quiser ver o dado que acabou
21:04
de ser criado você pode clicar em
21:05
procurar ele vai dar um selecto eles
21:07
foram amigos exatamente o comando que a
21:09
gente tem utilizado direto que os
21:11
electrões teria inclusive já até
21:12
irritado aqui ó
21:13
a nossa electric ge são cursos que a
21:15
gente utilizou a bola passar dos anos a
21:17
pagar aquilo que não está utilizando
21:18
mas o fato é que o comando que você
21:21
sempre utiliza basicamente ele tem lá as
21:23
minhas colunas também agora você
21:25
consegue visualizar os campos são as
21:27
colunas
21:27
os registros são as linhas as duplas são
21:30
as linhas e além disso ele você pode
21:32
fazer aquilo tudo que a gente viu
21:33
anteriormente
21:34
lembra do comando up date para fazer o
21:36
update 1 dizer o seguinte aqui ó
21:38
o a maria joão se separaram eles não
21:40
moram mais juntos então vem aqui ó edita
21:42
ele vai me dar os dados do joão e eu vou
21:45
botar o telefone de novo aqui 122
21:49
executar
21:51
então ele bota aqui ó então o joão agora
21:54
mora no 12 2002 a ele foi morar com a
21:57
ana
21:57
josafá de ei e outra coisa você vê aqui
22:01
o comando a up date amigos 7 telefone
22:04
para 122 o é e de igual a 2 leva a gente
22:08
vai utilizar sempre o ideia que sempre
22:11
minha chave para que ele não tem
22:12
alterações dúbias para que ele não faça
22:14
a outra imagem o registro
22:16
você lembra também que dá para utilizar
22:17
o limite um aqui sem problema nenhum
22:20
você viu o update e tinha outro comando
22:22
do comando de elite se lembra dele
22:24
então por exemplo que eu vou apagar a
22:26
ana porque já que fiquei bolado com ela
22:28
já não é mais minha amiga porque ela
22:30
tava lá com joão que traiu a maioria são
22:33
várias preta no cemec não pra apagar os
22:35
dados da ana você pode clicar aqui a
22:37
pagar
22:37
ele vai ter o comando de elite from
22:39
amigos o rdd é igual a quatro
22:42
você percebe que antes ele coloca o nome
22:43
do banco de dados constantemente a ele
22:45
bota que o nome da base de dados
22:47
e aqui o nome da tabela isso aqui é
22:49
opcional mas você pode especificar o
22:51
exemplo ponto amigos ea minha tabela
22:53
amigos que está na base exemplo amigos
22:55
ponto de é o meu campo e de que está na
22:57
tabela amigos ou clicar em ok
23:00
ele carregou a foi excluído com sucesso
23:02
agora não tem mais ana se você quiser
23:05
você pode até escolher várias pessoas a
23:06
clicando aqui e apertando aqui embaixo
23:09
ea pagar pra você fazer com os campos
23:11
selecionados alguma operação em massa
23:14
viu como é simples cara é muito fácil
23:16
vamos ver se todos esses dados estão lá
23:18
na minha base de dados mesmo pois sempre
23:20
ficar aqui com o ocidente já que está
23:22
utilizando ele pouco vai pensar aqui
23:24
caramba banco de dados exemplo foi
23:25
criado caota aperta aqui em atualizar ó
23:29
você tem o cadastro eo banco de dados
23:31
exemplo sabendo que está aberto o banco
23:32
de dados de cadastro e clicar duas vezes
23:34
para abrir o exemplo ou bota aqui o iuci
23:37
exemplo né
23:39
então você pode utilizar esse comando
23:41
vou vir aqui nas minhas tabelas na
23:43
tabela amigos na tabela amigos eu tenho
23:45
as colunas e de nome sexo telefone
23:47
vamos ver aqui quais são os amigos que a
23:49
gente tem pressiona contra o inter ele
23:55
vai te mostrar lá maria joão josé avelar
23:57
a situação tá tudo bonitinho sem
23:59
problema nenhum
24:00
uma funcionalidade bem legal que mostrei
24:02
no rock band foi a exportação importação
24:04
de dados se lembra disso
24:05
geraldo dunk o phpmyadmin também
24:08
permitirá da anp para fazer um banco da
24:10
base de dados o que você pode fazer
24:12
clique aqui na casinha é importante que
24:13
você venha antes na casinha para
24:15
exportar uma base de dados que você pode
24:16
clicar aqui em exportar muita atenção
24:20
porque existe o botão de exportar em
24:21
outras partes do php mal de mim
24:24
se você quiser ir ao banco da base de
24:25
dados você tem gente tem que clicar na
24:27
casinha não se esquece disso aquele vai
24:29
permitir que você esporte
24:30
no modo rápido que exporta todas as
24:32
bases que estão aqui inclusive o
24:33
cadastro exemplo tudo mais
24:35
ou então personalizado ele vai ter a
24:37
opção de escolher qual a base de dados e
24:39
quer exportar por exemplo as exportações
24:40
em alta
24:42
deixei o marca aqui ele vai te dá a
24:45
opção aceitável tipo troféu ele vai te
24:48
dizer aqui ó formato utf-8 tudo
24:50
bonitinho não vai ter com pressão
24:52
nenhuma se você quiser ele já se pra
24:53
vocês a base de dados foi grande
24:55
o formato sql você pode exportar até pra
24:58
pdf pode exportar para excel cabe aqui ó
25:01
cef para excel word ele exporta para
25:05
vários formatos
25:06
vou deixar a escola é que são as
25:07
instruções se você quiser você pode
25:09
mostrar os comentários têm uma opção
25:11
aqui que é incluir creatina base que a
25:15
gente viu antes que na exportação que
25:17
aqui ó
25:19
noutro bent só clicar aqui
25:22
em cerva data esporte ele permite
25:25
na verdade ele chama de incluir críticas
25:29
que mama é a mesma coisa que você vir
25:31
aqui e marcar weah e crítida vez se você
25:35
quiser também pode criar todos os
25:37
procedimentos não tem um procedimento no
25:40
cliente tempo ele vai marcar o iff norma
25:42
existisse um alto incremento
25:44
vou deixar tudo aqui faço algumas outras
25:46
configurações não vou fazer mais nenhuma
25:47
aqui e clique em executar clicando
25:52
executas ele já vai gerar o arquivo 127
25:55
0 0 1 ponto sql
25:56
vamos abrir a pasta ele vai abrir aqui ó
26:00
o arquivo sql vou clicar com o botão
26:03
direito e destacou que pede mais mágica
26:04
ferramenta que instale aqui é gratuita
26:06
se você quiser
26:07
ou então você pode abrir com o seu bloco
26:08
de notas normal se você não tiver nos
26:10
pés mãos vou abrir só pra geral a
26:14
colorização aqui então você vê ó é o da
26:16
anp semelhante não é exatamente igual ao
26:19
outro
26:19
mas ele é bem semelhante e sidão anp
26:21
também serve para importá la no
26:23
worldbench na verdade esse tanque são as
26:25
instruções que foram utilizadas para
26:27
chegar à base de dados nessa estrutura
26:29
além disso a gente não pode manipular
26:30
por alguns comandos de dl as tabelas e à
26:33
própria base de dados
26:34
apagando elas eu possa eliminar uma
26:37
tabela vindo aqui clicando no nome da
26:39
tabela vindo em estrutura selecionando
26:42
aqui ou simplesmente clicando em ele
26:44
mina ele vai te dar o comando a drop
26:46
table amigos ok ele vai apagar
26:49
lembrando que o drop table apaga a
26:51
estrutura e também os dados se quiser
26:54
pagar só os dados você usa o tom kitt
26:56
não se esquece disso pra pagar à base de
26:58
dados também é simples você pode vir
27:00
aqui na casinha clicar em base de dados
27:03
escolher a base de dados por exemplo
27:05
aqui exemplo e clicar em elimina aqui
27:09
embaixo
27:09
ele vai te dar o comando a drop terá vez
27:12
exemplo
27:12
ok eo banco de dados foi eliminado
27:15
vamos ver aqui no nosso oponente vamos
27:18
atualizar e você vai ver aqui que a base
27:22
de dados já foi excluída
27:25
e aí gostou phpmyadmin é claro que ele
27:28
tem muitas outras funcionalidades mas o
27:30
que eu quis mostrar aqui é o phpmyadmin
27:32
fazendo aquilo que você já fez até agora
27:34
no curso de banco de dados
27:35
então fique à vontade para aprender as
27:37
novas funcionalidades dele a gente vai
27:38
dar uma parada aqui no phpmyadmin porque
27:40
a gente tem que aprender novos comandos
27:42
e na próxima aula têm uma aula especial
27:44
foi criada para você que a aula que vai
27:46
aprofundar no comando mais famoso do sql
27:48
que é o comando select então na próxima
27:50
aula a gente começa a estudar a fundo a
27:53
estrutura do select e quais são as
27:54
possibilidades que ele te dá para buscar
27:57
dados no banco de dados
27:58
é isso aí meu querido como sempre venho
28:00
aqui pedir
28:01
clique aqui para você se inscreva no
28:03
canal caso você não seja inscrito se
28:05
você já inscrito está se inscrevendo
28:06
agora não se esquece que do lado do
28:08
botão se inscrever e depois que você se
28:09
inscreve numa engrenagem zinha clica
28:11
nela vai ter uma opção para você assinar
28:13
o canal e dizer que você quer receber um
28:16
e-mail sempre que sai uma aula nova
28:18
você sabe que a gente só lança vídeo
28:19
legal pelo menos divertido clicando aqui
28:21
você vai pra playlist completa e ver
28:23
todas as aulas mas kelly feito até agora
28:25
essa é uma aula bem mais pra frente do
28:27
curso tenho mais aulas básicas você
28:29
chegou aqui só pelo phpmyadmin saiba que
28:32
aqui ó tem um curso completo de banco de
28:34
dados
28:34
ele é bem legal para iniciantes pra
28:36
galera que nunca viu tudo de banco de
28:38
dados está gostando bastante e espero
28:40
que você seja mais um desses me dá uma
28:42
honra de seu professor e nunca se
28:43
esqueça aqui no meio tem o curso em
28:45
vídeo
28:45
lá você pode acessar e fazer seu login
28:47
assistir às aulas por lá e assistindo
28:49
por lá eu te dou um bônus no final do
28:52
curso assim que todas as aulas
28:53
terminarem
28:54
você vai poder imprimir um certificado e
28:56
um gafanhoto certificado
28:57
pelo curso em vídeo dizendo olha já fiz
28:59
o curso de banco de dados e serve para
29:01
todos os cursos
29:02
então aqui em cima interatividade os
29:04
cursos principais estão aqui ou então
29:06
acesso à nossa plataforma e dá uma
29:08
olhada por lá
29:09
é isso aí porque o gafanhoto a gente se
29:11
vê na próxima aula se prepara que foi
29:12
muito select por aí
29:14
um forte abraço e até lá
"""









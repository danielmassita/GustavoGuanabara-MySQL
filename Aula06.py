# Curso MySQL #06 - Alterando a Estrutura da Tabela (ALTER TABLE e DROP TABLE)
# https://youtu.be/To9qUcEMuY0
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/alterando-a-estrutura-da-tabela-alter-table-e-drop-table/

"""
Aula 06 - Curso MySQL #06 - Alterando a Estrutura da Tabela (ALTER TABLE e DROP TABLE)


"""





"""
Transcrição


0:20
Olá, pequeno gafanhoto seja bem vindo a mais uma aula do seu curso em vídeo de banco de dados!
0:25
O meu nome é Gustavo Guanabara, eu sou seu professor. E chegamos aqui a sexta aula do curso de banco de dados.
0:31
Pra falar sobre um assunto dando continuidade ao que vimos na aula passada. E dessa vez nós iremos aprender a alterar a estrutura de uma tabela.
0:38
Então Recapitulando Agente está fazendo a aula, assim, passo a passo, de Banco de Dados Cada aula agente ver, 1, 2 comandos no Máximo
0:45
A ideia é exatamente essa E agente já fez a criação do banco, A criação da tabela Agente já inseriu dados na Tabela
0:52
E agora agente vai fazer uma modificação da estrutura dessa tabela Pra isso Agente vai aprender dois comandos novos nessa aula
0:58
Então meu querido Ativa ai seu servidor 'MySql' Abre as Ferramentas Fecha o Facebook que eu to vendo!
1:04
E vamos trabalhar! * Som de Sino * Apenas relembrando Agente tinha criado essa estrutura ai no nosso banco de dados
1:11
A gente tem uma tabela chamada pessoas Com os campos: Id, nome, nascimento, sexo, peso, altura e nacionalidade, e o meu ID é minha chave primária
1:22
Vamos aqui ativar o nosso servidor 'MySql' Abre o WampServer Oh, está vermelho
1:27
Vamos aguardar ficar verde... Ficou verde. Agora nosso servidor está ativo Vamos abrir também o nosso 'Workbench'
1:33
Oh lá oh, Minha conexão está ativa Cliquei sobre ela Ele vai abrir o 'Workbench'
1:39
já, com o ultimo status Então nós temos o banco de dados, "Cadastro" Se não estiver em negrito clica duas vezes, pra abrir
1:45
nós temos as tabelas Dentro das tabelas, nós temos a tabela "Pessoas" Com todas aquelas informações oh
1:51
ID, nome nascimento, tudo bonitinho aqui já organizado E agora eu vou propor algumas alterações na tabela
1:58
A primeira coisa que vamos aprender é o comando para alterar a estrutura da tabela E é fácil ALTER TABLE
2:03
ALTER TABLE Significa alterar tabela e a primeira coisa que nós iremos fazer com o ALTER TABLE É adicionar uma nova coluna
2:10
Presta atenção no seguinte: Lembra que agente tem, Um banco de Dados No banco de dados agente tem, as tabelas
2:15
As tabelas têm os campos Os campos no 'MySql' são chamados de colunas
2:21
Então sempre que você for ver a palavra "column", ou "Coluna" Você está se referindo aos campos da sua Tabela
2:27
Então eu vou fazer o seguinte: "ADD COLUMN profissao varchar(10)" Então o que eu vou colocar aqui, é que
2:33
No cadastro de pessoas, eu também vou querer cadastrar a profissão delas. Então Então o que eu vou fazer é acrescentar este campo (ou coluna)
2:40
Utilizando o: "ADD COLUMN" do "ALTER TABLE" Então estamos de volta aqui no workbench E vamos fazer o seguinte
2:45
Se você não quiser só ver a estrutura da tabela assim Você pode usar o comando describe
2:50
describe pessoas; Aperta Ctrl Enter E ele vai te mostrar né descreva para mim
2:57
A palavra describe também pode ser comprimida como desc Então desc no início do comando
3:03
É o comando describe Então Apertando Ctrl Enter também vai ser exibida a mesma coisa Então eu tenho aqui id, nome, nascimento, sexo, peso, altura e nacionalidade
3:12
Vamos acrescentar aqui o comando ALTER TABLE pessoas Vamos adicionar profissao
3:18
Lembrando que a gente não pode utilisar acentos Então profissao vai ficar sem o tio(~) e eu vou colocar os campos sempre em letras minúsculas
3:25
Então eu vou colocar aqui o tipo da profissao De dez E você pode ta achando que dez letras para botar uma profissão é muito pouco
3:31
Pode até ser Mas nessa aula eu vou te ensinar como é que aumenta isso Como é que a gente vai modificar esse tipo de coisa
3:37
Aguarda pequeno gafanhoto tenha fé Vou botar ponto e virgula aqui Ctrl Enter Se você quiser ver se foi tudo certo é só você apertar aqui e ai vai aparecer a tabelinha
3:47
Sem problema nenhum Foi adicionado, tem um verdinho ok Usar o describe também de novo Ctrl Enter no describe
3:54
E agora eu tenho id, nome, nascimento, sexo, peso altura, nacionalidade e profissao
3:59
Exatamente da maneira que eu pedi Viu como é simples um comandinho pequeno já acrescentou um campo na sua tabela
4:06
E ai você pode esta se perguntando Mas Guanabara eu tinha gente cadastrada lá o que aconteceu com a profissao dessas pessoas?
4:12
Vamos dar uma olhada Se você se lembra a gente viu o inicio de um comando select * from pessoas;
4:20
Apertando Ctrl Enter tem lá ó As pessoas foram cadastradas E eu coloquei a profissao ó
4:25
Ja tem profissao Todos eles ja tem profissao Só que com o valor nulo Isso acontece porque a gente adicionou uma coluna
4:32
E não colocou os dados dele Mais para frente no curso nós vamos aprender comandos para adicionar coisas
4:37
para modificar dados nos registros mais para frente a gente vai aprender um comando que vamos poder sem ter que apagar esses registros e colocar tudo de novo
4:45
Nós vamos adicionar a profissao de cada pessoa Mas ai você deve ter percebido que quando a gente adiciona uma coluna
4:51
Essa coluna vai sempre parar no final a profissao foi adicionada como ultima coluna
4:56
Da uma olhadinha aqui Se a gente for no describe ó Ctrl Enter Você vê que a profissao foi adicionada como último campo
5:03
Mas Guanabara e se eu quiser colocar a profissao em outra posição É fácil e eu te ensino
5:09
Mas antes de colocar a profissao em outra posição A gente vai ter que eliminar ela Eliminar uma coluna é tão simples quanto colocar uma coluna
5:16
Então se para adicionar uma coluna eu coloquei ADD COLUMN Para remover uma coluna
5:22
Eu vou utilizar o ALTER TABLE pessoas Só que utilizando DROP COLUMN A palavra DROP é largar né
5:28
Se eu pego uma coisa e largo é DROP Então Largar uma coluna Seria eliminar essa coluna da tabela
5:34
A palavra DROP no SQL também é utilizada em outras situações A gente vai ver mais para frente Então lá da um DROP nessa coluna
5:40
Então, apenas lembrando oh... A profissão está aqui, no último A profissão está aqui no último Se eu vier aqui e colocar alter table
5:48
pessoas drop colum
5:53
profissão Não preciso dizer tipo nem nada, vou simplesmente dropar
6:00
a profissão Pressionando Ctrl+Enter nem uma informação foi dada. Aqui aparece profissão ainda
6:07
Mas vamos atualizar aqui oh... o sistema e automaticamente a profissão sumiu, se você usar o describe... A lá oh...
6:13
Ela foi eliminada do final Agora vem o processo de adicionar ela de novo. Vamos adiciona-la em outra posição
6:20
Por exemplo, após o nome Meu Deus! Essa obra não acaba!
6:27
Antes era martelada, agora é uma cerra elétrica! Tomara que ele não chegue aqui.
6:33
Eentão depois de "dropar" a coluna Nós vamos escolher uma nova posição para ela. E é simples também, Nós vamos colocar ALTERT TABLE pessoas
6:40
ADD COLUMN profissao varchar(10) igual estava antes. After nome, A palavra after é depois, isto é:
6:48
Depois do nome nós vamos adicionar a profissão Vamos testar esse comando ai...Então oh... Eu tenho alter table pessoas, adicionando a coluna profissão
6:56
after nome Então eu tenho uma coluna nome, se você olhar aqui eu tenho uma coluna nome
7:03
após o nome, ele vai adicionar a profissão vamos dar Ctrl+Enter
7:08
E ver o describe, Percebe lá oh... Depois do nome eu tenho a profissão ele adicionou a profissão com aquela estrutura
7:15
Depois do nome Eai você pode estar pensando: Eu fiz um curso de inglês básico Eu sei que after é depois e before é antes, então deve ter
7:24
before não esxite, e ai você fala E se eu quiser adicionar um campo, antes de algum
7:31
Antes do primeiro por exemplo. já que o after só coloca depois Para fazer isso é muito simples!
7:36
Vamos colocar de novo, ALTER TABLE pessoas E eu quero adicionar um campo como o primeiro campo da tabela
7:42
e ai eu coloco ADD column, código int por exemplo, first. então para o posicionamento do primeiro, eu vou colocar first
7:49
para qualquer outro posicionamento após o campo, você vai colocar AFTER e se você não colocar nada, ele considera o último
7:56
não existe o parâmetro last então é o seguinte, se você quiser colocar um campo lá no final, você não precisa dizer nada
8:02
coloca o alter table add column se você quiser colocar após qualquer outro campo, você vai colocar after
8:08
e se você quiser que ele seja o primeiro campo você coloca first então vamos fazer o teste, vamos lá!!
8:13
vou colocar alter table pessoas, vamos adicionar a coluna código
8:22
do tipo "int" lá no primeiro apenas uma pequena observação, seguinte: a palavra column aqui, ela é opcional, se eu tirar ele também funcionar
8:32
eu posso usar de forma simplificada alter table pessoas adicionando o codigo int, como primeiro campo
8:38
vamos ver se funciona dou enter, e vejo se ele adicionou, vamos ver o describe clico na linha, ctrl+enter, olha lá ó, o codigo e do tipo int
8:47
e está logo no inicio e ai, viu dificuldade nisso? eu também não vejo!!
8:52
e outra coisa que a gente pode fazer com alter table a guanabara eu adicionei o campo profissão mas eu coloquei só 10 letrinhas, eu quero aumentar, quero colocar 20 letrinhas
9:01
é fácil também meu querido e a gente usa o mesmo alter table para você alterar a estrutura da definição
9:06
a gente vai utilizar em vez de add column uma outra palavrinha no lugar do add que é adicionar
9:12
nós vamos usar o modify é só eu colocar modify column profissão varchar de 20 por exemplo
9:18
a palavra modify ela significa modificar, ta muito perto de você entender e você consegue alterar tipo primitivo do campo
9:26
e todas as constraints você pode redefinir as constraints você só não pode renomear um campo
9:31
Então por exemplo, profissão. Se você quiser renomear profissão e chamar de profi por exemplo. Não da pra usar o modify, mas agente vai aprender já já qual é a palavra para renomear também.
9:40
Por enquanto, vamos aprender a usar o modify. então o que eu vou fazer aqui oh... Tirar isso daqui vou botar alter table pessoas
9:47
modify colum Como eu disse antes, column é opcional
9:53
Posso não colocar eu gosto de colocar, principalmente quando eu estou dando aula. e vamos modificar profissão
9:59
para varchar de 20 Posso colocar até constrant como por exemplo:
10:05
not null, e dou o ponto e virgula Pressiono Ctrl+Enter Ele me deu um warning, ele me deu um aviso aqui
10:11
e é fácil de entender, dá uma olhadinha aqui. Se você perceber, eu coloquei uma constraint not null
10:17
Isto é, a profissão não pode ser nula. O problema, é que quando eu dou select para ver os campos, registros cadastrados.
10:25
Lembra que ele tinha adicionado a profissão como um campo e colocou como tudo nulo? Então se você coloca que um campo novo não pode ser nulo
10:33
e quando o mySql adiciona uma coluna nova e coloca tudo como nulo. teve um conflito ai. Então ou você tira a contraint
10:39
ou você pode fazer isso aqui que eu vou te mostrar... você pode colocar por exemplo o default para vizio. Abre e fecha aspas
10:45
Vamos executar... E agora ele aceitou Dando select, você vai perceber que a profissão ficou vazia aqui. Tranquilinho?
10:53
Então a gente nunca pode fazer que uma constraint passe por cima da outra. se não você vai receber esse aviso Mas e se eu quiser, guanabara, modificar o nome da coluna? Não tem como eu modificar usando o modify
11:03
Não tem como Mas eu vou te mostrar um outro parâmetro que você vai utiliazar no lugar do modify Se você quiser modificar o nome de uma coluna
11:11
e também suas constraints e seu tipo primitivo. No lugar do modify você vai utilizar CHAGE
11:17
Só que o change tem uma sintaxe um pouquinho diferente O change ele é chatinho porque você tem que botar o nome velho e o nome novo.
11:23
Então se você não for mudar o nome da coluna, você utiliza o modify. Modify permite somente mudar o tipo primitivo e as constrints
11:32
mas se você quiser mudar o nome, você vai ter que utilizar o change Vamos dar uma olhada ai. Eu vou criar aqui em baixo oh, alter table pessoas change coloumn profissao
11:44
Então profissao é o nome da coluna que existe no momento eu tenho uma coluna profissao e eu vou mudar para prof varchar(20)
11:52
Uma coisa que é o seguinte, olha só.. se eu faço desse tipo aqui, ele vai perder essas configurações de not null e default
11:58
se eu quiser manter as configurações antigas, eu tenho que colocar aqui... not null e default vazio
12:04
eu não vou colocar só pra ele ver se vai continuar com as configurações ctrl + enter, vamos dar o describe aqui.
12:13
e você percebe que ele tem lá... a profissão, ele aceita nulo. Antigamente não aceitava e não tinha o valor default
12:21
então eu tenho aqui a profissão que agora se chama prof varchar(20) Ele aceita nulo
12:26
Então aquele not null que tinha anteriormente, perdeu. E o valor padrão também é nulo, ele também perdeu o valor padrão.
12:34
Então eu tenho que especificar se eu utilizar o change não posso utilizar o change só para renomear a coluna.
12:41
eu tenho que renomear a coluna e colocar todas as contraints que ele tem. Ficou claro? Então eu te mostrei duas opções
12:47
O modify, para modificar tipos e constraints E o CHANGE que é também que é para modificar o tipo as constraints e o nome da coluna.
12:56
Mas e se no lugar de renomear uma coluna, eu quiser renomear uma tabela inteira? Dá pra fazer e eu vou te mostrar como.
13:02
Para renomear no lugar da coluna a tabela inteira, Você também vai utilizar o alter table, alter table pessoas
13:08
e vai utilizar o parâmetro RENAME TO Então nós vamos modificar o nome da tablea pessoas para Gafanhotos ;)
13:15
Lembrando que nós temos o modify, que é pra modificar coluna change, que é pra modificar coluna também.
13:21
E o RENAME TO é pra modificar o nome da tabela inteira Vamos ver s funciona Então vou colocar aqui em cima ó
13:28
Depois do describe eu vou colocar alter table pessoas rename to
13:34
Percebe aqui que eu coloco em outra linha mas você poderia colocar tudo na mesma linha É só uma quetão de organização gafanhatos;
13:40
Vou pressionar Ctrl + Enter Parece que nada aconteceu inclusive Inclusive aqui continua pessoas
13:46
Mas eu vou dar um desc pessoas aqui Ó ja me deu um errro dizendo que a tabela pessoas não existe
13:53
Ela não exite porque eu acabei de renomear-la para gafanhoto E ai se fala poxa mas não ta aparecendo la em cima
13:59
É porque você não deu refresh, vamos apertar aqui O Botão de Refresh (CANTO SUPERIOR ESQUERDO) e agora a tabela que tenho aqui é 'gafanhotos'
14:06
se eu der 'DESC ganfanhotos;' tá feito lá. viu como é simples? e ainda dá para fazer várias outras coisas com o 'ALTER TABLE '
14:12
mas para isso eu tenho que criar uma tabela extra . vamos começar o trabalho aqui. vamos criar uma nova tabela com a seguinte estrutura:
14:19
eu quero os campos `nome`, `descricao`,`carga`, `totaulas` (total de aulas) e também o `ano`
14:25
esses dados vão ser para cursos então eu vou criar uma tabela chmada cursos
14:30
percebe lá em cima que usei o 'CREATE TABLE IF NOT EXISTS' o 'IF NOT EXISTS' ou o 'IF EXISTS'
14:36
é um parâmetro muito legal do 'CREATE' que é o seguinte: você só vai criar uma tabela ou um banco de dados se ele não existir
14:43
você só vai apagar uma tabela ou um banco de dados se existir então você tem os parâmetros 'IF NOT EXISTS' e 'IF EXISTS'
14:50
vamos agora definir a estrutura de cada um desses campos o `nome` vou colocar como VARCHAR de 30, a `descricao` como TEXT...
14:58
e não confunda VARCHAR com TEXT TEXT como a gente já viu na aula de tipos primitivos, é para textos longos, uma descrição
15:04
eu posso botar vários parágrafos, vários valores a carga horária (`carga`) é INT o total de aulas (`totaulas`) também é INT
15:11
e o ano` é YEAR agora vamos partir para as nossas constraints alguns campos aqui planejei com constraints
15:17
o `nome`que é VARCHAR (30) eu vou colocar como 'NOT NULL' isso porque você não pode cadastrar um curso sem nome , né?
15:22
o nome é obrigatório e outra coisa, não dois cursos no mesmo cadastro com o mesmo nome
15:27
por exemplo curso de java, tem curso de java para iniciante e curso de java para avançado, sei lá... não pode ser assim: curso de java, curso de java
15:34
o cara se enganar. então tem uma constraint só para isso essa constraint é a 'UNIQUE' não confunda UNIQUE com PRIMARY KEY
15:41
PRIMARY KEY além de ser unique ele tem outras características então é o seguinte, o UNIQUE é o seguinte, eu não tô lhe dizendo que o nome é uma chave primária
15:48
ele não vai identificar os registros mas ele não vai deixar colocar dois cursos com o mesmo nome
15:54
a `carga` ela é INT. `carga` é carga horária, é quantas horas tem o curso, sei lá. eu vou botar um curso de 10 horas, curso de 40 horas
16:01
é um número inteiro, mas percebe que esse número nunca é negativo ah, quantas horas tem um curso? ah eu fiz um curso de menos 18 horas que foi oh... uma bosta
16:08
se bem que tem uns cursos por aí que parece ter menos horas que ... é o normal, mas deixa isso para lá.
16:14
o fato é no meu banco de dados aqui eu não vou aceitar cursos com carga negativa então o que vou utilizar uma constraint específica aqui
16:20
para `carga` que é do tipo INT eu vou colocar a constraint UNSIGNED UNSIGNED significa sem sinal
16:26
isso vai economizar um Byte para cada registro que tenha `carga` registrada e o `ano` vou utilizar um constraint aqui pro YEAR que vai ser DEFAULT '2016', isso é:
16:35
se o curso cadastrado não tiver definido o ano de criação então colocar 2016 que é o ano atual
16:40
perceba ali embaixo que `ano` YEAR DEFAULT 2016 não tem vígula porque é a última definição e o DEFAULT CHARSET lá no final coloquei utf8 para a gente não ter
16:49
problemas de digitação, de acentuação lá no campo `nome`. Beleza? você deva está sentindo falta de uma chave primária aí,calma meu querido, digita dessa maneira aqui
16:58
acompanha o raciocínio do tio. então vou fazer o seguinte. vou pressionar + aqui selecionar tudo e apagar. vamos colocar o comando novo aqui
17:06
CREATE ...IF NOT EXISTS quer ver? por exemplo, vou criar uma tabela
17:11
CREATE TABLE IF NOT EXISTS ... vou tentar criar uma tabela `gafanhotos`
17:20
`gafanhotos` vai ter um `teste` tipo INT só isso o comando está totalmente certo. o problema é que se eu criar uma tabela `gafanhotos`
17:29
ela vai sobrescrever o que eu tenho aqui tudo bonitinho, oh, com as colunas todas organizadas, eu vou perder isso tudo. seu faço isso, oh, se eu boto isso aqui e dou +
17:39
você vai apagar a tabela `gafanhotos` e criar uma nova mas eu vou fazer o seguinte, oh, isso só vai criar a tabela `gafanhotos` se ela não existir
17:49
vamos ver. vou apertar + aqui e oh, ele te deu um warning , oh, nenhuma linha foi afetada
17:55
teve um warning que foi a tabela `gafanhotos` já existi vamos então criar a tabela cursos, os campos que eu vou ter são `nome`, `descricao`,`carga`,`totaulas` e `ano`
18:09
botar aqui DEFAULT CHARSET = utf8 vamos colocar os nomes aqui, os tipos , né? VARCHAR de 30 pro `nome`
18:18
a `descricao` vai ser TEXT a `carga` vai ser INT, total de aulas ( `totaultas`) também INT e o `ano` vai ser YEAR
18:27
vamos às constraints. o meu `nome`não pode ser nulo ( NOT NULL) e vai ser UNIQUE (único)
18:33
botar vírgula no final, não esquece, a descrição não vai ter nenhuma constraint , vou botar a vírgula a `carga` vai ser UNSIGNED e o total de aulas (`totaulas`)também vai ser UNSIGNED, tá?
18:42
e o YEAR vai ser DEFAULT '2016' lembrando que, mesmo sendo numérico, eu tenho que colocar entre aspas simples
18:50
tá digitado o nosso comando, vamos pressionar + , oh, percebe lá embaixo o botãozinho verde
18:56
tá tudo ok, esconder aqui embaixo e vamos atualizar aqui. então agora você percebe que nós temos 2 tabelas
19:03
tabela cursos e a tabela gafanhotos tabela cursos com as colunas que eu defini lá. basta clicar aqui em cursos e você vê também aqui embaixo
19:12
a estrutura ou você vem aqui e coloca DESCRIBE ou DESC cursos;
19:18
+. ta lá. tudo na mais perfeira tranquilidade? agora o que nós vamos fazer é adicionar a chave primária, por exemplo: criamos a tabela
19:25
e esquecemos de fazer a chave primária ah, eu vou ter que apagar a tabela e fazer de novo. não. a gente aprendeu a adicionar um campo, não aprendeu?
19:33
então vou colocar o código do curso como primeira coluna para fazer isso vou utilizar o ALTER TABLE `cursos`, que é o nome de nossa tabela
19:39
ADD COLUMN `idcurso` INT FIRST; então eu vou colocar o identificador do curso como primeira coluna na minha tabela de cursos
19:46
isso a gente já viu, esse comando já foi dado. então vamos fazer aqui, oh, ALTER TABLE cursos
19:53
adicionando a coluna (ADD COLUMN) identificador do curso (`idcurso`) como inteiro ( INT)
20:00
na tabela como primeira coluna (FIRST); +. vamos dar o DESCRIBE aqui
20:07
adicionei o id do curso, ta lá, tudo bonitinho como primeiro campo lá, tá a primeira coluna da tabela. Beleza?
20:13
a partir de agora a gente vai utilizar mais um comando para adicionar a chave primária não tem como adicionar a coluna e colocar ela como chave primárias em um comando
20:20
a gente tem que utilizar dois e esse segundo comando é tão simples quanto o primeiro nós vamos dar
20:25
ALTER TABLE cursos adicionando (ADD), em vez de COLUMN, PRIMARY KEY para `idcursos` viu como é que é simples?
20:32
a gente vai fazer parte do que deveria ter feito lá no CREATE TABLE, só que agora dentro do ALTER TABLE porque a gente esqueceu de fazer
20:38
então em vez de digitar ADD COLUMN ou simplesmente só ADD, porque COLUMN é o padrão nós vamos colocar ADD PRIMARY KEY
20:45
e nesse caso você não pode omitir o PRIMARY KEY então vamos lá, vamos dar o ALTER TABLE `cursos`
20:52
vamos adicionar (ADD) uma PRIMARY KEY para `idcursos`
20:57
ponto-e-vírgula, + adicionou, vamos ver aqui, no DESCRIBE, se nós temos ela lá, oh.
21:04
o nome é único, oh lá UNIQUE, e o id docurso (`idcurso`) é PRIMARY KEY
21:10
provando que os dois são realmente diferentes. chave primária é a única, mas não é simplesmente única
21:16
o nome é único, mas não é chave primária chave primária vai ser aquilo que você define como PRIMARY KEY
21:22
UNIQUE é uma outra coisa não confunda as bolas, pequeno gafanhoto você pode está imaginado aí: " caramba o Guanabara me prometeu lá no início da aula que ia me ensinar
21:30
2 comandos até agora só vi ALTER TABLE, ALTER TABLE, ALTER TABLE" ALTER TABLE é um comando grande, ele tem vários parâmetros
21:35
não é nem dos maiores, vai se preparando aí quê, quando a gente começar no SELECT a coisa vai começar a ficar bonita. mas eu vou te ensinar um novo comando aqui
21:42
existe um comando agora, por exemplo: se eu quiser apagar uma tabela que eu criei se eu quiser apagar a tabela cursos
21:48
vou utilizar o ALTER TABLE com DROP? não. ALTER TABEL com DROP é para apagar colunas
21:53
para apagar tabela inteira o comando é diferente por exemplo, se eu quiser apagar a tabela cursos que eu acabei de criar
21:59
eu posso utilizar o comando DROP TABLE cursos; viu como é que é simples? viu como a palavra DROP apareceu de outra forma?
22:06
a palavra DROP ela pode ser um parâmetro de ALTER TABLE então, ALTER TABLE DROP é para apagar coluna
22:12
mas se o comando for DROP, no modo DROP TABLE alguma coisa ou DROP DATABASE alguma coisa
22:18
eu vou apagar o banco de dados ou a tabela que defini no comando é claro que não vou apagar minha tabela cursos que acabei de criar, ela tá bonitinha aqui
22:25
eu vou criar uma tabela qualquer para a gente poder ver como é que apaga então, mais uma vez vou selecionar tudo
22:30
+. apaguei. e vamos fazer o seguinte, oh CREATE TABLE IF NOT EXISTS
22:38
agora vou començar a usar direto isso daqui. criar uma tabela `teste` com os campos `id`
22:45
campo `nome` e o campo, sei lá, idade não pode, vou colocar lá, "apaga logo", não tem problema não
22:53
vou nem botar CHARSET aqui + ... vou atualizar aqui, oh.
22:59
agora eu tenho as tabelas cursos, gafanhotos e teste vamos adicionar, sei lá, um registro aqui no cara. INSERT INTO teste
23:10
os valores, vou colocar os valores, '1' pro `id`, 'Pedro', idade '22', vamos colocar também
23:21
isso, a gente já viu em uma aula anterior, né? se você perdeu isso acessa a play list do curso para poder não ter dúvida no comando INSTERT INTO
23:29
nem pra eu deixar de *free mar * esse também, né? 'Maricota'
23:34
tem '77' anos vou adicionar essas três pessoas aqui pressionando +
23:40
e, eu pressionei o + duas vezes, oh o que vai acontecer, oh. SELECT * FROM teste;
23:47
olha que belezura oh lá, Pedro, Maria e Maricota foram adicionados três vezes se você perceber aqui, oh, o `id` está se repetindo, inclusive
23:55
isso porque eu estou sem chave primária, viu a importância da chave primária aí? então se o id fosse chave primária, eu não teria esse problema
24:01
mas essa tabela aqui já está prestes a ir embora o fato é: eu criei uma tabela, adicionei registros
24:06
com um único comando eu apago a tabela e os dados que estão dentro da tabela
24:11
então tenho as tabelas, oh, curso, tenho gafanhotos, e teste dei o SELECT, ta tudo bonitinho.agora eu vou dar um DROP TABLE
24:20
você pode botar IF EXISTS isto é, eu vou apagar, sei lá, se existir a tabela `alunos`
24:27
essa tabela, ela não existe, então eu não vou poder apagar eu só vou apagar se ela existir +, oh, ela te deu um warning lá dizendo que a tabela não existe
24:34
se eu tentar apagar aqui teste, que foi a tabela que acabei de criar, oh +, oh lá, oh, agora apareceu verdinho não apareceu uma warning
24:42
a tabela não existe mais vamos atualizar cursos e gafanhotos, a tabela teste que existia aqui , não existe mais. ficou tranquilo?
24:50
tá com muito comando? essa aula acabou, fica calmo, respira, testa tudo, porque essa aula chegou ao fim.
24:57
mas mais pra frente a gente vai ver mais comando. por enquanto a gente encerrou a maioria das possibilidades
25:02
dos comandos ALTER TABLE e DROP TABLE. e aí, vem um questionamento: na aula passada
25:07
eu defini CREATE TABLE e CREATE DATABASE como comandos DDL, comandos de definição
25:13
e o INSERT INTO como comando DML, comando de manipulação de dados e aí eu te pergunto:os comandos ALTER TABLE e DROP TABLE se encaixariam em qual classificação?
25:24
DDL ou DML? vou te dar um tempo para pensar. então, DDL são comando para a definição da tabela
25:30
eu defino estrutura, eu mexo na estrutura os comandos DML são para manipulação de dados
25:35
aí eu te pergunto, ALTER TABLE e DROP TABLE eles mexeram em que? na estrutura ou nos dados?
25:41
o ALTER TABLE é mais fácil, né? o ALTER TABLE mexe na definição ele mexe na estrutura, então é um comando classificado como DDL
25:49
o DROP TABLE voê até pode gerar uma confusãozinha, por que , olha só, uma coisa que é importante. na hora que eu botei lá: DROP TABLE `teste`
25:55
ele apagou a tabela e apagou os dados também aí cê fala:"poxa ele não pediu uma confrimação?"
26:01
cara, olha só, presta atenção se você foi capaz de digitar DROP TABLE e o nome da tabela
26:07
é sinal que você quer apagar. ele não vai te perguntar: "realmente você quer apagar? " "tem certeza se você quer apagar?",não meu irmão.
26:12
você soube digitar o comando inteiro, então ele vai apagar, não tem + então muito cuidado ao usar os comandos, mantenha sempre um backup de sua base de dados
26:21
uma coisa que é muito comum, nunca mexa no banco de dados em produção, nunca mexa em um banco de dados que está ativo no momento
26:26
sempre crie uma cópia para você poder mexer nele e por acaso você der algum DROP, se você dropar uma tabela se você dropar uma coluna
26:32
todos os dados são perdidos e aí você pode está acanhdo:"ah, então beleza então o DROP TABLE é um comando de DML, ele manipula dados
26:41
não. manipular dados, apagar os dados foi só uma consequência de eu apagar a estrutura
26:46
de uma tabela. exitem comandos para apagar dados, inclusive para apagar todos os dados. isso a gente vai ver mais para frente
26:52
o que nós estamos tratando aqui é o seguinte o DROP TABLE, ele apaga a estrutura da tabela é claro que se eu apagar a estrutura, os dados não se mantêm
26:59
então a classificação agora fica simples. o DROP TABLE também é um comando DDL
27:04
é os dois comando que a gente viu hoje o ALTER TABLE e o DROP TABLE são comando de definição
27:10
♫ tambores ♫ ficou claro? então é isso, pequeno gafanhoto eu espero que você tenha gostado de mais essa aula do curso de banco de dados
27:17
esteja mostrando para as pessoas:"olha só esse curso, que legal e tal, mostra os comando...dé é bátuta "
27:22
e nunca se esqueça, clicando aqui você pose se inscrever e sempre que tiver uma aula legal como essa você vai ser avisado
27:28
clicando desse lado você vai ver a play list com todas as aulas que compõe o curso de banco de dados. e aqui no meio o curso em vídeo, onde você vai poder assistir as aulas
27:36
e as aulas terminarem, quando todas as aulas de banco de dados terminarem você vai poder imprimir o seu certificado
27:42
nunca se esqueça também, vem o Guanabara chato de novo, você não pode assistir essa aula segurando o seu queixo com a mão
27:49
se você tá aqui, né, nesse tempo todo e tá só assim olhando, olhando eu utilizar...
27:54
eu sei usar, você ainda não então ative seu MySQL se você chegou nessa aula, no meio
28:00
e não, não, viu as anteriores tá, a play list que eu mostrei pra vocês... então. lá você vai poder assistir todas as aulas, inclusive como você ativa o servidor
28:09
tem tudo passo-a-passo. aqui a gente está na sexta aula então se você está na 6a aula você tem a 1a, a 2a, a 3a... não pule etapas
28:16
ah, mas eu só vim aqui por causa do ALTER TABLE Beleza, você tem um servidor ativo na sua casa? não tem? então volta aqui, volta para as primeira aulas
28:23
e vê como você instala um ambiente, como é que você faz o teste e tudo mais "ah, mas eu ouvir dizer que o banco de dados, é só se eu tiver em um servidor"
28:29
não, meu querido você pode testar em casa. esto testando aqui sem acesso a Internet então você consegue aprender banco de dados de maneira correta
28:35
mas uma vez falando, a gente não tá criando um curso de banco de dado ou um curso conceitual de banco de dados
28:41
a gente tá criando um curso prático de banco de dado então eu não tô falando ainda de modelo relacional, mais pra frente vou até falar um pouquinho
28:47
mas você tem que ter umas teoria básica de banco de dados para pode assistir esse curso se você não tiver, você consegue criar um banco de dados sem problema nenhum
28:55
só não vai normalizar, só não vai ter a estrutura tão bem elaborada apesar de que eu tô fazendo a estrutura bem elaborada aqui,mas nunca se esqueça
29:03
esse curso em vídeo é para iniciantes então se tiver alguma reclamação "ah, ele mas ele não falou do modelo relacional", beleza
29:08
... ele é para iniciantes, eu gosto de ensinar iniciantes, começando com SQL
29:13
pra ele ver na prática mais pra frente ele vai aprendendo outras coisas mais chatas como modelo relacional, normalizações
29:19
e pra poder evoluir como profissional mas vamos para de papo que essa aula a gente chegou ao fim eu quero deixar aqui um agradecimento a todos os inscritos
29:25
a todo mundo que está tendo paciência com essas marteladas com queimar lâmpada, vê até o final dessa aula que você vai entender o queimar lâmpada
29:32
é luz que apaga cá é difícil gravar essas aulas mas eu tô fazendo pelo esforço, pela força de vontade
29:39
então, nada mais justo você dar aquele joinha compartilhar nas redes sociais favoritar esse vídeo
29:44
mostrar o curso em vídeo pras pessoas eu tô fazendo meu esforço, faça o seu pro curso em vídeo sobreviver
29:50
é isso aí, meu querido, pratique sempre, estude bastante. um forte abraço e até a próxima
29:56
olha, eu fui inventar de gravar coisa diferente, num ângulo diferente, me dei mal, olha só
30:01
♫ trilha sonora ao fundo ♫ isso aqui você sabe que tem lâmpada, né? ê,eu vou só mostrar assim... " ah é fácil só gravar um tutorial", olha só
30:09
sem a luz eu fico assim esse é o tutorial, os primeiros cursos em vídeos eram dessa maneira
30:15
isso tirando esse barulho de martelo era dessa maneira, agora ...
30:21
fica assim, com a luz, é, né, bem melhor só que essa luz, é, oh, isso aqui é uma lâmpada queimada normal, tá vendo, lá embaixo, oh, rompeu o filamento
30:31
agora , há segundos atrás, aconteceu isso, incendiou uma
30:38
e eu fico aqui trancado em uma sala de, sei lá, 3x3
30:44
imagine o tamanho do meu susto, calcule aí. "ah é fácil cara, é só você gravar e colocar na Internet.
30:51
♫ vinheta de encerramento ♫
"""

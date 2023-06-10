# Curso MySQL #05 - Inserindo Dados na Tabela (INSERT INTO)
# https://youtu.be/NCG9niOlm40
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/inserindo-dados-na-tabela-insert-into/

"""
Aula 05 - Curso MySQL #05 - Inserindo Dados na Tabela (INSERT INTO)

- Inserindo (alimentando) dados na tabela! 
- No passado, usamos os seguintes dados e types:
""" 
CREATE TABLE pessoas (
    `id` int NOT NULL AUTO_INCREMENT,
    `nome` varchar(30) NOT NULL ,
    `nascimento` date,
    `sexo` enum('M', 'F'),
    `peso` decimal(5,2),
    `altura` decimal(3,2),
    `nacionalidade` varchar(20) DEFAULT 'Brasil', 
    PRIMARY KEY (id)
) default charset = utf8;
"""
- Vamos aprender a inserir dados nessa tabela, mas vamos relembrar algumas definições: 
- A SQL é separada por CATEGORIAS:
- CRATE TABLE = definição da estrutura da tabela
- 

COMANDOS POR TIPOS DE CATEGORIA
- DDL (Data Definition Language): craete database, create table
- DML (Data Modification Language): 

(id, nome, nascimento, sexo, peso, altura, nacionalidade)

"""
USE cadastro;
DESCRIBE pessoas;

INSERT INTO pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES
('1', 'Godofredo', '1984-01-02', 'M', '78.5', '1.83', 'Brasil'); 

# NÂO EXECUTA!
# Datas em SQL são YYYY-MM-DD
# Como o `id` é um valor do tipo INT, NOT NULL, AUTO_INCREMENT, eu não preciso especificar o `id`. Melhorando o código...

INSERT INTO pessoas
(nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES
('Godofredo', '1984-01-02', 'M', '78.5', '1.83', 'Brasil'); 
SELECT * FROM pessoas;
# 1	Godofredo	1984-01-02	M	78.50	1.83	Brasil

INSERT INTO pessoas
(nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES
('Maria', '1999-12-30', 'F', '55.2', '1.65', 'Portugal'); 
SELECT * FROM pessoas;
# 1	Godofredo	1984-01-02	M	78.50	1.83	Brasil
# 2	Maria	1999-12-30	F	55.20	1.65	Portugal





"""
Transcrição


0:00
Você que assistiu as primeiras aulas de "Banco de Dados"
0:03
deve ter ouvido isto daqui, olha...
0:04
(barulho ao fundo)
0:05
Dá pra ouvir?
0:06
Umas marteladas de vez em quando.
0:08
Acho que dá né?!
0:09
Eu gostaria de pedir desculpas, mas...
0:11
Tem um outro prédio muito próximo que está em obra.
0:15
Então assim, por mais que o estúdio tenha tratamento acústico, não é um tratamento acústico para martelada
0:22
Então, eu fiquei na duvida de lançar ou não...
0:24
Com certeza você vai preferir
0:27
o "Curso em Vídeo" com marteladas
0:28
do que não ter um curso em video.
0:30
Então meu querido, reclama não, agradeço!
0:33
Voltamos para a nossa programação normal...
0:35
(Barulho de Fundo)
0:37
...com marteladas.
0:39
♫ Cantarolando uma música ♫
0:49
♫ Música de Fundo ♫
0:59
Olá, pequeno gafanhoto!
1:00
Seja bem vindo a mais uma aula.
1:02
Essa é a quinta aula do seu curso de "Banco de Dados".
1:05
O meu nome é Gustavo Guanabara,
1:06
eu sou seu professor.
1:07
e nessa quinta aula a gente vai dar continuidade
1:09
a um assunto que a gente parou na aula passada
1:11
que é a "Inserção de Dados na Tabela"
1:13
Sim,
1:14
nas aulas passadas a gente apendeu
1:15
como criar o Banco de Dados
1:16
com "create database"
1:18
e como criar a tabela com "create table".
1:21
Agora, a gente vai aprender a inserir dados
1:23
a alimentar esses dados
1:25
dentro do "Banco" que você criou no seu computador.
1:27
E aí, volta o Guanabara chato...
1:29
Você já criou seu Banco de Dados?
1:32
Você já instalou o seu ambiente "MySQL"?
1:34
Meu querido, olha só...
1:36
Vários alunos já entraram em contato
1:38
e falaram assím
1:38
"Eu não cosigo assistir
1:40
não consigo acertar os exercícios de PHP".
1:43
Beleza!
1:44
Durante a aula você fez os exercícios?
1:46
Se você não fizer, meu querido, não adianta.
1:49
Então, se por acaso você chegou até aqui
1:51
e ainda não fez o seu "Banco de Dados"
1:54
está vendo as aulas primeiro...
1:55
cara, não existe a possibilidade
1:57
de você aprender "Banco de Dados"
1:59
sem praticar.
2:01
Não existe a possibilidade de aprender nada na área de Tecnologia sem praticar.
2:04
E eu te digo mais: não adianta você tentar aprender nada na vida sem praticar!
2:09
Então, dá uma pausa ...
2:11
Você não está fazendo maratona, você não está assistindo uma série,
2:14
você não está assistindo no YouTube um cara jogando Minecraft, pelo amor de Deus!
2:18
Então
2:18
instala seu ambiente ... prepara tudo bonitinho ... e vamos começar!
2:23
Você deve se lembrar, das aulas passadas, eu apresentei meu amigo para vocês
2:27
O nome dele é Godofredo, ele tem 32 anos, do sexo masculino, pesa 78,5 kg
2:32
1,83 metros de altura e ele nasceu no Brasil.
2:35
E nós usamos estes dados do Godofredo para
2:38
criar nossa estrutura do Banco de Dados e da nossa primeira tabela.
2:41
Você lembra dos campos que existem, né?
2:43
Existem os campos:
2:44
nome, data de nascimento, sexo, peso, altura e nacionalidade.
2:49
Você lembra que tivemos que fazer uma pequena alteração
2:52
porque não se cadastra idade no banco de dados.
2:55
Se você cadastrar idade no banco de dados,
2:56
você tem que alterar toda vez que a pessoa fizer aniversário.
3:00
Isso não existe.
3:01
Então se você colocar a data de nascimento da pessoa, fica mais fácil.
3:05
Então vamos fazer uma alteração aqui.
3:07
O Godofredo tem 32 anos mas ele nasceu no dia 02 de janeiro de 1984
3:12
e é essa data que eu vou registar no meu banco de dados.
3:15
Então o primeiro passo já foi dado:
3:16
a gente já criou o banco `cadastro` com a tabela `pessoa`.
3:20
Agora, nós vamos inserir os dados do Godofredo lá dentro.
3:24
Para criar tabelas, se você lembra muito bem, ela teve está estrutura aqui oh:
3:28
Eu utilizei 'CREATE TABLE', coloquei os campos `ID`, que vai ser minha chave primaria,
3:33
E eu coloquei ela como auto-incrementável
3:35
Coloquei um `nome` para aceitar até 30 letras.
3:38
E não se esqueça que o VARCHAR aceita até 30 letras.
3:42
Ele não vai guardar 30 letras.
3:43
Se o nome da pessoa for "Godofredo", ele vai guardar essas letras e as outras ele não vai ocupar.
3:48
Se fosse CHAR, ele ocuparia todas as 30 letras, e completaria com espaço, caso fosse necessário
3:55
Então ele é VARCHAR. Ele é uma quantidade de caracteres variável,
3:58
mas chega até 30 letras, nesse nosso caso aqui.
4:01
Também utilizei o constraint NOT NULL, tanto para o `ID`, quanto para o `nome`.
4:05
Ele não vai aceitar você não digitar, não informar o nome e não informar o ID.
4:09
A data de nascimento é tipo DATE.
4:11
O sexo é ENUM.
4:12
Eu podeira utilizar SET nesse caso.
4:14
Então ele vai aceitar apenas "M" ou "F" maiúsculo.
4:17
O peso é DECIMAL(5,2).
4:19
São 5 casa ao todo, sendo 2 casas para decimais,
4:21
e a altura é DECIMAL(3,2).
4:24
São 3 casa ao todo e, sendo 2 casas para decimais.
4:26
A nacionalidade é um VARCHAR de 20
4:28
e se eu não digitar a nacionalidade
4:30
o DEFAULT vai ser Brasil.
4:31
Por último, dentro da estrutura, eu defini meu PRIMARY KEY, que é minha chave primária,
4:36
como sendo o `id` que é meu primeiro campo lá em cima.
4:38
O DEFAULT CHARSET vai indicar que eu posso aceitar caracteres acentuados
4:42
no padrão latino, que é o padrão que o Brasil utiliza.
4:45
Beleza? Isso foi a aula passada. Volto a ser chato. Se você não fez
4:49
volta as aulas e revê fazendo!
4:54
Agora nós vamos aprender a inserir dados dentro dessa tabela.
4:58
A inserção de dados é muito simples,
5:00
mas antes de dar o primeiro passo, eu quero te dar uma relembrada em uma coisa,
5:03
que é uma definição muito importante.
5:05
Como você se lembra, a SQL, como eu digo que é a linguagem de busca,
5:09
a linguagem total, ela é separada por categorias, ela tem comandos
5:13
que se classificam de acordo com essa categoria.
5:15
O CREATE TABLE que está aqui na tela como exemplo,
5:18
ele é um comando para definição da minha tabela.
5:22
Isso é, eu vou mexer nas definições do banco de dados.
5:24
Todo comando SQL que faz parte da estrutura, que faz parte da definição
5:29
da estrutura de um banco de dados, segue uma sigla.
5:32
Então o comando CREATE TABLE, ele é conhecido como um dos comandos DDL do SQL.
5:38
DDL significa 'Data Definition Languange', ou Linguagem de Definição de Dados.
5:44
Então os comandos: CREATE DATABASE e CREATE TABLE que a gente ja viu até agora,
5:49
eles são comandos ditos DDL.
5:52
Preste atenção somente na letra do meio.
5:54
e defini assim: é sempre D e L.
5:56
É D, de Data e L, de Language.
5:59
O que muda é a letra do meio, a letra do meio sendo D, é Definition.
6:03
Então fica 'Data Definition Languange'.
6:05
Estes comandos DDL, eles são comandos de definição.
6:08
Então, na hora de criar o banco de dados, eu uso um camando para definir uma banco de dados:
6:12
DDL
6:12
Na hora de criar uma tabela, eu utilizei um comando para definição da tabela:
6:16
DDL, também
6:17
E aí, você pode estar perguntando? Mas Guanabara...
6:19
- Exitem outros? - Existem outros!
6:21
Existem DML, DQL, DCL e um monte...DTL.
6:25
Mas a gente vai ver isto aos poucos. Por enquanto, vamos nos focar nos DDL's
6:30
da aula passada, e numa nova classe que a gente vai ver na aula de hoje.
6:34
Ficou claro? Então agora a gente pode partir para o próximo passo
6:36
que é criar o comando para poder incluir dados dentro desta tabela
6:41
que acabamos de definir.
6:43
A primeira coisa que devemos fazer é pegar todos os campos.
6:45
Os campos que acabamos de colocar aqui:
6:46
id, nome, nascimento, sexo, peso, altura e nacionalidade.
6:50
Então o que você vai fazer é, pegar uma lista e colocar os nomes dos campos.
6:55
Percebe aí
6:56
separados por vírgula e entre um parenteses "( )" grandão.
6:59
Então este é o primeiro passo.
7:00
Vamos abrir o ambiente, né, porque eu esqueci de abrir aqui.
7:04
Então vamos ligar nossa máquina, eu estou utilizando o Windows 10.
7:08
Lembrando o Windows 10, WampServer e o MySQL Workbench.
7:15
Está é minha foto de usuário. Modelo.
7:18
Eu sou muito bonito né. ( ͡° ͜ʖ ͡°) Pode falar.
7:20
Acabei de ligar a máquina, você percebe porque você vai fazer isso na sua casa.
7:24
Provavelmente você ja vai esta com a maquina ligada
7:25
se não você não estava vendo. Não, você pode estar vendo no celular né.
7:29
E eu vou abrir aqui o WampServer, primeira coisa
7:32
Lembrando ele vai ficar vermelinho,
7:35
laranja
7:35
e depois verde.
7:36
Laranja...verde.
7:39
Ficou verde, eu venho aqui, e abro o Workbench. O ambiente vai ser carregado
7:46
ele vai me dizer que eu tenho uma instancia no wampmysql 64 bits.
7:51
Vou clicar...
7:52
ele vai abrir a estrutura. Eu estou com o banco `cadastro` e o banco `teste`,
7:57
que vem como padrão, e eu não estou com o cadastro aberto.
8:01
Então, a primeira coisa que temos que fazer é abrir um dos Bancos de Dados,
8:04
no caso nosso `cadastro`.
8:06
Você pode abrir de duas maneiras: ou clica duas vezes em cadastro, o que é bem simples,
8:10
mas vou dar uma relembrada no comando.
8:11
Então eu tenho um comando aqui.
8:13
USE cadastro;
8:14
O comando "USE cadastro;" serve para usar o cadastro.
8:17
Agora ou eu clico aqui neste raiozinho com tracinho em cima
8:19
ou você pressiona o CTRL + Enter.
8:22
O banco cadastro, já foi aberto. Vou abrir as tabelas.
8:27
Eu tenho a tabela `pessoas` Na tabela `pessoas`, eu tenho:
8:30
id , nome, nascimento, sexo, peso, altura e nacionalidade.
8:33
Então, vamos lá. Vamos começar!
8:34
Vou colocar entre parênteses, separados por vírgulas, vou colocar todos os nomes dos campos.
8:40
(id , nome, nascimento, sexo, peso, altura e nacionalidade)
8:50
Lembrando que você pode colocar entre crases, o nome dos campos.
8:57
Mas eu não vou colocar, porque eu não gosto muito, mas você pode colocar aqui.
9:02
Beleza?
9:02
Primeiro passo dado. Esquece aquele errinho ali na frente porque o comando ainda não está completo.
9:07
Vamos dar continuidade aqui.
9:08
A partir de agora na linha de baixo. Vamos dar um espacinho e colocar o seguinte,
9:12
entre parenteses também, e entre aspas simples,
9:14
cada um dos dados que vamos inserir, por exemplo:
9:18
id ('1'), nome ('godofredo'), nascimento('1984-01-02')
9:24
e aí, você pode estar achando estranho essa data neste formato.
9:27
As datas nos bancos de dados MySQL, são dadas da seguinte maneira:
9:30
Primeiro o ano, sinal de menos, depois o mês, sinal de menos, depois o dia.
9:35
Então é exatamente a data no formato contrário do que nós estamos acostumados.
9:38
dia, mês e ano. Coloca ano, mês, dia.
9:41
o sexo é ('Masculino'), o peso é ('78.5'), a altura é ('1.83') e a nacionalidade ('Brasil').
9:47
Nada diferente do que a gente colocou antes, então vamos colocar os dados entre parenteses,
9:52
entre aspas isoladamente cada dado, separados por vírgula e o final, o ponto-e-virgula (;).
9:56
Vamos lá para o ambiente. E, vamos digitar isso aí.
9:58
Vamos colocar: '1', 'Gordofredo', ...[Marteladas Gostosas]....
10:06
...[Soam no meu ouvido]... '1984-01-02', 'masculino', Aqui, o primeiro é o ID, segundo é o nome
10:15
Terceiro é a data de nascimento, quarto é o sexo. Viu, é na ordem.
10:18
Agora vamos colocar o peso, '78,5', e você deve estar com uma dúvida absurda agora.
10:23
Mas "Guanabara"!
10:24
Você ensinou lá na linguagem de programação que,
10:27
o que está entre aspas, é só Character e só String, seria só Varchar?
10:30
Não!
10:31
O que está entre aspas são dados, pro banco de dados: o que está entre aspas são dados.
10:36
O que não está entre aspas, é considerado com (Constraint).
10:38
A gente já vai ver isso, aí.
10:40
Então...
10:40
O peso. Vamos a altura, que é '1,83', A nacionalidade, 'Brasil'
10:46
Fechou a parênteses e ponto-e-vírgula [;].
10:49
Pause o seu vídeo, digite exatamente isto daqui. Não execute ainda, rapaz.
10:53
Coloque aqui, lembrando que a única coisa que termina o comando é o ponto-e-vírgula.
10:57
Isso aqui não é fim de comando, meu comando é que vai ter várias linhas
11:00
Beleza até aí? Vamos dar continuidade!
11:03
A partir de agora agente vai preencher o comando da seguinte maneira, olha só...
11:07
Eu quero inserir na tabela de 'pessoas', aqueles dados, que estão em cima, com os valores que estão embaixo.
11:13
Concorda comigo? Concorda? Concorda? Diz cara!
11:17
Se você concorda ou não? Fala...eu não vou continuar a aula,
11:20
se você não disser! Vai fala. Fala, "eu concordo", fala...
11:24
"Risos"
11:26
Não acredito que você falou com o seu computador
11:28
Maluco!!
11:29
então o que a gente que é
11:30
insira na tabela pessoas
11:31
Os valores, 1, godofredo, 2... e etc
11:34
tranquilo?!
11:35
só que seria ótimo se a gente pudesse escrever em português
11:37
Mas os comandos são em inglês
11:38
mas não é dificil
11:40
insira na tabela pessoas vira insert into pessoas
11:43
os valores, values
11:45
e ai vem o seguinte cara.
11:47
Não é errado, mas pelo amor de Deus insert INTU não
11:52
nada disso o certo é insert INTO
11:54
tem algum problema de falar isso?
11:56
por favor, fala assim comigo?!
11:58
insert "intu" me incomoda
12:00
insert "intu" é péssimo
12:02
então esse é o comando
12:04
insira na tabela pessoas
12:06
com os campos ID, nome, nascimento, sexo, peso, altura e nacionalidade
12:10
os valores: 1, Godofredo,
12:12
A data lá de nascimento
12:14
O sexo dele
12:15
O peso dele, a altura dele e a nacionalidade dele. Simples desse jeito
12:20
Vamos complementar o nosso comando lá
12:21
Então eu vou colocar aqui o comando 'insert into'
12:26
Para ser 'insert into', mas fala 'intiu' cara
12:30
pessoas
12:31
os valores
12:35
só isso, viu?! não tem mas erro
12:37
agora eu tenho um comando prestes a ser executado
12:39
mamamamamama
12:41
calma, não executa
12:42
espera
12:44
aguarda aí
12:44
Você deve se lembrar da estrutura da sua tabela, não lembra?
12:47
eu vou te mostrar
12:48
se você se lembra muito bem, olha aí a estrutura da sua tabela
12:51
o 'ID' ta com um valor inteiro, não nulo... isso é, ele ta inteiro, 1 é inteiro
12:56
é não nulo? é, é 1, não é nulo
12:59
e ele ta com 'AUTO_INCREMENT'
13:00
se você se lembra na aula passada, eu utilizei a constante 'AUTO_INCREMENT'
13:04
para que ele a cada vez que uma pessoa nova seja cadastrada
13:07
o próprio sistema decida, defina sequencialmente como o código vai ser gerado
13:13
então, eu não preciso informar que o 'Godofredo' é o número 1
13:16
eu simplesmente posso dizer, olha só insere isso aí...
13:18
tranquilo?
13:19
então eu não preciso especificar o ID
13:22
vamos ver se funciona!!
13:24
então o que eu posso fazer aqui, ó, é eliminar o ID
13:28
e eliminar o '1' daqui
13:30
então insira nome, nascimento, sexo e etc
13:33
insira o nome godofredo, nascimento 2 de janeiro de 1984
13:36
sexo masculino, peso '78,5', altura '1,83', nacionalidade 'Brasil'
13:42
eu não informei o ID
13:43
isso porque ele é auto incrementado
13:45
vamos executar pressionando ctrl + enter
13:48
"Ahh", antes de executar ó, clica aqui, para exibir a barra de status
13:52
ele já me deu o comando use cadastro, que foi com sucesso!
13:55
caso você execute e esse comando dê problema
13:58
ele vai aparecer um "x" aqui
14:00
então, ctrl + enter, olha lá, inseriu sem problema!
14:04
quer ver se foi inserido mesmo?
14:05
vou mostrar o inicio de um programa que vamos ver mais pra frente!
14:08
mas, é um comando bem simples
14:10
eu vou esconder a parte de baixo
14:13
Selecione tudo de pessoas
14:17
Isso é todos os dados para pessoas
14:20
ctrl + ENTER
14:22
Aqui embaixo, cadastrei o 'Godofredo' com a data que eu coloquei, o sexo, peso, altura e nacionalidade
14:29
tudo certinho
14:30
E o 'ID' foi colocado como 1
14:32
Vamos inserir outra pessoa aqui
14:34
Vou botar aqui: 'Maria', nasceu em: '1999-12-30', é mulher, ela tem 55,2kg e ela tem 1.65m
14:53
Maria vem de Portugal.
14:55
certo!
14:57
Vamos executar.
14:58
Ctrl + ENTER
14:59
Você percebe que sumiu lá de baixo
15:01
Vamos ver se o comando foi executado com sucesso...
15:04
Foi!
15:04
Vou esconder aqui
15:06
Você percebe que eu não tem o 'ID', certo?!, vamos dar o SELECT, clica no SELECT e Ctrl + ENTER
15:11
E ele vai mostrar lá, o 'Godofredo' é ID: 1 e 'Maria' é ID: 2
15:15
E aí você pode estar pensando... mas, ficou faltando o ID lá em cima. Tá me incomodando isso
15:19
Você pode colocar o ID.
15:20
Vamos inserir outra pessoa com o ID colocado.
15:23
Então, eu vou colocar o ID aqui de novo.
15:24
E agora eu não sei qual é o próximo nome.
15:26
Digo o próximo ID.
15:27
Eu não posso colocar aqui , sei lá... 3
15:29
Quer dizer eu até posso, vai funcionar.
15:31
Mas...
15:31
...no lugar do 3 eu vou substituir o valor deste campo por uma CONSTRAINT
15:35
Lembrando que CONSTRAINT's não tem aspas.
15:37
Então, eu vou botar aqui oh!
15:38
DEFAULT, pode ser em minusculo tá, não tem problema não
15:40
O meu ID vai ser o DEFAULT
15:42
DEFAULT, significa padrão
15:44
Então assim, o meu ID vai ser o padrão... isso é!
15:46
Se ele está como auto numeração, ele vai ser o padrão
15:49
Por exemplo...
15:50
Lembra da estutura do banco?
15:51
Vamos voltar aqui na estrutura do banco.
15:53
Se você se lembra muito bem.
15:54
Dá uma olhada lá na nacionalidade
15:56
Nacionalidade é VARCHAR(20).
15:57
E o DEFAULT é 'BRASIL'... isso é!
15:59
Se eu não informar é 'BRASIL'.
16:01
Então por exemplo aqui...
16:02
Vamos adicionar CREUZA...
16:04
CREUZA é uma senhorinha.
16:05
1920... é feminino... pesa 50 kg... mesmo 1,85m... e aqui eu vou colocar DEFAULT
16:16
Isso é, vamos ver o que vai acontecer com a CREUZA.
16:18
ctrl + ENTER
16:19
Vamos ver se funcionou.
16:20
Oh!
16:21
Funcionou!
16:22
É o último comando lá, o comando 6.
16:24
Vamos "dar" um SELECT. Tá lá.
16:25
Olha lá, a Creuza ...
16:27
... tem o ID 3, que foi feito como DEFAULT,
16:29
foi feito o nascimento dela, o sexo, o peso, a altura,
16:32
e a nacionalidade ó, Brasil.
16:34
Eu não informei ...
16:35
... o DEFAULT é Brasil.
16:36
Isso, porque eu defini na estrutura do banco de dados.
16:39
Viu como o uso das DDL's são importantes?
16:42
Então,
16:42
mostrei várias formas de você inserir dados,
16:45
mas, ainda tem mais coisa.
16:46
Então, como eu disse, posso substituir ali o ID, no lugar de 1,
16:50
e colocar a palavra DEFAULT, que fica mais inteligente.
16:54
Também posso colocar o DEFAULT lá no Brasil que, já que o Godofredo é brasileiro,
16:58
posso colocar DEFAULT, ele vai como brasileiro.
17:00
Mas o que importa é o seguinte,
17:01
se você perceber ai na lista,
17:02
ele foi colocado exatamente na ordem em que está lá no MySQL.
17:06
Vamos dar uma olhadinha.
17:07
Se você perceber aqui ó, ID, nome, nascimento, sexo, peso, altura e nacionalidade,
17:11
estão exatamente nesta mesma ordem,
17:13
ID, nome, nascimento, sexo, peso, altura e nacionalidade,
17:17
exatamente na mesma ordem.
17:18
Quando a ordem é EXATAMENTE a mesma, quando você não quer ocultar ou quando não quiser definir,
17:23
qualquer um dos campos,
17:24
se a ordem é exatamente a ordem dos campos,
17:27
você não precisa informar os campos no início.
17:30
Vamos ver como é que funciona isso.
17:32
Então, se a ordem da minha tabela é ID, nome, nascimento, sexo, peso, altura e nacionalidade,
17:36
eu simplesmente posso omitir isso ó, fazendo ...
17:38
... dessa maneira,
17:39
colocando INSERT INTO pessoas, os valores,
17:42
e colocando o valor lá. Fica mais simples ainda.
17:44
Então, se você for inserir dados,
17:46
e a ordem dos campos for exatamente a ordem que foi definida no banco.
17:49
Então, você não precisa dizer quais são os campos.
17:52
Vamos ver se funciona?
17:53
Vamos pra prática.
17:54
Vou inserir outra pessoa aqui,
17:55
sei lá ... Adalgiza,
17:57
nasceu em 1930,
17:59
no mês 11 (Novembro)
18:00
no dia 2,
18:01
é mulher,
18:01
pesa 53.2 kg, mede 1.75m,
18:05
vou colocar o peso em 63.2 kg, já que ela é alta.
18:08
Vou colocar que ela nasceu na Irlanda.
18:12
Sabe lá porque.
18:13
Então vou adicionar aqui.
18:14
Se a ordem é: ID, nome, nascimento, sexo, peso, altura e nacionalidade,
18:20
simplesmente, segundo a regra,
18:22
posso selecionar isso daqui,
18:24
e simplesmente,
18:25
puum,
18:25
apagar, então tá aqui ó.
18:27
Beleza?!
18:27
Então, o que ele vai definir?
18:29
DEFAULT ... é o ID,
18:31
Adalgiza é o nome,
18:32
esse ... é a data de nascimento,
18:34
esse aqui é o sexo,
18:35
esse aqui ... Certo?! Até o final.
18:37
Tem que informar todos os dados.
18:39
Vamos pressionar ctrl + ENTER.
18:40
Vamos ver se ele ...
18:41
adicionou a dona Adalgiza.
18:44
Vem aqui no SELECT. ctrl + ENTER.
18:46
A lá ó.
18:47
Dona Adalgiza foi adicionada sem problema nenhum.
18:50
O código é 4, o nome, a data, o sexo, está tudo perfeito.
18:54
Dentro do banco de dados.
18:55
Viu? Então existe a maneira completa,
18:57
e a maneira simplificada.
18:59
E existe mais uma técnica.
19:01
Você acha que o Curso em Vídeo ia deixar de fora alguma coisa?
19:03
Existem maneiras de inserir vários dados ao mesmo tempo.
19:06
Eu não preciso ficar colocando o INSERT INTO pra cada registro que eu quero colocar,
19:10
eu posso usar um INSERT INTO,
19:12
e cadastrar quantas pessoas eu quiser.
19:14
Como é que se faz isso?
19:15
Eu te mostro.
19:15
Então vamos voltar ao comando anterior.
19:17
Olha só, vamos em INSERT INTO pessoas,
19:19
colocou todos os campos, eles são opcionais, se quiser pode até omitir.
19:23
Vamos colocar os valores.
19:24
A primeira pessoa vai ser DEFAULT, Ana,
19:26
1975-12-22, Feminino, 52.3, 1.45,
19:31
Estados Unidos [EUA].
19:32
Perceba ali no final que eu não coloquei ponto-e-vírgula (";"), eu coloquei vírgula (",")
19:35
E eu vou colocar,
19:36
outro parênteses,
19:38
com os dados da segunda pessoa. Terminou, ...
19:40
... ponto-e-vírgula (";").
19:41
Dá uma olhada nesse código, dá uma pausa,
19:43
e olha bem esse código. Perceba
19:45
que cada registro, que cada pessoa
19:48
está entre parênteses
19:49
Perceba que os dados estão separados por vírgula,
19:52
e cada pessoa está separada de outra também por vírgula.
19:55
Somente a última pessoa,
19:57
vai ter ponto-e-vírgula (";")
19:58
pra encerrar o comando.
19:59
Beleza?!
20:00
Espero que você tenha pausado,
20:01
e analisado.
20:02
Mas , agora vamos digitar
20:04
e vamos ver se isso funciona.
20:05
Então vamos lá,
20:06
Insira nas pessoas ...
20:07
Eu não vou colocar os dados aqui não, tá?
20:09
Vou inserir Cláudio, que nasceu em 1975,
20:13
no mês 4 (Abril), no dia 1º.
20:16
Não, no dia 22.
20:18
Sexo masculino.
20:21
Pesa 99 kg.
20:23
Tem 2.15 metros.
20:25
Gigante.
20:27
Cláudio é do Brasil.
20:28
No lugar de ponto-e-vírgula (";") ó,
20:29
vírgula (",")
20:30
vou abrir fechar parênteses
20:32
e vou colocar o dado da próxima pessoa
20:33
DEFAULT ... vou colocar com minúscula aqui, pra você ver
20:35
Sem problema ó.
20:36
Pedro
20:37
vírgula
20:38
1999, mês 12, dia 3
20:43
Também é do sexo masculino,
20:47
Pesa 87 kg.
20:49
Posso informar, tem inteiro aqui, não tem problema
20:53
2 metros, vou fazer tudo ... tudo redondo aqui.
20:57
O Pedro é é é é Brasil.
21:00
Ele é do Brasil? Então vou colocar aqui, DEFAULT.
21:02
Vírgula.
21:03
Abre parênteses.
21:05
Vamos colocar mais uma pessoa
21:07
Janaína. 1987, mês 11, dia 12.
21:13
É mulher, tem 75.4 kg
21:19
Tome Martelada!!!!
21:20
Tem 1.66m
21:23
Ih, é, sei lá, dos Estados Unidos (EUA)
21:25
TOC, TOC, TOC [MARTELADA]
21:26
Janaína é dos Estados Unidos
21:29
Terminou, ponto-e-vírgula.
21:31
Pode fazer isso quantas vezes você quiser
21:33
Vamos ... abrir aqui a tela,
21:36
do terminal, e executar o comando.
21:38
Executou sem problemas.
21:40
E vamos ver o SELECT * FROM pessoas
21:43
Deixa eu esconder aqui.
21:44
E tá lá. Olha os finais aqui.
21:46
Cláudio, Pedro e Janaína.
21:50
Tudo perfeito. Sem problema. Olha o Pedro que eu tinha colocado
21:53
UHH ... Aqui ó. 87 e 2. Números inteiros
21:58
A lá ó. 87. E 2. Sem problema nenhum. Tá vendo?
22:03
Tudo organizadinho, com duas casas decimais, porque eu defini no Banco de Dados que o peso tem
22:09
duas casas decimais.
22:10
Tá na dúvida? Olha lá o peso
22:13
Ele tem 5 casas ao todo ...
22:15
... e duas casas decimais. Assim como altura, tem 3 casas ao todo e 2 decimais
22:20
Todos os dados foram adicionados com sucesso
22:22
Tranquilo?!!
22:23
Gostou dessa aula?
22:24
Ainda tem mais uma coisinha, só pra você, antes de terminar.
22:27
Aprender mais uma novidade.
22:29
Lembra que falei, que os comandos CREATE BATABASE e CREATE TABLE
22:32
são comandos DDL, são comandos de definição,
22:34
então, como disse anteriormente.
22:36
DDL são comandos de definição. O que vale é a letra do meio.
22:41
O comando que nós vimos hoje,
22:42
é o comando INSERT INTO.
22:43
E o comando INSERT INTO,
22:45
ele não serviu pra definir a estrutura do Banco,
22:47
ele serviu pra inserir dados, ele serviu pra manipular dados.
22:52
E por conta dessa manipulação,
22:54
o comando INSERT INTO,
22:55
é o primeiro comando que você vai aprender, que é ...
22:57
... da classificação DML, esse M
23:00
é 'Data Manipulation Language'.
23:03
Então, os comandos de manipulação de dados
23:05
são considerados DML,
23:07
e os comandos de definição de dados
23:09
são considerados DDL.
23:11
Ficou claro?
23:12
Então esse foi o primeiro comando
23:13
DML, que estamos aprendendo.
23:15
Então, existem vários outros comandos DDL,
23:18
vários outros comandos DML.
23:20
Vamos ver isso aos poucos.
23:22
Porque essa aula, acabou de acabar.
23:24
Como sempre, no finalzinho.
23:25
Eu queria te pedir uma honra
23:27
Eu queria te pedir, pra que você se transforme, se você já não é.
23:31
Um "gafanhoto" inscrito.
23:32
Então ó. clicando aqui, você vai se inscrever no canal.
23:35
Gostou dessa aula? Dá um jóinha. Favorita. Mostra pros amigos.
23:40
Pô, olha só essa aula.
23:41
Olha a paciência que essa cara está tendo. Olha que coisa de Jó.
23:44
Olha essas marteladas malditas.
23:46
E nunca se esqueça, depois de se inscrever.
23:48
Clica na engrenagem e diz que você quer receber por e-mail.
23:52
Nós temos vários cursos. Tem curso em andamento.
23:55
Tem mais de um curso, você sabe que está tendo ...
23:57
... né, várias informações ai pra você.
23:59
Então não pode perder cara.
24:01
É o canal onde você vai aprender coisas.
24:04
E se você chegou aqui nessa aula só pra dar uma olhadinha.
24:07
Seja bem vindo.
24:07
Nunca se esqueça, aqui ... Dobrei o dedo dele.
24:11
Deixa dobrado.
24:12
Você vai ter acesso a todas as aulas de Banco de Dados que saíram até agora
24:15
Essa é a quinta aula?
24:16
Então, eu acho que você já presume ...
24:20
... que existem outras quatro (4).
24:21
Então, clicando aqui, você vai ter acesso a todas as playlists
24:23
Aqui em cima, na parte interativa, tem um "izinho" aqui?,
24:26
pode apertar. Aqui você vai ter a seleção de alguns cursos
24:29
Então, assim. Pra Banco de Dados,
24:31
não é importante que você tenha conhecimento prévio nenhum, nenhum.
24:34
Mas, é importante ... Coloquei aqui em cima.
24:36
Um curso de Algoritmo.
24:38
Um curso de PHP.
24:39
Por que? Mais tarde,
24:41
você vai conseguir unificar esses Banco de Dados que estamos criando
24:44
com seu código PHP.
24:46
Então, pequeno gafanhoto
24:47
Se seu foco não é Banco de Dados.
24:49
Estuda aqui ó.
24:50
Algoritmo e PHP
24:51
Porque isso vai ser de suma importância,
24:54
pra dentro do seu ... currículo ... de ... educação de TI
24:58
Mais uma vez, eu queria agradecer por todos os comentários.
25:00
Por todos os comentários positivos, por todas as críticas construtivas.
25:05
Né.
25:05
A galera que reclamou das marteladas.
25:07
Sinto muito.
25:08
Volto a dizer. Até param agora. Você prefere não ter curso?
25:11
Ou curso com martelada?
25:12
Eu decide
25:13
Dar curso até com martelada.
25:15
É isso ai pequeno gafanhoto.
25:16
Pratique sempre, estude
25:18
Faça seu Banco de Dados, instala seu ambiente, configura tudo bonitinho,
25:22
faça as inserções que você quiser.
25:24
Crie tabelas extras, você pode criar mais de uma tabela.
25:27
Faça testes.
25:28
Eu vou ensinar mais pra frente como apaga tabela, modifica e tudo mais.
25:31
Então, vai passo-a-passo, vai que você está no caminho certo.
25:35
Um forte abraço!
25:36
E até a próxima aula.
"""

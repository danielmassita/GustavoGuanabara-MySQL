# Curso MySQL #04 - Melhorando a Estrutura do Banco de Dados 

# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/melhorando-a-estrutura-do-banco-de-dados/ 
# https://youtu.be/cHLKtALWDos

"""
Aula 04 - Curso MySQL #04 - Melhorando a Estrutura do Banco de Dados 

Hello, world! Vamos melhorar a estrutura do banco de dados. Basicamente, vamos refazer de uma maneira melhor (comandos de alter-table). 
E lembra do bug? Múltiplos cadastros do seu Valdemir? Vamos corrigir!

  Godofredo
  32 anos
  Masc
  78.5 kg
  1.83 m
  Brasil
  
  Dolores
  30 anos
  Fem
  52.3 kg
  1.65 m
  México
  
  Godolores
  3 anos
  Fem
  25.8 kg
  0.89 m
  EUA

Na aula passada, usamos os seguintes comandos:

MySQL Workbench

      SHOW databases;
      CREATE DATABASE cadastro;
      USE cadastro; 
      CREATE TABLE pessoas (
        nome VarChar(30),
        idade TinyInt(3),
        sexo Char(1),
        peso Float,
        altura Float,
        nacionalidade VarChar(20)
      ); 
      DESCRIBE pessoas; 
"""

# Vamos começar deletando o último BD chamado cadastro.
DROP DATABASE cadastro;

# Vamos criar um novo DB com dois PARÂMETROS (Constraints)
CREATE DATABASE cadastro
DEFAULT CHARACTER SET utf8
DEFAULT COLLATE utf8_general_ci;

# Vamos agora atualizar a ESTRUTURA da tabela, com campos mais inteligentes e tipos primitivos bem dimensionados... Mas já vamos OTIMIZAR a estrutura das tabelas.
# Se um INT usa 11 bytes e TinyInt usa 3 bytes. Mas se falarmos de milhões de dados... ;)
# Por exemplo, ao cadastrar a idade vamos usar o dia que nasceu, assim a tabela será dinâmica e atualizada sempre.

CREATE TABLE pessoas (
    `id` int NOT NULL AUTO_INCREMENT,
    `nome` varchar(30) NOT NULL ,
    `nascimento` date,
    `sexo` enum('M', 'F'),
    `peso` decimal(5,2),
    `altura` decimal(3,2),
    `nacionalidade` varchar(20) DEFAULT 'Brasil', 
    primary key (id)
) default charset = utf8;

DESCRIBE pessoas;

# Usamos duas constraints (not null e default).
# Sempre importante ter um campo tipo CHAVE PRIMÁRIA (únicas).

"""
Transcrição


0:00
♫ Cantarolando a música do 007 ♫
0:08
Anh?
0:09
Unh?
0:10
♫ Música ♫
0:20
Olá pequeno "gafanhoto" ! Sejam Bem vindos
0:22
a mais uma aula do seu curso de Banco de Dados com MySQL
0:25
O meu nome e Gustavo Guanabara e eu sou seu Professor
0:27
E chegamos a quarta aula do curso de Banco de Dados.
0:30
Onde nós vamos fazer oque a gente tinha prometido antes
0:33
Nós vamos melhorar a estrutura do Banco de Dados que nós já criamos na aula anterior
0:38
Bem, basicamente nós não iremos "melhorar", nós vamos refazer de uma maneira melhor.
0:42
Porque existe alguns comandos que veremos nas próximas aulas,
0:44
que são os comandos de Alter Table, comandos para alterar a estrutura de uma tabela já criada.
0:49
Como a gente não cadastrou ninguém e queremos melhorar, e como nós estamos nos primeiros
0:54
passos e tudo mais. Da para gente apagar a tabela... Apagar o banco... E criar ele de novo.
0:59
E de quebra nós vamos resolver um problema que era o cadastro do Sr.Vladimir!
1:03
Lembra que eu falei que dava para cadastrar vários Srs.Vladirmir
1:05
Então a gente vai resolver esse problema com uma maneira muito simples que são
1:08
as Chaves Primárias.
1:10
Então é isso gafanhoto! Se prepara ai! Abre seu ambiente... tudo bonitinho
1:14
Porque agente vai começar, e você tem que praticar!
1:16
♪ Transição ♪
1:18
Se você se lembra da aula passada, eu apresentei o meu amigo Godofredo, lembra ? de 32 anos de idade,
1:23
sexo masculino, 78kg... Ele tinha algumas características como nome, idade, sexo, peso, altura
1:30
e nacionalidade. Essas características eram compartilhadas
1:32
pela sua esposa Dolores, e pela sua pequena filhinha Godolores,
1:37
e que tinham todos eles as mesmas características.
1:39
E ai você deve se lembrar que colocamos todos eles dentro de um contêiner,
1:41
colocamos o contêiner em um navio
1:43
e ai começamos a estudar banco de dados a partir dessa teoria maluca,
1:47
que eu criei na minha cabeça insana e doentia.
1:49
Na aula passada você aprendeu os comandos
1:52
CREATE DATABASE e CREATE TABLE
1:54
Só que de uma maneira bem simples.
1:55
A gente utilizou os comandos bem simplesinhos,
1:58
Os comandos CREATE DATABASE sem parâmetros nenhum e o comando
2:02
CREATE TABLE com o minimo de parâmetros possiveis
2:04
Então a gente ainda está evoluindo no estudo de Banco de Dados
2:06
Então
2:07
Vai devagarinho, com calma que a gente vai criar banco de dados melhores ainda.
2:12
Com mais que uma tabela, relação entre tabelas.
2:14
Calma! que esse curso vai chegar a esse ponto.
2:16
Você só precisa ter paciência!
2:18
Vamos começar melhorando o CREATE DATABASE, por exemplo
2:20
E como você já sabe o comando CREATE DATABASE ele cria um banco de dados...
2:24
...Mais da para criar um banco de dados melhor do que isso daqui...
2:27
Por que o banco de dados, contem dados, ele contem palavras, nomes, números
2:32
Da para eu especificar que formatos esses dados vão ter diretamente do comando CREATE DATABASE
2:37
Se você se lembra muito bem, quando a gente começou a estudar HTML
2:40
Se você não fez o curso de HTML, aqui ó, playlist toda organizadinha
2:44
Da para fazer um curso de HTML show de bola, e ai você vai juntar algoritmos com PHP,
2:49
Com HTML e com tudo mais e vai virar um gafanhoto programador.
2:53
Tem muita gente que agradece a gente, tem muita gente que já esta conseguindo emprego
2:56
conseguindo emprego por conta dos nossos cursos, é eu fico muito feliz, muito orgulhoso por conta do
3:00
tamanho que esse projeto ganhou.
3:01
então se você se lembra do curso de HTML
3:03
a gente teve um problema de formatação de caracteres acentuados
3:07
porque a gente trabalha com a língua portuguesa, e a língua portuguesa contém acentuações
3:12
e essa acentuação não é padrão americano por exemplo
3:17
palavras em inglês não possuem acento
3:19
palavras em português sim
3:20
e eu apresentei para vocês o formato UTF-8
3:22
O formato UTF-8 tem caracteres especiais, inclusive as acentuações que agente trabalha
3:28
E não existe somente a nossa acentuação, existem outros tipos de acentuações em outros idiomas.
3:33
O UTF-8 está preparado para os nossos caracteres, caracteres com acentuação latina
3:38
Então, antes da gente criar o banco de dados aqui, a gente vai apagar o Banco de dados anterior
3:43
Pra fazer isso, abra seu ambiente, abra seu WampServer, abra seu MySQL Workbench
3:48
E vamos trabalhar.
3:49
Então, eu já estou aqui dentro do meu ambiente do Workbench...
3:52
e já estou com o meu servidor do MySQL devidamente aberto...
3:55
e ativo.
3:56
aqui no meu WampServer, já que o ícone está verdinho.
3:59
Se você não sabe como fazer tudo isso funcionar
4:01
é por que você é um gafanhoto teimoso e pulou as primeiras aulas.
4:05
Nas primeiras aulas, eu mostro como você prepara o ambiente...
4:08
como você abre aos arquivos, como você abre o Workbench...
4:11
e faz ele funcionar.
4:12
Não pule passos.
4:14
Temos aqui o banco de dados cadastro, que agente criou na aula passada.
4:18
Então, eu não vou querer mais este banco de dados "Cadastro".
4:21
Pra apagar o banco de dados "Cadastro", eu vou vir aqui oh!
4:24
Clicar sobre o botão, pra criar uma nova de tabela de SQL File
4:29
E vou dar o comando DROP, que é largar, abandonar
4:33
DATABASE cadastro
4:37
Pra executar, basta clicar sobre este botão, ou, pressionar Ctrl + Enter.
4:42
A partir de agora o banco de dados "cadastro", não existe mais.
4:46
Viu como é simples?
4:47
Então, o comando CREATE DATABASE cria...
4:49
o DROP DATABASE apaga.
4:51
Vou apagar esta linha aqui, pois eu não preciso mais dela.
4:53
Então, eu não tenho mais um banco de dados, vamos recriar o banco.
4:57
Só que nós vamos recriar modificando um pouco esta linha.
4:59
Então, o comando da aula anterior foi, CREATE DATABASE cadastro
5:02
" ; "
5:03
Lembrando que ";" indica o final de comando em MySQL, eu posso colocar
5:06
CREATE...
5:07
DATABASE...
5:07
cadastro
5:08
;
5:09
Então, são três linhas... mas é um comando só.
5:11
O que indica o final do comando é o " ; ".
5:14
Então, eu vou tirar o " ; "... por que eu vou acrescentar coisas
5:17
e vou colocar dois parâmetros
5:19
esses parâmetros em MySQL se chamam CONSTRAINTS
5:22
Então, eu vou colocar duas CONSTRAINTS
5:24
A primeira vai ser DEFAULT CHARACTER SET, que eu vou colocar UTF-8.
5:28
Então, vamos colocar lá no seu ambiente.
5:31
CREATE
5:32
DATABASE
5:34
cadastro
5:35
com...
5:36
DEFAULT
5:37
SET
5:38
utf-8
5:39
Esse utf-8 aqui tem que ser em minusculas tá?
5:42
Então, o resto você pode escolher maiúsculas ou minusculas.
5:44
Aqui, em minusculas.
5:45
Os nomes, todos em letras minusculas.
5:47
E além disso vou configurar um negócio chamado COLLECTION
5:49
O COLLECTION, também serve para a definição dos caracteres
5:53
Então eu vou colocar lá DEFAULT COLLATE utf8_general_ci;
5:57
E aí eu posso colocar " ; " que meu comando está terminado
6:01
Então, vamos lá digitar
6:03
default collate utf8_general_ci;
6:13
ficou claro!
6:15
agora eu já estou aprimorando ainda mais a estrutura do meu banco de dados.
6:19
eu vou
6:19
criar um banco de dados
6:20
e ele ja irá ter uma codificação de caracteres por padrão e um Collation por padrão
6:26
todos eles voltados para o Utf8, que como eu já expliquei são caracteres acentuados no padrão que a gente vai trabalhar
6:32
para executar esse comando, Ctrl+Enter ou click sobre o botão para a execução do comando
6:38
Ctrl Enter, deixa eu abrir antes de precionar Ctrl Enter, deixa eu abrir aqui ah, ah lista
6:44
Ctrl Enter,
6:46
Ò, a ultima linha indica que o banco de dados foi criado com sucesso
6:50
Vamos atualizar o esquema e aqui eu tenho o cadastro
6:55
Tá, mas e qual é a diferença ?
6:57
Vamos fazer o seguinte,
6:59
Eu vou criar um banco de dados chamado teste aqui
7:01
Sem definir Collation
7:02
Vamos aqui em baixo, vou dar
7:05
create databese meubanco;
7:09
Sem espaço, não pode ter espaço
7:11
Ctrl Enter
7:12
para executar
7:12
Vamos atualizar os esquemas, eu tenho meu banco aqui
7:15
Qual é a diferença?
7:17
Vou clicar aqui no Information do meu cadastro e vou clicar aqui no information do meu banco
7:25
Na informação do cadastro
7:27
Percebe aqui ó o Default collation é utf8 , como eu mandei o characterset é utf8
7:33
E o meu banco aqui, para o meu ambiente ele criou como " latin1 swedish " da Suécia, Suiça, sla como é
7:41
o negócio
7:42
E, o Default characterset por padrão está latin1
7:45
Isso foi para o meu ambiente no seu pode ser até de diferente, então
7:48
Esse create database é um pouquinho maior concordo com você
7:51
mas ele tem a configuração especial para caracteres que a gente vai precisar mais para frente
7:57
Então meu querido
7:58
não tenha preguiça, aprende o comando da maneira correta
8:01
vou fechar aqui, fechar aqui
8:04
vou apagar o meu banco aqui por que eu não quero ele
8:08
então drop datebase meubanco
8:12
ponto e virgula
8:14
Ctrl Enter
8:15
Já apaguei o banco de dados meubanco que estava lá
8:18
Esse é o meu comando , create database
8:20
com atualizações
8:22
vamos agora atualizar também a estrutura da minha tabela pensando em campos mais inteligentes
8:29
Em tipos primitivos mais bem dimensionados, e muito mais.
8:33
Se você se lembra bem o seu comando create table da aula passada foi exatamente esse daqui
8:38
Então eu tinha o campos
8:39
Nome
8:40
Idade
8:41
Sexo
8:41
Peso
8:42
Altura
8:43
e nacionalidade
8:43
E eles estavão dimencionados utilizando principios muito simples, muito simploros como por exemplo
8:47
Utilizar somente char, varchar, int e float.
8:51
E é importante que já de cara você consiga otimizar as estruturas das suas tabelas
8:55
Quando você aprendeu provavelmente na sua escola ou na sua faculdade
8:59
Se o seu professor não teve tanta paciência para te explicar ele mandou você utilizar
9:02
Int
9:02
Eu já coloquei aqui tinyint, eu já otimizei um pouquinho mais eu estou economizando espaço
9:07
Pensa comigo aqui
9:08
se um
9:09
int ocupa 11 bytes
9:10
E um tinyint ocupa 3 bytes
9:12
A mais ah diferença é pequena
9:14
mas para cada um registro
9:16
Se eu tenho 1 milhão de pessoas cadastradas a economia de espaço em disco vai ser muito maior
9:20
Então
9:21
Pensa nisso, a coisa em vez de usar o char
9:24
usar o varchar
9:25
Então, é esse tipo de coisa que você tem que pensar quando você for criar um banco de dados
9:30
Vamos dar uma otimizada, vamos dar uma melhorada nesses campos aqui dando uma relembrada nos tipos primitivos que a gente
9:35
viu na aula passada
9:36
Então se você se lembra a gente tinha esses tipos primitivos.
9:39
O que basicamente eu vou fazer é o seguinte:
9:41
A primeira coisa
9:42
é trabalhar com os números reais.
9:44
Isso porque eu utilizei um tipo float, um tipo muito genérico
9:48
que já coloca lá o valor no formato que ele decidir no banco de dados.
9:52
Nós vamos partir para o tipo decimal, que é um tipo mais personalizável, que vou ensinar como funciona.
9:57
Além disso a gente vai trabalhar com tipos de data e tempo.
10:01
Se você se lembra, na aula passada eu falei que cadastro de idade não é uma coisa legal.
10:05
Então a gente vai cadastrar o dia em que a pessoa nasceu.
10:08
Em vez de cadastrar a idade dela.
10:10
Isso porque se eu cadastrar a idade, por exemplo
10:12
Hoje, eu tenho 37 anos, mas, daqui dois meses, eu vou ter 38
10:17
Eu vou ter que entrar no banco de dados
10:18
e ficar atualizando minha idade?
10:20
se eu cadastro o dia que eu nasci
10:22
Na hora em que eu for trabalhar com os dados
10:25
Ele já vai saber calcular minha idade, de acordo com o dia que eu nasci
10:27
Muito mais inteligente
10:29
Então, como pedi na aula passada pra você ter paciência
10:32
Agora a gente já está resolvendo esse problema.
10:33
A gente não vai mais cadastrar a idade da pessoa
10:35
A gente vai cadastrar o dia do nascimento dela.
10:37
Outra coisa que a gente vai trabalhar é em relação ao sexo
10:41
A gente vai trabalhar com uma coleção
10:43
Não simplesmente com um caracter simples
10:45
Então vamos colocar a mão na massa
10:47
E vamos entender o que a gente planejou aqui
10:49
para essa nova estrutura.
10:50
Dessa tabela bem simples, ainda continua simples
10:53
Mas agora, ela vai ficar mais aprimorada.
10:55
Então a primeira coisa que a gente vai fazer é remover
10:57
os tipos primitivos, e modificar a idade para nascimento.
11:01
Agora, nós vamos colocar os tipos primitivos
11:03
para cada um dos campos que a gente definir aqui
11:06
Antes de mais nada, nós vamos colocar também
11:08
A configuração de caracteres padrão na criação da tabela.
11:13
para isso vamos colocar lá no final, no fechamento do parêntese
11:16
Default charset = utf8
11:19
é importante também na hora de criar a tabela, você pode definir
11:23
O conjunto de caracteres padrão que vão ser suportados.
11:26
Vamos então definir o nome, como varchar de 30
11:29
continua o mesmo tipo primitivo, mas, eu vou adicionar
11:32
mais umas constraints, lembrando constraints são regras
11:36
Que a gente vai definir para a criação de coisas dentro do meu banco de dados.
11:39
A primeira constraint que a gente vai ver, é o not null
11:42
é not "espaço" null, not null significa que você vai ter que preencher os dados
11:47
Por padrão, se eu quiser cadastrar uma pessoa e não quiser informar por exemplo
11:51
a data de nascimento dela, sem problema, por padrão.
11:54
Mas se você quiser obrigar, por exemplo que toda pessoa tenha nome
11:57
não tem como eu cadastrar uma pessoa, se ela não tiver um nome
12:00
então nesses campos que são obrigatoriamente digitáveis
12:03
Eu vou colocar a constraint not null, ficou claro?!
12:07
o nascimento eu vou colocar como date
12:09
o sexo em vez de char um, eu vou utilizar um tipo de coleção
12:14
que é o "enum"
12:16
então eu vou colocar lá, enum, 'M','F'.
12:18
Quando eu uso o set ou enum, colocando entre parenteses, entre aspas os valores
12:21
valores, separados por vírgula, eu estou dizendo
12:24
quais são os valores que serão aceitos
12:26
então para sexo, ele so vai aceitar 'M' ou 'F'
12:30
isso vai permitir que você defina a estrutura de forma um pouco mais rígida
12:35
Para que o cara não coloque, sei lá, a letra "A", sexo "A"
12:39
com char um, eu posso colocar "A", agora com enum, eu so posso colocar 'M' ou 'F'
12:43
o peso que era float. agora eu vou colocar como decimal
12:47
e vou colocar 5,2 entre parenteses separados por vírgula
12:50
e o que significa esse 5,2 ? calma, eu te explico!
12:54
5,2 é o seguinte, imagina que sejam 5 casas ao todo
12:58
então esse primeiro valor 5, e o total de casas
13:02
O segundo número é a quantidade de números que vão ficar após a vírgula.
13:06
Então desses 5, 2 vão ficar após a vírgula, e três antes da vírgula.
13:12
A partir de agora eu posso colocar qualquer peso
13:14
Por exemplo 102,35 KG
13:17
Deu pra entender?
13:18
Então você pode colocar qualquer par de valores
13:20
contanto que o primeiro seja maior
13:21
E isso vai indicar o número total de dígitos
13:24
E depois, a quantidade de dígitos depois da vírgula.
13:26
Com isso, você economiza espaço
13:28
E configura qual a precisão exata que o número vai precisar ter
13:31
A altura eu também vou colocar utilizando o tipo decimal
13:35
Vou colcoar decimal, 3,2
13:37
Só dando uma revisada, são três dígitos ao todo
13:41
dois depois da vírgula, então só posso ter 1 dígito vírgula 2 dígitos
13:46
isso porque ninguém tem 10 metros de altura, no máximo é dois metros de altura
13:51
3 metros de altura no máximo
13:52
então, e um dígito vírgula dois dígitos
13:55
Com isso eu economizo a quantidade de bytes
13:57
que eu estou utilizando para armazenar esses dados
13:59
e o dado vai ficar mais preciso.
14:02
A nacionalidade vou manter o varchar de 20
14:06
só que eu também vou colocar uma constraint, a constraint default
14:10
então default 'Brasil'
14:11
Isso significa o seguinte na nacionalidade
14:14
Se ninguém digitar nada, por padrão será Brasil
14:17
viu?! então eu posso utilizar algumas constraints
14:20
A gente já viu aqui algumas, como not null e o default
14:23
Mais para frente nós vamos ver mais algumas constraints
14:25
fica calma meu pequeno gafanhoto você ainda tem muito que aprender
14:28
por hora, vamos digitar exatamente esse comando lá no MySql Workbench.
14:34
então vamos lá, create table o nome da minha tabela será "pessoas"
14:39
abre e fecha parenteses, utilizando default, charset = utf8
14:49
lembrando, utf8 tudo em minusculas
14:52
vamos colocar os campos aqui, nome, nascimento,sexo, peso, altura e nacionalidade
15:02
vou colocar virgula no final para eu nao esquecer
15:05
muito importante que você faça isso, passo a passo
15:08
Não fica tentando digitar tudo uma vez só
15:11
nacionalidade não tem virgula porque é o último
15:14
é muito importante que você não tente ficar decorando comando inteiro
15:16
Vai fazendo aos poucos, faz como eu estou fazendo aqui
15:20
por isso eu estou digitando de novo
15:22
Vamos colocar agora os tipos primitivos
15:24
o nome, varchar de (30) not null, é uma constraint por isso fica em azul
15:31
nascimento e do tipo date, sexo enum M ou F
15:39
lembrando que esse M ou F tem que ser colocados em maiusculo, e entre aspas simples ta?!
15:47
então quando o usuário digitar, ele vai aceitar M ou F
15:49
Se quiser que aceita 'M', 'F' em minusculo também você coloca M F minusculo
15:53
Não recomendo, deixa tudo assim.
15:56
O peso vai ser decimal 5,2, e a altura decimal , 3,2
16:03
a nacionalidade eu vou colocar varchar de 20, default, mais uma constraint, é 'Brasil'
16:14
Definimos aqui
16:15
Importante dizer um negócio que eu não falei na aula passada
16:18
também porque manter informações mais precisas
16:21
Pode acontece em algum tutorial, ou material, inclusive na exportação do seu banco de dados
16:26
Que os nomes dos campos estejam colocados entre crase
16:30
Assim ó
16:31
eu posso informar aqui pessoas entre crases, nome também entre crases
16:37
e assim para cada um deles
16:39
isso permite que eu utilize por exemplo, campos com acentos
16:43
campos com espaços, apesar disso não ser recomendado
16:47
então você pode ver isso aqui em alguns tutoriais
16:52
ou algum material específico
16:54
você pode ver esse tipo de sitaxe aqui
16:56
Está completamento correto sem problema nenhum
16:58
eu é que não vou ficar digitando todas as vezes a mesma coisa
17:01
E não confunda aspas simples, com crase, com acento agudo
17:05
você tem que utilizar certinho
17:06
todo caracter em SQL entre aspas simples, e toda palavra de definição entre crases
17:11
vamos executar isso aqui
17:12
CTRL+ENTER
17:13
ele deu um erro dizendo que o banco de dados não foi selecionado
17:16
você pode usar o USE, ou você clica duas vezes ó, ele já abriu o banco de dados cadastro
17:21
e antes de pressionar CTRL+ENTER, ainda não acabou o comando não
17:23
vamos adicionar mais algumas coisinhas
17:25
Lembra de um problema que a gente viu na aula passada
17:27
lembra que com aquele comando a gente poderia cadastrar todas essas pessoas ai
17:30
Inclusive o seu vladimir, que tem 65 anos e veio da Rússia
17:34
E que eu falei que era possível com essa estrutura
17:37
que a gente criou, cadastrar não só dois, mas vários seus vladimir
17:41
e qualquer outra pessoa
17:43
Sim, num banco de dados eu posso ter duas pessoas
17:45
chamadas vladimir, né?! ou maria da silva
17:48
São pessoas, existem homônimos, pessoas que tem o mesmo nome
17:52
E numa tabela é importante que você defina
17:54
pelo menos um dos campos, como um campo que chamamos de chave primaria
17:58
Um campo chave primária, ele não se repete
18:01
Então por exemplo, quando você, sei lá, você tem sua academia
18:05
Então você tem sua matricula na academia
18:07
você está estudando na faculdade, você tem sua matricula na faculdade
18:11
Seu cadastro de pessoa fisica (CPF)
18:14
Você não tem seu nome como sua chave primaria
18:16
você tem seu CPF
18:18
Não existem duas pessoas com o mesmo CPF no mundo
18:19
Não existem dois alunos na faculdade com a mesma matricula
18:23
Não existem dois alunos na cademia com a mesma matricula
18:27
então a matricula ou o seu CPF são campos, chaves primarias
18:32
São campos em que as pessoas não vão ter o mesmo valor
18:36
Não vão existir duas tuplas, falando um poquinho mais técnico
18:40
Não vão existir dois registros com o mesmo valor para chave primaria
18:45
Vamos aprender então como resolver isso
18:48
Basicamente nós vamos pegas esse comando que acabamos de digitar
18:51
e vamos adicionar duas linhas
18:54
umas no início e uma no final
18:55
Eu vou dar uma clareada aqui pra gente poder focar so nas linhas novas
18:59
basiamento o que eu vou fazer e criar um campo novo
19:02
Já que nome não pode ser chave primaria
19:04
como já disse, existem pessoas com o mesmo nome
19:07
como você pode imaginar, podem existir várias pessoas com a mesma nacionalidade
19:10
com o mesmo sexo, exatamente com a mesma idade
19:13
com a mesma data de nascimento, altura, mesmo peso
19:16
Então nenhum desses campos que estão aqui, podem ser chaves primárias
19:20
Então eu vou criar um identificador para uma pessoa
19:22
esse identificador vai ser numérico
19:23
eu vou colocar lá, ID vai ser o meu campo, e vai ser inteiro
19:29
e eu vou colocar duas constraint
19:30
ele vai ser not null, isso porque você não pode ser aluno
19:34
se você não tiver uma matricula
19:36
Então ele vai obrigar você a digitar
19:37
a gente já viu essa constraint
19:39
e tem uma outra constraint que eu acho legal
19:40
Nem sempre você vai utilizar, mas , nesse caso a gente vai
19:43
que é a constraint auto_increment
19:45
A constraint auto_increment funciona da seguinte maneira
19:47
A primeira pessoa que eu cadastrar, vai ser código 1
19:50
A segunda código 2, a terceira código 3
19:53
tudo isso automaticamente
19:55
para definir o ID como chave primária
19:57
Eu vou lá na última linha, depois de nacionalidade, e vou colocar PRIMARY KEY
20:02
e entre parenteses vou colocar ID
20:05
Que é o nome do campo que eu criei lá
20:07
como chave primaria, beleza?
20:09
vamos colocar a mão na massa para ver como funciona isso
20:11
no meu comando aqui ó, vou adicionar ID como int
20:16
e vai ser not null
20:18
isso é, não vai aceitar valores nulos
20:22
e ele vai ser auto_increment
20:25
As constraints são separadas por "espaço" não por vírgulas
20:29
Not null é com espaço entre eles
20:31
auto_increment e com underline
20:34
botei a virgula no final, e depois de nacionalidade
20:37
eu vou colocar uma virgula, pois eu terei mais coisa, ali deu erro, mas vou digitar aqui em baixo
20:41
Primary key, ó, ele já me sugere aqui primary key e entre parenteses vou colocar ID, nao tem virgula
20:51
porque não tenho mais comando lá no final
20:53
Então esse é o comando
20:55
beleza? esses são os nossos comandos de hoje!
20:57
Da uma comparada ai no que fizemos anteriormente
21:00
com o que fizemos agora, agora está bem melhor
21:02
para executar esse comando, você percebe aqui ó
21:05
que a tabela está vazia
21:06
para você abrir o banco de dados cadastro, basta você dar o comando use cadastro
21:11
ou clicar duas vezes, ó, cliquei duas vezes, abriu bando de dados test
21:13
cliquei duas vezes abriu bando de dados cadastro
21:16
abra o banco de dados cadastro
21:18
para o cursor em qualquer lugar do comando, pressionr CTRL+ENTER para executar o comando
21:24
e vamos atualizar o esquema para ver se a tabela foi criada
21:26
agora eu tenho a tabela pessoas
21:27
♫Música♫
21:28
clicando sob o icone de informação, agora eu tenho a tabela pessoas
21:33
com as colunas bonitinhas tudo organizado
21:35
a minha chave primaria, ó, meu indice eu tenho um indice primario
21:40
que é a coluna ID, agora eu tenho uma chave
21:43
♫Música♫
21:44
interrompemos a sua aula de banco de dados
21:46
para um pronunciamento muito importante, na verdade dois avisos
21:49
o primeiro, você deve estar percebendo umas coisas novas por aqui
21:53
Pois saiba que nós temos um video mostrando como tudo aconteceu
21:57
e o que aconteceu e o que está mudando no curso em video
22:00
Tem algumas coisas novas, você deve estar percebendo
22:03
esse video está meio atemporal
22:05
e o segundo aviso e o seguinte, você está gostando da aula de banco de dados?
22:08
gostou de criar um bando de dados novo?
22:11
todo bonitinho, organizado com conhecimento de chaves primarias
22:16
e tudo mais?
22:16
Pois saiba que a host net, que e a patrocinadora
22:18
eterna do curso em video
22:20
a empresa que mais apoia o curso em video
22:22
gente vocês não tem noção do apoio que essa empresa
22:26
que mora no nosso coração, mora aqui ó, ta aqui ó
22:28
essa empresa ajuda o curso em video desde o inicio da história
22:32
vocês tem muito que agradecer essa galera
22:34
Mas, o que eu vim mostrar pra vocês é o seguinte
22:36
como é que você cria um banco de dados, na internet
22:39
é claro que eu só vou começar, é só o "iniciozinho"
22:41
a gente vai ter mais aparições ai durante as aulas
22:44
Mas oque eu queria dizer é: Graças a Host net esse CURSO DE BANCO DE DADOS está indo até você
22:48
E ela tem uma solução de MySQL online Profissional
22:52
E eu vou te mostrar como:
22:53
Então pra você que já é assinante da HostNet basta entrar no painel de controle da empresa
22:58
Pra isso acesse @ www.hostnet.com.br @
23:00
Painel de controle
23:02
Você vai ser desviado pra esse site
23:04
Onde você vai botar seu 'login' e 'senha'
23:06
Clicar em entrar
23:08
E caso você não seja assinante,
23:10
Na página principal você tem a parte do 'assine'
23:12
Lá você vai poder botar seu site no ar (pago) com Banco de Dados MySQL
23:16
Você vai poder unir tudo que nós estamos aprendendo com a parte prática, a parte dos servidores.
23:22
Na página inicial do seu painel de controle
23:24
Você vai selecionar o domínio que você vai trabalhar aqui ó: (mostrou no vídeo)
23:26
O meu exemplo é @ criar-meu-site.com @
23:28
é um domínio que eu tenho aqui...
23:29
Vou clicar em Banco de Dados
23:32
Banco MySQL
23:34
Por padrão ele já vem com um banco criado
23:37
Mas você pode criar vários ATÉ 5 de forma gratuita
23:41
Então você pode vir aqui "Novo Banco"
23:43
E ele vai criar o banco de dados ó:
23:48
Vou colocar uma senha
23:50
Repete a senha:
23:51
E vamos clicar em adicionar
23:54
Imediatamente eu posso acessar este banco de dados diretamente do meu endereço de servidor
23:58
Vamos clicar nesse endereço
24:01
E você vai ser desviado aqui pro 'PHPMyAdmin'
24:04
Que é um administrador de banco de dados
24:06
Ele é semelhante ao WorkBench que você está utilizando
24:08
E mais pra frente no curso eu vou te ensinar a utilizar o 'PHPMyAdmin'
24:12
Eu só vou mostrar aqui que o banco de dados já está criado
24:14
Você não precisa nem dar o "CREATE DATABASE"
24:16
Apenas o "CREATE TABLE"
24:17
Então se você olhar aqui no canto ó:
24:19
Você já tem o seu Banco de dados 'criar-meu-site'
24:21
E eu tenho a possibilidade de criar uma tabela aqui:
24:25
E criar uma tabela é bem simples você acabou de aprender o comando.
24:29
"Mas Guanabara, aonde eu coloco esse comando?"
24:31
Moleza "Pequeno Gafanhoto"
24:33
Basta clicar em SQL
24:36
E aqui você digita o comando que você quiser por exemplo:
24:39
CREATE TABLE
24:41
Ó ele tá até te ajudando
24:42
O nome da minha tabela vai ser: Teste
24:44
Abre e fecha parênteses
24:45
Vou colocar lá
24:46
ID
24:48
é inteiro
24:49
AUTO INCREMENT
24:50
Vai ter também nome VARCHAR
24:53
De 20 por exemplo
24:55
NOT NULL
24:57
botar "," aqui
24:58
"," aqui
25:00
Também posso usar a chave primária
25:02
PRIMARY KEY
25:05
id
25:06
Vamos executar.
25:07
Clique aqui em GO
25:09
E pronto! seu banco de dados está criado
25:11
E você pode fazer experiências
25:13
Testar os comandos que nós estamos utilizando durante as aulas
25:16
Dentro do seu servidor
25:17
Então, se você está criando um projeto com MySQL e MariaDB
25:23
A HostNet é a opção correta
25:24
Voltamos com a nossa programação normal
25:26
Continua com a aula aí "gafanhoto"
25:28
♫Música♫
25:29
Espero que tenha ficado claro oque é uma chave primária
25:31
E qual a funcionalidade dela
25:33
é de suma importância
25:35
O uso de uma chave primária
25:36
Se você não quer repetições de tuplas
25:38
Dentro de uma mesma tabela
25:40
No próximo vídeo nós vamos saber como incluir dados
25:44
Dentro dessa tabela
25:46
utilizando o comando INSERT IN TO
25:48
Não perca nenhuma aula de banco de dados
25:49
Ou qualquer outra aula que nós lançarmos
25:52
Clicando aqui ó em "se inscrever"
25:54
e VOCÊ pode clicar na engrenagem e habilitar a opção de receber atualizações por e-mail
26:01
Esse canal me ensina coisas muito importantes!
26:05
você só vai ganhar com isso. Quando assina o canal e recebe informações sobre novas aulas!
26:13
Clicando aqui em +Aulas, vocês será redirecionado para playlists, onde você verá todas as aulas do curso
26:20
de banco de dados, tudo organizado. E nunca se esqueça de ver as outras playlists
26:25
pois estão todas organizadas, você nunca viu um canal tão organizado!
26:30
E aqui no meio você terá a experiência completa, www.cursoemvideo.com
26:33
Aqui, você vai encontrar as informações sobre tudo aquilo que for lançado e tudo aquilo que for baixável
26:40
no curso de banco de dados. Então se inscreva e assista as aulas!
26:44
É isso aí pequeno gafanhoto, na próxima semana teremos mais uma aula, mais uma experiência
26:49
mais um comando do nosso curso de para você aprender a dominar o MySQL
26:56
que é essa poderosa solução de banco de dados que todo mundo deveria saber usar!
26:59
Um forte abraço, estude bastante e até a próxima!
27:03
♫Vinheta final♫
"""









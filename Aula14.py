# Curso MySQL #14 - Modelo Relacional
# https://youtu.be/8fxKJWJcRTw
# 

""" 
RELACIONAMENTO ENTRE TABELAS ou MODELO RELACIONAL
- Na década de 60, o Gov. EUA e IBM fizeram um evento CODASIL onde nasceu o COBOL.
- Na época, surgiram os modelos hierárquicos e em rede, mas aos longo dos anos ficou ineficiente.
- Na década de 70, Edgar F. Cood (Eng. IBM) pensou um modelo diferenciado, DADOS (muito mais que apenas ligações), eles teriam relações entre eles.
- Surgiu assim o Modelo Relacional.

- Foi criado relaçõess, sendo várias ligações (não apenas uma), e com significado entre as relações.
- Hoje em dia, um cadastro de uma pessoa, eu tenho um registro + etc., etc., etc.
- A partir dessa 'pessoa', podemos saber onde ela mora, produtos comprados, baixa de estoque, sistema financeiro, pedido de reposição, informação entrega, etc.

- Novos modelos surigram, como o MODELO ORIENTADO A OBJETO, mas o MODELO RELACIONAL ainda é muito usado e presente.
- Vamos voltar no nosso exemplo...

- No exemplo dos 'gafanhotos', temos um grupo de pessoas dentro de um contâiner chamado 'gafanhotos'. 
- Esse contâiner possui informações necessárias pra identificar cada um deles (id, nome, profissao, nascimento, sexo, peso, altura, nacionalidade).
- Vamos alterar os nomes:

ENTIDADE (contâiner onde vamos colocar DADOS sobre algo) será o antigo-contâiner, e vamos atribuir o valor de 'gafanhotos'
O contâiner de gafanhotos possui vários alunos... Nesse contâiner, tem vários dados sobre os alunos, os gafanhotos do Curso em Vídeo. 
Os DADOS dos alunos serão os ATRIBUTOS.

>>> Então, toda ENTIDADE possui uma coleção de ATRIBUTOS (ex-dados) definidos. Esses atributos vão compôr os dados que compõe cada um dos elementos que estão dentro dessa ENTIDADE. 

Entidade: Gafanhoto e Curso

Entidade Gafanhotos

(Atributos/Dados que são tuplas, registros identificados e armazenados dos elementos/coisas/dados da entidade, ou seja, os 'alunos-gafanhotos')
- >>> id
- nome
- profissao
- nascimento
- sexo
- peso
- altura
- nacionalidade

Entidade Cursos

(Atributos/Dados que são tuplas, registros identificados e armazenados dos elementos/coisas/dados da entidade, ou seja, os 'cursos')
- >>> idcurso
- nome
- descricao
- carga
- totaulas
- ano

A diferença, no Modelo Relacional, é que um desses atributos (ou conjunto) servirá pra identificar cada uma das tuplas. 
Não podendo existir pessoas diferentes com um mesmo CPF (são os ATRIBUTOS ESPECÍFICOS = CHAVE PRIMÁRIA).
A entidade 'gafanhotos' possui como Primary Key o atributo 'id'. A entidade 'cursos' possui como Chave Primária o atributo 'idcurso'.
Chaves Primárias servem para: - identificar as tuplas e; - relacionar as entidades, pois o modelo relacional relaciona essas entidades.

Existe uma LIGAÇÃO entre um 'gafanhoto' e um 'curso'. 
[Gafanhoto] <assiste> ao [Curso].
O [Curso] é <assistido> pelo [Gafanhoto].
[Entidade] <Relacionamento> [Entidade] - mas nesse curso introdutório não teremos rel. ternários, rel. quaternários, rel. n-ésimos.

Esse diagrama se chama DIAGRAMA ENTIDADE-RELACIONAMENTO (Diagrama E-R, ou DER).
Tabelas não relacionais, quando ganham ESCALABILIDADE, começam a demandar mais um Modelo Relacional.

- Entidades se relacionam umas com outras através de uma ligação, um Relacionamento. 
- Cada 'gafanhoto' pode assistir a vários 'cursos'.
- 'Gafanhoto' assiste N 'cursos'.
- Cada 'curso' pode ser assistido por vários 'gafanhotos'.
- 'Curso' é assistido por N 'gafanhotos.
- Isso se chama CARDINALIDADE.

# Até agora, temos os CONCEITOS: Entidades, Atributos, Relacionamentos, Cardinalidade (Simples-1 ou Múltipla-N, c. nula, c. mínima, c. máxima, etc.) 

- A partir da CARDINALIDADE, podemos classificar os relacionamentos. 

- CLASSIFICAÇÃO: 
- muitos-para-muitos, N-pra-N (Um gafanhoto assiste N cursos. Um curso é assistido por N gafanhotos.)

- CLASSIFICAÇÃO:
- um-para-um, 1-para-1 ("Marido" se 'casa com' apenas uma "Esposa". Cada "Esposa" se casa apenas com um "Marido".)

- CLASSIFICAÇÃO:
- um-para-muitos, 1-para-N (
- ("Funcionário" cuida de "Dependente". Um funcionário pode ter um dependente, vários dependentes ou nenhum dependente.)
- (Cada "Dependente" é cuidado por apenas um "Funcionário".))

Relembrando os conceitos de CHAVE PRIMÁRIA (atributo específico que identifica as Tuplas). (CPF, código de barra, etc.)
Temos também o conceito de CHAVE ESTRANGEIRA:

###

Chave Estrangeira:
Imagina o mundo; num lado do mundo eu tenho uma entidade X (pessoa no Brasil) e essa entidade X tem sua chave primária (CPF). 
Do outro lado do mundo eu tenho uma entidade Y (pessoa em Portugal) e essa entidade Y também tem sua chave primária (NIF).
Se eu quiser fazer uma relação entre uma entidade e outra, Relações Teóricas na forma prática nada mais são do que "troca de chaves".
Então vou pegar a chave de um lado (CPF no Brasil) e jogar pro outro (NIF em Portugal).

Por exemplo, eu tenho que relacionar a entidade X (pessoa com CPF no Brasil) com a entidade Y (pessoa com NIF em Portugal).
Vamos supor que, para relacionar essas duas, eu tenha que usar a chave de X (CPF no Brasil), criar uma cópia para Y (Y que tem NIF, e criar Cópia-CPF na Entidade Portugal).
Percebe que essa nova chave de baixo (Cópia-CPF) em Y, já era a Chave Primária de Y (NIF), mas a cópia aqui foi a chave que veio de X (ex CPF).

Então ela não é CHAVE PRIMÁRIA de X (CPF), a chave primária de X que veio pra cá (Portugal). Eu chamo essa cópia da Chave Primária de X de: Chave Estrangeira (Cópia-CPF).
Isso é, Chave Estrangeira ERA a Chave Primária de alguém (ex Brasil). Só que ela veio de um lugar (Brasil, X) para o outro lugar (Portugal, Y). 

E o que vem de um lugar para o outro: O que é? - Estrangeiro. Quando um cara dos EUA vem ao Brasil, ele é estrangeiro. 
Então, chave estrangeira é uma chave primária de algum lugar que veio pra outro lugar.

Basicamente, criar relacionamento entre tabelas é fazer uma troca de chaves, pegar uma chave de um lado, jogar para o outro lado, e deixar de ser Chave Primária pra se tornar em uma Chave Estrangeira.

As regras são baseadas nas CLASSIFICAÇÕES do relacionamento (1-1, 1-N, N-N).

- Classificação de Relacionamento de 1:1 
- Marido <casado> Esposa (manter a relação entre duas tabelas). 
      Marido (`cpf-marido`, nome, nascimento, nacionalidade, ´cpf-esposa´)     <<<
      Esposa (`cpf-esposa`, nome, nascimento, nacionalidade)                >>>

# Podemos adicionar a Chave Primária cpf-esposa, copiar pra Entidade Marido, com nome cpf-esposa (Chave Estrangeira).
# Os dados não precisam ser iguais/nome, mas os TIPOS DE DADOS devem ser compatíveis (varchar, int, time).

- Classificação de Relacionamento de 1:N - Regra: Pega a chave primária do lado ÚNICO e joga no lado MUITOS como Chave Estrangeira. 
- Funcionário <cuida> Dependentes (manter a relação entre duas tabelas, mesmo tipo: CPF = VarChar(12), cpf-func = VarChar(12)). 
      Funcionário (`cpf`, nome, cargo, especialidade, )                                >>>
      Dependente (`id`, nome, nascimento, nacionalidade, ´cpf-funcionario´)            <<<

- Classificação de Relacionamento de N:N - Regra: "". 
- Cliente <compra> Produtos (). 
      Cliente (`cpf`, nome, endereco, telefone)                >>>
      Produto (`cod-produto`, nome, fabricante, preco)        <<<
      [Cliente] n ---------- <compra> ---------- n [Produto]  # Vamos transformar a RELAÇÃO <compra> em um ENTIDADE [COMPRA]
      [Cliente] 1----<>---- n [Compra] n ----<>----1 [Produto]
                             /    |    \
                   `id-compra`   data    forma-pagto 

Aplica a regra 1:1 de maneira desmembrada, quando temos relacionamentos múltiplos n:n.
Então a regra de N-para-N é desmembrar os múltiplos relacionamentos desmembrados de 1:1.
- Regra 1:1 - Chave lado 1 (`cpf`) e jogo no lado MUITOS-n [Compra] como ´cpf-cliente´ (chave estrangeira).
- Regra 1:1 - Chave produto (`cod-prod`) e jogo no lado MUITOS-n [Compra] como ´cod-prod´ (chave estrangeira). 
"""





"""
Transcrição


Procurar no vídeo
0:00
hum hum hum hum
0:19
olá pequeno gafanhoto seja bem vindo a mais uma aula do seu curso em vídeo de
0:24
banco de dados como sql o meu nome é gustavo guanabara eu sou professor e agora nessa décima quarta aula do curso
0:31
do banco de dados com mais que l a gente vai dar uma pausa na parte prática e vamos falar um pouco sobre teoria falando um pouco sobre
0:37
relacionamento entre tabelas e essa é a partir dessa aula e calma você está
0:43
pensando em haia não ver ele com teoria popular a próxima aula se você pular para a próxima aula você não vai entender nada da 15ª eu te
0:51
garanto eu tenho uma proposta um pouco diferente quando o ensino banco de dados normalmente você fez no colégio na
0:56
faculdade com certeza o professor de banco de dados começou falando que o modelo relacional falou sobre aquele
1:02
monte de teoria e lá no meio do curso e começou a fazer banco de dados eu inverti um pouco as coisas eu comecei
1:09
fazendo um banco de dados a gente fez um banco de dados com duas tabelas simples e agora nós vamos
1:14
começar a conectar as tabelas eu vou falar um pouco agora sobre o modelo relacional e antes de mais nada é
1:20
importante que eu te digo o seguinte eu não vou me aprofundar no modelo relacional isso porque isso é um curso
1:26
introdutório de banco de dados na minha opinião se você é um aluno iniciante você não precisa saber exatamente como
1:33
funciona o modelo relacional logo de início e é claro que quanto maior o seu banco de dados melhor ele fica se você
1:40
utilizar conceitos de banco de dados como por exemplo o modelo relacional projeto de banco de dados normalizações
1:46
e muito mais o que eu quero deixar claro aqui é de que nenhuma dessas técnicas que acabei de citar são inúteis
1:52
elas são sim muito úteis mas para quando o usuário é iniciante para quando a
1:57
festa começando a aprender eu gostava guanabara seu professor
2:02
acho melhor começar com a parte prática cria uma ou duas tabelinha as básicas e
2:07
depois a gente entra mais aprofundadamente no modelo relacional e é exatamente isso que eu propus
2:13
utilizando no curso em vídeo de banco de dados e se você é daqueles que gosta de pular teoria com certeza você pulou a 1
2:19
do curso maxx da dru foi se criou lá a história de uma cidade não quero saber isso eu vou voltar aqui vou te falar um
2:25
pouquinho só nesse início sim sobre o que a gente tinha falado na aula um então se você perdeu o que importa da
2:30
aula um pra essa aula é exatamente esse conceito que vou passar água você deve se lembrar muito bem que lá na
2:37
década de 60 o governo dos estados unidos no departamento de defesa ea ibm fizeram o evento chamado com o brasil de
2:43
onde nasceu a linguagem cobol e os primeiros conceitos de banco de dados nessa época surgiu nos modelos e
2:49
hierárquico em rede que eram muito bons pra época mas com o passar dos anos eles acabaram se mostrando pouco
2:55
eficientes foi quando na década de 70 um dos engenheiros da ibm o edgar cot propôs a criação de um
3:02
modelo um tanto quanto diferenciado onde os dados muito mais do que apenas ligações eles teriam relações entre eles surgiu
3:09
então o modelo relacional nos modelos e hierárquico em rede você tinha simples ligações entre cidades
3:15
o modelo relacional trouxe essa ligação a um outro patamar ele criou relações onde eu não tenho
3:20
apenas uma ligação eu posso ter várias ligações e essas ligações têm significado graças ao modelo relacional
3:26
hoje em dia a gente pode ter um banco de dados onde por exemplo o cadastro uma pessoa e acabou que eu tenho um registro
3:32
a partir do acesso a esses dados dessa pessoa eu posso por exemplo ver onde ela mora ou que tipo de compras ela fez no
3:39
meu estabelecimento uma vez que ela tenha feito compras eu consigo ter acesso a data ea quanto isso afetou no meu estoque eu posso até
3:45
fazer com que meu sistema decida se o quanto que afetou meu estoque é o necessário para ter que entrar em
3:51
contato com o fornecedor e pediu uma reposição tudo isso é possível hoje em dia nos sistemas de forma simplificada
3:56
graças ao modelo relacional eu estou falando aqui o modelo racional é o ápice é o auge da tecnologia não já surgiram
4:03
outros modelos como por exemplo o modelo orientado a objeto que é bastante útil tem vantagens em relação ao modelo
4:08
relacional só que infelizmente ele não foi adotado em grande escala até o momento em que eu tô gravando esse vídeo
4:14
o modelo relacional reina dentro do mercado brasileiro do mercado mundial então é melhor que a gente vai se basear
4:19
e você deve se lembrar das aulas anteriores também quando eu apresentei o godofredo pra vocês lembram o problema do godofredo godofredo que tinha esposa
4:27
uma filha aquele negócio lá do início então a gente vai voltar a esse tipo de conceito porque ele é de suma importância para
4:33
que você entenda o ponto desse curso daqui pra frente a gente apresentou além de godofredo outras pessoas aí que a
4:38
gente tinha cadastrado o que eu propus numa das aulas iniciais do curso era pegar todo mundo e colocar
4:43
num container lembra disso peguei esse conteúdo escrevi um nome nele por exemplo gafanhoto e dentro eu posso
4:48
colocar gafanhotos eu posso colocar pessoas que são estudantes do curso em vídeo além de armazenar eles dentro de um container
4:54
eu coloquei todas as informações que são necessárias para identificar cada um deles como por exemplo a identificação
4:59
nome profissão nascimento sexo peso altura e nacionalidade você deve se lembrar dessa relação
5:05
conceitual que eu inventei aí localmente no início mas acontece que ela vai fazer mais sentido agora esse container
5:11
é como se fosse um retângulo que cabe dado dentro é isso só que em vez de desenhar um container eu vou desenhar de
5:16
maneira mais simplificada beleza eu vou transformar esse container num simples retângulo e vou escrever da mesma
5:22
maneira gafanhoto eu também vou parar de chamariz container de container eu vou passar a chamar ele de entidade então de forma
5:28
resumida uma entidade para o banco de dados é como se fosse um container onde eu vou colocar dados sobre alguma coisa
5:35
sobre alguma pessoa nesse meu caso aqui o meu container gafanhoto vai conter tados de alunos dados de gafanhotos que
5:42
são alunos do curso em vídeo então sempre que você vira uma entidade escrito gafanhoto imagine que a entidade como se fosse um
5:48
container e dentro dos contêineres gente tem vários gafanhotos porque está identificado na etiqueta que está logo
5:54
abaixo então se você olha por exemplo um container uma entidade escrito produto com certeza você vai imaginar o que
6:00
dentro desse contender tem um monte de dados sobre produtos têm lá o nome do produto quem fabricou quanto ele custa
6:07
quanto ele pesa com a cor da embalagem o que for necessário para armazenar dados sobre esse produto esses dados eu vou
6:14
parar de chamar de dado também eu vou passar a chamar de atributo então toda a entidade possui uma coleção de atributos
6:21
definidos esses atributos vão compor os dados que compõem cada um dos elementos
6:26
que estão dentro dessa entidade ficou confuso para você volta um pouquinho vídeo assistir esse pedaço de novo e com
6:33
certeza você vai entender no momento do nosso curso até agora a gente criou duas entidades a entidade
6:39
gafanhoto ea entidade curso a entidade gafanhoto possui atributos relacionados apenas alunos ea entidade
6:46
curso possui dados relativos apenas a cursos como identificação dele o nome de
6:52
inscrição carga total de aulas e o ano em que ele foi criado para entender que eu não consigo pegar um aluno e colocar
6:58
dentro do contêiner do curso deu pra entender que eu não consigo pegar um curso e coloco dentro do contêiner de aluno então são coisas
7:04
diferentes que eu vou colocar em container diferentes e guardar dados diferentes de forma mais técnica eu vou
7:11
dizer o seguinte dados são representados em forma de atributos esses conjuntos de atributos vão
7:16
identificar duplas vão identificar registros vão identificar coisas que estão armazenadas dentro de entidades e
7:24
tudo isso já existia nos outros modelos como modelo em rede ou modelo era a diferença do modelo relacional como eu
7:29
disse anteriormente é que eu consigo fazer ligações entre essas entidades outra coisa que nós vimos nas aulas
7:35
anteriores é que um desses atributos ou um conjunto desses atributos servem para identificar cada uma das duplas
7:41
isso é eu sou uma pessoa você é uma pessoa alguma coisa diferencia a gente
7:47
de forma que não exista duas pessoas com a mesma coisa por exemplo o meu cpf eu tenho um cpf você tem o cpf eu não
7:54
posso te me identificar e identificar por altura por exemplo pode ser que a minha altura seja diferente da sua
8:00
mas pode ser que a minha altura seja a mesma de outra pessoa pode existir outra pessoa que se chama gustavo guanabara pode acontecer mas com certeza
8:08
duas pessoas não têm o mesmo cpf e nós vimos que existem atributos específicos chamados atributos chave primária no
8:15
caso aqui da entidade de gafanhoto eu tenho e de como chave primária e no caso de curso eu tenho e de curso como chave
8:21
primária não existem dois gafanhotos com o mesmo de e nem dois cursos com o mesmo de curso e é aí que o modelo relacional
8:28
começa a se diferenciar dos modelos mais antigos a presença de chávez é algo muito importante e você vai entender jajá
8:35
porque isso precisa acontecer então a primeira base do modelo relacional foi o uso de chaves e essas chaves primárias
8:42
elas servem para identificar as duplas e elas vão servir também para relacionar as entidades isso porque como o próprio nome sugere o
8:49
modelo relacional relaciona essas entidades então quando você cria um modelo relacional vocês
8:55
pergunta a entidade tal pode se relacionar com outra entidade por exemplo um gafanhoto pode se ligar em
9:01
algum curso de alguma maneira e eu te pergunto existe uma ligação entre gafanhoto curso eu te digo claro que
9:08
existe uma ligação um gafanhoto assistir um curso percebe que eu representei em forma de um losango e coloquei uma
9:15
palavra que identifica qual é a relação entre gafanhoto e curso gafanhoto assistir cursos curso é assistido por
9:22
gafanhoto então existe uma relação entre um e outro e é claro existe uma entidade dominante e uma entidade relacionada a
9:29
ela mas nada impede que eu faça a leitura nos dois sentidos eu só vou ter que mudar um pouquinho a palavra cada livro de banco de dados da
9:35
uma regra um pouco diferente para a nomeação desses losangos eu vou utilizar o modelo relacional um pouco mais livre
9:42
isso porque o nosso curso é focado diretamente no ensino de modelo relacional eu estou fazendo aqui de uma
9:47
forma simples de uma forma um pouco mais didática apenas relembrando todo retângulo que vai aparecer aqui entidade
9:53
então eu tenho duas entidades a entidade gafanhoto entidade curso apareceu um losango no meio todo losango
10:00
a gente vai chamar de relacionamento então pode acontecer de duas entidades duas ou mais entidades se relacionar
10:08
entre si nós também não vamos falar sobre relacionamentos ter nariz e quatro cenários em cenários
10:13
nós não vamos falar de relacionamentos múltiplos nós vamos falar que nesse curso introdutório apenas de relacionamentos duplos que são aqueles
10:20
que envolvem apenas duas entidades então o que nós podemos dizer já que a entidade é um retângulo eo losango é o
10:26
relacionamento que esse diagrama tem um nome neste diagrama se chama diagrama entidade-relacionamento você pode
10:34
escrever diagrama entidade traz relacionamento ou diagrama é traço r ou
10:39
de forma mais simplificada ainda você pode simplesmente colocar der então o der que é o diagrama
10:44
entidade-relacionamento ele vai mostrar como o modelo relacional está sendo
10:49
aplicado dentro desse meu mini mundo dentro dessa minha possibilidade dentro dessa minha situação que eu quero criar
10:56
um banco de dados então nesse nosso curso a gente está criando um banco de dados para cadastrar o aluno e para cadastrar cursos só que
11:02
eu posso relacionar aluno concurso porque aluno assiste curso e eu posso simplesmente falar isso de forma
11:08
herbal e isso pode causar uma certa dúvida pra você ou então eu crio um diagrama de idade relacionamento que
11:14
essa maneira gráfica de representar como modelo relacional vai funcionar dentro do banco de dados
11:20
ficou claro pra você então antes de criar um banco de dados pequenininhos não precisa se preocupar com o modelo
11:25
relacional se o banco tem duas tabelas uma tabelinha só eu e você não precisa ligar uma tela com a outra relaxa fi você vai criar seu banco quero
11:33
cadastrar imagina só quero cadastrar pessoas beleza não saber o modelo relacional para isso agora se o banco começará a
11:39
crescer se você precisar ligar um dado de uma tabela com o dado de outra tabela vai
11:45
ficar colocando tudo em uma tabela só aí sim você vai precisar estudar um pouco mais sobre o modelo nacional e até um
11:51
pouco mais do que eu te passando aqui não acho que o que eu vou falar nessa aula teórica de modelo relacional vai
11:56
suprir toda a necessidade que você tende houve um pouquinho mais sobre o banco de dados o que eu quero fazer aqui é apenas
12:02
um papel legal é apenas o papel inicial se você quiser se aprofundar você vai ter que ler um livro você vai ter que
12:08
procurar um professor procurar um profissional responsável e aí sim você vai se aprofundar no estudo do banco de
12:13
dados então esse diagrama que está aparecendo na sua tela nada mais é do que um diagrama da entidade relacionamento um
12:19
der então a entidade se relacionam umas com as outras através de losangos através de
12:25
relacionamentos e como eu já falei um milhão de vezes sempre que aparecer uma entidade veja como se fosse um container isso é
12:32
votar um espaço um pouco mais para poder representar aqui pra vocês sempre que você vira uma entidade gafanhoto por
12:37
exemplo imagine como se fosse um grande contêiner onde dentro coloco gafanhotos coloquei ao se assim da mesma maneira
12:44
quando falar de curso fica imaginando que dentro desse contender tem dados sobre um determinado curso por exemplo o
12:51
curso de html5 que a gente tem aqui você não sabia que o curso em vídeo tem mais do que isso olha aqui ó dá uma olhada em cima aqui
12:57
em cima tem algumas playlists cíclica que a tese interativa que aparece até no celular aperta e sizing dá uma olhada pode
13:04
apertar agora não tem problema nenhum o ala não vai parar você não vai fechar nada a peça que o isim apareceu aqui do
13:09
lado apareceu então você tem um monte de curso aqui você pode clicar aqui e acessar ou então você acesso o curso em
13:15
vídeo pontocom então a nossa playlist no youtube é só procurar no youtube por curso em vídeo a gente vai aparecer logo o primeiro essa
13:21
fase seguinte por curso de html5 no youtube você vai ver que vai ser a dominação mundial e
13:27
não pense que de gafanhoto só tem um aluno dentro de curso tem um curso não eu posso ter vários afã e outros e eu
13:32
posso ter vários cursos esses dados podem coexistir de forma isolada como está acontecendo até o
13:37
momento nesse curso então eu tenho cadastro gafanhotos eu tenho cadastro de cursos o que não está acontecendo eu não posso fazer um
13:44
aluno assiste um curso ainda isso porque eu não falei de relação ainda e agora que a gente está vendo isso deu pra entender que você não
13:50
prestar atenção nas aulas se você não entender sala 100% você não vai conseguir prosseguir no curso banco de dados
13:55
então a dica que eu dou é assistir à aula mais uma vez você já o gafanhoto experiente com certeza tudo que estou falando aqui você já conhece mas acaba
14:02
que a galera se divertiu na maneira maluca de explicar as coisas é bem legal a partir do modelo relacional não posso dizer que existe
14:09
relacionamento entre as duplas das entidades por exemplo o primeiro gafanhoto ilsinho ele pode por exemplo
14:15
assistir o concerto ml pode mas ele também pode assistir o curso de php nada impede que eu tenho também por
14:22
exemplo a senhorinha lá embaixo está assistindo curso de word mas ela também assistir o curso de html e um de php
14:28
o godofredo godofredo faz java java que eu vou enfrentar limitado na parada
14:33
trabalhando mais é como é que essa coisa tomar conta de uma menininha político de putin o rapazinho de cabelo encaracolado
14:38
ali vai fazer o curso de html5 e o curso the word por exemplo recebe aí que cada
14:44
uma das cores representam qual curso que cada um tá assistindo então vamos prestar atenção aqui ó o
14:50
primeiro gafanhoto tá fazendo dois cursos o segundo gafanhoto também está fazendo dois cursos
14:56
o terceiro está fazendo um curso só ea última está fazendo três cursos então a gente chega à conclusão de que
15:02
um mesmo gafanhoto ele assistir vários cursos então eu vim aqui ó e coloco um emmy
15:09
então cada gafanhoto assistir vários cursos olha o sentido da leitura um gafanhoto
15:16
assistir n cursos deu pra ler é muito importante que você entenda esse sentido de leitura
15:23
vamos fazer do outro lado agora cada curso daqui pode ser assistido por exemplo html5 está sendo assistido por
15:30
quantos por três aqui não é que são o senhorzinho o rapaz de cabelo encaracolado ea mocinha lá no final
15:36
então cada um dos cursos pode ser assistido por n gafanhotos
15:44
então você sempre vai partir de um lado um desses aqui a assistir quanto do lado
15:49
de lá várias um do lado de lá é assistido por quantos desse lado vários
15:54
réus botar e nem de um lado nem do outro e isso tudo tem um nome é cardinale
16:00
idade então até o momento a gente vê alguns conceitos entidades atributos
16:05
relacionamentos e agora cardinale idade à cardinalle idade ela pode ser simples
16:10
ou múltipla 1 ou n eu não vou ficar me aprofundando aqui existe à cardinalle idade nula existe à
16:17
cardinalle idade mínima e máxima eu vou trabalhar nesse curso apenas com um modelo simples de cardinale idade
16:23
o modelo de cardinale idade máxima representado no diagrama de idade relacionamento mas se você se aprofundou
16:28
no curso se você estudou com uma outra bibliografia você vai ter o conceito de cardinale idade mínima racionalidade
16:35
máxima vai ver que existem turmas que não são relacionadas com outras mas a gente não vai se aprofundar aqui
16:41
você chato falando isso várias vezes porque com certeza lá no final vai ter gente comentando assim a você não falou
16:46
do conceito de por exemplo entidade fraca você não viu a eles e disse que toda entidade tem que ter uma chave mas
16:52
existem entidades fracas que são aquelas entidades que não possuem dados suficiente para ter uma chave eu sei
16:57
isso tudo porque o gafanhoto mas o que eu quero deixar claro aqui é que esse curso é um curso introdutório o
17:03
meu objetivo aqui não é me aprofundar até porque o curso é curso básico de
17:08
banco de dados é para criar um banco de dados básicos mas ainda assim eu vou criar relações entre as tabelas lá no
17:14
meu mas kerry mas eu preciso sentença que antes a partir da cardinale idade a gente pode classificar um relacionamento
17:20
esse relacionamento você tá vendo aí ele tem um gafanhoto pra n cursos e um curso
17:26
pra n gafanhotos então cada um dos gafanhotos pode assistir e minicursos e cada um dos
17:34
cursos pode ter em gafanhotos assistindo isso vai fazer com que a classificação
17:40
do meu relacionamento seja muitos para muitos e você pode chamar de n pra n
17:45
muitos para muitos a escola maneira que você achar melhor ele vai falar mas cuba o relacionamento de muito para muitos
17:51
não é não vamos ver alguns exemplos aqui não é um outro exemplo aqui de relacionamento por exemplo marido casa
17:58
com a esposa então você se lembra aí sempre que você encontrar entidades você expande ela na sua mente imagina que ela
18:04
expandida dentro da entidade marido eu tenho vários maridos dentro da entidade esposa eu tenho várias esposas e aí a
18:11
gente pode traçar uma relação entre essas pessoas por exemplo o godofredo é casado com dolores lembra disso
18:17
eu tenho por exemplo últimos ilsinho de baixo é casado com a moça japonesa ele percebe que o marido do meio ali ele não
18:24
tem relação com nenhuma dupla da entidade esposa que está no lado direito e significa que ele está solteiro
18:29
isso é uma dupla não tem obrigatoriedade de ter uma outra dupla que antes de continuar antes que eu seja enxurrada de
18:35
várias mensagens falando que eu sou homofóbico o senhor olha só eu sei que hoje em dia pode homem casar com homem e mulher com
18:42
mulher o marido casar com o marido uma esposa casa com a esposa existe esse tipo de coisa agora só nós
18:48
não estamos num curso preconceituoso mas estamos num curso básico se eu começar a dificultar as coisas se
18:55
eu começar a criar possibilidades eu não explica um conceito que é básico então vamos ficar com esse conceito de
19:01
casamento não estou dizendo que esse é o modelo certo esse é o modelo mais simples da gente entender certo é o
19:07
modelo mais simples que poderia explicar então aceita isso não é uma questão de preconceito é uma questão de didática
19:13
eles então vamos analisar aqui ó uma dupla desse lado por exemplo um cara
19:20
daqui só pode se casar com uma esposa então a um cara desse se casa com um
19:27
cara desse aqui então vou escrever lá um isso é cada marido casa com apenas uma
19:34
esposa vamos fazer sentido contrário cada esposa casa com apenas um marido
19:42
e aí mais uma vez não é uma questão de preconceito cultural porque sabe que existem culturas que aceitam que um cara
19:48
casa com várias mulheres uma mulher com vários caras enfim é uma questão didática é uma questão de
19:54
simplificação das coisas para que tudo fique mais fácil de compreender então para o nosso modelo cultural uma
20:00
pessoa só pode casar com uma pessoa isso gera um relação momento de cordialidade um pouco diferente da realidade que a gente viu
20:07
antes então a classificação desse relacionamento vai ser diferente em casos onde o marido casa com apenas uma
20:13
esposa e uma esposa casa com apenas um marido a gente tem um relacionamento um pouco
20:19
diferente é um relacionamento já cardinale da dita um de um lado a outro do outro então a classificação desse
20:24
relacionamento casa com é a classificação 1 para 1 então a gente acabou de ver mais um tipo de
20:30
relacionamento nós tínhamos anteriormente o relacionamento de muitos para muitos agora nós temos um relacionamento de um
20:35
para um pronto agora acabou ainda não tem mais um tipo de relacionamento aqui vamos ver mais um exemplo
20:42
por exemplo um funcionário cuida de dependente e independente é cuidado por funcionário mais uma vez vamos dar uma
20:49
ampliada na nossa mente colocar vários funcionários do lado esquerdo e vários independentes do lado direito
20:54
então vamos lá o godofredo ele tem um dependente que é a go dores
20:59
a gente tá aqui embaixo aqui cinco dolores é o filho do godofredo com dolores e já deve ter visto isso no curso de banco de dados esqueceu de
21:06
colocar ali o o senhorzinho debate que é casado com aquela japonesinha ele tem um dependente que o menino carsharing e
21:12
também tem outro que o rapazinho lá de cima então percebeu foi o terceiro funcionário ele está relacionado a dois
21:17
dependentes ele tem dois filhos por exemplo o primeiro só tem um o do mesmo resolver está sozinho tadim ele não tem
21:24
filho nenhum ele não tem independente nenhum então mais uma vez eu digo pode ter nenhum pode ter um ou pode ter
21:30
vários e aí vêm os conceitos de cardinale idade nula taxa de natalidade simples múltipla e tudo mais então vamos analisar aqui ó
21:36
um funcionário pode ter um independente vários independentes ou nenhum
21:41
dependente que é o caso desse aqui tá e aí o que eu escrevo 01 o n vai pelo
21:47
maior qual maior o maior caso aqui é esse último caso que ele tem vários então eu digo que cada funcionário pode
21:54
cuidar de n independentes e cada dependente e independente pode ter
22:00
vários funcionários relacionados a gente sabe que não né mas é só falar mas na minha empresa pode é uma situação adversa mas normalmente
22:08
um dependente existe apenas um funcionário tomando conta dele então tem
22:13
aqui ó cada dependente é cuidado por apenas um o funcionário mas guanabara se no meu
22:20
sistema foi esse modelo mais moderno esse modelo é que aceita que o mesmo independente tenha dois funcionário é só
22:26
você fazer um relacionamento muito pra muito nesse meu caso aqui na minha empresa fictícia que estou colocando
22:31
aqui um funcionário pode ter vários independentes mas cada dependente só pode estar relacionado a um funcionário
22:37
isso me gera um outro tipo de relacionamento onde cada funcionário pode ter e independentes e cada
22:44
dependente pode ser apenas de um funcionário temos agora um relacionamento que a gente classifica como de um para muitos
22:50
e tem livros que classificam um pra muitos muitos para 1 na verdade é só o sentido que você lê então eu tenho três maneiras de
22:57
classificar os meus relacionamentos 1 para 11 para muitos e muitos para muitos
23:02
então o seu primeiro passo deve ser modelar as entidades com seus atributos e seus relacionamentos e depois
23:09
classificar cada um dos relacionamentos a esse relacionamento aqui é um para um e se é um para muitos esse é muito pra
23:15
muitos então vai botando cardinale idade aí pertinho das suas entidades isso é de suma importância porque aí a gente vai
23:21
ver uma regrinha bem básica que é a regra principal do modelo relacional antes vamos fazer um exemplo aqui por
23:28
exemplo o cliente compra um produto e aí classificar pra mim cliente com o produto qual seria cardinale idade um
23:35
papel aqui então eu tenho cliente e tem o produto amplifica aí na sua mente
23:40
amplifica na sua cabeça cliente imagina vários clientes produto imagina vários produtos e faz a relação faz à
23:47
cardinalle idade e classifica esse relacionamento pra mim pausa o vídeo agora e tenta fazer isso mentalmente a sua resposta
23:54
já o kindle faz esse exercício faz isso paulo o vídeo agora e diz qual é a
23:59
classificação desse relacionamento então vai lá pausa eu espero que você
24:04
tenha pousado e tenha feito esse exercício mental que eu tinha falado anteriormente vamos ampliar aqui então vão aplicar
24:10
cliente e produto vou colocar vários clientes aqui na minha cidade cliente e vou colocar várias ocorrências de produtos dentro da
24:17
minha área de produto santa entidade de produtos agora vamos fazer o seguinte vou fazer os clientes comprarem produtos por
24:23
exemplo o godofredo ali ó comprou uma bola e também comprou um telefone à lá e comprou duas coisas ou sozinho lá de
24:29
baixo ele comprou um tênis comprou uma bola e comprou um telefone cirurgia da ostentação aí tá cheio da
24:36
grana ea dolores ela também comprou uma bola e em tênis provavelmente a dolores vai querer jogar
24:41
bola com esse teste percebe aí cada cliente comprou vários produtos então vamos conversar classificar aqui ó
24:48
pegar um cliente que um cliente pode comprar quantos produtos qual o máximo ó são vários o então eu vou colocar aqui
24:55
em cima um n isso é cada cliente pode comprar n produtos
25:02
agora vou pegar o seguinte ó a bola a bola foi comprado com os clientes a três clientes só têm 37 anos chegando a bola
25:08
então cada produto pode ser comprado por n clientes
25:15
temos aí mais uma vez um relacionamento muito para muitos que é o terceiro forma
25:21
de relacionamento que a gente viu anteriormente beleza agora que você citou uma dúvida pode ter na sua cabeça
25:26
beleza eu entendi que a entidade se relacionam eu entendi que eu posso ter duplas ligadas a várias a uma nenhuma
25:33
dupla do outro lado e criando esse relacionamento tá mas isso na prática na prática como é
25:39
que eu faça a ligação entre uma entidade outra ea gente vai ter que lembrar de um dos atributos muito especiais que a
25:45
gente já viu inclusive no início dessa aula é muito importante que a gente lembre que existem as chaves
25:51
a gente viu o conceito de chave primária não vimos só dando uma pequena relembrada chave primária é um atributo
25:56
específico que identifique as duplas é um atributo que vai fazer com que nenhuma das duplas do marido
26:03
nenhum dos maridos tem um atributo igual ao outro qual atributo que não pode ter um marido igual ao outro cpf por exemplo
26:10
então cpf seria chave primária da entidade marido por exemplo produto o
26:15
que o produto não tem igual ao outro são várias coisas que não tem igual mas acaba que algumas coisas podem se
26:20
repetir mas por exemplo o código de barras de um produto o código de barras não tem dois produtos com o mesmo código
26:26
de barra se eles tiverem o mesmo código eles são produtos iguais então o código de barra é um identificador do produto ficou
26:32
claro isso então nós vamos colocar o cpf código de barra como a minha chave primária dentro das
26:39
entidades de cada um dos produtos ou de cada um das pessoas do marido que enfim eu venho aqui existe um outro tipo de chave que a
26:46
chave é estrangeira e muita gente se enrola com o conceito de chave estrangeira
26:51
eu tenho uma maneira muito simples de explicar isso aquele meu jeito de sempre mas é simples vamos entender
26:57
que o conceito de chave estrangeira imagina o mundo num lado do mundo eu tenho uma entidade xixi e essa entidade
27:03
x tem sua chave primária do outro lado do mundo eu tenho uma entidade y e as entidades vão também tem sua chave
27:09
primária se eu quiser fazer uma relação entre uma entidade outra relações teóricas na
27:15
forma prática nada mais são do que troca de chávez então vou pegar a chave de um lado jogar
27:20
pro outro pegar a chave do outro jogar por 11 então basicamente por exemplo eu tenho que relacionar a entidade x quantidade y
27:27
vamos supor que para relacionar essas duas eu tenho que botar a chave d x criar uma cópia para y percebe que essa
27:33
chave de baixo já era a chave primária de y essa aqui foi a chave que veio de x
27:39
então ela não é chave privada dym a chave primária de x que veio pra cá então eu chamo essa chave primária de x
27:47
de chave e estrangeira isso é chave estrangeira era a chave primária de alguém só que ela veio de um
27:53
lugar para o outro e o que vem de um lugar para o outro o que é estrangeiro quando um cara dos estados unidos veem o
27:58
brasil é o que ele é estrangeiro então chave estrangeira é uma chave primária de algum lugar que veio pra outro lugar
28:06
à guanabara você está me dizendo que relação entre tabelas é só troca de chaves na prática
28:12
assim na prática você vai começar a pegar a chave de um lado jogar pro outro seguindo algumas regras é claro adianta
28:18
só da anata beleza eu vou pegar todas as chaves jogar que está tudo relacionado não existe uma técnica existem regras
28:24
para isso a gente vai ver daqui alguns segundos mas basicamente criar relacionamentos entre tabelas é fazer
28:30
troca de chávez é pegar a chave privada de um lado e jogar para outro lado e quando eu jogo dessa chave formada por
28:35
outro lado ela não virá mais uma chave primária é uma chave estrangeira eu espero que se você se enrolasse com isso
28:41
você não se enrole mais do que uma chave estrangeira a chave primária de alguém não é minha mas é alguém veio de algum
28:48
lugar da guanabara mas beleza que regras são essas essas regras são baseadas nas
28:53
classificações dos relacionamentos tá vendo como uma coisa se liga na outra você precisa modelar uma entidade
28:58
ver quais são os atributos dela definirá qual a chave primária para que eu preciso achar primária vou precisar para identificar as duplas
29:05
para você não ter registros duplicados mas também vou precisar dela porque eu preciso relacionar deu pra entender o
29:10
negócio sem chave primária não existe relação tão preciso pegar a chave privada de um lugar jogar em outro lugar
29:15
para poder fazer essa relação à guanabara mas se eu não tiver chave primária se não tivesse a primeira não tem relação porque não vou poder pegar um
29:21
chefe manda aqui e jogar como xavi estrangeira lá ficou simples ea regra pra você pegar uma chave jogar de um
29:26
lado para o outro depende da classificação do relacionamento então a gente viu três classificações 1 para 111
29:32
para muitos e muitos para muitos vamos ver a regra para cada um desses casos então começar um relacionamento um
29:37
para um aquele relacionamento que a gente viu anteriormente marido casa com a esposa o marido caso apenas como esposa uma
29:44
esposa é casada apenas com o marido quando o relacionamento é de um para um a gente tem que começar a pensar porque
29:49
o seguinte existe uma regra dizendo quando o relacionamento de um para um você pode juntar as tabelas numa tabela só já que o registro só se relaciona com
29:56
um você pode juntar só que essa regra também diz o seguinte você tem que ver se faz sentido manter esses dados separados nesse nosso caso
30:02
marido e esposa faz todo o sentido porque são duas pessoas que são casadas têm um relacionamento mas cada um tem a
30:08
sua própria vida então elas são separadas então nesse nosso caso aqui eu vou manter a relação entre duas tabelas
30:15
quando você tiver um relacionamento para um que quase não acontece você vai analisar o poço será que eu posso juntar
30:21
essas duas tabelas numa tabela só se a resposta for sim junta se a resposta for não deixa
30:27
separado tá deixa separado e faça o que aí vamos lá nós vamos pegar aqui marido esposa ou colocar que os atributos
30:33
marido marido tem cpf do marido o nome a data de nascimento e nacionalidade a esposa também tem o cpf
30:40
da esposa o nome do nascimento e nacionalidade na verdade aqui eu posso chamar só de cpf
30:45
cpf mas por questões didáticas só para simplificar o chamei de cpf marido ctf esposa para relacionamentos um para um é
30:52
mais fácil de fazer escolhe uma entidade geralmente quem chama de entidade dominante e antes que
30:57
a galera do preconceito teores na questão ética não a questão cultural na
31:03
questão didática para de ser chato então escolha aqui por exemplo marido
31:08
vou base aqui em marido que a regra diz pegue a chave primária da outra entidade
31:16
e transfira para o lado marido colocando ele como xavi estrangeira eu poderia por
31:22
exemplo fazer o contrário pegar a chave cpf marido e jogar aqui em esposa como xavi estrangeira quando
31:28
representei aqui na esquerda geralmente a gente representa na esquerda as entidades dominantes
31:33
então o que eu fiz foi o seguinte decide aqui que a entidade dominante é o marido peguei a chave primária de esposa e
31:39
transferir para cá da trama cpf esposa veio pra cá esse nome não precisa ser o mesmo tá mas os dados precisam ser os
31:47
mesmo por exemplo se isso aqui é um dado inteiro é esse que também tem seu lado inteiro se é baixar esse que tem precisa
31:52
se eu achar então é preciso que os atributos sejam compatíveis e não precisam ter o mesmo nome mas que eles sejam compatíveis
31:59
essa é a regra para relacionamentos um para um eu pego quantidade dominante descido quantidade dominante pega a
32:05
chave primária daqui não é dominante e jogo como xavi estrangeira para mim entidade dominante
32:10
vamos agora há outro tipo de relacionamento ela flamengo de um para muitos é o relacionamento de um para muitos o exemplo que a gente viu foi
32:16
funcionário independente de cada funcionário tem vários independentes cada dependente depende apenas de um funcionário
32:21
vamos ver os atributos de um funcionário que eu coloquei aqui o cpf e nome cargo e especialidade e pra dependente eu
32:26
coloquei ali e de nome nascimento e nacionalidade eu não votei cpf aquino dependente
32:32
porque pode ser que o dependente não tenha cpf apesar de hoje em dia tem muita criança que atende cpf a regra do relacionamento
32:38
para muitos ou muitos para um neves e chama do jeito que você quiser também é simples basicamente o que você vai fazer a regra
32:45
relacionamento de um para muitos é o seguinte você pega a chave primária do lado 1 e joga no lado muitos como xavi
32:52
estrangeira é sempre assim não vai precisar decidir nada é um relacionamento de um para muitos pega a chave primária do lado 1 e joga no lado
32:59
muitos como xavi estrangeiro vamos fazer isso daqui então a regra é pegue a chave primária do lado um e
33:07
jogue do lado do n como xavi estrangeira ontem ele o cpf do funcionário percebe
33:13
aqui eu chamei de cpf e aqui eu chamei de cpf do funcionário não precisa ter o mesmo nome mas por
33:19
exemplo se cpf aqui é rachar de 12 aqui também é baixar de 12 o tamanho tem
33:25
que ser o mesmo a gente não tem compatibilidade é uma regra é eu vou pegar o cpf daqui e vou
33:31
jogar lá no dependente como xavi estrangeiro viu esse passo na próxima aula a gente vai aprender
33:36
como definir uma chave estrangeiro na prática alguns abril mas quer lá e vamos definir chaves estrangeiros que são a
33:42
base do relacionamento vamos partir agora para a terceira forma de classificação dos relacionamentos que o relacionamento muitos para muitos um
33:49
relacionamento muito próximo do que a gente viu dois exemplos né o último foi cliente produto o cliente comprou vários produtos
33:55
o mesmo produto pode ser comprado por vários clientes o relacionamento muitos para muitos é o que é mais entre aspas
34:01
complicado é o que a galera mais se enrola não é difícil a regra simples para você criar uma relação muito para
34:07
muitos que se vai fazer vou colocar aqui os atributos de clientes o cliente tem cpf nome endereço telefone e vou colocar os atributos de
34:14
produto código do produto nome fabricante preço é saber que eu não botei a situação e nada por exemplo
34:19
endereço preço não tem acento não tem nada tudo letra minúscula essa é a regra os atributos que você precisa usar o
34:25
espaço a uso assim para representar o relacionamento intensidades muitos para muitos nós vamos fazer o seguinte o
34:32
relacionamento que é aqui no meio vai virar uma entidade olha só poderá afastada o meu relacionamento compra
34:39
virou uma entidade percebe que o enem que estava perto do cliente de produto andou pra essa entidade aqui vou fazer
34:46
de novo movimento voltei aqui ó percebe um movimento do n o enic estava colado em cliente e o enem
34:54
estava colado em produto vão andar pra compra e se mandar pra cá e e se mandar
34:59
para cá percebe olha a animação beleza então o m ficou mais próximo da compra e
35:05
compra também tem seus atributos por exemplo qual o identificador da compra qual foi a data que o catar comprou qual
35:12
a forma de pagamento que ele utilizou então vou botar forma de pagamento em produto nem cliente eu vou deixar em compra ele também tem sua chave primária
35:19
e aí eu tenho três entidades agora faltou os relacionamentos eu vou criar 2.000 relacionamentos aqui
35:25
ó dando criei 2000 e relacionamentos e falta cardinale desse lado não está nem
35:30
pensar é só colocar um então coloquei um aqui e coloquei um aqui então o que eu tinha de
35:36
relacionamento muitos para muitos se transformou nesse com junto relacional aqui mais uma vez eu te
35:41
digo tacom dúvida volta um pouquinho volta um pouquinho dá uma olhada na descrição do vídeo sempre boto ou os
35:48
minutos a minutagem dos dados importantes volta e assistir de novo você não pode sair dessa aula com
35:54
dúvidas então percebe agora que o que eu tenho são três entidades ligadas duas a duas como relacionamento para muitos
36:02
e qual é a regra de relacionamento são para muitos a chave primária do lado um vai para um lado muitos como xavi
36:07
estrangeiro não foi isso que eu te ensinei é só aplicar basicamente eu vou fazer aqui ó vou pegar o cpf ea chave de um lado um lado
36:14
um pega a chave primária e joga do lado muitos então vou pegar o cpf
36:19
vou jogar para lá como o cpf do cliente como também tem um relacionamento aqui vou pegar o código do produto
36:26
vou jogar aqui pra mim tirar de compra também como xavi estrangeira então basicamente que eu fiz foi pegar a chave
36:32
primária desse lado jogar pra cá como xavi estrangeira ea chave primário desse lado jogar pra cá como xavi estrangeira
36:38
isso porque são relacionamento e se relacionando o que para muitos a regra é peça-chave da que joga pra cá e aqui eu
36:45
também tenho um para muitos na verdade muitos para um né eu pego a regra público eu vou pegar a
36:50
chave primária do lado 1 e jogar do lado muitos aqui ó eu peguei o código do cliente tirou xavi
36:56
estrangeira e o código do produto também virou chave estrangeiro então a regra
37:01
para relacionamentos muitos para muitos é desmembrar esse relacionamento muito para muitos em vários relacionamentos de
37:08
um para muitos e com isso chegamos ao final dessa aula teórica você gostou eu espero que você tenha
37:13
gostado e espero que a forma de explicar tenha sido um pouco diferente do seu professor o que eu falei a mesma coisa
37:19
que um professor ficou chata pra mas eu tentei ilustrar tentei mostrar de forma prática de forma bem didática pra
37:25
você que aquele jeito que vocês gostam que eu faço sempre durante as nossas aulas mais uma vez eu venho pedir se você não
37:31
entendeu ou se ficou um pouquinho de dúvida assistir às aulas de novo antes de assistir à próxima aula
37:37
a 15ª aula do curso de banco de dados é exatamente a parte prática disso que eu falei então por exemplo se você não sabe
37:43
as regras de jogo da chave o que achava estrangeiros não sabe nem o que significa chave estrangeira pra que você vai seguir no curso porque
37:50
na próxima aula eu vou te mostrar como criar chaves estrangeiras e com isso criar relações entre tabelas
37:55
e fazer com que o dado funciona com o outro na 16ª aula nós vamos trabalhar jones
38:01
vamos trabalhar juntos ões um select com john lembro que você aprendeu o jovem tomou uma surra absurda é porque você
38:06
não tinha a classificação de relação que acaba que no seu curso o conceito de classificação de relação e o conceito de
38:13
joy estão muito distantes geralmente no início do curso você vê modelo relacional e lá no final do curso você
38:19
regiões e você não acaba não juntando eu vou dar um jovem bem pertinho do modelo relacional então você vai entender melhor acredita
38:26
em mim mas pra isso você precisa estudar e saber outra coisa que precisa fazer compartilhar isso tudo mostrar o maior
38:32
número de pessoas aqui agora tem uma mãozinha pensei que fosse digital já não há água que otão consegue fazer ó
38:38
primeiro se inscrever no canal se inscreva no canal é uma clique aqui sempre tivemos lá você vai ser avisado
38:43
se você marcar lá o mesmo assim na engrenagem você vai dizer ah quero
38:49
receber e meio desse canal que esse canal é bem legal nunca se esqueça também aqui você vê o curso completo aqui você vê todas as
38:56
aulas uma playlist completa e aqui no meio a experiência completa aqui é o curso em vídeo que a gente vai
39:01
poder ver todas as informações inclusive com esses links disponíveis nunca se esqueça também aqui em cima com
39:08
a interatividade você tem acesso ao que a gente julga eu e minha equipe jogamos como importante para você assistir essa aula e nunca se
39:14
esqueça pequeno gafanhoto estude bastante estude muito porque é só estudando que a gente consegue aprender
39:21
muita coisa e consegue evoluir na vida conta com a ajuda de vocês conta com a divulgação de você divulga esse vídeo
39:27
nas redes sociais essa ala ficou caprichada mostra para as pessoas queria agradecer queria mandar um grande
39:32
abraço para todos os professores não recebi muita foto de professores dando aula usando meus vídeos professores
39:39
dando aula usando meus slides eu fico muito feliz em poder ajudar você professor eu só peço que você mantenha a
39:45
fonte e mostra seus alunos que existe uma maneira de eles estudarem na sua própria casa no conforto do lar
39:51
é muito importante a sua aula mas é muito importante a minha também o seu trabalho é complementado pelo meu
39:57
o meu serviço é ajudar você sendo professor ou sendo aluno então é isso que o gafanhoto assistir a sala mais uma
40:03
vez você pode entender tudo bonitinho antes de partir para a 15ª ao ok combinado um forte abraço e até a
40:10
próxima então tem o cadastro gafanhotos e eu tenho cara
"""

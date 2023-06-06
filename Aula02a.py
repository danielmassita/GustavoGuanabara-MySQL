# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/instalando-o-mysql-com-wamp/
# https://youtu.be/5JbAOWJbgIA

"""
- Em 1994, Suécia, o Michael Widenius e o David Axmark resolveram criar um modelo gratuito de banco de dados relacional (MySQL), gratuito e aberto licença GPL.
- Nem tudo que é grátias é livre (open source).
- Em 2007 a Sun Microsystems comprou o MySQL. A Sun foi a empresa que criou a linguagem Java.
- Em 2009 a Sun Microsystems foi comprado pela Oracle. A Oracle, que já era uma gigante de dados, passou a ser também dona do MySQL. 
- Então, chateado, Michael Widenius saiu do MySQL e criou o MariaDB (fork do MySQL). 
- Empresas que usam o MySQL: Nasa, Google, Wikipedia, Adobe, Cisco, Ebay, Bradesco, Hostnet...

- MySQL possui todos os padrões: 1) Base de Dados, 2) Linguagem de Especificação, 3) Sistema Gerenciador, 4) Programas Adicionais

- Instruções do MySQL que se caracterizam como linguagens do tipo:
    DDL - Definição da Estrutura da BD
    DML - Manipulação (incluir, excluir, alterar)
    DQL - Solicitações (SELECT, solicitações)
    DCL - Controle (quais usuários podem acessar e etc)
    DDL - Transação (solicitação feita ao BD executados da melhor maneira seguinda as Características de Transação DICA (Durabilidade, Isolamento, Consistência e Atomicidade))

- Instalação dos Programas

    Microsoft .NET Framework 4.5 [ https://www.microsoft.com/en-us/download/details.aspx?id=30653 ]
    Visual C++ Redistr. for Visual 2019 [ https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022 ]
    MySQL Workbench [ https://dev.mysql.com/downloads/workbench/ ]
    Wamp Server [ Apache, PHP, MySQL ]
    MySQL 
"""

"""
Transcrição


0:19
Olá, pequeno gafanhoto! Seja bem-vindo a mais uma aula do seu curso de Banco de Dados
0:24
O meu nome é Gustavo Guanabara, eu sou seu professor
0:27
E chegamos a mais uma aula de Banco de Dados e dessa vez a gente vai começar
0:31
Já falando sobre o MySQL, vamos iniciar no mundo do MySQL
0:36
Na primeira aula a gente vê um pouquinho de histórias sobre evolução
0:39
Do banco de dados, como surgiu o Banco de Dados
0:42
E agora a gente vai falar especificamente sobre o MySQL
0:45
Você já viu na aula passada
0:47
Se você não viu, nunca se esqueça, veja aqui em baixo playlist
0:50
Você vai direto pra lá e assiste a primeira aula
0:53
E não esquece dela não cara, "mas é história e eu não preciso saber"
0:56
Lá tem muita informação importante, eu falo sobre o Modelo Relacional
1:00
Eu falo sobre o MySQL, do porque que o MySQL é diferente do Oracle, por exemplo
1:04
Então essa primeira aula
1:05
Foi importante você não pode perdê-la, não pule aulas, elas foram preparadas
1:10
Especialmente pra você. E essa aula de MySQL a gente vai começar vendo como ele surgiu
1:15
Como foi que começou o projeto do MySQL
1:18
Tudo surgiu em 1994, na Suécia
1:22
E você pensava que tudo é criado nos Estados Unidos
1:25
Cara, presta atenção, nós estamos num mundo globalizado, a maioria das coisas que
1:30
Você conhece e que você usa, como WhatsApp, o Waze
1:34
O Linux, nada disso foi criado nos Estados Unidos então da uma estudada meu querido
1:38
Da uma olhadinha porque tem muita coisa legal que foi criada inclusive no Brasil
1:42
Então como eu disse, em 1994 na Suécia, dois programadores
1:47
O Primeiro, Michael Widenius que é mais conhecido pela galera da comunidade como Monty e também
1:53
O Daivid Axmark
1:55
*Dialeto Desconhecido* ("arkaiks Marqss")
1:57
Então o Michael e o Daivid, resolveram criar um modelo gratuito
2:03
A ideia era criar um Banco de Dados gratuito, baseado no modelo Relacional
2:08
Surge então o MySQL
2:10
Então era um projeto de programadores dentro de comunidades
2:13
Foi criado o projeto e o MySQL ganhou notoriedade por ser simples, por ser gratuito,
2:20
Por ser baseado no Modelo Relacional
2:22
Compatível com SQL e tudo mais e além de grátis
2:26
O projeto era totalmente livre, tanto que logo de cara foi registrado como GPL
2:31
A GENERAL PUBLIC LICENSE é uma licença de software livre
2:34
é então que se você estudou um pouquinho de LINUX você sabe que
2:37
deixa o software livre isso é: você pode mexer no código fonte você pode
2:41
estudar você pode redistribuir
2:43
você pode gerar
2:43
redistribuições, forks, e tudo mais então mais do que grátis o MySQL
2:49
é livre
2:50
tem muita coisa que é grátis mas não é livre, você pode usar
2:54
gratuitamente mas não vai mexer no código
2:56
o MySQL ele é livre então ele grátis
2:59
e aberto ele é OPEN SOURCE então eu disse várias vezes que o projeto surgiu
3:03
em 1994
3:04
e foi se consolidando
3:06
no decorrer dos anos
3:07
até que se tornou um dos maiores bancos de dados e ai
3:11
veio uma empresa
3:12
com muito dinheiro em 2007 e comprou o MySQL
3:16
Essa empresa é a nossa conhecida Sun Micro Systems
3:19
e se você se lembra ele fez o curso de java com a gente a Sun
3:23
foi a empresa que criou, a empresa onde nasceu a linguagem java
3:27
então a Sun em 2007
3:29
comprou
3:30
o grupo MySQL.
3:31
E aí a partir desse momento o MySQL passou a ser de uma empresa.
3:35
Mas não pense seguinte ah não, ele vai ser de uma empresa ele vai ser pago, não ele continua sendo
3:39
gratuito e teve uma opção
3:42
produto pago acontece que se você assistiu o curso de Java você já sabe a
3:46
a Sun foi comprada
3:48
então em 2007 a Sun comprou a MySQL
3:50
em 2009 ela foi comprada
3:53
A Sun deixou de existir e agora pertence a Oracle.
3:56
Então olha só presta atenção:
3:58
O Java foi criado na Sun, aí a Oracle comprou a Sun, então veio o Java junto
4:04
o MySQL foi comprado pela Sun em 2007
4:07
2007 o MySQL passou a ser da Sun
4:11
e em 2009
4:12
ele deixou de ser da Sun e passou a ser da Oracle
4:15
então a Oracle que é uma das maiores produtoras de banco de dados
4:18
Banco de Dados pago!
4:19
Um dos mais famosos, agora também é a dona do MySQL
4:23
e isso deixou o Monty um pouquinho chateado
4:26
Por conta disso
4:27
Michael Widenius saiu do projeto do MySQL e criou, como eu disse na aula anterior,
4:31
o projeto MariaDB
4:33
O projeto MariaDB
4:34
é um fork do MySQL, então presta atenção, raciocina comigo:
4:37
O MySQL ele é grátis e ele é livre
4:40
então ele é OPEN SOURCE ele deixa o código livre pra qualquer pessoa mexer
4:44
O Widenius o dono, o Monty, pegou aquele código fonte que é
4:48
OPEN SOUCE
4:49
e criou um fork, criou
4:51
uma versão que agora vai caminhar separadamente do MySQL
4:55
que é o MariaDB
4:56
O MariaDB também está ganhando parte do mercado
4:59
mas ele ainda não evoluiu tanto as ferramentas não evoluíram tanto
5:02
quanto o MySQL
5:03
tem hoje no mercado
5:05
Então, por isso eu
5:06
optei pelo MySQL e não pelo MariaDB
5:08
Mas saiba que o MariaDB é uma ótima solução, mas eu só optei por uma coisa
5:13
mais consolidada no mercado
5:14
do que uma coisa muito mais recente, e o MySQL é tão famoso que várias
5:18
empresas no mundo utilizam ele, alguns exemplos que eu posso dar são: a NASA
5:23
o Google
5:24
o Wikipedia
5:26
a Adobe
5:27
a Cisco, o Ebay
5:29
todas as empresas de telecomunicação
5:32
Bradesco
5:33
as forças armadas
5:35
representadas aqui pela aeronáutica
5:37
e a HOSTNET
5:38
A HOSTNET a nossa eterna patrocinadora do curso em vídeo utiliza MySQL
5:42
nas suas entranhas, a HOSTNET já tem uma opção
5:44
do MySQL e do MariaDB mas basicamente aqui dentro da empresa a gente utiliza
5:48
bastante MySQL, então é isso cara, não tem desculpa pra você não
5:52
aprender o MySQL
5:53
não tem desculpa para você falar assim "Ha não, mas é que é de graça"
5:55
ele é livre meu querido, ele é mais do que grátis, ele é livre
5:59
aí você pode estar se perguntando "mas Guanabara,
6:01
então o MySQL segue
6:02
todos aqueles padrões lá que você falou na aula anterior
6:05
que precisa ter quatro coisas:
6:07
precisa ter a base de dados
6:08
uma linguagem de especificação o sistema gerenciador e programas adicionais?"
6:13
O MySQL tem isso tudo o MySQL, ele tem uma linguagem tão potente que
6:17
ela tem comandos específicos
6:19
pra determinadas situações
6:21
vamos ver aqui, por definição o MySQL possui dentro dele algumas
6:25
instruções que se caracterizam como linguagens do tipo, por exemplo:
6:29
DDL que é uma linguagem de definição
6:31
na linguagem DDL você vai definir você pode por exemplo criar um banco de
6:35
dados, criar uma tabela, alterar esse banco de dados
6:39
qualquer comando de definição da estrutura da base de dados
6:42
e mantida dentro do MYSQL pela porção DDL dele, existe também a
6:47
posição DML que é de manipulação então você vai poder incluir novos
6:51
dados, excluír dados, manipular dados de qualquer maneira, alterar
6:55
a composição deles, então a
6:58
definição define a estrutura e a manipulação
7:01
manipula os dados. Além disso nós temos uma porção DQL que é de
7:05
solicitações
7:06
você vai pode fazer um select do seu poder um famigerado select
7:10
faz parte da porção DQL do MYSQL, então qualquer solicitação
7:13
que você vai precisar
7:15
a DQL vai te atender. Nos temos também uma porção DCL que é de
7:18
controle onde você pode definir aí que usuários podem acessar seu banco, que
7:22
tipo de acesso ele vai poder fazer, que tipo de comandos ele vai poder executar
7:26
e muito mais e por fim
7:28
nós temos a porção DTL que trata das transações
7:32
transação
7:33
é qualquer solicitação que pode ser feita a um banco de dados e ele vai te atender
7:37
da melhor maneira possível seguindo os quatro princípios que a gente chama de
7:41
dica que é (D.I.C.A)
7:43
que é: Durabilidade
7:45
Isolamento
7:46
Consistência e atonicidade
7:48
Então se você de estudo na faculdade ou fez algum curso ou estudou
7:52
segundo grau
7:53
as características
7:54
de uma boa transação são:
7:56
durabilidade, isolamento, consistência e
8:00
atonicidade, então dá uma olhada nisso daí basicamente diz o seguinte:
8:05
Durabilidade: todo dado que é colocado ou alterado ou manipulado tem que
8:10
permanecer duravel tem que permanecer dessa maneira
8:13
enquanto eu quiser que ele esteja lá.O isolamento diz o seguinte: Se eu tenho duas
8:17
transações feitas ao mesmo tempo elas têm que ser executadas sem uma
8:20
interferir na outra, precisa que ser isoladas
8:23
A consistência é o seguinte:
8:24
Toda transação tem que levar o banco de dados de um estado consistente a outro
8:29
consistente
8:30
se tudo estava ok antes, tudo tem continuar ok
8:33
e atonicidade
8:34
trata exatamente disso: toda transação tem que ser atonica ou
8:37
toda ela acontece ou nada acontece ou
8:40
tudo dar certo ou ele dá um ctrl + z, que é o retorno pra um estado
8:44
anteriormente consistente
8:47
O MYSQL é compatível com tudo isso que eu tô falando, tudo que você
8:50
estudou na teoria de banco de dados o MySQL
8:54
é totalmente capaz de executar
8:56
Mas por fim, como é que a gente vai trazer isso pro meu computador? Você pode
9:00
estar se perguntando
9:00
"Caramba o MYSQL é potente, ele precisa, ele roda em um servidor?"
9:03
Sim, ele roda em um servidor, "então tem que ter um servidor em casa?" É mais ou menos por aí
9:08
mas eu vou te mostrar como você faz a instalação diretamente no seu Windows
9:11
Sem complicação nenhuma, para instalar o MySQL no seu computador
9:15
você vai precisar do seguinte: Nós vamos utilizar no Windows, assim, eu exemplifico sempre
9:19
no Windows porque a maioria dos gafanhotos utilizam Windows
9:24
Mas se você é um gafanhoto que utiliza Linux ou utiliza MAC como eu utilizo MAC aqui
9:28
dá uma pesquisada aí na internet que você vai ver
9:30
como é que você faz para o MySQL funcionar dentro do seu ambiente.
9:33
Eu vou exemplificar aqui
9:35
num ambiente só por questões de praticidade pra gente pode ganhar
9:38
tempo aqui
9:39
No Windows eu vou instalar um conjunto, um pacote chamado WampServer
9:43
Esse WampServer ele vai utilizar
9:45
o MYSQL junto com o PHP então eu já tô pensando no futuro eu não vou
9:50
instalar o MYSQL separadamente na minha máquina, eu vou utilizar o WampServer porque
9:54
mais para frente você vai precisar o unificar tudo isso no PHP
9:58
e esse pacote vai te atender muito melhor
10:00
e por fim
10:01
nós vamos instalar uma ferramenta chamada MySQL Workbench
10:05
O Workbench ele vai fazer o seguinte: Ele vai permitir que eu digite os comandos
10:09
MySQL
10:09
de uma maneira mais amigável, vamos dizer assim, de uma maneira mais cômoda sem
10:14
utilizar o terminal
10:15
Hoje eu vou mostra como é que usa o terminal
10:17
e eu vou te mostrar qual a diferença com Workbench. Então é isso meu querido
10:20
arregace suas mangas, abra o seu sistema operacional,
10:24
faça os download que eu vou precisar, eu nunca vou cansar de te dizer isso meu
10:28
querido
10:28
não adianta você assistir nenhum curso do Curso em Video, na verdade nenhum curso da sua
10:33
vida sem praticar, não adianta você botar a mão
10:37
tem gente que fica assim: Bota a mão no queixo
10:39
e fica assistindo vídeo, assistindo vídeo, assistindo vídeo... 40 minutos de vídeo aí depois ele acha
10:44
o ser humano acha que ele já sabe
10:47
e ele nunca praticou
10:48
ele só vai perceber que ele não aprendeu
10:50
quando ele for tentar fazer
10:51
Então vai por mim meu querido gafanhoto: Use
10:53
o pause, use muito pause, play, pause, play, pause, play... Pausa,
10:58
faz no seu,
10:59
vê funcionando,
11:00
retorna, a aula vai durar mais tempo assim?
11:03
Vai durar mais tempo, mas você tem uma semana para poder praticar tudo isso
11:06
o cara assiste a aula em, sei lá, 40 minutos
11:09
e reclama "Ai cadê a próxima?". Não é assim que funciona meu querido
11:12
estuda, pratica
11:14
então eu já tô aqui num ambiente
11:16
com Windows
11:17
exemplificando aqui no Windows 10 que a última versão mas você pode
11:21
instalar esses programas em qualquer versão, se você tem o Windows 7, Windows 8
11:25
pode instalar sem problema nenhum
11:27
eu vou abrir aqui o EDGE , abra o seu navegador preferido, no caso aqui
11:31
o Windows ele tá limpo, ele esta sem programa nenhum instalado
11:34
e a primeira coisa que nós vamos fazer
11:35
é acessar o site do MYSQL
11:39
www.mysql.com
11:40
no site do MySQL
11:42
nós vamos acessar a developer zone a zonas de desenvolvedores
11:47
a developer zone aqui do lado esquerdo
11:49
nós vamos entrar na parte do MySQL downloads
11:52
e na parte do MySQL downloads nós vamos entrar no MySQL Workbench
11:56
que é a ferramenta que eu falei para vocês para gente acessa
11:59
o Workbench não é o MySQL, ele uma ferramenta para acessar o
12:03
ambiente MYSQL
12:05
ficou claro
12:06
mais para frente a gente vai instalar o MySQL na nossa maquina, na verdade não vamos instalar o
12:09
MySQL, vamos instalar o pacote WampServer que eu já expliquei
12:13
você ta sacando
12:14
primeira coisa que você tem que perceber é que existem
12:17
pré requisitos pra você pode instalar o Workbench, a primeira coisa
12:21
é instalar o Microsoft .NET Framework 4 Client Profile
12:24
e depois Visual C++ Redistributable
12:27
for Visual Studio 2013 , vou fazer o seguinte vou segura o CTRL
12:31
vou clicar no primeiro segurando CTRL e cliquei no segundo e vai abrir duas janelas
12:35
aqui em cima
12:37
e abaixando
12:38
framework 4
12:40
Client Profile
12:42
então vou escolher aqui o idioma
12:43
tem português brasil
12:45
vou clicar em download
12:46
aguardar alguns segundos
12:48
e o download
12:49
já vai ser iniciado, tá aqui ó, é bem rapidinho
12:53
ta baixando e já baixou
12:54
já vou executa ele
12:56
esses são pré-requisitos
12:58
para rodar o Workbench
12:59
então você tem que instalar esses dois já instalamos aqui já só
13:03
avançar, avançar, avançar, avançar...
13:04
instalamos
13:05
o .Net Framework
13:07
agora vamos para o segundo passo: Vou fechar essa janela
13:10
vamos ao C++
13:12
Redistributable
13:13
Packages
13:15
não têm português brasil, então eu vou baixar em inglês mesmo
13:18
download
13:20
ele vai me perguntar: Qual é a versão que eu quero?
13:23
essa aqui é para processadores a arm
13:25
para processadores
13:27
x64 e x86
13:29
x86 se seu processador for 32 bits
13:32
x64 se seu processador for 64 bits
13:34
vou marcar aqui que eu quero a versão 64 bits
13:37
vou clicar em next
13:40
mais uma vez
13:42
vai fazer o download
13:43
bem rapidinha aqui, esse aqui é um pouquinho maior
13:46
mas não vai levar muito tempo
13:48
colocando aqui ó terminou
13:51
vamos executar mais uma vez
13:53
aceita licença
13:55
e assim: avança, avança, avança... e conclui
13:59
instalação de programas no Windows não tem muito o que falar, você vai ter que
14:02
instalar
14:03
essas duas bibliotecas
14:04
então: Está dizendo aqui que foi instalado com sucesso
14:07
cliquei em close posso fechar aqui e voltar para o meu download do MySQL
14:12
então já instalei os meus dois pré-requisitos, agora vamos lá embaixo
14:16
e vamos escolher
14:18
qual é a versão do Workbench que a gente quer
14:20
então ele da a opção aqui do Linux,
14:22
do Windows, do Red Hat, do Fedora, Mac OS
14:26
ou código-fonte. Vamos baixar aqui a versão para windows
14:29
32 bits
14:32
vou procurar a versão 64 com instalador aqui, download dela, ele vai me perguntar
14:37
se você quer fazer login, eu vou colocar aqui: No thanks, just start
14:41
my download
14:41
para ele começar a baixar
14:45
esse daqui vai demorar
14:47
um pouquinho mais
14:48
ele vai baixar o arquivo
14:49
.msi que é o pacote de instalação
14:52
sem mistério,
14:53
sem novidade, a instalação de pacotes e bem simples, vou aguardar um pouquinho
14:58
para terminar o meu download
14:59
e vou continuar a instalação
15:01
iniciando aqui a instalação
15:02
Estou na versão 6.3 que eu baixei no site
15:05
avançar, pode ser que a versão seja mais nova
15:08
fazer a instalação completa aqui
15:10
instal, esta todas as
15:12
autorizações que precisar e a instalação vai continuar
15:16
é importante dizer o seguinte: Você só vai conseguir instalar Workbench se você
15:20
tiver instalado aqueles dois pacotes antes
15:23
não pule passos
15:24
porque se não você não vai conseguir. Terminada a instalação, ta aqui, ele vai lançar
15:28
o MySQL Workbench now, pode deixar ele abrir
15:31
na verdade ele não tem MySQL ainda, mas
15:33
tá lá, então ele
15:34
colocou
15:35
o Workbench aqui
15:36
eu vou minimizar
15:38
e nós vamos partir para o segundo passo
15:40
que é a instalação
15:42
do pacote o wamp
15:44
então nós vamos digitar aqui
15:45
www.
15:47
wampserver
15:49
.com
15:50
e ele vai entrar aqui nesse site, que esta
15:54
em francês, vamos transformar ele para inglês
15:57
esta em inglês, vamos clicar em download
16:00
aqui você vai ter a opção de baixa 32 ou 64 bits, vou baixar aqui em 64
16:06
e ele vai te dizer que existe um pré-requisito
16:09
que é o Visual Studio... redistribuição, basicamente
16:13
você acabou de instalar a versão 2013, ele está pedindo a versão 2012
16:17
eu vou te dizer o seguinte: Em alguns computadores pode funcionar somente
16:21
a 2013
16:22
em alguns outros pode precisar da 2012, então fique atento a isso
16:25
se por acaso a gente instalar agora e der erro a gente baixa versão 2012, se não
16:29
der erro a gente continua funcionando sem problema nenhum, então eu não vou
16:33
baixar esse aqui, eu vou abrir esse site só por desencargo de
16:35
conciência, eu vou deixar ele aberto aqui, uma vez que você tenha entrado nessa tela
16:40
pode clicar aqui no download e o download e vai ser iniciado, aguarde
16:44
o download
16:45
e depois é só instalar
16:47
vou abrir aqui a instalação
16:48
autorizar
16:50
esta dizendo lá
16:51
já tá instalando,o Wampserver é 2.5
16:55
vamos avançar
16:56
aceitar aqui o
16:58
contrato, ele vai instalar em C:/wamp, mantenha essa pasta
17:03
e vamos avançar, avançar, avançar..., e instalar
17:06
a instalação também vai levar alguns segundos
17:08
vai demorar um pouquinho porque o Wampserver como a própria sigla
17:11
diz no Windows: Ele instala o Apache
17:14
o php
17:16
e o MySQL, então
17:17
ele esta instalando essa quantidade grande de programas
17:20
e você vai precisar talvez de uma biblioteca
17:23
a gente já deixou alí reservado, se o seu
17:25
der erro, você vá lá embaixo, eu não sei se o meu vai dar erro aqui, se der
17:28
eu vou lá, baixo, instalo
17:30
e mais tarde coloco para funcionar, aqui no meio ele..
17:32
deu uma mensagem
17:33
perguntado se você quer instalar o novo Wampserver homepage, diz que sim e vai..
17:38
aqui ele deu erro, o programa não pode ser iniciado porque não têm
17:42
a biblioteca no computador, estão ele já
17:44
me deu aqui o erro e eu precisam realmente
17:47
baixar a versão
17:48
2012 do C++ aqui
17:51
Para fazer isso vamos abrir
17:53
aquele link que a gente abriu anteriormente, não tem português,
17:56
vamos clicar em download, vou escolher aqui a versão 64 bits
18:01
a primeira aqui
18:03
clicar em next
18:05
então o download vai começar rapidinho
18:06
feito download
18:08
vamos executar
18:09
aceitar
18:10
instalar
18:12
autoriza tudo
18:14
ele vai instalar a runtime aqui
18:16
e pronto
18:18
agora já está tudo
18:21
bonitinho
18:22
o Wampserver vai me pedir aqui as configurações de servidor, é só avançar
18:27
e finalizar
18:28
ele vai solicitar aqui a autorização para abrir o Wampserver e
18:32
nota aqui em baixo, tem um W vermelho
18:35
quando ele ficar verde, como acabou de ficar
18:37
ele já está funcionando
18:39
sem problema nenhum
18:40
então recapitulando, a gente instalou as duas biblioteca necessárias para o Workbench,
18:44
instalou o Workbench, depois baixamos o Wampserver, baixamos uma
18:48
biblioteca adicional, no meu caso aqui foi necessário, se no seu caso não for
18:52
não precisa, mas
18:53
fica de olho aí, já abre o link
18:55
para não ter problema
18:56
então nós já estamos com o Workbench,
18:58
três bibliotecas instaladas,
19:00
e o Wampserver. Vamos fazer isso tudo funcionar junto agora, mas antes vamos testar se o meu
19:04
servidor MySQL está ativo
19:06
sempre que o seu W estiver verde
19:09
se você olhar aqui o W está verde, ele está
19:12
funcionando corretamente, para testar se o MySQL está funcionando
19:15
vamos
19:16
abrir
19:17
o Wampserver clicando sobre o W verde, clicar sobre o MySQL e
19:22
clicar em MySQL console, para ver se o console está funcionando
19:26
ele vai pedir uma senha
19:28
o ambiente do MySQL
19:30
tem um usuário chamado root (r.o.o.t)
19:33
e a senha
19:33
para o caso do Wampserver é uma senha vazia
19:37
então basta você pressionar enter
19:38
se você tá utilizando outro ambiente
19:40
verifique qual é a senha do seu servidor MySQL
19:43
no caso do Wampserver se você está seguindo o que eu tô fazendo
19:45
a senha é vazia
19:46
então basta dar enter
19:47
então eu vou dar enter aqui, pressionando enter ele já botou o prompt aqui do MySQL
19:52
para mim
19:52
para testar o status do sistema basta digitar: status
19:57
se ele esta mostrando informação
19:59
é sinal de que ele tá funcionando sem problema nenhum. Agora chegou a hora de
20:04
a gente ir para o Workbench, se não a gente vai ter que trabalhar diretamente nesse terminal
20:07
então a gente tem que ficar dando comandos
20:09
na tela preta, então
20:10
o Workbench torna isso mais bonitinho, nada impede de você pegar todos os
20:14
comandos que a gente vai aprendem nas aulas
20:16
daqui pra frente
20:17
e digitar diretamente no terminal, colocar no terminal
20:20
a gente vai utilizar uma ferramenta
20:22
para ficar mais bonitinho, mais agradável o aprendizado, não só bonito
20:26
agradável e mais útil, então eu vou abrir aqui
20:29
o Workbench
20:29
que já vai ter reconhecido uma instância local
20:33
aqui: localhost3306
20:35
e usuário: root
20:37
clicando
20:38
sobre esse servidor
20:40
ele vai abrir
20:41
e ele acabou de abrir aqui o Workbench. Basicamente essa tela vai
20:46
pode ficar um pouquinho diferente dentro do seu ambiente, porque aqui já é
20:49
um ambiente que eu já tenho inclusive no meu Mac, mas
20:52
você vai ver que
20:54
a gente vai aprender a utilizar
20:55
essa ferramenta
20:56
da maneira mais completa possível
20:59
e você vê que ela é um pouquinho mais agradável aos olhos,
21:03
interfaces, janelinha, tudo mais
21:05
pode ser feito
21:06
só com um clique, não vou recomendar, a gente vai aprender
21:09
a utilizar comandos
21:11
estão é isso meu querido, instalamos todos os programas que a gente precisa pra poder
21:15
trabalhar com MySQL, na próxima aula a gente vai aprender a criar o
21:18
nosso primeiro banco, na terceira aula do Curso em Vídeo de banco de dados você já
21:22
vai criar o seu primeiro banco de dados com uma tabelinha bem simples e tudo
21:25
mais
21:26
para a gente poder
21:26
aprender como utilizar
21:28
o MySQL
21:29
através de linhas de comando. Estão é isso meu querido
21:32
como sempre a gente tem aquele script no final onde eu sempre agradeço
21:36
peço para que você me der a honra de ser um inscrito
21:39
para isso, você clica aqui ó
21:41
clicando nesse botão você vai se inscrever no canal
21:44
sempre que tiver um vídeo novo você vai ser avisado. Do lado do inscrever
21:48
clica na engrenagem que aparece no youtube e clica em: Quero receber e-mails desse canal
21:53
"esse canal é muito legal,
21:55
esse canal é batuta", então coloca lá, se inscreve
21:59
pede pra receber e-mail, porque sempre que tiver uma aula nova
22:02
você vai ser avisado. A gente aqui no curso em vídeo
22:04
só trabalha com vídeos de qualidade
22:07
clicando aqui você vai ter acesso a playlist.
22:09
Mais uma vez eu te peço não pule a primeira aula
22:12
tem gente que gosta de pular primeira aula porque acha que é só
22:14
a coisa prática e tudo mais
22:16
aprenda um pouquinho mais sobre banco de dados
22:18
abra sua mente e você vai aprender muito mais sobre essa teoria de banco de dados
22:23
Isso eu garanto. Aqui no meio a experiência completa
22:27
Tudo que a gente preparou, os links para baixar esse pacotes
22:30
links alternativos
22:32
todas as informações estão no cursoemvideo.com
22:35
você vai poder baixar todos os pacotes e ser feliz!
22:38
um forte abraço meu querido
22:40
pratique sempre, instale seu ambiente, porque na próxima aula
22:44
a gente vai cair dentro
22:45
e vai criar nosso primeiro banco de dados
22:47
um forte abraço e até a próxima!
23:07
cara, esse martelo vai ser chato!
23:17
Olá, pequeno ga...
23:21
[suspiro]
23:23
vamos tentar ignorar
23:25
Olá, pequeno gafanhoto, seja-bem..[sons com boca]
23:30
Olá pequeno gafanhoto seja bem-vindo a mais um episódio do seu ...[careta]
"""

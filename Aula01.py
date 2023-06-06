# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/o-que-e-um-banco-de-dados/
# https://youtu.be/Ofktsne-utM

"""
Transcrição


0:00
♫ Cantarolando ♫
0:10
♫ Bateria tocando ♫
0:19
Olá, pequeno gafanhoto!
0:21
Há quanto tempo!
0:22
Estava com saudades de mim?
0:23
E ai, como é que foram as férias?
0:25
Eu espero que você tenha aproveitado.
0:27
Porque, a partir de agora, oficialmente
0:29
começa o seu curso de banco de dados
0:33
com MySQL, aqui do Curso em Video.
0:35
e claro você já viu na descrição do video
0:37
você já recebeu o seu e-mail
0:39
você que é escrito no canal já recebeu o e-mail
0:41
então estamos aí bem vindo novamente ao curso em video
0:45
e esse é um dos videos que as pessoas pedem bastante
0:47
muita gente depois que eu fiz o curso de Algoritmo depois que eu coloquei o curso de PHP
0:51
muita gente fala assim
0:52
Guanabara mostra como é que é Banco de Dados para pode intregar com PHP
0:56
E esse é o primeiro passo que a gente ta dando nesse sentido
0:59
então meu querido coloca esse celular no silencioso!
1:01
fecha essa janela do facebook que eu estou vendo!
1:03
Tem outros sites (( ͡° ͜ʖ ͡°)) aí também aberto, pode fechar!
1:05
acomode-se na sua cadeira
1:07
e vamos começar
1:09
e como eu ja disse 1 milhão de vezes
1:11
nós vamos comecar agora o nosso curso em video de banco de dados
1:16
e aí, gostou da piada? Não!?
1:19
mas pode esperar que vai ter piada pior até o final
1:22
e nessa primeira aula como não poderia deixar de ser
1:24
nos vamos ver a Origem dos Bancos de Dados
1:27
Sim! Se você é um gafanhoto experiente aqui do curso em video
1:31
você já sabe que eu tenho esse problema, que eu não consigo começar nada sem contar suas origens
1:36
eu acho muito importante a gente conhecer a origem das coisas
1:40
para a gente pode entender até onde ela foi
1:43
e tambem para a gente comprender, que não para por aqui
1:45
O que eu vou falar de banco de dados hoje, pode ficar velho amanhã
1:48
então, vamos aproveitar logo pra você aprender tudo bonitinho, organizado nesse curso básico
1:53
para iniciantes, de Banco de Dados com MySQL
1:56
E eu vou começar como sempre voltando no tempo, pra década de 50
2:01
se você se lembra muito bem da sua aula de história da computação
2:04
se você teve no colégio, na faculdade, sei lá de qualquer lugar, todo mundo falou
2:09
os primeiros computadores eram universitários e militares
2:12
e surgiram ali na década de 40, mais ou menos 1945, 1946
2:16
foi o surgimento dos computadores pra uso militar e acadêmico
2:20
E eu não sei se você ja se perguntou.
2:22
Nessa época, como é que os dados eram guardados?
2:25
E eu lhe respondo.
2:26
Antes dos computadores, os dados eram guardados em papel
2:30
Sim! Papel.
2:31
As pessoas iam se cadastrar, e seus dados eram preenchidos em papel
2:35
que era a única maneira da época
2:37
e se você parar para pensar, até hoje em alguns lugares se faz isso
2:41
só que convenhamos, é um negócio muito velho
2:43
Nessa época a gente preenchia uma ficha
2:46
essa ficha preenchida era colocada dentro de uma pasta
2:50
e esta pasta era armazenada dentro de um arquivo metálico
2:53
Isso é uma coisa óbvia, isso é uma coisa que você provavelmente já viu
2:56
mas provavelmente os gafanhotos mais jovens sabem que existe, mas nunca viram acontecer
3:01
O fato é! Na década de 50, era a única maneira que se tinha, hoje em dia tem essa maneira e tem outras
3:07
mas na época, na década de 50 era a única maneira de se guardar dados
3:11
e seguindo essa mesma linha de raciocínio
3:13
a gente pode começar a ver algumas teorias de banco de dados
3:16
a partir dessa historinha que eu acabei de contar pra você
3:18
acontece, que esses três componentes que você está vendo ai na sua tela
3:21
a ficha, a pasta e o arquivo
3:24
tem nomes específicos na área da tecnologia da informação
3:27
As fichas, são tratadas como registros.
3:30
As pastas, como tabelas.
3:32
E os armários, como arquivos.
3:34
Então, apenas recapitulando
3:36
Os armários grandes, guardam pastas
3:38
essas pastas, guardam fichas.
3:40
Vamos trazer para área de TI
3:42
Arquivos, guardam tabelas
3:44
tabelas, armazenam registros.
3:46
Guarda isso! Isso vai ser muito importante quando a gente começar a ver o MySQL.
3:51
E eu não preciso nem dizer que antigamente na década de 50, com esse meio de armazenamento
3:56
de fichas guardadas em pastas e pastas guardadas em grandes armários
4:00
a gente tinha um acúmulo muito grande de papel
4:03
e o grande desafio do final da década de 50, e início da década de 60, foi digitalizar todos esses dados
4:08
Isso porque a computação já começou a ganhar o mundo das empresas
4:13
então, os computadores eram gigantes, universitários e militares
4:17
depois eles começaram a reduzir, e reduzir um pouquinho mais
4:20
e ai, eles começaram a ganhar empresas
4:23
e ai, se tornou necessário guardar essa massa de dados de forma digital
4:27
mas calma que não foi tudo muito bonito logo de cara surgiram banco de dados não
4:31
logo no início, as fichas, os registros, eram armazenados de uma maneira bem arcaica
4:36
basicamente o que acontecia, era pegar uma ficha dessa de forma digital
4:40
e colocar uma após a outra, dentro de um arquivo sequêncial
4:44
isso porque, os arquivos antigamente, eram guardados em fitas magnéticas ou cartões perfurados
4:49
e esses meios de armazenamento eram sequênciais
4:52
para você ler um cartão perfurado, sei lá. O quinto!
4:55
Você tinha que ler o primeiro, segundo, terceiro, quarto e quinto. Até chegar no final.
4:58
As fitas de papel ou as fitas magnéticas funcionam da mesma maneira
5:02
para você ler o meio da fita, você tinha que rebobinar ela toda, e ir lendo até chegar no momento onde você quer
5:06
então, os arquivos iniciais não poderiam ser diferentes
5:09
basicamente se você quisesse encontrar um registro específico
5:13
você tinha que varrer do primeiro até o registro ser encontrado
5:17
e por conta dessa característica das sequências dos registros
5:20
esse tipo de arquivo tem um nome muito fácil de lembrar
5:23
esse tipo de armazenamento ficou conhecido como Arquivos Sequênciais
5:26
isso por que, como eu acabei de falar, os dados eram guardados numa sequência
5:30
e é claro que isso trazia uma lentidão muito grande.
5:32
Mas pare para pensar comigo.
5:33
Antes disso, o que que tinha?
5:35
Ficha de papel.
5:36
Agora estava digitalizado.
5:38
Então era melhor do que a gente tinha antes.
5:40
Nunca pense numa tecnologia, como arcaica, como velha, se ela é velha.
5:45
Então você vai pensar assim: "Nossa! Mas é muito ruim arquivo sequencial né?
5:49
Tá, mas era melhor do que tinha antes.
5:51
É por isso que eu gosto de contar a história das coisas.
5:54
O que a gente tem hoje, é melhor do que a gente tinha ontem.
5:57
e o que a gente vai ter amanhã com certeza vai ser melhor do que a gente tem hoje.
6:00
E como o amanhã é sempre melhor, depois das fitas surgiram o que?
6:05
Os discos: disquetes e HDs, o primeiro winchester (que na época tinha esse nome)
6:10
e esses tipos de mecanismos armazenavam dados de maneira direta, não de maneira sequencial
6:15
Num disco, você não precisa ler o início do disco para ler a metade dele
6:18
Você pode ir direto para um lugar
6:20
e os arquivos também evoluíram para isso
6:22
Nesses mecanismos de armazenamento era possível guardar todos os registros
6:26
e manter dentro de uma espécie de tabela, índices, numerações,
6:30
guardar chaves identificadoras de cada um dos registros.
6:34
Isso a gente chama de: "índice"
6:36
E a partir do momento em que os registros são armazenados num meio de armazenamento
6:40
direto e indexado, a forma de encontrar os dados se tornou muito mais rápida.
6:44
Vamos imaginar aqui que eu estivesse procurando pelo registro 5, por exemplo.
6:48
Como tudo estava armazenado num meio direto, bastava você ir diretamente até o registro...
6:53
pega-lo, e tratar os seus dados da maneira que quiser.
6:56
Esses tipos de arquivos ganharam o nome de: "arquivos de acesso direto"
7:00
Viu como é simples?
7:01
Até a nomenclatura é fácil.
7:03
Arquivos de Acesso Sequencial - são aqueles onde os registros são acessados sequencialmente.
7:08
Arquivos de Acesso Direto - são arquivos onde os registros são armazenados e acessados de maneira direta
7:14
Simples assim!
7:15
Mas ainda que os arquivos de acesso direto fossem muito melhores que os sequenciais
7:19
a gente ainda tinha um problema, porque esse índice era muito simplista, era muito simples.
7:24
E aí, na década de 60, surgiu um momento muito importante para a história dos bancos de dados.
7:29
E foi exatamente na década de 60, que o departamento de defesa dos Estados Unidos
7:35
arregaçou as mangas e começou a trabalhar.
7:37
Sim! O departamento de defesa dos Estados Unidos
7:40
tinha como uma das tarefas criar uma maneira de armazenar dados de maneira mais segura e inteligente.
7:46
E você pode estar achando estranho: "Caramba! O departamento de defesa se metendo nisso."
7:50
Se você parar para pensar na história da tecnologia, nessa época: década de 50, 60, 70
7:56
a pesquisa militar era algo muito importante e muito valioso para a história da humanidade
8:01
E com a tecnologia não poderia ser diferente.
8:03
O departamento de defesa dos Estados Unidos criou um evento que tinha um nome específico:
8:07
O CODASYL.
8:08
O CODASYL foi um grande encontro que reuniu: militares, empresas e universidades.
8:14
Lá! Foram discutidas grandes tecnologias emergentes, coisas que poderiam ser criadas
8:19
e dessa conversa, entre as empresas, os militares e o governo
8:22
surgiu uma das linguagens mais valiosas da história.
8:26
Foi no CODASYL que surgil o: "COBOL".
8:29
Sim! Não sei se você já ouviu falar nessa linguagem, mas ela é muito importante,
8:33
porque ele foi a primeira linguagem que se preocupou efetivamente tanto com a lógica da programação
8:38
como com os dados embedados nela.
8:41
Então, a estrutura de dados era primordial pro COBOL.
8:45
Inclusive grandes empresas ainda usam o COBOL até hoje.
8:49
É claro que muitas delas estão migrando, mas existem ainda... nós estamos em 2016... que eu tô gravando este vídeo
8:55
existem empresas que ainda utilizam o COBOL.
8:57
Os programadores COBOL são contratados a peso de ouro.
9:01
Não tô falando aqui para você, pequeno gafanhoto, hoje com 15, 16, 20 anos, começar a aprender COBOL
9:06
eu simplesmente estou dando uma informação.
9:08
Em momento nenhum eu quero incentivar aqui o aprendizado de uma linguagem que começou
9:12
na década de 60 e não evoluiu.
9:14
Não existem versões novas do COBOL.
9:16
Versões atualizadas. Simplesmente, quem sabe COBOL, quem já sabe COBOL, sabe COBOL.
9:22
Então, tá ganhando uma graninha extra com a migração ou com a atualização deste sistema.
9:27
Porque não existe mais programador para isto. Quer dizer, existe sim. Só que são poucos.
9:31
E além do COBOL, no CODASYL foi discutido o surgimento de uma nova tecnologia.
9:36
Essa tecnologia ganhou logo um nome, Banco de Dados.
9:40
Esse é o objetivo do nosso curso, a gente vai aprender como criar Banco de Dados.
9:45
E claro! que esse curso é um curso para iniciante. Você vai precisa estudar mais?
9:49
E óbvio! todo curso do curso em vídeo é isso, a gente não tenta de maneira alguma ser total ser completo.
9:55
(ironia) Curso completo para você ganha. Não!
9:58
O curso em vídeo tem uma ideia de uma maneira
10:01
descontraída, de uma maneira pedagógica, séria e comprometida.
10:05
Mostrar para vocês o inicio. E você pede ter certeza, quantos curso de Bancos de Dados
10:09
que você fez pela internet mostra esses dados que eu estou mostrando aqui.
10:13
Acredita na gente pequeno gafanhoto, o curso em vídeo vai trazer muita coisa boa para você.
10:17
E num modelo criado na década de 60, o Banco de Dados, até hoje, é composto de quatro partes:
10:23
A base de dados, que são os dados propriamente ditos né, a estrutura de todo banco de dados
10:29
que está no baco de dados, obviamente se o banco de dados não guardasse dados não seria banco de dados.
10:32
☆☆☆(✲✪‿✪)ﾉ☆☆
10:34
Pra que, que eu perco tempo falando isso.
10:35
Só que não por aí, além da base de dados, a gente também tem um sistema gerenciador.
10:40
Você já deve ter ouvido falar no seu colégio ou na sua faculdade da sigla SGBD, que e uma sigla em português
10:47
para Sistema Gerenciador de Banco de Dados, em inglês essa sigla e DMS se você começa a procura ai
10:52
procura pela sigla DMS, que e a mesma coisa para nossa sigla em português para SGBD.
10:57
Então, além dos dados um banco de dados tem que ter um Sistema Gerenciador. Dentro da estrutura, dentro
11:04
de todo ecossistema que constrói um banco de dados, a gente tem que ter um sistema que gerencie esses dados.
11:10
Além da base de dados e do sistema gerenciador, também e necessário ter uma linguagem de exploração.
11:15
Ai você pode está perguntando. Caramba, quem acessa o banco de dados não e a linguagem de programação?
11:20
Então porque tem que ter uma linguagem de exploração?
11:22
Aí que vem a chave, você não precisa ficar aprendendo um milhão de linguagem, você, na teoria criada pela
11:28
CODASYL, você precisaria aprender uma única linguagem, que a linguagem de acesso aos dados
11:33
que e uma linguagem de exploração, isso foi muito valioso esse extra para os estudos que deram origem
11:40
ao Banco de Dados.
11:41
E, por último você teria também programas adicionais.
11:45
Coisas adicionais como, gerencia de usuários com atomizadores de dados
11:50
então tudo que tiver extra o banco de dados também vai conter.
11:53
Então esse e o princípio do banco de dados, surgiu na década de 60 junto ao CODASYL.
11:58
Aí teve uma empresa que foi muito importante nos estudos de tudo isso aqui.
12:02
Talvez você tenha ouvido falar nela.
12:03
Além do departamento de defesa dos Estados Unidos.
12:06
A IBM foi muito valiosa para construção e evolução dos bancos de dados
12:11
E se você não ouvi falar na IBM? Dá uma pesquisada aí.
12:14
Ela surgiu muito antes com Herman Hollerith.
12:16
E deu a maior...Uma das maiores empresas de tecnologias no mundo.
12:21
A IBM foi a criou o PC, por exemplo.
12:24
Ele é muito mais do que isso, hoje ela nem é tão mais falada.
12:28
E como se fosse, é na época do inicio, quando eu comecei a estudar.
12:31
IBM, era como se hoje eu falasse pequeno gafanhoto, o Google!
12:35
Caramba, o Google? [Expressão de espanto]
12:36
A IBM tem grande valor na área de tecnologia.
12:39
Hoje em dia ela ainda existe, mas se voltou para outros ramos, ainda continua grande.
12:43
Mas não é gigantesca, não é tão famosa como era antigamente.
12:46
E a primeira coisa que a IBM propôs:
12:48
Foi a criação de Dados Hierárquicos.
12:51
Basicamente os dados seriam armazenados e teriam uma hierarquia.
12:55
Você teria dados interligados.
12:58
Você teria dados interligados de uma forma bem simplista, mas tudo de forma hierárquica.
13:03
Esse foi o primeiro modelo proposto pela IBM.
13:06
Esse modelo ficou conhecido como: modelo Hierárquico.
13:09
Além do modelo Hierárquico foi proposto um outro modelo que foi a evolução do Hierárquico.
13:13
Nele os dados não teriam, quem é superior ou quem é inferior.
13:17
Eles seriam ligados numa forma de Rede Inteligente.
13:21
isso trouxe o Modelo em Rede!
13:23
Os modelos Hierárquicos e em Rede.
13:25
Foram os primeiros modelos, sugeridos lá no íniciozinho, no meio década de 60, pela IBM.
13:31
É claro que ele foram importante, a gente não vai se aprofundar neles.
13:34
Mais saiba que eles existiram.
13:36
Mais não é esse o modelo utilizado até hoje em dia.
13:39
Os modelos Hierárquicos e em Rede, permitiam que eu guardassem, por exemplo:
13:42
Os dados dos meus clientes, dos meus serviços, dos meu funcionários, das minhas empresas e dos meus fornecedores.
13:49
Isso sem problema nenhum, o problema é que esses modelos eles não facilitavam uma coisa simples.
13:55
O Relacionamento!
13:57
[Risos] Mas calma, não é esse tipo de relacionamento que eu tô falando.
14:02
O relacionamento que eu tô falando é esse daqui.
14:05
Os dados teriam relação entre eles.
14:08
Então eu poderia um ou um conjunto de registros, a outro conjunto de registro que está em outra tabela.
14:15
Isso foi muito valioso e deu origem a um novo modelo.
14:19
E foi pensando nesse modelo que na época de 70.
14:22
Um dos pesquisadores da IBM, o Edgar Codd, propôs um novo modelo.
14:26
Nesse novo paradigma os dados eles seriam armazenados.
14:30
Invés de Hierarquia ou ligações de Redes.
14:33
Eles teriam ligações mais intrínsecas, elas teriam relação.
14:38
E foi dos estudo de Codd, que surgiu o modelo Relacional.
14:42
E é esse modelo Relacional que nós vamos utilizar, para criar nossos os bancos de dados em MySQL.
14:48
E você pode tá perguntando, mas Guanabara, para por aí? O modelo Relacional é o melhor que a gente hoje?
14:52
Não!
14:53
A gente tem modelos mas recentes, como por exemplo:
14:55
Os modelos baseados em Documento, ou ainda mais recente, os modelos Orientados a Objetos.
15:00
Porém, quando a gente começa a estudar em Colégios e Faculdades, a gente sempre começa pelo modelo Relacional.
15:05
Que é muito mais simples de explicar, aí você vai tendo seu processo evolutivo.
15:10
Como eu disse, seus estudos nunca vão parar.
15:12
Então a gente vai começar no modelo Relacional.
15:14
E você vai continuar seus estudos e aprendendo muito mais sempre!
15:18
Esse modelo Relacional é muito importante e permite coisas do tipo:
15:22
Se eu tenho um banco de dados e eu tenho um cadastro de cliente, por exemplo.
15:26
Eu vou pegar essa ficha e guarda no meu banco de dados.
15:29
Daqui eu posso ter acesso a todos os dados do meu cliente.
15:32
Até então qualquer um dos modelos tem acesso a isso, qualquer um dos modelos daria permissão pra isso.
15:38
Mais o modelo Relacional dá um passo a frente.
15:41
Eu poderia por exemplo, identificar onde ele mora, e quais foram as compras que ele fez.
15:46
A partir dessas compra que ele fez, eu posso, eu posso ter acesso a data que ela foi feita e qual foi a influência que ela teve no meu estoque.
15:52
E se por acaso esse estoque ficar baixo, eu posso ter acesso diretamente ao meu fornecedor.
15:57
Viu, como é valioso esse tipo de paradigma.
16:00
A partir de um dado armazenado eu consigo caminhar por eles, contato que elas tenham relação entre si.
16:06
E eu como construtor do banco de dados, especifique essas relações.
16:09
As vezes você pode se perguntar, mas Guanabara, especificar como?
16:13
É um programa onde eu vou, clicando, clicando, clicando e eu vou fazendo?
16:16
Não!
16:17
Lembra que eu falei antes que um banco de dados tinha que ter uma linguagem de exploração?
16:20
Pois é essa linguagem de exploração que a gente vai ter que aprender, durante varias aulas por esse curso.
16:25
O nosso foco, aqui no Curso em Vídeo, de banco de dados como iniciante.
16:29
Vai ser a explicação mais aprofundada de uma linguagem de uma especifica.
16:34
Essa linguagem especifica, ela já teve alguns nomes: O primeiro delas foi "Structured Query English Language"
16:40
Difícil de falar neh! Mas a sigla é mais fácil de você decorar.
16:43
Essa linguagem ficou conhecida inicialmente como "SEQUEL".
16:47
Sacou a piadoca? Não!
16:49
"Seek, Well".
16:52
Burcar bem.
16:53
Não?
16:54
E você achando que minha piada do Banco de Dados, seria ruim neh?
17:00
Não demorou muito para esse nome mudar para "Structured Query Language", ou SQL.
17:06
Então SQL, basicamente é uma linguagem de consulta.
17:09
É uma linguagem onde você vai poder dar comandos, dar instruções ao meio ambiente do banco de dados.
17:16
E aí ele vai te retornar uma "Query", uma solicitação, uma resposta a uma solicitação.
17:21
E a ideia inicial é que a linguagem SQL, fosse universal.
17:25
Você teria uma única linguagem SQL
17:27
E todos os bancos de dados suportaria comandos nessa linguagem.
17:32
O grande problema é que, cada fabricante resolveu dá sua apimentada e criou sua própria SQL.
17:38
Isso tornou o mercado confuso, porque invés de uma linguagem a gente tinha várias linguagens.
17:44
E essa várias linguagens criavam certa confusão.
17:47
Basicamente cada bando de dados, tinha suporte SQL.
17:50
Mas dava uma aprimorada, dava uma pequena apimentada, no seus comandos.
17:55
Isso gerou uma grande despadronização.
17:58
E aí vieram os órgãos de padronização para resolver a bagunça.
18:01
Basicamente o que aconteceu, é que os órgãos americanos ANSI e ISO
18:06
resolveram entrar na briga e padronizar!
18:08
então, basicamente quando você ouve, quando você lê por ai
18:11
Aha! O banco de dados tal é compatível com ANSI-SQL
18:15
Basicamente ele é compatível com SQL padronizado universalmente
18:20
Dai então, surgiram vários bancos de dados
18:23
Como por exemplo! O Oracle, que é um dos maiores bancos de dados do mercado hoje em dia
18:27
Alem da Oracle, nós temos a IBM ainda trabalhando no seu DB2
18:31
Sim! A IBM que criou o modelo do banco de dados, tem o seu próprio banco de dados, que é o DB2
18:36
Tem um banco de dados que é bem antiguinho, que é o dBase
18:38
que eu estudei no meu segundo grau, cara o dBase é véi pra ca#%te, não se usa mais.
18:42
Mais é vei! Mais é um banco de dados.
18:44
E como não poderia deixar de ser, a Microsoft também tá no bolo com o SQL Server
18:48
Essas quatro soluções, são soluções pagas de banco de dados, são soluções empresarias de banco de dados
18:54
são soluções de grandes empresas na tecnologia
18:56
mas você pode estar se perguntando: mas Guanabara, não existe uma solução gratuita?
19:00
Não existe nada Free?
19:01
Aqui no Curso em Vídeo a gente sempre dá opção meu querido
19:03
Em relação á bancos de dados gratuitos
19:05
e não confunda gratuito com ruim
19:08
gratuitos e bons
19:10
tenho alguns para citar aqui pra vocês
19:11
O MySQL, é uma das soluções mais populares
19:14
E é a solução que a gente vai trabalhar nessas aulas
19:17
MySQL é um banco de dados gratuito, que agora pertence a Oracle, mas permanece gratuito
19:23
e que já tem uma história muito grande, já tem um número grande de ferramentas
19:26
e é com elas que a gente vai trabalhar durante todas as aulas
19:29
e o MySQL não é a única opção não
19:31
parte do grupo que criou o MySQL, depois que ele foi vendido pra Oracle
19:34
criou um fork, criou uma versão que vai ser atualizada agora de forma separada do MySQL
19:40
chamado MariaDB.
19:42
Então é assim, no finalzinho de 2015, início de 2016
19:45
MySQL e MariaDB, são basicamente a mesma coisa. Um é fork do outro.
19:49
Mas a partir do momento que eu estou gravando essa aula, eles vão começar a tomar caminhos diferentes
19:54
Então, se você ouviu falar em MariaDB, saiba que ele foi criado por parte dos programadores que criaram MySQL
20:00
Alem do MySQL e o do MariaDB, a gente tem o Firebird e também o PostgreSQL
20:07
Todas essas soluções, são soluções de bancos de dados
20:10
eu já te dei quatro soluções pagas e quatro soluções gratuitas
20:13
nós vamos trabalhar basicamente com o MySQL
20:16
mas sinta-se a vontade para estudar todas essas tecnologias
20:20
Então é isso meu querido gafanhoto!
20:21
Eu espero que você tenha gostado dessa sua primeira aula do curso de banco de dados do Curso em Vídeo
20:26
e a gente volta na próxima aula com algumas informações extras sobre o MySQL
20:31
e vamos aprender já de cara, como instalar a base
20:34
como instalar todas as ferramentas que a gente vai utilizar durante as aulas
20:37
nunca se esqueça, toda a semana a gente tem aula aqui no Curso em Vídeo
20:41
e sempre que um curso estiver ativo, a gente conta sempre com a colaboração de vocês
20:45
compartilhando e mostrando pras pessoas que este projeto está surgindo, e é só assim
20:50
só com uma quantidade muito grande de gafanhotos, com a quantidade muito grande de alunos
20:54
que a gente consegue patrocínio, que a gente consegue estrutura pra criar um curso novo
20:58
então a gente precisa muito do apoio de vocês
21:01
E nunca se esqueça!
21:02
Clicando aqui você vai se iscrever no canal
21:04
a inscrição no canal, é uma coisa muito importante pra gente
21:07
por que faz com que a comunidade aumente e o canal cresça cada vez mais
21:12
no momento que eu estou gravando este vídeo, a gente já passou de 120.000 pessoas inscritas
21:16
e assistindo aulas do Curso em Vídeo, e eu ficou muito feliz e muito orgulhoso com isso
21:21
a gente precisa muito mais, a gente precisa de muitos gafanhotos pra chamar de nossos
21:25
Clicando aqui como sempre, você vai ter acesso a Playlist
21:28
então essa é a primeira aula do curso de banco de dados
21:30
clicando aqui você vai dar uma olhadinha pra ver se tem mais
21:33
se tiver mais, já vai estudando meu pequeno gafanhoto.
21:36
e clicando aqui no meio, você vai ter acesso ao Curso em Vídeo, lá a gente disponibiliza alem das aulas
21:41
os pacotes extras, com banco de dados, com as ferramentas, tem os links e tem tudo mais
21:46
se inscreve lá, acessa o cursoemvideo.com
21:49
que lá tem todas as informações extras necessárias e que o YouTube as vezes não permite pra gente
21:54
É isso ai meu pequeno gafanhoto
21:56
um forte abraço pra você
21:57
continue sempre estudando
21:59
esse curso é uma continuidade
22:01
então dá uma olhada também no curso de algorítimo
22:03
dá uma olhada no curso de PHP
22:05
por que na sequência do curso de banco de dados, a gente vai unificar isso tudo
22:08
e você precisa estar preparado
22:10
um forte abraço meu querido
22:12
bom ter você de volta, eu espero que você tenha aproveitado essas férias
22:16
mas agora voltou a hora de estudar.
22:18
Um forte abraço, estude sempre e até a próxima.
"""

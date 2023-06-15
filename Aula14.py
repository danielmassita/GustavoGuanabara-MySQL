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

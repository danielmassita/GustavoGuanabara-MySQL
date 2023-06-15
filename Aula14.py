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


"""

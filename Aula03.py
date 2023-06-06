# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/criando-o-primeiro-banco-de-dados/
# https://youtu.be/m9YPlX0fcJk

"""
Aula 03 - Curso MySQL #03 - Criando o primeiro Banco de Dados

Vamos utilizar uma contação de história. Conheceremos o nosso amigo, Godofredo, para entendermos a ESTRUTURA DO BANCO DE DADOS! 

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
  
Características que todos possuem... Pessoas diferentes, com CARACTERÍSTICAS semelhantes e comuns entre eles (nome, idade, sexo, peso, altura, nacionalidade). 
Cada pessoa é uma INSTÂNCIA. São unidades diferentes.
O Banco de Dados tem como OBJETIVO registrar coisas separadas (instâncias) que possuem características semelhantes e afins.
Usando esse padrão, podemos ADICIONAR qualquer tipo de pessoa, com essas CARATERÍSTICAS comuns. Mas os VALORES são diferentes. 
Desse modo, podemos colocar essas personagens em um CONTAINER que será chamado de 'PESSOAS'. 
E todas as INSTÂNCIAS dentro do container terão essas MESMAS CARACTERÍSTICAS (nome, idade, sexo, peso, altura, nacionalidade), algumas opcionais embora, mas sempre existe a possibilidade de CADASTRO.
Podemos criar container's diferentes, como por exemplo em distinção do container de 'pessoas', podemos ter um de 'JOGOS' com todas as características diferentes (de jogos, estilos, etc.).

A idéia é, em um Banco de Dados, ter a capacidade de:
- AGRUPAR coisas com CARACTERÍSTICAS semelhantes, e
- SEPARAR coisas com CARACTERÍSTICAS diferentes, mas que pela diferença, eu vou agrupar elas nas semelhanças entre elas;

Vamos colocar o container dentro de um 'navio'. Esse navio vai ser o nosso Banco de Dados.
- Banco de Dados são COLEÇÕES DE DADOS com características separadas, mas organizados em LOCAIS específicos.
- Os LOCAIS específicos são as TABELAS ('pessoas', 'jogos'), com coisas com CARACTERÍSTICAS semelhantes.
- E os dados dentro das tabelas são os REGISTROS. 

RESUMINDO: Banco de Dados > Conjunto de Tabelas         > Tableas são Conjunto de Registros
RESUMINDO: Local          > Características Semelhantes > Instâncias Distintas  > Registros difeferentes. 

"""

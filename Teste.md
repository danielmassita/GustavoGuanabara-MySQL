Teste de MySQL
MySQL [40 Horas]  Teste de MySQL
Resultados
10 of 10 Perguntas answered correctly

Your time: 00:12:08

Você alcançou 10 de 10 Ponto(s), (100%)

Clique aqui para continuar
Examine as tabelas “Empregado” e “Departamento” do Banco de dados, e a instrução SQL a seguir.



SELECT Departamento.nome
FROM Departamento, Empregado
WHERE Departamento.id = Empregado.departamento_id
AND Empregado.salario > 2500
Qual o resultado da consulta SQL?

 Informática
 Pessoal
 Pagamento
 Finanças
 Administração
Correto
Considerando os conceitos de Banco de Dados, a sigla SQL significa:

 Super Query Language
 Small Question Language
 Simple Question Language
 Structure Query Language
 Structure Question Language
Correto
Uma transação representa uma interação entre a aplicação e o sistema de banco de dados tratada de forma única e independente. De acordo com as propriedades da transação, relacione as colunas e, a seguir, assinale a alternativa com a sequência correta.

1 - Atomicidade
2 - Consistência
3 - Isolamento
4 - Durabilidade

( ) Garante que o banco de dados esteja em um estado íntegro depois de a transação ser realizada.
( ) Garante que todas as tarefas da transação sejam cumpridas, ou a mesma seja cancelada como um todo.
( ) Garante que o resultado de uma transação só seja visível para outras transações no momento em que ela é finalizada com sucesso.
( ) Garante que a transação seja persistida assim que finalizada, ou seja, não será desfeita ou perdida mesmo na ocorrência de falhas do sistema.

 2, 1, 4, 3
 2, 3, 1, 4
 4, 2, 3, 1
 2, 1, 3, 4
 3, 1, 4, 2
Correto
Assinale a alternativa que completa corretamente a lacuna da assertiva a seguir.

A chave __________________ identifica um registro de forma única, isto é, na mesma base de dados não pode haver mais de um registro com a mesma chave.

 primária
 estrangeira
 secundária
 de registro
 de busca
Correto
Considere a instrução SQL a seguir:

INSERT INTO pessoas (codigo, nome) VALUES ('1', 'Maria');

Verifique as afirmações abaixo, dizendo se cada uma é verdadeira ou falsa.

( ) o nome da tabela que está sendo usada é "nome"
( ) o nome da table que está sendo usada é "pessoas"
( ) o comando INSERT atualiza dados em uma tabela
( ) Utilizando esta instrução, será inserida uma nova linha na tablela

 F - V - V - F
 F - V - F - V
 V - V - V - V
 F - V - F - F
 F - F - F - F
Correto
A linguagem SQL inclui um componente de linguagem de definição de dados (DDL – Data Definition Language) e um componente de linguagem de manipulação de dados (DML – Data Manipulation Language). Qual das opções a seguir possui instruções apenas de definição de dados?

 CREATE TABLE, ALTER TABLE.
 SELECT, INSERT.
 COMMIT, ROLLBACK.
 GRANT, REVOKE.
 OPEN, CLOSE.
Correto
Considerando os conceitos de Banco de Dados, relacione os parênteses vazios aos seus conceitos, depois assinale a alternativa que apresenta a sequência correta.

1 - DCL
2 - DDL
3 - DML

( ) permite conceder, retirar e controlar permissões de uso
( ) voltado à manipulação de dados
( ) voltado à definição de dados

 1, 3, 2
 1, 2, 3
 2, 3, 1
 3, 1, 2
 3, 2, 1
Correto
Examine as tabelas Empregado e Pagamento do banco de dados a seguir e a instrução SQL, e assinale a opção correta.



SELECT count (*)
FROM Empregado, Pagamento
WHERE Empregado.id = Pagamento.empregado_id
AND Empregado.idade < 25 AND Pagamento.valor > 1500
O resultado da consulta SQL é:

 1
 2
 3
 4
 5
Correto
Uma consulta SQL pode conter mais de seis cláusulas, porém, somente duas são obrigatórias. Estas duas são:

 SELECT E ORDER BY
 FROM E WHERE
 WHERE E GROUP BY
 SELECT E FROM
 SELECT E WHERE
Correto
Um banco de dados pode ser criado sobre um dos seguintes enfoques:

 hierárquico, em rede e relacional
 em árvore, relacional e sequencial
 hierárquico, indexado e em rede
 em árvore, em rede e sequencial indexado
 indexado, relacional e sequencial
Correto

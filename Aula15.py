# Curso MySQL #15 - Chaves Estrangeiras e JOIN
# https://youtu.be/paZNDJAPT4E
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/chaves-estrangeiras-e-join/

"""
RELACIONANDO TABELAS - Parte 2

Quando criamos uma tabela usando o MySQL, precisamos definir uma ENGINE, uma máquina que será capaz de criar os registros.
InnoDB = uma 'engine', um mecanismo (InnoBase < Oracle) permite criar tabelas com características que vamos precisar. 

A principar característica dessa engine é SUPORTAR CHAVES ESTRANGEIRAS. 
Todas essas são 'engines' que permitem criar BD e Tabelas em MySQL que sejam compatíveis com CHAVES ESTRANGEIRAS.

- MyISAM (não é complacente com as regras transacionais do ACID)
- InnoDB (suportam ACID e Chaves Estrangeiras!!!)
- XtraDB (suportam ACID)

Transação é tudo aquilo que podemos PEDIR pro Banco de Dados e que ele possa EXECUTAR.
ACID = 
- Atomicidade (não pode ser subdividida em sub-tarefas, ou toda é feita ou nada é feito, não há transação). Sua mãe manda arrumar o quarto // arrumar somente o armário.
- Consistência (um BD consistente antes, precisa continuar consistente após a transação). Se antes tava OK, depois da transação está OK, sem falhas/inconsistências, se ocorrer, volta pro estado anterior.
- Isolamento (se existirem duas transações ocorrendo ao mesmo tempo em paralelo, ambas devem acontecer como se sendo executadas isoladas). Se dois usuários requisitarem algo do BD, ambos os pedidos devem ocorrer de forma isoladas, uma sem afetar a outra.
- Durabilidade (uma transação deve ser durável, durar o tempo que for necessário). O dado do cliente fica no DB pelo tempo que quiser (telefone, nome, atributos, etc.), com alteração que vai persistir e ser durável enquanto existir.


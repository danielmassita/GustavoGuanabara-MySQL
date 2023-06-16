# Curso MySQL #16 - INNER JOIN com várias tabelas
# https://youtu.be/jx2ne8iZMOA
# https://www.cursoemvideo.com/curso/mysql/aulas/banco-de-dados/modulos/inner-join-com-varias-tabelas/

""" 
[Gafanhoto] n--------- <Assiste a> ---------n [Curso]
- id (pk)                                   - idcurso (pk)
- nome                                      - nome 
- sexo                                      - descricao 
- nascimento                                - aulas 

Classificação de Relacionamento: Cardinalidade de muitos-para-muitos (N-to-N).
Regra de N-para-N, nas extremidades (N), vou trazer pro meio uma NOVA entidade <antiga Relação: Assiste> com novos relacionamentos das extremidades. 

[Gafanhoto] ---1-------n--- [Assiste] ---n-------1--- [Curso]
- id (pk) >>>               - id (pk)             <<<   - idcurso (pk)
- nome                      - data                      - nome 
- sexo                  >>> - idgafanhotos (FK)         - descricao 
- nascimento                - idcurso (FK)  <<<         - aulas 

Entidade 'gafanhotos' possui 'id' como primary key pra cada alunos.
Entidade 'cursos' possui 'idcurso' como primary key pra cada curso.
Entidade 'assiste' possui 'id' como primary key, idgafanhoto e idcurso como Foreign Keys.

Técnica aula passada: Trazer a chave primária do Lado-1 para o Lado-N-muitos, duas vezes.

# CRIANDO A TABELA EXTRA
CREATE TABLE gafanhoto_assiste_curso (
  id int NOT NULL AUTO_INCREMENT,
  data date,
  idgafanhoto int,
  idcurso int,
  
  PRIMARY KEY (id),
  FOREIGN KEY (idgafanhoto) REFERENCES gafanhotos(id)
  FOREIGN KEY (idcurso) REFERENCES cursos(idcurso)
) DEFAULT CHARSET = utf8;

# A chave estrangeira DEVE ser do mesmo TIPO da chave primária.
"""

# XAMP Server + MySQL Workbench
USE cadastro;

CREATE TABLE gafanhoto_assiste_curso (
	id int NOT NULL AUTO_INCREMENT,
    data date,
    idgafanhoto int,
    idcurso int,
    
    PRIMARY KEY (id),
    FOREIGN KEY (idgafanhoto) REFERENCES gafanhotos(id),
    FOREIGN KEY (idcurso) REFERENCES cursos(idcurso)
) DEFAULT CHARSET = utf8;
# 1	2	17:06:00	CREATE TABLE gafanhoto_assiste_curso (3719 'utf8' is currently an alias for the character set UTF8MB3, but will be an alias for UTF8MB4 in a future release. Please consider using UTF8MB4 in order to be unambiguous.	1.672 sec

""" Vamos elaborar o exemplo:

[Gafanhoto] ---1-------n--- [Assiste] ---n-------1--- [Curso]

- Menino                 menino.[  ].hmtl5               - HTML5
                         menino.[  ].word            
                         
- Godofredo           godofredo.[  ].hmtl5               - PHP 
                      godofredo.[  ].php
                      
- Dolores               dolores.[  ].html                - Word
                        dolores.[  ].php                     
                        dolores.[  ].word                     


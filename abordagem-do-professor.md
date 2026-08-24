# O professor: perfil acadêmico e o que ele espera

> Duas fontes distintas aqui, e vale manter a distinção: o **perfil acadêmico** é público e
> verificável; a **leitura da postura em sala** vem da experiência do estudante em aula e é
> impressão, não fato documentado. Não trate a segunda parte como retrato definitivo de ninguém.

## Perfil acadêmico

**Gustavo Alberto Giménez-Lugo** — Departamento de Informática (DAINF), UTFPR/Curitiba, desde
2005. Também no Programa de Pós-Graduação em Computação Aplicada (PPGCA).

| Formação | |
|---|---|
| Graduação | Engenharia Elétrica, ênfase em Eletrônica — UFPR, 1990 |
| Mestrado | Ciências — UTFPR, 1994 |
| Doutorado | Engenharia Elétrica (Inteligência Artificial) — Escola Politécnica da USP, 2004 |

**Tese de doutorado:** *Um modelo de sistemas multiagentes para partilha de conhecimento
utilizando redes sociais comunitárias*. Propõe agentes de informação que assistem comunidades
humanas que partilham conhecimento — agentes **cientes do ambiente social do usuário**, com
representações do conhecimento do usuário e das redes sociais ao seu redor, **organizadas
subjetivamente**.

**Orientador: Jaime Simão Sichman** (EP-USP).

**Áreas de atuação:** sistemas cognitivos artificiais, sistemas multiagentes, modelagem e
simulação de redes complexas, emergência e geração de objetivos em agentes, robótica cognitiva,
ontologias, apoio à decisão, teoria dos jogos, negociação automatizada, coordenação e cooperação.

**Comunidade:** publica com Cesar A. Tacla (colega de DAINF e autor dos slides de agentes do
bloco 1) e Mariela Morveli-Espinoza, entre outros. A UTFPR sediou o **WESAAC** (Workshop-Escola
de Sistemas de Agentes, seus Ambientes e Aplicações).

### O que isso explica sobre o material da disciplina

A pasta `Teoria_de_Agencia_SMA/` do bloco 1 não é acervo aleatório: é a **linhagem intelectual
dele**. Sichman é seu orientador; Helder Coelho é da mesma comunidade lusófona de sistemas
multiagentes. Quando ele disponibiliza essas três obras junto com o Cap. 2 do Russell & Norvig,
a mensagem implícita é que o capítulo do livro é o **ponto de partida**, e a noção rica de
agência está nos outros textos.

E há uma continuidade direta entre a pesquisa dele e o que ele cobra: uma tese sobre
representações **subjetivamente organizadas** do conhecimento e das relações sociais de um
usuário é, no fundo, uma tese sobre o **fator humano embutido no modelo computacional**. Quando
ele insiste que "esquecem do fator humano e da intenção de quem criou", isso não é digressão —
é o programa de pesquisa dele.

## A postura em sala, e o que fazer com ela

Impressões relatadas, a serem calibradas ao longo do semestre:

- **O livro é ponto de partida, não autoridade.** O valor está em trazer o que o livro não diz,
  o que ele simplifica e o que ele apaga ao formalizar.
- **Crítica à intenção por trás da criação técnica.** Exemplo citado por ele: Turing não teria
  sido movido por um humanismo do progresso, mas pela automação do trabalho — livrar a produção
  da dependência de humanos frágeis. O mesmo argumento aplicado ao tear mecânico.
- **"Nunca vamos entender o âmago de quem criou algo"** — daí a exigência de deixar explícitas
  as próprias escolhas, premissas e justificativas. É a raiz metodológica da seção de
  METODOLOGIA da Tarefa 1 e da política rígida de autoria.
- **Crítica geopolítica ampla e simétrica** — EUA, Europa, China e também Índia. Simétrica é a
  palavra importante: não é alinhamento a um polo, é desconfiança da narrativa de progresso
  neutro. Um argumento que troque um centro por outro não satisfaz esse critério.

### Como isso se traduz em nota

**Na participação:** perguntas que localizam a escolha de modelagem e perguntam o que ela apaga
valem mais que perguntas de esclarecimento técnico.

**No artigo da Tarefa 1:** o enunciado pede justificativas de **DOMÍNIO** antes das de modelagem,
representação e implementação. É exatamente aí que essa exigência aterrissa — justificar pelo
domínio é dizer o que a abstração jogou fora e por que era aceitável jogar.

**Nos ensaios de novembro/dezembro:** é o terreno natural dele. O primeiro é sobre o artigo do
Turing; o terceiro é sobre "tópico avançado em IA **e Cognição**".

## Eixos de crítica ao livro que a leitura já oferece

Candidatos honestos, para desenvolver com o texto na mão — não para repetir:

- **Cap. 2** — a racionalidade é definida contra uma medida de desempenho externa, mas o livro
  trata essa medida como **dada**. Quem a define? Um agente "racional" é racional segundo o
  critério de quem.
- **Cap. 2** — a taxonomia de ambientes é apresentada quase como descrição do mundo. Mas decidir
  que um ambiente "é episódico" é uma **escolha de modelagem**, não uma observação. O que se
  ganha e o que se perde ao declarar isso.
- **Cap. 2** — o agente do R&N é individual. Toda a dimensão social da agência (a linhagem
  Sichman/Coelho) fica fora do capítulo.
- **Cap. 3 e 4** — a função objetivo é sempre dada de antemão. No TSP "minimizar distância" é
  inocente; em aplicação real, a função objetivo codifica o interesse de alguém.
- **Turing 1950** — o jogo da imitação testa a capacidade de **passar por** humano, não de
  pensar. Substituir a pergunta original por um teste operacional é, ele próprio, um gesto de
  modelagem com consequências.

## Onde a crítica tem literatura de verdade

A leitura do Turing como automação do trabalho é uma interpretação historiográfica forte e
contestável. Para **discutir** em vez de repetir, a bibliografia existe:

- TURING, A. M. (1950). *Computing Machinery and Intelligence*. Mind 49:433–460 — a fonte primária
- SCHAFFER, Simon (1994). *Babbage's Intelligence: Calculating Engines and the Factory System* —
  a ponte histórica entre divisão do trabalho fabril, tear e máquinas de calcular. É o texto que
  o argumento do tear pede
- BABBAGE, Charles (1832). *On the Economy of Machinery and Manufactures* — a fonte do século XIX
- MIROWSKI, Philip (2002). *Machine Dreams: Economics Becomes a Cyborg Science* — o contexto de
  Guerra Fria e RAND por trás de Newell e Simon
- SUCHMAN, Lucy (2007). *Human-Machine Reconfigurations*
- DREYFUS, Hubert. *What Computers Still Can't Do*

E, já citados pelo próprio professor nos slides do bloco 1 — ou seja, fontes que ele reconhece:

- BERMÚDEZ, J. L. *Cognitive Science: An Introduction to the Science of the Mind*, 2ª ed., 2014
  (também na bibliografia complementar da disciplina)
- CARIANI, Peter — emergência e adaptatividade em organismos e dispositivos
- MERKLE, L. E. (2002). *Disciplinary and Semiotic Relations across Human-Computer Interaction*
- PFEIFER, IIDA & GOMEZ (2006). *Designing intelligent robots — on the implications of embodiment*
- NILSSON, N. J. (2009). *The Quest for Artificial Intelligence*

> Uma nota de calibragem: concordar com a crítica não é o que está sendo avaliado. Um estudante
> que apenas devolve a tese do professor não demonstrou análise — demonstrou eco. O critério
> declarado é localizar a prática no marco conceitual e sustentar o **porquê**. Isso vale também
> quando o porquê discorda dele, desde que sustentado.

## Fontes

- https://www.escavador.com/sobre/442272/gustavo-alberto-gimenez-lugo
- https://www.researchgate.net/profile/Gustavo-Gimenez-Lugo
- https://www.teses.usp.br/teses/disponiveis/3/3141/tde-15112004-190053/pt-br.php
- http://dainf.pg.utfpr.edu.br/wesaac2020/bestPapers.html
- http://lattes.cnpq.br/2787038908575326 (Lattes — fora do ar no momento da consulta)

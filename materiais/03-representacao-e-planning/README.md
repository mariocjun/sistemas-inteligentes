# Bloco 3 — Representação de Conhecimento e Planejamento

Pasta do Moodle: *"pasta_03_RepresentacaoDeConhecimento_e_Planning"*. Cobre os encontros 3 (parte
final) e 4. **33 arquivos** — o maior bloco, e o único com **código executável**.

> ✅ **Responde uma pergunta que estava em aberto:** Prolog **entra na disciplina**, e com peso.
> Há dois conjuntos de exercícios, oito programas `.pl` de aprendizado e dois planejadores
> completos. A ementa citava "inferência em Prolog" e o planejamento semanal não mencionava —
> agora está claro.

---

## Slides de aula

| Arquivo | Autor | Págs | Conteúdo |
|---|---|---|---|
| `00_Hipotese_SistemasSimbolosFisicos_e_LingDoPensamento.pdf` | **Giménez-Lugo** | 11 | Hipótese do Sistema de Símbolos Físicos e Linguagem do Pensamento |
| `01_SensoComum_TACLA.pdf` | Tacla | 34 | Conhecimento e raciocínio de senso comum |
| `02_Planning_COG_SCI.pdf` | **Giménez-Lugo** | 14 | Planning: conceitos fundamentais |
| `03_FRAME_PROBLEM.pdf` | **Giménez-Lugo** | 6 | O *frame problem* — ações, situações e eventos |
| `04_PLANEJAMENTO_7.pdf` | DI-UFPE | 43 | Planejamento × resolução de problemas; cálculo situacional + provador de teoremas; STRIPS + POP; limitações |
| `05_Planning-POP_TACLA.pdf` | Tacla | 13 | Planejamento clássico, POP |
| `06_RedesSemanticas_Frames_8.pdf` | CIn-UFPE | 22 | Redes semânticas e sistemas de frames |
| `00_DeliveryRobot.pdf` | Poole & Mackworth | 10 | O mundo do robô entregador — **domínio usado por todo o código Prolog** |

> Três dos oito decks são **do próprio professor**, e um deles retoma a Hipótese do Sistema de
> Símbolos Físicos — a mesma que abre o bloco 1 e reaparece no bloco 4. É a espinha do semestre.

## Artigos

| Arquivo | Referência | Págs |
|---|---|---|
| `00_2010_Sowa_LogicAndOntology_in_LanguageAndReasoning.pdf` | SOWA, J. F. (2010). *The Role of Logic and Ontology in Language and Reasoning* | 28 |
| `00_2011_WhyDoHumansReason_ArgumentativeTheory.pdf` | MERCIER, H. & SPERBER, D. (2011). *Why Do Humans Reason? Arguments for an Argumentative Theory* | 57 |
| `00_2012_PROBLEMS_with_the_PROBLEM_SOLVING_PARADIGM.pdf` | OHLSSON, S. (2012). *The Problems with Problem Solving: Reflections on the Rise, Current Status, and Possible Future of a Cognitive Research Paradigm*. J. of Problem Solving, 5(1) | 28 |
| `00_2018_Applications_of_ONTOLOGIES.pdf` | KARRAY, H. — Ontology in application: use cases (LGP-ENIT-DIDS) | 24 |

**Os dois do meio são as críticas**, e vão na mesma direção do bloco 2. Ohlsson (2012) faz o
balanço do paradigma de resolução de problemas inaugurado por Newell e Simon — leia **depois** do
Turing Award de 1975, porque é a resposta a ele, quarenta anos depois. Mercier & Sperber (2011)
argumentam que a função do raciocínio humano não é chegar à verdade, e sim **argumentar e
convencer** — o que desloca todo o pressuposto de "agente racional".

## Código Prolog

### Exercícios de aprendizado (do básico ao recursivo)

| Arquivo | Tema |
|---|---|
| `ex000-00-PrimeirosPassosEmPROLOG.txt` | primeiros comandos: `is` × `=`, variáveis maiúsculas, aritmética |
| `ex010-00-comida.pl` | fatos e consultas |
| `ex020-00-nacionalidade-comida.pl` | regras com múltiplas condições |
| `ex030-00-expressividade-simpsons.pl` | expressividade |
| `ex040-00-simpsons-recursividade.pl` | recursividade |
| `ex050-00-exemplo-unificacao.pl` | **unificação e backward chaining** |
| `ex060-00-Fatorial.pl` | recursão numérica |
| `ex60-10-unificacao-recursividade-interminavel.pl_` | recursão que não termina — o contraexemplo |

Enunciados: `00-ExerciciosPROLOG.pdf` e `00_Exercicios_resolucao_PROLOG.pdf`.

### Planejadores

Dois planejadores completos, em Prolog, sobre o mesmo domínio (`00_DeliveryRobot.pdf`):

| Arquivo | O que é |
|---|---|
| `01_strips.pl` + `01_STRIPS_running_delRobot.pl` | planejador **STRIPS** |
| `02_pop.pl` + `02_POP_running_delRobot.pl` | planejador de **ordem parcial (POP)** |
| `00_delRob_SC.pl`, `03_delRob_Strips.pl` | o domínio do robô nas duas formulações |
| `LEIAME_Execucao1_STRIPS.txt` | ⭐ instruções de execução no SWI-Prolog, com queries e saídas comentadas |
| `LEIAME_Execucao2_POP.txt` | ⭐ o mesmo para POP, explicando **links causais** e **restrições de ordem** |
| `01_DelRobot_PlannersProlog_StripsPop.zip` | os dois planejadores empacotados |
| `02_PlanningApplet.zip` | applet de planejamento |

Os dois LEIAME são bem escritos e valem mais que os slides para entender a diferença entre os
paradigmas. Exemplo do STRIPS, com a dica de que o plano se lê **de trás para frente**:

```prolog
achieve(carrying(rob,k1), init, S, 10, _).
S = do(pickup(rob,k1,mail), do(move(rob,o103,mail), do(move(rob,o109,o103), init)))
```

E o do POP devolve um plano com ações numeradas e ordem parcial:

```prolog
solve([carrying(rob,k1)], P, 3).
P = plan([act(1, move(rob,o109,o103)), act(2, move(rob,o103,mail)), act(3, pickup(rob,k1,...))])
```

> Rodar os dois no mesmo objetivo e comparar as saídas é o melhor caminho para entender por que
> o planejamento de ordem parcial existe. O LEIAME do STRIPS inclusive provoca: *"o plano está
> correto? ;-)"* no exemplo 2.

Precisa do **SWI-Prolog** instalado. Vale instalar antes do encontro 4 (09/09).

## Ordem sugerida

1. `00_DeliveryRobot.pdf` — o domínio, 10 páginas, base de tudo que vem depois
2. Exercícios `ex000` a `ex060`, na ordem, no SWI-Prolog
3. `06_RedesSemanticas_Frames_8.pdf` e `01_SensoComum_TACLA.pdf` — representação
4. `04_PLANEJAMENTO_7.pdf` e `05_Planning-POP_TACLA.pdf` — planejamento
5. Rodar STRIPS e POP seguindo os LEIAME
6. `03_FRAME_PROBLEM.pdf` — curto e conceitualmente denso
7. Ohlsson (2012), depois de ter lido Newell & Simon do bloco 2

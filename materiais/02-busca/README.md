# Bloco 2 — Busca como método de resolução de problemas

Pasta do Moodle: *"pasta_02_Busca [como método de Resolução de Problemas]"*. Cobre os encontros
2 e 3. **11 arquivos**, divididos em dois grupos com funções muito diferentes.

---

## Grupo A — Slides de aula (5 decks, 216 slides)

Acompanham o R&N e são o mapa do que será debatido.

| Arquivo | Autor | Slides | Conteúdo |
|---|---|---|---|
| `01_BuscaIntro.pdf` | Prof. Cesar Tacla | 51 | Resolução de problemas por busca, parte 1 — formulação e busca cega |
| `02_BuscaInformada_ou_Heuristica.pdf` | Tacla | 51 | Busca informada, heurísticas, A\* |
| `03_BuscaLocal.pdf` | Tacla | 34 | **Busca local — o deck do encontro 3** |
| `04a_ALG_GENET.pdf` | (adaptado de R&N) | 42 | Algoritmos de busca informada, com AG |
| `04b_AlgGeneticos.pdf` | Myriam Delgado | 38 | **AG canônico, completo — direto para a Tarefa 1** |

### `03_BuscaLocal.pdf` — roteiro

Declara na abertura: *R&N capítulo 4*. Cobre subida de encosta → têmpera simulada → feixe local →
algoritmos genéticos, exatamente a escada discutida em `../../conceitos/busca-local-e-heuristicas.md`.

| Slides | Conteúdo |
|---|---|
| 4–7 | Por que busca local: o **caminho é irrelevante**, só interessa o estado final. Vantagens sobre busca cega/informada: memória constante, soluções factíveis em espaços enormes |
| 8–11 | Estratégia geral; a figura da paisagem (máximo local, global, platô, planície); completude |
| 12–17 | Subida de encosta. Metáfora: *"escalando o Everest numa tempestade de neve, com amnésia"*. **8-rainhas** como exemplo, com h = número de pares de rainhas se atacando |
| 18–21 | Os três problemas: máximo local, cumeeiras, platôs. Solução parcial: **reinício aleatório** |
| 22–28 | **Têmpera simulada.** Metáfora metalúrgica; a prova de que com resfriamento suficientemente lento acha o ótimo global com probabilidade ≈ 1; **slide 27 é o agendamento exponencial decrescente de T**; slide 28 simula `p = e^(ΔE/T)` para ΔE = −1, −50, −100 |
| 29–34 | **Busca em feixe local**, com pseudocódigo, a figura dos k estados e um exemplo no problema da mochila comparando dois feixes |

> **Slides 27 e 28 são exatamente o "gráfico decrescente" que ficou obscuro na aula.** O 28
> mostra o ponto principal em forma de curva: para o mesmo T, piorar pouco (ΔE = −1) permanece
> provável muito depois de piorar muito (ΔE = −100) ter virado impossível.

### `04b_AlgGeneticos.pdf` — roteiro

⚠️ **É o deck mais importante para a Tarefa 1.** Vai do AG canônico até permutações.

| Slides | Conteúdo |
|---|---|
| 2–4 | AG dentro de Computação Natural / Inteligência Computacional. Holland (1975) |
| 5–8 | Construtos: **cromossomo, gene, alelo, locus**. AG como busca informada, com *fitness* no papel de h(n) |
| 10 | Aplicações — **cita o caixeiro viajante explicitamente** |
| 11–14 | Etapas e operadores: seleção, crossover, mutação. **AG Canônico** definido: codificação binária, seleção por roleta, crossover simples, mutação uniforme, sobrevivência dos melhores |
| 16–21 | **Seleção por roleta passo a passo**, com exemplo numérico executável à mão |
| 22–24 | Crossover de 1 ponto e mutação, com exemplo |
| 25–26 | Pseudocódigo do AG canônico e valores típicos (pCROSS ≈ 0,8; pMUT ≈ 0,05) |
| 27–32 | Codificação binária × inteira; 8-rainhas nas duas; problema da mochila |
| **33–38** | **AG em problemas de permutação** |

Os slides 33–38 são o coração da Tarefa 1:

- **Slide 34–35** — permutação como representação: no caixeiro viajante o gene indica a ordem de
  visita. É a decisão de modelagem central do trabalho.
- **Slide 29** faz a pergunta que a tarefa cobra: *"os operadores de crossover e mutação ainda
  funcionam?"* — com codificação inteira/permutação, não funcionam. É esse o problema.
- **Slide 36** — **PMX (Crossover de Mapeamento Parcial)**, apresentado como o operador que *"não
  gera infactibilidade"*, com exemplo numérico passo a passo.
- **Slides 37–38** — mutação para permutações: **baseada em posição**, **baseada em ordem** e
  **por embaralhamento** de uma sublista.

> Ou seja: o próprio material da disciplina já traz o argumento de que a **representação força os
> operadores**. Na Tarefa 1 não basta usar PMX — é preciso explicar *por que* o crossover de um
> ponto quebra e o PMX não. O slide 36 dá a mecânica; o porquê é seu.

---

## Grupo B — Artigos sobre heurística (5 papers, 117 páginas)

Aqui está a jogada do professor, e vale entender antes de ler.

No R&N, "heurística" é uma coisa técnica e estreita: uma função `h(n)` que estima o custo até o
objetivo. **Os cinco artigos abrem o conceito muito além disso** — heurística em ciência
cognitiva, o debate sobre se heurísticas são atalhos racionais ou fontes de erro, e a relação
entre complexidade cognitiva e complexidade computacional.

É o movimento característico dele: o livro dá a definição operacional, os artigos mostram o que
a definição operacional deixou de fora.

| Arquivo | Referência | Págs |
|---|---|---|
| `1975_SYMBOLS__HEURISTICS_NewellSimon_TuringAward.pdf` | NEWELL, A. & SIMON, H. A. (1976). *Computer Science as Empirical Inquiry: Symbols and Search*. ACM Turing Award Lecture, 1975 | 14 |
| `1991_Beyond_BIASESandHEURISTICS_GIGERENZER.pdf` | GIGERENZER, G. (1991). *How to Make Cognitive Illusions Disappear: Beyond "Heuristics and Biases"*. European Review of Social Psychology, 2, 83–115 | 25 |
| `2005_Heuristics_EncyclopediaOfSocialMeasurement.pdf` | MUMFORD, M. D. & LERITZ, L. E. (2005). *Heuristics*. Encyclopedia of Social Measurement, Elsevier | 6 |
| `2011_HEURISTIC_DecisionMaking_GIGERENZER.pdf` | GIGERENZER, G. & GAISSMAIER, W. (2011). *Heuristic Decision Making*. Annual Review of Psychology, 62, 451–482 | 35 |
| `2019_Cognitive_and_ComputationalComplexity.pdf` | PANTSAR, M. (2019). *Cognitive and Computational Complexity: Considerations from Mathematical Problem Solving*. Erkenntnis | 37 |

`Papers_Heuristica_links.txt` traz os links originais de cada um.

### O que cada um acrescenta

**Newell & Simon (1976)** — ★ o mais importante, e o mais curto. É a palestra do Prêmio Turing de
1975, e é a **fonte primária da Hipótese do Sistema de Símbolos Físicos** que aparece no deck
histórico do bloco 1. O argumento tem duas metades: sistemas de símbolos físicos são meio
necessário e suficiente para ação inteligente geral; e a inteligência opera por **busca
heurística**. É literalmente a tese que sustenta os capítulos 3 e 4 do R&N — e o alvo das
críticas de Brooks que ele mostrou no bloco 1.

**Gigerenzer (1991)** — ataque frontal ao programa "heurísticas e vieses" de Kahneman e Tversky.
Argumenta que a maioria dos supostos "erros" de raciocínio probabilístico **não viola a teoria da
probabilidade**: os pesquisadores adotaram uma visão normativa estreita demais e ignoraram
distinções conceituais (caso único × frequência relativa). Excesso de confiança, falácia da
conjunção e negligência da taxa-base seriam artefatos do enquadramento, não falhas cognitivas.

**Gigerenzer & Gaissmaier (2011)** — a versão madura e positiva do mesmo programa: **racionalidade
ecológica**. Heurísticas não são atalhos de segunda classe; sob incerteza, podem ser *mais*
precisas que métodos que usam mais informação. Palavras-chave do abstract: compromisso
precisão-esforço, decisão médica, decisão jurídica, inteligência social.

**Mumford & Leritz (2005)** — verbete de enciclopédia, 6 páginas. Heurísticas como estratégias de
processamento em **resolução de problemas complexos e mal-definidos**. É a leitura rápida que
cola o vocabulário cognitivo ao vocabulário computacional.

**Pantsar (2019)** — o mais denso e o mais afiado para a disciplina. Usa os **três níveis de
Marr** (computacional, algorítmico, implementacional) para perguntar se a complexidade de um
problema matemático pode ser caracterizada no nível computacional. Fala diretamente com PAA: a
classe de complexidade de um problema é a mesma coisa que a sua dificuldade cognitiva?

### O eixo que os cinco desenham

> **Newell & Simon**: heurística é o mecanismo da inteligência, e inteligência é busca.
> **Gigerenzer**: heurística não é defeito nem atalho — é adaptação ao ambiente, e chamá-la de
> viés é erro do avaliador.
> **Pantsar**: a dificuldade computacional e a dificuldade cognitiva não são a mesma coisa.

Junte com o que o R&N diz — heurística é uma função que estima custo, obtida por relaxamento —
e você tem quatro sentidos distintos da mesma palavra. **Perguntar qual deles o livro está usando,
e o que os outros três revelam sobre a escolha, é exatamente o tipo de pergunta que a disciplina
avalia.**

---

## Ordem de leitura sugerida

1. `03_BuscaLocal.pdf` — antes do encontro 3, junto com R&N §4.1. Foque em 22–28 e 29–34
2. `04b_AlgGeneticos.pdf` slides 33–38 — a parte de permutação, para a Tarefa 1
3. **Newell & Simon (1976)** — 14 páginas, e é a espinha conceitual do semestre inteiro
4. `04b` completo — quando for implementar o AG
5. Gigerenzer (2011) e Pantsar (2019) — para o debate e para os ensaios de novembro
6. Gigerenzer (1991) e Mumford & Leritz (2005) — complementares

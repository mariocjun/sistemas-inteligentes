# Bloco 4 — Aprendizagem simbólica e árvores

Pasta do Moodle: *"pasta_04_AprendizagemSimbolica_ARVORES"*. Cobre os encontros 7 e 8 (30/09 e
07/10) e é o conteúdo da **Tarefa 2**. **11 arquivos.**

Correspondência no livro: **R&N 4ª ed. Cap. 19** (Aprendizado por Exemplos), §19.3 para árvores
de decisão.

## Slides

| Arquivo | Autor | Págs | Conteúdo |
|---|---|---|---|
| `01_Hipotese_SistemaSimbolosFisicos_e_LingDoPensamento.pdf` | **Giménez-Lugo** | 10 | a Hipótese, de novo — terceira aparição no semestre |
| `02_APRENDIZAGEM.pdf` | — | 4 | abertura do tema |
| `03_AprendizadoSimbolico_completo.pdf` | Tacla | 56 | **o deck principal** — aprendizado simbólico, parte 1 |
| `04_B_TREES_RandomForests.pdf` | **Giménez-Lugo** | 10 | árvores e florestas aleatórias |

## Artigos seminais

| Arquivo | Referência | Págs |
|---|---|---|
| `00_1984_PAC_ProbablyApproximatelyCorrect_LeslieValiant.pdf` | VALIANT, L. G. (1984). *A Theory of the Learnable*. CACM | 9 |
| `00_1986_QUINLAN_ID3.pdf` | QUINLAN, J. R. (1986). *Induction of Decision Trees*. Machine Learning, 1, 81–106 | 26 |

Os dois são fundacionais e curtos o bastante para ler de verdade:

- **Valiant (1984)** funda o aprendizado **PAC** (*probably approximately correct*) — a teoria que
  responde "o que significa ter aprendido?" com uma definição formal, em vez de intuição. Rendeu
  o Prêmio Turing de 2010.
- **Quinlan (1986)** é o **ID3**, o algoritmo de indução de árvores de decisão por ganho de
  informação. É literalmente o que a Tarefa 2 provavelmente vai pedir para implementar. Ler o
  original em vez da versão do livro é barato e rende muito na defesa.

## Random Forests

| Arquivo | Referência | Págs |
|---|---|---|
| `00_2012_RandomForest_HOW_MANY_TREES.pdf` | OSHIRO, PEREZ & BARANAUSKAS (2012). *How Many Trees in a Random Forest?* LNAI 7376 | 16 |
| `00_2015_RandomForest_TOUR.pdf` | BIAU, G. & SCORNET, E. (2015). *A Random Forest Guided Tour* | 42 |
| `00_2014_RandomForest_UNDERSTANDING_PhDThesis.pdf` | LOUPPE, G. (2014). *Understanding Random Forests: From Theory to Practice*. Tese de doutorado, Univ. de Liège | **223** |

A tese do Louppe é referência, não leitura. O *Guided Tour* do Biau & Scornet é a síntese
matemática; o *How Many Trees* é empírico e responde a uma pergunta prática bem delimitada — bom
modelo de artigo curto com resultado claro.

## Crítica epistemológica

| Arquivo | Referência | Págs |
|---|---|---|
| `2017_DataScience__EPISTEMOLOGY.pdf` | NERESINI, F. (2017). *On Data, Big Data and Social Research. Is It a Real Revolution?* | 9 |

Discute criticamente os pressupostos epistemológicos da ciência de dados aplicada à pesquisa
social. **O mesmo arquivo aparece no bloco 5** — sinal de que ele volta ao tema.

`00_TREES_some_LINKS.txt` traz links complementares: StatQuest sobre viés e variância e sobre
Random Forest, a *Introdução Visual ao Aprendizado de Máquina* do r2d3 (versão em português,
excelente e animada), e uma lista dos hiperparâmetros de floresta aleatória com explicação.

## Padrão que se repete

Igual aos blocos 2 e 3: **artigo seminal + slides + crítica**. Valiant e Quinlan dão o
fundamento; os slides dão a operação; Neresini pergunta o que a abordagem pressupõe. Já dá para
antecipar que a Tarefa 2 vai cobrar as três camadas.

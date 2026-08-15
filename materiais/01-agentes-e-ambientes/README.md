# Bloco 1 — Agentes e Ambientes

Material distribuído em 15/08/2026 (zip `01_Agentes_e_Ambientes20260815`), para o **encontro 1
(qua 19/08)**. Seis PDFs, ~740 páginas no total, em dois grupos muito diferentes: três peças de
aula curtas e um acervo de referência em Sistemas Multiagentes.

---

## 1. `005a-introducao-agentes-ambientes.pdf` — ★ leitura prioritária

| | |
|---|---|
| Título | **AGENTES E AMBIENTES — Breve introdução a agentes** |
| Autor | Prof. **Cesar Augusto Tacla** — UTFPR/Curitiba |
| Formato | 34 slides (PowerPoint, 19/02/2021) |
| Base declarada | Cap. 2 do Russell & Norvig (2ª ed.); parte são traduções dos slides dos autores. Também Wooldridge, *Introduction to Multiagent Systems*, 2009 (slide 34) |

É o Cap. 2 condensado, com uma formalização de ambiente que **não está no R&N** e que vale levar
para o debate.

**Roteiro do deck**

| Slides | Conteúdo |
|---|---|
| 2–3 | Agente situado e racional; o que conta como agente (robôs, softbots, dispositivos móveis, humanos) |
| 4 | **Função agente** (histórico de percepções → ações) × **programa agente** (executa a função numa arquitetura física) |
| 5–7 | Aspirador de pó: percepções `[A, sujo]`, ações `left/right/suck/NoOp`; a função como tabela, `f: P* → A` |
| 8–12 | Racionalidade: medida de desempenho, definição formal de agente racional, racional ≠ onisciente, papel de exploração e autonomia |
| 13–14 | Ambientes; **definição formal `Env: S × A → ɣ(S)`**, com `ɣ(S)` = conjunto potência dos estados |
| 15–22 | As dimensões de ambiente, uma por slide: observável, mono/multiagente, **competitivo/cooperativo**, determinístico/estocástico, episódico/sequencial, estático/dinâmico (com *semidinâmico*), discreto/contínuo |
| 23–24 | Estrutura dos agentes: por que a função considera `P*` e o programa considera só a última percepção |
| 25–27 | Agentes reativos; regras simples e comportamento emergente; exemplo em **AgentSpeak**; ponteiro para a arquitetura *subsumption* de Rodney Brooks |
| 28–31 | Agentes deliberativos: crenças e objetivos explícitos, mecanismos de deliberação (teoria de jogos, raciocínio prático); exemplo em AgentSpeak com objetivos |
| 32 | Características de agentes: situado, reativo, proativo, autônomo (autonomia = inversa à interferência humana) |
| 33 | Agentes × sistemas funcionais × objetos — **"locus de decisão externo ao objeto"** |

**Três pontos onde este deck vai além do R&N** — e que por isso rendem pergunta:

1. **`Env: S × A → ɣ(S)`** torna a distinção determinístico/estocástico *quantitativa*:
   determinístico é `|ɣ(S)| = 1`, estocástico é `|ɣ(S)| > 1`. O slide 19 registra que o R&N
   **ignora a incerteza originada pelo próprio agente** nessa classificação. Isso é uma escolha
   de modelagem, não um fato — boa pergunta para o encontro.
2. **Competitivo × cooperativo × colaborativo** aparece como dimensão própria, e o deck separa
   *colaborativo* (objetivos independentes, ganho em trabalhar junto) de *cooperativo* (objetivo
   comum). O R&N trata isso dentro de "multiagente".
3. **Reativo × deliberativo** é apresentado como o eixo estrutural, com código AgentSpeak dos dois
   lados. Comparar os dois trechos de código do slide 27 e do slide 31 mostra em 8 linhas o que a
   representação explícita de objetivos custa e compra.

---

## 2. `00_a_Historico_HSSF.pdf` — ★ leitura prioritária

| | |
|---|---|
| Título | **"SINTÉTICOS": Artefatos que "CONTENHAM" INTELIGÊNCIA (?)** |
| Autor | Prof. **Gustavo Giménez-Lugo** — UTFPR/DAINF (o professor da disciplina) |
| Formato | 22 slides (Impress, 24/08/2021) |
| Sigla | HSSF ≈ *Hipótese do Sistema de Símbolos Físicos* — o eixo do deck |

É o enquadramento histórico-conceitual da disciplina, e é o deck **do próprio professor** — a
narrativa dele sobre o que a área tentou fazer e por quê. Estrutura em duas partes, com um
epílogo:

| Slides | Conteúdo |
|---|---|
| 2–5 | A pergunta motriz: como criar artefatos que "contenham" inteligência? Genealogia dos autômatos — homúnculo, golem, papiro de Edwin Smith, o Pombo de Arquitas (~350 a.C.), o Pato de Vaucanson (1739), o Turco (1770) |
| 6–7 | **Turing (1950)**, *Computing Machinery and Intelligence*, Mind 49:433–460 — "Can machines think?" e a exigência de definir "machine" e "think". Pergunta do slide 7: qual o percurso de modelagem de artefatos computacionais **a partir de** Turing? |
| 8–13 | **PARTE I — as "partes" da inteligência, uma "teoria geral", e o corpo como contenedor.** Newell & Simon (Turing Award 1975; Nobel de Economia 1978 para Simon — racionalidade limitada e *satisficing*); resolução de Davis & Putnam (1960) e unificação de Robinson (1965); SHAKEY (1966/72); e o **axioma-base: Hipótese do Sistema de Símbolos Físicos (1976)** — "um sistema de símbolos físicos tem os meios necessários e suficientes para a ação inteligente geral" |
| 14–17 | **PARTE II — Behavior Based Robotics: o corpo como parte do algoritmo.** "Elefantes não jogam xadrez" (Brooks); computação morfológica e biorrobótica; o peixe robótico WANDA (Pfeifer, Iida & Gomez, 2006) |
| 19–22 | Epílogo: como pensamos modelos computacionais artificiais — fenômeno observado, "Computação 1" × "Computação 2 (clássica)", crenças. Referências a Merkle (PhD, UWO 2002) e Peter Cariani (emergência e adaptatividade em organismos e dispositivos) |

**Por que este deck importa mais do que parece:** ele monta a tensão que atravessa o semestre
inteiro — **símbolos físicos × cognição corporificada** — e é o pano de fundo do ensaio sobre o
artigo de Turing (18/11, 1,0 ponto, escrito em sala). O slide 15 anuncia "continua…", então
provavelmente há uma continuação em bloco posterior.

Referências rastreáveis a partir do deck, se quiser ir fundo:

- NILSSON, N. J. (2009). *The Quest for Artificial Intelligence*. Cambridge University Press
- NEWELL & SIMON (1976). Hipótese do Sistema de Símbolos Físicos
- BERMÚDEZ, J. L. *Cognitive Science*, 2ª ed., 2014 — pgs. 199, 425, 428 são as citadas (e o livro
  está na **bibliografia complementar** da disciplina)
- PFEIFER, IIDA & GOMEZ (2006). *Designing intelligent robots — on the implications of embodiment*
- TURING, A. M. (1950). *Computing Machinery and Intelligence*. Mind 49:433–460

---

## 3. `00_AREAS_IA___IJCAI2020.pdf`

Um slide único (Impress, 14/10/2020), montado a partir de https://www.ijcai20.org/. Mapa das
áreas da IA segundo os *tracks* do IJCAI 2020:

**Main tracks** — Multiagent Systems · AI Ethics · Computer Vision · Constraints and SAT ·
Data Mining · Heuristic Search and Game Playing · Humans and AI · Knowledge Representation and
Reasoning · Machine Learning · Natural Language Processing · Planning and Scheduling · Robotics ·
Uncertainty in AI

**Workshops** — Human Brain and Artificial Intelligence · Humanizing Artificial Intelligence ·
Explainable AI (XAI) · Symbolic Data Oriented Deep Learning

Uso: 5 minutos para situar onde cada bloco do semestre cai no mapa da área. Note que *Heuristic
Search*, *KRR*, *Planning* e *Multiagent Systems* — quatro dos treze tracks — são exatamente o
que a disciplina cobre até a Prova 1.

---

## 4. `Teoria_de_Agencia_SMA/` — acervo de referência (~690 páginas)

**Não é leitura linear.** São três obras completas de Sistemas Multiagentes, muito além do
escopo do Cap. 2. Servem para (a) aprofundar a noção de agência quando o debate empurrar para
lá, e (b) material dos ensaios sobre "tópico avançado em IA" (25/11 e 02/12).

### `A_2008_TeoriaDaAgenciaArquitecturaECenografia_HelderCOELHO.pdf`

**Teoria da Agência: Arquitectura e Cenografia** — Helder Coelho, LabMAg e ICC, FCUL
(Universidade de Lisboa), abril/2008. 273 páginas, em português europeu.

Índice em 11 capítulos: 1 Introdução · 2 Panorâmica da Área · 3 Noções de Agentes ·
4 Modelação Computacional Baseada em Agentes · **5 Teorias dos Agentes e da Agência** (BDI,
ACT-R, SOAR e comparações entre eles) · **6 Ambientes** (organização do espaço, adereços,
iluminação, movimento da câmara — daí a "cenografia" do título) · 7 Interacções (coordenação,
comunicação, cooperação) · 8 Organizações (TAEMS, AALAADIN, TOVE, TEAMCORE, MOISE, MOISE+, OMNI) ·
9 Plataformas (AgentSpeak(L), JACK, COOL) · 10 Aplicações · 11 Conclusões. Mais glossário e
listas de ferramentas em apêndice.

> **Recorte útil para o encontro 1:** capítulos 3, 5 e 6. O cap. 6 é a contraparte "rica" da
> definição enxuta de ambiente do R&N — a metáfora cenográfica (o ambiente como palco projetado,
> com iluminação e câmara) é uma leitura de modelagem que contrasta bem com `Env: S × A → ɣ(S)`.
> O cap. 5 (BDI × ACT-R × SOAR) é a continuação natural do slide 28–31 do deck do Tacla.

### `B_2003_RaciocinioSocial_e_Org_Sichman_LivreDocencia.pdf`

**Raciocínio social e organizacional em sistemas multiagentes** — Jaime Simão Sichman. Texto
apresentado à Escola Politécnica da USP (Depto. de Engenharia de Computação e Sistemas Digitais)
para obtenção do título de professor livre-docente. São Paulo, 2003. 258 páginas.

> O PDF foi gerado por Ghostscript 5.50 com fontes bitmap (Type 3): **o texto não é
> selecionável/pesquisável** e a extração automática produz lixo. Para busca por termo, seria
> preciso passar OCR. Tratar como leitura de tela, não como fonte para citação rápida.

> **Recorte útil:** é a referência mais avançada do pacote — raciocínio social, dependência entre
> agentes, organizações. Fora do escopo do encontro 1; forte candidata a base de ensaio sobre
> tópico avançado (25/11 ou 02/12), sobretudo se o recorte for *agência social*.

### `MAS_BOOK_JoseVidal_2010_03_01.pdf`

**Fundamentals of Multiagent Systems, with NetLogo Examples** — José M. Vidal, 01/03/2010.
155 páginas, em inglês, LaTeX, com sumário navegável e exercícios por capítulo.

Capítulos: 1 Multiagent Problem Formulation (utilidade, utilidade esperada, **MDPs**, MDPs
multiagente, **POMDPs**, planejamento hierárquico) · 2 Distributed Constraints (DCSP e DCOP:
filtering, hyper-resolution, asynchronous backtracking, weak-commitment, distributed breakout,
Adopt, OptAPO) · 3 Standard and Extended Form Games (forma normal, conceitos de solução, jogos
famosos, jogos repetidos, forma estendida) · 4 Characteristic Form Games and Coalition Formation ·
5 **Learning in Multiagent Systems** (fictitious play, replicator dynamics, AWESOME, jogos
estocásticos, aprendizado por reforço, modelo CLRI, agentes N-level, inteligência coletiva) ·
6 Negotiation (bargaining, soluções axiomáticas e estratégicas) · e adiante.

> **Recorte útil:** é o mais "computacional" dos três — algoritmos com pseudocódigo e exercícios.
> O cap. 1 (utilidade e MDPs) conecta diretamente com o agente **baseado em utilidade** do Cap. 2
> do R&N; o cap. 5 é ponte natural com o bloco de Aprendizado de Máquina (encontros 7–11).
> Os exemplos em NetLogo são um bom laboratório, mas lembre que a disciplina exige implementação
> própria — usar como referência conceitual, não como artefato de entrega.

---

## Como usar este bloco na semana 1

1. **Sábado**, depois do R&N Cap. 2: passar os 34 slides do Tacla como *checagem* do próprio
   fichamento. O que estiver no deck e não estiver no seu fichamento = releitura da seção.
2. **Domingo ou segunda**, 40 min: os 22 slides do Histórico + o slide do IJCAI. Anotar a tensão
   símbolos físicos × corporificação — é dela que sai a melhor pergunta para o debate.
3. **Terça**: folhear apenas os índices de Coelho e Vidal (15 min), sem ler. Objetivo é saber o
   que existe ali para quando precisar, não absorver agora.
4. Deixar Sichman fechado por enquanto. Marcar como candidato a ensaio de tópico avançado.

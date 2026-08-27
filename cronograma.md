# Cronograma — 17 encontros (quartas-feiras)

Fontes: **slides de planejamento do professor** (`materiais/planejamento/2026_2_Planejamento_SI_SLIDES.pdf`,
que trazem o mapeamento oficial de capítulos por edição) e o **Planejamento de Aula da turma**
(datas e pesos).

**Edição de referência: Russell & Norvig, 4ª edição (exemplar físico).** A coluna "Ler ANTES"
usa a numeração da 4ª ed.; equivalências para 2ª e 3ª ed. no fim do arquivo.

A leitura prévia vence na **terça à noite**, não na quarta de manhã.

| # | Data | Conteúdo previsto | Ler ANTES (4ª ed.) | Tarefas / avaliação |
|---|---|---|---|---|
| 1 | qua 19/08 | Apresentação. Agentes e Ambientes. Busca Cega × Informada × Online | **Cap. 2** (todo) + **Cap. 3** (todo) + **§4.5** (busca online) | 🚀 **TAREFA 1 lançada** — TSP com Têmpera Simulada e AG, artigo SBC. Detalhes em `tarefas/tarefa-01-busca.md` |
| 2 | qua 26/08 | Busca informada. Heurísticas (e.g. A\*) | Cap. 3, com foco em **§3.5–3.6** | — |
| 3 | qua 02/09 | Busca local. AG canônico. Representação de Conhecimento | **Cap. 4** — Busca em Ambientes Complexos (§4.1 local e algoritmos evolutivos) — ⚠️ **é o conteúdo da Tarefa 1, leia antes** | 📍 **ANDAMENTO da Tarefa 1** cobrado em aula |
| 4 | qua 09/09 | Representação de Conhecimento / Planejamento [cont] | **Cap. 10** (Repr. de Conhecimento) + **Cap. 11** (Planejamento). *Pré-req: Lógica* — relembrar **Caps. 8 e 9** | — |
| 5 | qua 16/09 | Discussão conceitual sobre abordagens e conteúdo da prova | revisão integrada Caps. 2–4, 10–11 | ✅ **ENTREGA Tarefa 1 [1,0]** |
| 6 | qua 23/09 | — | revisão | 📝 **PROVA 1 — questões abertas [2,0]** (Agentes e Ambientes, Busca, Repr. de Conhecimento) |
| 7 | qua 30/09 | Aprendizado de Máquina: aprendizado simbólico (Árvores de Decisão) | **Cap. 19** — Aprendizado por Exemplos (§19.3 árvores de decisão) | 🚀 **TAREFA 2 lançada** (Aprendizado de Máquina) |
| 8 | qua 07/10 | Árvores de Decisão [cont]. Redes Neurais tradicionais | Cap. 19 + **Cap. 21** (Deep Learning) | — |
| 9 | qua 14/10 | Redes Neurais tradicionais [cont]. MLP | Cap. 21 (redes feedforward, backpropagation) | — |
| 10 | qua 21/10 | MLP [cont]. Tipos de redes, arquiteturas, formas de treinamento. Redes recentes | Cap. 21 (convolucionais, recorrentes, generalização) | — |
| — | **26/10–01/11** | **sem encontro** — semana livre no planejamento | *buffer* | fechar a Tarefa 2 |
| 11 | qua 04/11 | Redes Neurais mais recentes [cont] | Cap. 21 + material complementar | ✅ **ENTREGA Tarefa 2 [1,5]** |
| 12 | qua 11/11 | — | revisão de ML | 📝 **PROVA 2 — questões abertas [2,5]** (Aprendizado de Máquina) |
| 13 | qua 18/11 | Escrita de ensaio **em sala** + discussão | **artigo seminal de Turing** — *Computing Machinery and Intelligence*, Mind 49:433–460, 1950 | ✍️ **Tarefa em sala I [1,0]** |
| 14 | qua 25/11 | Escrita de ensaio **em sala** | artigo sobre tópico avançado em IA *(a definir)* | ✍️ **Tarefa em sala II [1,0]** |
| 15 | qua 02/12 | Escrita de ensaio **em sala** | artigo sobre tópico avançado em **IA e Cognição** *(a definir)* | ✍️ **Tarefa em sala III [1,0]** |
| 16 | qua 09/12 | Discussão da disciplina e desdobramentos da Linha de Sistemas Inteligentes / "IA" | — | — |
| 17 | qua 16/12 | Fechamento. Reserva para imprevistos | — | — |

## Quatro pontos de atenção

1. **A Tarefa 1 é lançada já no encontro 1** e tem *andamento cobrado em aula* no encontro 3
   (02/09), antes da entrega em 16/09. Ou seja: não há como deixar para as duas últimas semanas —
   há um checkpoint público no meio.
2. **19/08 exige dois capítulos**, e você tem 4 dias. É o único encontro com carga dupla de
   leitura. Plano dia a dia em `encontros/encontro-01.md`.
3. **Lógica é pré-requisito declarado** para os encontros 3–4. O slide do professor grifa
   *"Pré Req: Lógica !"* e manda relembrar os Caps. 8 e 9. Se lógica de primeira ordem estiver
   enferrujada, o momento de tratar é a semana do encontro 2, não a do 4.
4. **Duas semanas duplas**: 16/09 (entrega) → 23/09 (prova), e 04/11 (entrega) → 11/11 (prova).
   Use a semana livre de 26/10 para fechar a Tarefa 2.

## Roteiro de leitura do Cap. 2 e 3 (4ª ed.) — encontro 1

| Seção | Tema |
|---|---|
| 2.1 | Agentes e ambientes; função agente × programa agente |
| 2.2 | Bom comportamento: o conceito de racionalidade; medida de desempenho; onisciência × racionalidade |
| 2.3 | A natureza dos ambientes: **PEAS** e as dimensões (observável, agente único/multi, determinístico/estocástico, episódico/sequencial, estático/dinâmico, discreto/contínuo, conhecido/desconhecido) |
| 2.4 | Estrutura dos agentes: reflexo simples → reflexo com modelo → baseado em objetivos → baseado em utilidade → com aprendizado; representações atômica / fatorada / estruturada |
| 3.1–3.2 | Agentes de resolução de problemas; formulação de problema; problemas-exemplo |
| 3.3 | Algoritmos de busca: best-first, estruturas de dados, **caminhos redundantes** (árvore × grafo), medindo desempenho (completude, otimalidade, tempo, espaço) |
| 3.4 | **Busca cega**: BFS, custo uniforme (Dijkstra), DFS, profundidade limitada, aprofundamento iterativo, bidirecional |
| 3.5 | **Busca informada**: gulosa, **A\***, busca satisfatória (A\* ponderado), busca com memória limitada (beam, **IDA\***, RBFS, SMA\*) |
| 3.6 | **Funções heurísticas**: fator de ramificação efetiva, problemas relaxados, bancos de dados de padrões, aprendizado de heurísticas |
| **4.5** | **Busca online** e ambientes desconhecidos (LRTA\*) — *não está no Cap. 3, mas o encontro 1 anuncia busca online* |

> A 4ª ed. junta busca cega **e** informada no Cap. 3 — por isso "Cap. 3 — Busca" já cobre duas
> das três famílias anunciadas. A terceira, busca online, está em §4.5. Vale ler ao menos essa
> seção antes de 19/08, mesmo que o Cap. 4 completo só entre no encontro 3.

## Equivalência entre edições

O professor deu o mapeamento oficial nos slides; a coluna da 4ª ed. é a sua.

| Tema | **4ª ed. (sua)** | 3ª ed. | 2ª ed. (BR, 2004) |
|---|---|---|---|
| Agentes inteligentes | **Cap. 2** | Cap. 2 | Cap. 2 |
| Busca cega | **Cap. 3** | Cap. 3 | Cap. 3 |
| Busca informada, A\*, heurísticas | **Cap. 3** | Cap. 3 | Cap. 4 |
| Além da busca clássica: local, AG, online | **Cap. 4** | Cap. 4 | Cap. 4 |
| Lógica de 1ª ordem e inferência (pré-req.) | **Caps. 8, 9** | Caps. 8, 9 | Caps. 8, 9 |
| Representação de Conhecimento | **Cap. 10** | Cap. 12 | Cap. 10 |
| Planejamento | **Cap. 11** | Cap. 10 | Cap. 11 |
| Aprendizado por exemplos / árvores de decisão | **Cap. 19** | Cap. 18 | Cap. 18 |
| Redes Neurais / Deep Learning | **Cap. 21** | Cap. 18 | Cap. 20 |

## Ementa oficial → onde cai no cronograma

| # | Ementa | Conteúdo | Encontros |
|---|---|---|---|
| 1 | Definição de IA. Histórico | Fundamentos filosóficos, científicos, sociais, tecnológicos | 1, 13 |
| 2 | Resolução de Problemas | Agentes e Ambientes. IA como representação e busca | 1 |
| 3 | Estratégias de pesquisa em espaços de estados | Busca cega, informada, online. Busca local e AG | 1–3 |
| 4 | Conhecimento e Raciocínio | Repr. de conhecimento, abordagem lógica, inferência em Prolog, conhecimento como restrição em buscas | 3–4 |
| 5 | Elaboração de planos | Conhecimento incerto e raciocínio. Planejamento | 4 |
| 6 | Paradigmas | Modelos cognitivos e IA | 13, 15, 16 |
| 7 | Aprendizado | Aprendizado simbólico | 7–8 |
| 8 | Fundamentos de Computação Natural | Redes Neurais. Sistemas Fuzzy | 8–11 |
| 9 | Aplicações | Aplicações práticas de IA | 14–16 |

> **Prolog: confirmado.** O bloco 3 do Moodle traz dois conjuntos de exercícios, oito programas
> `.pl` e dois planejadores completos (STRIPS e POP) sobre o mundo do robô entregador. Instalar o
> SWI-Prolog antes do encontro 4 (09/09).
>
> **Sistemas Fuzzy** continua sem material correspondente em nenhum bloco — segue como pergunta.

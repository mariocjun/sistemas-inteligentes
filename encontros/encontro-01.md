# Encontro 1 — qua 19/08/2026

**Conteúdo:** Apresentação da disciplina. Agentes e Ambientes. Busca Cega × Busca Informada ×
Busca Online.
**Leitura obrigatória prévia:** Russell & Norvig **4ª ed.** — **Cap. 2** e **Cap. 3**, mais
**§4.5** (busca online, anunciada no encontro mas fora do Cap. 3 nesta edição).
**Material de apoio:** `../materiais/01-agentes-e-ambientes/` — ver catálogo comentado lá.
**🚀 Neste encontro é lançada a TAREFA 1** (entrega em 16/09, andamento cobrado em 02/09).

É o encontro mais pesado do semestre em leitura prévia: dois capítulos, quatro dias. O plano
abaixo assume ~10h30. Se o tempo apertar, o **caminho mínimo** está marcado com ⭐ — cobre o
suficiente para participar do debate; o resto se recupera na semana 2, que é mais leve.

---

## Sábado 15/08 — Cap. 2 integral + slides do Tacla (3h00)

⭐ **R&N §2.1–2.4** (2h15):

- §2.1 Agentes e ambientes; **função agente** × **programa de agente**
- §2.2 Racionalidade: por que é definida sobre uma **medida de desempenho externa**;
  onisciência × racionalidade × aprendizado × autonomia
- §2.3 **PEAS**; as dimensões de ambiente: observável (total/parcial), agente único/multiagente,
  determinístico/estocástico, episódico/sequencial, estático/dinâmico, discreto/contínuo,
  conhecido/desconhecido
- ⭐ §2.4 **Tipos de agente**: reflexo simples → reflexo com modelo → baseado em objetivos →
  baseado em utilidade → com aprendizado. Para cada um: que limitação do anterior ele resolve, e a
  que custo. Representações atômica / fatorada / estruturada

**Slides `005a-introducao-agentes-ambientes.pdf`** (45 min): os 34 slides do Prof. Tacla são o
Cap. 2 condensado — passe-os *depois* de ler, como checagem do próprio fichamento. O que estiver
no deck e não estiver no seu fichamento indica seção para reler. Três coisas ali **não estão no
R&N** e rendem pergunta: a definição formal `Env: S × A → ɣ(S)`, a dimensão
competitivo/cooperativo/colaborativo, e os dois trechos de AgentSpeak (reativo × deliberativo).

**Entregável do dia:** uma tabela sua com as dimensões de ambiente aplicadas a 3 domínios
concretos (ex.: xadrez, direção autônoma, diagnóstico médico). Costuma cair em prova aberta.

## Domingo 16/08 — Cap. 3, busca cega (3h00)

⭐ **R&N §3.1–3.4**:

- §3.1–3.2 Agentes de resolução de problemas; **formulação de problema**: estado inicial, ações,
  modelo de transição, teste de objetivo, custo de ação. Formulação de objetivo → de problema →
  busca → execução
- §3.3 Algoritmos de busca: espaço de estados × árvore de busca; **nó** ≠ **estado**; fronteira;
  **caminhos redundantes** (busca em árvore × em grafo, e o que o conjunto de alcançados custa);
  ⭐ as 4 métricas — **completude, otimalidade, complexidade de tempo, complexidade de espaço**
- §3.4 **Busca cega**: BFS, custo uniforme (Dijkstra), DFS, profundidade limitada,
  **aprofundamento iterativo**, bidirecional

Ao ler cada algoritmo, preencha você a linha da tabela comparativa (b, d, m, ℓ) **antes** de olhar
a tabela pronta do livro. Depois confira. As divergências viram pergunta.

**Fechar o dia** (30 min) com os 22 slides de `00_a_Historico_HSSF.pdf` — é o deck do próprio
professor, e monta a tensão **símbolos físicos × cognição corporificada** que atravessa o
semestre. Mais o slide único do IJCAI 2020, 5 minutos.

## Segunda 17/08 — Busca informada (2h30)

⭐ **R&N §3.5–3.6**:

- §3.5 Busca best-first; função de avaliação f(n); busca gulosa
- ⭐ **A\***: f = g + h; condições de otimalidade; **admissibilidade** × **consistência**
  (monotonicidade); por que a busca em grafo exige a condição mais forte
- §3.5 Busca satisfatória (A\* ponderado) e busca com **memória limitada**: beam, **IDA\***, RBFS,
  SMA\* — todos motivados por **espaço**, não por tempo
- ⭐ §3.6 **Funções heurísticas**: obtenção por **relaxamento do problema**, bancos de dados de
  padrões, **dominância**, **fator de ramificação efetiva**

## Terça 18/08 — Busca online + código + perguntas (2h30)

- ⭐ **§4.5** Agentes de busca online e ambientes desconhecidos: DFS online, **LRTA\***,
  **razão de competitividade**, exploração. Por que a busca offline clássica não se aplica
- ⭐ **Implementar** BFS, DFS, UCS, gulosa e A\* sobre uma única interface de problema e rodá-los
  no mesmo grafo, contando nós expandidos / nós em memória / custo da solução
  (ver `../implementacoes/README.md`). Não precisa estar bonito — precisa produzir números
- ⭐ Escrever as 3–5 perguntas para o debate
- 15 min: folhear só os **índices** de Coelho e Vidal em `../materiais/01-agentes-e-ambientes/Teoria_de_Agencia_SMA/`,
  para saber o que existe ali. Não ler agora

## Quarta 19/08, manhã — revisão (0h30)

Reler o próprio fichamento e as perguntas. Levar impressas ou em tela. E ir preparado para
**receber o enunciado da Tarefa 1** — anotar formato, critérios e se é individual ou em dupla.

---

## Perguntas candidatas para o debate

O professor pediu para chegar com "questões que provocaram descobertas, curiosidades e
inquietações". Os slides reforçam o critério: o que se avalia é **localizar a prática no marco
conceitual e vice-versa — o POR QUÊ, dado que um certo COMO foi escolhido**. Estas são sementes;
**substituir pelas suas**, e levar as 3–5 que você realmente não conseguiu fechar sozinho.

**Sobre agentes (Cap. 2)**

1. A racionalidade é definida sobre uma medida de desempenho **externa** ao agente. Que problemas
   aparecem se ela for definida sobre o objetivo interno do próprio agente? Há paralelo com
   especificação × implementação, de PAA?
2. A função agente é uma tabela (potencialmente infinita) e o programa de agente é sua realização
   finita. Se toda IA é, nesse sentido, uma compressão de tabela, a questão central da área é
   representação ou é busca?
3. A escada reflexo → modelo → objetivo → utilidade é hierarquia de **expressividade** ou de
   **custo computacional**? Um agente de utilidade sempre domina um reflexo?
4. *(a partir do deck do Tacla)* Formalizando ambiente como `Env: S × A → ɣ(S)`, determinístico é
   `|ɣ(S)| = 1`. O deck registra que o R&N **ignora a incerteza originada pelo próprio agente**
   nessa classificação. Por que essa escolha de modelagem, e o que ela esconde?
5. *(idem)* O deck separa **competitivo / cooperativo / colaborativo** como dimensão própria; o
   R&N dissolve isso em "multiagente". Qual das duas escolhas de modelagem é mais defensável, e
   sob que critério?

**Sobre busca (Cap. 3)**

6. Por que em custo uniforme o teste de objetivo é aplicado na **expansão** e não na geração do
   nó? Que garantia se perde ao antecipá-lo — e por que em BFS a antecipação é segura?
7. A busca em grafo poda caminhos redundantes. Em que condição essa poda descarta um caminho
   melhor, e por que a **consistência** da heurística é exatamente a hipótese que impede isso?
8. Admissibilidade garante otimalidade em busca em árvore; consistência é exigida em busca em
   grafo. Por que a diferença é sobre a **estrutura do espaço** e não sobre a heurística em si?
9. IDS e IDA\* recomputam trabalho **de propósito**. Em PAA isso soaria desperdício. Sob qual
   métrica a troca compensa, e o que isso revela sobre o gargalo real da busca em IA?
10. Heurística obtida por relaxamento do problema é sempre admissível. Isso é uma prova geral ou
    uma construção válida só para certas relaxações? Onde está o argumento?
11. Se h₁ domina h₂ e ambas são admissíveis, A\* com h₁ nunca expande mais nós. O **custo de
    calcular** h₁ entra nessa comparação? Como se decide na prática?

**Integrando os dois capítulos**

12. A busca clássica do Cap. 3 assume ambiente **determinístico, estático, totalmente observável,
    discreto e conhecido** — dimensões do Cap. 2. Relaxando uma de cada vez, qual algoritmo
    responde a qual relaxamento? Busca online responde a "desconhecido" ou a "parcialmente
    observável"?
13. Se o ambiente é dinâmico, o tempo gasto planejando altera a medida de desempenho. Como o
    modelo de busca offline sequer acomoda esse custo — ou ele é simplesmente ignorado?

**A partir do deck histórico do professor**

14. A Hipótese do Sistema de Símbolos Físicos (Newell & Simon, 1976) afirma que símbolos físicos
    são **necessários e suficientes** para ação inteligente geral. A busca do Cap. 3 é um caso
    exemplar dessa hipótese. O que exatamente "Elefantes não jogam xadrez" (Brooks) ataca: a
    suficiência, a necessidade, ou ambas?
15. Um agente reativo à la Brooks tem função agente bem definida no sentido do Cap. 2, mas nenhum
    modelo explícito do mundo. Isso o coloca fora do arcabouço do R&N, ou apenas no degrau mais
    baixo da escada de §2.4?

## Perguntas administrativas para o encontro 1

- [ ] **Tarefa 1**: formato de entrega, linguagem, peso relatório × código, o que é aceito como
      biblioteca (numpy conta como "framework"?), e o que será cobrado no *andamento* de 02/09
- [ ] Tarefas são **individuais ou em dupla**? Vale para as duas? Pode trocar de parceria?
- [ ] Como funciona a **"defesa de tarefas"** citada na conformação da nota final
- [ ] Quando serão anunciados os artigos das Tarefas em Sala II e III (25/11 e 02/12)
- [ ] **Prolog** e **Sistemas Fuzzy** estão na ementa mas não no planejamento — entram?
- [ ] As **tarefas opcionais** mencionadas nos slides: como e quando são lançadas, e como pontuam
- [ ] O deck histórico termina em "continua…" — haverá uma parte II em bloco posterior?

## Depois do encontro

Preencher na quinta (bloco de consolidação):

**Enunciado da Tarefa 1 — o que foi pedido:**

**O que foi debatido além do previsto:**

**Perguntas minhas que ficaram sem resposta:**

**Ponte conceitual anunciada para o encontro 2:**

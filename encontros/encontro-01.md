# Encontro 1 — qua 19/08/2026

**Conteúdo:** Apresentação da disciplina. Agentes e Ambientes. Busca Cega × Busca Informada ×
Busca Online.
**Leitura obrigatória prévia:** Russell & Norvig — Cap. 2 (Agentes) e Cap. 3 (Busca).
Na 2ª ed. brasileira, busca informada e online estão no Cap. 4 — ver tabela em `../cronograma.md`.

É o encontro mais pesado do semestre em leitura prévia: dois capítulos, quatro dias. O plano
abaixo assume ~10h30. Se o tempo apertar, o **caminho mínimo** está marcado com ⭐ — cobre o
suficiente para participar do debate; o resto se recupera na semana 2, que é mais leve.

---

## Sábado 15/08 — Cap. 2, integral (2h30)

⭐ Alvos de leitura:

- Agente, percepção, sequência de percepções; **função agente** × **programa de agente**
- Racionalidade: por que é definida sobre uma **medida de desempenho externa**
- Onisciência × racionalidade × aprendizado
- **PEAS** — especificar o ambiente de tarefa
- **Propriedades de ambientes**: observável (total/parcial), agente único/multiagente,
  determinístico/estocástico, episódico/sequencial, estático/dinâmico, discreto/contínuo,
  conhecido/desconhecido
- ⭐ **Tipos de agente**: reflexo simples → reflexo com modelo → baseado em objetivos → baseado
  em utilidade → com aprendizado. Para cada um: que limitação do anterior ele resolve, e a que custo
- Representação atômica / fatorada / estruturada

Entregável do dia: uma tabela sua com as 7 dimensões de ambiente aplicadas a 3 domínios
concretos (ex.: xadrez, direção autônoma, diagnóstico médico). Isso costuma cair em prova aberta.

## Domingo 16/08 — Cap. 3, busca cega (3h00)

⭐ Alvos:

- **Formulação de problema**: estado inicial, ações, modelo de transição, teste de objetivo,
  custo de caminho. Formulação de objetivo → formulação de problema → busca → execução
- Espaço de estados × árvore de busca; **nó** ≠ **estado**; fronteira; conjunto explorado
- **Busca em árvore × busca em grafo** — o que o conjunto explorado compra e o que ele custa
- ⭐ As 4 métricas: **completude, otimalidade, complexidade de tempo, complexidade de espaço**
- BFS, custo uniforme, DFS, profundidade limitada, **aprofundamento iterativo**, bidirecional

Ao ler cada algoritmo, preencher a linha da tabela comparativa (b, d, m, ℓ) **antes** de olhar a
tabela pronta do livro. Depois conferir. As divergências viram pergunta.

## Segunda 17/08 — Busca informada (2h30)

⭐ Alvos:

- Busca best-first; função de avaliação f(n); busca gulosa
- ⭐ **A\***: f = g + h; condições de otimalidade; **admissibilidade** × **consistência**
  (monotonicidade); por que busca em grafo exige a condição mais forte
- Contornos, A\* é otimamente eficiente, e por que ainda assim é impraticável em memória
- IDA\*, RBFS, SMA\* — todos motivados por **espaço**, não por tempo
- ⭐ Heurísticas: obtenção por **relaxamento do problema**, bancos de dados de padrões,
  **dominância**, fator de ramificação efetiva

## Terça 18/08 — Busca online + código + perguntas (2h30)

- Busca online: agente de busca online, DFS online, LRTA\*, **razão de competitividade**,
  exploração × exploração de conhecimento. Por que a busca offline clássica não se aplica
- ⭐ **Implementar** BFS, DFS, UCS, gulosa e A\* sobre uma única interface de problema e rodá-los
  no mesmo grafo, contando nós expandidos / nós em memória / custo da solução (ver
  `../implementacoes/README.md`). Não precisa estar bonito — precisa produzir números
- ⭐ Escrever as 3–5 perguntas para o debate (seção abaixo)

## Quarta 19/08, manhã — revisão (0h30)

Reler o próprio fichamento e as perguntas. Levar impressas ou em tela — perguntar exige ter a
formulação pronta, não improvisar no momento.

---

## Perguntas candidatas para o debate

O professor pediu para chegar com "questões que provocaram descobertas, curiosidades e
inquietações". Estas são sementes — **substituir pelas suas** conforme a leitura, e escolher as
3–5 que você realmente não conseguiu resolver sozinho.

**Sobre agentes (Cap. 2)**

1. A racionalidade é definida sobre uma medida de desempenho externa ao agente. Que problemas
   aparecem se ela for definida sobre o objetivo interno do próprio agente? Isso tem paralelo em
   especificação × implementação, de PAA?
2. A função agente é uma tabela (potencialmente infinita) e o programa de agente é sua realização
   finita. Se toda IA é, nesse sentido, uma compressão de tabela, a questão central da área é
   representação ou é busca?
3. A escada reflexo → modelo → objetivo → utilidade é uma hierarquia de expressividade ou de
   custo computacional? Um agente de utilidade sempre domina um reflexo?

**Sobre busca (Cap. 3)**

4. Por que o teste de objetivo em custo uniforme é aplicado na **expansão** e não na geração do nó?
   Que garantia se perde ao antecipá-lo — e por que em BFS a antecipação é segura?
5. A busca em grafo poda estados repetidos. Em que condição essa poda descarta um caminho melhor,
   e por que a consistência da heurística é exatamente a hipótese que impede isso?
6. Admissibilidade garante otimalidade em busca em árvore; consistência é exigida em busca em
   grafo. Por que a diferença é sobre a **estrutura do espaço** e não sobre a heurística em si?
7. IDS e IDA\* recomputam trabalho de propósito. Em PAA isso soaria desperdício. Qual é a métrica
   sob a qual a troca compensa, e o que ela revela sobre o gargalo real da busca em IA?
8. Heurística obtida por relaxamento do problema é sempre admissível. Isso é uma prova geral ou
   uma construção que só vale para certas relaxações? Onde está o argumento?
9. Se h₁ domina h₂ e ambas são admissíveis, A\* com h₁ nunca expande mais nós. O custo de calcular
   h₁ entra nessa comparação? Como se decide na prática?

**Integrando os dois capítulos**

10. A busca clássica do Cap. 3 assume ambiente **determinístico, estático, totalmente observável,
    discreto e conhecido** — as cinco propriedades do Cap. 2. Relaxando uma de cada vez, qual
    algoritmo responde a qual relaxamento? Busca online é a resposta a *qual* propriedade
    exatamente: "desconhecido" ou "parcialmente observável"?
11. Se o ambiente é dinâmico, o tempo gasto planejando muda a medida de desempenho. Como o
    modelo de busca offline sequer acomoda esse custo — ou ele é simplesmente ignorado?

## Perguntas administrativas para o encontro 1

- [ ] Formato exato das Tarefas de Busca e de ML: linguagem, o que se entrega, peso do relatório
      × código, uso de bibliotecas permitido (numpy conta como framework?)
- [ ] Como funciona a **recuperação processual** citada nos procedimentos de avaliação
- [ ] Quando serão anunciados os artigos das Tarefas em Sala II e III (25/11 e 02/12)
- [ ] **Prolog** e **Sistemas Fuzzy** estão na ementa mas não no planejamento semanal — entram?
- [ ] Duplas: valem para as duas tarefas? Pode trocar de parceria entre elas?
- [ ] Edição do Russell & Norvig adotada como referência de numeração de capítulos

## Depois do encontro

Preencher na quinta (bloco de consolidação):

**O que foi debatido além do previsto:**

**Perguntas minhas que ficaram sem resposta:**

**Ponte conceitual anunciada para o encontro 2:**

# Métodos Determinísticos e Procedimentais de Cálculo para Sistemas Operacionais (Prof. Carlos Maziero - UFPR)

Este guia apresenta técnicas puramente **matemáticas, lógicas e tabulares** para resolver todas as "continhas" e algoritmos das três Avaliações Teóricas (AT01, AT02 e AT03) **sem precisar desenhar gráficos de Gantt tick por tick ou diagramas à mão**.

---

# Sumário Geral por Avaliação

1. **AT01 (Capítulos 01 a 09 - Partes I, II e III)**
   - Definições e Relações Fundamentais de Escalonamento de CPU
   - O Método Universal dos Marcos Críticos (Event-Driven Table)
   - Resolução Determinística: FCFS (First-Come, First-Served)
   - Resolução Determinística: SJF (Shortest Job First - Cooperativo)
   - Resolução Determinística: SRTF (Shortest Remaining Time First - Preemptivo)
   - Resolução Determinística: PRIOc (Prioridade Estática Cooperativa)
   - Resolução Determinística: PRIOp (Prioridade Estática Preemptiva)
   - Resolução Determinística: RR (Round-Robin / Revezamento por Quantum)
   - Resolução Determinística: PRIOd (Prioridade Dinâmica / Aging / Envelhecimento)
   - Validação Completa com o Exemplo Oficial dos Slides ($t_1$ a $t_5$)

2. **AT02 (Capítulos 10 a 18 - Partes III e IV)**
   - Cap 10: Condições de Bernstein para Concorrência Determinística (Álgebra de Conjuntos)
   - Cap 13: Impasses e Teste de Estado Seguro (Algoritmo do Banqueiro)
   - Cap 14: Memória Virtual e Tradução de Endereços (Aritmética Binária / Hexa)
   - Cap 14: Dimensionamento de Tabelas de Páginas e Paginação Multinível
   - Cap 16: Alocador Buddy System (Operador XOR e Árvore Binária)
   - Cap 17: Substituição de Páginas (FIFO, ÓTIMO, LRU, Segunda-Chance/Relógio) sem Desenhar Molduras

3. **AT03 (Capítulos 19 a 25 - Partes V e VI)**
   - Cap 21: Escalonamento de Braço de Disco (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK) via Fórmulas Fechadas
   - Cap 21: Cálculos de Arranjos RAID (Capacidade Útil, Sobrecarga e Álgebra XOR)
   - Cap 24: Cálculo de Tamanho Máximo de Arquivos em Inodes Multinível (Ext2/Ext3/Unix)
   - Cap 24: Resolução de Acesso Direto de Byte $\to$ Bloco Físico

---

# PARTE 1 — AVALIAÇÃO TEÓRICA 01 (AT01)
## Capítulos 01 a 09: Escalonamento de Tarefas (Slide 06)

### 1.1 Relações Algébricas Fundamentais (Invariantes)

Para qualquer algoritmo de escalonamento, dada uma tarefa $i$ com:
- $c_i$: Instante de ingresso / chegada (arrival)
- $d_i$: Duração / tempo de CPU necessário (burst)
- $f_i$: Instante em que a tarefa conclui sua execução (fim)
- $p_i$: Instante em que a tarefa ganha a CPU pela primeira vez (primeira execução)

As métricas individuais e médias são dadas **estritamente por aritmética elementar**:

$$\begin{aligned}
\text{Tempo de Vida / Retorno (Turnaround):} \quad & t_t(i) = f_i - c_i \\
\text{Tempo de Espera (Waiting):} \quad & t_w(i) = t_t(i) - d_i = (f_i - c_i) - d_i \\
\text{Tempo de Resposta (Response):} \quad & t_r(i) = p_i - c_i \\
\text{Médias para } N \text{ tarefas:} \quad & T_t = \frac{1}{N}\sum_{i=1}^N t_t(i), \quad T_w = \frac{1}{N}\sum_{i=1}^N t_w(i)
\end{aligned}$$

> **Teorema de Redução de Esforço**:
> Para achar $t_w$, **nunca** conte os buracos vazios no tempo! Basta encontrar **$f_i$** (quando a tarefa acabou) e aplicar:
> $$t_w(i) = f_i - c_i - d_i$$

---

### 1.2 O Método dos Marcos Críticos (Sem desenhar Gantt)

Em vez de desenhar uma linha do tempo com 14 ou 100 segundos, observe que **a CPU só muda de decisão em instantes críticos**:
$$\mathcal{T}_{\text{críticos}} = \{ c_i \mid i \text{ ingressa no sistema} \} \cup \{ f_{\text{bloco}} \mid \text{tarefa termina ou esgota seu quantum}\} $$

Tudo o que você precisa no papel é uma **Tabela de Marcos**:
1. Relógio atual $t$.
2. Fila de tarefas prontas $R(t) = \{ i \mid c_i \le t \text{ e tarefa } i \text{ ainda tem } d_{rem}(i) > 0 \}$.
3. Regra de desempate / seleção do algoritmo.

---

### 1.3 Dados do Exemplo Canônico do Professor Maziero (Slide 06)

| Tarefa | Ingresso ($c_i$) | Duração ($d_i$) | Prioridade ($p_i$) |
| :---: | :---: | :---: | :---: |
| **$t_1$** | 0 | 5 | 2 |
| **$t_2$** | 0 | 2 | 3 |
| **$t_3$** | 1 | 4 | 1 |
| **$t_4$** | 3 | 1 | 4 |
| **$t_5$** | 5 | 2 | 5 |

*(Convenção Maziero: maior número = maior prioridade)*.

---

### 1.4 Algoritmos Cooperativos / Não-Preemptivos (FCFS, SJF, PRIOc)

Nos algoritmos não-preemptivos, uma vez que uma tarefa assume a CPU no instante $inicio$, ela roda ininterruptamente até $fim = inicio + d_i$.

#### A) FCFS (First-Come, First-Served)
- **Critério**: Ordenar por $c_i$. Se empate em $c_i$, usar a ordem de índice ($t_1, t_2$).
- **Procedimento Algébrico**:
  - $t = 0$: executa $t_1$ ($d=5$) $\implies f(t_1) = 0 + 5 = 5$.
  - $t = 5$: prontas $\{t_2, t_3, t_4, t_5\}$. Ordem de chegada: $t_2 (c=0) \to t_3 (c=1) \to t_4 (c=3) \to t_5 (c=5)$.
  - $t_2$ executa: $5 + 2 = 7 \implies f(t_2) = 7$.
  - $t_3$ executa: $7 + 4 = 11 \implies f(t_3) = 11$.
  - $t_4$ executa: $11 + 1 = 12 \implies f(t_4) = 12$.
  - $t_5$ executa: $12 + 2 = 14 \implies f(t_5) = 14$.

**Tabela de Resultados Imediatos**:
| Tarefa | $c$ | $d$ | $f$ | $t_t = f - c$ | $t_w = t_t - d$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $t_1$ | 0 | 5 | 5 | $5 - 0 = 5$ | $5 - 5 = \mathbf{0}$ |
| $t_2$ | 0 | 2 | 7 | $7 - 0 = 7$ | $7 - 2 = \mathbf{5}$ |
| $t_3$ | 1 | 4 | 11 | $11 - 1 = 10$ | $10 - 4 = \mathbf{6}$ |
| $t_4$ | 3 | 1 | 12 | $12 - 3 = 9$ | $9 - 1 = \mathbf{8}$ |
| $t_5$ | 5 | 2 | 14 | $14 - 5 = 9$ | $9 - 2 = \mathbf{7}$ |
| **Total / Média** | | | | **40 / 5 = 8,0 s** | **26 / 5 = 5,2 s** |

---

#### B) SJF (Shortest Job First - Não-Preemptivo)
- **Critério**: No instante de término da tarefa anterior, escolher do conjunto de prontas a de **menor duração $d_i$**.
- **Procedimento Algébrico Passo a Passo**:
  - $t = 0$: Prontas $\{t_1 (d=5), t_2 (d=2)\}$. Menor $d$ é $t_2$.
    - Executa $t_2$: $f(t_2) = 0 + 2 = 2$.
  - $t = 2$: Prontas $\{t_1 (d=5), t_3 (d=4)\}$. Menor $d$ é $t_3$.
    - Executa $t_3$: $f(t_3) = 2 + 4 = 6$.
  - $t = 6$: Prontas $\{t_1 (d=5), t_4 (d=1), t_5 (d=2)\}$. Menor $d$ é $t_4$.
    - Executa $t_4$: $f(t_4) = 6 + 1 = 7$.
  - $t = 7$: Prontas $\{t_1 (d=5), t_5 (d=2)\}$. Menor $d$ é $t_5$.
    - Executa $t_5$: $f(t_5) = 7 + 2 = 9$.
  - $t = 9$: Apenas $\{t_1 (d=5)\}$ resta.
    - Executa $t_1$: $f(t_1) = 9 + 5 = 14$.

**Resultados**:
- $f = [t_1: 14, t_2: 2, t_3: 6, t_4: 7, t_5: 9]$
- $t_t = [14, 2, 5, 4, 4] \implies T_t = 29 / 5 = \mathbf{5,8\text{ s}}$
- $t_w = t_t - d = [9, 0, 1, 3, 2] \implies T_w = 15 / 5 = \mathbf{3,0\text{ s}}$

---

#### C) PRIOc (Prioridade Cooperativa / Não-Preemptiva)
- **Critério**: No instante de término, escolher do conjunto de prontas a de **maior prioridade $p_i$**.
- **Procedimento Passo a Passo**:
  - $t = 0$: Prontas $\{t_1(p=2), t_2(p=3)\}$. Maior prioridade: $t_2$.
    - Executa $t_2$: $f(t_2) = 0 + 2 = 2$.
  - $t = 2$: Prontas $\{t_1(p=2), t_3(p=1)\}$. Maior prioridade: $t_1$.
    - Executa $t_1$: $f(t_1) = 2 + 5 = 7$.
  - $t = 7$: Prontas $\{t_3(p=1), t_4(p=4), t_5(p=5)\}$. Maior prioridade: $t_5$.
    - Executa $t_5$: $f(t_5) = 7 + 2 = 9$.
  - $t = 9$: Prontas $\{t_3(p=1), t_4(p=4)\}$. Maior prioridade: $t_4$.
    - Executa $t_4$: $f(t_4) = 9 + 1 = 10$.
  - $t = 10$: Resta $t_3$.
    - Executa $t_3$: $f(t_3) = 10 + 4 = 14$.

**Resultados**:
- $f = [t_1: 7, t_2: 2, t_3: 14, t_4: 10, t_5: 9]$
- $t_t = [7, 2, 13, 7, 4] \implies T_t = 33 / 5 = \mathbf{6,6\text{ s}}$
- $t_w = t_t - d = [2, 0, 9, 6, 2] \implies T_w = 19 / 5 = \mathbf{3,8\text{ s}}$

---

### 1.5 Algoritmos Preemptivos (SRTF, PRIOp, RR, PRIOd)

Aqui há preempção. O método puramente procedural consiste em atualizar um **Vetor de Estado das Tarefas** apenas nos **instantes de evento**:
$$\text{Instantes de Chegada: } \{0, 1, 3, 5\}$$

#### D) SRTF (Shortest Remaining Time First)
- **Regra de Preempção**: Quando uma nova tarefa $j$ chega em $t_{chegada}$, ela preempta a tarefa atual $i$ **se e somente se**:
  $$d(j) < d_{\text{restante}}(i)$$
- **Execução por Intervalos de Evento**:
  - $t = 0$: Chegam $t_1 (rem=5)$ e $t_2 (rem=2)$. Escolhe $t_2$. Próximo evento de chegada: $t=1$.
  - $t \in [0, 1]$: $t_2$ roda por 1 s. $rem(t_2) = 1$.
  - $t = 1$: Chega $t_3 (d=4)$. Compara: $rem(t_2)=1 \le d(t_3)=4 \implies$ Não preempta!
  - $t = 2$: $t_2$ conclui! $\mathbf{f(t_2) = 2}$.
    - Prontas: $\{t_1(rem=5), t_3(rem=4)\}$. Menor restante: $t_3$. Próxima chegada: $t=3$.
  - $t \in [2, 3]$: $t_3$ roda por 1 s. $rem(t_3) = 3$.
  - $t = 3$: Chega $t_4 (d=1)$. Compara: $d(t_4)=1 < rem(t_3)=3 \implies$ **PREEMPTA $t_3$**!
    - $t_4$ roda. Como $d(t_4)=1$, vai até $t = 3 + 1 = 4$.
  - $t = 4$: $t_4$ conclui! $\mathbf{f(t_4) = 4}$.
    - Prontas: $\{t_1(rem=5), t_3(rem=3)\}$. Escolhe $t_3$. Próxima chegada: $t=5$.
  - $t \in [4, 5]$: $t_3$ roda por 1 s. $rem(t_3) = 2$.
  - $t = 5$: Chega $t_5 (d=2)$. Compara: $d(t_5)=2$ vs $rem(t_3)=2$ (empate, não preempta).
    - Não há mais chegadas! Agora executa como SJF simples pelo restante:
    - $t_3$ conclui seu resto (2 s): termina em $t = 5 + 2 = 7 \implies \mathbf{f(t_3) = 7}$.
    - Prontas: $\{t_5(rem=2), t_1(rem=5)\}$. Executa $t_5$: termina em $7 + 2 = 9 \implies \mathbf{f(t_5) = 9}$.
    - Executa $t_1$: termina em $9 + 5 = 14 \implies \mathbf{f(t_1) = 14}$.

**Resultados**:
- $f = [t_1: 14, t_2: 2, t_3: 7, t_4: 4, t_5: 9]$
- $t_t = [14-0, 2-0, 7-1, 4-3, 9-5] = [14, 2, 6, 1, 4] \implies T_t = 27 / 5 = \mathbf{5,4\text{ s}}$
- $t_w = t_t - d = [9, 0, 2, 0, 2] \implies T_w = 13 / 5 = \mathbf{2,6\text{ s}}$

---

#### E) PRIOp (Prioridade Preemptiva)
- **Regra de Preempção**: Uma tarefa $j$ que chega em $t$ preempta a atual $i$ se $p(j) > p(i)$.
- **Passo a Passo**:
  - $t = 0$: Prontas $t_1(p=2), t_2(p=3)$. Executa $t_2$.
  - $t = 1$: Chega $t_3(p=1)$. $p(t_3) < p(t_2) \implies$ não preempta.
  - $t = 2$: $t_2$ termina! $\mathbf{f(t_2) = 2}$.
    - Prontas: $t_1(p=2), t_3(p=1)$. Executa $t_1$.
  - $t = 3$: Chega $t_4(p=4)$. Como $p(t_4) = 4 > p(t_1) = 2 \implies$ **PREEMPTA $t_1$** (t1 rodou 1 s, restam 4 s).
  - $t = 4$: $t_4$ roda por 1 s e conclui! $\mathbf{f(t_4) = 4}$.
    - Prontas: $t_1(p=2, rem=4), t_3(p=1, rem=4)$. Executa $t_1$.
  - $t = 5$: Chega $t_5(p=5)$. Como $p(t_5) = 5 > p(t_1) = 2 \implies$ **PREEMPTA $t_1$** (t1 rodou mais 1 s, restam 3 s).
  - $t_5$ roda seus 2 s e conclui em $t = 5 + 2 = 7 \implies \mathbf{f(t_5) = 7}$.
  - Fim das chegadas. Executa por prioridade restante:
    - $t_1(p=2)$ roda seus 3 s restantes: $7 + 3 = 10 \implies \mathbf{f(t_1) = 10}$.
    - $t_3(p=1)$ roda seus 4 s: $10 + 4 = 14 \implies \mathbf{f(t_3) = 14}$.

**Resultados**:
- $f = [t_1: 10, t_2: 2, t_3: 14, t_4: 4, t_5: 7]$
- $t_t = [10-0, 2-0, 14-1, 4-3, 7-5] = [10, 2, 13, 1, 2] \implies T_t = 28 / 5 = \mathbf{5,6\text{ s}}$
- $t_w = t_t - d = [5, 0, 9, 0, 0] \implies T_w = 14 / 5 = \mathbf{2,8\text{ s}}$

---

#### F) Round-Robin (RR com Quantum $q = 2$)
- **Rastreamento Procedimental da Fila**:
  Apenas mantenha a **fila FIFO de prontas** nos instantes de troca de quantum ou término.
  *Regra canônica do slide 11 do Maziero*: tarefas que chegam durante ou exatamente no término do quantum entram na fila **antes** da tarefa que sofreu preempção de quantum.

| Instante $t$ | Tarefa na CPU | Duração do Bloco | Restante pós-bloco | Fila de Espera Resultante |
| :---: | :---: | :---: | :---: | :--- |
| $0$ | $t_1$ | 2 | $t_1: 3$ | Inicial: $[t_2]$; $t=1$ entra $t_3$. Fim do $q$: entra $t_1$. Fila: $[t_2, t_3, t_1]$ |
| $2$ | $t_2$ | 2 | $t_2: 0$ (FIM) | $t=3$ entra $t_4$. Fila: $[t_3, t_1, t_4]$. $\mathbf{f(t_2) = 4}$ |
| $4$ | $t_3$ | 2 | $t_3: 2$ | $t=5$ entra $t_5$. Fim do $q$: entra $t_3$. Fila: $[t_1, t_4, t_5, t_3]$ |
| $6$ | $t_1$ | 2 | $t_1: 1$ | Fim do $q$: entra $t_1$. Fila: $[t_4, t_5, t_3, t_1]$ |
| $8$ | $t_4$ | 1 (precisa só 1) | $t_4: 0$ (FIM) | Terminou em $t=9$! Fila: $[t_5, t_3, t_1]$. $\mathbf{f(t_4) = 9}$ |
| $9$ | $t_5$ | 2 | $t_5: 0$ (FIM) | Terminou em $t=11$! Fila: $[t_3, t_1]$. $\mathbf{f(t_5) = 11}$ |
| $11$ | $t_3$ | 2 | $t_3: 0$ (FIM) | Terminou em $t=13$! Fila: $[t_1]$. $\mathbf{f(t_3) = 13}$ |
| $13$ | $t_1$ | 1 | $t_1: 0$ (FIM) | Terminou em $t=14$! $\mathbf{f(t_1) = 14}$ |

**Resultados**:
- $f = [t_1: 14, t_2: 4, t_3: 13, t_4: 9, t_5: 11]$
- $t_t = [14-0, 4-0, 13-1, 9-3, 11-5] = [14, 4, 12, 6, 6] \implies T_t = 42 / 5 = \mathbf{8,4\text{ s}}$
- $t_w = t_t - d = [9, 2, 8, 5, 4] \implies T_w = 28 / 5 = \mathbf{5,6\text{ s}}$

---

#### G) PRIOd (Aging / Envelhecimento com $\alpha = 1$)
- **Regras Matemáticas (Slide 22)**:
  - Prioridade dinâmica inicial: $pd_i = pe_i$.
  - A cada decisão a cada segundo ($q=1$):
    - Escolhe $t_{\text{prox}}$ com maior $pd$.
    - Reseta a prioridade de quem executa: $pd_{\text{prox}} \leftarrow pe_{\text{prox}}$.
    - Incrementa todas as outras prontas: $pd_j \leftarrow pd_j + 1 \quad (\forall j \neq \text{prox})$.
- **Evolução Determinística**:
  - $t=0$: $t_1(pd=2), t_2(pd=3)$. Escolhe $t_2$.
  - $t=1$: $t_2$ roda. Chega $t_3(pd=1)$. $pd(t_1) = 2+1=3$. $pd(t_2)$ reseta para 3. Escolhe $t_2$ de novo.
  - $t=2$: $t_2$ conclui ($\mathbf{f(t_2)=2}$). Prontas: $t_1(pd=4), t_3(pd=2)$. Escolhe $t_1$.
  - $t=3$: Chega $t_4(pd=4)$. $t_1$ reseta para 2. $t_3$ sobe para 3. Escolhe $t_4$.
  - $t=4$: $t_4$ conclui ($\mathbf{f(t_4)=4}$). Prontas: $t_1(pd=3), t_3(pd=4)$. Escolhe $t_3$.
  - $t=5$: Chega $t_5(pd=5)$. $t_3$ reseta para 1. $t_1$ sobe para 4. Escolhe $t_5$.
  - $t=6$: $t_5$ reseta para 5, $t_1$ sobe para 5, $t_3$ sobe para 2. Desempate por maior estática: $t_5$.
  - $t=7$: $t_5$ conclui ($\mathbf{f(t_5)=7}$). Prontas: $t_1(pd=6), t_3(pd=3)$. Escolhe $t_1$.
  - Seguindo a regra: $t_1$ conclui em $t=11$ ($\mathbf{f(t_1)=11}$) e $t_3$ em $t=14$ ($\mathbf{f(t_3)=14}$).

**Resultados**:
- $t_t = [11, 2, 13, 1, 2] \implies T_t = 29 / 5 = \mathbf{5,8\text{ s}}$
- $t_w = t_t - d = [6, 0, 9, 0, 0] \implies T_w = 15 / 5 = \mathbf{3,0\text{ s}}$

---

# PARTE 2 — AVALIAÇÃO TEÓRICA 02 (AT02)
## Capítulos 10 a 18: Concorrência, Impasses e Memória Virtual

### 2.1 Condições de Bernstein para Concorrência (Capítulo 10)

Para duas tarefas ou blocos de código $T_1$ e $T_2$ poderem executar concorrentemente de forma **determinística** (sem condições de corrida), seus conjuntos de leitura $R$ (variáveis lidas) e escrita $W$ (variáveis modificadas) devem satisfazer:

$$\begin{aligned}
1. \quad & R(T_1) \cap W(T_2) = \emptyset \\
2. \quad & W(T_1) \cap R(T_2) = \emptyset \\
3. \quad & W(T_1) \cap W(T_2) = \emptyset
\end{aligned}$$

**Procedimento de Prova**:
1. Liste explicitamente $R(T_i)$ e $W(T_i)$ para cada trecho.
2. Faça a interseção de pares. Se todas as 3 forem o conjunto vazio $\emptyset$, podem rodar em paralelo. Se qualquer uma $\neq \emptyset$, há dependência de dados (leitura após escrita, escrita após leitura ou escrita após escrita).

---

### 2.2 Impasses: Algoritmo do Banqueiro e Teste de Segurança (Capítulo 13)

Dadas $n$ tarefas e $m$ tipos de recursos:
- Matriz de Alocação: $Aloc_{n \times m}$
- Matriz de Máximo: $Max_{n \times m}$
- Vetor de Recursos Disponíveis: $Disp_{1 \times m}$

#### Passo 1: Calcular a Matriz de Necessidade ($Nec$)
$$Nec[i, j] = Max[i, j] - Aloc[i, j]$$

#### Passo 2: Procedimento Determinístico de Simulação (Safety Test)
1. Vetor de trabalho $Trab = Disp$ e vetor $Finalizado[1 \dots n] = [False, \dots, False]$.
2. Encontre um índice $i$ não finalizado tal que:
   $$Nec[i, :] \le Trab[:]$$
3. Se encontrar:
   - A tarefa $i$ pode concluir e devolver todos os seus recursos!
   - Atualize: $Trab \leftarrow Trab + Aloc[i, :]$
   - Marque: $Finalizado[i] = True$
   - Volte ao passo 2.
4. Se todos forem $True \implies$ **Estado SEGURO** (ordem dos índices encontrados é a sequência segura).
5. Se restar algum $False$ e nenhuma tarefa puder ser atendida $\implies$ **Estado INSEGURO** (risco iminente de deadlock).

---

### 2.3 Memória Virtual: Tradução de Endereços e Paginação (Capítulo 14)

#### Fórmulas de Decomposição de Bits
Para um sistema com endereços de $N$ bits e páginas de tamanho $S = 2^k$ bytes:
$$\text{Número de bits de Deslocamento (Offset):} \quad k = \log_2(S)$$
$$\text{Número de bits de Página Virtual (VPN):} \quad p = N - k$$
$$\text{Número de páginas no espaço virtual:} \quad 2^p$$

#### Método Procedimental para Provas (Hexadecimal Direto):
Em provas de SO, os endereços são dados em Hexadecimal e $k$ é quase sempre múltiplo de 4:
- $S = 4 \text{ KB} = 2^{12} \text{ bytes} \implies k = 12 \text{ bits} = \mathbf{3 \text{ dígitos hexa}}$.
- Em qualquer endereço hexa, **os últimos 3 dígitos são SEMPRE o offset**; o que sobra à esquerda é o **número da página**.

**Exemplo do Slide 26**:
- Endereço virtual: `01803E9Ah`
- Como $4\text{ KB} = 12\text{ bits} = 3\text{ dígitos hexa}$:
  - $\text{Offset} = \mathbf{E9Ah}$
  - $\text{Página Virtual} = \mathbf{01803h}$
- Se a tabela diz que a página `01803h` está mapeada no quadro físico `00017h`:
  - $\text{Endereço Físico} = \text{Quadro} \mathbin{\Vert} \text{Offset} = \mathbf{00017E9Ah}$.

#### Dimensionamento de Tabela de Páginas
$$\text{Tamanho da Tabela Simples} = 2^p \times (\text{tamanho da entrada em bytes})$$
*Exemplo*: 32 bits, páginas de 4 KB ($p=20$), entrada de 4 bytes:
$$\text{Tamanho} = 2^{20} \times 4 \text{ bytes} = 1.048.576 \times 4 = 4 \text{ MB por processo!}$$

---

### 2.4 Alocação Contígua: Buddy System (Capítulo 16)

Dado o espaço total de memória inicial $M = 2^K$ (ex: 1024 KB = 1 MB):

#### Regras de Alocação:
1. Para uma requisição de tamanho $S$, determine o bloco mínimo em potência de 2:
   $$B = 2^{\lceil \log_2 S \rceil}$$
   *(Ex: pedido de 85 KB $\implies B = 128 \text{ KB}$; pedido de 200 KB $\implies B = 256 \text{ KB}$)*.
2. Divida recursivamente o bloco livre maior ao meio até atingir o tamanho $B$.

#### Identificação Numérica do Camarada (Fórmula XOR):
O endereço do camarada (buddy) de um bloco no endereço $A$ com tamanho $B$ é dado por:
$$\text{Endereço\_Buddy}(A, B) = A \oplus B$$
*(Exemplo: Bloco de tamanho 128 KB no endereço 0 tem camarada no endereço $0 \oplus 128 = 128$ KB)*.

#### Regra de Fusão (Merge):
Ao liberar o bloco em $A$, ele **só se funde** com seu camarada se o bloco $\text{Buddy}(A, B)$ estiver **totalmente livre e com o mesmo tamanho $B$**. A fusão gera um novo bloco em $\min(A, \text{Buddy}(A, B))$ de tamanho $2B$.

---

### 2.5 Substituição de Páginas (Capítulo 17)

Dada a sequência de referências:
$$7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1$$
e $M$ molduras de memória (ex: $M = 3$).

Para resolver sem desenhar quadros gráficos: construa uma matriz de colunas onde cada coluna é a moldura $1, 2, 3$ e anote apenas quando ocorre **Falta de Página (FP)**.

#### A) FIFO (First-In, First-Out)
- **Regra**: Substitui a página que está na memória há mais tempo (use um ponteiro circular de substituição $ptr = 0, 1, 2, 0, 1, 2 \dots$).
- Toda vez que ocorrer uma falta de página, substitui na posição $ptr$ e faz $ptr = (ptr + 1) \bmod M$.

#### B) ÓTIMO (Belady / MIN)
- **Regra**: Em caso de falta de página, olhe para a cadeia de referências **para a frente (futuro)**.
- Substitua a página cujo próximo acesso estiver **mais distante no futuro** (ou que nunca mais será acessada).

#### C) LRU (Least Recently Used)
- **Regra**: Em caso de falta de página, olhe para a cadeia de referências **para trás (passado)**.
- Substitua a página cujo último acesso foi o **mais antigo**.

#### D) Segunda Chance / Relógio (Clock)
- Cada moldura tem um bit $R \in \{0, 1\}$ e há um ponteiro circular.
- Quando a página é acessada (já em RAM): seta $R = 1$.
- Na falta de página:
  - Enquanto $R[ponteiro] == 1$:
    - Faz $R[ponteiro] = 0$
    - $ponteiro = (ponteiro + 1) \bmod M$
  - Se $R[ponteiro] == 0$:
    - Substitui a página nessa posição, seta seu $R = 1$, avança $ponteiro = (ponteiro + 1) \bmod M$ e para.

---

# PARTE 3 — AVALIAÇÃO TEÓRICA 03 (AT03)
## Capítulos 19 a 25: E/S, Discos, RAID e Sistemas de Arquivos

### 3.1 Escalonamento de Braço de Disco (Capítulo 21)

Dados:
- Posição inicial da cabeça: $C_0$ (Exemplo dos slides: $C_0 = 500$)
- Cilindros solicitados: $\{71, 161, 278, 335, 447, 659, 914\}$
- Limites físicos do disco: $0$ a $MAX$ (no exemplo: $MAX = 999$).
- Sentido inicial (para o elevador): crescente (para a direita/cima).

#### Deslocamento Total sem Desenhar Linhas:

##### 1. FCFS
Ordem estrita de chegada:
$$\text{Deslocamento} = \sum_{k=1}^K |C_k - C_{k-1}|$$

##### 2. SSTF (Shortest Seek Time First)
Procedimento guloso: a cada passo, vá para o bloco pendente com menor distância $|C_{\text{atual}} - C_{\text{candidato}}|$.
- De 500: candidato mais próximo é 447 (dist 53).
- De 447: mais próximo é 335 (dist 112) ... continue computando a diferença.

##### 3. SCAN (Algoritmo do Elevador) — FÓRMULA FECHADA DIRETA!
Se a cabeça sobe até o extremo superior físico ($MAX$) e depois desce até a menor requisição ($\min$):
$$\text{Deslocamento SCAN} = (MAX - C_0) + (MAX - \min) = 2 \times MAX - C_0 - \min$$
*No exemplo do slide*: $MAX = 999, C_0 = 500, \min = 71$:
$$\text{Deslocamento} = (999 - 500) + (999 - 71) = 499 + 928 = \mathbf{1.427 \text{ cilindros!}}$$
*(Cálculo feito em 5 segundos, sem traçar um único traço no gráfico!)*.

##### 4. LOOK (Variante do SCAN que não vai ao extremo físico inútil)
$$\text{Deslocamento LOOK} = (\max - C_0) + (\max - \min) = 2 \times \max - C_0 - \min$$
*No exemplo*: $\max = 914$:
$$\text{Deslocamento} = (914 - 500) + (914 - 71) = 414 + 843 = \mathbf{1.257 \text{ cilindros!}}$$

##### 5. C-SCAN (Circular SCAN com retorno ao zero físico)
Se subir até $MAX$, saltar para $0$ e subir até a maior requisição abaixo de $C_0$ ($req_{\text{inf}}$):
$$\text{Deslocamento C-SCAN} = (MAX - C_0) + \text{salto}(MAX - 0) + (req_{\text{inf}} - 0)$$

---

### 3.2 Cálculos de Arranjos RAID (Capítulo 21)

Sejam $N$ discos idênticos, cada um com capacidade $C$:

| Tipo de RAID | Descrição | Capacidade Útil | Discos de Paridade / Espelho | Tolerância a Falhas |
| :--- | :--- | :---: | :---: | :---: |
| **RAID 0** | Striping (sem redundância) | $N \times C$ | $0$ | $0$ discos |
| **RAID 1** | Espelhamento puro | $C$ (ou $N \times C / 2$ em pares) | $N/2$ discos | $1$ disco (ou até metade) |
| **RAID 5** | Paridade distribuída simples | $\mathbf{(N - 1) \times C}$ | $1$ disco equivalente | $\mathbf{1 \text{ disco}}$ |
| **RAID 6** | Paridade dupla (códigos Reed-Solomon) | $\mathbf{(N - 2) \times C}$ | $2$ discos equivalentes | $\mathbf{2 \text{ discos}}$ |
| **RAID 10 (1+0)** | Listras de espelhos | $\frac{N}{2} \times C$ | $N/2$ discos | $1$ disco por espelho |

#### Cálculo da Paridade (Operador XOR):
$$P = D_1 \oplus D_2 \oplus \dots \oplus D_{N-1}$$
Se o disco $D_2$ falhar, sua recuperação é instantânea e unívoca por XOR:
$$D_2 = P \oplus D_1 \oplus D_3 \oplus \dots \oplus D_{N-1}$$

---

### 3.3 Inodes e Tamanho Máximo de Arquivos (Capítulo 24)

Considerando a arquitetura padrão de Inode dos slides do Prof. Maziero:
- Tamanho do bloco lógico de dados: $B$ bytes (ex: $4.096 \text{ bytes} = 4\text{ KB}$)
- Tamanho do ponteiro de bloco: $P$ bytes (geralmente $4 \text{ bytes}$)
- Quantidade de ponteiros por bloco indireto:
  $$K = \frac{B}{P} \quad \left(\text{No exemplo dos slides: } K = \frac{4096}{4} = \mathbf{1.024 \text{ ponteiros}}\right)$$

#### Fórmula Fechada da Capacidade Máxima do Inode (Slide 31):
Dado um inode com:
- $N_{dir}$ ponteiros diretos (padrão: 12)
- 1 ponteiro indireto simples
- 1 ponteiro indireto duplo
- 1 ponteiro indireto triplo

$$\text{TamMax} = \left( N_{dir} + K + K^2 + K^3 \right) \times B \text{ bytes}$$

**Substituição Numérica dos Slides**:
$$\begin{aligned}
\text{Diretos:} \quad & 12 \times 4.096 = 49.152 \text{ bytes} \ (48 \text{ KB}) \\
\text{1-Indireto:} \quad & 1.024 \times 4.096 = 4.194.304 \text{ bytes} \ (4 \text{ MB}) \\
\text{2-Indireto:} \quad & 1.024^2 \times 4.096 = 1.048.576 \times 4.096 = 4.294.967.296 \text{ bytes} \ (4 \text{ GB}) \\
\text{3-Indireto:} \quad & 1.024^3 \times 4.096 = 1.073.741.824 \times 4.096 = 4.398.046.511.104 \text{ bytes} \ (4 \text{ TB}) \\
\mathbf{\text{Total Máximo:}} \quad & \mathbf{4.402.345.721.856 \text{ bytes} \approx 4 \text{ TBytes}}
\end{aligned}$$

---

### 3.4 Localização de um Byte em Bloco Físico (Acesso Direto - Slide 32 e 33)

Dado o byte offset $i$ dentro de um arquivo:
1. Calcule o **número do bloco lógico**:
   $$pos = \lfloor i / B \rfloor$$
2. Calcule o **deslocamento dentro do bloco**:
   $$oi = i \bmod B$$
3. Identifique o nível de indireção através de faixas de comparação:
   - **Faixa Direta**: se $pos < 12 \implies$ Bloco está no ponteiro direto $ptr[pos]$.
   - **Faixa 1-Indireta**: se $12 \le pos < 12 + K$:
     - Posição no bloco indireto: $pos' = pos - 12$.
     - Lê $block_1$ a partir de $ptr[12]$. O bloco físico é $block_1[pos']$.
   - **Faixa 2-Indireta**: se $12 + K \le pos < 12 + K + K^2$:
     - $pos'' = pos - 12 - K$.
     - Primeiro índice: $\lfloor pos'' / K \rfloor$.
     - Segundo índice: $pos'' \bmod K$.
   - **Faixa 3-Indireta**: similar com divisões sucessivas por $K^2$ e $K$.

---

### Resumo das Fórmulas de Ouro para a Prova

1. **Tempo de espera de CPU**: $t_w = t_{fim} - t_{chegada} - duracao$.
2. **SCAN de disco**: $2 \times MAX - C_0 - \min$.
3. **LOOK de disco**: $2 \times \max - C_0 - \min$.
4. **Página Virtual**: $Endereço \div Tamanho\_Pagina$ (ou corte os 3 dígitos hexa finais se $4\text{ KB}$).
5. **Capacidade RAID 5**: $(N-1) \times C$.
6. **Buddy XOR**: $Endereço\_Buddy = A \oplus B$.
7. **Inode**: $TamMax = (N_{dir} + K + K^2 + K^3) \times B$ com $K = B / P$.

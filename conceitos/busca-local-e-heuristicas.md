# Busca local e heurísticas — notas conceituais com exercícios de papel

Notas de apoio aos encontros 2 e 3, cobrindo R&N 4ª ed. §3.5–3.6 e §4.1. Escrito para ser
executado à mão, no caderno.

---

## 1. A escada: o que cada algoritmo compra e o que paga

O professor apresentou como uma progressão — A\* introduz memória, têmpera introduz
aleatoriedade, feixe introduz população. A escada abaixo organiza isso. Cada degrau **compra uma
capacidade e paga um preço**; é a leitura que a disciplina cobra.

| Algoritmo | O que guarda na memória | O que adiciona | O que paga |
|---|---|---|---|
| Subida de encosta | 1 estado | — | prende no máximo local; nenhuma garantia |
| **A\*** | fronteira inteira + estados alcançados | **memória e ordenação por f = g + h** | memória exponencial — é o gargalo real |
| **Têmpera simulada** | 1 estado + a temperatura T | **aleatoriedade controlada por um parâmetro que decai** | abre mão da garantia (ótimo só no limite teórico) |
| **Feixe local** | k estados | **população + partilha de informação entre os k** | perde diversidade: os k colapsam na mesma região |
| **Feixe estocástico** | k estados | **seleção proporcional ao valor**, não os k melhores | — é a ponte direta para o AG |
| **Algoritmo genético** | k estados | **cruzamento: combina duas soluções em uma** | exige representação que sobreviva à recombinação |

Note o corte no meio da tabela. A\* guarda a fronteira toda; a busca local joga a memória fora e
guarda só o estado atual. Não é um refinamento do A\* — é uma **troca de contrato**: abre-se mão
de completude e otimalidade para caber na memória em espaços onde o A\* nem começa.

Isso responde à pergunta que a Tarefa 1 pede na comparação com "outras técnicas de busca
clássica".

---

## 2. Têmpera simulada

### A ideia em uma frase

**É um botão que começa como passeio aleatório e termina como subida de encosta.**

A subida de encosta só aceita movimento que melhora — por isso trava no primeiro pico. A têmpera
às vezes aceita **piorar**, e a chance de aceitar depende de duas coisas: quanto piora, e de um
parâmetro **T** (temperatura) que vai caindo ao longo da execução.

### A regra de decisão

A cada passo:

1. Sorteie **um** vizinho do estado atual (só um, não todos).
2. Calcule `ΔE = valor(vizinho) − valor(atual)`.
3. Se `ΔE > 0` (melhorou) → **aceite sempre**.
4. Se `ΔE ≤ 0` (piorou) → aceite com probabilidade `e^(ΔE/T)`.
5. Esfrie: diminua T e repita.

### O tal gráfico decrescente

É o **esquema de resfriamento**: a curva de T ao longo do tempo. Ele não é decoração — é o
algoritmo inteiro. Olhe o que `e^(ΔE/T)` faz nos extremos:

| T | `e^(ΔE/T)` para uma piora | Comportamento |
|---|---|---|
| **muito alto** | expoente ≈ 0, probabilidade ≈ **1** | aceita quase tudo → **passeio aleatório** |
| médio | probabilidade intermediária | explora, mas resiste a pioras grandes |
| **→ 0** | expoente → −∞, probabilidade → **0** | recusa toda piora → **subida de encosta** |

Ou seja: a curva decrescente de T é o cronograma de **quando parar de explorar e começar a
explorar o que já achou**. Cair rápido demais = subida de encosta disfarçada, trava no primeiro
pico. Cair devagar demais = passeio aleatório, nunca converge.

E repare no `ΔE` no numerador: para um mesmo T, **piorar pouco é muito mais provável de ser
aceito que piorar muito**. A têmpera não é aleatória; é seletivamente aleatória.

### A metáfora que dá nome

Têmpera (ou recozimento) é metalurgia: aquece-se o metal para que os átomos se movam livremente,
depois resfria-se **devagar** para que se assentem numa estrutura de baixa energia. Resfriar
rápido demais congela os defeitos no lugar — o análogo exato de travar num máximo local.

### 🖊️ Exercício de papel — têmpera simulada

**Paisagem** (maximização; vizinhos são posição ±1):

```
posição:   1   2   3   4   5   6   7   8   9
valor:     2   4   6   4   3   5   7   9   6
                 ↑máx local           ↑máx global
```

**Comece na posição 2.**

Primeiro faça a **subida de encosta**: de 2 vai para 3 (6), e de 3 os dois vizinhos valem 4 —
ambos piores. **Travou em 6.** Uma linha, e você já viu o problema.

Agora a têmpera. Para executar à mão sem computador, use estas listas no lugar dos sorteios:

- **Vizinho sorteado** (E = esquerda, D = direita), em ordem:
  `D · D · E · D · D · D · D · D · D · D`
- **Números aleatórios** (consuma um **só quando precisar decidir uma piora**):
  `0,31 · 0,55 · 0,09 · 0,62 · 0,20 · 0,44 · 0,12 · 0,77`
- **Temperatura**, um valor por passo:
  `4 · 3,5 · 3 · 2,5 · 2 · 1,5 · 1 · 0,7 · 0,4 · 0,2`
- **Tabela de `e^x`** (arredonde ΔE/T para o valor mais próximo):

  | ΔE/T | −0,25 | −0,5 | −0,75 | −1 | −1,5 | −2 | −3 | −4 |
  |---|---|---|---|---|---|---|---|---|
  | `e^(ΔE/T)` | 0,78 | 0,61 | 0,47 | 0,37 | 0,22 | 0,14 | 0,05 | 0,02 |

Aceite a piora se **aleatório < probabilidade**.

Os dois primeiros passos, resolvidos, para você pegar o ritmo:

> **Passo 1** — T = 4, estou em 2 (valor 4). Moeda = D → vizinho é 3 (valor 6).
> ΔE = 6 − 4 = **+2**, melhorou → aceito sem sortear nada. **Agora estou em 3.**
>
> **Passo 2** — T = 3,5, estou em 3 (valor 6). Moeda = D → vizinho é 4 (valor 4).
> ΔE = 4 − 6 = **−2**. ΔE/T = −2/3,5 ≈ −0,57 → arredondo para −0,5 → probabilidade **0,61**.
> Sorteio o primeiro aleatório: 0,31. Como 0,31 < 0,61, **aceito piorar**. **Estou em 4.**
>
> Repare no que acabou de acontecer: eu **desci do máximo local por vontade própria**. É isso, e
> só isso, que a têmpera adiciona.

Continue até o passo 10. **Se você seguir as listas certo, termina na posição 8 — o máximo
global.** Use isso para conferir.

Depois, duas variações de 5 minutos que valem mais que reler a seção:

- Refaça com **T = 0,2 em todos os passos** (esfriou instantaneamente). Onde você para?
- Refaça com **T = 4 em todos os passos** (nunca esfriou). Você para em algum lugar?

---

## 3. Busca em feixe local

### Corrigindo a intuição

Sua leitura foi "k instâncias de têmpera rodando junto". Isso é quase, mas é **outro algoritmo**:
k buscas independentes é o que se chama **subida de encosta com reinício aleatório** — k execuções
que nunca conversam, e no fim você fica com a melhor.

A busca em feixe é diferente **por causa de uma linha**: a cada passo, ela gera os sucessores de
**todos** os k estados, joga tudo num balaio único, e escolhe os **k melhores do balaio inteiro**.

A consequência é que os k estados **não são independentes**. Um estado que gerou bons sucessores
toma as vagas de um estado que gerou sucessores ruins. Russell & Norvig descrevem isso como os
ramos se comunicando: *"venha para cá, a grama aqui é mais verde"*. É isso que faz dela uma
**população** e não um paralelismo.

### Sobre a sua ideia de replicação exponencial

Boa intuição, e o interessante é que ela aponta exatamente para o que o feixe **impede**. Se você
guardasse todos os sucessores de todos os estados a cada passo, teria explosão exponencial — que
é, literalmente, a busca em largura. O **k é o teto** que corta isso: a população nunca cresce.

E o preço desse teto é justamente a **perda de diversidade** — os k rapidamente viram variações
da mesma coisa, e o feixe degenera numa subida de encosta cara. A correção é o **feixe
estocástico**: em vez dos k melhores, escolha k sucessores com probabilidade proporcional ao
valor. Um sucessor medíocre ainda tem chance.

E aqui está a ponte que o professor está construindo: **feixe estocástico é seleção natural** —
sucessores são descendentes, o valor é a aptidão, a escolha proporcional é a sobrevivência do mais
apto. Falta um único ingrediente para chegar no algoritmo genético: **o cruzamento**, que combina
*dois* estados num terceiro. Feixe tem população e seleção; o AG acrescenta reprodução sexuada.

### 🖊️ Exercício de papel — feixe local

Mesma paisagem. **k = 3**, começando em `{1, 5, 9}` (valores 2, 3, 6).

**Passo 1** — gere os sucessores de todos:

| Estado | Sucessores (valor) |
|---|---|
| 1 | 2 (4) |
| 5 | 4 (4), 6 (5) |
| 9 | 8 (9) |

Balaio: 2(4), 4(4), 6(5), 8(9). Os 3 melhores: **8(9), 6(5), 2(4)**. Novo feixe: `{8, 6, 2}`.

**Passo 2** — faça você. Gere os sucessores de 8, de 6 e de 2, junte tudo e pegue os 3 melhores.

Duas coisas vão saltar aos olhos, e as duas são o conteúdo da seção:

1. Você vai acabar com **o mesmo estado ocupando duas vagas**. Isso é o colapso de diversidade,
   acontecendo em dois passos.
2. O estado 8, que era o máximo global, **sai do feixe** — porque o feixe guarda os melhores
   *sucessores*, não os melhores estados atuais. Se você não guardar o melhor-até-agora à parte,
   você o perde.

Agora refaça o passo 2 com **seleção proporcional ao valor** em vez dos 3 melhores e veja a
diferença no colapso.

---

## 4. Admissível × consistente (monotônica)

### A relação, na ordem certa

São duas propriedades diferentes, e **a implicação tem um sentido só**:

- **Admissível**: `h(n) ≤ custo real de n até o objetivo`. Nunca superestima. É um piso.
- **Consistente** (= **monotônica**): para todo nó `n` e todo sucessor `n'`,
  `h(n) ≤ c(n, a, n') + h(n')`. É a desigualdade triangular aplicada à heurística.

> **Toda heurística consistente é admissível. A recíproca é falsa.**

Vale registrar porque a direção importa: admissibilidade **não depende** de monotonicidade —
consistência é a condição **mais forte**. Se a anotação do caderno ficou ao contrário, é aqui que
corrige.

### Por que "monotônica"

Porque se `h` é consistente, então `f(n) = g(n) + h(n)` **nunca decresce** ao longo de um caminho.
Você caminha e o `f` só sobe ou empata. Daí o nome.

E é isso que dá a garantia forte: com `f` não decrescente, quando o A\* retira um nó da fronteira
para expandir, **já achou o melhor caminho até ele**. Nunca precisa voltar atrás.

### 🖊️ Exercício de papel — o contraexemplo

Quatro nós. Custos das arestas:

```
S --3--> A        A --4--> G
S --1--> B        B --1--> A
```

Heurística: `h(S) = 6`, `h(A) = 0`, `h(B) = 5`, `h(G) = 0`.

**Primeiro, confirme que ela é admissível.** Custos reais até G: de S é 6 (via B e A), de A é 4,
de B é 5. Compare com os h: 6 ≤ 6 ✓, 0 ≤ 4 ✓, 5 ≤ 5 ✓. **Todos admissíveis.**

**Agora teste a consistência** na aresta S→A: `h(S) ≤ c(S,A) + h(A)` → `6 ≤ 3 + 0 = 3`?
**Falso.** A heurística é admissível mas **não** consistente.

**Veja a não-monotonicidade acontecer.** Calcule f: em S, `f = 0 + 6 = 6`. Chegando em A por S,
`f = 3 + 0 = 3`. O `f` **caiu** de 6 para 3 ao caminhar. É literalmente a monotonicidade quebrando
na sua frente.

**Agora rode o A\* à mão** e observe a consequência:

1. Expanda S. Gera A com `g=3, f=3` e B com `g=1, f=6`.
2. A fronteira tem A (f=3) e B (f=6). Você expande **A**, porque tem o menor f.
3. Mas o melhor caminho até A custa **2** (via B), não 3. Você expandiu A cedo demais, com o
   caminho errado.
4. Depois, ao expandir B, aparece A com `g=2` — melhor que o 3 já registrado.

O que acontece daí depende da versão do algoritmo, e a diferença é instrutiva:

- Na formulação do **R&N 4ª ed.**, a tabela de alcançados é atualizada quando surge um caminho
  mais barato, e A volta para a fronteira. O resultado final sai **correto** (custo 6), mas **A
  foi expandido duas vezes**. A inconsistência custou trabalho.
- Na versão clássica com lista de fechados que **nunca reabre** nó expandido, o caminho melhor é
  descartado e o algoritmo devolve **7** — subótimo, silenciosamente.

Resumo do que o exercício mostra: **admissibilidade garante que a resposta está certa; consistência
garante que você não paga duas vezes pelo mesmo nó** — e, na versão que não reabre, é ela que
salva a corretude.

---

## 5. Perguntas que esse material rende para o debate

- Se a têmpera simulada só garante o ótimo com resfriamento infinitamente lento, em que sentido a
  garantia é útil? O que ela realmente diz sobre a execução finita que rodo na prática?
- O feixe local partilha informação entre os k ramos. Isso é uma forma de memória? Se for, a
  distinção "busca local não tem memória" se sustenta?
- Feixe estocástico já tem população e seleção. O cruzamento do AG é um salto qualitativo, ou só
  um operador de vizinhança mais elaborado? *(esta é diretamente a pergunta sobre o enunciado da
  Tarefa 1 chamar o AG de "técnica de busca local")*
- A consistência é propriedade da heurística ou da relação entre a heurística e a **estrutura de
  custos** do grafo? Por que a distinção importa ao projetar uma heurística nova?

# Implementações — plano do código próprio

## Princípio

O plano de ensino é explícito: **não é disciplina voltada ao treinamento artefatual nem a
frameworks específicos**. O código existe para produzir os dados que sustentam a discussão de
*por que* os métodos são modelados como são.

Consequência prática de projeto: **a instrumentação é parte do algoritmo, não um extra.** Um A\*
que devolve só o caminho é inútil aqui. Um A\* que devolve caminho + nós expandidos + pico de
memória da fronteira + custo da solução + tempo permite responder "por que h₁ domina h₂" com
número, e não com citação.

Sem bibliotecas de IA. `numpy` para álgebra linear na parte de ML é razoável, mas **confirmar com
o professor no encontro 1** — a fronteira do que conta como "framework" precisa vir dele.

## Estrutura sugerida

```
implementacoes/
  busca/
    problema.py        # interface abstrata: estado_inicial, acoes, transicao, teste_objetivo, custo
    instrumentacao.py  # contadores: gerados, expandidos, pico_fronteira, tempo, custo_solucao
    cega.py            # BFS, DFS, profundidade limitada, IDS, custo uniforme, bidirecional
    informada.py       # best-first, gulosa, A*, IDA*
    online.py          # DFS online, LRTA*
    heuristicas.py     # relaxações, dominância, fator de ramificação efetiva
    dominios/          # 8-puzzle, labirinto em grade, mapa da Romênia, n-rainhas
    experimentos.py    # roda a bateria e emite a tabela comparativa
  local/
    subida_encosta.py  # + reinício aleatório, subida estocástica
    tempera.py         # simulated annealing
    ag.py              # AG canônico: seleção, cruzamento, mutação, elitismo
  ml/
    arvore.py          # ID3/C4.5 do zero: entropia, ganho de informação, poda
    perceptron.py
    mlp.py             # backpropagation escrito à mão
```

## A interface de problema é a decisão central

Definir **uma** abstração de problema e fazer todos os algoritmos de busca consumirem a mesma é o
que torna a comparação honesta — e é exatamente o tipo de decisão de modelagem que a disciplina
avalia. Se BFS e A\* rodam sobre representações diferentes do 8-puzzle, os números não comparam
nada.

Mínimo da interface: `estado_inicial()`, `acoes(estado)`, `resultado(estado, acao)`,
`teste_objetivo(estado)`, `custo_passo(estado, acao, proximo)`. A heurística fica **fora** do
problema, como função `h(estado, problema)` — separar isso deixa visível que a heurística é
conhecimento adicional injetado, não parte da definição do problema.

## Métricas a instrumentar desde o primeiro algoritmo

| Métrica | Por que importa |
|---|---|
| Nós **gerados** × nós **expandidos** | a diferença expõe o efeito do teste de objetivo na geração vs. expansão |
| Pico de tamanho da fronteira | é a complexidade de **espaço** medida — o gargalo real, e o argumento a favor de IDS/IDA\* |
| Tamanho do conjunto explorado | custo da busca em grafo sobre a busca em árvore |
| Custo da solução | verifica otimalidade empiricamente; deve divergir entre gulosa e A\* |
| Profundidade da solução | permite estimar o fator de ramificação efetiva b\* |
| Tempo de parede | secundário — não confundir com complexidade assintótica |

## Roteiro por semana

| Semana | Encontro | Implementar | Experimento que gera discussão |
|---|---|---|---|
| 1 | 19/08 | Interface de problema + BFS, DFS, UCS, gulosa, A\* | Mesmo grafo, 5 algoritmos: onde gulosa perde otimalidade e por quanto |
| 2 | 26/08 | IDS, IDA\*, heurísticas do 8-puzzle (peças fora do lugar × Manhattan) | Dominância medida em nós expandidos; b\* efetivo de cada heurística |
| 3 | 02/09 | Subida de encosta, têmpera simulada, AG canônico | n-rainhas: taxa de sucesso × custo, subida simples vs. reinício aleatório vs. AG |
| 4 | 09/09 | Busca online (LRTA\*) em labirinto desconhecido | Razão de competitividade medida contra o ótimo offline |
| — | 16/09 | **Entrega da Tarefa de Busca** | |
| 7–8 | 30/09, 07/10 | Árvore de decisão do zero (entropia, ganho, poda) | Efeito da poda em treino × teste; overfitting visto, não citado |
| 9–10 | 14/10, 21/10 | Perceptron; MLP com backprop manual | XOR: por que o perceptron falha e o que exatamente a camada oculta adiciona |
| — | 04/11 | **Entrega da Tarefa de ML** | |

> O roteiro é anterior aos enunciados oficiais das tarefas. Quando os enunciados saírem
> (Moodle), ajustar — mas manter a interface e a instrumentação, que servem a qualquer enunciado.

## Registro de experimentos

Cada bateria rodada gera uma linha em `resultados.md`: domínio, instância, algoritmo,
heurística, e as métricas acima. Sem isso, na semana da entrega os números terão de ser
regerados e a análise vira descrição de saída em vez de argumento.

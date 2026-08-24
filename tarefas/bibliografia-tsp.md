# Bibliografia para a Tarefa 1 — TSP, Têmpera Simulada e AG

Levantada via Scholar Gateway (corpus Wiley, atualização maio/2026). São referências
**verificadas**, com citação pronta para o artigo SBC. Não substituem o Russell & Norvig §4.1,
que é a base conceitual — servem para a seção de comparação e para sustentar as escolhas de
modelagem com literatura.

> Resultados obtidos via Scholar Gateway. Os resumos abaixo são meus, a partir dos abstracts
> retornados — leia os originais antes de citar.

## Operadores de cruzamento para permutações

O ponto mais direto para o item *"onde e como a modelagem se reflete em cada algoritmo"*.

- **Katayama, K., Hirabayashi, H., & Narihisa, H. (1999).** Performance analysis for crossover
  operators of genetic algorithm. *Systems and Computers in Japan, 30*(2), 20–30.
  https://doi.org/10.1002/(SICI)1520-684X(199902)30:2<20::AID-SCJ3>3.0.CO;2-M
  — Análise comparativa de operadores de cruzamento aplicados ao TSP. É a referência mais direta
  para justificar por que a escolha do operador não é detalhe de implementação.

- **Hussain, A., Muhammad, Y. S., Sajid, M. N., Hussain, I., Shoukry, A. M., & Gani, S. (2017).**
  Genetic Algorithm for Traveling Salesman Problem with Modified Cycle Crossover Operator.
  *Computational Intelligence and Neuroscience, 2017*(1). https://doi.org/10.1155/2017/7430125
  — Acesso aberto. Propõe variação do cycle crossover e compara com operadores estabelecidos.

- **Iqbal, Z., Bashir, N., Hussain, A., & Cheema, S. A. (2020).** A novel completely mapped
  crossover operator for genetic algorithm to facilitate the traveling salesman problem.
  *Computational and Mathematical Methods, 2*(6). https://doi.org/10.1002/cmm4.1122

- **Takahashi, R. (2010).** Extended changing crossover operators to solve the traveling salesman
  problem. *Electronics and Communications in Japan, 93*(7), 1–16.
  https://doi.org/10.1002/ecj.10313

## Cruzamento × mutação: o que realmente move o AG

- **Osaba, E., Carballedo, R., Diaz, F., Onieva, E., de la Iglesia, I., & Perallos, A. (2014).**
  Crossover versus Mutation: A Comparative Analysis of the Evolutionary Strategy of Genetic
  Algorithms Applied to Combinatorial Optimization Problems. *The Scientific World Journal,
  2014*(1). https://doi.org/10.1155/2014/154676
  — Útil para uma análise honesta: quanto do desempenho vem do cruzamento e quanto da mutação. Se
  a mutação por inversão de segmento fizer o trabalho pesado, o AG está operando perto de uma
  busca local — e isso conversa direto com a pergunta de por que o enunciado chama o AG de
  "técnica de busca local".

## Híbridos AG + Têmpera Simulada

- **Deng, Y., Xiong, J., Wang, Q., & Hosseinabadi, A. A. (2021).** A Hybrid Cellular Genetic
  Algorithm for the Traveling Salesman Problem. *Mathematical Problems in Engineering, 2021*(1).
  https://doi.org/10.1155/2021/6697598
  — Combina AG celular com têmpera simulada, testado em **13 instâncias da TSPLIB**, com
  comparação contra GA, SA e CGA isolados. Boa fonte de protocolo experimental: mostra como se
  reporta esse tipo de comparação.

- **Mohsen, A. M., & Masciari, E. (2016).** Annealing Ant Colony Optimization with Mutation
  Operator for Solving TSP. *Computational Intelligence and Neuroscience, 2016*(1).
  https://doi.org/10.1155/2016/8932896
  — Outra família de metaheurística no mesmo problema. Útil se a comparação com "outras técnicas"
  for além da busca clássica.

## Ajuste de parâmetros — a armadilha metodológica

Têmpera Simulada e AG têm muitos parâmetros. Comparar "TS contra AG" sem falar de ajuste é
comparar *as suas escolhas de parâmetros*, não os algoritmos. Vale ao menos declarar isso na
metodologia.

- **Barbosa, E. B., Senne, E. L., & Silva, M. B. (2015).** Improving the Performance of
  Metaheuristics: An Approach Combining Response Surface Methodology and Racing Algorithms.
  *International Journal of Engineering Mathematics, 2015*(1). https://doi.org/10.1155/2015/167031

- **Barbosa, E. B., & Senne, E. L. (2017).** Improving the Fine-Tuning of Metaheuristics: An
  Approach Combining Design of Experiments and Racing Algorithms. *Journal of Optimization,
  2017*(1). https://doi.org/10.1155/2017/8042436

## Ferramentas e instâncias

- **Ismkhan, H., & Zamanifar, K. (2014).** Developing Programming Tools to Handle Traveling
  Salesman Problem by the Three Object-Oriented Languages. *Applied Computational Intelligence
  and Soft Computing, 2014*(1). https://doi.org/10.1155/2014/137928

- **TSPLIB** — biblioteca padrão de instâncias com ótimos conhecidos. Use instâncias pequenas
  (`berlin52`, `eil51`, `st70`) para reportar distância percentual do ótimo em vez de custo
  absoluto sem referência.

## Falta ainda

Estas referências cobrem o AG bem e a Têmpera Simulada de raspão. Antes de escrever, valeria
buscar:

- [ ] Kirkpatrick, Gelatt & Vecchi (1983), *Optimization by Simulated Annealing* — o artigo
      seminal da têmpera simulada
- [ ] Esquemas de resfriamento e sua influência na qualidade da solução
- [ ] Operadores de vizinhança 2-opt e 3-opt no TSP
- [ ] Formulação clássica do TSP e sua NP-dificuldade, para a seção de definição formal

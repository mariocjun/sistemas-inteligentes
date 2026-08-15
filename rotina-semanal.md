# Rotina semanal — as 6 horas mínimas

O encontro é quarta (3 aulas). A semana de estudo, portanto, vai de **quinta a terça**, e a
leitura prévia vence **terça à noite**. Ancorar a rotina nesse ciclo em vez de "estudar quando
der" é o que faz o flipped-classroom funcionar.

| Dia | Bloco | Duração | O quê |
|---|---|---|---|
| **Quinta** | Consolidação | 1h00 | Passar as notas do encontro a limpo *no mesmo dia*. Marcar o que ficou em aberto no debate — vira pergunta da próxima semana. |
| **Sexta** | Leitura I | 1h30 | Primeira passagem do capítulo: ler inteiro, sem parar em detalhe. Objetivo é o mapa, não o domínio. |
| **Sábado** | Leitura II | 1h30 | Segunda passagem: fichamento ativo. Derivações refeitas à mão, pseudocódigo copiado e anotado, contraexemplos testados. |
| **Domingo** | Implementação | 1h30 | Código próprio do algoritmo da semana, com instrumentação (ver `implementacoes/`). |
| **Terça** | Perguntas | 0h30 | Escrever 3–5 perguntas para o encontro, no formato de `encontros/_template.md`. |
| | **total** | **6h00** | |

Semanas de tarefa ou prova: os blocos de sábado/domingo migram para a entrega, e a leitura fica
só na primeira passagem. Não corte o bloco de terça — é o que diferencia assistir do participar.

## Fichamento: o formato que serve a esta disciplina

Para cada seção lida, três linhas:

1. **Mecanismo** — o que o algoritmo/conceito faz, em uma frase, sem jargão.
2. **Porquê** — que decisão de modelagem produziu essa forma, e o que ela custa.
3. **Quebra** — sob que condição a garantia falha (heurística inadmissível, ambiente parcialmente
   observável, espaço contínuo, ruído nos dados...).

A linha 3 é a que vira pergunta de prova aberta e pergunta de debate.

## Auto-teste de pré-requisitos (PAA)

A disciplina assume PAA cursada a contento. Se algum item abaixo estiver enferrujado, tratar
**nas duas primeiras semanas** — depois não haverá folga.

- [ ] Enunciar e usar notação assintótica (O, Θ, Ω) com rigor, incluindo por que O(b^d) e O(b^m)
      dizem coisas diferentes sobre busca
- [ ] Provar corretude por invariante de laço
- [ ] BFS, DFS, Dijkstra: implementar de memória e justificar a estrutura de dados de cada um
- [ ] Filas de prioridade / heaps: custo de cada operação e impacto no custo total do algoritmo
- [ ] Estratégia gulosa vs. programação dinâmica: quando a escolha local é segura, e como se prova
- [ ] Distinguir complexidade **de tempo** e **de espaço** de uma busca — em IA o gargalo costuma
      ser memória, e é aí que IDS e IDA\* ganham sentido
- [ ] Redução entre problemas e noção de NP-dificuldade (justifica por que se recorre a heurística
      e busca local)

## Higiene do semestre

O plano de ensino pede explicitamente para compatibilizar o tempo disponível "sem abrir mão da
própria saúde". Traduzindo em regra prática: 6h distribuídas em 5 blocos curtos ao longo da
semana funcionam; 6h empilhadas na terça à noite não — e é a leitura em profundidade que
degrada primeiro.

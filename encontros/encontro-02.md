# Encontro 2 — qua 26/08/2026

**Conteúdo:** Busca informada. Heurísticas (e.g. algoritmo A\*).
**Leitura correspondente:** R&N 4ª ed. §3.5–3.6.

## O que foi discutido em sala

Anotações a partir do relato pós-aula — confira contra o próprio caderno.

- **O A\* como mudança de patamar.** A leitura apresentada foi que o A\* eleva o nível da busca
  ao introduzir o conceito de **memória**: ele mantém a fronteira inteira ordenada por
  `f = g + h`, e é isso que permite a garantia de otimalidade — ao custo de memória exponencial,
  que é o gargalo real.
- **A têmpera simulada como passo seguinte**, por acrescentar **aleatoriedade**: aceita piorar
  com probabilidade `e^(ΔE/T)`, e a curva decrescente de T controla a transição de passeio
  aleatório para subida de encosta.
- **A busca em feixe como introdução de população**: k estados simultâneos, com os k melhores
  sucessores escolhidos do balaio conjunto.
- **Heurística admissível e monotonicidade.** Ver a correção da direção da implicação em
  `../conceitos/busca-local-e-heuristicas.md` §4 — consistência (monotonicidade) é a condição
  mais forte, e é ela que implica admissibilidade, não o contrário.

> As explicações desenvolvidas, com exercícios de papel para têmpera, feixe e o contraexemplo de
> heurística admissível não consistente, estão em
> **`../conceitos/busca-local-e-heuristicas.md`**.

## Artigos externos

⚠️ **Pendente.** O professor distribuiu artigos complementares, incluindo pelo menos um sobre
heurísticas. Ainda não foram lidos nem catalogados aqui.

- [ ] Localizar os artigos no Moodle
- [ ] Catalogar em `../materiais/02-busca-informada/` no mesmo formato do bloco 1
- [ ] Ler o artigo de heurísticas antes do encontro 3

## Para o encontro 3 (02/09)

**Ler:** fim do §3.5–3.6 + **Cap. 4 inteiro**, com prioridade em §4.1 (busca local e
otimização) — é o conteúdo direto da Tarefa 1.

📍 Lembrete: **o andamento da Tarefa 1 é cobrado em aula em 02/09.**

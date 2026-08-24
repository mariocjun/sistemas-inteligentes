# TAREFA 1 — Busca: artigo com análise da modelagem e implementação

| | |
|---|---|
| **Vence** | **quarta 16/09/2026, 14h00** — não é meia-noite |
| Abre | terça 25/08/2026, 00h00 |
| Peso | 1,0 ponto (componente AV1_A) |
| Equipe | **DUPLAS** — exatamente 2 integrantes |
| Entrega | **PDF, exclusivamente via Moodle** |
| Checkpoint | **andamento cobrado em aula em 02/09** |

## O que o enunciado pede

Modelagem computacional do **Caixeiro Viajante** (TSP), com **duas** implementações:

- **a)** Têmpera Simulada
- **b)** Busca local por **Algoritmo Genético**

E um **artigo no formato SBC** (a estrutura interna fica a cargo da equipe) contendo:

1. A **definição formal** do problema em Computação
2. A **modelagem** utilizada em ambos os enfoques, detalhada
3. **Onde e como a modelagem se reflete em CADA algoritmo** — precisa e claramente
4. Os **resultados, análises e consequências computacionais** nos algoritmos, decorrentes das
   escolhas de modelagem
5. **Comparação** entre os dois algoritmos, e deles em relação às **outras técnicas de busca
   clássica** (cega ou informada)

Seções obrigatórias:

- **METODOLOGIA** — escolhas de modelagem e técnicas, com justificativas de **domínio**,
  **modelagem**, **representação computacional** e **implementação**
- **RESULTADOS** — o que foi obtido em **cada etapa** da metodologia, com detalhamento
- **Papéis e horas** — papel de cada membro e estimativa de horas despendidas **por integrante**
  (intenção declarada: distribuição igualitária da carga e estimativa de horas fora de sala)

## Restrições

- 2 integrantes
- **Até 5 páginas** de corpo, fonte 11, espaçamento simples, incluindo referências
- Apêndices **além** das 5 páginas para diagramas, tabelas volumosas e código — ou GitHub
- Só pseudocódigos e figuras que sejam resultados relevantes, criações próprias, ou necessários
  ao entendimento num nível de abstração mais alto que o da implementação
- Formato PDF

## Checklist de nota zero

- [ ] Entregue **pelo Moodle**, não por link — "envios indiretos do TEXTO serão desconsiderados
      com NOTA ZERO"
- [ ] PDF, não .docx nem .tex
- [ ] Corpo dentro de 5 páginas (apêndice não conta)
- [ ] Seção de papéis e horas por integrante presente
- [ ] Declaração de uso de LLM na seção de Método (ver `../politica-uso-llm.md`)
- [ ] Enviado com folga — o prazo é 14h00 de quarta

## Calendário

| Quando | O quê |
|---|---|
| ter 25/08 | Submissão abre no Moodle. Baixar o **modelo SBC** |
| qua 26/08 | Aula 2. Combinar a divisão do trabalho com a dupla, por escrito |
| qui 27 – dom 30/08 | **R&N Cap. 4 §4.1** (têmpera simulada e algoritmos evolutivos). Definição formal do TSP |
| seg 31 – ter 01/09 | Representação decidida. Têmpera Simulada rodando, mesmo que tosca |
| **qua 02/09** | 📍 **Andamento em aula**: TSP formalizado, representação decidida, TS funcionando, esqueleto do AG |
| qui 03 – ter 08/09 | AG implementado. Instrumentação. Experimentos rodados |
| qua 09 – seg 14/09 | Redação do artigo — 5 dias não sobram |
| ter 15/09 | Revisão, contagem de páginas, referências, tabela de horas, PDF gerado |
| **qua 16/09** | Entregar de manhã |

## Estratégia com dupla de baixa disponibilidade

Premissa assumida: você toca o caminho crítico e a dupla complementa depois.

**Fique com o que não pode atrasar:** definição formal do TSP, decisão de representação,
Têmpera Simulada, e a instrumentação. São os itens cobrados no andamento de 02/09 e dos quais
todo o resto depende.

**Dê à dupla uma fatia separável e tardia**, que você consegue absorver se não vier: as execuções
em lote com múltiplas sementes, a tabulação dos resultados, e a seção de comparação com as
técnicas de busca clássica do Cap. 3. Nenhuma delas bloqueia as outras.

**Congele as interfaces cedo.** Se a função objetivo, o formato da instância e o formato de saída
dos experimentos estiverem definidos na primeira semana, o trabalho da dupla encaixa sem
retrabalho, mesmo que chegue tarde.

**Registre as horas honestamente, desde já.** O enunciado pede estimativa por integrante e diz
que a intenção é ver a distribuição da carga. Inflar a participação da dupla é falsear o
documento; apagá-la também. Se a distribuição ficar desigual, ela ficou — relate como foi.

## O que instrumentar

A seção de resultados precisa sustentar argumento, não descrever saída.

- **Ambos os algoritmos são estocásticos**: uma execução não é resultado. Rode várias sementes e
  reporte média e dispersão
- Use **instâncias com ótimo conhecido** (TSPLIB tem várias pequenas), para reportar distância
  percentual do ótimo em vez de um número absoluto sem referência
- Conte **avaliações da função objetivo**, não só tempo — é a moeda que permite comparar TS e AG
  de forma justa, já que fazem trabalho por iteração muito diferente
- Guarde a **curva de convergência** (melhor custo × avaliações)
- Registre os parâmetros de cada execução: esquema de resfriamento na TS, tamanho de população,
  taxas e elitismo no AG

## Ponto de apoio conceitual

O item central do enunciado é *onde e como a modelagem se reflete em cada algoritmo*. No TSP, o
eixo que organiza a resposta é a **representação** — e como ela se propaga de forma diferente
para dentro de cada técnica: na Têmpera Simulada ela determina o que conta como vizinhança; no
AG ela restringe quais operadores de recombinação são sequer válidos.

Desenvolver esse argumento é o trabalho avaliado. Não terceirize.

## Perguntas em aberto para o professor

- [ ] O AG é chamado de "técnica de busca local" no enunciado. Em que sentido, se ele mantém
      população e recombina? (o R&N §4.1 tem uma resposta — vale confirmar a leitura dele)
- [ ] Há instância de referência sugerida, ou a equipe escolhe?
- [ ] O repositório no GitHub é opcional ou esperado?

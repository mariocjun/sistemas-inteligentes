# Política de autoria e uso de LLM — ICSI30

Transcrição do que o plano de ensino determina, e como operar dentro disso.

## O que o plano de ensino diz

> PLÁGIO É CRIME e não será tolerado, implicando em REPROVAÇÃO na unidade.
>
> Da mesma maneira, uso de LLMs (Large Language Models — LLMs), tais como ChatGPT, atualmente não
> satisfazem os critérios de AUTORIA acadêmica [...]. Como apontado em tal fonte, notadamente uma
> ATRIBUIÇÃO DE AUTORIA carrega a RESPONSABILIZAÇÃO pelo trabalho, o que NÃO pode ser
> efetivamente APLICADO a LLMs (ou seja, caso fosse, a NOTA É ZERO). Já o eventual uso
> instrumental de um LLM (e.g. como auxiliar em buscas), caso exista, deve ser OBRIGATORIAMENTE
> documentado no Texto, na seção dedicada a MÉTODO e/ou em seção apropriada, DETALHANDO explícita
> e concretamente o tipo, condição, limitações e resultado de tal ação de maneira INEQUÍVOCA.

Referência citada: diretrizes do periódico *Minds and Machines* (Springer),
https://www.springer.com/journal/11023/submission-guidelines

## A regra em uma linha

**Texto ou código entregue tem de ser de autoria própria, porque autoria implica responder por
ele.** Uso instrumental é permitido *e* obrigatoriamente declarado, em detalhe, na seção de Método.

## Linha divisória prática

| Fora do limite (risco de nota zero / reprovação) | Dentro do limite (declarável) |
|---|---|
| Gerar o texto do relatório, do ensaio ou da análise | Localizar referência bibliográfica, que depois se lê na fonte |
| Gerar a implementação da tarefa | Esclarecer dúvida conceitual antes de escrever o próprio código |
| Produzir a resposta e depois "parafrasear" | Revisar ortografia/gramática de texto já escrito por você |
| Pedir a interpretação de um resultado experimental | Pedir contra-argumento a uma interpretação que você já formulou |
| Colar saída de LLM como fundamentação | Usar como interlocutor socrático para testar seu entendimento |

Teste rápido antes de aceitar qualquer ajuda: **se o professor perguntar "por que você fez
assim?" no debate, você consegue defender sem consultar nada?** Se não, a autoria não é sua.

Uso seguro e de alto valor nesta disciplina: pedir *perguntas* sobre o capítulo, não respostas.
Ex.: "me faça 5 perguntas difíceis sobre admissibilidade vs. consistência de heurísticas e
critique minhas respostas" — o produto final continua sendo seu raciocínio.

## Registro

Manter um log em `registro-uso-llm.md` (não versionado até virar entrega) com uma linha por uso:

```
| data | ferramenta/modelo | o que foi pedido | o que foi feito com a saída | limitação observada |
```

Sem esse log, escrever a seção de Método na véspera vira reconstrução de memória — que é
exatamente o oposto de "inequívoca".

## Template da declaração no relatório

Colar na seção de **Método** de toda entrega escrita. Se não houve uso, declarar isso também.

```markdown
### Declaração de uso de ferramentas de apoio (LLM)

**Houve uso instrumental de LLM neste trabalho:** [SIM / NÃO]

<!-- Se NÃO, encerrar aqui com: "Nenhuma ferramenta baseada em LLM foi utilizada em qualquer
     etapa da concepção, implementação, análise ou redação deste trabalho." -->

- **Tipo:** <ferramenta e versão/modelo, ex.: ChatGPT (GPT-x), acesso via navegador>
- **Condição de uso:** <em que etapa exata; ex.: "levantamento de referências sobre heurísticas
  admissíveis, antes da redação da Seção 3; nenhum trecho de texto ou código gerado foi
  incorporado ao trabalho">
- **Consultas realizadas:** <descrição concreta do que foi perguntado; anexar log se extenso>
- **Resultado e destino da saída:** <o que a ferramenta produziu e o que foi efetivamente feito
  com aquilo; ex.: "indicou 4 referências, das quais 2 foram verificadas na fonte primária e
  citadas; as demais não existiam e foram descartadas">
- **Limitações observadas:** <erros, alucinações, imprecisões encontradas na verificação>
- **Autoria:** a concepção, a modelagem, a implementação, a análise dos resultados e a redação
  deste trabalho são de autoria dos signatários, que respondem integralmente por seu conteúdo.
```

# Registro de uso de LLM — projeto grafo-estados-jogos

Log exigido pela `../../politica-uso-llm.md`: uma linha por uso, para que a
seção de Método de qualquer entrega futura seja escrita a partir de
registro, não de memória. Ferramenta em todas as linhas: **Claude Code
(Anthropic), modelos Sonnet 5 / Opus 5 / Fable 5.1 conforme a sessão**,
acesso via terminal, sessão de 2026-09-01 a 2026-09-02.

| data | o que foi pedido | o que foi feito com a saída | limitação observada |
|---|---|---|---|
| 2026-09-01 | Engenharia reversa assistida do binário SLUS-21410 (Ghidra headless, comparação de savestates, patches no ELF) para fazer o jogo bootar direto no Motor Kombat | Os patches foram aplicados e **testados por mim no emulador** em cada rodada; o resultado final (ISO bootando direto na pista) é verificado empiricamente, não tomado da saída do LLM | O LLM **errou 3 hipóteses** antes de acertar (handler `0x18e100` era attract mode, não seleção; slot `0x5A0B08` era do sistema de luta, não do kart; leu o argumento de `jal` na instrução anterior em vez do delay slot). Todas as três foram descobertas por teste, não pela ferramenta. Isso é dado do experimento-piloto (baseline manual), registrado em `caso-motor-kombat.md` |
| 2026-09-02 | Revisão de literatura em 3 frentes (automata learning / PRE; decompilação de jogos e arquitetura de PS2; padrões de game dev) para saber se o problema já tinha nome | A saída (nomes, referências, vocabulário) foi usada para **redigir o rascunho** em `README.md`. **Nenhuma referência foi ainda verificada na fonte primária por mim** — ver coluna ao lado | Busca via web e fontes abertas apenas; **não cobriu ACM DL, DBLP, Google Scholar nem literatura em português**. O próprio LLM apontou isso. Cada DOI/arXiv precisa ser aberto e conferido antes de citar; a política prevê exatamente o risco de referência inexistente |
| 2026-09-02 | Redação de um rascunho de plano de formalização (hipótese, desenho experimental, referências, ligação com a disciplina) | Guardado como `README.md` deste diretório, **rotulado como gerado por LLM no topo**. Destino previsto: reler, verificar, e **reescrever com minhas palavras** antes de qualquer entrega. Nada dele vai para entrega como está | É texto de LLM — pela política, colar como fundamentação seria nota zero. A ligação com Newell & Simon e Gigerenzer foi proposta pelo LLM a partir dos meus resumos no repo; preciso julgar se sustenta |
| 2026-09-02 | Pesquisa sobre rodar o jogo isolado no navegador (Play!.js, EmulatorJS, Parsec) e redução da ISO | Informou decisão de distribuição (Parsec) e a truncagem da ISO, que **testei e funcionou** | Fora do escopo acadêmico; registrado por completude |

## O que é meu e o que não é, neste diretório

- `caso-motor-kombat.md`: registro factual do experimento-piloto — endereços,
  patches, resultados de teste. Os **fatos** foram verificados por mim no
  emulador; a **redação** é do LLM.
- `README.md`: rascunho inteiramente redigido pelo LLM. Não é texto meu.
- `registro-uso-llm.md`: este arquivo, redigido pelo LLM a pedido meu, a
  partir do que aconteceu na sessão.

Antes de qualquer entrega: reescrever, e preencher o template de declaração
da política na seção de Método.

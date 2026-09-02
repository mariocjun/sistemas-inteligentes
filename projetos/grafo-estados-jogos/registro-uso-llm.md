# O que foi pesquisado, e o que ficou por verificar

Histórico da sessão com Claude Code em 2026-09-01/02 (modelos Sonnet 5,
Opus 5 e Fable 5.1, conforme a etapa). Serve para dois propósitos:
rastrear de onde veio cada coisa do `README.md`, e guardar o dado do
experimento-piloto — inclusive os erros, que são a métrica de baseline.

## Engenharia reversa do caso (2026-09-01)

Ghidra headless, comparação de savestates e patches no ELF do SLUS-21410.
**Cada patch foi testado no emulador**; o resultado final (ISO bootando
direto na pista) é verificado empiricamente.

**Três hipóteses erradas antes de acertar** — isso é dado, não anedota:

| Erro | O que era de fato | Como foi descoberto |
|---|---|---|
| handler `0x18e100` | attract mode (a luta demo), não a seleção do kart | patch aplicado → jogo caiu em loop de demo |
| slot `0x5A0B08` | mecanismo do sistema de arenas de luta; o kart não usa | 7 savestates dentro do kart, valor nunca mudou |
| argumento do `jal` lido na instrução anterior | em MIPS o argumento vai no **delay slot**, a instrução seguinte | mapa de estados saiu inteiro errado |

O acerto veio quando parei de deduzir e comparei dois savestates: o único
endereço que mudava entre "menu" e "seleção do kart" era `0x64de88`, o slot
do handler ativo. Total: 5 patches, ~1 dia, 3 erros.

Isso é o **grupo de controle** do experimento descrito no `README.md` §5 —
o custo do método feito à mão, contra o qual medir a versão automatizada.

## Revisão de literatura (2026-09-02)

Três frentes em paralelo: (a) automata learning e protocol reverse
engineering; (b) projetos de decompilação de jogos e arquitetura de PS2;
(c) padrões de game dev e romhacks que isolam modos.

**O que rendeu:** a técnica já tem nome em segurança de redes — *grey-box
state variable identification* (STATEINSPECTOR, USENIX Security 2022) — e
nunca foi aplicada a jogos. E a hipótese forte ("todo jogo de PS2") caiu:
não há arquitetura de PS2 induzida pelo SDK, e jogos da mesma geração usam
mecanismos diferentes. As duas coisas mudaram o `README.md`.

**Limitação para lembrar:** a busca foi por web e fontes abertas (arXiv,
GitHub, sites de projeto). **Não cobriu ACM DL, DBLP, Google Scholar de
forma sistemática, nem literatura em português.** Nenhuma das referências
da §7 foi aberta na fonte — conferir antes de citar em qualquer lugar.

## Distribuição (2026-09-02)

Pesquisa sobre rodar o jogo no navegador (Play!.js, EmulatorJS) e
alternativas. Resultado: PS2 no navegador é experimental e tem teto de 2 GB;
Parsec com guest gamepad é o caminho maduro. A ISO reduzida (2,63 GB, sem
os vídeos) foi gerada e **testada, funciona**.

# Projeto: recuperar a máquina de estados de telas de um jogo compilado

Projeto de hobby, com potencial de virar TCC. Nasceu de um caso real: fazer
Mortal Kombat: Armageddon (PS2) bootar direto no minigame de kart —
documentado em `caso-motor-kombat.md`.

> Rascunho escrito numa sessão com Claude (2026-09-01/02), a partir de
> revisão de literatura e do experimento-piloto. **As referências da §7 não
> foram abertas na fonte** — conferir antes de citar. O que foi pesquisado
> está em `registro-uso-llm.md`. Se virar entrega da disciplina, reler a
> `../../politica-uso-llm.md` antes.

## 1. O achado que abre a introdução

O problema "recuperar a máquina de estados de um sistema opaco observando-o
de fora" foi batizado **quatro vezes, por quatro comunidades que não se
citam**:

| Comunidade | Nome que usa | Âncora |
|---|---|---|
| Métodos formais | *active automata learning* / *model learning* | Angluin 1987 (L\*), Vaandrager 2017 |
| Segurança de redes | *protocol reverse engineering*; no subcaso por memória, **grey-box state variable identification** | STATEINSPECTOR, USENIX Security 2022 |
| Engenharia de software | *specification mining* | Ammons, Bodík, Larus, POPL 2002 |
| TAS / romhacking (informal) | *RAM diffing*, *differential analysis*, "game mode" | wiki Data Crystal, prática de décadas |

E uma quinta comunidade — quem **constrói** jogos — tem o vocabulário de
como isso é implementado: *State pattern* (GoF), *pushdown automaton*
(Nystrom, *Game Programming Patterns*), *ScreenManager* (sample XNA da
Microsoft). Ninguém das quatro primeiras cita a quinta.

Essa constatação é citável por si só e amarra introdução com trabalhos
relacionados.

## 2. O nome da técnica

O que fizemos não tem nome publicado no domínio de jogos. O mais próximo é
o termo do STATEINSPECTOR, e vale adotá-lo com o qualificador do oráculo:

> **Identificação grey-box de variável de estado por diferenciação de
> savestates.**

Grey-box porque não é caixa-preta (olhamos a memória) nem caixa-branca (não
lemos o código todo — o Ghidra deu zero xrefs onde importava). O oráculo é o
savestate do emulador: um dump completo e congelado do estado interno, que
funciona como *membership query* no vocabulário de Angluin.

## 3. A hipótese, reformulada

A versão forte ("todo jogo de PS2 tem isso porque é PS2") **não se
sustenta** e seria refutada rápido: nem o SDK da Sony nem o middleware
(RenderWare, que MK Armageddon usa) induzem convenção de telas. Jogos da
mesma geração implementam o mesmo padrão de jeitos diferentes:

| Jogo / projeto | Mecanismo de estado de tela |
|---|---|
| MK Armageddon (nosso caso, PS2) | pilha de 8 entradas + `push_state`/`pop_state` + despacho por ponteiro de handler |
| Jak and Daxter (OpenGOAL, PS2) | *process* com *state* ativo, macro `go` troca de handler |
| GTA III/VC (re3, RenderWare) | par `m_nCurrentMenuPage` / `m_nPreviousMenuPage`, sem pilha |
| Ocarina of Time (zeldaret, N64) | um único ponteiro de função trocado direto |
| Super Mario 64 (decomp, N64) | interpretador de bytecode de *level script* |

A versão defensável:

> **Todo jogo com múltiplas telas, seguindo a prática convencional da
> indústria (State pattern / pushdown automaton), implementa alguma
> representação explícita de estado — mas o mecanismo varia entre pelo
> menos quatro variantes documentadas — e o método de diferenciação de
> savestates deve recuperá-la independentemente de plataforma, adaptando-se
> ao mecanismo.**

É falsificável (um jogo sem representação explícita a derruba), tem escopo
honesto (não promete PS2, promete "prática convencional"), e sugere o
experimento direto: aplicar em N jogos e catalogar qual variante aparece.

## 4. A contribuição, dita com honestidade

Não é técnica inédita — o insight "achar a variável comparando memória"
existe em pelo menos três lugares. A contribuição é:

1. **Transferência de domínio**: primeira aplicação (encontrada) a binário
   de console, sem fonte, na camada de navegação de telas de um jogo 3D.
2. **Consequência prática original**: usar a máquina recuperada para
   **patchear estaticamente o ELF** e isolar um sub-modo como jogo que boota
   direto. Nem STATEINSPECTOR (que usa a FSM para fuzzing) nem o
   romhacking (que faz *level select* dentro do jogo rodando) fazem isso.
3. **O experimento de generalização** — que ainda não foi feito e é a parte
   empírica real.

Escrever como "aplicação + transferência + estudo de caso completo +
experimento", não como "método novo".

## 5. Desenho experimental

**Unidade de análise**: um jogo. Validação cruzada **por jogo**, nunca por
tela — senão só se prova que decorou o Mortal Kombat.

**Para cada jogo**:
1. Coletar savestates em cada tela do fluxo de abertura até um alvo
2. Diferenciar pares consecutivos; filtrar endereços cujo valor é ponteiro
   de código em ambos os lados → candidatos a slot de handler
3. Confirmar o slot lendo-o num terceiro savestate
4. A partir do handler, subir a cadeia no Ghidra até o despachante
5. Patchear para bootar direto no alvo; testar

**Métricas** (as que importam, na ordem):
- Recuperou a máquina de estados? (sim/não/parcial) — testa a hipótese
- Qual variante de mecanismo? (pilha / ponteiro único / par / bytecode / outra)
- Quantas hipóteses erradas antes de acertar — **a métrica que mais
  importa**, porque é o que a automação eliminaria
- Patches necessários até o boot direto
- Tempo

**Grupo de controle**: o caso Motor Kombat, feito manualmente e registrado
passo a passo, com os erros datados. Baseline honesto: 3 hipóteses erradas
(`0x18e100`, `0x5A0B08` e a leitura errada do delay slot), 5 patches, ~1 dia.

**Amostra**: a coleção de jogos de PS2, mais alguns de outras plataformas
para testar independência de hardware.

**O que falsificaria**: um jogo em que a diferenciação não isola nenhum
ponteiro de código estável, ou em que o estado de tela é implícito no fluxo
de controle sem variável dedicada.

## 6. Ligação com a disciplina

- **Newell & Simon (1975)**: a hipótese reformulada é uma "lei de estrutura
  qualitativa" no sentido deles — afirmação simples, empírica, refutável,
  que reorganiza o problema (de artesanato para busca em grafo). E o texto
  defende que Ciência da Computação é ciência empírica: este trabalho é um
  experimento, não uma prova.
- **Busca (R&N cap. 3)**: o grafo de telas é pequeno (dezenas de nós); BFS
  resolve o caminho. Vale dizer explicitamente que A\* seria overkill. A
  dificuldade real não é buscar no grafo, é **construir** o grafo — nós
  ocultos por indireção só aparecem via observação (savestate). Isso é
  busca com informação parcial, e é a parte interessante.
- **Gigerenzer**: a heurística "compare dois savestates" é ecologicamente
  racional — funciona porque explora uma regularidade real do ambiente
  (jogos guardam o estado de tela em endereço fixo). Trocado o ambiente, a
  heurística falha. Isso dá o critério de escopo: medir *onde* a estrutura
  existe, não afirmar que existe sempre.
- **Automata learning**: hoje o "professor" das queries somos nós. Trabalho
  futuro: substituir por LearnLib/AALpy com um oráculo que consulta o
  emulador (PINE ou savestate), tornando o processo ativo e automático.

## 7. Trabalhos relacionados — o que citar (verificar cada um na fonte)

**Núcleo acadêmico**
1. Angluin, D. (1987). Learning Regular Sets from Queries and Counterexamples. *Information and Computation* 75(2). DOI 10.1016/0890-5401(87)90052-6
2. Vaandrager, F. (2017). Model Learning. *CACM* 60(2). DOI 10.1145/2967606
3. Stone, Thomas, Vanhoef, Henderson, Bailluet, Chothia (2022). The Closer You Look, The More You Learn: A Grey-box Approach to Protocol State Machine Learning. *USENIX Security*. arXiv:2106.02623 — **o mais próximo; comparação explícita obrigatória**
4. Ammons, Bodík, Larus (2002). Mining Specifications. *POPL*. DOI 10.1145/503272.503275
5. Sija et al. (2018). Survey de Protocol Reverse Engineering. *Security and Communication Networks*. DOI 10.1155/2018/8370341
6. Bellemare et al. (2013). The Arcade Learning Environment. *JAIR*. arXiv:1207.4708 — sustenta que a RAM do console é observação markoviana válida do estado
7. Ali et al. (2019). Model Learning: A Survey. *Frontiers of Computer Science*. arXiv:1901.01910

**Técnicas, não peer-reviewed (citar separado)**
8. Nystrom, R. *Game Programming Patterns*, cap. State — gameprogrammingpatterns.com/state.html
9. OpenGOAL, "Process and State" — opengoal.dev/docs/reference/process_and_state/
10. Data Crystal wiki, RAM maps e "Game Mode" — evidência de prática comunitária

**O que a comparação com STATEINSPECTOR precisa dizer**: igual no insight
(memória em runtime revela a variável de estado) e na abordagem grey-box;
diferente no domínio (binário de console em emulador vs. processo TLS com
debugger), no nível de "estado" (navegação de UI vs. protocolo), na
automação (manual, caso único vs. ferramenta avaliada) e na consequência
(patch para isolar modo vs. fuzzing para achar bug).

## 8. Vocabulário por leitor

- Para banca de **IA/métodos formais**: *model learning*, *membership query*,
  *oracle*, *grey-box*.
- Para leitor de **segurança/RE**: *grey-box state variable identification*,
  *stateful variable*, *protocol reverse engineering* como classe-mãe.
- Para leitor de **game dev**: *State pattern*, *pushdown automaton*,
  *ScreenManager*, *game mode*; e, do OpenGOAL, *process/state* com
  *enter/exit/trans/code/post* — descreve com precisão o que as 5
  instruções patcheadas fazem.

## 9. O que ainda falta

- O experimento em N jogos (§5) — é a contribuição empírica
- Automatizar a diferenciação e a filtragem de candidatos (hoje é script
  ad hoc; virar pipeline)
- Construir o grafo automaticamente a partir das chamadas ao `push_state`
  (argumento no delay slot) e comparar com o grafo observado por savestate —
  a divergência entre os dois mede quantos nós são ocultos por indireção
- Trocar o "professor" humano por LearnLib/AALpy (trabalho futuro)

## 10. Caveats

A revisão cobriu buscas na web e fontes primárias abertas (arXiv, GitHub,
sites de projeto), mas **não** varreu ACM DL, DBLP ou Google Scholar de
forma sistemática, nem literatura em português. O gap central (ninguém
aplicou a jogos de console) apareceu consistentemente nas três frentes, mas
vale uma segunda passada formal com o orientador antes de fechar a seção de
trabalhos relacionados. **Cada DOI/arXiv acima precisa ser aberto e
conferido** — a política da disciplina prevê exatamente esse risco.

Material operacional (fora deste repo): skill `ps2-tela-direta` no
`~/.claude/skills/` (método, scripts, armadilhas) e o registro completo do
caso em `caso-motor-kombat.md` aqui ao lado.

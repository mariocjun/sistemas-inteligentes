# Newell & Simon (1976) — *Computer Science as Empirical Inquiry: Symbols and Search*

**Nota sobre este arquivo.** Isto **não é uma tradução** do artigo. É um resumo conceitual
completo, escrito em português e com minhas próprias palavras, cobrindo a estrutura, os
argumentos e os exemplos do texto inteiro — feito porque o artigo é digitalização de 1976 e
resistiu ao pipeline automático de tradução (ver `../../ferramentas/traducao-de-artigos.md`).
O objetivo é entender o conteúdo, não citá-lo; para citar, use o original em inglês
(`1975_SYMBOLS__HEURISTICS_NewellSimon_TuringAward.pdf` ou a versão re-OCRizada e pesquisável
`1975_NewellSimon_TuringAward_reOCR-EN.pdf`).

**Ficha:** Palestra do Prêmio Turing de 1975, entregue a Allen Newell e Herbert A. Simon
(Carnegie-Mellon University) na Conferência Anual da ACM em Minneapolis, 20 de outubro de 1975.
Publicada em *Communications of the ACM*, 19(3), março de 1976, pp. 113–126.

---

## Por que este texto importa para a disciplina

É a fonte primária de duas ideias que atravessam o semestre inteiro: a **Hipótese do Sistema de
Símbolos Físicos** (que aparece nos slides do bloco 1 e do bloco 3, sempre em deck do próprio
Giménez-Lugo) e a ideia de que **inteligência = busca heurística** — o que sustenta os capítulos
3 e 4 do Russell & Norvig. É também o alvo direto da crítica de Rodney Brooks ("elefantes não
jogam xadrez") citada no bloco 1.

## A tese central, em uma frase

**Ciência da Computação é uma ciência empírica** — não uma ramo da matemática — e os autores
provam isso apresentando **duas hipóteses científicas** (testáveis, refutáveis, sustentadas por
evidência empírica, não por dedução formal) que organizam o campo da Inteligência Artificial.

---

## Abertura: o que é uma "lei de estrutura qualitativa"

Antes de apresentar as duas hipóteses, os autores explicam **que tipo de afirmação** elas são.
Toda ciência tem leis que não são fórmulas quantitativas, mas caracterizações qualitativas do que
o domínio *é* — e essas leis, apesar de parecerem simples, costumam ser as descobertas mais
importantes do campo. Quatro exemplos, de áreas bem diferentes:

- **A doutrina celular** (biologia): todo organismo vivo é feito de células. A afirmação é
  simples, mas reorganizou a biologia inteira.
- **Tectônica de placas** (geologia): a superfície da Terra é um conjunto de placas que se movem
  lentamente. Explica terremotos, vulcões, a forma dos continentes — com uma ideia qualitativa,
  não uma equação.
- **Teoria dos germes** (medicina): doenças são causadas por organismos microscópicos que se
  transmitem entre hospedeiros. Tem exceções (nem toda doença é causada por germe), e mesmo assim
  foi uma revolução.
- **Atomismo** (química): os elementos são compostos de partículas uniformes. Diferente dos três
  anteriores, aqui a estrutura era simples o bastante para logo virar teoria quantitativa.

O ponto: leis assim **não são triviais só porque são simples**. Elas fixam os termos dentro dos
quais o resto da ciência vai trabalhar. É esse o status que os autores reivindicam para as duas
hipóteses que vêm a seguir.

---

## Parte I — Sistemas de Símbolos Físicos

### O que é um "símbolo" aqui

Um **sistema de símbolos físicos** é definido com precisão de engenharia, não de metafísica:

- **Símbolos** são padrões físicos (não precisam ser humanos ou linguísticos).
- Símbolos se combinam em **expressões** (estruturas simbólicas).
- O sistema tem **processos** que criam, modificam, copiam e destroem expressões.
- Duas relações são centrais: **designação** (uma expressão pode "apontar para" um objeto, no
  sentido de que o sistema pode agir sobre esse objeto ou em função dele) e **interpretação**
  (o sistema pode executar o processo que uma expressão designa).

Um sistema com essas propriedades — capaz de designar qualquer coisa, criar e modificar
expressões livremente, manter expressões estáveis no tempo, e armazenar essencialmente sem
limite — é, segundo os autores, **essencialmente o mesmo tipo de coisa que um computador de
propósito geral**. Não é coincidência: a definição foi desenhada para bater com o que um
computador (ou uma linguagem como LISP) já faz.

### A Hipótese do Sistema de Símbolos Físicos

> **Um sistema de símbolos físicos possui os meios necessários e suficientes para a ação
> inteligente geral.**

Os autores insistem no peso exato das palavras:

- **"Necessário"**: todo sistema que exibe inteligência geral, analisado de perto, vai se revelar
  um sistema de símbolos físicos.
- **"Suficiente"**: qualquer sistema de símbolos físicos, de tamanho suficiente, pode ser
  organizado para exibir inteligência geral.
- **"Ação inteligente geral"**: o mesmo alcance de inteligência que vemos no comportamento
  humano — comportamento adequado ao objetivo e adaptado ao ambiente, dentro de limites de
  velocidade e complexidade.

E fazem questão de marcar: **isto é uma hipótese empírica, não um teorema.** Poderia ser falsa.
Não há como prová-la por lógica pura — só há como testá-la contra o mundo.

### De onde essa hipótese veio (a genealogia histórica)

Os autores traçam uma linha de desenvolvimento, cada etapa contribuindo uma peça:

1. **Lógica formal** (Frege, Whitehead e Russell) — tratar raciocínio como manipulação de símbolos
   sem significado, segundo regras puramente sintáticas. É o estágio da "manipulação formal de
   símbolos" — mas ainda sem a noção de que o próprio sistema pudesse *interpretar* seus símbolos.
2. **Máquina de Turing** — mostra que esse jogo sintático pode rodar numa máquina física, e
   introduz a noção (parcial) de interpretação: uma descrição pode ser executada.
3. **O conceito de programa armazenado** (anos 1940) — completa a outra metade da interpretação:
   os próprios dados do sistema podem ser tratados como programa.
4. **Processamento de listas** (1956) — a peça que faltava: agora o conteúdo das estruturas de
   dados são símbolos que **designam** algo, não apenas bits inertes. É aqui, dizem os autores,
   que a noção moderna de "símbolo" em Ciência da Computação nasce de fato.
5. **LISP** (McCarthy, 1959-60) — completa a abstração, libertando as listas de qualquer máquina
   concreta.

Cada etapa era necessária; nenhuma sozinha bastava.

### A evidência

Como é hipótese empírica, precisa de evidência — e os autores apontam duas linhas principais:

- **Construir sistemas inteligentes** (a própria pesquisa em IA): testar a *suficiência* da
  hipótese, construindo programas para tarefas cada vez mais amplas — de jogos e quebra-cabeças a
  visão, linguagem natural, coordenação motora.
- **Modelar o comportamento simbólico humano** (psicologia cognitiva): testar a *necessidade* da
  hipótese, verificando se o comportamento inteligente humano pode ser explicado como o
  funcionamento de um sistema de símbolos. Aqui os autores citam explicitamente que muitas ideias
  do GPS (General Problem Solver) vieram da análise de protocolos verbais de sujeitos "pensando em
  voz alta" — uma evidência de mão dupla entre IA e psicologia.

Concluem observando que as **teorias rivais da época** (behaviorismo, teoria da Gestalt) nunca
demonstraram ter mecanismos suficientes para dar conta de comportamento inteligente complexo —
o que deixa a hipótese dos símbolos sem competidor real no momento da palestra.

---

## Parte II — Busca Heurística

### A segunda hipótese

> **Sistemas de símbolos físicos resolvem problemas usando busca heurística: geram e modificam
> progressivamente estruturas simbólicas até produzir uma estrutura-solução.**

O argumento para *por que* isso é necessário: todo sistema de símbolos físicos tem **recursos de
processamento limitados** — executa um número finito de processos em tempo finito. Por isso, na
prática, pode ser tratado como um dispositivo serial (uma coisa de cada vez). E um sistema serial
com recursos escassos, ao resolver um problema, só pode proceder **gerando possibilidades e
testando-as**, uma de cada vez — o que é, por definição, busca.

### O que é "ter um problema"

Os autores dão uma formulação enxuta: **um problema é definido por um teste** (que reconhece
soluções) **e um gerador** (que produz candidatas). Resolver o problema é usar o gerador até
produzir algo que passe no teste.

Isso resolve, dizem eles, o paradoxo do *Mênon* de Platão ("como você pode buscar aquilo que você
não conhece, e como saberia se encontrasse?"). Platão respondeu com a teoria da reminiscência
(você já sabia, de uma vida anterior). A resposta simbólica é mais direta: você não precisa
*conhecer* a solução para ter um gerador capaz de produzi-la e um teste capaz de reconhecê-la.

### O exemplo da equação algébrica

Um exemplo simples e muito didático: resolver `AX + B = CX + D`. Um gerador ingênuo (chutar
números e testar) não seria inteligente. Um gerador melhor usa duas fontes de informação:

- **O que é constante** para toda a classe de problemas (que operações preservam a solução da
  equação — somar/subtrair dos dois lados, etc.)
- **O que muda a cada passo** (a diferença de forma entre a expressão atual e a forma desejada)

Ao comparar a expressão atual com a forma-alvo e escolher a modificação que reduz essa diferença,
o gerador incorpora conhecimento sobre o problema **no próprio processo de gerar**, e não apenas
no teste final. Isso, dizem os autores, é a essência da **análise de meios e fins**
(*means-ends analysis*) — a técnica central do GPS.

### Árvores de busca e o problema da explosão

Quando o "ramo" (branching factor) de um problema é maior que 1, o espaço de busca cresce como
`B^D` (ramificação elevada à profundidade) — a explosão combinatória. Xadrez é o exemplo clássico:
programas chegam a explorar milhões de ramos, enquanto grandes mestres humanos raramente exploram
mais de cem — não porque busquem menos profundo, mas porque **ramificam de forma muito mais
seletiva em cada nó**. A seletividade está embutida no próprio gerador.

**Conclusão "paradoxal" dos autores**: buscar é essencial ao exercício da inteligência, mas a
*quantidade* de busca não é medida de inteligência. Um problema é difícil não porque exige muita
busca, mas porque exigiria muita busca **se não houvesse inteligência suficiente aplicada**.
Quando o sistema sabe o que fazer, vai direto ao objetivo; quando o conhecimento falta, entra em
"terreno desconhecido" e precisa buscar.

### Melhor-primeiro e o kit de técnicas

Os autores descrevem o que já era, em 1975, um "pequeno kit" comum a todo pesquisador de IA:
**busca melhor-primeiro** (escolher o próximo nó que parece mais perto do objetivo) e **análise de
meios e fins** (guiar a busca por diferenças específicas entre o estado atual e o objetivo). Eles
notam que essas técnicas foram reinventadas várias vezes e batizam-nas de **"métodos fracos"**
(*weak methods*) — não porque sejam ruins, mas porque servem exatamente quando o conhecimento do
sistema sobre o domínio não é suficiente para evitar a busca por completo. Contrastam com
situações altamente estruturadas (como programação linear), onde não há ramificação: cada passo
já avança direto para a solução.

### Três formas de reduzir a busca sem eliminá-la

Na parte final, os autores discutem caminhos de pesquisa para tornar sistemas mais inteligentes
sem depender só de buscar mais rápido:

1. **Uso não-local de informação** — hoje, a informação obtida em um nó da árvore de busca costuma
   servir só para aquele nó, e o mesmo fato precisa ser redescoberto em cada ramo. Os autores
   citam esforços (como a análise causal de Berliner em xadrez) para transportar uma informação
   descoberta num ponto para outros contextos onde ela também se aplica.
2. **Sistemas de reconhecimento semântico** — em vez de buscar, **reconhecer** um padrão já visto.
   O exemplo é o mestre de xadrez, cuja perícia vem em boa parte de reconhecer dezenas de milhares
   de padrões de tabuleiro armazenados, não de calcular mais rápido. Reconhecimento substitui busca
   quando o padrão carrega muita informação sobre a estrutura do problema.
3. **Escolha de representação apropriada** — o exemplo clássico é o problema do tabuleiro de damas
   mutilado (cortar dois cantos opostos de um tabuleiro 8×8 e perguntar se ele ainda pode ser
   coberto por peças de dominó). Tentar todas as coberturas possíveis é buscar ingenuamente; notar
   que as duas casas cortadas são da mesma cor, e que cada peça cobre uma casa de cada cor, resolve
   o problema **sem buscar nada** — só que, dizem os autores, isso não elimina a busca, apenas a
   **desloca** para o espaço de representações possíveis. Como escolher boa representação é, em
   1975, "território quase inexplorado".

---

## Conclusão do artigo

Os autores fecham revisitando as duas leis: **símbolos físicos** dão o material da inteligência;
**busca heurística** é o mecanismo pelo qual esse material resolve problemas. Chamam a atenção
para o caráter das próprias leis — mais parecidas com geologia ou biologia evolutiva do que com
física teórica: qualitativas, não-matemáticas, mas fortes o bastante para orientar a construção de
sistemas reais.

Terminam citando a última frase do artigo de 1950 de Alan Turing (a quem a palestra presta
homenagem): que só se pode ver um pouco à frente, mas há bastante para fazer com o que se vê — e
reafirmam que a pergunta central para todo sistema de símbolos físicos, condenado à busca serial,
continua sendo sempre a mesma: **o que fazer a seguir?**

---

## Ganchos para o debate da disciplina

- A hipótese diz que símbolos físicos são **necessários e suficientes**. O "elefantes não jogam
  xadrez" de Brooks (bloco 1) ataca principalmente a **suficiência** — argumenta que corpo e
  ambiente fazem trabalho cognitivo que o modelo simbólico atribui inteiramente a símbolos
  internos. Vale perguntar: o argumento de Brooks também ataca a *necessidade*, ou só a
  suficiência?
- A "análise de meios e fins" do exemplo algébrico é, estruturalmente, o mesmo esqueleto da busca
  informada do Cap. 3 do R&N: usar uma medida de diferença/distância para guiar a geração. Vale
  comparar com a heurística `h(n)` de A\*.
- Os "métodos fracos" (best-first, means-ends) são explicitamente descritos como recurso para
  quando falta conhecimento específico do domínio — o oposto de sistemas com muito conhecimento
  semântico embutido (como os "sistemas de reconhecimento" do xadrez mestre). Isso antecipa a
  tensão entre busca genérica e aprendizado/representação específica de domínio que atravessa o
  resto do semestre (blocos 3 e 4).

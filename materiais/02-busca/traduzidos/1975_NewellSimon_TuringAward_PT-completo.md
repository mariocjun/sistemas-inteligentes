# Ciência da Computação como Investigação Empírica: Símbolos e Busca

**Allen Newell e Herbert A. Simon** — Palestra do Prêmio Turing da ACM, 1975

**Nota sobre este arquivo.** Esta é uma **tradução integral**, feita à mão (não pelo pipeline
`pdf2zh`), do texto completo da palestra. O PDF original é uma digitalização de 1976 cuja camada
de OCR resistiu a todas as tentativas de correção automática (`--redo-ocr`, `--force-ocr`,
`--ocr-workaround` combinados de várias formas — ver `../../ferramentas/traducao-de-artigos.md`);
mesmo depois de um re-OCR de boa qualidade, o texto extraído vem fora de ordem de leitura (colunas
misturadas), o que confunde o tradutor automático. Esta tradução foi feita lendo o artigo
diretamente — reconstruindo a ordem de leitura a partir das duas colunas — e vertendo cada
parágrafo para o português com o cuidado de preservar os exemplos, as citações e a estrutura
formal dos dois argumentos centrais. Substitui, como referência de estudo, o resumo conceitual em
`1975_NewellSimon_resumo-conceitual-PT.md` (mantido por ainda ser útil como visão rápida) e a
tradução parcial em `1975_NewellSimon_TuringAward_PT-dual-PARCIAL.pdf` (mantida por registro
histórico da tentativa automática).

**Ficha:** Palestra do Prêmio Turing de 1975, entregue a Allen Newell e Herbert A. Simon
(Carnegie-Mellon University) na Conferência Anual da ACM, em Minneapolis, 20 de outubro de 1975.
Publicada em *Communications of the ACM*, v. 19, n. 3, março de 1976, pp. 113–126.

Para citar o original: NEWELL, A.; SIMON, H. A. Computer Science as Empirical Inquiry: Symbols
and Search. *Communications of the ACM*, v. 19, n. 3, mar. 1976, p. 113–126.

---

## A citação de apresentação do prêmio

*Lida por Bernard A. Galler, presidente do Comitê do Prêmio Turing:*

> "É um privilégio poder apresentar o Prêmio Turing da ACM a dois amigos de longa data, os
> professores Allen Newell e Herbert A. Simon, ambos da Carnegie-Mellon University.
>
> "Em esforços científicos conjuntos que se estendem por vinte anos, inicialmente em colaboração
> com J. C. Shaw na RAND Corporation, e depois com numerosos colegas docentes e alunos na
> Carnegie-Mellon University, eles deram contribuições básicas à inteligência artificial, à
> psicologia da cognição humana e ao processamento de listas.
>
> "Em inteligência artificial, contribuíram para estabelecer o campo como uma área de empreitada
> científica, para o desenvolvimento da programação heurística em geral, e da busca heurística,
> da análise de meios e fins, e de métodos de indução em particular; fornecendo demonstrações da
> suficiência desses mecanismos para resolver problemas interessantes.
>
> "Em psicologia, foram os principais instigadores da ideia de que a cognição humana pode ser
> descrita em termos de um sistema de símbolos, e desenvolveram teorias detalhadas para a
> resolução humana de problemas, aprendizagem verbal e comportamento indutivo em vários domínios
> de tarefa, usando programas de computador que incorporam essas teorias para simular o
> comportamento humano.
>
> "Foram, ao que tudo indica, os inventores do processamento de listas, e foram grandes
> contribuidores tanto para a tecnologia de software quanto para o desenvolvimento do conceito do
> computador como um sistema que manipula estruturas simbólicas, e não apenas como processador de
> dados numéricos.
>
> "É uma honra para os professores Newell e Simon receber este prêmio, mas é também uma honra
> para a ACM poder acrescentar seus nomes à nossa lista de agraciados, já que, por sua presença,
> eles somam prestígio e importância ao Prêmio Turing da ACM."

---

## Abertura

Ciência da computação é o estudo dos fenômenos que cercam os computadores. Os fundadores desta
sociedade entenderam isso muito bem quando se chamaram *Association for Computing Machinery* —
Associação para a Maquinaria de Computar. A máquina — não só o hardware, mas a máquina viva,
programada — é o organismo que estudamos.

Esta é a décima Palestra Turing. As nove pessoas que nos precederam neste palco apresentaram nove
visões diferentes da ciência da computação. Pois nosso organismo, a máquina, pode ser estudado em
muitos níveis e de muitos lados. Sentimo-nos profundamente honrados por estar aqui hoje para
apresentar mais uma visão — aquela que permeou o trabalho científico pelo qual fomos citados.

Nossa visão é apenas uma entre muitas; as palestras anteriores deixam isso claro. Porém, mesmo
somadas, as palestras não cobrem todo o escopo da nossa ciência. Muitos aspectos fundamentais dela
não foram representados nestes dez prêmios. E se algum dia chegar o momento em que a bússola tiver
percorrido todos os pontos, em que a ciência da computação tiver sido discutida de todos os
ângulos, será hora de recomeçar o ciclo — pois, para a lebre que discursa, será preciso um sprint
anual para alcançar o acúmulo de pequenos ganhos incrementais que a tartaruga do desenvolvimento
científico e técnico já alcançou. A cada ano se abrirá uma nova lacuna, exigindo um novo sprint,
porque em ciência não existe a última palavra.

Nosso propósito aqui, no entanto, não é pleitear compreensão do mundo exterior. É examinar um
aspecto de nossa ciência: o desenvolvimento de nova compreensão básica por meio da investigação
empírica. Isso se faz melhor por ilustração. Sejamos perdoados se, aproveitando a ocasião,
escolhemos nossos exemplos da área de nossa própria pesquisa. Como ficará claro, esses exemplos
envolvem todo o desenvolvimento da inteligência artificial, especialmente em seus primeiros anos.
Eles se apoiam em muito mais do que nossas próprias contribuições pessoais — e mesmo onde demos
contribuições diretas, isso foi feito em cooperação com outros. Nossos colaboradores incluíram
especialmente Cliff Shaw, com quem formamos um time de três ao longo do período empolgante do fim
dos anos 1950; mas também trabalhamos com muitos outros colegas e alunos na Carnegie-Mellon
University.

Ciência da computação é uma disciplina empírica. Nós a chamaríamos de ciência experimental, mas,
como a astronomia, a economia e a geologia, algumas de suas formas peculiares de observação e
experiência não se encaixam no estereótipo estreito do método experimental. Ainda assim, são
experimentos. Cada nova máquina que se constrói é um experimento. Construir de fato a máquina
coloca uma pergunta à natureza; e ouvimos a resposta observando a máquina em operação e a
analisando por todos os meios analíticos e de medição disponíveis. Cada novo programa que se
constrói é um experimento. Ele coloca uma pergunta à natureza, e seu comportamento oferece pistas
para uma resposta. Nem máquinas nem programas são caixas-pretas; são artefatos que foram
projetados, tanto o hardware quanto o software, e podemos abri-los e olhar dentro. Podemos
relacionar sua estrutura ao seu comportamento e tirar muitas lições de um único experimento. Não
precisamos construir 100 cópias de, digamos, um provador de teoremas, para demonstrar
estatisticamente que ele não superou a explosão combinatória da busca do jeito que se esperava. A
inspeção do programa à luz de algumas execuções revela a falha e nos deixa prontos para a próxima
tentativa.

Construímos computadores e programas por muitas razões. Construímo-los para servir à sociedade e
como ferramentas para realizar as tarefas econômicas da sociedade. Mas, como cientistas básicos,
construímos máquinas e programas como forma de descobrir novos fenômenos e analisar fenômenos que
já conhecemos. A sociedade muitas vezes se confunde quanto a isso, acreditando que computadores e
programas só devem ser construídos para o uso econômico que se pode fazer deles (ou como itens
intermediários numa sequência de desenvolvimento que leva a esse uso). É preciso entender que os
fenômenos que cercam os computadores são profundos e obscuros, exigindo muita experimentação para
que sua natureza seja avaliada. É preciso entender que, como em qualquer ciência empírica, os
ganhos obtidos com essa experimentação e compreensão se traduzem na aquisição permanente de novas
técnicas; e que são essas técnicas que vão criar os instrumentos para ajudar a sociedade a atingir
seus objetivos.

Falaremos de ciência da computação como investigação empírica.

## I. Símbolos e Sistemas de Símbolos Físicos

Uma das contribuições fundamentais ao conhecimento dadas pela ciência da computação foi explicar,
em um nível bastante básico, o que são símbolos. Essa explicação é uma proposição científica sobre
a Natureza. Ela é derivada empiricamente, com um desenvolvimento longo e gradual.

Os símbolos estão na raiz da ação inteligente, que é, claro, o tópico primário da inteligência
artificial. Aliás, é uma questão primária para toda a ciência da computação, pois toda informação é
processada por computadores a serviço de fins, e medimos a inteligência de um sistema por sua
capacidade de atingir fins declarados diante de variações, dificuldades e complexidades impostas
pelo ambiente da tarefa. Esse investimento geral da ciência da computação em atingir inteligência
fica obscurecido quando as tarefas realizadas são limitadas em escopo, pois aí as variações do
ambiente podem ser previstas com precisão. Ele se torna mais óbvio à medida que estendemos os
computadores a tarefas mais globais, complexas e intensivas em conhecimento — à medida que
tentamos torná-los nossos agentes, capazes de lidar por conta própria com todas as contingências
do mundo natural.

Nossa compreensão dos requisitos de sistema para a ação inteligente emerge lentamente. Ela é
composta, pois nenhuma coisa elementar isolada explica a inteligência em todas as suas
manifestações. Não existe um "princípio da inteligência", assim como não existe um "princípio
vital" que transmita, por sua própria natureza, a essência da vida. Mas a ausência de um simples
*deus ex machina* não implica que não existam requisitos estruturais para a inteligência. Um
desses requisitos é a capacidade de armazenar e manipular símbolos. Para formular a pergunta
científica, podemos parafrasear o título de um artigo célebre de Warren McCulloch [1961]: o que é
um símbolo, que a inteligência possa usá-lo, e o que é a inteligência, que possa usar um símbolo?

### Leis de estrutura qualitativa

Todas as ciências caracterizam a natureza essencial dos sistemas que estudam. Essas
caracterizações são invariavelmente qualitativas em sua natureza, pois fixam os termos dentro dos
quais um conhecimento mais detalhado pode ser desenvolvido. Sua essência muitas vezes pode ser
capturada em afirmações muito curtas e muito gerais. Poder-se-ia julgar que essas leis gerais, por
sua especificidade limitada, contribuem relativamente pouco para a soma de uma ciência — não
fosse a evidência histórica que mostra serem elas resultados da maior importância.

**A doutrina da célula, em biologia.** Um bom exemplo de lei de estrutura qualitativa é a doutrina
da célula em biologia, que afirma que o bloco de construção básico de todos os organismos vivos é
a célula. As células vêm numa grande variedade de formas, embora todas tenham um núcleo cercado
por protoplasma, o conjunto envolto por uma membrana. Mas essa estrutura interna não fazia parte,
historicamente, da especificação da doutrina da célula; foi especificidade desenvolvida depois,
por investigação intensiva. A doutrina da célula pode ser transmitida quase inteiramente pela
afirmação que demos acima, junto com algumas noções vagas sobre o tamanho que uma célula pode ter.
O impacto dessa lei sobre a biologia, no entanto, foi tremendo, e o tempo perdido no campo antes de
sua aceitação gradual foi considerável.

**A tectônica de placas, em geologia.** A geologia oferece um exemplo interessante de lei de
estrutura qualitativa — interessante porque ganhou aceitação apenas na última década, de modo que
sua ascensão de status ainda está fresca na memória. A teoria da tectônica de placas afirma que a
superfície do globo é um conjunto de enormes placas — algumas dezenas ao todo — que se movem (em
velocidades geológicas) umas contra as outras, sobre e sob umas às outras, até o centro da Terra,
onde perdem sua identidade. Os movimentos das placas explicam as formas e localizações relativas
dos continentes e oceanos, as áreas de atividade vulcânica e sísmica, as fossas oceânicas
profundas, e assim por diante. Com alguns detalhes adicionais sobre velocidade e tamanho, a teoria
essencial estava especificada. Ela não foi aceita, claro, até conseguir explicar uma série de
detalhes que se encaixavam entre si (por exemplo, semelhanças de flora, fauna e estratificação
entre a África Ocidental e o Nordeste da América do Sul). A teoria da tectônica de placas é
altamente qualitativa. Agora que foi aceita, a Terra inteira parece oferecer evidência para ela em
toda parte, pois passamos a ver o mundo em seus termos.

**A teoria dos germes, em medicina.** A teoria dos germes da doença é pouco mais do que um século
mais nova que Pasteur — uma lei de estrutura qualitativa que produziu uma revolução na medicina. A
teoria propõe que a maioria das doenças é causada pela presença e multiplicação, no corpo, de
minúsculos organismos vivos unicelulares, e que o contágio consiste na transmissão desses
organismos de um hospedeiro a outro. Boa parte da elaboração da teoria consistiu em identificar os
organismos associados a doenças específicas, descrevê-los, e traçar seu histórico de vida. O fato
de a lei ter muitas exceções — que muitas doenças não são produzidas por germes — não diminui sua
importância. A lei nos diz onde procurar um determinado tipo de causa; não insiste que sempre a
encontraremos.

**A doutrina do atomismo, em química.** A doutrina do atomismo oferece um contraste interessante
com as três leis de estrutura qualitativa que acabamos de descrever. Tal como emergiu do trabalho
de Dalton e de suas demonstrações de que os elementos químicos se combinavam em proporções fixas,
a lei forneceu um exemplo típico de estrutura qualitativa: os elementos são compostos de pequenas
partículas uniformes, diferentes de um elemento para outro. Mas, como as espécies subjacentes de
átomos são tão simples e limitadas em sua variedade, logo se formularam teorias quantitativas que
assimilaram toda a estrutura geral da hipótese qualitativa original. Com células, placas
tectônicas e germes, a variedade de estrutura é tão grande que o princípio qualitativo subjacente
permanece distinto, e sua contribuição para a teoria total é claramente discernível.

Leis de estrutura qualitativa são vistas por toda a ciência. Algumas de nossas maiores descobertas
científicas estão entre elas. Como os exemplos ilustram, elas costumam fixar os termos sobre os
quais toda uma ciência opera, e são importantes, com consequências de longo alcance.

### Sistemas de símbolos físicos

Voltemos ao tópico dos símbolos, e definamos um **sistema de símbolos físicos**. O adjetivo
"físico" denota duas características importantes: (1) tais sistemas obviamente obedecem às leis
da física — são realizáveis por sistemas construídos com componentes de engenharia; (2) embora
nosso uso do termo "símbolo" prefigure a interpretação que pretendemos dar a ele, não estamos
restritos a sistemas de símbolos humanos.

Um sistema de símbolos físicos consiste em um conjunto de entidades, chamadas símbolos, que são
padrões físicos que podem ocorrer como componentes de outro tipo de entidade chamada expressão (ou
estrutura simbólica). Assim, uma estrutura simbólica é composta de várias instâncias (ou tokens)
de símbolos relacionados de alguma forma física (como um token estar ao lado de outro). A qualquer
instante, o sistema conterá uma coleção dessas estruturas simbólicas. Além dessas estruturas, o
sistema também contém uma coleção de processos que operam sobre expressões para produzir outras
expressões: processos de criação, modificação, reprodução e destruição. Um sistema de símbolos
físicos é uma máquina que produz, ao longo do tempo, uma coleção evolutiva de estruturas
simbólicas. Tal sistema existe em um mundo de objetos mais amplo do que apenas essas expressões
simbólicas em si.

Duas noções são centrais para essa estrutura de expressões, símbolos e objetos: **designação** e
**interpretação**.

- **Designação.** Uma expressão *designa* um objeto se, dada a expressão, o sistema pode ou afetar
  o próprio objeto, ou se comportar de maneiras que dependem do objeto. Em qualquer dos casos, o
  acesso ao objeto por meio da expressão foi obtido — o que é a essência da designação.
- **Interpretação.** O sistema pode *interpretar* uma expressão se a expressão designa um
  processo, e se, dada a expressão, o sistema pode executar o processo. A interpretação implica
  uma forma especial de ação dependente: dada uma expressão, o sistema pode realizar o processo
  indicado, isto é, pode evocar e executar seus próprios processos a partir de expressões que os
  designam.

Um sistema capaz de designação e interpretação, no sentido que acabamos de indicar, deve também
atender a vários outros requisitos, de completude e fechamento. Teremos espaço só para mencioná-los
brevemente; todos são bem conhecidos: (1) um símbolo pode ser usado para designar qualquer
expressão, seja qual for — ou seja, dado um símbolo, não é prescrito *a priori* quais expressões
ele pode designar; essa arbitrariedade cabe só aos símbolos, os tokens simbólicos e suas relações
mútuas é que determinam qual objeto é designado por uma expressão complexa; (2) existem expressões
que designam todo processo do qual a máquina é capaz; (3) existem processos para criar qualquer
expressão e para modificar qualquer expressão de formas arbitrárias; (4) as expressões são
estáveis — uma vez criadas, continuam existindo até serem explicitamente modificadas ou apagadas;
(5) o número de expressões que o sistema pode manter é essencialmente ilimitado.

O tipo de sistema que acabamos de definir não é estranho aos cientistas da computação. Ele guarda
forte parentesco com todos os computadores de propósito geral. Se uma linguagem de manipulação
simbólica como LISP for tomada como definindo uma máquina, o parentesco se torna verdadeiramente
fraternal. Nossa intenção, ao delinear tal sistema, não é propor algo novo. Muito pelo contrário: é
mostrar quais sistemas satisfazem essa caracterização.

### A Hipótese do Sistema de Símbolos Físicos

Podemos agora enunciar uma hipótese científica geral — uma lei de estrutura qualitativa para
sistemas de símbolos:

> **A Hipótese do Sistema de Símbolos Físicos.** *Um sistema de símbolos físicos possui os meios
> necessários e suficientes para a ação inteligente geral.*

Por "necessários" queremos dizer que qualquer sistema que exiba inteligência geral se mostrará,
mediante análise, um sistema de símbolos físicos. Por "suficientes" queremos dizer que qualquer
sistema de símbolos físicos de tamanho suficiente pode ser organizado ainda mais para exibir
inteligência geral. Por "ação inteligente geral" queremos indicar o mesmo escopo de inteligência
que vemos na ação humana: que em qualquer situação real ocorra um comportamento apropriado aos
fins do sistema e adaptado às exigências do ambiente, dentro de certos limites de velocidade e
complexidade.

A Hipótese do Sistema de Símbolos Físicos é claramente uma lei de estrutura qualitativa. Ela
especifica uma classe geral de sistemas dentro da qual se encontrarão aqueles capazes de ação
inteligente.

Esta é uma hipótese empírica. Definimos uma classe de sistemas; queremos perguntar se essa classe
dá conta de um conjunto de fenômenos que encontramos no mundo real. A ação inteligente está por
toda parte ao nosso redor no mundo biológico, sobretudo no comportamento humano. É uma forma de
comportamento que podemos reconhecer por seus efeitos, seja ela realizada por humanos ou não. A
hipótese poderia, de fato, ser falsa. O comportamento inteligente não é hoje tão fácil de produzir
a ponto de qualquer sistema exibi-lo indiscriminadamente. Aliás, há pessoas cujas análises as levam
a concluir, seja por motivos filosóficos, seja por motivos científicos, que a hipótese é falsa.
Cientificamente, só se pode atacá-la ou defendê-la trazendo evidência empírica sobre o mundo
natural.

Precisamos agora traçar o desenvolvimento dessa hipótese e examinar a evidência a favor dela.

### O desenvolvimento da Hipótese do Sistema de Símbolos

Um sistema de símbolos físicos é uma instância de uma máquina universal. Assim, a hipótese do
sistema de símbolos implica que a inteligência será realizada por um computador universal. Porém,
a hipótese vai muito além do argumento, comumente feito com base no determinismo físico em geral,
de que qualquer computação realizável pode ser realizada por uma máquina universal, desde que seja
especificada. Pois ela afirma especificamente que a máquina inteligente é um sistema de símbolos,
fazendo assim uma afirmação arquitetural específica sobre a natureza dos sistemas inteligentes. É
importante entender como essa especificidade adicional surgiu.

**Lógica formal.** As raízes da hipótese remontam ao programa de Frege e de Whitehead e Russell
para formalizar a lógica: capturar as noções conceituais básicas da matemática em lógica e colocar
as noções de prova e dedução sobre um fundamento seguro. Esse esforço culminou na lógica
matemática — nossas familiares lógicas proposicional, de primeira ordem e de ordem superior. Ele
desenvolveu uma visão característica, muitas vezes chamada de "o jogo dos símbolos": a lógica, e
por incorporação toda a matemática, era um jogo jogado com tokens desprovidos de significado,
segundo certas regras puramente sintáticas. Todo significado havia sido expurgado. Tinha-se um
sistema mecânico, ainda que permissivo (hoje diríamos não determinístico), sobre o qual várias
coisas podiam ser provadas. Assim, o progresso foi feito, a princípio, afastando-se de tudo que
parecia relevante para o significado e para os símbolos humanos. Poderíamos chamar isso de estágio
da **manipulação formal de símbolos**.

Essa atitude geral se reflete bem no desenvolvimento da teoria da informação. Apontou-se repetidas
vezes que Shannon havia definido um sistema útil apenas para comunicação e seleção, e que nada
tinha a ver com significado. Manifestou-se pesar por um nome tão geral quanto "teoria da
informação" ter sido dado ao campo, e tentou-se rebatizá-lo como "teoria da informação seletiva" —
sem sucesso algum, claro.

**Máquinas de Turing e o computador digital.** O desenvolvimento dos primeiros computadores
digitais e da teoria dos autômatos, começando com o próprio trabalho de Turing nos anos 1930, pode
ser tratado em conjunto. Concordam quanto ao que é essencial. Usemos o próprio modelo de Turing,
pois ele mostra bem as características.

Uma máquina de Turing consiste em duas memórias: uma fita ilimitada e um controle de estados
finito. A fita guarda os dados — os famosos zeros e uns. A máquina tem um pequeno conjunto de
operações próprias — ler, escrever, e mover-se sobre a fita. A operação de leitura não é uma
operação sobre dados, mas fornece o ramo condicional para um estado de controle em função dos
dados sob a cabeça de leitura. Como todos sabemos, esse modelo contém os elementos essenciais de
todos os computadores, em termos do que eles podem fazer — embora outros computadores, com
memórias e operações diferentes, possam realizar as mesmas computações com requisitos diferentes
de espaço e tempo. Em particular, o modelo de máquina de Turing contém, em si, as noções tanto do
que não pode ser computado quanto de máquinas universais — computadores que conseguem fazer
qualquer coisa que qualquer outra máquina faça.

Deveríamos maravilhar-nos com o fato de que duas de nossas mais profundas percepções sobre
processamento de informação foram alcançadas nos anos 1930, antes mesmo de os computadores
modernos existirem. É um tributo ao gênio de Alan Turing. É também um testemunho da profundidade da
dívida da ciência da computação para com ele. Concomitantemente ao trabalho de Turing surgiu o
trabalho dos lógicos Emil Post e (independentemente) Alonzo Church. Partindo de noções
independentes de sistemas logísticos (produções de Post e funções recursivas, respectivamente),
chegaram a resultados análogos sobre indecidibilidade e universalidade — resultados logo mostrados
como implicando que os três sistemas eram equivalentes. Aliás, a convergência de todas essas
tentativas de definir a classe mais geral de sistemas de processamento de informação fornece parte
da força de nossa convicção de que capturamos os elementos essenciais do processamento de
informação nesses modelos.

Em nenhum desses sistemas há, na superfície, um conceito do símbolo como algo que designa.

**O conceito de programa armazenado.** Com o desenvolvimento da segunda geração de máquinas
eletrônicas em meados dos anos 1940 (depois do ENIAC), veio o conceito de programa armazenado.
Isso foi corretamente saudado como um marco, tanto conceitual quanto praticamente. Programas agora
podem ser dados, e podem ser operados como dados. Essa capacidade, claro, já está implícita no
modelo de Turing: as descrições estão na mesma fita que os dados. No entanto, a ideia só se
concretizou quando as máquinas adquiriram memória suficiente para tornar praticável localizar
programas de fato em algum lugar interno. Afinal, o ENIAC tinha apenas vinte registradores.

O conceito de programa armazenado incorpora a segunda metade do princípio de interpretação, a
parte que diz que os próprios dados do sistema podem ser interpretados. Mas ainda não contém a
noção de designação — da relação física que fundamenta o significado.

**Processamento de listas.** O passo seguinte, dado em 1956, foi o processamento de listas. O
conteúdo das estruturas de dados passou a ser, agora, símbolos, no sentido de nosso sistema de
símbolos físicos: padrões que designavam, que tinham referentes. Listas guardavam endereços que
permitiam acesso a outras listas — daí a noção de estruturas de lista. Que essa era uma visão nova
ficou demonstrado muitas vezes, nos primeiros dias do processamento de listas, quando colegas
perguntavam onde estavam os dados — isto é, qual lista, no fim das contas, continha as coleções de
bits que eram o conteúdo do sistema. Achavam estranho que não houvesse tais bits, que houvesse
apenas símbolos que designavam outras estruturas simbólicas.

O processamento de listas é, simultaneamente, três coisas no desenvolvimento da ciência da
computação. (1) É a criação de uma estrutura de memória genuinamente dinâmica numa máquina que até
então era percebida como tendo estrutura fixa. Acrescentou ao nosso conjunto de operações aquelas
que constroem e modificam estrutura, além das que substituem e mudam conteúdo. (2) Foi uma
demonstração precoce da abstração básica de que um computador consiste num conjunto de tipos de
dado e num conjunto de operações próprias a esses tipos de dado, de modo que um sistema
computacional deveria empregar quaisquer tipos de dado apropriados à aplicação, independentemente
da máquina subjacente. (3) O processamento de listas produziu um modelo de designação, definindo
assim a manipulação de símbolos no sentido em que usamos esse conceito na ciência da computação
hoje.

Como costuma acontecer, a prática da época já antecipava todos os elementos do processamento de
listas: endereços obviamente eram usados para obter acesso, as máquinas de tambor usavam programas
encadeados (o chamado endereçamento um-mais-um), e assim por diante. Mas a concepção do
processamento de listas como abstração criou um mundo novo, no qual designação e estrutura
simbólica dinâmica eram as características definidoras. A inserção dos primeiros sistemas de
processamento de listas em linguagens (as IPLs, o LISP) muitas vezes foi criticada por ter sido uma
barreira à difusão das técnicas de processamento de listas por toda a prática da programação; mas
foi o veículo que manteve a abstração coesa.

**LISP.** Vale notar mais um passo: a criação do LISP por McCarthy, em 1959-60 [McCarthy, 1960].
Ele completou o ato de abstração, retirando as estruturas de lista de sua inserção em máquinas
concretas, criando um novo sistema formal com as S-expressions, que podia ser mostrado equivalente
aos outros esquemas universais de computação.

**Conclusão.** Que o conceito de símbolo designador e de manipulação de símbolos só emerja em
meados dos anos 1950 não significa que os passos anteriores tenham sido inessenciais ou menos
importantes. O conceito total é a junção de computabilidade, realizabilidade física (e por
múltiplas tecnologias), universalidade, representação simbólica de processos (isto é,
interpretabilidade) e, por fim, estrutura simbólica e designação. Cada um dos passos forneceu uma
parte essencial do todo.

O primeiro passo dessa cadeia, de autoria de Turing, é motivado teoricamente, mas todos os outros
têm raízes profundamente empíricas. Fomos conduzidos pela própria evolução do computador. O
princípio do programa armazenado surgiu da experiência com o ENIAC. O processamento de listas
surgiu da tentativa de construir programas inteligentes. Tomou sua deixa do surgimento das
memórias de acesso aleatório, que forneceram uma clara realização física de um símbolo designador
no endereço. O LISP surgiu da experiência em evolução com o processamento de listas.

### A evidência

Chegamos agora à evidência para a hipótese de que sistemas de símbolos físicos são capazes de ação
inteligente, e de que a ação inteligente geral requer um sistema de símbolos físicos. A hipótese é
uma generalização empírica, não um teorema. Não conhecemos nenhuma forma de demonstrar a conexão
entre sistemas de símbolos e inteligência em bases puramente lógicas. Na falta de tal
demonstração, precisamos olhar para os fatos. Nosso objetivo central, porém, não é revisar a
evidência em detalhe, mas usar o exemplo diante de nós para ilustrar a proposição de que a ciência
da computação é um campo de investigação empírica. Assim, indicaremos apenas que tipos de
evidência existem, e a natureza geral do processo de teste.

A noção de sistema de símbolos físicos havia tomado, essencialmente, sua forma atual em meados dos
anos 1950, e é possível datar desse período o crescimento da inteligência artificial como um
subcampo coerente da ciência da computação. Os vinte anos de trabalho desde então viram um acúmulo
contínuo de evidência empírica de dois tipos principais. O primeiro se dirige à suficiência dos
sistemas de símbolos físicos para produzir inteligência, tentando construir e testar sistemas
específicos que tenham essa capacidade. O segundo tipo de evidência se dirige à necessidade de
haver um sistema de símbolos físicos onde quer que a inteligência seja exibida. Há outras formas de
evidência, sobre as quais comentaremos brevemente mais adiante, mas essas duas são as importantes.
Vamos considerá-las por sua vez. A primeira é geralmente chamada de inteligência artificial; a
segunda, pesquisa em psicologia cognitiva.

**Construindo sistemas inteligentes.** O paradigma básico para o teste inicial da teoria dos
germes da doença era: identificar uma doença; depois procurar o germe. Um paradigma análogo
inspirou boa parte da pesquisa em inteligência artificial: identificar um domínio de tarefa que
exija inteligência; depois construir um programa, para um computador digital, capaz de lidar com
tarefas nesse domínio. As tarefas fáceis e bem-estruturadas foram examinadas primeiro: quebra-
cabeças e jogos, problemas de pesquisa operacional de escalonamento e alocação de recursos, tarefas
simples de indução. Dezenas, se não centenas, de programas desses tipos já foram construídos, cada
um capaz de alguma medida de ação inteligente no domínio apropriado.

É claro que a inteligência não é uma questão de tudo ou nada, e houve progresso constante rumo a
níveis mais altos de desempenho em domínios específicos, bem como rumo à ampliação do leque desses
domínios. Os primeiros programas de xadrez, por exemplo, eram considerados bem-sucedidos se
conseguissem jogar legalmente e com algum indício de propósito; um pouco depois, alcançaram o nível
de iniciantes humanos; dentro de dez ou quinze anos, começaram a competir com amadores sérios. O
progresso foi lento (e o esforço total de programação investido foi pequeno), mas contínuo, e o
paradigma de construir-e-testar prossegue num ciclo regular — toda a atividade de pesquisa
imitando, num nível macroscópico, o ciclo básico de gerar-e-testar de muitos dos programas de IA.

Há uma área que se amplia continuamente dentro da qual a ação inteligente é alcançável. A partir
das tarefas originais, a pesquisa se estendeu para construir sistemas que lidam com linguagem
natural e a compreendem de várias formas, sistemas para interpretar cenas visuais, sistemas para
coordenação olho-mão, sistemas que projetam, sistemas que escrevem programas de computador,
sistemas para compreensão de fala — a lista, se não infinita, é ao menos muito longa. Se existem
limites além dos quais a hipótese não nos levará, eles ainda não se tornaram aparentes.

Até o presente, o ritmo do progresso tem sido governado principalmente pela quantidade bastante
modesta de recursos científicos aplicados, e pela exigência inevitável de um esforço substancial de
construção de sistema para cada novo empreendimento importante. Claro que muito mais tem
acontecido do que simplesmente um empilhar de exemplos de sistemas inteligentes adaptados a
domínios específicos de tarefa. Seria surpreendente e pouco atraente se os programas de IA
realizando essas tarefas diversas não tivessem nada em comum além de serem instâncias de sistemas
de símbolos físicos. Por isso, houve grande interesse em buscar mecanismos dotados de generalidade,
e componentes comuns entre programas que realizam uma variedade de tarefas. Essa busca leva a
teoria além da hipótese inicial do sistema de símbolos, rumo a uma caracterização mais completa dos
tipos específicos de sistemas de símbolos que são eficazes em inteligência artificial. Na segunda
parte deste texto, discutiremos um exemplo de hipótese nesse segundo nível de especificidade: a
hipótese da busca heurística.

A busca por generalidade gerou uma série de programas projetados para separar mecanismos gerais de
resolução de problemas das exigências de domínios de tarefa específicos. O *General Problem Solver*
(GPS) foi talvez o primeiro deles; entre seus descendentes estão sistemas contemporâneos como o
PLANNER e o CONNIVER. A busca por componentes comuns levou a esquemas generalizados de
representação para objetivos e planos, métodos para construir redes de discriminação, procedimentos
para o controle de busca em árvore, mecanismos de casamento de padrões e sistemas de análise
sintática de linguagem. Experimentos estão em andamento para encontrar dispositivos convenientes
para representar sequências de tempo e tempo verbal, movimento, causalidade e coisas do gênero. Cada
vez mais, torna-se possível montar grandes sistemas inteligentes de forma modular a partir desses
componentes básicos.

**Modelagem do comportamento simbólico humano.** O comportamento do homem surge porque ele tem as
características de um sistema de símbolos físicos. Assim, os resultados dos esforços de modelar o
comportamento humano com sistemas de símbolos se tornam parte importante da evidência para a
hipótese, e a pesquisa em inteligência artificial avança em colaboração estreita com a pesquisa em
psicologia do processamento de informação, como costuma ser chamada.

A busca por explicações do comportamento inteligente do homem em termos de sistemas de símbolos
teve uma medida de sucesso ao longo dos últimos vinte anos, a ponto de a teoria do processamento de
informação ser hoje o ponto de vista dominante na psicologia cognitiva contemporânea. Especialmente
nas áreas de resolução de problemas, aquisição de conceitos e memória de longo prazo, modelos de
manipulação de símbolos hoje dominam a cena.

A pesquisa em psicologia do processamento de informação envolve dois tipos principais de atividade
empírica. O primeiro é a condução de observações e experimentos sobre o comportamento humano em
tarefas que exigem inteligência. O segundo, muito semelhante à atividade paralela em inteligência
artificial, é a programação de sistemas de símbolos para modelar o comportamento humano observado.
As observações e experimentos psicológicos levam à formulação de hipóteses sobre os processos
simbólicos que os sujeitos estão usando, e essas são uma fonte importante das ideias que entram na
construção dos programas. Assim, muitas das ideias para os mecanismos básicos do GPS derivaram da
análise cuidadosa dos protocolos que sujeitos humanos produziam ao pensar em voz alta durante a
realização de uma tarefa de resolução de problemas.

O caráter empírico da ciência da computação em nenhum lugar é mais evidente do que nessa aliança
com a psicologia. Não são apenas necessários experimentos psicológicos para testar a fidelidade dos
modelos de simulação como explicações do comportamento humano — dos experimentos também saem
ideias novas para o projeto e a construção de sistemas de símbolos físicos.

**Outra evidência.** O principal corpo de evidência para a hipótese do sistema de símbolos que
ainda não consideramos é evidência negativa: a ausência de hipóteses concorrentes específicas sobre
como a atividade inteligente poderia ser realizada — seja pelo homem, seja pela máquina. A maioria
das tentativas de construir tais hipóteses ocorreu dentro do campo da psicologia. Aqui tivemos um
continuum de teorias, desde os pontos de vista usualmente chamados de "behaviorismo" até os
usualmente chamados de "teoria da Gestalt". Nenhum desses pontos de vista se coloca como um
verdadeiro competidor da hipótese do sistema de símbolos, e isso por duas razões. Primeiro, nem o
behaviorismo nem a teoria da Gestalt demonstraram, ou sequer mostraram como demonstrar, que os
mecanismos explicativos que postulam bastam para dar conta do comportamento inteligente em tarefas
complexas. Segundo, nenhuma das duas teorias foi formulada com algo parecido com a especificidade
dos programas artificiais. Na verdade, as teorias alternativas são suficientemente vagas a ponto de
não ser muito difícil dar-lhes interpretações em termos de processamento de informação, e assim
assimilá-las à hipótese do sistema de símbolos.

Essa generalização, como a anterior, repousa sobre evidência empírica, e não foi derivada
formalmente de outras premissas. No entanto, veremos daqui a pouco que ela tem alguma conexão
lógica com a hipótese do sistema de símbolos, e talvez possamos esperar por uma formalização dessa
conexão em algum momento no futuro. Até que esse momento chegue, nossa história precisa
novamente ser de investigação empírica.

## II. Busca Heurística

Saber que os sistemas de símbolos físicos fornecem a matriz para a ação inteligente não nos diz
como eles a realizam. Nosso segundo exemplo de lei de estrutura qualitativa na ciência da
computação trata dessa segunda questão, afirmando que os sistemas de símbolos resolvem problemas
usando os processos de **busca heurística**.

### Resolução de problemas

Como a capacidade de resolver problemas costuma ser tomada como principal indicador de que um
sistema tem inteligência, é natural que boa parte da história da inteligência artificial esteja
tomada por tentativas de construir e compreender sistemas de resolução de problemas. A resolução de
problemas tem sido discutida por filósofos e psicólogos ao longo de dois milênios, em discursos
carregados de sentido de mistério. Se você acha que não há nada problemático ou misterioso num
sistema de símbolos resolver problemas, então você é filho de hoje, cujas visões se formaram desde
meados do século. Platão (e, segundo seu relato, Sócrates) tinha dificuldade para entender até
mesmo como problemas poderiam ser cogitados, quanto mais como poderiam ser resolvidos. Deixe-me
lembrá-los de como ele apresentou o enigma no *Mênon*:

> **Mênon:** E como você vai procurar, Sócrates, por algo que você não sabe o que é? Qual, dentre
> as coisas que você não conhece, você vai propor como objeto de sua busca? E, mesmo se por acaso
> topar com ela, como saberá que é essa a coisa que você não conhecia?

Para lidar com esse enigma, Platão inventou sua célebre teoria da reminiscência: quando você pensa
que está descobrindo ou aprendendo algo, está na verdade apenas recordando o que já sabia numa
existência anterior. Se essa explicação lhe parece absurda, há uma explicação muito mais simples
disponível hoje, baseada em nossa compreensão dos sistemas de símbolos. Uma formulação aproximada
dela é:

> Enunciar um problema é designar (1) um **teste** para uma classe de estruturas simbólicas
> (soluções do problema), e (2) um **gerador** de estruturas simbólicas (soluções potenciais).
> Resolver um problema é gerar uma estrutura, usando (2), que satisfaça o teste de (1).

Temos um problema se sabemos o que queremos fazer (o teste), e se não sabemos imediatamente como
fazê-lo (nosso gerador não produz de imediato uma estrutura simbólica que satisfaça o teste). Um
sistema de símbolos pode enunciar e resolver problemas (às vezes) porque pode gerar e testar.

Se isso é tudo o que há na resolução de problemas, por que não simplesmente gerar de uma vez uma
expressão que satisfaça o teste? É, de fato, o que fazemos quando desejamos e sonhamos. "Se desejos
fossem cavalos, mendigos poderiam cavalgar." Mas fora do mundo dos sonhos, isso não é possível.
Saber como testaríamos algo, uma vez construído, não significa que saibamos como construí-lo — que
tenhamos algum gerador para fazê-lo.

Por exemplo, é bem sabido o que significa "resolver" o problema de jogar xadrez de forma
vencedora. Existe um teste simples para reconhecer posições vencedoras: o teste de xeque-mate do
rei inimigo. No mundo dos sonhos, basta gerar uma estratégia que leve ao xeque-mate para todas as
contra-estratégias do adversário. Infelizmente, nenhum gerador que faça isso é conhecido pelos
sistemas de símbolos existentes (homem ou máquina). Em vez disso, boas jogadas de xadrez são
buscadas gerando várias alternativas e avaliando-as com esforço, usando medidas aproximadas, e
muitas vezes falhas, que supostamente indicam a probabilidade de uma determinada linha de jogo
estar a caminho de uma posição vencedora. Geradores de jogadas existem; geradores de jogadas
vencedoras, não.

Antes que possa haver um gerador de jogadas para um problema, é preciso que haja um **espaço de
problema**: um espaço de estruturas simbólicas nas quais as situações do problema, incluindo as
situações inicial e objetivo, possam ser representadas. Geradores de movimento são processos que
modificam uma situação no espaço de problema em outra. As características básicas dos sistemas de
símbolos físicos garantem que eles conseguem representar espaços de problema e que possuem
geradores de movimento. Como, em qualquer situação concreta, eles sintetizam um espaço de problema
e geradores de movimento apropriados a essa situação, é uma questão ainda muito presente na
fronteira da pesquisa em inteligência artificial.

A tarefa que se apresenta a um sistema de símbolos, então, quando ele recebe um problema e um
espaço de problema, é usar seus recursos limitados de processamento para gerar soluções possíveis,
uma após a outra, até encontrar uma que satisfaça o teste que define o problema. Se o sistema
tivesse algum controle sobre a ordem em que soluções potenciais fossem geradas, seria desejável
organizar essa ordem de geração de modo que as soluções reais tivessem alta probabilidade de
aparecer cedo. Um sistema de símbolos exibiria inteligência na medida em que conseguisse fazer
isso. A inteligência, para um sistema com recursos limitados de processamento, consiste em fazer
escolhas sábias sobre o que fazer a seguir.

### Busca na resolução de problemas

Durante a primeira década, mais ou menos, da pesquisa em inteligência artificial, o estudo da
resolução de problemas foi quase sinônimo do estudo dos processos de busca. A partir de nossa
caracterização de problemas e resolução de problemas, é fácil ver por que foi assim. Na verdade,
poder-se-ia perguntar se poderia ser diferente. Mas antes de tentar responder a essa pergunta,
precisamos explorar melhor a natureza dos processos de busca, tal como se revelou durante aquela
década de atividade.

**Extraindo informação do espaço de problema.** Considere um conjunto de estruturas simbólicas, das
quais um pequeno subconjunto são soluções de um dado problema. Suponha, ainda, que as soluções
estejam distribuídas aleatoriamente por todo o conjunto. Com isso queremos dizer que não existe
informação que permita a nenhum gerador de busca ter desempenho melhor que uma busca aleatória.
Nesse caso, nenhum sistema de símbolos poderia exibir mais inteligência (ou menos inteligência) do
que qualquer outro na resolução do problema — embora um pudesse ter mais sorte que outro.

Uma condição para o aparecimento da inteligência, portanto, é que a distribuição das soluções não
seja inteiramente aleatória, que o espaço de estruturas simbólicas exiba ao menos algum grau de
ordem e padrão. Uma segunda condição é que esse padrão, no espaço de estruturas simbólicas, seja
mais ou menos detectável. Uma terceira condição é que o gerador de soluções potenciais consiga se
comportar de forma diferencial, dependendo do padrão detectado.

Precisa haver informação no espaço de problema, e o sistema de símbolos precisa ser capaz de
extraí-la e usá-la. Vejamos primeiro um exemplo bem simples, em que a inteligência é fácil de
conseguir. Considere o problema de resolver uma equação algébrica simples:

> AX + B = CX + D

O teste define uma solução como qualquer expressão da forma X = E, tal que AE + B = CE + D. Agora,
poder-se-ia usar como gerador qualquer processo que produzisse números, os quais seriam então
testados por substituição na equação. Não chamaríamos isso de gerador inteligente.

Alternativamente, poder-se-ia usar geradores que aproveitassem o fato de que a equação original
pode ser modificada — somando ou subtraindo quantidades iguais de ambos os lados, ou multiplicando
ou dividindo ambos os lados pela mesma quantidade — sem mudar suas soluções. Mas, claro, podemos
obter ainda mais informação para guiar o gerador comparando a expressão original com a forma da
solução, e fazendo precisamente aquelas mudanças na equação que deixam sua solução inalterada, ao
mesmo tempo trazendo-a para a forma desejada. Um gerador desses poderia notar que havia um CX
indesejado no lado direito da equação original, subtraí-lo de ambos os lados e reunir os termos
novamente. Poderia então notar que havia um B indesejado no lado esquerdo, e subtraí-lo também. Por
fim, poderia se livrar do coeficiente indesejado (A − C) do lado esquerdo, dividindo. Assim, por
este procedimento — que já exibe considerável inteligência — o gerador produz estruturas simbólicas
sucessivas, cada uma obtida modificando a anterior, e as modificações visam a reduzir as diferenças
entre a forma da expressão de entrada e a forma da expressão de teste, mantendo, ao mesmo tempo, as
outras condições para uma solução.

Esse exemplo simples já ilustra muitos dos principais mecanismos usados pelos sistemas de símbolos
para a resolução inteligente de problemas. Primeiro, cada expressão sucessiva não é gerada de forma
independente, mas produzida modificando uma produzida anteriormente. Segundo, as modificações não
são aleatórias, mas dependem de dois tipos de informação. Dependem de informação constante ao longo
de toda essa classe de problemas de álgebra, e que está embutida na estrutura do gerador em si:
todas as modificações de expressões devem deixar inalterada a solução da equação. Dependem também
de diferenças de forma que permanecem entre a expressão corrente e a expressão desejada. Com
efeito, o gerador incorpora alguns dos testes que a solução precisa satisfazer, de modo que
expressões que não atendem a esses testes nunca serão geradas. Usar o primeiro tipo de informação
garante que apenas um pequeno subconjunto de todas as expressões possíveis é de fato gerado, sem
perder a expressão-solução desse subconjunto. Usar o segundo tipo de informação chega à solução
desejada por meio de uma sucessão de aproximações, empregando uma forma simples de **análise de
meios e fins** para dar direção à busca.

**Árvores de busca.** O problema algébrico simples pode parecer um exemplo incomum, até
patológico, de busca. Certamente não é busca por tentativa e erro, pois, embora tenha havido
algumas tentativas, não houve erro. Estamos mais acostumados a pensar na busca de resolução de
problemas como a geração de árvores de possibilidades de solução parcial, densamente ramificadas,
que podem crescer a milhares, ou até milhões, de ramos, antes de produzir uma solução. Assim, se, a
partir de cada expressão que produz, o gerador cria B novos ramos, a árvore crescerá como B^D, onde
D é sua profundidade. A árvore gerada para o problema de álgebra teve a peculiaridade de sua
ramificação, B, ser igual à unidade.

Programas que jogam xadrez, tipicamente, geram árvores de busca amplas, chegando, em alguns casos,
a um milhão de ramos ou mais. (Embora este exemplo sirva para ilustrar nossos pontos sobre busca em
árvore, deve-se notar que o propósito da busca em xadrez não é gerar soluções propostas, mas
avaliá-las — testá-las.) Uma linha de pesquisa sobre programas de jogo tem se dedicado, sobretudo, a
melhorar a representação do tabuleiro de xadrez, e os processos para fazer jogadas nele, de modo a
acelerar a busca e tornar possível buscar árvores maiores. A justificativa para essa direção, claro,
é que quanto mais profunda a busca dinâmica, mais precisas devem ser as avaliações no fim dela. Por
outro lado, há boa evidência empírica de que os jogadores humanos mais fortes, os grão-mestres,
raramente exploram árvores de mais de cem ramos. Essa economia é alcançada não tanto por buscar
menos profundamente do que fazem os programas de xadrez, mas por ramificar de forma muito esparsa e
seletiva em cada nó. Isso só é possível, sem causar deterioração das avaliações, tendo mais
seletividade embutida no próprio gerador, de modo que ele consegue selecionar para geração apenas
os ramos muito prováveis de fornecer informação relevante importante sobre a posição.

A conclusão, um tanto paradoxal na aparência, a que essa discussão leva é que a busca — a geração
sucessiva de estruturas de solução potenciais — é um aspecto fundamental do exercício de
inteligência de um sistema de símbolos na resolução de problemas, mas que a quantidade de busca
não é uma medida da quantidade de inteligência exibida. O que faz de um problema um problema não é
que uma grande quantidade de busca seja necessária para resolvê-lo, mas que uma grande quantidade
seria necessária se um determinado nível de inteligência não fosse aplicado. Quando o sistema
simbólico que está se empenhando em resolver um problema sabe o suficiente sobre o que fazer,
simplesmente segue direto rumo ao seu objetivo; mas sempre que seu conhecimento se torna
inadequado, quando ele entra em terra incógnita, se vê diante da ameaça de ter que passar por
grandes quantidades de busca antes de encontrar de novo o caminho.

O potencial para a explosão exponencial da árvore de busca, presente em todo esquema para gerar
soluções de problema, nos adverte contra depender da força bruta dos computadores — mesmo os
maiores e mais rápidos computadores — como compensação pela ignorância e falta de seletividade de
seus geradores. A esperança ainda se acende, periodicamente, em alguns peitos humanos, de que se
possa encontrar um computador suficientemente rápido, e programado com esperteza suficiente, para
jogar bom xadrez por busca de força bruta. Não há nada de conhecido, em teoria, sobre o jogo de
xadrez que descarte essa possibilidade. Estudos empíricos sobre o manejo de busca em árvores de
tamanho considerável, com resultados apenas modestos, tornam essa uma direção bem menos promissora
do que era quando o xadrez foi escolhido pela primeira vez como tarefa apropriada para a
inteligência artificial. Devemos considerar isso um dos achados empíricos importantes da pesquisa
com programas de xadrez.

**As formas da inteligência.** A tarefa da inteligência, então, é evitar a ameaça sempre presente
da explosão exponencial da busca. Como isso pode ser alcançado? Podem-se identificar três formas.

A primeira via, já ilustrada pelo exemplo da álgebra, e por programas de xadrez que só geram
jogadas "plausíveis" para análise posterior, é embutir seletividade no gerador: gerar apenas
estruturas que mostrem promessa de ser soluções, ou de estar no caminho rumo a soluções. A
consequência usual disso é diminuir a taxa de ramificação, não impedi-la inteiramente. A explosão
exponencial final não é evitada — salvo em situações excepcionalmente bem-estruturadas, como o
exemplo da álgebra — apenas adiada. Por isso, um sistema inteligente geralmente precisa
complementar a seletividade de seu gerador de soluções com outras técnicas de uso de informação
para guiar a busca. Vinte anos de experiência em manejar busca em árvore, numa variedade de
ambientes de tarefa, produziram um pequeno kit de técnicas gerais que hoje faz parte do
instrumental de todo pesquisador em inteligência artificial. Como essas técnicas já foram descritas
em obras gerais, como a de Nilsson [1971], podem ser resumidas aqui de forma bem breve.

Na busca heurística serial, a pergunta básica é sempre: o que fazer a seguir? Na busca em árvore,
essa pergunta, por sua vez, tem dois componentes: (1) a partir de qual nó da árvore devemos buscar
em seguida, e (2) em que direção devemos seguir a partir desse nó? Informação útil para responder à
primeira pergunta pode ser interpretada como medindo a distância relativa de diferentes nós até o
objetivo. A **busca pelo melhor primeiro** (*best-first search*) pede que se busque em seguida a
partir do nó que parece mais próximo do objetivo. Informação útil para responder à segunda pergunta
— em que direção buscar — é frequentemente obtida, como no exemplo de álgebra, detectando
diferenças específicas entre a estrutura do nó corrente descrita pelo teste de uma solução, e
selecionando ações relevantes para reduzir esses tipos particulares de diferença. Essa é a técnica
conhecida como **análise de meios e fins**, que desempenha papel central na estrutura do *General
Problem Solver*.

A importância dos estudos empíricos como fonte de ideias gerais na pesquisa em IA pode ser
demonstrada claramente traçando a história, ao longo de um grande número de programas de resolução
de problemas, dessas duas ideias centrais: busca pelo melhor primeiro e análise de meios e fins.
Rudimentos dessas duas já estavam presentes, embora sem nome, no *Logic Theorist* em 1955. O
*General Problem Solver*, incorporando a análise de meios e fins, apareceu por volta de 1957 — mas
combinou-a com busca em profundidade modificada, em vez de busca pelo melhor primeiro. Programas de
xadrez, em geral, ficaram atrelados, por razões de economia de memória, à busca em profundidade,
complementada, depois de cerca de 1958, pelo poderoso procedimento de poda alfa-beta. Cada uma
dessas técnicas parece ter sido reinventada várias vezes, e é difícil encontrar discussões teóricas
gerais, independentes de tarefa, sobre resolução de problemas em termos desses conceitos até meados
ou fins dos anos 1960. A quantidade de sustentação formal que receberam da teoria matemática ainda
é minúscula: alguns teoremas sobre a redução de busca que se pode obter usando a heurística
alfa-beta, um par de teoremas sobre busca de caminho mais curto (revisados por Nilsson [1971]), e
alguns teoremas recentes sobre busca pelo melhor primeiro com uma função de avaliação probabilística.

**Métodos "fracos" e "fortes".** As técnicas que temos discutido se dedicam ao controle da expansão
exponencial, e não à sua prevenção. Por essa razão, foram apropriadamente chamadas de "métodos
fracos" — métodos a serem usados quando o conhecimento do sistema de símbolos, ou a quantidade de
estrutura de fato contida no espaço de problema, é inadequada para permitir que a busca seja
evitada por completo. É instrutivo contrastar uma situação altamente estruturada, que pode ser
formulada, digamos, como um problema de programação linear, com as situações menos estruturadas de
problemas combinatórios, como o problema do caixeiro-viajante ou problemas de escalonamento.
("Menos estruturada", aqui, se refere à insuficiência ou inexistência de teoria relevante sobre a
estrutura do espaço de problema.) Na resolução de problemas de programação linear, pode ser
necessária uma quantidade substancial de computação, mas a busca não se ramifica. Todo passo é um
passo a caminho de uma solução. Na resolução de problemas combinatórios, ou na prova de teoremas, a
busca em árvore raramente pode ser evitada, e o sucesso depende de métodos de busca heurística do
tipo que temos descrito.

Nem todas as vertentes da pesquisa em resolução de problemas de IA seguiram o caminho que estamos
delineando. Um exemplo de um ponto um tanto diferente é fornecido pelo trabalho sobre sistemas de
prova de teoremas. Aqui, ideias importadas da matemática e da lógica tiveram forte influência na
direção da investigação. Por exemplo, o uso de heurísticas foi resistido enquanto propriedades de
completude não pudessem ser provadas (algo um tanto irônico, já que se sabe que a maioria dos
sistemas matemáticos interessantes é indecidível). Como a completude raramente pode ser provada
para heurísticas de busca pelo melhor primeiro, ou para muitos tipos de geradores seletivos, o
efeito dessa exigência foi bastante inibidor. Quando programas de prova de teoremas foram
continuamente incapacitados pela explosão combinatória de suas árvores de busca, começou-se a
pensar em heurísticas seletivas, que em muitos casos se revelaram análogas a heurísticas usadas em
programas gerais de resolução de problemas. A heurística do **conjunto de suporte** (*set of
support*), por exemplo, é uma forma de trabalhar de trás para frente, adaptada ao ambiente de prova
de teoremas por resolução.

**Um resumo da experiência.** Já descrevemos o funcionamento de nossa segunda lei de estrutura
qualitativa, que afirma que sistemas de símbolos físicos resolvem problemas por meio de busca
heurística. Além disso, examinamos algumas características subsidiárias da busca heurística, em
particular a ameaça, sempre presente, de explosão exponencial da árvore de busca, e alguns dos
meios que ela usa para evitar essa ameaça. As opiniões divergem quanto a quão eficaz a busca
heurística tem sido como mecanismo de resolução de problemas — as opiniões dependendo de quais
domínios de tarefa são considerados e de que critério de adequação é adotado. O sucesso pode ser
garantido fixando níveis de aspiração baixos — ou o fracasso, fixando-os altos. A evidência poderia
ser resumida mais ou menos assim: poucos programas resolvem problemas em nível "de especialista". O
programa de damas de Samuel e o DENDRAL de Feigenbaum e Lederberg são talvez as exceções mais
conhecidas, mas poder-se-ia apontar também para vários programas de busca heurística em domínios de
pesquisa operacional, como escalonamento e programação inteira. Em vários domínios, os programas
têm desempenho no nível de amadores competentes: xadrez, alguns domínios de prova de teoremas,
muitos tipos de jogos e quebra-cabeças. Níveis humanos ainda não foram nem de perto alcançados por
programas que têm um "front end" perceptual complexo: reconhecedores de cena visual,
compreendedores de fala, robôs que precisam manobrar em espaço e tempo reais. Ainda assim, progresso
impressionante foi feito, e um grande corpo de experiência foi reunido sobre essas tarefas difíceis.

Não temos explicações teóricas profundas para o padrão particular de desempenho que emergiu. Em
bases empíricas, no entanto, podemos tirar duas conclusões. Primeiro, a partir do que se aprendeu
sobre o desempenho de especialistas humanos em tarefas como o xadrez, é provável que qualquer
sistema capaz de igualar esse desempenho precise ter acesso, em suas memórias, a reservas muito
grandes de informação semântica. Segundo, parte da superioridade humana em tarefas com grande
componente perceptual pode ser atribuída à estrutura de processamento paralelo, especializada e
embutida, do olho e do ouvido humanos.

De qualquer forma, a qualidade do desempenho precisa necessariamente depender tanto das
características dos domínios de problema quanto dos sistemas de símbolos usados para enfrentá-los.
Para a maioria dos domínios da vida real que nos interessam, a estrutura do domínio não se mostrou
suficientemente simples para render (até agora) teoremas sobre complexidade, ou para nos dizer,
senão empiricamente, quão grandes são os problemas do mundo real em relação às capacidades de
nossos sistemas de símbolos para resolvê-los. Essa situação pode mudar, mas até que mude, precisamos
confiar em explorações empíricas, usando os melhores resolvedores de problemas que sabemos
construir, como fonte principal de conhecimento sobre a magnitude e as características da
dificuldade de um problema. Mesmo em áreas altamente estruturadas, como a programação linear, a
teoria tem sido muito mais útil para fortalecer as heurísticas subjacentes aos algoritmos de solução
mais poderosos do que para fornecer uma análise profunda de complexidade.

### Inteligência sem muita busca

Nossa análise da inteligência a equiparou à capacidade de extrair e usar informação sobre a
estrutura do espaço de problema, de modo a permitir que uma solução de problema seja gerada da
forma mais rápida e direta possível. Novas direções para melhorar as capacidades de resolução de
problemas dos sistemas de símbolos podem, então, ser equiparadas a novas formas de extrair e usar
informação. Ao menos três dessas formas podem ser identificadas.

**Uso não local da informação.** Primeiro, vários pesquisadores notaram que a informação reunida
ao longo do curso de uma busca em árvore costuma ser usada apenas localmente, para ajudar a tomar
decisões no nó específico onde a informação foi gerada. Informação sobre uma posição de xadrez,
obtida pela análise dinâmica de uma subárvore de continuações, costuma ser usada para avaliar
apenas aquela posição, não para avaliar outras posições que possam conter muitas das mesmas
características. Assim, os mesmos fatos precisam ser redescobertos repetidamente em diferentes nós
da árvore de busca. Simplesmente tirar a informação do contexto em que surgiu e usá-la de forma
geral não resolve o problema, pois a informação pode ser válida apenas numa faixa limitada de
contextos. Nos últimos anos, poucos esforços exploratórios foram feitos para transportar informação
de seu contexto de origem para outros contextos apropriados. Embora ainda seja cedo demais para
avaliar o poder dessa ideia, ou mesmo exatamente como ela deve ser alcançada, ela mostra promessa
considerável. Uma importante linha de investigação que Berliner [1975] tem perseguido é usar
análise causal para determinar o alcance dentro do qual uma determinada informação é válida. Assim,
se uma fraqueza numa posição de xadrez puder ser rastreada até a jogada que a causou, então a mesma
fraqueza pode ser esperada em outras posições descendentes daquela mesma jogada.

O sistema de compreensão de fala HEARSAY adotou outra abordagem para tornar a informação
disponível globalmente. Esse sistema busca reconhecer cadeias de fala perseguindo uma busca
paralela em vários níveis diferentes: fonêmico, lexical, sintático e semântico. À medida que cada
uma dessas buscas fornece e avalia hipóteses, ela repassa a informação que obteve a um "quadro
negro" comum, que pode ser lido por todas as fontes. Essa informação compartilhada pode ser usada,
por exemplo, para eliminar hipóteses, ou até classes inteiras de hipóteses, que de outra forma
teriam de ser buscadas por um dos processos. Assim, aumentar nossa capacidade de usar informação de
busca em árvore de forma não local oferece promessa para elevar a inteligência de sistemas de
resolução de problemas.

**Sistemas de reconhecimento semântico.** Uma segunda possibilidade ativa para elevar a
inteligência é fornecer ao sistema de símbolos um corpo rico de informação semântica sobre o
domínio de tarefa com o qual está lidando. Por exemplo, a pesquisa empírica sobre a habilidade de
mestres de xadrez mostra que uma fonte importante da habilidade do mestre é a informação
armazenada que lhe permite reconhecer um grande número de características específicas e padrões de
características num tabuleiro de xadrez, e informação que usa esse reconhecimento para propor ações
apropriadas às características reconhecidas. Essa ideia geral, claro, foi incorporada em programas
de xadrez quase desde o início. O que é novo é a percepção do número de tais padrões e da
informação associada que pode ser necessário armazenar para o jogo em nível de mestre — algo da
ordem de 50.000. A possibilidade de substituir busca por reconhecimento surge porque um padrão
particular, e especialmente um padrão raro, pode conter uma quantidade enorme de informação, desde
que esteja intimamente ligado à estrutura do espaço de problema. Quando essa estrutura é
"irregular", e não está sujeita a descrição matemática simples, então o conhecimento de um grande
número de padrões relevantes pode ser a chave para o comportamento inteligente. Se isso é assim em
qualquer domínio de tarefa particular é uma questão mais facilmente resolvida por investigação
empírica do que por teoria.

A discussão acima se refere especificamente à informação semântica associada a um sistema de
reconhecimento. Há, claro, também toda uma grande área de pesquisa em IA sobre processamento de
informação semântica e a organização de memórias semânticas que foge ao escopo dos tópicos que
discutimos neste texto. Nossa experiência com sistemas de símbolos ricamente dotados de informação
semântica e de capacidades de reconhecimento de padrões para acessá-la ainda é extremamente
limitada.

**Selecionando representações apropriadas.** Uma terceira linha de investigação se ocupa da
possibilidade de que a busca possa ser reduzida ou evitada pela seleção de um espaço de problema
apropriado. Um exemplo padrão que ilustra essa possibilidade de forma dramática é o problema do
**tabuleiro de damas mutilado**. Um tabuleiro de damas padrão, de 64 casas, pode ser coberto
exatamente com 32 peças, cada uma um retângulo 1×2 cobrindo exatamente duas casas. Suponha, agora,
que cortamos as casas em dois cantos diagonalmente opostos do tabuleiro, deixando um total de 62
casas. Esse tabuleiro mutilado pode ser coberto exatamente com 31 peças? Com paciência (literalmente)
celestial, a impossibilidade de conseguir tal cobertura pode ser demonstrada tentando todos os
arranjos possíveis. A alternativa, para quem tem menos paciência e mais inteligência, é observar que
os dois cantos diagonalmente opostos de um tabuleiro de damas são da mesma cor. Logo, o tabuleiro
mutilado tem duas casas a menos de uma cor do que da outra. Mas cada peça cobre uma casa de uma cor
e uma casa da outra, e qualquer conjunto de peças precisa cobrir o mesmo número de casas de cada
cor. Logo, não há solução. Como pode um sistema de símbolos descobrir esse argumento indutivo
simples, como alternativa a uma tentativa sem esperança de resolver o problema por busca entre
todas as coberturas possíveis? Concederíamos nota alta em inteligência a um sistema que encontrasse
essa solução.

Talvez, no entanto, ao formular esse problema, não estejamos escapando dos processos de busca.
Simplesmente deslocamos a busca de um espaço de soluções de problema possíveis para um espaço de
representações possíveis. Em todo caso, todo o processo de passar de uma representação a outra, e
de descobrir e avaliar representações, é território amplamente inexplorado no domínio da pesquisa
sobre resolução de problemas. As leis de estrutura qualitativa que governam representações ainda
estão por ser descobertas. É quase certo que a busca por elas receberá atenção considerável na
década que se aproxima.

## Conclusão

Esse é o nosso relato sobre sistemas de símbolos e inteligência. Foi um longo caminho, do *Mênon*
de Platão até o presente, mas talvez seja animador que a maior parte do progresso ao longo desse
caminho tenha ocorrido desde a virada do século vinte, e boa parte dele desde a metade do século. O
pensamento ainda era totalmente intangível e inefável até que a lógica formal moderna o
interpretasse como a manipulação de tokens formais. E ainda parecia habitar sobretudo o céu dos
ideais platônicos, ou os espaços igualmente obscuros da mente humana, até que os computadores nos
ensinaram como símbolos podiam ser processados por máquinas. A. M. Turing, a quem hoje de manhã
celebramos, deu suas grandes contribuições exatamente no cruzamento, em meados do século, desses
desenvolvimentos que levaram da lógica moderna ao computador.

**Sistemas de símbolos físicos.** O estudo da lógica e dos computadores nos revelou que a
inteligência reside em sistemas de símbolos físicos. Esta é a lei de estrutura qualitativa mais
básica da ciência da computação. Sistemas de símbolos são coleções de padrões e processos, sendo os
últimos capazes de produzir, destruir e modificar os primeiros. A propriedade mais importante dos
padrões é que eles podem designar objetos, processos ou outros padrões, e que, quando designam
processos, podem ser interpretados. Interpretar significa executar o processo designado. As duas
classes mais significativas de sistemas de símbolos com as quais estamos familiarizados são os
seres humanos e os computadores.

Nossa compreensão atual dos sistemas de símbolos cresceu, como indicado anteriormente, ao longo de
uma sequência de estágios. A lógica formal nos familiarizou com os símbolos, tratados
sintaticamente, como a matéria-prima do pensamento, e com a ideia de manipulá-los segundo processos
formais cuidadosamente definidos. A máquina de Turing tornou o processamento sintático de símbolos
verdadeiramente semelhante ao de uma máquina, e afirmou a universalidade potencial de sistemas de
símbolos estritamente definidos. O conceito de programa armazenado, para computadores, reafirmou a
interpretabilidade dos símbolos, já implícita na máquina de Turing. O processamento de listas trouxe
à tona as capacidades denotacionais dos símbolos, e definiu o processamento de símbolos de formas
que permitiram independência em relação à estrutura fixa da máquina física subjacente. Por volta de
1956, todos esses conceitos estavam disponíveis, junto com o hardware para implementá-los. O estudo
da inteligência dos sistemas de símbolos, o tema da inteligência artificial, podia começar.

**Busca heurística.** Uma segunda lei de estrutura qualitativa para a IA é que sistemas de símbolos
resolvem problemas gerando soluções potenciais e testando-as, isto é, buscando. Soluções costumam
ser buscadas criando expressões simbólicas e modificando-as sucessivamente até que satisfaçam as
condições de uma solução. Logo, sistemas de símbolos resolvem problemas por meio de busca. Como
possuem recursos finitos, a busca não pode ser realizada toda de uma vez, mas precisa ser
sequencial. Ela deixa para trás ou um único caminho, do ponto de partida ao objetivo, ou, se
correção e retrocesso forem necessários, uma árvore inteira de tais caminhos.

Sistemas de símbolos não podem parecer inteligentes quando cercados por puro caos. Eles exercem
inteligência extraindo informação de um domínio de problema e usando essa informação para guiar sua
busca, evitando desvios errados e caminhos tortuosos. O domínio de problema precisa conter
informação — algum grau de ordem e estrutura — para que o método funcione. O paradoxo do *Mênon* é
resolvido pela observação de que informação pode ser lembrada, mas nova informação também pode ser
extraída do domínio que os símbolos designam. Em ambos os casos, a fonte última da informação é o
domínio da tarefa.

**A base empírica.** A pesquisa em inteligência artificial se ocupa de como os sistemas de símbolos
precisam ser organizados para se comportar de forma inteligente. Vinte anos de trabalho na área
acumularam um corpo considerável de conhecimento, suficiente para preencher vários livros (e já
preencheu), a maior parte dele na forma de experiência bastante concreta sobre o comportamento de
classes específicas de sistemas de símbolos em domínios de tarefa específicos. Dessa experiência,
porém, também emergiram algumas generalizações, atravessando domínios de tarefa e sistemas, sobre
as características gerais da inteligência e seus métodos de implementação.

Tentamos enunciar algumas dessas generalizações nesta manhã. Elas são, em sua maioria,
qualitativas, e não matemáticas. Têm mais o sabor da geologia ou da biologia evolutiva do que o
sabor da física teórica. São suficientemente fortes para nos permitir, hoje, projetar e construir
sistemas moderadamente inteligentes para uma gama considerável de domínios de tarefa, bem como
obter uma compreensão bastante profunda de como a inteligência humana funciona em muitas situações.

**E agora?** Em nosso relato de hoje, mencionamos tanto questões em aberto quanto questões
resolvidas: há muitas de ambos os tipos. Não vemos nenhum arrefecimento da empolgação da
exploração que cercou este campo ao longo do último quarto de século. Dois limites de recursos vão
determinar o ritmo do progresso ao longo do próximo período semelhante. Um é a quantidade de poder
computacional que estará disponível. O segundo, e provavelmente o mais importante, é o número de
jovens cientistas da computação talentosos que serão atraídos para esta área de pesquisa como a
mais desafiadora que podem enfrentar.

A. M. Turing concluiu seu famoso artigo "Computing Machinery and Intelligence" com as palavras: "Só
conseguimos ver um pouco à frente, mas conseguimos ver bastante ali que precisa ser feito." Muitas
das coisas que Turing via em 1950 como necessárias já foram feitas, mas a agenda continua tão cheia
quanto sempre. Talvez estejamos lendo demais nessa simples afirmação acima, mas gostamos de pensar
que, nela, Turing reconheceu a verdade fundamental que todos os cientistas da computação conhecem
por instinto. Para todo sistema de símbolos físicos, condenado como estamos à busca serial do
ambiente de problema, a questão crítica é sempre: o que fazer a seguir?

---

## Referências

- BERLINER, H. [1975]. *Chess as problem solving: the development of a tactics analyzer.* Tese de
  doutorado, Computer Science Dept., Carnegie-Mellon University (não publicada).
- McCARTHY, J. [1960]. Recursive functions of symbolic expressions and their computation by
  machine. *Communications of the ACM*, v. 3, n. 4 (abr. 1960), p. 184–195.
- McCULLOCH, W. S. [1961]. What is a number, that a man may know it, and a man, that he may know a
  number. *General Semantics Bulletin*, n. 26–27 (1961), p. 7–18.
- NILSSON, N. J. [1971]. *Problem Solving Methods in Artificial Intelligence.* Nova York:
  McGraw-Hill.
- TURING, A. M. [1950]. Computing machinery and intelligence. *Mind*, v. 59 (out. 1950), p.
  433–460.

---

## Nota de tradução

Esta tradução foi feita com o cuidado de manter os termos técnicos já consolidados no restante da
disciplina: **sistema de símbolos físicos**, **designação**, **interpretação**, **busca
heurística**, **análise de meios e fins**, **espaço de problema**, **métodos fracos**. Onde o
original usa uma metáfora ou expressão coloquial em inglês (por exemplo, "if wishes were horses,
beggars might ride" — um provérbio inglês), optou-se por uma tradução literal com nota, em vez de
substituir por um provérbio equivalente em português, para preservar a voz dos autores. A citação
do *Mênon* de Platão foi vertida diretamente do inglês do artigo (que por sua vez é uma paráfrase
de Newell e Simon, não uma citação literal de uma tradução clássica do diálogo), mantendo o mesmo
grau de paráfrase do original.

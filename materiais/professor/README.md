# A tese do professor — resumo e leituras para TCC

**GIMÉNEZ-LUGO, Gustavo Alberto.** *Um modelo de sistemas multiagentes para partilha de
conhecimento utilizando redes sociais comunitárias.* Tese de Doutorado, Escola Politécnica da
Universidade de São Paulo, Departamento de Engenharia de Computação e Sistemas Digitais, 2004.
213 p. Orientador: **Jaime Simão Sichman**.
DOI: 10.11606/t.3.2004.tde-15112004-190053 — acesso aberto (gold).

Arquivos nesta pasta:

| Arquivo | O que é |
|---|---|
| `TESE_Gimenez-Lugo_2004.pdf` | a tese completa, 213 páginas |
| `tese-2004-ocr-introducao.txt` | Cap. 1 (Introdução) via OCR |
| `tese-2004-ocr-conclusoes.txt` | Cap. 6 (Conclusões e trabalhos futuros) via OCR |

> ⚠️ O PDF foi gerado com Ghostscript 5.50 e usa fontes bitmap (Type 3): **o texto não é
> selecionável nem pesquisável**. Os `.txt` acima vieram de OCR (tesseract, português) e podem
> conter erros de reconhecimento — confira contra o PDF antes de citar.

## O problema

Buscadores convencionais indexam uma fração da Web, e há conhecimento que ninguém publica
abertamente. Mas na vida real as pessoas não buscam só no Google: buscam no seu círculo de
conhecidos. E o quanto alguém compartilha depende do **tipo de relação** que tem com quem
pergunta.

A tese pergunta: como construir um agente computacional que leve isso em conta?

## A proposta

Um sistema multiagente aberto, arquitetura P2P, com um agente dedicado a cada usuário. Cada
agente carrega três representações acopladas:

1. **Ontologia** — a estruturação do conhecimento daquele usuário
2. **Rede social pessoal** — extraída automaticamente das mensagens de e-mail
3. **Visão organizacional subjetiva** — grupos e papéis sociais atribuídos aos contatos,
   formalizados pelo modelo organizacional **MOISE⁺** (Hübner, 2003)

A contribuição central: **conceitos da ontologia são anotados com informação organizacional**,
registrando em que situação social aquele conceito foi aprendido e usado. Isso permite ao agente
(a) rastrear quem usa quais conceitos e quando, (b) responder a pedidos considerando o **papel
social** de quem pede, e (c) modular privacidade por papel em vez de tudo-ou-nada.

Implementação experimental: o agente **COMMUNET**, testado com usuários reais.

## Estrutura

| | |
|---|---|
| 1 | Introdução — problema, objetivo, motivação, proposta, contribuições esperadas |
| **Parte I — Conceitos envolvidos** | |
| 2 | Acesso à informação: enfoques clássicos — recuperação de informação, categorização de textos |
| 3 | Acesso à informação: novos caminhos — agentes de informação, redes comunitárias, redes pessoais, P2P, organização e SMA, ontologias |
| **Parte II — Abordagem proposta** | |
| 4 | Agentes de informação para partilha de conhecimento — papéis sociais, ontologias com anotações organizacionais, arquitetura do agente |
| 5 | Tratamento experimental — o agente COMMUNET, condições, resultados, sociogramas conceituais |
| 6 | Conclusões e trabalhos futuros |
| Anexos | A: ações e categorias em sequências de busca · B: sociogramas conceituais · C: questionário |

## As perguntas que a tese se propõe a responder

Vale ver o formato: são **perguntas de projeto**, listadas na introdução e retomadas uma a uma na
conclusão. É um modelo de estruturação que funciona bem num TCC.

- Como construir uma representação da rede social do usuário que se aproxime da visão dele?
- Como relacionar a estruturação do conhecimento e a rede social de um usuário?
- Como usar as duas para localizar quem tem conhecimento num certo domínio?
- Como dar ao usuário mais controle sobre seus recursos, preservando privacidade sem inviabilizar
  a partilha P2P?
- Quais são as inovações do método?
- Como construir a ontologia de um usuário com o mínimo de intervenção dele? *(respondida
  parcialmente)*

## Trabalhos futuros — a mina para TCC

O §6.2 é literalmente uma lista de projetos que ele deixou em aberto. Propor algo daqui é chegar
com uma agenda que é dele:

- **Cooperação pró-ativa entre agentes** — quando um agente descobre que outro tem certo
  conhecimento, convidá-lo a formar/entrar num grupo e assumir um papel
- **Geração e transmissão de conceitos em redes sociais** — sob que condições e mecanismos
  conceitos surgem e se propagam em comunidades virtuais; permanências e rupturas entre grupos e
  culturas distintas
- **Influência dos papéis sociais na transmissão** — o efeito de tornar papéis explícitos do ponto
  de vista de quem recebe a informação; aderência entre representação explicitada e grupos
  vividos, em comunidades numerosas
- **Emergência de organizações** — há correlação entre acumulação de conhecimento específico e o
  surgimento de papéis e grupos?
- **Sistemas de reputação** — que condições organizacionais favorecem a acumulação de certos tipos
  de conhecimento; que variáveis ligam reputação e conhecimento
- **Medir conformidade de agentes a papéis** — que parâmetros associam um comportamento observado
  a um papel, e a viabilidade computacional disso

Ele fecha dizendo que qualquer desses caminhos pode ser tratado **com grupos reais ou em
simulação** — o que abre a porta para um TCC de escopo controlável.

## Trajetória de publicações — para saber onde ele está hoje

O tema não parou em 2004. A linha se manteve e se atualizou:

| Ano | Trabalho | Nota |
|---|---|---|
| 1998–99 | *Modelling an Extended/Virtual Enterprise by the Composition of Enterprise Models* (com T. Janowski); e outros sobre modelagem formal de empresas | fase pré-doutorado, semântica formal |
| 2003 | *Integrating knowledge centered MAS through organizational links* (com Jomi Fred Hübner), KIMAS/IEEE | núcleo da tese |
| 2005 | *Addressing the social components of knowledge to foster communitary exchanges*, Int. J. of Web Based Communities | desdobramento da tese |
| 2007 | *Intelligent Citizenship Assistants for Distributed Governance* (com Tacla e Hübner) | agentes, e-democracia, poder e cidadania |
| 2007 | *An Application Ontology for Furniture Packaging Design* (com Tacla) | ontologias aplicadas |
| 2013 | *Vertex Cover in Complex Networks*, Int. J. of Modern Physics C | redes complexas, aproximação e leis de potência |
| 2018 | *Interpretação de Imagens como Tarefa Cognitiva: uma Abordagem Inicial com Redes Neurais de Aprendizagem Profunda*, WESAAC | deep learning **dentro de** arcabouço cognitivo |
| 2022 | *Data Modeling with Ontological Formalism for Semantic Interoperability between Health Information Systems*, CLEI/IEEE | ontologias em saúde pública |
| 2024 | *Abordagens multiagentes para resiliência e reestabelecimento do fornecimento de energia elétrica*, WESAAC | SMA com dados reais da COPEL |
| **2026** | ***Padronização técnica em MLOps: mediação ética, autonomia profissional e governança sociotécnica***, WICS/SBC | **o mais recente** |

O de 2018 é revelador: usa deep learning, mas o argumento é sobre **os limites** dessas
abordagens e sobre como encaixá-las num arcabouço cognitivo. Não é entusiasmo com a ferramenta.

O de 2026 é o mais próximo do que ele fala em sala: argumenta que padronização técnica em MLOps
**não é neutra** — versionamento, CI/CD, monitoramento e automação de deploy materializam
valores (segurança, auditabilidade, responsabilização) e redistribuem autonomia profissional. A
análise é sobre repositórios públicos do GitHub. Se o TCC for por aí, é a agenda ativa dele.

Abertos e baixáveis (o proxy desta sessão bloqueia o sol.sbc.org.br, baixe pelo navegador):

- WESAAC 2018 — https://sol.sbc.org.br/index.php/wesaac/article/download/33277/33072
- WESAAC 2024 — https://sol.sbc.org.br/index.php/wesaac/article/download/33453/33248

## Se a ideia for pedir orientação

Três observações práticas:

1. **A tese é de 2004 e a Web mudou.** Propor "refazer o COMMUNET" é fraco. O que envelheceu bem
   é a *pergunta*: como um sistema representa relações sociais e modula o que compartilha em
   função delas. Isso hoje toca privacidade, federação, e governança de dados.
2. **Ele publica com estudantes em WESAAC e WICS**, ambos da SBC. Um TCC bem feito nessa linha
   tem destino natural de publicação, e isso costuma pesar na disposição de orientar.
3. **A linha viva hoje** parece ser a interseção de sistemas multiagentes, cognição e crítica
   sociotécnica — não SMA clássico puro. O paper de 2026 é o melhor indicador.

## Fontes

- Metadados e DOI via scite (`search_literature`, autor "Giménez-Lugo", 37 registros)
- PDF: http://www.teses.usp.br/teses/disponiveis/3/3141/tde-15112004-190053/publico/TESE_Gimenez-Lugo.pdf
- Conteúdo desta página: OCR próprio dos capítulos 1 e 6 + sumário

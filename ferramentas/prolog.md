# SWI-Prolog — para o bloco 3

Necessário para os exercícios e os dois planejadores (STRIPS e POP) em
`../materiais/03-representacao-e-planning/`. Vale instalar antes do encontro 4 (09/09).

## Instalação

**Windows, o caminho simples:** instalador oficial em https://www.swi-prolog.org/download/stable

**Docker**, se preferir não instalar nada na máquina — https://www.swi-prolog.org/Docker.html

```bash
docker run -it --rm -v "%cd%":/work -w /work swipl
```

Monta a pasta atual em `/work` e abre o interpretador. Útil para manter a máquina limpa, mas para
rodar meia dúzia de exercícios da disciplina o instalador nativo é menos atrito.

## Pacotes

A lista de add-ons está em https://www.swi-prolog.org/pack/list e se instala de dentro do
interpretador:

```prolog
?- pack_install(nome_do_pacote).
```

**Para esta disciplina não é necessário nenhum pacote.** Os planejadores do bloco 3 são Prolog
puro. Fica registrado como curiosidade.

## Primeiros passos

```prolog
?- consult('ex010-00-comida.pl').   % carrega um arquivo
?- listing.                          % mostra a base de conhecimento
?- halt.                             % sai
```

Os arquivos `LEIAME_Execucao1_STRIPS.txt` e `LEIAME_Execucao2_POP.txt` do bloco 3 trazem as
queries prontas com as saídas comentadas. Comece por `ex000-00-PrimeirosPassosEmPROLOG.txt`.

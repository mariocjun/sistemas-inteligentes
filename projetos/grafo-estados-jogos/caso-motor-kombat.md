# Caso completo: Motor Kombat (Mortal Kombat: Armageddon, SLUS-21410)

Objetivo: transformar a ISO num jogo dedicado ao minigame de kart — liga e
já está na seleção de pista. **Conseguido em 2026-09-01.**

CRC original: `104F08F4`. Base do ELF: `VA = offset_no_arquivo + 0xFFF00`.
ELF dentro da ISO no offset `0xE52800` (setor 7333).

## Endereços mapeados

```
push_state(estado)        FUN_00185d60   argumento no DELAY SLOT
pop_state()               FUN_00185d30
despacho(modo, handler)   FUN_001225d0   guarda o handler e cria o processo
pilha de estados          0x69f010       8 entradas de 4 bytes
índice do topo            0x64c40c
game_state                0x69f014       = pilha[1]
SLOT DO HANDLER ATIVO     0x64de88       <- ler isto diz qual tela roda
GP (global pointer)       0x6540f0
slot .mko da pista ativa  0x6600a0       nulo fora do kart
flag "pedido de init"     0x64e090       (gp-0x6060)
bloco de estado do kart   0x660088-0x660128
```

### Estados

```
 3  ATTRACT (luta demo em loop)
 6  GAME
 8  MENU principal
10  KRYPT
12  player profile
18  corrida do kart rodando
24  KONQUEST
26  SELEÇÃO do kart (pista + personagem)   <- o alvo
```

### Handlers (ponteiros de função de cada tela)

```
0x155250   menu principal
0x52bdd0   seleção do kart          <- o alvo
0x3f19d0   init da corrida do kart
0x18e100   sequência de abertura (memory card + vídeos)
0x245930   os filminhos
0x18db60   transição final antes do menu
```

### Funções de profile (todas fazem push_state(12))

```
FUN_00241870  ver profile      string "common/player_profile/pp_view_profile"
FUN_002420b0  criar profile    "common/player_profile/pp_create_profile"
FUN_00240d80  deletar profile  "common/player_profile/pp_delete_profile"
```
Registradas por `FUN_00155250` (o handler do menu principal).

## Os três patches aplicados

```
VA 0x155250 = 0814af74   j 0x52bdd0            (era addiu sp,sp,-0x40)
VA 0x155254 = 00000000   nop                   (era sd ra,0x20(sp))
VA 0x52be18 = 00000000   nop                   (era beql v0,zero,0x52beb0)
VA 0x122990 = 3c060053   lui a2,0x53           (era 3c060019)
VA 0x12299c = 24c6bdd0   addiu a2,a2,-0x4230   (era 24c6e100)
```

**1 e 2** — o handler do menu salta direto para o da seleção do kart.
Intercepta as 36 rotas que levavam ao menu de uma vez só. Bônus: tentar
"voltar ao menu" durante o jogo devolve para a seleção de pista, fechando
o loop de um jogo dedicado.

**3** — remove o `beql` que pulava a inicialização da tela quando a flag
`0x64e090` está zerada. Sem isso a tela aparecia por um instante e caía no
attract mode: o handler ia direto ao `push_state(26)` sem montar nada.

**4 e 5** — no boot, `entry` → `FUN_00122740` → cria o processo da abertura
com `FUN_0012dcc0(0x2001, 0x20, 0x18e100, 0, 0)`. Trocando `0x18e100` por
`0x52bdd0`, pula memory card e vídeos, indo direto à pista.

## Sequência de boot mapeada (por savestate em cada etapa)

```
entry (0x100008)
  -> FUN_00122740 (main)
       -> FUN_0012dcc0(..., 0x18e100)  sequência de abertura
            handler 0x245930  = filminhos
            handler 0x18db60  = transição (push_state(3) = attract)
       -> menu (0x155250)  ->  [PATCHEADO] seleção do kart
```

## Como o mecanismo do kart foi confirmado

`0x6600a0` guarda um ponteiro para o `.mko` da pista carregada. Validado em
quatro savestates:

```
Motortown  -> "kart_track_motortown.mko"
Jungle     -> "kart_track_jungle.mko"
Lin Kuei   -> "kart_track_linkuei.mko"     (a pista de gelo)
no menu    -> 0 (nulo)
```

O mecanismo de arena de luta documentado pelo projeto
[MKAHook](https://github.com/ermaccer/MKAHook) (slot `0x5A0B08`, struct
`mk_toc_entry`) **não é usado pelo kart** — fica travado em "pyramidtop"
mesmo dentro da corrida. O MKAHook foi útil para outra coisa: confirmou
`game_state = 0x69F014` e o enum de estados, e deu os hook points
`0x122A9C` (render) e `0x198B84` (menu init), que batem byte a byte.

## Limite conhecido

O botão "L1 = profile" continua aparecendo na tela de seleção. Varri
`0x52bb00-0x52c600` inteiro: não há `check_switch(_, 2)` (PAD_L1), nem
`jal` para as funções de profile, nem `push_state(12)`. O botão vem dos
**arquivos de recursos** da tela (`.sec`/`.mko` de layout), não do ELF.
Removê-lo exige mexer nos assets — outro tipo de trabalho.

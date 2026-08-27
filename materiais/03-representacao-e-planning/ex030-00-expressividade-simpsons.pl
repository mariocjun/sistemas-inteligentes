%% EXPRESSIVIDADE COM VARIAVEIS vs. SEM VARIAVEIS
%
%  Objetivo: estabelecer um paralelo entre expressividade
%  da logica de primeira-ordem e proposicional.
%  Tambem serve para introduzir posteriormente recursividade
%  em PROLOG
%
%  observe que:
%  1. variaveis iniciam com letra maiuscula
%  2. constantes iniciam com letra minuscula
%  3. predicados iniciam com letra minuscula
%
%

antepassado(abrahamSimpson, homerSimpson) :-
        progenitor(abrahamSimpson, homerSimpson).
antepassado(abrahamSimpson, bartSimpson) :-
	progenitor(abrahamSimpson, homerSimpson),
	progenitor(homerSimpson, bartSimpson).

progenitor(abrahamSimpson, homerSimpson).
progenitor(homerSimpson,  bartSimpson).
progenitor(homerSimpson,  lisaSimpson).
progenitor(homerSimpson,  maggieSimpson).
progenitor(margeSimpson,  bartSimpson).
progenitor(margeSimpson,  lisaSimpson).
progenitor(margeSimpson,  maggieSimpson).
progenitor(mrBouvier,     margeSimpson).
progenitor(jackieBouvier, margeSimpson).

masc(homerSimpson).
masc(bartSimpson).
masc(abrahamSimpson). %pai homer
masc(mrBouvier).      %pai da marge

fem(jackieBouvier).   %mae da marge
fem(penelopeSimpson). %mae homer
fem(maggieSimpson).   %filha
fem(lisaSimpson).     %filha
fem(margeSimpson).    %mae
fem(selmaBouvier).    %irma da marge
fem(pattyBouvier).    %irma da marge

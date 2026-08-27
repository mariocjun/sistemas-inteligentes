%% RECURSIVIDADE
%
%  A recursividade em PROLOG exige dois predicados:
%  a) um para expressar o caso base, para parar a recursão
%  b) um predicado que apresenta a recursão. Este predicado
%     deve vir apos o caso base.

antepassado(X, Y) :- progenitor(X, Y).
antepassado(X, Y) :- progenitor(X, Z), antepassado(Z, Y).

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

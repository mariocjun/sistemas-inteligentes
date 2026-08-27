% O objetivo deste exemplo eh mostrar como
% funciona substituicao e unificacao em
% PROLOG (principio da RESOLUCAO em logica).
%
% Fazer queries, porem, ligue o trace antes:
% ?- trace.
% [trace]?- neva(curitiba). <teclar c (de creep) para avancar>
% [trace]?- neva(Z).
%
% O aluno devera ser capaz de identificar quando ocorre
% substituicao, unificacao e backtracking. Devera observar
% que o modo de encadeamento eh para tras = backward chaining
%
chuvosa(curitiba).
chuvosa(joinville).
chuvosa(saoJoaquim).
chuvosa(urubici).
fria(curitiba).
muitaFria(saoJoaquim).
muitaFria(urubici).
neva(X) :- chuvosa(X), muitaFria(X).

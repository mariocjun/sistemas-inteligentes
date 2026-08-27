%% Operadores aritmeticos, recursividade e unificacao
%
%
% fatorial(3, Y) unifica com fatorial(X, Y), X=3, Y=Y
% .X1 is 2
% .fatorial(2, Y1) unifica com fatorial(X, Y), X=2, Y=Y1
% ..X1 is 1
% ..fatorial(1, Y1) unifica com fatorial(X, Y), X=1, Y=Y1
% ...X1 is 0
% ...fatorial(0, Y1) unifica com fatorial (0, 1), X=0, Y1=1
% ...Y is 1*1 =:= 1
% ..Y is 2*1 =:= 2
% .Y is 3*2 =:= 6
%
% %

fatorial(0,1).            %fato - caso base
fatorial(X, Y) :-
	X1 is X-1,
	fatorial(X1, Y1),
	Y is X*Y1.

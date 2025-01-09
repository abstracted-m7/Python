/*Prime Number*/
is_prime(2).
is_prime(3).
is_prime(N):-
    N>3,
    N mod 2 =\= 0,
    \+ factorCal(N,3).
factorCal(N,Factor):-
    N mod Factor =:=0.
factorCal(N,Factor):-
    Factor*Factor < N,
    NextFactor is Factor + 2,
    factorCal(N,NextFactor).
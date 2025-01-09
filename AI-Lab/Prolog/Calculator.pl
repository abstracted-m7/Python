/* calculate*/
sum(A,B):-
    C is A+B,
    write(C).

sub(A,B):-
    C is A-B,
    write(C).

multi(A,B):-
    C is A*B,
    write(C).

div(A,B):-
    C is A/B,
    write(C).
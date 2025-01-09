% Star Pattern
pattern(0).
pattern(N):-
    N > 0,
    print_pattern(1, N).

print_pattern(Current, N):-
    Current =< N,
    print_row(Current),
    nl,
    Next is Current + 1,
    print_pattern(Next,N).

print_pattern(Current, N):-
    Current > N.

print_row(0).
print_row(Col):-
    Col > 0,
    write("*"),
    NextCol is Col - 1,
    print_row(NextCol).

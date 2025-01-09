% Number Pattern
number_pattern(0).
number_pattern(N) :- 
    N > 0, 
    print_number_pattern(1, N).

print_number_pattern(Current, N) :- 
    Current =< N, 
    print_row(Current),
    nl,
    Next is Current + 1, 
    print_number_pattern(Next, N).

print_number_pattern(Current, N):-
    Current > N.

% Print numbers from 1 to Current
print_row(Current) :- 
    print_row(Current, 1).

% Helper predicate to print numbers from 1 to Current
print_row(Current, Current) :- 
    write(Current).
print_row(Current, Col) :- 
    Col < Current, 
    write(Col), 
    write(' '),
    NextCol is Col + 1,
    print_row(Current, NextCol).
/*
N netural numbers
UI: loop(5).
*/
loop(N):-
    write("Printing the numbers upto : "),
    write(N),
    nl,
    increment(1,N).
increment(Current, N):-
    Current =< N,
    write("The value : "),
    write(Current),
    nl,
    Next is Current + 1,
    increment(Next, N).
increment(Current, N):-
    Current > N.
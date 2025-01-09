/*
Max of three numbers
*/
max(A,B,C,Max):-
    (
    A >= B, A>= C->  Max = A;
    B >= A, B>=C ->  Max = B;
    C >= A, C>= B ->   Max = C
    ).
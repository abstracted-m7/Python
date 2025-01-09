/*
Palindrome
Note User input should be :is_palindrom([1, 2, 3, 4, 5, 2, 1]). <- for list
is_palindrom("maam"). <- For str
*/
%For List 
is_palindrome([]).
is_palindrome([_]).
is_palindrome(List):-
    reverse(List,List).
%For single number or word
check_palindrome(Str):-
    string_chars(Str, Chars),
    reverse(Chars, ReverseChars),
    Chars = ReverseChars.

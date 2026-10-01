% =====================================================================
% Task 2: Hello Prolog
% File: hello_prolog.pl
% =====================================================================
 
% Program that prints "Hello Prolog" to the console
hello :-
    write('Hello Prolog!'), nl.
 
% Alternative with formatting
hello_format :-
    format('Hello Prolog!~n').
 
% Greeting with name
greet(Name) :-
    format('Hello ~w!~n', [Name]).
 
% Multiple greetings
greet_multiple :-
    write('Hello'), nl,
    write('Prolog'), nl,
    write('Students!'), nl.

greet_two(Name1, Name2) :-
    format('Hello ~w and ~w!~n', [Name1, Name2]).
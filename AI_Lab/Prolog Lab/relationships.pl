% =====================================================================
% Task 3: Simple Relationships
% File: relationships.pl
% =====================================================================
 
% Facts about people and their relationships
% parent(Parent, Child)
parent(john, mary).
parent(john, peter).
parent(mary, david).
parent(mary, susan).
parent(peter, tom).
parent(peter, liz).
parent(susan, emma).
parent(susan, jack).

% Gender
male(john).
male(peter).
male(david).
male(tom).
male(jack).

female(mary).
female(susan).
female(liz).
female(emma).

% Rules for relationships
% Father
father(X, Y) :-
    male(X),
    parent(X, Y).
 
% Mother
mother(X, Y) :-
    female(X),
    parent(X, Y).
 
% Grandparent
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
 
% Sibling
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
 
% Brother
brother(X, Y) :-
    male(X),
    sibling(X, Y).
 
% Sister
sister(X, Y) :-
    female(X),
    sibling(X, Y).
 
% Child
child(X, Y) :-
    parent(Y, X).
 
% Son
son(X, Y) :-
    male(X),
    parent(Y, X).
 
% Daughter
daughter(X, Y) :-
    female(X),
    parent(Y, X).
 
% Ancestor (recursive)
ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
 
% Descendant (recursive)
descendant(X, Y) :-
    ancestor(Y, X).
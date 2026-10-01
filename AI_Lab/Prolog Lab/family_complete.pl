% =====================================================================
% Task 5: Complete Family Relationships
% File: family_complete.pl
% =====================================================================
 
% =====================================================================
% FACTS - Gender
% =====================================================================

 
male(jack).
male(oliver).
male(ali).
male(james).
male(simon).
male(harry).
male(tom).
male(bob).
male(jim).
 
female(helen).
female(sophie).
female(jess).
female(lily).
female(pam).
female(liz).
female(ann).
female(pat).
female(emma).
 
% =====================================================================
% FACTS - Parent relationships
% =====================================================================
 
parent(jack, jess).
parent(jack, lily).
parent(helen, jess).
parent(helen, lily).
parent(oliver, james).
parent(sophie, james).
parent(jess, simon).
parent(ali, simon).
parent(lily, harry).
parent(james, harry).
 
parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).
parent(simon, emma).

% =====================================================================
% RULES - Basic Relationships
% =====================================================================
 
% Father
father(X, Y) :-
    male(X),
    parent(X, Y).
 
% Mother
mother(X, Y) :-
    female(X),
    parent(X, Y).
 
% Grandfather
grandfather(X, Y) :-
    male(X),
    parent(X, Z),
    parent(Z, Y).
 
% Grandmother
grandmother(X, Y) :-
    female(X),
    parent(X, Z),
    parent(Z, Y).
 
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
 
% =====================================================================
% RULES - Extended Relationships
% =====================================================================
 
% Ancestor (recursive)
ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
 
% Descendant (recursive)
descendant(X, Y) :-
    ancestor(Y, X).
 
% Uncle
uncle(X, Y) :-
    male(X),
    parent(P, Y),
    sibling(X, P).
 
% Aunt
aunt(X, Y) :-
    female(X),
    parent(P, Y),
    sibling(X, P).
 
% Cousin
cousin(X, Y) :-
    parent(P, X),
    parent(Q, Y),
    sibling(P, Q),
    X \= Y.
 
% Great Grandparent
great_grandparent(X, Y) :-
    parent(X, Z),
    grandparent(Z, Y).
 
% Nephew
nephew(X, Y) :-
    male(X),
    parent(P, X),
    sibling(P, Y).
 
% Niece
niece(X, Y) :-
    female(X),
    parent(P, X),
    sibling(P, Y).
 
% Spouse (using parent relationships as proxy)
spouse(X, Y) :-
    parent(X, Z),
    parent(Y, Z),
    X \= Y.
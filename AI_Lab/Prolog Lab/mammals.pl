% =====================================================================
% Task 6:  Mammals and Warm-Blooded
% File:  mammals.pl
% =====================================================================
 
% =====================================================================
% FACTS - Mammals
% =====================================================================
 
mammal(cat).
mammal(dog).
mammal(whale).
mammal(elephant).
mammal(human).
mammal(squirrel).
mammal(rabbit).
mammal(lion).
mammal(tiger).
mammal(horse).
mammal(dolphin).
mammal(bat).
 
% =====================================================================
% FACTS - Animals (for extended testing)
% =====================================================================
 
animal(cat).
animal(dog).
animal(whale).
animal(elephant).
animal(human).
animal(squirrel).
animal(rabbit).
animal(lion).
animal(tiger).
animal(horse).
animal(shark).      % Fish, not a mammal
animal(eagle).      % Bird, not a mammal
animal(snake).      % Reptile, not a mammal
animal(dolphin).
animal(bat).

% =====================================================================
% RULE 1:  All mammals are warm-blooded
% =====================================================================
 
warm_blooded(X) :-
    mammal(X).
 
% =====================================================================
% RULE 2:  All animals are living things
% =====================================================================
 
living(X) :-
    animal(X).
 
% =====================================================================
% RULE 3:  All warm-blooded animals are warm-blooded
% =====================================================================
 
warm_blooded_animal(X) :-
    animal(X),
    warm_blooded(X).
 
% =====================================================================
% RULE 4:  All mammals are animals
% =====================================================================
 
animal(X) :-
    mammal(X).
 
% =====================================================================
% RULE 5:  All cats are mammals (implied by facts)
% =====================================================================
 
% The fact mammal(cat) already exists.
 
% =====================================================================
% RULE 6:  Cats are warm-blooded (deduced from rules)
% =====================================================================
 
cat_warm_blooded :-
    mammal(cat),
    warm_blooded(cat).
 
% =====================================================================
% RULE 7:  All warm-blooded creatures have blood
% =====================================================================
 
has_blood(X) :-
    warm_blooded(X).

has_hair(X) :-
    mammal(X).
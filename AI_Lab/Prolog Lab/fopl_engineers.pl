% =====================================================================
% Task 7: FOPL - Engineers and Coffee Drinkers
% File: fopl_engineers.pl
% =====================================================================
 
% =====================================================================
% FACTS
% =====================================================================
 
% Alice is a software developer
software_developer(alice).
 
% Alice drinks coffee
drinks_coffee(alice).
 
% Additional facts for testing
software_developer(bob).
drinks_coffee(carol).
engineer(david).

software_developer(charlie).
drinks_coffee(charlie).
engineer(frank).
software_developer(diana).
drinks_coffee(emma).

% =====================================================================
% RULE 1: All engineers are problem solvers
% =====================================================================
% for all x (Engineer(x) -> ProblemSolver(x))
 
problem_solver(X) :-
    engineer(X).
 
% =====================================================================
% RULE 2: All software developers are engineers
% =====================================================================
% for all x (SoftwareDeveloper(x) -> Engineer(x))
 
engineer(X) :-
    software_developer(X).
 
% =====================================================================
% RULE 3: All problem solvers are analytical thinkers
% =====================================================================
% for all x (ProblemSolver(x) -> AnalyticalThinker(x))
 
analytical_thinker(X) :-
    problem_solver(X).
 
% =====================================================================
% RULE 4: Everyone who drinks coffee is good at something
% =====================================================================
% for all x (DrinksCoffee(x) -> GoodAtSomething(x))
 
good_at_something(X) :-
    drinks_coffee(X).
 
% =====================================================================
% RULE 5: Alice is an analytical thinker (derived)
% =====================================================================
% Alice is a software developer -> engineer -> problem solver -> analytical thinker
 
alice_analytical_thinker :-
    analytical_thinker(alice).
 
% =====================================================================
% RULE 6: Alice is good at something (derived)
% =====================================================================
% Alice drinks coffee -> good at something
 
alice_good_at_something :-
    good_at_something(alice).
 
% =====================================================================
% RULE 7: Both properties combined
% =====================================================================
% Alice is an analytical thinker AND good at something
 
alice_proof :-
    analytical_thinker(alice),
    good_at_something(alice).
 
% =====================================================================
% ADDITIONAL RULES FOR TESTING
% =====================================================================
 
% Who is an engineer?
who_is_engineer(X) :-
    engineer(X).
 
% Who is a problem solver?
who_is_problem_solver(X) :-
    problem_solver(X).
 
% Who is an analytical thinker?
who_is_analytical_thinker(X) :-
    analytical_thinker(X).
 
% Who is good at something?
who_is_good_at_something(X) :-
    good_at_something(X).
 
% Who drinks coffee and is an engineer?
coffee_drinking_engineer(X) :-
    drinks_coffee(X),
    engineer(X).
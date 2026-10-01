% =====================================================================
% Task 4: Friendship Based on Common Interests
% File: friendship.pl
% =====================================================================
 
% Facts - People and their interests
likes(john, pizza).
likes(john, pasta).
likes(john, salad).
likes(mary, pizza).
likes(mary, salad).
likes(mary, ice_cream).
likes(peter, pizza).
likes(peter, pasta).
likes(susan, salad).
likes(susan, ice_cream).
likes(susan, pasta).
likes(david, pizza).
likes(david, burger).
likes(david, fries).

likes(emma, sushi).
likes(emma, pizza).
likes(emma, pasta).
likes(liam, sushi).
likes(liam, burger).
likes(liam, fries).

% Facts - People and their hobbies
hobby(john, reading).
hobby(john, swimming).
hobby(mary, painting).
hobby(mary, reading).
hobby(peter, swimming).
hobby(peter, running).
hobby(susan, painting).
hobby(susan, reading).
hobby(david, running).
hobby(david, swimming).
 
% Rule 1: Friends if they share at least one interest
friend(X, Y) :-
    likes(X, Z),
    likes(Y, Z),
    X \= Y.
 
% Rule 2: Best friends if they share at least two interests
best_friend(X, Y) :-
    likes(X, Z1),
    likes(Y, Z1),
    likes(X, Z2),
    likes(Y, Z2),
    Z1 \= Z2,
    X \= Y.
 
% Rule 3: Activity partners if they share a hobby
activity_partner(X, Y) :-
    hobby(X, H),
    hobby(Y, H),
    X \= Y.
 
% Rule 4: Close friends if they share interests AND hobbies
close_friend(X, Y) :-
    friend(X, Y),
    activity_partner(X, Y).
 
% Rule 5: Interests of a person
interests(Person, Interests) :-
    findall(Interest, likes(Person, Interest), Interests).
 
% Rule 6: Hobbies of a person
hobbies(Person, Hobbies) :-
    findall(Hobby, hobby(Person, Hobby), Hobbies).
 
% Rule 7: Common interests between two people
common_interests(X, Y, Interests) :-
    findall(Z, (likes(X, Z), likes(Y, Z)), Interests).
 
% Rule 8: Common hobbies between two people
common_hobbies(X, Y, Hobbies) :-
    findall(H, (hobby(X, H), hobby(Y, H)), Hobbies).
 
% Rule 9: Mutual friends
mutual_friend(X, Y, Z) :-
    friend(X, Z),
    friend(Y, Z).
 
% Rule 10: Suggestion for new friends
suggest_friend(Person, Suggested) :-
    likes(Person, Interest),
    likes(Suggested, Interest),
    Person \= Suggested,
    not(friend(Person, Suggested)).
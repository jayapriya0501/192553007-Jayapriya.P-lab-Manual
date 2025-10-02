% Facts
fact(has_feathers, bird).
fact(can_fly, bird).
fact(lays_eggs, bird).
fact(warm_blooded, mammal).
fact(has_fur, mammal).
fact(gives_milk, mammal).

% Rules for backward chaining
is_animal(X) :- is_bird(X).
is_animal(X) :- is_mammal(X).

is_bird(X) :- fact(has_feathers, X).
is_bird(X) :- fact(can_fly, X), fact(lays_eggs, X).

is_mammal(X) :- fact(warm_blooded, X), fact(has_fur, X).
is_mammal(X) :- fact(gives_milk, X).

% Specific animal facts
animal_fact(tweety, has_feathers).
animal_fact(tweety, can_fly).
animal_fact(dog, warm_blooded).
animal_fact(dog, has_fur).
animal_fact(cow, gives_milk).

% Backward chaining with trace
prove(Goal) :-
    write('Trying to prove: '), write(Goal), nl,
    prove_goal(Goal, 0).

prove_goal(fact(Property, Type), Depth) :-
    indent(Depth),
    write('Checking fact: '), write(fact(Property, Type)), nl,
    fact(Property, Type).

prove_goal(animal_fact(Animal, Property), Depth) :-
    indent(Depth),
    write('Checking animal fact: '), write(animal_fact(Animal, Property)), nl,
    animal_fact(Animal, Property).

prove_goal(Goal, Depth) :-
    clause(Goal, Body),
    indent(Depth),
    write('Using rule: '), write(Goal), write(' :- '), write(Body), nl,
    NewDepth is Depth + 1,
    prove_body(Body, NewDepth).

prove_body((Goal1, Goal2), Depth) :-
    prove_goal(Goal1, Depth),
    prove_goal(Goal2, Depth).

prove_body(Goal, Depth) :-
    prove_goal(Goal, Depth).

indent(0).
indent(N) :- N > 0, write('  '), N1 is N - 1, indent(N1).

% Query predicates
query_animal(Animal) :-
    write('=== Checking if '), write(Animal), write(' is an animal ==='), nl,
    (prove(is_animal(Animal)) ->
        write(Animal), write(' is an animal: YES') ;
        write(Animal), write(' is an animal: NO')), nl.

query_bird(Animal) :-
    write('=== Checking if '), write(Animal), write(' is a bird ==='), nl,
    (prove(is_bird(Animal)) ->
        write(Animal), write(' is a bird: YES') ;
        write(Animal), write(' is a bird: NO')), nl.

% Run queries
run_queries :-
    query_bird(tweety),
    query_animal(dog),
    query_animal(cow).
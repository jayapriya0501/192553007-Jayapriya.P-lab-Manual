% Facts
fact(sunny).
fact(warm).
fact(weekend).

% Rules for forward chaining
rule(go_beach) :- fact(sunny), fact(warm).
rule(go_picnic) :- fact(sunny), fact(weekend).
rule(stay_home) :- fact(rainy).
rule(wear_jacket) :- fact(cold).
rule(happy) :- rule(go_beach).
rule(happy) :- rule(go_picnic).

% Forward chaining implementation
forward_chain :-
    write('Starting forward chaining...'), nl,
    derive_new_facts,
    write('Forward chaining complete.'), nl.

derive_new_facts :-
    rule(Conclusion),
    \+ derived_fact(Conclusion),
    call(rule(Conclusion)),
    assertz(derived_fact(Conclusion)),
    write('Derived: '), write(Conclusion), nl,
    fail.
derive_new_facts.

% Query predicates
can_derive(Fact) :-
    derived_fact(Fact).

can_derive(Fact) :-
    rule(Fact),
    call(rule(Fact)).

% Example queries
query_all :-
    write('=== Forward Chaining Results ==='), nl,
    forward_chain,
    write('=== Derived Facts ==='), nl,
    derived_fact(X),
    write('- '), write(X), nl,
    fail.
query_all.

% Specific queries
query_beach :-
    (can_derive(go_beach) ->
        write('Can go to beach: YES') ;
        write('Can go to beach: NO')), nl.

query_happy :-
    (can_derive(happy) ->
        write('Will be happy: YES') ;
        write('Will be happy: NO')), nl.

% Run all queries
run_queries :-
    query_all,
    query_beach,
    query_happy.
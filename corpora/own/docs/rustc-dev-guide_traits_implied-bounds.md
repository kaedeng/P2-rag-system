# Implied bounds

Implied bounds

We currently add implied region bounds to avoid explicit annotations. e.g.
fn foo<'a, T>(x: &'a T) can freely assume that T: 'a holds without specifying it.

There are two kinds of implied bounds: explicit and implicit.
Explicit implied bounds get added to the fn clauses_of of the relevant item,
while implicit ones are handled, well... implicitly.

explicit implied bounds

The explicit implied bounds are computed in [fn inferred_outlives_of].
Only ADTs and CTAs have explicit implied bounds
which are computed via a fixpoint algorithm in the [fn inferred_outlives_crate] query.

We use [fn insert_required_clauses_to_be_wf] on all fields of all ADTs in the crate.
This function computes the outlives bounds for each component of the field using a
separate implementation.

For ADTs, trait objects, and associated types the initially required clauses are
computed in [fn check_explicit_clauses].
This simply uses fn explicit_clauses_of without elaborating them.

Region clauses are added via [fn insert_outlives_clause].
This function takes an outlives clause,
decomposes it, and adds the components as explicit clauses only
if the outlived region is a region parameter.
[It does not add 'static requirements][nostatic].

implicit implied bounds

As we are unable to handle implications in binders yet, we cannot simply add the outlives
requirements of impls and functions as explicit predicates.

using implicit implied bounds as assumptions

These bounds are not added to the ParamEnv of the affected item itself.
For lexical region resolution,
they are added using [fn OutlivesEnvironment::from_normalized_bounds].
Similarly, during MIR borrowck we add them using
[fn UniversalRegionRelationsBuilder::add_implied_bounds].

[We add implied bounds for the function signature and impl header in MIR borrowck][mir].
Outside of MIR borrowck we add the outlives requirements for the types returned by the
[fn assumed_wf_types] query.

The assumed outlives constraints for implicit bounds are computed using the
[fn implied_outlives_bounds] query.
This directly [extracts the required outlives bounds from fn wf::obligations][boundsfromty].

MIR borrowck adds the outlives constraints for both the normalized and unnormalized types,
lexical region resolution [only uses the unnormalized types][notnorm].

proving implicit implied bounds

As the implicit implied bounds are not included in fn clauses_of we have to
separately make sure they actually hold.
We generally handle this by checking that
all used types are well-formed by emitting WellFormed predicates.

We cannot emit WellFormed predicates when instantiating impls, as this would result
in - currently often inductive - trait solver cycles.
We also do not emit constraints involving higher ranked regions
as we're lacking the implied bounds from their binder.

This results in multiple unsoundnesses:
by using subtyping: [#25860]
by using super trait upcasting for a higher ranked trait bound: [#84591]
by being able to normalize a projection when using an impl while not being able
  to normalize it when checking the impl: [#100051]

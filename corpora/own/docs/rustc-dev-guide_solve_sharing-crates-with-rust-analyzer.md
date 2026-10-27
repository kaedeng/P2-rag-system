# Sharing the trait solver with rust-analyzer

Sharing the trait solver with rust-analyzer

rust-analyzer can be viewed as a compiler frontend: it performs tasks similar to the parts of rustc
that run before code generation, such as parsing, lexing, AST construction and lowering, HIR
lowering, and even limited MIR building and const evaluation.

However, because rust-analyzer is primarily a language server, its architecture differs in several
important ways from that of rustc.
Despite these differences, a substantial portion of its responsibilities—most notably type
inference and trait solving—overlap with the compiler.

To avoid duplication and to maintain consistency between the two implementations, rust-analyzer
reuses several crates from rustc, relying on shared abstractions wherever possible.

Shared Crates

Currently, rust-analyzer depends on several rustc_* crates from the compiler:

rustc_abi
rustc_ast_ir
rustc_index
rustc_lexer
rustc_next_trait_solver
rustc_parse_format
rustc_pattern_analysis
rustc_type_ir

Since these crates are not published on crates.io as part of the compiler's normal distribution
process, rust-analyzer maintains its own publishing pipeline.
It uses the [rustc-auto-publish script][rustc-auto-publish] to publish these crates to crates.io
with the prefix ra-ap-rustc_*
(for example: https://crates.io/crates/ra-ap-rustc_next_trait_solver).
rust-analyzer then depends on these re-published crates in its own build.

For trait solving specifically, the primary shared crates are rustc_type_ir and
rustc_next_trait_solver, which provide the core IR and solver logic used by both compiler
frontends.

The Abstraction Layer

Because rust-analyzer is a language server, it must handle frequently changing source code and
partially invalid or incomplete source codes.
This requires an infrastructure quite different from rustc's, especially in the layers between
the source code and the HIR—for example, Ty and its backing interner.

To bridge these differences, the compiler provides rustc_type_ir as an abstraction layer shared
between rustc and rust-analyzer.
This crate defines the fundamental interfaces used to represent types, predicates, and the context
required by the trait solver.
Both rustc and rust-analyzer implement these traits for their own concrete type representations,
and rustc_next_trait_solver is written to be generic over these abstractions.

In addition to these interfaces, rustc_type_ir also includes several non-trivial components built
on top of the abstraction layer—such as elaboration logic and the search graph machinery used by the
solver.

Design Concepts

rustc_next_trait_solver is intended to depend only on the abstract interfaces defined in
rustc_type_ir.
To support this, the type-system traits in rustc_type_ir must expose every interface the solver
requires—for example, [creating a new inference type variable][ir new_infer]
([rustc][rustc new_infer], [rust-analyzer][r-a new_infer]).
For items that do not need compiler-specific representations, rustc_type_ir defines them directly
as structs or enums parameterized over these traits—for example, [TraitRef][ir tr].

The following are some notable items from the rustc_type_ir crate.

trait Interner

The central trait in this design is [Interner][ir interner], which specifies all
implementation-specific details for both rustc and rust-analyzer.
Among its essential responsibilities:

it specifies the concrete types used by the implementation via its
  [associated types][ir interner assocs]; these form the backbone of how each compiler frontend
  instantiates the shared IR,
it provides the context required by the solver (e.g., querying [lang items][ir require_lang_item],
  enumerating [all blanket impls for a trait][ir for_each_blanket_impl]);
and it must implement [IrPrint][ir irprint] for formatting and tracing.

  In practice, these IrPrint impls simply route to existing formatting logic inside rustc or
  rust-analyzer.

In rustc, [TyCtxt implements Interner][rustc interner impl]: it exposes the rustc's query
methods, and the required Interner trait methods are implemented by invoking those queries.
In rust-analyzer, the implementing type is named [DbInterner][r-a interner impl] (as it performs
most interning through the [salsa] database), and most of its methods are backed by salsa queries
rather than rustc queries.

mod inherent

Another notable item in rustc_type_ir is the [inherent module][ir inherent].
This module provides forward definitions of inherent methods—expressed as traits—corresponding to
methods that exist on compiler-specific types such as Ty or GenericArg.

These definitions allow the generic crates (such as rustc_next_trait_solver) to call methods that
are implemented differently in rustc and rust-analyzer.

Code in generic crates should import these definitions with:

use inherent::*;

These forward definitions must never be used inside the concrete implementations themselves.
Crates that implement the traits from mod inherent should call the actual inherent methods on
their concrete types once those types are nameable.

You can find rustc’s implementations of these traits in the
[rustc_middle::ty::inherent][rustc inherent impl] module.
For rust-analyzer, the corresponding implementations are located across several modules under
hir_ty::next_solver, such as [hir_ty::next_solver::region][r-a inherent impl].

trait InferCtxtLike and trait SolverDelegate

These two traits correspond to the role of [InferCtxt][rustc inferctxt] in rustc.

[InferCtxtLike][ir inferctxtlike] must be defined in rustc_infer due to coherence
constraints (orphan rules).
As a result, it cannot provide functionality that lives in rustc_trait_selection.
Instead, behavior that depends on trait-solving logic is abstracted into a separate trait,
[SolverDelegate][ir solverdelegate].
Its implementator in rustc is [simply a newtype struct over InferCtxt][rustc solverdelegate impl]
in rustc_trait_selection.

(In rust-analyzer, it is also implemented for a newtype wrapper over its own
[InferCtxt][r-a inferctxtlike impl], primarily to mirror rustc’s structure, although this is not
strictly necessary because all solver-related logic already resides in the hir-ty crate.)

In the long term, the ideal design is to move all of the logic currently expressed through
SolverDelegate into rustc_next_trait_solver, with any required core operations added directly to
InferCtxtLike.
This would allow more of the solver’s behavior to live entirely inside the shared solver crate.

rustc_type_ir::search_graph::{Cx, Delegate}

The abstraction traits [Cx][ir searchgraph cx impl] and [Delegate][ir searchgraph delegate impl]
are already implemented within rustc_next_trait_solver itself.
Therefore, users of the shared crates—both rustc and rust-analyzer—do not need to provide their own
implementations.

These traits exist primarily to support fuzzing of the search graph independently of the full trait
solver.
This infrastructure is used by the external fuzzing project:
https://github.com/lcnr/search_graph_fuzz.

Derived Traits

[trait TypeVisitable and TypeVisitable_Generic][type-visitable-trait-macro]
[trait TypeFoldable and TypeFoldable_Generic][type-foldable-trait-macro]
[trait Lift and Lift_Generic][lift-trait-macro]
[trait GenericTypeVisitable][generictypevisitable]

These traits are used heavily in rustc_type_ir, their associated macros
primarily exist to reduce the amount of boilerplate otherwise required to implement Lift,
TypeFoldable, TypeVisitable and GenericTypeVisitable.

trait TypeVisitable and TypeVisitable_Generic

This trait requires a struct or enum implements the method visit_with(...),
which in turn will transfer control to TypeVisitor, this can be
[seen in detail here][rustc_typevisitable].

While ostensibly similar due to their names, TypeVisitable_Generic and
[GenericTypeVisitable][generictypevisitable] they implement two different visiting systems.

TypeVisitable_Generic means: derive the ordinary TypeVisitable trait
  generically over an Interner.
GenericTypeVisitable means: derive the separate GenericTypeVisitable trait
  used by non-nightly consumers such as rust-analyzer.

TypeVisitable_Generic

It visits the value's fields in declaration order, delegating each field to that
field's own TypeVisitable<I> implementation.
The traversal can stop early if the visitor returns a residual result.

Use #[type_visitable(ignore)] to ignore a field; it will not be part of the
traversal and will not need to implement TypeVisitable<I>.
This should only be used when the field does not need to be traversed.

trait TypeFoldable and TypeFoldable_Generic

The trait is implemented by things that need to embed types.
This concept is discussed in detail here and can be
[followed in the source][rustc_typefoldable].

TypeFoldable_Generic derives rustc_type_ir::TypeFoldable<I> for a struct or enum.

It consumes a value and reconstructs the same struct or enum variant after folding its fields.
It generates both fallible and infallible folding methods.

Use #[type_foldable(identity)] for a field whose value must be preserved unchanged.
The macro moves that field directly into the reconstructed value
instead of passing it to the folder.
Its type therefore does not need to implement TypeFoldable<I>.

For an enum, the generated match contains one reconstruction arm per variant.

trait Lift and Lift_Generic

The trait has a method lift_to_interner(...).
As the name suggests, it should 'lift' something to the interner.
See here to read more about the interner [and here for the source][rustc_lift].

The macro Lift_Generic derives Lift for a struct or enum, with three non-obvious considerations:

1. The generic parameters I and J are reserved for I: Interner and J
   being the interner it is being lifted to.
2. PhantomData is handled automatically, creating a new PhantomData.
   But it has to be used in the fully unqualified form -- you cannot use
   std::marker::PhantomData directly in the field.
3. The bounds are deliberately written as associated type bounds on the Interner
   trait rather than as where clauses on LiftInto.
   Given only I: LiftInto<J>,
   Rust can then treat bounds such as the following as implied:

I::Ty: Lift<J, Lifted = J::Ty>
I::Const: Lift<J, Lifted = J::Const>

This allows Lift_Generic to emit the bound I: LiftInto<J> while still
calling lift_to_interner on fields of type I::Ty, I::Const, and the other
declared associated types.
It also guarantees that each call produces the
destination field type expected after the derive rewrites I::Assoc to J::Assoc.

Without declare_lift_into!, the derive would need to generate a separate bound
for every interner-associated type used by every field.
If a new Interner associated type is expected to work with Lift_Generic, it needs an appropriate
Lift implementation and normally needs to be included in the declare_lift_into! invocation.

If you want to ignore a field, such as a primitive like a u32 which can't be
lifted you can skip the field with #[lift(ignore)].

trait GenericTypeVisitable

This a separate more general traversal trait purely used by rust-analyzer.
The visitor type is a parameter of the trait rather than a parameter of the method,
and visiting neither returns a result nor supports short-circuiting.

As such a struct or enum can derive both TypeVisitable_Generic and GenericTypeVisitable

There is intentionally no ignore attribute.
The traversal must visit every field.
This is a soundness requirement for rust-analyzer's use of the traversal
when tracing and garbage-collecting interned types.

Long-term plans for supporting rust-analyzer

In general, we aim to support rust-analyzer just as well as rustc in these shared crates—provided
doing so does not substantially harm rustc's performance or maintainability.
(e.g., [#145377][pr 145377], [#146111][pr 146111], [#146182][pr 146182] and [#147723][pr 147723])

Shared crates that require nightly-only features must guard such code behind a nightly feature
flag, since rust-analyzer is built with the stable toolchain.

Looking forward, we plan to uplift more shared logic into rustc_type_ir.
There are still duplicated implementations between rustc and rust-analyzer—such as ObligationCtxt
([rustc][rustc oblctxt], [rust-analyzer][r-a oblctxt]) and type coercion logic
([rustc][rustc coerce], [rust-analyzer][r-a coerce])—that we would like to unify over time.

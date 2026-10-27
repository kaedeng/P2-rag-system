# Glossary

Glossary

Term | Meaning
-----------------------------------------------|--------
1-ZST | A one-aligned zero-sized type. A type of size zero with an [alignment][size-align] of one.
abby | Short for assumptions on binders. Alternatively: a-bi, though this is very close to ABI.
arena, arena allocation | An arena is a large memory buffer from which other memory allocations are made. This style of allocation is called arena allocation. See this chapter for more info.
AFIDT | Short for async function in dyn Trait. See also AFIT.
AFIT | Short for async function in trait. They desugar to RPITITs.
AST | The abstract syntax tree (an IR) produced by the parser; reflects the surface / user syntax very closely.
APIT | Short for argument-position impl Trait. Also known as universial impl Trait (as opposed to existential) or anonymous type parameter. (see the reference).
ATPIT | Short for associated-type-position impl Trait. Also known as ITIAT.
binder | A binder is a place where a variable or type is declared; for example, the <T> is a binder for the type parameter T in fn foo<T>(..), for<'a> is a binder for the lifetime parameter 'a and \|a\| … is a binder for the parameter a. See the background chapter for more.
body | The definition of a function or constant that contains "executable code".
BodyId | An identifier that refers to a specific body in the crate. See the HIR chapter for more.
bound variable | A bound variable is one that is declared within an expression or term (in the general sense). For example, the variable a is bound within the closure expression \|a\| a * 2 and lifetime variable 'a is bound within the type expression for<'a> fn(&'a str) -> bool. See the background chapter for more
codegen | Short for code generation. The code to translate MIR into LLVM IR.
codegen unit | When we produce LLVM IR, we group the Rust code into a number of codegen units (sometimes abbreviated as CGUs). Each of these units is processed by LLVM independently from one another, enabling parallelism. They are also the unit of incremental re-use. (see more)
completeness | A technical term in type theory, it means that every type-safe program also type-checks. Having both soundness and completeness is very hard, and usually soundness is more important. (see "soundness").
control-flow graph, CFG | A representation of the control-flow of a program; see the background chapter for more
CTA | A checked type alias, a type alias that gets "properly" represented as an alias in the middle ty IR; contrary to (unchecked) type aliases whose reference sites get expanded to the underlying aliased type (the RHS of the type alias after instantiation) during HIR ty lowering, its reference sites get lowered to an [AliasTy].
CTFE | Short for compile-time function evaluation, this is the ability of the compiler to evaluate const fns at compile time. This is part of the compiler's constant evaluation system. (see more)
cx | We tend to use cx as an abbreviation for context. See also tcx, infcx, etc.
ctxt | We also use ctxt as an abbreviation for context, e.g. TyCtxt. See also cx or tcx.
DAG | A directed acyclic graph is used during compilation to keep track of dependencies between queries. (see more)
data-flow analysis | A static analysis that figures out what properties are true at each point in the control-flow of a program; see the background chapter for more.
de Bruijn index | A technique for describing which binder a variable is bound by using only integers. It has the benefit that it is invariant under variable renaming. (see more)
DefId | An index identifying a definition (see rustc_middle/src/hir/def_id.rs). Uniquely identifies a DefPath. See the HIR chapter for more.
discriminant | The underlying value associated with an enum variant or generator state to indicate it as "active" (but not to be confused with its "variant index"). At runtime, the discriminant of the active variant is encoded in the tag.
double pointer | A pointer with additional metadata. See fat pointer for more.
drop glue | (Internal) compiler-generated instructions that handle calling the destructors (Drop) for data types.
DST | Short for dynamically-sized type, this is a type for which the compiler cannot statically know the size in memory (e.g. str or [u8]). Such types don't implement Sized and cannot be allocated on the stack. They can only occur as the last field in a struct. They can only be used behind a pointer (e.g. &str or &[u8]).
early-bound lifetime | A lifetime / region that is substituted at its definition site. Bound in an item's Generics and substituted/instantiated using a GenericArgs. Contrast with late-bound lifetime. (see more)
effects | Right now only means const traits and ~const bounds. (see more)
empty type | See uninhabited type.
fat pointer | A two word value carrying the address of some value, along with some further information necessary to put the value to use. Rust includes two kinds of fat pointers: references to slices, and trait objects. A reference to a slice carries the starting address of the slice and its length. A trait object carries a value's address and a pointer to the trait's implementation appropriate to that value. "Fat pointers" are also known as "wide pointers", and "double pointers".
free variable | A free variable is one that is not bound within an expression or term (in the general sense); see the background chapter for more
GAC | A generic associated constant, an associated constant with (own) generic parameters or a where-clause. Part of feature [generic_const_items] (GCI).
GAT | A generic associated type, an associated type that has (own) generic parameters or a where-clause. Introduced in [RFC 1598].
generics | The list of generic parameters defined on an item. There are three kinds of generic parameters: Type, lifetime and const parameters.
HIR | The high-level IR, created by lowering / desugaring the AST. (see more)
HirId | Identifies a particular node in the HIR by combining a def-id with an "intra-definition offset". See the HIR chapter for more.
IAC | A (more often than not type-level) inherent associated constant, an associated constant in an inherent impl impl Type { … }. Often mentioned in the context of feature [min_generic_const_items] (mGCA, MGCA). An IGAC is an inherent GAC.
IAT | An inherent associated type, an associated type defined in an inherent impl impl Type { … }. An IGAT is an inherent GAT, a generic IAT.
ICE | Short for internal compiler error, this is when the compiler crashes.
ICH | Short for incremental compilation hash, these are used as fingerprints for things such as HIR and crate metadata, to check if changes have been made. This is useful in incremental compilation to see if part of a crate has changed and should be recompiled.
infcx | The type inference context (InferCtxt). (see rustc_middle::infer)
inference variable, infer var | When doing type, region, const inference, an inference variable is a kind of special type/region that represents what you are trying to infer. Think of X in algebra. For example, if we are trying to infer the type of a variable in a program, we create an inference variable to represent that unknown type.
intern | Interning refers to storing certain frequently-used constant data, such as strings, and then referring to the data by an identifier (e.g. a Symbol) rather than the data itself, to reduce memory usage and number of allocations. See this chapter for more info.
interpreter | The heart of const evaluation, running MIR code at compile time. (see more)
intrinsic | Intrinsics are special functions that are implemented in the compiler itself but exposed (often unstably) to users. They do magical and dangerous things. (See std::intrinsics)
IR | Short for intermediate representation, a general term in compilers. During compilation, the code is transformed from raw source (ASCII text) to various IRs. In Rust, these are primarily HIR, MIR, and LLVM IR. Each IR is well-suited for some set of computations. For example, MIR is well-suited for the borrow checker, and LLVM IR is well-suited for codegen because LLVM accepts it.
IRLO, irlo | Sometimes used as an abbreviation for internals.rust-lang.org.
item | A kind of "definition" in the language, such as a static, const, use statement, module, struct, etc. Concretely, this corresponds to the Item type.
item signature | The type signature / annotation / ascription of an item (e.g., struct, function). Often mentioned in the context of type inference since they are a place where we don't perform inference contrary to types in bodies.
ITIAT | Short for impl Trait in associated type. Also known as ATPIT.
lang item | Items that represent concepts intrinsic to the language itself, such as special built-in traits like Sync and Send; or traits representing operations such as Add; or functions that are called by the compiler. (see more)
late-bound lifetime | A lifetime / region that is substituted at its call site. Bound in a HRTB and substituted by specific functions in the compiler, such as liberate_late_bound_regions. Contrast with early-bound lifetime. (see more)
local crate | The crate currently being compiled. This is in contrast to "upstream crates" which refer to dependencies of the local crate.
lowering | The act of converting a higher-level IR to a lower-level one. E.g., AST lowering (from AST to HIR) or HIR ty lowering (from HIR to middle ty IR).
LTA 👎 | Short for lazy type alias. Renamed to CTA.
LTO | Short for link-time optimizations, this is a set of optimizations offered by LLVM that occur just before the final binary is linked. These include optimizations like removing functions that are never used in the final program, for example. ThinLTO is a variant of LTO that aims to be a bit more scalable and efficient, but possibly sacrifices some optimizations. You may also read issues in the Rust repo about "FatLTO", which is the loving nickname given to non-Thin LTO. LLVM documentation: [here][lto] and [here][thinlto].
[LLVM] | (actually not an acronym :P) an open-source compiler backend. It accepts LLVM IR and outputs native binaries. Various languages (e.g. Rust) can then implement a compiler front-end that outputs LLVM IR and use LLVM to compile to all the platforms LLVM supports.
memoization | The process of storing the results of (pure) computations (such as pure function calls) to avoid having to repeat them in the future. This is typically a trade-off between execution speed and memory usage.
middle ty IR | The collection of types defined in module [rustc_middle::ty] used by the type checker and the trait solver. They essentially form an IR.
MIR | The mid-level IR that is created after type-checking for use by borrowck and codegen. (see more)
Miri | A tool to detect Undefined Behavior in (unsafe) Rust code. (see more)
monomorphization | The process of taking generic implementations of types and functions and instantiating them with concrete types. For example, in the code we might have Vec<T>, but in the final executable, we will have a copy of the Vec code for every concrete type used in the program (e.g. a copy for Vec<usize>, a copy for Vec<MyStruct>, etc).
normalize | A general term for converting to a more canonical form, but in the case of rustc typically refers to associated type normalization.
newtype | A wrapper around some other type (e.g., struct Foo(T) is a "newtype" for T). This is commonly used in Rust to give a stronger type for indices.
niche | Invalid bit patterns for a type that can be used for layout optimizations. Some types cannot have certain bit patterns. For example, the NonZero* integers or the reference &T cannot be represented by a 0 bitstring. This means the compiler can perform layout optimizations by taking advantage of the invalid "niche value". An example application for this is the Discriminant elision on Option-like enums, which allows using a type's niche as the "tag" for an enum without requiring a separate field.
NLL | Short for non-lexical lifetimes, this is an extension to Rust's borrowing system to make it be based on the control-flow graph.
node-id or NodeId | An index identifying a particular node in the AST or HIR; gradually being phased out and replaced with HirId. See the HIR chapter for more.
obligation | Something that must be proven by the trait system. (see more)
placeholder | NOTE: skolemization is deprecated by placeholder a way of handling subtyping around "for-all" types (e.g., for<'a> fn(&'a u32)) as well as solving higher-ranked trait bounds (e.g., for<'a> T: Trait<'a>). See the chapter on placeholder and universes for more details.
point | Used in the NLL analysis to refer to some particular location in the MIR; typically used to refer to a node in the control-flow graph.
projection | A general term for a "relative path", e.g. x.f is a "field projection", and T::Item is an "associated type projection".
promoted constants | Constants extracted from a function and lifted to static scope; see this section for more details.
provider | The function that executes a query. (see more)
quantified | In math or logic, existential and universal quantification are used to ask questions like "is there any type T for which is true?" or "is this true for all types T?"; see the background chapter for more.
query | A sub-computation during compilation. Query results can be cached in the current session or to disk for incremental compilation. (see more)
recovery | Recovery refers to handling invalid syntax during parsing (e.g. a missing comma) and continuing to parse the AST. This avoid showing spurious errors to the user (e.g. showing 'missing field' errors when the struct definition contains errors).
region | Another term for "lifetime" often used in the literature and in the borrow checker.
rib | A data structure in the name resolver that keeps track of a single scope for names. (see more)
RPIT | Short for return-position impl Trait. An existential impl Trait (as opposed to universial) like TAITs and ATPIT. (see the reference).
RPITIT | Short for return-position impl Trait in trait. Unlike RPIT, this is desugared to a generic associated type (GAT). Introduced in [RFC 3425]. (see more)
rustbuild 👎 | A deprecated term for the part of bootstrap that is written in Rust
scrutinee | A scrutinee is the expression that is matched on in match expressions and similar pattern matching constructs. For example, in match x { A => 1, B => 2 }, the expression x is the scrutinee.
sess | The compiler session, which stores global data used throughout compilation
side tables | Because the AST and HIR are immutable once created, we often carry extra information about them in the form of hashtables, indexed by the id of a particular node.
sigil | Like a keyword but composed entirely of non-alphanumeric tokens. For example, & is a sigil for references.
soundness | A technical term in type theory. Roughly, if a type system is sound, then a program that type-checks is type-safe. That is, one can never (in safe rust) force a value into a variable of the wrong type. (see "completeness").
span | A location in the user's source code, used for error reporting primarily. These are like a file-name/line-number/column tuple on steroids: they carry a start/end point, and also track macro expansions and compiler desugaring. All while being packed into a few bytes (really, it's an index into a table). See the [Span] datatype for more.
subst 👎 | The act of substituting the generic parameters inside of a type, constant expression, etc. with concrete generic arguments by supplying substs. Nowadays referred to as instantiating in the compiler.
substs 👎 | The substitutions for a given generic item (e.g. the i32, u32 in HashMap<i32, u32>). Nowadays referred to as the list of generic arguments in the compiler (but note that strictly speaking these two concepts differ, see the literature).
sysroot | The directory for build artifacts that are loaded by the compiler at runtime. (see more)
tag | The "tag" of an enum/generator encodes the discriminant of the active variant/state. Tags can either be "direct" (simply storing the discriminant in a field) or use a "niche".
TAIT | Short for type-alias impl Trait. Introduced in [RFC 2515].
tcx | Standard variable name for the "typing context" (TyCtxt), main data structure of the compiler. (see more)
'tcx | The lifetime of the allocation arenas used by TyCtxt. Most data interned during a compilation session will use this lifetime with the exception of HIR data which uses the 'hir lifetime. (see more)
token | The smallest unit of parsing. Tokens are produced after lexing (see more).
[TLS] | Thread-local storage. Variables may be defined so that each thread has its own copy (rather than all threads sharing the variable). This has some interactions with LLVM. Not all platforms support TLS.
trait reference, trait ref | The name of a trait along with a suitable list of generic arguments. (see more)
trans 👎 | Short for translation, the code to translate MIR into LLVM IR. Renamed to codegen.
Ty | The internal representation of a type. (see more)
TyCtxt | The data structure often referred to as tcx in code which provides access to session data and the query system.
Type-Level Term | An expression at the type level, such as a Type or Const Generic.
UFCS 👎 | Short for universal function call syntax, this is an unambiguous syntax for calling a method. Term no longer in use! Prefer fully-qualified path / syntax. (see more, see the reference)
uninhabited type | A type which has no values. This is not the same as a ZST, which has exactly 1 value. An example of an uninhabited type is enum Foo {}, which has no variants, and so, can never be created. The compiler can treat code that deals with uninhabited types as dead code, since there is no such value to be manipulated. ! (the never type) is an uninhabited type. Uninhabited types are also called empty types.
upvar | A variable captured by a closure from outside the closure.
variance | Determines how changes to a generic parameter affect subtyping; for example, if T is a subtype of U, then Vec<T> is a subtype Vec<U> because Vec is covariant in its generic parameter. See the background chapter for a more general explanation. See the variance chapter for an explanation of how type checking handles variance.
variant index | In an enum, identifies a variant by assigning them indices starting at 0. This is purely internal and not to be confused with the "discriminant" which can be overwritten by the user (e.g. enum Bool { True = 42, False = 0 }).
well-formedness, wfness, wf | Semantically: An expression that evaluates to meaningful result. In type systems: A type related construct which follows rules of the type system.
wide pointer | A pointer with additional metadata. See fat pointer for more.
ZST | Zero-sized type. A type whose values have size 0 bytes. Since 2^0 = 1, such types can have exactly one value. For example, () (unit) is a ZST. struct Foo; is also a ZST. The compiler can do some nice optimizations around ZSTs.

See also https://doc.rust-lang.org/reference/glossary.html#glossary.

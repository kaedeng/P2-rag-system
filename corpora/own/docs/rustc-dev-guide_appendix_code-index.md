# Code Index

Code Index

rustc has a lot of important data structures.
This is an attempt to give some guidance on where to learn more
about some of the key data structures of the compiler.

Item | Kind | Short description | Chapter | Declaration
----------------|----------|-----------------------------|--------------------|-------------------
BodyId | struct | One of four types of HIR node identifiers | [Identifiers in the HIR] | compiler/rustc_hir/src/hir.rs
Compiler | struct | Represents a compiler session and can be used to drive a compilation. | [The Rustc Driver and Interface] | compiler/rustc_interface/src/interface.rs
ast::Crate | struct | A syntax-level representation of a parsed crate | [The parser] | compiler/rustc_ast/src/ast.rs
hir::Crate | struct | A more abstract, compiler-friendly form of a crate's AST | [The Hir] | compiler/rustc_middle/src/hir/mod.rs
DefId | struct | One of four types of HIR node identifiers | [Identifiers in the HIR] | compiler/rustc_hir/src/def_id.rs
Diag | struct | A struct for a compiler diagnostic, such as an error or lint | [Emitting Diagnostics] | compiler/rustc_errors/src/diagnostic.rs
DocContext | struct | A state container used by rustdoc when crawling through a crate to gather its documentation | [Rustdoc] | src/librustdoc/core.rs
HirId | struct | One of four types of HIR node identifiers | [Identifiers in the HIR] | compiler/rustc_hir_id/src/lib.rs
Lexer | struct | This is the lexer used during parsing. It consumes characters from the raw source code being compiled and produces a series of tokens for use by the rest of the parser | [The parser] | compiler/rustc_parse/src/lexer/mod.rs
NodeId | struct | One of four types of HIR node identifiers. Being phased out | [Identifiers in the HIR] | compiler/rustc_ast/src/ast.rs
ParamEnv | struct | Information about generic parameters or Self, useful for working with associated or generic items | [Parameter Environment] | compiler/rustc_middle/src/ty/mod.rs
ParseSess | struct | This struct contains information about a parsing session | [The parser] | compiler/rustc_session/src/parse/parse.rs
Rib | struct | Represents a single scope of names | [Name resolution] | compiler/rustc_resolve/src/lib.rs
Session | struct | The data associated with a compilation session | [The parser], [The Rustc Driver and Interface] | compiler/rustc_session/src/session.rs
SourceFile | struct | Part of the SourceMap. Maps AST nodes to their source code for a single source file. Was previously called FileMap | [The parser] | compiler/rustc_span/src/lib.rs
SourceMap | struct | Maps AST nodes to their source code. It is composed of SourceFiles. Was previously called CodeMap | [The parser] | compiler/rustc_span/src/source_map.rs
Span | struct | A location in the user's source code, used for error reporting primarily | [Emitting Diagnostics] | compiler/rustc_span/src/span_encoding.rs
TokenStream | struct | An abstract sequence of tokens, organized into TokenTrees | [The parser], [Macro expansion] | compiler/rustc_ast/src/tokenstream.rs
TraitDef | struct | This struct contains a trait's definition with type information | [The ty modules] | compiler/rustc_middle/src/ty/trait_def.rs
TraitRef | struct | The combination of a trait and its input types (e.g. P0: Trait<P1...Pn>) | [Trait Solving: Goals and Clauses] | compiler/rustc_middle/src/ty/sty.rs
Ty<'tcx> | struct | This is the internal representation of a type used for type checking | [Type checking] | compiler/rustc_middle/src/ty/mod.rs
TyCtxt<'tcx> | struct | The "typing context". This is the central data structure in the compiler. It is the context that you use to perform all manner of queries | [The ty modules] | compiler/rustc_middle/src/ty/context.rs

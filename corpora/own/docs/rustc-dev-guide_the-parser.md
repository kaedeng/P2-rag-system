# Lexing and parsing

Lexing and parsing

The very first thing the compiler does is take the program (in UTF-8 Unicode text)
and turn it into a data format the compiler can work with more conveniently than strings.
This happens in two stages: Lexing and Parsing.

  1. Lexing takes strings and turns them into streams of [tokens].
     For example, foo.bar + buz would be turned into the tokens foo, ., bar,
  +, and buz.
  This is implemented in [rustc_lexer][lexer].

  2. Parsing takes streams of tokens and turns them into a structured form
  which is easier for the compiler to work with, usually called an [*Abstract
  Syntax Tree* (AST)][ast].

The AST

The AST mirrors the structure of a Rust program in memory, using a Span to
link a particular AST node back to its source text.
The AST is defined in [rustc_ast][rustc_ast], along with some definitions for tokens and token
streams, data structures/traits for mutating ASTs, and shared definitions for
other AST-related parts of the compiler (like the lexer and macro-expansion).

Every node in the AST has its own [NodeId], including top-level items
such as structs, but also individual statements and expressions.
A [NodeId] is an identifier number that uniquely identifies an AST node within a crate.

However, because they are absolute within a crate, adding or removing a single
node in the AST causes all the subsequent [NodeId]s to change.
This renders [NodeId]s pretty much useless for incremental compilation, where you want as
few things as possible to change.

[NodeId]s are used in all the rustc bits that operate directly on the AST,
like macro expansion and name resolution (more on these over the next couple chapters).

Parsing

The parser is defined in [rustc_parse][rustc_parse], along with a
high-level interface to the lexer and some validation routines that run after macro expansion.
In particular, the [rustc_parse::parser][parser] contains the parser implementation.

The main entrypoint to the parser is via the various parse_* functions and others in
[rustc_parse][rustc_parse].
They let you do things like turn a [SourceFile][sourcefile]
(e.g. the source in a single file) into a token stream, create a parser from
the token stream, and then execute the parser to get a [Crate] (the root AST node).

To minimize the amount of copying that is done,
both [Lexer] and [Parser] have lifetimes which bind them to the parent [ParseSess].
This contains all the information needed while parsing, as well as the [SourceMap] itself.

Note that while parsing, we may encounter macro definitions or invocations.
We set these aside to be expanded (see Macro Expansion).
Expansion itself may require parsing the output of a macro, which may reveal more macros to be expanded, and so on.

More on lexical analysis

Code for lexical analysis is split between two crates:

[rustc_lexer] crate is responsible for breaking a &str into chunks constituting tokens.
  Although it is popular to implement lexers as generated finite state machines,
  the lexer in [rustc_lexer] is hand-written.

[Lexer] integrates [rustc_lexer] with data structures specific to rustc.
  Specifically,
  it adds Span information to tokens returned by [rustc_lexer] and interns identifiers.

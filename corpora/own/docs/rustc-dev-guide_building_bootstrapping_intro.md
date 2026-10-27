# Bootstrapping the compiler

Bootstrapping the compiler

[Bootstrapping] is the process of using a compiler to compile itself.
More accurately, it means using an older compiler to compile a newer version of the same compiler.

This raises a chicken-and-egg paradox: where did the first compiler come from?
It must have been written in a different language.
In Rust's case, it was [written in OCaml][ocaml-compiler].
However, it was abandoned long ago, and the
only way to build a modern version of rustc is with a slightly less modern version.

This is exactly how Rust's bootstrap build system works: it downloads the current beta release of
rustc, then uses it to compile the new compiler.

In this section, we give a high-level overview of
what Bootstrap does, followed by a high-level
introduction to how Bootstrap does it.

Additionally, see debugging bootstrap to learn about debugging methods.

# Command-line Arguments

Command-line Arguments

Command-line flags are documented in the [rustc book][cli-docs].
All stable flags should be documented there.
Unstable flags should be documented in the [unstable book].

See the [forge guide for new options] for details on the procedure for
adding a new command-line argument.

Guidelines

Flags should be orthogonal to each other.
  For example, if we'd have a json-emitting variant of multiple actions foo and bar,
  an additional --json flag is better than adding --foo-json and --bar-json.
Avoid flags with the no- prefix.
  Instead, use the [parse_bool] function,
  such as -C embed-bitcode=no.
Consider the behavior if the flag is passed multiple times.
  In some situations, the values should be accumulated (in order!).
  In other situations, subsequent flags should override previous flags (for example,
  the lint-level flags).
  And some flags (like -o) should generate an error
  if it is too ambiguous what multiple flags would mean.
Always give options a long descriptive name, if only for more understandable compiler scripts.
The --verbose flag is for adding verbose information to rustc output.
  For example,
  using it with the --version flag gives information about the hashes of the compiler code.
Experimental flags and options must be guarded behind the -Z unstable-options flag.

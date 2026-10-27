# Move paths

Move paths

In reality, it's not enough to track initialization at the granularity
of local variables. Rust also allows us to do moves and initialization
at the field granularity:

fn foo() {
    let a: (Vec<u32>, Vec<u32>) = (vec![22], vec![44]);

    // a.0 and a.1 are both initialized

    let b = a.0; // moves a.0

    // a.0 is not initialized, but a.1 still is

    let c = a.0; // ERROR
    let d = a.1; // OK
}

To handle this, we track initialization at the granularity of a **move
path**. A [MovePath] represents some location that the user can
initialize, move, etc. So e.g. there is a move-path representing the
local variable a, and there is a move-path representing a.0. Move
paths roughly correspond to the concept of a [Place] from MIR, but
they are indexed in ways that enable us to do move analysis more
efficiently.

Move path indices

Although there is a [MovePath] data structure, they are never referenced
directly. Instead, all the code passes around indices of type
[MovePathIndex]. If you need to get information about a move path, you use
this index with the [move_paths field of the MoveData][move_paths]. For
example, to convert a [MovePathIndex] mpi into a MIR [Place], you might
access the [MovePath::place] field like so:

move_data.move_paths[mpi].place

Building move paths

One of the first things we do in the MIR borrow check is to construct
the set of move paths. This is done as part of the
[MoveData::gather_moves] function. This function uses a MIR visitor
called [MoveDataBuilder] to walk the MIR and look at how each [Place]
within is accessed. For each such [Place], it constructs a
corresponding [MovePathIndex]. It also records when/where that
particular move path is moved/initialized, but we'll get to that in a
later section.

Illegal move paths

We don't actually create a move-path for every [Place] that gets
used. In particular, if it is illegal to move from a [Place], then
there is no need for a [MovePathIndex]. Some examples:

You cannot move an individual element of an array, so if we have e.g. foo: [String; 3],
  there would be no move-path for foo[1].
You cannot move from inside of a borrowed reference, so if we have e.g. foo: &String,
  there would be no move-path for *foo.

These rules are enforced by the [move_path_for] function, which
converts a [Place] into a [MovePathIndex] -- in error cases like
those just discussed, the function returns an Err. This in turn
means we don't have to bother tracking whether those places are
initialized (which lowers overhead).

Projections

Instead of using [PlaceElem], projections in move paths are stored as [MoveSubPath]s.
Projections that can't be moved out of and projections that can be skipped are not represented.

Subslice projections of arrays (produced by slice patterns) are special; they're turned into
multiple [ConstantIndex] subpaths, one for each element in the subslice.

Looking up a move-path

If you have a [Place] and you would like to convert it to a [MovePathIndex], you
can do that using the [MovePathLookup] structure found in the [rev_lookup] field
of [MoveData]. There are two different methods:

[find_local], which takes a [mir::Local] representing a local
  variable. This is the easier method, because we always create a
  [MovePathIndex] for every local variable.
[find], which takes an arbitrary [Place]. This method is a bit
  more annoying to use, precisely because we don't have a
  [MovePathIndex] for every [Place] (as we just discussed in
  the "illegal move paths" section). Therefore, [find] returns a
  [LookupResult] indicating the closest path it was able to find
  that exists (e.g., for foo[1], it might return just the path for
  foo).

Cross-references

As we noted above, move-paths are stored in a big vector and
referenced via their [MovePathIndex]. However, within this vector,
they are also structured into a tree. So for example if you have the
[MovePathIndex] for a.b.c, you can go to its parent move-path
a.b. You can also iterate over all children paths: so, from a.b,
you might iterate to find the path a.b.c (here you are iterating
just over the paths that are actually referenced in the source,
not all possible paths that could have been referenced). These
references are used for example in the
[find_in_move_path_or_its_descendants] function, which determines
whether a move-path (e.g., a.b) or any child of that move-path
(e.g.,a.b.c) matches a given predicate.

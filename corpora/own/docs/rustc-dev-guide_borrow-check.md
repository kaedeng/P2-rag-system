# MIR borrow check

MIR borrow check

The borrow check is Rust's "secret sauce" – it is tasked with enforcing a number of properties:

That all variables are initialized before they are used.
That you can't move the same value twice.
That you can't move a value while it is borrowed.
That you can't access a place while it is mutably borrowed (except through the reference).
That you can't mutate a place while it is immutably borrowed.
etc

The borrow checker operates on the MIR.
An older implementation operated on the HIR.
Doing borrow checking on MIR has several advantages:

The MIR is far less complex than the HIR; the radical desugaring
  helps prevent bugs in the borrow checker.
  (If you're curious, you can see
  [a list of bugs that the MIR-based borrow checker fixes here][47366].)
Even more importantly, using the MIR enables ["non-lexical lifetimes"][nll],
  which are regions derived from the control-flow graph.

Major phases of the borrow checker

The borrow checker source is found in [the rustc_borrowck crate][b_c].
The main entry point is the [mir_borrowck] query.

We first create a local copy of the MIR.
  In the coming steps,
  we will modify this copy in place to modify the types and things to
  include references to the new regions that we are computing.
We then invoke [replace_regions_in_mir] to modify our local MIR.
  Among other things, this function will replace all of the regions
  in the MIR with fresh inference variables.
Next, we perform a number of dataflow analyses that
  compute what data is moved and when.
We then do a second type check across the MIR:
  the purpose of this type check is to determine all of the constraints between different regions.
Next, we do region inference, which computes
  the values of each region — basically, the points in the control-flow graph where
  each lifetime must be valid according to the constraints we collected.
At this point, we can compute the "borrows in scope" at each point.
Finally, we do a second walk over the MIR, looking at the actions it does and reporting errors.
  For example, if we see a statement like *a + 1,
  we would check that the variable a is initialized and that it is not mutably borrowed,
  as either of those would require an error to be reported.
  Doing this check requires the results of all the previous analyses.

Debugging the borrow checker

See Debugging the borrow checker and MIR Debugging.

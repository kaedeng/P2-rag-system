# `wasm32v1-none`

wasm32v1-none

Tier: 2

The wasm32v1-none target is a WebAssembly compilation target that:

Imports nothing from its host environment
Enables no proposals / features past the [W3C WebAssembly Core 1.0 spec]

The target is very similar to wasm32-unknown-unknown and similarly uses LLVM's wasm32-unknown-unknown backend target. It contains only three minor differences:

Setting the target-cpu to mvp rather than the default generic. Requesting mvp disables all WebAssembly proposals / LLVM target feature flags.
Enabling the [Import/Export of Mutable Globals] proposal (i.e. the +mutable-globals LLVM target feature flag)
Not compiling the std library at all, rather than compiling it with stubs.

Target maintainers

@alexcrichton
@graydon

Requirements

This target is cross-compiled. It does not support std, only core and alloc. Since it imports nothing from its environment, any std parts that use OS facilities would be stubbed out with functions-that-fail anyways, and the experience of working with the stub std in the wasm32-unknown-unknown target was deemed not something worth repeating here.

Everything else about this target's requirements, building, usage and testing is the same as what's described in the wasm32-unknown-unknown document, just using the target string wasm32v1-none in place of wasm32-unknown-unknown.

Conditionally compiling code

It's recommended to conditionally compile code for this target with:

#[cfg(all(target_family = "wasm", target_os = "none"))]

Note that there is no way to tell via #[cfg] whether code will be running on
the web or not.

Enabled WebAssembly features

As noted above, no WebAssembly proposals past 1.0 are enabled on this target by default. Indeed, the entire point of this target is to have a way to compile for a stable "no post-1.0 proposals" subset of WebAssembly on stable Rust.

The [W3C WebAssembly Core 1.0 spec] was adopted as a W3C recommendation in December 2019, and includes exactly one "post-MVP" proposal: the [Import/Export of Mutable Globals] proposal.

All subsequent proposals are disabled on this target by default, though they can be individually enabled by passing LLVM target-feature flags.

For reference sake, the set of proposals that LLVM supports at the time of writing, that this target does not enable by default, are listed here along with their LLVM target-feature flags:

Post-1.0 proposals (integrated into the WebAssembly core 2.0 spec):
[Bulk memory] - +bulk-memory
[Sign-extending operations] - +sign-ext
[Non-trapping fp-to-int operations] - +nontrapping-fptoint
[Multi-value] - +multivalue
[Reference Types] - +reference-types
[Fixed-width SIMD] - +simd128
Post-2.0 proposals:
[Threads] (supported by atomics) - +atomics
[Exception handling] - +exception-handling
[Extended Constant Expressions] - +extended-const
[Half Precision] - +half-precision
[Multiple memories]- +multimemory
[Relaxed SIMD] - +relaxed-simd
[Tail call] - +tail-call
Post-3.0 proposals:
[Wide Arithmetic] - +wide-arithmetic

Additional proposals in the future are, of course, also not enabled by default.

Rationale relative to wasm32-unknown-unknown

As noted in the wasm32-unknown-unknown document, it is possible to compile with --target wasm32-unknown-unknown and disable all WebAssembly proposals "by hand", by passing -Ctarget-cpu=mvp. Furthermore one can enable proposals one by one by passing LLVM target feature flags, such as -Ctarget-feature=+mutable-globals.

Is it therefore reasonable to wonder what the difference is between building with this:

$ rustc --target wasm32-unknown-unknown -Ctarget-cpu=mvp -Ctarget-feature=+mutable-globals

and building with this:

$ rustc --target wasm32v1-none

The difference is in how the core and alloc crates are compiled for distribution with the toolchain, and whether it works on stable Rust toolchains or requires nightly ones. Again referring back to the wasm32-unknown-unknown document, note that to disable all post-MVP proposals on that target one actually has to compile with this:

$ export RUSTFLAGS="-Ctarget-cpu=mvp -Ctarget-feature=+mutable-globals"
$ cargo +nightly build -Zbuild-std=panic_abort,std --target wasm32-unknown-unknown

Which not only rebuilds std, core and alloc (which is somewhat costly and annoying) but more importantly requires the use of nightly Rust toolchains (for the -Zbuild-std flag). This is very undesirable for the target audience, which consists of people targeting WebAssembly implementations that prioritize stability, simplicity and/or security over feature support.

This wasm32v1-none target exists as an alternative option that works on stable Rust toolchains, without rebuilding the stdlib.

Unwinding

This target is compiled with -Cpanic=abort by default. Using -Cpanic=unwind
would require using the WebAssembly exception-handling proposal stabilized
mid-2025, and if that's desired then you most likely don't want to use this
target and instead want to use wasm32-unknown-unknown instead. It's unlikely
that this target will ever support unwinding with the precompiled artifacts
shipped through rustup. For documentation about using -Zbuild-std to enable
using -Cpanic=unwind see the documentation of
wasm32-unknown-unknown.

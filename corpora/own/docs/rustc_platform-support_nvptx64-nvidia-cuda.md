# `nvptx64-nvidia-cuda`

nvptx64-nvidia-cuda

Tier: 2

This is the target meant for deploying code for Nvidia® accelerators based on their CUDA
platform.

Target maintainers

@kjetilkjeka
@kulst

Requirements

This target is no_std, and uses the llvm-bitcode-linker by default. For PTX output, build with crate-type cdylib.
The necessary components for this workflow are:

rustup toolchain add nightly
rustup component add llvm-tools --toolchain nightly
rustup component add llvm-bitcode-linker --toolchain nightly

There are two options for using the core library:

rustup component add rust-src --toolchain nightly and build using -Z build-std=core.
rustup target add nvptx64-nvidia-cuda --toolchain nightly

Target and features

It is often beneficial to specify the target SM architecture, such as -C target-cpu=sm_89, because the default prioritizes broad compatibility rather than performance. Doing so also selects the PTX version as the maximum of (a) the oldest PTX version that supports the chosen target processor (see this table) and (b) the oldest PTX version supported by the Rust toolchain, which maximizes driver compatibility.
One can use -C target-feature=+ptx80 to choose a later PTX version without changing the target SM architecture (the default in this case, ptx78, requires CUDA driver version 11.8, while ptx80 would require driver version 12.0).
Later PTX versions may allow more efficient code generation.

For this target, the compiler enforces that all crates built into a binary use the same value for -C target-cpu. Therefore, if specifying a value different from the current default (sm_70), it is necessary to also build core manually with this value. This is possible by invoking cargo with -Z build-std=core using a nightly toolchain.
Although Rust follows LLVM in representing ptx* and sm_* as target features, they should also be thought of as having binary granularity. However, this is not enforced by the compiler. When building crates together, the same value for all crates should be set via -C target-feature.
While the compiler accepts #[target_feature(enable = "ptx80", enable = "sm_89")], it is not supported, may not behave as intended, and may become erroneous in the future.

Minimum SM and PTX support by Rust version
Support for old hardware architectures and PTX ISA versions is periodically dropped. This table shows the minimum supported versions per Rust version.

Rust | SM minimum | PTX ISA minimum

- 1.96 | 2.0 | 3.2
1.97 - TBD | 7.0 (Volta+) | 7.0 (CUDA 11+)

For a full overview of which GPUs support code built for a specific SM version, see the CUDA GPU Compute Capability documentation.

Building Rust kernels

A no_std crate containing one or more functions with extern "ptx-kernel" can be compiled to PTX using a command like the following.

$ RUSTFLAGS='-Ctarget-cpu=sm_89' cargo +nightly rustc --target=nvptx64-nvidia-cuda -Zbuild-std=core --crate-type=cdylib

Intrinsics in core::arch::nvptx may use #[cfg(target_feature = "...")], thus it's necessary to use -Zbuild-std=core with appropriate RUSTFLAGS. The following components are needed for this workflow:

$ rustup component add rust-src --toolchain nightly
$ rustup component add llvm-tools --toolchain nightly
$ rustup component add llvm-bitcode-linker --toolchain nightly

Target specific restrictions

The PTX instruction set architecture has special requirements regarding what is
and isn't allowed. In order to avoid producing invalid PTX or generating undefined
behavior by LLVM, some Rust language features are disallowed when compiling for this target.

Static initializers must be acyclic

A static's initializer must not form a cycle with itself or another static's
initializer. Therefore, the compiler will reject not only the self-referencing static A,
but all of the following statics.

struct Foo(&'static Foo);

static A: Foo = Foo(&A); //~ ERROR static initializer forms a cycle involving `A`

static B0: Foo = Foo(&B1); //~ ERROR static initializer forms a cycle involving `B0`
static B1: Foo = Foo(&B0);

static C0: Foo = Foo(&C1); //~ ERROR static initializer forms a cycle involving `C0`
static C1: Foo = Foo(&C2);
static C2: Foo = Foo(&C0);

Initializers that are acyclic are allowed:

struct Bar(&'static u32);

static BAR: Bar = Bar(&INT); // is allowed
static INT: u32 = 42u32; // also allowed

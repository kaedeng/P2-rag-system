# `*-unikraft-linux-musl`

*-unikraft-linux-musl

Tier: 3

Targets for the [Unikraft] Unikernel Development Kit (with musl).

Target triplets available so far:

x86_64-unikraft-linux-musl

Target maintainers

@mkroening

Requirements

These targets only support cross-compilation.
The targets do support std.

Unikraft pretends to behave exactly like Linux.
How much of that functionality is available depends on the individual unikernel configuration.
For example, the basic Unikraft + musl config does not support poll or networking out of the box.
That functionality requires enabling [LIBPOSIX_EVENT] or [lwIP] respectively.

The Unikraft targets follow Linux's extern "C" calling convention.

For these targets, rustc does not perform the final linking step.
Instead, the Unikraft build system will produce the final Unikernel image for the selected platform (e.g., KVM, Linux user space, and Xen).

Building the targets

You can build Rust with support for the targets by adding it to the target list in bootstrap.toml:

[build]
build-stage = 1
target = ["x86_64-unikraft-linux-musl"]

Building Rust programs

Rust does not yet ship pre-compiled artifacts for these targets.
To compile for these targets, you will either need to build Rust with the targets enabled
(see “Building the targets” above), or build your own copy of core by using build-std or similar.

Linking requires a [KraftKit] shim.
See [unikraft/kraftkit#612] for more information.

Testing

The targets do support running binaries in the form of unikernel images.
How the unikernel image is run depends on the specific platform (e.g., KVM, Linux user space, and Xen).
The targets do not support running the Rust test suite.

Cross-compilation toolchains and C code

The targets do support C code.
To build compatible C code, you have to use the same compiler and flags as does the Unikraft build system for your specific configuration.
The easiest way to achieve that, is to build the C code with the Unikraft build system when building your unikernel image.

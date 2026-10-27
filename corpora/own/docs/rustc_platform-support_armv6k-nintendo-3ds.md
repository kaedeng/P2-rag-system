# `armv6k-nintendo-3ds`

armv6k-nintendo-3ds

Tier: 3

The Nintendo 3DS platform, which has an Armv6k processor, and its associated
operating system (horizon).

Rust support for this target is not affiliated with Nintendo, and is not derived
from nor used with any official Nintendo SDK.

Target maintainers

This target is maintained by members of the @rust3ds
organization:

@Meziu
@AzureMarker
@ian-h-chamberlain

Requirements

This target is cross-compiled. Dynamic linking is not supported.

#![no_std] crates can be built using build-std to build core and optionally
alloc, and either panic_abort or panic_unwind.

std is partially supported, but mostly works. Some APIs are unimplemented
and will simply return an error, such as std::process. An allocator is provided
by default.

In order to support some APIs, binaries must be linked against libc written
for the target, using a linker for the target. These are provided by the
devkitARM toolchain. See
Cross-compilation toolchains and C code
for more details.

Additionally, some helper crates provide implementations of some libc functions
use by std that may otherwise be missing. These, or an alternate implementation
of the relevant functions, are required to use std:

pthread-3ds provides pthread APIs for std::thread.
shim-3ds fulfills some other missing libc APIs (e.g. getrandom).

Binaries built for this target should be compatible with all variants of the
3DS (and 2DS) hardware and firmware, but testing is limited and some versions may
not work correctly.

This target generates binaries in the ELF format.

Building the target

You can build Rust with support for the target by adding it to the target
list in bootstrap.toml and providing paths to the devkitARM toolchain.

[build]
build-stage = 1
target = ["armv6k-nintendo-3ds"]

[target.armv6k-nintendo-3ds]
cc = "/opt/devkitpro/devkitARM/bin/arm-none-eabi-gcc"
cxx = "/opt/devkitpro/devkitARM/bin/arm-none-eabi-g++"
ar = "/opt/devkitpro/devkitARM/bin/arm-none-eabi-ar"
ranlib = "/opt/devkitpro/devkitARM/bin/arm-none-eabi-ranlib"
linker = "/opt/devkitpro/devkitARM/bin/arm-none-eabi-gcc"

Also, to build compiler_builtins for the target, export these flags before
building the Rust toolchain:

export CFLAGS_armv6k_nintendo_3ds="-mfloat-abi=hard -mtune=mpcore -mtp=soft -march=armv6k"

Building Rust programs

Rust does not yet ship pre-compiled artifacts for this target.

The recommended way to build binaries is by using the
cargo-3ds tool, which uses build-std
and provides commands that work like the usual cargo run, cargo build, etc.
The cargo 3ds new will automatically set up a new project with the dependencies
needed to build a simple binary.

You can also build Rust with the target enabled (see
Building the target above).

As mentioned in Requirements, programs that use std must link
against both the devkitARM toolchain and libraries providing the libc APIs used
in std. There is a general-purpose utility crate for working with nonstandard
APIs provided by the OS: ctru-rs.
Add it to Cargo.toml to use it in your program:

[dependencies]
ctru-rs = { git = "https://github.com/rust3ds/ctru-rs.git" }

Depending on ctru-rs ensures that all the necessary symbols are available at
link time.

Testing

Binaries built for this target can be run in an emulator (most commonly
Citra), or sent to a device through
the use of a tool like devkitARM's 3dslink. They may also simply be copied
to an SD card to be inserted in the device.

The cargo-3ds tool mentioned in Building Rust programs
supports the use of 3dslink with cargo 3ds run. The default Rust test runner
is not supported, but
custom test frameworks
can be used with cargo 3ds test to run unit tests on a device.

The Rust test suite for library/std is not yet supported.

Cross-compilation toolchains and C code

C code can be built for this target using the
devkitARM toolchain.
This toolchain provides arm-none-eabi-gcc as the linker used to link Rust
programs as well.

The toolchain also provides a libc implementation, which is required by std
for many of its APIs, and a helper library libctru which is used by several
of the helper crates listed in Requirements.
This toolchain does not, however, include all of the APIs expected by std,
and the remaining APIs are implemented by pthread-3ds and linker-fix-3ds.

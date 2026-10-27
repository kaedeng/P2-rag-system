# `powerpc64-ibm-aix`

powerpc64-ibm-aix

Tier: 3

Rust for AIX operating system, currently only 64-bit PowerPC is supported.

Target maintainers

@daltenty
@gilamn5tr
@amy-kwan

Requirements

This target supports host tools, std and alloc. This target cannot be cross-compiled as for now, mainly because of the unavailability of system linker on other platforms.

Binary built for this target is expected to run on Power7 or newer CPU, and AIX 7.2 or newer version.

Binary format of this platform is XCOFF. Archive file format is 'AIX big format'.

Testing

This target supports running test suites natively, but it's not available to cross-compile and execute in emulator.

Interoperability with C code

This target supports C code. C code compiled by XL, Open XL and Clang are compatible with Rust. Typical triple of AIX on 64-bit PowerPC of these compilers are also powerpc64-ibm-aix.

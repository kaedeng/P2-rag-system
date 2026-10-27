# aarch64_be-unknown-linux-musl

aarch64_be-unknown-linux-musl

Tier: 3

ARM64 Linux (big-endian) with musl-libc.

Target maintainers

@neuschaefer
@Gelbpunkt

Requirements

The target requires a aarch64_be-*-linux-musl toolchain, which likely has to
be built from source because this is a rare combination. [Buildroot] provides
a way of doing so:

select Target options → Target Architecture → AArch64 (big endian)
select Toolchain → C library → musl
select Toolchain → Enable C++ support

Host tools are supported.

Building the target

The target can be enabled in bootstrap.toml:

[build]
target = ["aarch64_be-unknown-linux-musl"]

[target.aarch64_be-unknown-linux-musl]
cc = "/path/to/buildroot/host/bin/aarch64_be-buildroot-linux-musl-cc"
cxx = "/path/to/buildroot/host/bin/aarch64_be-buildroot-linux-musl-c++"
linker = "/path/to/buildroot/host/bin/aarch64_be-buildroot-linux-musl-cc"
ar = "/path/to/buildroot/host/bin/aarch64_be-buildroot-linux-musl-ar"
ranlib = "/path/to/buildroot/host/bin/aarch64_be-buildroot-linux-musl-ranlib"
musl-root = "/path/to/buildroot/staging"
runner = "qemu-aarch64_be -L /path/to/buildroot/target"
crt-static = "/path/to/buildroot/target"

Testing

Binaries can be run under qemu-aarch64_be or under a big-endian Linux kernel.

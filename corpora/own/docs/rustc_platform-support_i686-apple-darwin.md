# `i686-apple-darwin`

i686-apple-darwin

Apple macOS on 32-bit x86.

Target maintainers

@thomcc
@madsmtm

Requirements

See the docs on *-apple-darwin for general macOS requirements.

Building the target

You'll need the macOS 10.13 SDK shipped with Xcode 9. The location of the SDK
can be passed to rustc using the common SDKROOT environment variable.

Once you have that, you can build Rust with support for the target by adding
it to the target list in bootstrap.toml:

[build]
target = ["i686-apple-darwin"]

Using the unstable -Zbuild-std with a nightly Cargo may also work.

Building Rust programs

Rust [no longer] ships pre-compiled artifacts for this target. To compile for
this target, you will either need to build Rust with the target enabled (see
"Building the target" above), or build your own copy using build-std or
similar.

Testing

Running this target requires an Intel Macbook running macOS 10.14 or earlier,
as later versions removed support for running 32-bit binaries.

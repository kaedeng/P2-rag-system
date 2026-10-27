# *-linux-android and *-linux-androideabi

*-linux-android and *-linux-androideabi

Tier: 2

[Android] is a mobile operating system built on top of the Linux kernel.

Target maintainers

@chriswailes
@jfgoog
@maurer
@pirama-arumuga-nainar

Requirements

This target is cross-compiled from a host environment. Development may be done
from the [source tree] or using the Android NDK.

Android targets support std. Generated binaries use the ELF file format.

NDK/API Update Policy

Rust will support the most recent Long Term Support (LTS) [Android Native
Development Kit (NDK)][NDK]. By default Rust will support all [API levels supported
by the NDK][API-levels], but a higher minimum API level may be required if deemed necessary.

Building the target

To build Rust binaries for Android you'll need a copy of the most recent LTS
edition of the [Android NDK]. Supported Android targets are:

aarch64-linux-android
arm-linux-androideabi
armv7-linux-androideabi
i686-linux-android
thumbv7neon-linux-androideabi
x86_64-linux-android

The riscv64-linux-android target is supported as a Tier 3 target.

A list of all supported targets can be found
here

Architecture Notes

riscv64-linux-android

Currently the riscv64-linux-android target requires the following architecture features/extensions:

a (atomics)
d (double-precision floating-point)
c (compressed instruction set)
f (single-precision floating-point)
m (multiplication and division)
v (vector)
Zba (address calculation instructions)
Zbb (base instructions)
Zbs (single-bit instructions)

aarch64-linux-android on Nightly compilers

As soon as -Zfixed-x18 compiler flag is supplied, the ShadowCallStack sanitizer
instrumentation is also made available by supplying the second compiler flag -Zsanitizer=shadow-call-stack.

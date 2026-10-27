# `armebv7r-none-eabi` and `armebv7r-none-eabihf`

armebv7r-none-eabi and armebv7r-none-eabihf

Tier: 3
Library Support: core and alloc (bare-metal, #![no_std])

Bare-metal target for CPUs in the Armv7-R architecture family running in Big
Endian mode. These processors support dual ARM/Thumb mode, with ARM mode as
the default.

NOTE: You should almost always prefer the little-endian
versions of these target. Big Endian Arm systems are
highly unusual.

Processors in this family include the [Arm Cortex-R4, 5, 7, and 8][cortex-r].

See arm-none-eabi for information applicable to all
arm-none-eabi targets.

Target maintainers

@chrisnc

Requirements

Note that some variants of the Cortex-R have both big-endian instructions and
data. This configuration is known as BE-32, while data-only big-endianness is
known as BE-8. To build programs for BE-32 processors, the GNU linker must be
used with the -mbe32 option. See [ARM Cortex-R Series Programmer's Guide:
Endianness][endianness] for more details about different endian modes.

When using the hardfloat targets, the minimum floating-point features assumed
are those of the vfpv3-d16, which includes single- and double-precision, with
16 double-precision registers. This floating-point unit appears in Cortex-R4F
and Cortex-R5F processors. See [VFP in the Cortex-R processors][vfp]
for more details on the possible FPU variants.

If your processor supports a different set of floating-point features than the
default expectations of vfpv3-d16, then these should also be enabled or
disabled as needed with -C target-feature=(+/-).

Start-up and Low-Level Code

The [Rust Embedded Devices Working Group Arm Team] maintain the [aarch32-cpu]
and [aarch32-rt] crates, which may be useful for writing bare-metal code
using this target. Those crates include several examples which run in QEMU and
build using these targets.

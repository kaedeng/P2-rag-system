# `thumbv7m-none-eabi`

thumbv7m-none-eabi

Tier: 2
Library Support: core and alloc (bare-metal, #![no_std])

Bare-metal target for CPUs in the [Armv7-M] architecture family, supporting a
subset of the [T32 ISA][t32-isa].

Processors in this family include the:

[Arm Cortex-M3][cortex-m3]

See arm-none-eabi for information applicable to all
arm-none-eabi targets.

This target uses the soft-float ABI: functions which take f32 or f64 as
arguments will have those values packed into integer registers. This is the
only option because there is no FPU support in [Armv7-M].

Target maintainers

Rust Embedded Devices Working Group Arm Team
[arm-maintainers][arm_maintainers] ([rust@arm.com][arm_email])
Use @rustbot ping arm-maintainers to ping us

Target CPU and Target Feature options

See the bare-metal Arm
docs for details on how
to use these flags.

Table of supported CPUs

CPU | FPU | Target CPU | Target Features

Cortex-M3 | No | cortex-m3 | None

Arm Cortex-M3

The target CPU option is cortex-m3.

There are no relevant feature flags, and the FPU is not available.

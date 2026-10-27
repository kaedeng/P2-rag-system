# `thumbv7em-none-eabi` and `thumbv7em-none-eabihf`

thumbv7em-none-eabi and thumbv7em-none-eabihf

Tier: 2
Library Support: core and alloc (bare-metal, #![no_std])

Bare-metal target for CPUs in the [Armv7E-M] architecture family, supporting a
subset of the [T32 ISA][t32-isa].

Processors in this family include the:

[Arm Cortex-M4][cortex-m4] and Arm Cortex-M4F
[Arm Cortex-M7][cortex-m7] and Arm Cortex-M7F

See arm-none-eabi for information applicable to all
arm-none-eabi targets, in particular the difference between the eabi and
eabihf ABI.

Target maintainers

Rust Embedded Devices Working Group Arm Team
[arm-maintainers][arm_maintainers] ([rust@arm.com][arm_email])
Use @rustbot ping arm-maintainers to ping us

Target CPU and Target Feature options

See the bare-metal Arm
docs for details on how
to use these flags.

Table of supported CPUs for thumbv7em-none-eabi

CPU | FPU | DSP | Target CPU | Target Features

Any | No | Yes | None | None
Cortex-M4 | No | Yes | cortex-m4 | -fpregs
Cortex-M4F | SP | Yes | cortex-m4 | None
Cortex-M7 | No | Yes | cortex-m7 | -fpregs
Cortex-M7F | SP | Yes | cortex-m7 | -fp64
Cortex-M7F | DP | Yes | cortex-m7 | None

Table of supported CPUs for thumbv7em-none-eabihf

CPU | FPU | DSP | Target CPU | Target Features

Any | SP | Yes | None | None
Cortex-M4F | SP | Yes | cortex-m4 | None
Cortex-M7F | SP | Yes | cortex-m7 | -fp64
Cortex-M7F | DP | Yes | cortex-m7 | None

Never use the -fpregs target-feature with the thumbv7em-none-eabihf target
as it will cause compilation units to have different ABIs, which is unsound.

Arm Cortex-M4 and Arm Cortex-M4F

The target CPU is cortex-m4.

All Cortex-M4 have DSP extensions
support is controlled by the dsp target-feature
enabled by default with this target
Cortex-M4F has a single precision FPU
support is enabled by default with this target-cpu
disable support using the -fpregs target-feature (eabi only)

Arm Cortex-M7 and Arm Cortex-M7F

The target CPU is cortex-m7.

All Cortex-M7 have DSP extensions
support is controlled by the dsp target-feature
enabled by default with this target
Cortex-M7F have either a single-precision or double-precision FPU
double-precision support is enabled by default with this target-cpu
opt-out by using the -f64 target-feature
disable support entirely using the -fpregs target-feature (eabi only)

# `*-espidf`

*-espidf

Tier: 3

Targets for the ESP-IDF development framework running on RISC-V and Xtensa CPUs.

Target maintainers

@ivmarkov
@MabezDev
@SergioGasquez

Requirements

The target names follow this format: $ARCH-esp-espidf, where $ARCH specifies the target processor architecture. The following targets are currently defined:

Target name | Target CPU(s) | Minimum ESP-IDF version

riscv32imc-esp-espidf | ESP32-C2 | v5.0
riscv32imc-esp-espidf | ESP32-C3 | v4.4
riscv32imac-esp-espidf | ESP32-C6 | v5.1
riscv32imac-esp-espidf | ESP32-H2 | v5.1
riscv32imafc-esp-espidf | ESP32-P4 | v5.2
xtensa-esp32-espidf | ESP32 | v4.4
xtensa-esp32s2-espidf | ESP32-S2 | v4.4
xtensa-esp32s3-espidf | ESP32-S3 | v4.4

It is recommended to use the latest ESP-IDF stable release if possible.

Building the target

The target can be built by enabling it for a rustc build. The build-std feature is required to build the standard library for ESP-IDF. ldproxy is also required for linking, it can be installed from crates.io.

[build]
target = ["$ARCH-esp-espidf"]

[target.$ARCH-esp-espidf]
linker = "ldproxy"

[unstable]
build-std = ["std", "panic_abort"]

The esp-idf-sys crate will handle the compilation of ESP-IDF, including downloading the relevant toolchains for the build.

Cross-compilation toolchains and C code

esp-idf-sys exposes the toolchain used in the compilation of ESP-IDF, see the crate documentation for build output propagation for more information.

# `riscv64a23-unknown-linux-gnu`

riscv64a23-unknown-linux-gnu

Tier: 2 (without Host Tools)

RISC-V target using the ratified RVA23 Profile.
This target will enable all mandatory features of rva23u64 by default.

Target maintainers

@ZhongyaoChen
@CaiWeiran

Requirements

This target can be successfully built on the following platform: ubuntu 24.04 (Linux Kernel version 6.8.0, glibc 2.39).

Other platforms may work, but are not tested. Please contact us if you encounter any issues.

Building the target

Tier-2 targets are distributed through rustup. Install the target with:

rustup target add riscv64a23-unknown-linux-gnu

Building Rust programs

Cross compile crates with:

cargo build --target=riscv64a23-unknown-linux-gnu

For cross-compilation, you may need to install the appropriate linker:

# Ubuntu/Debian
sudo apt-get install gcc-riscv64-linux-gnu

# Then set the linker
RUSTFLAGS="-C linker=riscv64-linux-gnu-gcc" cargo build --target=riscv64a23-unknown-linux-gnu

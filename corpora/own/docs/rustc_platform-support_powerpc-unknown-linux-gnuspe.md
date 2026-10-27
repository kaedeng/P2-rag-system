# powerpc-unknown-linux-gnuspe

powerpc-unknown-linux-gnuspe

Tier: 3

powerpc-unknown-linux-gnuspe is a target for Linux on 32-bit PowerPC
processors that implement the Signal Processing Engine (SPE), such as e500, and
uses a different ABI than standard powerpc-unknown-linux-gnu.
When building for other 32-bit PowerPC processors, use
powerpc-unknown-linux-gnu instead.

See also Debian Wiki for details on
this platform, and ABI reference
for details on SPE ABI.

Note that support for PowerPC SPE by GCC was removed in GCC 9,
so recent GCC cannot be used as linker/compiler for this target.

Target maintainers

There are currently no formally documented target maintainers.

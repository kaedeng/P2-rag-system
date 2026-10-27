# Stability guarantees

Stability guarantees

This page gives an overview of our stability guarantees.

RFCs

RFC 1105 api evolution
RFC 1122 language semver

Blog posts

Stability as a Deliverable

rustc-dev-guide links

Stabilizing library features
Stabilizing language features
What qualifies as a bug fix?

Exemptions

Even if some of our infrastructure can be used by others, it is still considered
internal and comes without stability guarantees.
This is a non-exhaustive list of components without stability guarantees:

The CLIs and environment variables used by remote-test-client / remote-test-server

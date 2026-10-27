# Notification groups

Notification groups

The notification groups are an easy way to help out with rustc in a
"piece-meal" fashion, without committing to a larger project.
Notification groups are easy to join (just submit a PR!)
and joining does not entail any particular commitment.

Once you join a notification group, you will be added to
a list that receives pings on github whenever a new issue is found
that fits the notification group's criteria.
If you are interested, you can then [claim the issue] and start working on it.

Of course, you don't have to wait for new issues to be tagged!
If you prefer, you can use the GitHub label for a notification group to
search for existing issues that haven't been claimed yet.

List of notification groups

Here's the list of the notification groups:
Apple
ARM
Emscripten
Fuchsia
LoongArch
RISC-V
WASI
WebAssembly
Windows
Rust for Linux
GPU target

What issues are a good fit for notification groups?

Notification groups tend to get pinged on isolated bugs,
particularly those of middle priority:

By isolated, we mean that we do not expect large-scale refactoring
  to be required to fix the bug.
By middle priority, we mean that we'd like to see the bug fixed,
  but it's not such a burning problem that we are dropping everything else to fix it.
  The danger with such bugs, of course, is that they
  can accumulate over time, and the role of the notification group is
  to try and stop that from happening!

Joining a notification group

To join a notification group, you just have to open a PR adding your
GitHub username to the appropriate file in the Rust team repository.
See the "example PRs" below to get a precise idea and to identify the file to edit.

Also, if you are not already a member of a Rust team then -- in addition
to adding your name to the file -- you have to checkout the repository and
run the following command:

cargo run add-person $your_user_name

Example PRs:

Example of adding yourself to the Apple group.
Example of adding yourself to the ARM group.
Example of adding yourself to the Emscripten group.
Example of adding yourself to the LoongArch group.
Example of adding yourself to the RISC-V group.
Example of adding yourself to the WASI group.
Example of adding yourself to the WebAssembly group.
Example of adding yourself to the Windows group.

Tagging an issue for a notification group

To tag an issue as appropriate for a notification group, you give
[rustbot] a [ping] command with the name of the notification group.
For example:

@rustbot ping apple
@rustbot ping arm
@rustbot ping emscripten
@rustbot ping risc-v
@rustbot ping wasi
@rustbot ping wasm
@rustbot ping windows

To make some commands shorter and easier to remember, there are aliases,
defined in the [triagebot.toml] file.
For example, all of these commands are equivalent and will ping the Apple group:

@rustbot ping apple
@rustbot ping macos
@rustbot ping ios

Keep in mind that these aliases are meant to make humans' life easier.
They might be subject to change.
If you need to ensure that a command
will always be valid, prefer the full invocations over the aliases.

**Note though that this should only be done by compiler team members
or contributors, and is typically done as part of compiler team triage.**

Adding a notification group

See Forge.

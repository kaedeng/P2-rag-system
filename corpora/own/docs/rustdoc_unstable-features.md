# Unstable features

Unstable features

Rustdoc is under active development, and like the Rust compiler, some features are only available
on nightly releases. Some of these features are new and need some more testing before they're able to be
released to the world at large, and some of them are tied to features in the Rust compiler that are unstable. Several features here require a matching #![feature(...)] attribute to
enable, and thus are more fully documented in the [Unstable Book]. Those sections will link over
there as necessary.

Nightly-gated functionality

These features just require a nightly build to operate. Unlike the other features on this page,
these don't need to be "turned on" with a command-line flag or a #![feature(...)] attribute in
your crate. This can give them some subtle fallback modes when used on a stable release, so be
careful!

Error numbers for compile-fail doctests

As detailed in [the chapter on documentation tests][doctest-attributes], you can add a
compile_fail attribute to a doctest to state that the test should fail to compile. However, on
nightly, you can optionally add an error number to state that a doctest should emit a specific error
number:

```compile_fail,E0044
extern { fn some_func<T>(x: T); }
```

This is used by the error index to ensure that the samples that correspond to a given error number
properly emit that error code. However, these error codes aren't guaranteed to be the only thing
that a piece of code emits from version to version, so this is unlikely to be stabilized in the
future.

Attempting to use these error numbers on stable will result in the code sample being interpreted as
plain text.

missing_doc_code_examples lint

This lint will emit a warning if an item doesn't have a code example in its documentation.
It can be enabled using:

#![deny(rustdoc::missing_doc_code_examples)]

It is not emitted for items that cannot be instantiated/called such as fields, variants, modules,
associated trait/impl items, impl blocks, statics and constants.
It is also not emitted for foreign items, aliases, extern crates and imports.

Extensions to the #[doc] attribute

These features operate by extending the #[doc] attribute, and thus can be caught by the compiler
and enabled with a #![feature(...)] attribute in your crate.

Adding your trait to the "Notable traits" dialog

Tracking issue: #45040

Rustdoc keeps a list of a few traits that are believed to be "fundamental" to
types that implement them. These traits are intended to be the primary interface
for their implementers, and are often most of the API available to be documented
on their types. For this reason, Rustdoc will track when a given type implements
one of these traits and call special attention to it when a function returns one
of these types. This is the "Notable traits" dialog, accessible as a circled i
button next to the function, which, when clicked, shows the dialog.

In the standard library, some of the traits that are part of this list are
Iterator, Future, io::Read, and io::Write. However, rather than being
implemented as a hard-coded list, these traits have a special marker attribute
on them: #[doc(notable_trait)]. This means that you can apply this attribute
to your own trait to include it in the "Notable traits" dialog in documentation.

In addition to the "Notable traits" dialog, every type that implements a
#[doc(notable_trait)] trait renders a colored badge for that trait at the top
of its page, making the relationship easy to spot when browsing the type.

The #[doc(notable_trait)] attribute currently requires the #![feature(doc_notable_trait)]
feature gate. For more information, see [its chapter in the Unstable Book][unstable-notable_trait]
and [its tracking issue][issue-notable_trait].

Exclude certain dependencies from documentation

Tracking issue: #44027

The standard library uses several dependencies which, in turn, use several types and traits from the
standard library. In addition, there are several compiler-internal crates that are not considered to
be part of the official standard library, and thus would be a distraction to include in
documentation. It's not enough to exclude their crate documentation, since information about trait
implementations appears on the pages for both the type and the trait, which can be in different
crates!

To prevent internal types from being included in documentation, the standard library adds an
attribute to their extern crate declarations: #[doc(masked)]. This causes Rustdoc to "mask out"
types from these crates when building lists of trait implementations.

The #[doc(masked)] attribute is intended to be used internally, and requires the
#![feature(doc_masked)] feature gate. For more information, see [its chapter in the Unstable
Book][unstable-masked] and [its tracking issue][issue-masked].

Document primitives

This is for Rust compiler internal use only.

Since primitive types are defined in the compiler, there's no place to attach documentation
attributes. The #[rustc_doc_primitive = "..."] attribute is used by the standard library to
provide a way to generate documentation for primitive types, and requires #![feature(rustc_attrs)]
to enable.

Document keywords

This is for internal use in the std library.

Rust keywords are documented in the standard library (look for match for example).

To do so, the #[doc(keyword = "...")] attribute is used. Example:

#![feature(rustdoc_internals)]
#![allow(internal_features)]

/// Some documentation about the keyword.
#[doc(keyword = "break")]
const _: () = ();

Document builtin attributes

This is for internal use in the std library.

Rust builtin attributes are documented in the standard library (look for repr for example).

To do so, the #[doc(attribute = "...")] attribute is used. Example:

#![feature(rustdoc_internals)]
#![allow(internal_features)]

/// Some documentation about the attribute.
#[doc(attribute = "repr")]
const _: () = ();

Use the Rust logo as the crate logo

This is for official Rust project use only.

Internal Rustdoc pages like settings.html and scrape-examples-help.html show the Rust logo.
This logo is tracked as a static resource. The attribute #![doc(rust_logo)] makes this same
built-in resource act as the main logo.

#![feature(rustdoc_internals)]
#![allow(internal_features)]
#![doc(rust_logo)]
//! This crate has the Rust(tm) branding on it.

Effects of other nightly features

These nightly-only features are not primarily related to Rustdoc,
but have convenient effects on the documentation produced.

fundamental types

Annotating a type with #[fundamental] primarily influences coherence rules about generic types,
i.e., they alter whether other crates can provide implementations for that type.
The unstable book [links to further information][unstable-fundamental].

For documentation, this has an additional side effect:
If a method is implemented on F<T> (or F<&T>),
where F is a fundamental type,
then the method is not only documented at the page about F,
but also on the page about T.
In a sense, it makes the type transparent to Rustdoc.
This is especially convenient for types that work as annotated pointers,
such as Pin<&mut T>,
as it ensures that methods only implemented through those annotated pointers
can still be found with the type they act on.

If the fundamental feature's effect on coherence is not intended,
such a type can be marked as fundamental only for purposes of documentation
by introducing a custom feature and
limiting the use of fundamental to when documentation is built.

Unstable command-line arguments

These features are enabled by passing a command-line flag to Rustdoc, but the flags in question are
themselves marked as unstable. To use any of these options, pass -Z unstable-options as well as
the flag in question to Rustdoc on the command-line. To do this from Cargo, you can either use the
RUSTDOCFLAGS environment variable or the cargo rustdoc command.

--write-doc-meta-dir, and --read-doc-meta-dir

These options control how rustdoc handles files that combine data from multiple crates.

By default, rustdoc will read the doc meta from the doc output dir itself and merge them together.
This is very easy to use in scripts that manually invoke rustdoc, but it's also slow, because it
performs O(crates) work on every crate, meaning it performs O(crates2) work. When
--write-doc-meta-dir and/or --read-doc-meta-dir are supplied, this is turned off.

When --write-doc-meta-dir is supplied, rustdoc will write the crate's shared metadata to
that directory. This is an intermediate mode where it may write some files to the doc output
directory, but some features won't work until it is finalized.

When --read-doc-meta-dir is supplied, rustdoc runs in finalize mode. No crate source code is
passed to rustdoc when it runs in this mode. Multiple --read-doc-meta-dir can be passed to
rustdoc, so your build system can split the state between multiple directories if that helps.

--write-doc-meta-dir and --read-doc-meta-dir cannot both be passed to the same rustdoc invocation.

$ rustdoc crate1.rs --out-dir=doc
$ cat doc/search.index/crateNames/*
rd_("fcrate1")
$ rustdoc crate2.rs --out-dir=doc
$ cat doc/search.index/crateNames/*
rd_("fcrate1fcrate2")

To delay shared-data merging until the end of a build, so that you only have to perform O(crates)
work, use --write-doc-meta-dir on every crate, and the last will use --read-doc-meta-dir.

You can use separate metadata directories:

$ rustdoc +nightly crate1.rs --write-doc-meta-dir=crate1.d -Zunstable-options
$ cat doc/search.index/crateNames/*
cat: 'doc/search.index/crateNames/*': No such file or directory
$ rustdoc +nightly crate2.rs --write-doc-meta-dir=crate2.d -Zunstable-options
$ cat doc/search.index/crateNames/*
cat: 'doc/search.index/crateNames/*': No such file or directory
$ rustdoc +nightly --read-doc-meta-dir=crate1.d --read-doc-meta-dir=crate2.d -Zunstable-options
$ cat doc/search.index/crateNames/*
rd_("fcrate1fcrate2")

Or you can use a single metadata directory for all of the crates:

$ rustdoc +nightly crate1.rs --write-doc-meta-dir=meta.d -Zunstable-options
$ cat doc/search.index/crateNames/*
cat: 'doc/search.index/crateNames/*': No such file or directory
$ rustdoc +nightly crate2.rs --write-doc-meta-dir=meta.d -Zunstable-options
$ cat doc/search.index/crateNames/*
cat: 'doc/search.index/crateNames/*': No such file or directory
$ rustdoc +nightly --read-doc-meta-dir=meta.d -Zunstable-options
$ cat doc/search.index/crateNames/*
rd_("fcrate1fcrate2")

--document-hidden-items: Show items that are #[doc(hidden)]

By default, rustdoc does not document items that are annotated with
#[doc(hidden)].

--document-hidden-items causes all items to be documented as if they did not have #[doc(hidden)], except that hidden items will be shown with a 👻 icon.

Here is a table that fully describes which items are documented with each combination of --document-hidden-items and --document-private-items:

rustdoc flags | items that will be documented

neither flag | only public items that are not hidden
only --document-hidden-items | all public items
only --document-private-items | all items that are not hidden
both flags | all items

--markdown-before-content: include rendered Markdown before the content

Tracking issue: #44027

Using this flag looks like this:

$ rustdoc src/lib.rs -Z unstable-options --markdown-before-content extra.md
$ rustdoc README.md -Z unstable-options --markdown-before-content extra.md

Just like --html-before-content, this allows you to insert extra content inside the <body> tag
but before the other content rustdoc would normally produce in the rendered documentation.
However, instead of directly inserting the file verbatim, rustdoc will pass the files through a
Markdown renderer before inserting the result into the file.

--markdown-after-content: include rendered Markdown after the content

Using this flag looks like this:

$ rustdoc src/lib.rs -Z unstable-options --markdown-after-content extra.md
$ rustdoc README.md -Z unstable-options --markdown-after-content extra.md

Just like --html-after-content, this allows you to insert extra content before the </body> tag
but after the other content rustdoc would normally produce in the rendered documentation.
However, instead of directly inserting the file verbatim, rustdoc will pass the files through a
Markdown renderer before inserting the result into the file.

--playground-url: control the location of the playground

Using this flag looks like this:

$ rustdoc src/lib.rs -Z unstable-options --playground-url https://play.rust-lang.org/

When rendering a crate's docs, this flag gives the base URL of the Rust Playground, to use for
generating Run buttons. Unlike --markdown-playground-url, this argument works for standalone
Markdown files and Rust crates. This works the same way as adding #![doc(html_playground_url =
"url")] to your crate root, as mentioned in [the chapter about the #[doc]
attribute][doc-playground]. Please be aware that the official Rust Playground at
https://play.rust-lang.org does not have every crate available, so if your examples require your
crate, make sure the playground you provide has your crate available.

If both --playground-url and --markdown-playground-url are present when rendering a standalone
Markdown file, the URL given to --markdown-playground-url will take precedence. If both
--playground-url and #![doc(html_playground_url = "url")] are present when rendering crate docs,
the attribute will take precedence.

--sort-modules-by-appearance: control how items on module pages are sorted

Using this flag looks like this:

$ rustdoc src/lib.rs -Z unstable-options --sort-modules-by-appearance

Ordinarily, when rustdoc prints items in module pages, it will sort them alphabetically (taking
some consideration for their stability, and names that end in a number). Giving this flag to
rustdoc will disable this sorting and instead make it print the items in the order they appear in
the source.

--show-type-layout: add a section to each type's docs describing its memory layout

Tracking issue: #113248

Using this flag looks like this:

$ rustdoc src/lib.rs -Z unstable-options --show-type-layout

When this flag is passed, rustdoc will add a "Layout" section at the bottom of
each type's docs page that includes a summary of the type's memory layout as
computed by rustc. For example, rustdoc will show the size in bytes that a value
of that type will take in memory.

Note that most layout information is completely unstable and may even differ
between compilations.

--resource-suffix: modifying the name of CSS/JavaScript in crate docs

Tracking issue: #54765

Using this flag looks like this:

$ rustdoc src/lib.rs -Z unstable-options --resource-suffix suf

When rendering docs, rustdoc creates several CSS and JavaScript files as part of the output. Since
all these files are linked from every page, changing where they are can be cumbersome if you need to
specially cache them. This flag will rename all these files in the output to include the suffix in
the filename. For example, light.css would become light-suf.css with the above command.

--extern-html-root-url: control how rustdoc links to non-local crates

Using this flag looks like this:

$ rustdoc src/lib.rs -Z unstable-options --extern-html-root-url some-crate=https://example.com/some-crate/1.0.1

Ordinarily, when rustdoc wants to link to a type from a different crate, it looks in two places:
docs that already exist in the output directory, or the #![doc(doc_html_root)] set in the other
crate. However, if you want to link to docs that exist in neither of those places, you can use these
flags to control that behavior. When the --extern-html-root-url flag is given with a name matching
one of your dependencies, rustdoc use that URL for those docs. Keep in mind that if those docs exist
in the output directory, those local docs will still override this flag.

The names in this flag are first matched against the names given in the --extern name= flags,
which allows selecting between multiple crates with the same name (e.g. multiple versions of
the same crate). For transitive dependencies that haven't been loaded via an --extern flag, matching
falls backs to using crate names only, without ability to distinguish between multiple crates with
the same name.

-Z force-unstable-if-unmarked

Using this flag looks like this:

$ rustdoc src/lib.rs -Z force-unstable-if-unmarked

This is an internal flag intended for the standard library and compiler that applies an
#[unstable] attribute to any dependent crate that doesn't have another stability attribute. This
allows rustdoc to be able to generate documentation for the compiler crates and the standard
library, as an equivalent command-line argument is provided to rustc when building those crates.

--index-page: provide a top-level landing page for docs

This feature allows you to generate an index-page with a given markdown file. A good example of it
is the rust documentation index.

With this, you'll have a page which you can customize as much as you want at the top of your crates.

Using index-page option enables enable-index-page option as well.

--enable-index-page: generate a default index page for docs

This feature allows the generation of a default index-page which lists the generated crates.

--no-capture: disable output capture for test

When this flag is used with --test, the output (stdout and stderr) of your tests won't be
captured by rustdoc. Instead, the output will be directed to your terminal,
as if you had run the test executable manually. This is especially useful
for debugging your tests!

--check: only checks the documentation

When this flag is supplied, rustdoc will type check and lint your code, but will not generate any
documentation or run your doctests.

Using this flag looks like:

rustdoc -Z unstable-options --check src/lib.rs

--static-root-path: control how static files are loaded in HTML output

Using this flag looks like this:

$ rustdoc src/lib.rs -Z unstable-options --static-root-path '/cache/'

This flag controls how rustdoc links to its static files on HTML pages. If you're hosting a lot of
crates' docs generated by the same version of rustdoc, you can use this flag to cache rustdoc's CSS,
JavaScript, and font files in a single location, rather than duplicating it once per "doc root"
(grouping of crate docs generated into the same output directory, like with cargo doc). Per-crate
files like the search index will still load from the documentation root, but anything that gets
renamed with --resource-suffix will load from the given path.

--persist-doctests: persist doctest executables after running

Tracking issue: #56925

Using this flag looks like this:

$ rustdoc src/lib.rs --test -Z unstable-options --persist-doctests target/rustdoctest

This flag allows you to keep doctest executables around after they're compiled or run.
Usually, rustdoc will immediately discard a compiled doctest after it's been tested, but
with this option, you can keep those binaries around for farther testing.

--show-coverage: calculate the percentage of items with documentation

Tracking issue: #58154

Using this flag looks like this:

$ rustdoc src/lib.rs -Z unstable-options --show-coverage

It generates something like this:

+-------------------------------------+------------+------------+------------+------------+
| File | Documented | Percentage | Examples | Percentage |
+-------------------------------------+------------+------------+------------+------------+
| lib.rs | 4 | 100.0% | 1 | 25.0% |
+-------------------------------------+------------+------------+------------+------------+
| Total | 4 | 100.0% | 1 | 25.0% |
+-------------------------------------+------------+------------+------------+------------+

If you want to determine how many items in your crate are documented, pass this flag to rustdoc.
When it receives this flag, it will count the public items in your crate that have documentation,
and print out the counts and a percentage instead of generating docs.

Some methodology notes about what rustdoc counts in this metric:

Rustdoc will only count items from your crate (i.e. items re-exported from other crates don't
  count).
Docs written directly onto inherent impl blocks are not counted, even though their doc comments
  are displayed, because the common pattern in Rust code is to write all inherent methods into the
  same impl block.
Items in a trait implementation are not counted, as those impls will inherit any docs from the
  trait itself.
By default, only public items are counted. To count private items as well, pass
  --document-private-items at the same time.

Public items that are not documented can be seen with the built-in missing_docs lint. Private
items that are not documented can be seen with Clippy's missing_docs_in_private_items lint.

Calculating code examples follows these rules:

1. These items aren't accounted by default:
struct/union field
enum variant
constant
static
typedef
2. If one of the previously listed items has a code example, then it'll be counted.

If you use the -o option with it, it will generate the file into the given older name. For example:

rustdoc foo.rs --show-coverage -o doc

Will generate a foo.txt into the doc folder. If the -o option isn't passed, it will display
on stdout.

JSON output

When using --output-format json with this option, it will display the coverage information in
JSON format. For example, here is the JSON for a file with one documented item and one
undocumented item:

/// This item has documentation
pub fn foo() {}

pub fn no_documentation() {}

{"no_std.rs":{"total":3,"with_docs":1,"total_examples":3,"with_examples":0}}

Note that the third item is the crate root, which in this case is undocumented.

If you want the JSON output to be displayed on stdout instead of having a file generated, you can
use -o -.

-w/--output-format: output format

json

Tracking Issue: #76578

--output-format json emits documentation in the experimental
JSON format.

JSON Output for toolchain crates (std, alloc, core, test, and proc_macro)
is available via the rust-docs-json rustup component.

rustup component add --toolchain nightly rust-docs-json

Then the json files will be present in the share/doc/rust/json/ directory
of the rustup toolchain directory.

It can also be used with --show-coverage. Take a look at its
documentation for more
information.

doctest

Tracking issue: #134529

--output-format doctest emits JSON on stdout which gives you information about doctests in the
provided crate.

You can use this option like this:

rustdoc -Zunstable-options --output-format=doctest src/lib.rs

For this rust code:

/// ```
/// #![allow(dead_code)]
/// let x = 12;
/// Ok(())
/// ```
pub trait Trait {}

The generated output (formatted) will look like this:

{
  "format_version": 2,
  "doctests": [
    {
      "file": "src/lib.rs",
      "line": 1,
      "doctest_attributes": {
        "original": "",
        "should_panic": false,
        "no_run": false,
        "ignore": "None",
        "rust": true,
        "test_harness": false,
        "compile_fail": false,
        "standalone_crate": false,
        "error_codes": [],
        "edition": null,
        "added_css_classes": [],
        "unknown": []
      },
      "original_code": "#![allow(dead_code)]\nlet x = 12;\nOk(())",
      "doctest_code": {
        "crate_level": "#![allow(unused)]\n#![allow(dead_code)]\n\n",
        "code": "let x = 12;\nOk(())",
        "wrapper": {
          "before": "fn main() { fn _inner() -> core::result::Result<(), impl core::fmt::Debug> {\n",
          "after": "\n} _inner().unwrap() }",
          "returns_result": true
        }
      },
      "name": "src/lib.rs - (line 1)"
    }
  ]
}

format_version gives you the current version of the generated JSON. If we change the output in any way, the number will increase.
doctests contains the list of doctests present in the crate.
file is the file path where the doctest is located.
line is the line where the doctest starts (so where the \\\ is located in the current code).
   * doctest_attributes contains computed information about the attributes used on the doctests. For more information about doctest attributes, take a look [here](write-documentation/documentation-tests.html#attributes).
   * original_code is the code as written in the source code before rustdoc modifies it.
   * doctest_code is the code modified by rustdoc that will be run. If there is a fatal syntax error, this field will not be present.
     * crate_level is the crate level code (like attributes or extern crate) that will be added at the top-level of the generated doctest.
     * code is "naked" doctest without anything from crate_level and wrapper content.
     * wrapper contains extra code that will be added before and after code.
       * returns_result is a boolean. If true, it means that the doctest returns a Result type.
   * name is the name generated by rustdoc which represents this doctest.

### html

--output-format html has no effect, as the default output is HTML. This is
accepted on stable, even though the other options for this flag aren't.

## --with-examples: include examples of uses of items as documentation

 * Tracking issue: [#88791](https://github.com/rust-lang/rust/issues/88791)

This option, combined with --scrape-examples-target-crate and
--scrape-examples-output-path, is used to implement the functionality in [RFC
#3123](https://github.com/rust-lang/rfcs/pull/3123). Uses of an item (currently
functions / call-sites) are found in a crate and its reverse-dependencies, and
then the uses are included as documentation for that item. This feature is
intended to be used via cargo doc --scrape-examples, but the rustdoc-only
workflow looks like:

28

First, the library must be checked to generate an rmeta. Then a
reverse-dependency like examples/ex.rs is given to rustdoc with the target
crate being documented (foobar) and a path to output the calls
(output.calls). Then, the generated calls file can be passed via
--with-examples to the subsequent documentation of foobar.

To scrape examples from test code, e.g. functions marked #[test], then
add the --scrape-tests flag.

## --generate-link-to-definition: Generate links on types in source code

 * Tracking issue: [#89095](https://github.com/rust-lang/rust/issues/89095)

This flag enables the generation of links in the source code pages which allow the reader
to jump to a type definition.

> [!WARNING]
> In very specific scenarios, enabling this feature may lead to your program getting rejected if you
> rely on rustdoc intentionally not running all semantic analysis passes on function bodies to aid
> with documenting cfg-conditional items.
>
> More concretely, rustdoc may choose to type-check bodies if they contain type-dependent paths
> including method calls. This may result in name resolution and type errors getting reported that
> rustdoc would usually suppress.

### --test-builder: rustc-like program to build tests

 * Tracking issue: [#102981](https://github.com/rust-lang/rust/issues/102981)

Using this flag looks like this:

29

Rustdoc will use the provided program to compile tests instead of the default rustc program from
the sysroot.

### --test-builder-wrapper: wrap calls to the test builder

 * Tracking issue: [#102981](https://github.com/rust-lang/rust/issues/102981)

Using this flag looks like this:

30

Similar to cargo build.rustc-wrapper option, this flag takes a rustc wrapper program.
The first argument to the program will be the test builder program.

This flag can be passed multiple times to nest wrappers.

## Passing arguments to rustc when compiling doctests

You can use the --doctest-build-arg flag if you want to add options when compiling the
doctest. For example if you have:

31

And you run rustdoc --test on it, you will get:

32

But if you can limit the lint level to warning by using --doctest-build-arg=--cap-lints=warn:

33

In order to pass multiple arguments to the underlying compiler,
pass --doctest-build-arg ARG for each argument ARG.

## --generate-macro-expansion: Generate macros expansion toggles in source code

This flag enables the generation of toggles to expand macros in the HTML source code pages.

## --remap-path-scope: Scopes to which the source remapping should be done

This flag is the equivalent flag from rustc --remap-path-scope.

Defines which scopes of paths should be remapped by --remap-path-prefix.

### documentation scope

rustdoc (and by extension rustc) have a special documentation remapping scope, it
permits remapping source paths that ends up in the generated documentation.

It can specified with --remap-path-scope=documentation.

## #[doc(cfg)] and #[doc(auto_cfg)]

This feature aims at providing rustdoc users the possibility to add visual markers to the rendered documentation to know under which conditions an item is available (currently possible through the following unstable feature: doc_cfg).

It does not aim to allow having a same item with different cfgs to appear more than once in the generated documentation.

It does not aim to document items which are *inactive* under the current configuration (i.e., “cfged out”).

This features adds the following attributes:

 * #[doc(auto_cfg)]/#[doc(auto_cfg = true)]/#[doc(auto_cfg = false)]
 * #[doc(cfg(...))]
 * #![doc(auto_cfg(hide(...)))] / #[doc(auto_cfg(show(...)))]

All of these attributes can be added to a module or to the crate root, and they will be inherited by the child items unless another attribute overrides it. This is why "opposite" attributes like auto_cfg(hide(...)) and auto_cfg(show(...)) are provided: they allow a child item to override its parent.

### #[doc(cfg(...))]

This attribute provides a standardized format to override #[cfg()] attributes to document conditionally available items. Example:

34

It will display in the documentation for this module:

35

You can use it to display information in generated documentation, whether or not there is a #[cfg()] attribute:

36

It will be displayed exactly the same as the previous code.

This attribute has the same syntax as conditional compilation, but it only causes documentation to be added. This means #[doc(cfg(not(windows)))] will not cause your docs to be hidden on non-windows targets, even though #[cfg(not(windows))] does do that.

If doc(auto_cfg) is enabled on the item, doc(cfg) will override it anyway so in the two previous examples, even if the doc(auto_cfg) feature was enabled, it would still display the same thing.

This attribute works on modules and on items.

### #[doc(auto_cfg(hide(...)))]

This attribute is used to prevent some cfg to be generated in the visual markers. It only applies to #[doc(auto_cfg = true)], not to #[doc(cfg(...))]. So in the previous example:

37

It currently displays both unix and feature = "futures-io" into the documentation, which is not great. To prevent the unix cfg to ever be displayed, you can use this attribute at the crate root level:

38

Or directly on a given item/module as it covers any of the item's descendants:

39

Then, the unix cfg will never be displayed into the documentation.

The syntax of hide is as follows: you can list as many cfg name as you want:

40

With the above example, it means that #[cfg(feature)] and #[cfg(target_os)] won't be displayed in the docs. However, #[cfg(target_os = "linux)] or #[cfg(feature = "something")] will be displayed because only the key without values was marked as hidden. if you want to hide some values, you can do:

41

In this case, #[cfg(feature = "linux")], #[cfg(feature = "something")], #[cfg(target_os = "something")] and #[cfg(target_os = "linux")] will be hidden. All listed keys will be impacted by values(...). You can split them by having two hide:

42

Now, only #[cfg(feature = "something")] and #[cfg(target_os = "linux")] will be hidden. If you want to hide a key and all its values, you can use any():

43

If you want to hide only when there is no value you can use none():

44

So now, if you want to forbid all values for a key, but allow the key itself, you can do:

45

If the previous example, both #[cfg(feature)] and #[cfg(feature = "something")] will be hidden.

Rustdoc currently hides test, doc and doctest attributes by default and reserves the right to change the list of "hidden by default" attributes.

The attribute accepts only a list of identifiers and values(). So you can write:

46

But you cannot write:

47

So if we use doc(auto_cfg(hide(unix))), it means it will hide all mentions of unix without a value:

48

However, it only impacts the unix cfg, not the feature:

49

Using this attribute will re-enable auto_cfg if it was disabled at this location:

50

And using doc(auto_cfg) will re-enable it:

51

The reason behind this is that doc(auto_cfg = ...) enables or disables the feature, whereas doc(auto_cfg(...)) enables it unconditionally, making the first attribute to appear useless as it will be overidden by the next doc(auto_cfg) attribute.

### #[doc(auto_cfg(show(...)))]

This attribute does the opposite of #[doc(auto_cfg(hide(...)))]: if you used #[doc(auto_cfg(hide(...)))] and want to revert its effect on an item and its descendants, you can use #[doc(auto_cfg(show(...)))].
It only applies to #[doc(auto_cfg = true)], not to #[doc(cfg(...))].

It follows the same syntax rules as for #[doc(auto_cfg(hide(...)))].

For example:

52

The attribute accepts only a list of identifiers or key/value items. So you can write:

53

But you cannot write:

54

If auto_cfg(show(...)) and auto_cfg(hide(...)) are used to show/hide a same cfg on a same item, it'll emit an error. Example:

55

Using this attribute will re-enable auto_cfg if it was disabled at this location:

56

### #[doc(auto_cfg)/#[doc(auto_cfg = true)]/#[doc(auto_cfg = false)]

By default, #[doc(auto_cfg)] is enabled at the crate-level. When it's enabled, Rustdoc will automatically display cfg(...) compatibility information as-if the same #[doc(cfg(...))] had been specified.

This attribute impacts the item on which it is used and its descendants.

So if we take back the previous example:

57

There's no need to "duplicate" the cfg into a doc(cfg()) to make Rustdoc display it.

In some situations, the detailed conditional compilation rules used to implement the feature might not serve as good documentation (for example, the list of supported platforms might be very long, and it might be better to document them in one place). To turn it off, add the #[doc(auto_cfg = false)] attribute on the item.

If no argument is specified (ie #[doc(auto_cfg)]), it's the same as writing #[doc(auto_cfg = true)].

## Inheritance

Rustdoc merges cfg attributes from parent modules to its children. For example, in this case, the module non_unix will describe the entire compatibility matrix for the module, and not just its directly attached information:

58

This code will display:

59

### Re-exports and inlining

cfg attributes of a re-export are never merged with the re-exported item(s) attributes except if the re-export has the #[doc(inline)] attribute. In this case, the cfg of the re-exported item will be merged with the re-export's.

When talking about "attributes merge", we mean that if the re-export has #[cfg(unix)] and the re-exported item has #[cfg(feature = "foo")], you will only see cfg(unix) on the re-export and only cfg(feature = "foo") on the re-exported item, unless the re-export has #[doc(inline)], then you will only see the re-exported item with both cfg(unix) and cfg(feature = "foo").

Example:

60

In this example, non_unix_desktop will only display cfg(target_os = "freeebsd") and not display any cfg from desktop::non_unix.

On the contrary, inlined_non_unix_desktop will have cfgs from both the re-export and the re-exported item.

So that also means that if a crate re-exports a foreign item, unless it has #[doc(inline)], the cfg and doc(cfg)` attributes will not be visible:

// dep:
#[cfg(feature = "a")]
pub struct S;

// crate using dep:

// There will be no mention of `feature = "a"` in the documentation.
pub use dep::S as Y;

# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 424 (the final check needs at least 200)
- Words: 372,062
- Estimated tokens (words times 1.4): 520,886 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `rustc-dev-guide_about-this-guide` | 659 | - | - | - |
| `rustc-dev-guide_ambig-unambig-ty-and-consts` | 926 | - | - | - |
| `rustc-dev-guide_analysis_well-formed` | 1,862 | - | - | - |
| `rustc-dev-guide_appendix_additional-resources` | 622 | - | - | - |
| `rustc-dev-guide_appendix_background` | 1,659 | - | - | - |
| `rustc-dev-guide_appendix_bibliography` | 526 | - | - | - |
| `rustc-dev-guide_appendix_code-index` | 534 | - | - | - |
| `rustc-dev-guide_appendix_compiler-lecture` | 417 | - | - | - |
| `rustc-dev-guide_appendix_glossary` | 3,211 | - | - | - |
| `rustc-dev-guide_appendix_humorust` | 54 | - | - | - |
| `rustc-dev-guide_appendix_reading-club` | 121 | - | - | - |
| `rustc-dev-guide_asm` | 1,092 | - | - | - |
| `rustc-dev-guide_ast-validation` | 163 | - | - | - |
| `rustc-dev-guide_attributes` | 565 | - | - | - |
| `rustc-dev-guide_autodiff_debugging` | 1,315 | - | - | - |
| `rustc-dev-guide_autodiff_flags` | 327 | - | - | - |
| `rustc-dev-guide_autodiff_installation` | 648 | - | - | - |
| `rustc-dev-guide_autodiff_internals` | 285 | - | - | - |
| `rustc-dev-guide_autodiff_type-trees` | 648 | - | - | - |
| `rustc-dev-guide_backend_backend-agnostic` | 1,208 | - | - | - |
| `rustc-dev-guide_backend_codegen` | 529 | - | - | - |
| `rustc-dev-guide_backend_debugging` | 1,756 | - | - | - |
| `rustc-dev-guide_backend_implicit-caller-location` | 1,408 | - | - | - |
| `rustc-dev-guide_backend_libs-and-metadata` | 1,181 | - | - | - |
| `rustc-dev-guide_backend_lowering-mir` | 298 | - | - | - |
| `rustc-dev-guide_backend_monomorph` | 510 | - | - | - |
| `rustc-dev-guide_backend_updating-llvm` | 1,419 | - | - | - |
| `rustc-dev-guide_borrow-check` | 403 | - | - | - |
| `rustc-dev-guide_borrow-check_debugging` | 190 | - | - | - |
| `rustc-dev-guide_borrow-check_drop-check` | 902 | - | - | - |
| `rustc-dev-guide_borrow-check_moves-and-initialization` | 249 | - | - | - |
| `rustc-dev-guide_borrow-check_moves-and-initialization_move-paths` | 715 | - | - | - |
| `rustc-dev-guide_borrow-check_opaque-types-region-inference-restr` | 1,492 | - | - | - |
| `rustc-dev-guide_borrow-check_region-inference` | 1,311 | - | - | - |
| `rustc-dev-guide_borrow-check_region-inference_closure-constraint` | 545 | - | - | - |
| `rustc-dev-guide_borrow-check_region-inference_constraint-propaga` | 1,395 | - | - | - |
| `rustc-dev-guide_borrow-check_region-inference_lifetime-parameter` | 731 | - | - | - |
| `rustc-dev-guide_borrow-check_region-inference_member-constraints` | 1,418 | - | - | - |
| `rustc-dev-guide_borrow-check_region-inference_placeholders-and-u` | 2,500 | - | - | - |
| `rustc-dev-guide_borrow-check_two-phase-borrows` | 454 | - | - | - |
| `rustc-dev-guide_borrow-check_type-check` | 585 | - | - | - |
| `rustc-dev-guide_bug-fix-procedure` | 1,874 | - | - | - |
| `rustc-dev-guide_building_bootstrapping_bootstrap-in-dependencies` | 353 | - | - | - |
| `rustc-dev-guide_building_bootstrapping_debugging-bootstrap` | 1,048 | - | - | - |
| `rustc-dev-guide_building_bootstrapping_how-bootstrap-does-it` | 247 | - | - | - |
| `rustc-dev-guide_building_bootstrapping_intro` | 140 | - | - | - |
| `rustc-dev-guide_building_bootstrapping_what-bootstrapping-does` | 2,590 | - | - | - |
| `rustc-dev-guide_building_bootstrapping_writing-tools-in-bootstra` | 198 | - | - | - |
| `rustc-dev-guide_building_build-install-distribution-artifacts` | 155 | - | - | - |
| `rustc-dev-guide_building_compiler-documenting` | 358 | - | - | - |
| `rustc-dev-guide_building_how-to-build-and-run` | 2,375 | - | - | - |
| `rustc-dev-guide_building_new-target` | 778 | - | - | - |
| `rustc-dev-guide_building_optimized-build` | 659 | - | - | - |
| `rustc-dev-guide_building_prerequisites` | 298 | - | - | - |
| `rustc-dev-guide_building_quickstart` | 379 | - | - | - |
| `rustc-dev-guide_building_suggested` | 2,568 | - | - | - |
| `rustc-dev-guide_cli` | 199 | - | - | - |
| `rustc-dev-guide_closure` | 1,170 | - | - | - |
| `rustc-dev-guide_coherence` | 505 | - | - | - |
| `rustc-dev-guide_compiler-debugging` | 1,747 | - | - | - |
| `rustc-dev-guide_compiler-src` | 1,029 | - | - | - |
| `rustc-dev-guide_compiler-team` | 867 | - | - | - |
| `rustc-dev-guide_const-eval` | 335 | - | - | - |
| `rustc-dev-guide_const-eval_interpret` | 1,696 | - | - | - |
| `rustc-dev-guide_const-generics` | 1,924 | - | - | - |
| `rustc-dev-guide_contributing` | 334 | - | - | - |
| `rustc-dev-guide_contributing-to-guide` | 429 | - | - | - |
| `rustc-dev-guide_conventions` | 1,096 | - | - | - |
| `rustc-dev-guide_coroutine-closures` | 2,954 | - | - | - |
| `rustc-dev-guide_crates-io` | 54 | - | - | - |
| `rustc-dev-guide_debugging-support-in-rustc` | 2,336 | - | - | - |
| `rustc-dev-guide_debuginfo_debugger-internals` | 133 | - | - | - |
| `rustc-dev-guide_debuginfo_debugger-visualizers` | 976 | - | - | - |
| `rustc-dev-guide_debuginfo_intro` | 1,031 | - | - | - |
| `rustc-dev-guide_debuginfo_lldb-internals` | 1,502 | - | - | - |
| `rustc-dev-guide_debuginfo_lldb-visualizers` | 3,770 | - | - | - |
| `rustc-dev-guide_debuginfo_llvm-codegen` | 76 | - | - | - |
| `rustc-dev-guide_debuginfo_rust-codegen` | 943 | - | - | - |
| `rustc-dev-guide_debuginfo_testing` | 1,665 | - | - | - |
| `rustc-dev-guide_diagnostics` | 5,352 | - | - | - |
| `rustc-dev-guide_diagnostics_diagnostic-items` | 795 | - | - | - |
| `rustc-dev-guide_diagnostics_diagnostic-structs` | 2,114 | - | - | - |
| `rustc-dev-guide_diagnostics_error-codes` | 414 | - | - | - |
| `rustc-dev-guide_diagnostics_error-guaranteed` | 240 | - | - | - |
| `rustc-dev-guide_diagnostics_lintstore` | 707 | - | - | - |
| `rustc-dev-guide_diagnostics_translation` | 971 | - | - | - |
| `rustc-dev-guide_early-late-parameters` | 3,051 | - | - | - |
| `rustc-dev-guide_effects` | 912 | - | - | - |
| `rustc-dev-guide_external-repos` | 1,175 | - | - | - |
| `rustc-dev-guide_feature-gate-check` | 613 | - | - | - |
| `rustc-dev-guide_feature-gates` | 261 | - | - | - |
| `rustc-dev-guide_fuzzing` | 892 | - | - | - |
| `rustc-dev-guide_generic-parameters-summary` | 252 | - | - | - |
| `rustc-dev-guide_getting-started` | 1,159 | - | - | - |
| `rustc-dev-guide_git` | 4,145 | - | - | - |
| `rustc-dev-guide_guides_editions` | 2,514 | - | - | - |
| `rustc-dev-guide_hir` | 940 | - | - | - |
| `rustc-dev-guide_hir-typeck_coercions` | 2,550 | - | - | - |
| `rustc-dev-guide_hir-typeck_method-lookup` | 673 | - | - | - |
| `rustc-dev-guide_hir-typeck_summary` | 262 | - | - | - |
| `rustc-dev-guide_hir_attribute-parsing` | 826 | - | - | - |
| `rustc-dev-guide_hir_debugging` | 110 | - | - | - |
| `rustc-dev-guide_hir_lowering` | 513 | - | - | - |
| `rustc-dev-guide_implementing-new-features` | 2,129 | - | - | - |
| `rustc-dev-guide_incrcomp-debugging` | 666 | - | - | - |
| `rustc-dev-guide_lang-items` | 433 | - | - | - |
| `rustc-dev-guide_licenses` | 323 | - | - | - |
| `rustc-dev-guide_llm-guidance` | 66 | - | - | - |
| `rustc-dev-guide_llm-guidance_reviewing` | 799 | - | - | - |
| `rustc-dev-guide_llm-guidance_writing` | 1,068 | - | - | - |
| `rustc-dev-guide_llvm-coverage-instrumentation` | 702 | - | - | - |
| `rustc-dev-guide_macro-expansion` | 3,307 | - | - | - |
| `rustc-dev-guide_memory` | 681 | - | - | - |
| `rustc-dev-guide_mir_construction` | 879 | - | - | - |
| `rustc-dev-guide_mir_dataflow` | 1,114 | - | - | - |
| `rustc-dev-guide_mir_debugging` | 368 | - | - | - |
| `rustc-dev-guide_mir_drop-elaboration` | 1,394 | - | - | - |
| `rustc-dev-guide_mir_index` | 1,982 | - | - | - |
| `rustc-dev-guide_mir_optimizations` | 687 | - | - | - |
| `rustc-dev-guide_mir_passes` | 1,053 | - | - | - |
| `rustc-dev-guide_mir_visitor` | 239 | - | - | - |
| `rustc-dev-guide_name-resolution` | 1,319 | - | - | - |
| `rustc-dev-guide_normalization` | 2,921 | - | - | - |
| `rustc-dev-guide_notification-groups_about` | 559 | - | - | - |
| `rustc-dev-guide_notification-groups_apple` | 318 | - | - | - |
| `rustc-dev-guide_notification-groups_arm` | 96 | - | - | - |
| `rustc-dev-guide_notification-groups_emscripten` | 96 | - | - | - |
| `rustc-dev-guide_notification-groups_gpu-target` | 78 | - | - | - |
| `rustc-dev-guide_notification-groups_loongarch` | 96 | - | - | - |
| `rustc-dev-guide_notification-groups_risc-v` | 96 | - | - | - |
| `rustc-dev-guide_notification-groups_rust-for-linux` | 121 | - | - | - |
| `rustc-dev-guide_notification-groups_wasi` | 96 | - | - | - |
| `rustc-dev-guide_notification-groups_wasm` | 97 | - | - | - |
| `rustc-dev-guide_notification-groups_windows` | 161 | - | - | - |
| `rustc-dev-guide_offload_contributing` | 334 | - | - | - |
| `rustc-dev-guide_offload_installation` | 254 | - | - | - |
| `rustc-dev-guide_offload_internals` | 850 | - | - | - |
| `rustc-dev-guide_offload_usage` | 473 | - | - | - |
| `rustc-dev-guide_opaque-types-impl-trait-inference` | 1,425 | - | - | - |
| `rustc-dev-guide_opaque-types-type-alias-impl-trait` | 487 | - | - | - |
| `rustc-dev-guide_overview` | 2,968 | - | - | - |
| `rustc-dev-guide_panic-implementation` | 736 | - | - | - |
| `rustc-dev-guide_parallel-rustc` | 1,081 | - | - | - |
| `rustc-dev-guide_part-2-intro` | 121 | - | - | - |
| `rustc-dev-guide_part-3-intro` | 82 | - | - | - |
| `rustc-dev-guide_part-4-intro` | 117 | - | - | - |
| `rustc-dev-guide_part-5-intro` | 383 | - | - | - |
| `rustc-dev-guide_pat-exhaustive-checking` | 1,344 | - | - | - |
| `rustc-dev-guide_pr-lifecycle` | 1,474 | - | - | - |
| `rustc-dev-guide_profile-guided-optimization` | 711 | - | - | - |
| `rustc-dev-guide_profiling` | 677 | - | - | - |
| `rustc-dev-guide_profiling_with-perf` | 1,877 | - | - | - |
| `rustc-dev-guide_profiling_with-rustc-perf` | 477 | - | - | - |
| `rustc-dev-guide_profiling_wpa-profiling` | 836 | - | - | - |
| `rustc-dev-guide_queries_incremental-compilation` | 1,173 | - | - | - |
| `rustc-dev-guide_queries_incremental-compilation-in-detail` | 4,107 | - | - | - |
| `rustc-dev-guide_queries_query-evaluation-model-in-detail` | 1,452 | - | - | - |
| `rustc-dev-guide_queries_salsa` | 1,395 | - | - | - |
| `rustc-dev-guide_query` | 2,023 | - | - | - |
| `rustc-dev-guide_return-position-impl-trait-in-trait` | 2,277 | - | - | - |
| `rustc-dev-guide_rustbot` | 371 | - | - | - |
| `rustc-dev-guide_rustc-driver_external-rustc-drivers` | 402 | - | - | - |
| `rustc-dev-guide_rustc-driver_intro` | 277 | - | - | - |
| `rustc-dev-guide_rustdoc` | 1,364 | - | - | - |
| `rustc-dev-guide_rustdoc-internals` | 1,736 | - | - | - |
| `rustc-dev-guide_rustdoc-internals_rustdoc-gui-test-suite` | 92 | - | - | - |
| `rustc-dev-guide_rustdoc-internals_rustdoc-html-test-suite` | 1,111 | - | - | - |
| `rustc-dev-guide_rustdoc-internals_rustdoc-json-test-suite` | 449 | - | - | - |
| `rustc-dev-guide_rustdoc-internals_search` | 3,145 | - | - | - |
| `rustc-dev-guide_sanitizers` | 569 | - | - | - |
| `rustc-dev-guide_serialization` | 835 | - | - | - |
| `rustc-dev-guide_solve_caching` | 771 | - | - | - |
| `rustc-dev-guide_solve_candidate-preference` | 2,129 | - | - | - |
| `rustc-dev-guide_solve_canonicalization` | 638 | - | - | - |
| `rustc-dev-guide_solve_coinduction` | 1,411 | - | - | - |
| `rustc-dev-guide_solve_invariants` | 1,554 | - | - | - |
| `rustc-dev-guide_solve_opaque-types` | 955 | - | - | - |
| `rustc-dev-guide_solve_proof-trees` | 335 | - | - | - |
| `rustc-dev-guide_solve_sharing-crates-with-rust-analyzer` | 1,652 | - | - | - |
| `rustc-dev-guide_solve_significant-changes` | 687 | - | - | - |
| `rustc-dev-guide_solve_the-solver` | 490 | - | - | - |
| `rustc-dev-guide_solve_trait-solving` | 317 | - | - | - |
| `rustc-dev-guide_stability` | 1,437 | - | - | - |
| `rustc-dev-guide_stability-guarantees` | 82 | - | - | - |
| `rustc-dev-guide_stabilization-guide` | 1,286 | - | - | - |
| `rustc-dev-guide_stabilization-report-template` | 1,146 | - | - | - |
| `rustc-dev-guide_syntax-intro` | 112 | - | - | - |
| `rustc-dev-guide_test-implementation` | 745 | - | - | - |
| `rustc-dev-guide_tests_adding` | 1,233 | - | - | - |
| `rustc-dev-guide_tests_autodiff-ci-job` | 164 | - | - | - |
| `rustc-dev-guide_tests_best-practices` | 1,266 | - | - | - |
| `rustc-dev-guide_tests_ci` | 3,675 | - | - | - |
| `rustc-dev-guide_tests_codegen-backend-tests_cg_gcc` | 643 | - | - | - |
| `rustc-dev-guide_tests_codegen-backend-tests_intro` | 50 | - | - | - |
| `rustc-dev-guide_tests_compiletest` | 5,153 | - | - | - |
| `rustc-dev-guide_tests_crater` | 360 | - | - | - |
| `rustc-dev-guide_tests_directives` | 3,512 | - | - | - |
| `rustc-dev-guide_tests_docker` | 749 | - | - | - |
| `rustc-dev-guide_tests_ecosystem` | 134 | - | - | - |
| `rustc-dev-guide_tests_ecosystem-test-jobs_fuchsia` | 998 | - | - | - |
| `rustc-dev-guide_tests_ecosystem-test-jobs_rust-for-linux` | 321 | - | - | - |
| `rustc-dev-guide_tests_intro` | 797 | - | - | - |
| `rustc-dev-guide_tests_minicore` | 292 | - | - | - |
| `rustc-dev-guide_tests_misc` | 291 | - | - | - |
| `rustc-dev-guide_tests_optional-x86_64-gnu-parallel-frontend` | 82 | - | - | - |
| `rustc-dev-guide_tests_perf` | 512 | - | - | - |
| `rustc-dev-guide_tests_running` | 1,991 | - | - | - |
| `rustc-dev-guide_tests_stdlib-semver-check` | 354 | - | - | - |
| `rustc-dev-guide_tests_ui` | 3,908 | - | - | - |
| `rustc-dev-guide_tests_x86_64-gnu-next-trait-solver-polonius-ci-j` | 267 | - | - | - |
| `rustc-dev-guide_the-parser` | 504 | - | - | - |
| `rustc-dev-guide_thir` | 721 | - | - | - |
| `rustc-dev-guide_tracing` | 1,573 | - | - | - |
| `rustc-dev-guide_traits_caching` | 481 | - | - | - |
| `rustc-dev-guide_traits_canonical-queries` | 1,337 | - | - | - |
| `rustc-dev-guide_traits_canonicalization` | 1,368 | - | - | - |
| `rustc-dev-guide_traits_chalk` | 259 | - | - | - |
| `rustc-dev-guide_traits_goals-and-clauses` | 1,286 | - | - | - |
| `rustc-dev-guide_traits_hrtb` | 748 | - | - | - |
| `rustc-dev-guide_traits_implied-bounds` | 447 | - | - | - |
| `rustc-dev-guide_traits_lowering-to-logic` | 1,072 | - | - | - |
| `rustc-dev-guide_traits_resolution` | 1,583 | - | - | - |
| `rustc-dev-guide_traits_separate-projection-bounds` | 345 | - | - | - |
| `rustc-dev-guide_traits_specialization` | 380 | - | - | - |
| `rustc-dev-guide_traits_unsize` | 521 | - | - | - |
| `rustc-dev-guide_ty` | 2,553 | - | - | - |
| `rustc-dev-guide_ty-fold` | 696 | - | - | - |
| `rustc-dev-guide_ty-module_binders` | 549 | - | - | - |
| `rustc-dev-guide_ty-module_early-binder` | 673 | - | - | - |
| `rustc-dev-guide_ty-module_generic-arguments` | 985 | - | - | - |
| `rustc-dev-guide_ty-module_instantiating-binders` | 1,796 | - | - | - |
| `rustc-dev-guide_ty-module_param-ty-const-regions` | 724 | - | - | - |
| `rustc-dev-guide_type-inference` | 1,504 | - | - | - |
| `rustc-dev-guide_typing-parameter-envs` | 1,640 | - | - | - |
| `rustc-dev-guide_unsafety-checking` | 456 | - | - | - |
| `rustc-dev-guide_variance` | 1,949 | - | - | - |
| `rustc-dev-guide_walkthroughs_lang-feature` | 1,677 | - | - | - |
| `rustc-dev-guide_walkthroughs_test` | 595 | - | - | - |
| `rustc_check-cfg` | 1,110 | - | - | - |
| `rustc_check-cfg_cargo-specifics` | 226 | - | - | - |
| `rustc_codegen-options_index` | 4,956 | - | - | - |
| `rustc_command-line-arguments` | 3,198 | - | - | - |
| `rustc_command-line-arguments_print-options` | 618 | - | - | - |
| `rustc_contributing` | 62 | - | - | - |
| `rustc_exploit-mitigations` | 2,755 | - | - | reference list dropped, 6,336 characters (heading) |
| `rustc_instrument-coverage` | 2,381 | - | - | - |
| `rustc_jobserver` | 369 | - | - | - |
| `rustc_json` | 1,745 | - | - | - |
| `rustc_linker-plugin-lto` | 1,203 | - | - | - |
| `rustc_lints_groups` | 104 | - | - | - |
| `rustc_lints_index` | 368 | - | - | - |
| `rustc_lints_levels` | 1,736 | - | - | - |
| `rustc_platform-support` | 3,803 | - | - | - |
| `rustc_platform-support_aarch64-nintendo-switch-freestanding` | 118 | - | - | - |
| `rustc_platform-support_aarch64-unknown-linux-gnu` | 140 | - | - | - |
| `rustc_platform-support_aarch64-unknown-linux-musl` | 127 | - | - | - |
| `rustc_platform-support_aarch64-unknown-linux-pauthtest` | 2,287 | - | - | - |
| `rustc_platform-support_aarch64-unknown-none` | 372 | - | - | - |
| `rustc_platform-support_aarch64-unknown-qtee` | 429 | - | - | - |
| `rustc_platform-support_aarch64-unknown-teeos` | 418 | - | - | - |
| `rustc_platform-support_aarch64_be-unknown-linux-musl` | 121 | - | - | - |
| `rustc_platform-support_aarch64_be-unknown-none-softfloat` | 399 | - | - | - |
| `rustc_platform-support_aarch64v8r-unknown-none` | 416 | - | - | - |
| `rustc_platform-support_aix` | 134 | - | - | - |
| `rustc_platform-support_amdgcn-amd-amdhsa` | 500 | - | - | - |
| `rustc_platform-support_android` | 219 | - | - | - |
| `rustc_platform-support_apple-darwin` | 298 | - | - | - |
| `rustc_platform-support_apple-ios` | 385 | - | - | - |
| `rustc_platform-support_apple-ios-macabi` | 287 | - | - | - |
| `rustc_platform-support_apple-tvos` | 348 | - | - | - |
| `rustc_platform-support_apple-visionos` | 182 | - | - | - |
| `rustc_platform-support_apple-watchos` | 200 | - | - | - |
| `rustc_platform-support_arm-linux` | 1,297 | - | - | - |
| `rustc_platform-support_arm-none-eabi` | 1,215 | - | - | - |
| `rustc_platform-support_arm64e-apple-darwin` | 131 | - | - | - |
| `rustc_platform-support_arm64e-apple-ios` | 117 | - | - | - |
| `rustc_platform-support_arm64e-apple-tvos` | 127 | - | - | - |
| `rustc_platform-support_arm64ec-pc-windows-msvc` | 409 | - | - | - |
| `rustc_platform-support_armeb-unknown-linux-gnueabi` | 353 | - | - | - |
| `rustc_platform-support_armebv7r-none-eabi` | 257 | - | - | - |
| `rustc_platform-support_armv4t-none-eabi` | 143 | - | - | - |
| `rustc_platform-support_armv5te-none-eabi` | 138 | - | - | - |
| `rustc_platform-support_armv5te-unknown-linux-gnueabi` | 89 | - | - | - |
| `rustc_platform-support_armv6-none-eabi` | 218 | - | - | - |
| `rustc_platform-support_armv6k-nintendo-3ds` | 636 | - | - | - |
| `rustc_platform-support_armv7-rtems-eabihf` | 336 | - | - | - |
| `rustc_platform-support_armv7-sony-vita-newlibeabihf` | 376 | - | - | - |
| `rustc_platform-support_armv7-unknown-linux-gnueabi` | 149 | - | - | - |
| `rustc_platform-support_armv7-unknown-linux-uclibceabi` | 710 | - | - | - |
| `rustc_platform-support_armv7-unknown-linux-uclibceabihf` | 264 | - | - | - |
| `rustc_platform-support_armv7a-none-eabi` | 396 | - | - | - |
| `rustc_platform-support_armv7r-none-eabi` | 478 | - | - | - |
| `rustc_platform-support_armv8r-none-eabihf` | 281 | - | - | - |
| `rustc_platform-support_avr-none` | 330 | - | - | - |
| `rustc_platform-support_bpf-unknown-none` | 627 | - | - | - |
| `rustc_platform-support_csky-unknown-linux-gnuabiv2` | 304 | - | - | - |
| `rustc_platform-support_esp-idf` | 197 | - | - | - |
| `rustc_platform-support_freebsd` | 239 | - | - | - |
| `rustc_platform-support_fuchsia` | 2,991 | - | - | - |
| `rustc_platform-support_helenos` | 536 | - | - | - |
| `rustc_platform-support_hermit` | 304 | - | - | - |
| `rustc_platform-support_hexagon-unknown-linux-musl` | 362 | - | - | - |
| `rustc_platform-support_hexagon-unknown-none-elf` | 854 | - | - | - |
| `rustc_platform-support_hexagon-unknown-qurt` | 567 | - | - | - |
| `rustc_platform-support_hurd` | 137 | - | - | - |
| `rustc_platform-support_hyperlight` | 288 | - | - | - |
| `rustc_platform-support_i686-apple-darwin` | 150 | - | - | - |
| `rustc_platform-support_illumos` | 202 | - | - | - |
| `rustc_platform-support_kmc-solid` | 231 | - | - | - |
| `rustc_platform-support_l4re` | 271 | - | - | - |
| `rustc_platform-support_loongarch-linux` | 594 | - | - | - |
| `rustc_platform-support_loongarch-none` | 546 | - | - | - |
| `rustc_platform-support_lynxos178` | 345 | - | - | - |
| `rustc_platform-support_m68k-unknown-linux-gnu` | 357 | - | - | - |
| `rustc_platform-support_m68k-unknown-none-elf` | 262 | - | - | - |
| `rustc_platform-support_managarm` | 125 | - | - | - |
| `rustc_platform-support_mips-mti-none-elf` | 113 | - | - | - |
| `rustc_platform-support_mips-release-6` | 789 | - | - | - |
| `rustc_platform-support_mips64-openwrt-linux-musl` | 132 | - | - | - |
| `rustc_platform-support_mips64-unknown-linux-muslabi64` | 149 | - | - | - |
| `rustc_platform-support_mipsel-sony-psx` | 133 | - | - | - |
| `rustc_platform-support_mipsel-unknown-linux-gnu` | 96 | - | - | - |
| `rustc_platform-support_motor` | 126 | - | - | - |
| `rustc_platform-support_netbsd` | 635 | - | - | - |
| `rustc_platform-support_nto-qnx` | 1,256 | - | - | - |
| `rustc_platform-support_nuttx` | 256 | - | - | - |
| `rustc_platform-support_nvptx64-nvidia-cuda` | 644 | - | - | - |
| `rustc_platform-support_oe-linux-gnu` | 140 | - | - | - |
| `rustc_platform-support_openbsd` | 219 | - | - | - |
| `rustc_platform-support_openharmony` | 434 | - | - | - |
| `rustc_platform-support_powerpc-unknown-linux-gnuspe` | 92 | - | - | - |
| `rustc_platform-support_powerpc-unknown-linux-muslspe` | 168 | - | - | - |
| `rustc_platform-support_powerpc64-sony-ps3` | 564 | - | - | - |
| `rustc_platform-support_powerpc64-unknown-linux-gnuelfv2` | 156 | - | - | - |
| `rustc_platform-support_powerpc64-unknown-linux-musl` | 158 | - | - | - |
| `rustc_platform-support_powerpc64le-unknown-linux-gnu` | 124 | - | - | - |
| `rustc_platform-support_powerpc64le-unknown-linux-musl` | 128 | - | - | - |
| `rustc_platform-support_redox` | 204 | - | - | - |
| `rustc_platform-support_riscv32-unknown-none-elf` | 248 | - | - | - |
| `rustc_platform-support_riscv32e-unknown-none-elf` | 122 | - | - | - |
| `rustc_platform-support_riscv32im-risc0-zkvm-elf` | 585 | - | - | - |
| `rustc_platform-support_riscv32imac-unknown-xous-elf` | 201 | - | - | - |
| `rustc_platform-support_riscv64-unknown-none-elf` | 245 | - | - | - |
| `rustc_platform-support_riscv64a23-unknown-linux-gnu` | 116 | - | - | - |
| `rustc_platform-support_riscv64gc-unknown-linux-gnu` | 368 | - | - | - |
| `rustc_platform-support_riscv64gc-unknown-linux-musl` | 141 | - | - | - |
| `rustc_platform-support_s390x-unknown-linux-gnu` | 442 | - | - | - |
| `rustc_platform-support_s390x-unknown-linux-musl` | 301 | - | - | - |
| `rustc_platform-support_s390x-unknown-none-softfloat` | 401 | - | - | - |
| `rustc_platform-support_solaris` | 98 | - | - | - |
| `rustc_platform-support_template` | 307 | - | - | - |
| `rustc_platform-support_thumbv6m-none-eabi` | 204 | - | - | - |
| `rustc_platform-support_thumbv7a-vex-v5` | 1,381 | - | - | - |
| `rustc_platform-support_thumbv7em-none-eabi` | 356 | - | - | - |
| `rustc_platform-support_thumbv7m-none-eabi` | 155 | - | - | - |
| `rustc_platform-support_thumbv8m.base-none-eabi` | 157 | - | - | - |
| `rustc_platform-support_thumbv8m.main-none-eabi` | 839 | - | - | - |
| `rustc_platform-support_trusty` | 198 | - | - | - |
| `rustc_platform-support_unikraft-linux-musl` | 302 | - | - | - |
| `rustc_platform-support_unknown-uefi` | 1,740 | - | - | - |
| `rustc_platform-support_uwp-windows-msvc` | 220 | - | - | - |
| `rustc_platform-support_vxworks` | 197 | - | - | - |
| `rustc_platform-support_wasm32-none-component` | 323 | - | - | - |
| `rustc_platform-support_wasm32-unknown-emscripten` | 861 | - | - | - |
| `rustc_platform-support_wasm32-unknown-unknown` | 1,673 | - | - | - |
| `rustc_platform-support_wasm32-wali-linux` | 565 | - | - | - |
| `rustc_platform-support_wasm32-wasip1` | 797 | - | - | - |
| `rustc_platform-support_wasm32-wasip1-threads` | 1,063 | - | - | - |
| `rustc_platform-support_wasm32-wasip2` | 285 | - | - | - |
| `rustc_platform-support_wasm32-wasip3` | 846 | - | - | - |
| `rustc_platform-support_wasm32v1-none` | 712 | - | - | - |
| `rustc_platform-support_wasm64-unknown-unknown` | 427 | - | - | - |
| `rustc_platform-support_win7-windows-gnu` | 166 | - | - | - |
| `rustc_platform-support_win7-windows-msvc` | 314 | - | - | - |
| `rustc_platform-support_windows-gnu` | 235 | - | - | - |
| `rustc_platform-support_windows-gnullvm` | 308 | - | - | - |
| `rustc_platform-support_windows-msvc` | 260 | - | - | - |
| `rustc_platform-support_x86_64-fortanix-unknown-sgx` | 273 | - | - | - |
| `rustc_platform-support_x86_64-pc-cygwin` | 178 | - | - | - |
| `rustc_platform-support_x86_64-unknown-linux-gnuasan` | 171 | - | - | - |
| `rustc_platform-support_x86_64-unknown-linux-gnumsan` | 171 | - | - | - |
| `rustc_platform-support_x86_64-unknown-linux-gnutsan` | 171 | - | - | - |
| `rustc_platform-support_x86_64-unknown-linux-none` | 194 | - | - | - |
| `rustc_platform-support_x86_64-unknown-none` | 431 | - | - | - |
| `rustc_platform-support_x86_64h-apple-darwin` | 304 | - | - | - |
| `rustc_platform-support_xtensa` | 88 | - | - | - |
| `rustc_profile-guided-optimization` | 1,762 | - | - | - |
| `rustc_remap-source-paths` | 597 | - | - | - |
| `rustc_symbol-mangling_index` | 269 | - | - | - |
| `rustc_symbol-mangling_v0` | 6,071 | - | - | - |
| `rustc_target-tier-policy` | 6,898 | - | - | - |
| `rustc_targets_built-in` | 92 | - | - | - |
| `rustc_targets_custom` | 289 | - | - | - |
| `rustc_targets_index` | 175 | - | - | - |
| `rustc_targets_known-issues` | 209 | - | - | - |
| `rustc_tests_index` | 1,590 | - | - | - |
| `rustc_what-is-rustc` | 283 | - | - | - |
| `rustdoc_advanced-features` | 766 | - | - | - |
| `rustdoc_command-line-arguments` | 2,194 | - | - | - |
| `rustdoc_deprecated-features` | 74 | - | - | - |
| `rustdoc_how-to-read-rustdoc` | 595 | - | - | - |
| `rustdoc_how-to-write-documentation` | 1,422 | - | - | - |
| `rustdoc_lints` | 1,390 | - | - | - |
| `rustdoc_read-documentation_in-doc-settings` | 385 | - | - | - |
| `rustdoc_read-documentation_search` | 1,920 | - | - | - |
| `rustdoc_references` | 64 | - | - | - |
| `rustdoc_scraped-examples` | 309 | - | - | - |
| `rustdoc_unstable-features` | 5,277 | - | - | - |
| `rustdoc_what-is-rustdoc` | 731 | - | - | - |
| `rustdoc_write-documentation_documentation-tests` | 2,982 | - | - | - |
| `rustdoc_write-documentation_linking-to-items-by-name` | 837 | - | - | - |
| `rustdoc_write-documentation_re-exports` | 776 | - | - | - |
| `rustdoc_write-documentation_the-doc-attribute` | 1,262 | - | - | - |
| `rustdoc_write-documentation_what-to-include` | 587 | - | - | - |
| `style-guide_advice` | 121 | - | - | - |
| `style-guide_cargo` | 525 | - | - | - |
| `style-guide_editions` | 334 | - | - | - |
| `style-guide_expressions` | 3,477 | - | - | - |
| `style-guide_items` | 2,022 | - | - | - |
| `style-guide_nightly` | 246 | - | - | - |
| `style-guide_principles` | 110 | - | - | - |
| `style-guide_readme` | 1,544 | - | - | - |
| `style-guide_statements` | 889 | - | - | - |
| `style-guide_types` | 338 | - | - | - |

## Not added in the last run

- `COMMIT`: File type (none) is not one ingest reads (it reads PDF, HTML, Markdown and plain text).
- `paths.tsv`: A spreadsheet is rows of data, not a document. Leave it out, or turn the rows into sentences yourself and say so in DECISIONS.md.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.

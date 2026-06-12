# Chapter 3 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter3/Chapter3Exercises.tex`
Source PDF: `Probability/Exercises/Chapter3/Chapter3Exercises.pdf`

This dataset turns the solved Chapter 3 exercises into retrieval-ready records, reusable method cards, and exercise-derived knowledge pieces.

## Files

- `chapter3_exercise_records.jsonl`: one record per solved exercise, including question, solution, knowledge used, and method tags.
- `chapter3_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter3_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter3_exercise_method_flashcards.tsv`: flashcard import file for method and new-knowledge cards.
- `chapter3_exercise_viki.md`: human-readable overview.

## Section Method Cards

### 3.1 - De Moivre-Laplace theorem, Stirling asymptotics, and binomial normal approximation

Solved exercise records: 4

Use Stirling's formula and product-log expansions to turn exact binomial or rare-event probabilities into normal or exponential limits.

Tags: stirling, binomial, product-limit, normal-approximation

Reusable knowledge: exercise_ch3_stirling_binomial_ratio_method, exercise_ch3_product_to_exponential_method, exercise_ch3_linear_deviation_not_clt

### 3.2 - Weak convergence, Portmanteau criteria, tightness, and continuous mapping

Solved exercise records: 17

Translate weak convergence into CDF continuity-point checks, bounded continuous test functions, open/closed set bounds, tightness, and continuous mappings.

Tags: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky

Reusable knowledge: exercise_ch3_buffer_events_for_weak_convergence, exercise_ch3_subsequence_principle_for_limits, exercise_ch3_tightness_by_tail_or_moment_bound, exercise_ch3_converging_together_slutsky_template

### 3.3 - Characteristic functions, inversion, moments, independence, and Levy continuity

Solved exercise records: 25

Identify distributions and limits through characteristic functions; use transform tables, Taylor expansions at zero, inversion, and factorization.

Tags: characteristic-functions, levy-continuity, moments, inversion, independence

Reusable knowledge: exercise_ch3_cf_table_matching, exercise_ch3_cf_taylor_moment_extraction, exercise_ch3_cf_factorization_independence, exercise_ch3_inversion_for_lattice_or_density

### 3.4 - Central limit theorems, triangular arrays, Lindeberg, and normal approximations

Solved exercise records: 13

Choose the correct normalization, verify Lindeberg or Lyapunov conditions, and reduce random-index or triangular-array sums to known CLT forms.

Tags: clt, lindeberg, lyapunov, triangular-array, random-sums

Reusable knowledge: exercise_ch3_lindeberg_truncation_check, exercise_ch3_lyapunov_shortcut, exercise_ch3_random_index_clt_template, exercise_ch3_poisson_or_multinomial_clt_scaling

### 3.5 - Local limit theorems and lattice-level normal approximation

Solved exercise records: 0

Use local limit theorem thinking when a problem asks for point probabilities or lattice-scale approximations rather than only distributional convergence.

Tags: local-limit, lattice, point-probability, normal-density

Reusable knowledge: exercise_ch3_local_limit_vs_global_clt, exercise_ch3_lattice_span_check

### 3.6 - Total variation, couplings, and maximal coupling construction

Solved exercise records: 1

Prove total variation bounds by coupling, and prove sharpness by constructing a maximal coupling from the common mass of two measures.

Tags: coupling, total-variation, maximal-coupling, discrete-measures

Reusable knowledge: exercise_ch3_coupling_bounds_total_variation, exercise_ch3_maximal_coupling_common_mass

### 3.7 - Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings

Solved exercise records: 9

Exploit exponential survival functions, Poisson thinning/splitting, and Dirichlet uniform spacings to solve process and occupancy limits.

Tags: poisson-process, exponential, thinning, splitting, uniform-spacings

Reusable knowledge: exercise_ch3_memoryless_survival_equation, exercise_ch3_competing_exponentials, exercise_ch3_poisson_thinning_for_infinite_server_queue, exercise_ch3_poisson_splitting_occupancy, exercise_ch3_dirichlet_uniform_spacings, exercise_ch3_extreme_spacing_second_moment

### 3.8 - Stable laws, heavy tails, positive stable laws, and subordination

Solved exercise records: 7

Read stable-law questions through scaling, regular variation, tail integrals, Laplace transforms, and conditioning on positive stable subordinators.

Tags: stable-laws, heavy-tails, regular-variation, laplace-transform, subordination

Reusable knowledge: exercise_ch3_stable_no_centering_alpha_less_than_one, exercise_ch3_borderline_normal_log_correction, exercise_ch3_stable_fractional_moment_tail_test, exercise_ch3_positive_stable_laplace_functional_equation, exercise_ch3_stable_subordination_product_rule

### 3.9 - Infinitely divisible distributions and Levy measures

Solved exercise records: 4

Use convolution roots, support diameter, symmetrized characteristic functions, and Levy-Khinchin exponent matching for infinite divisibility problems.

Tags: infinite-divisibility, gamma, levy-khinchin, characteristic-functions, support

Reusable knowledge: exercise_ch3_gamma_shape_splitting, exercise_ch3_bounded_infinitely_divisible_degenerate, exercise_ch3_infinitely_divisible_cf_nonvanishing, exercise_ch3_levy_measure_by_exponent_matching

### 3.10 - Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws

Solved exercise records: 8

Recover marginals by sending coordinates to infinity, build joint laws with copulas, and prove independence or normality by multivariate characteristic functions.

Tags: multivariate, marginals, copula, joint-characteristic-function, multivariate-normal

Reusable knowledge: exercise_ch3_marginals_from_joint_cdf, exercise_ch3_fgm_copula_density_check, exercise_ch3_mixed_partial_recovers_density, exercise_ch3_joint_cf_independence_factorization, exercise_ch3_multivariate_normal_diagonal_covariance, exercise_ch3_cramer_wold_normal_identification

## Exercise Records

- `3.1.1` (3.1): De Moivre-Laplace theorem, Stirling asymptotics, and binomial normal approximation
  - Methods: stirling, binomial, product-limit, normal-approximation
  - Knowledge used: durrett_ch3_product_exponential_limit; durrett_ch3_stirling_local_binomial
- `3.1.2` (3.1): De Moivre-Laplace theorem, Stirling asymptotics, and binomial normal approximation
  - Methods: stirling, binomial, product-limit, normal-approximation
  - Knowledge used: durrett_ch3_stirling_local_binomial; durrett_ch3_demoivre_laplace; durrett_ch3_normal_approximation_continuity_correction
- `3.1.3` (3.1): De Moivre-Laplace theorem, Stirling asymptotics, and binomial normal approximation
  - Methods: stirling, binomial, product-limit, normal-approximation
  - Knowledge used: durrett_ch3_stirling_local_binomial; durrett_ch3_large_deviation_stirling_patterns
- `3.1.4` (3.1): De Moivre-Laplace theorem, Stirling asymptotics, and binomial normal approximation
  - Methods: stirling, binomial, product-limit, normal-approximation
  - Knowledge used: durrett_ch3_stirling_local_binomial; durrett_ch3_large_deviation_stirling_patterns
- `3.2.1` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_weak_convergence_definition; durrett_ch3_bounded_continuous_test_functions; durrett_ch3_scheffe_theorem
- `3.2.2` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_weak_convergence_definition; durrett_ch3_continuous_mapping_theorem; durrett_ch3_product_exponential_limit
- `3.2.3` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_weak_convergence_definition; durrett_ch3_product_exponential_limit; durrett_ch3_converging_together_slutsky
- `3.2.4` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_skorokhod_quantile_representation; durrett_ch3_bounded_continuous_test_functions
- `3.2.5` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_bounded_continuous_test_functions; durrett_ch3_moment_tightness_criterion; durrett_ch3_skorokhod_quantile_representation
- `3.2.6` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_weak_convergence_definition; durrett_ch3_portmanteau_open_closed; durrett_ch3_helly_selection_tightness
- `3.2.7` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_weak_convergence_definition; durrett_ch3_convergence_in_probability_to_distribution
- `3.2.8` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_convergence_in_probability_to_distribution; durrett_ch3_weak_convergence_definition
- `3.2.9` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_weak_convergence_definition; durrett_ch3_portmanteau_open_closed
- `3.2.10` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_skorokhod_quantile_representation; durrett_ch3_weak_convergence_definition
- `3.2.11` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_weak_convergence_definition; durrett_ch3_portmanteau_open_closed; durrett_ch3_scheffe_theorem
- `3.2.12` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_convergence_in_probability_to_distribution; durrett_ch3_portmanteau_open_closed
- `3.2.13` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_converging_together_slutsky; durrett_ch3_convergence_in_probability_to_distribution; durrett_ch3_continuous_mapping_theorem
- `3.2.14` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_converging_together_slutsky; durrett_ch3_convergence_in_probability_to_distribution; durrett_ch3_continuous_mapping_theorem
- `3.2.15` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_converging_together_slutsky; durrett_ch3_continuous_mapping_theorem; durrett_ch3_iid_clt
- `3.2.16` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_convergence_in_probability_to_distribution; durrett_ch3_moment_tightness_criterion
- `3.2.17` (3.2): Weak convergence, Portmanteau criteria, tightness, and continuous mapping
  - Methods: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky
  - Knowledge used: durrett_ch3_moment_tightness_criterion; durrett_ch3_portmanteau_open_closed
- `3.3.1` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_characteristic_function_definition; durrett_ch3_cf_independent_sums
- `3.3.2` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_cf_inversion_formula; durrett_ch3_characteristic_function_definition
- `3.3.3` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_cf_independent_sums; durrett_ch3_cf_inversion_formula; durrett_ch2_joint_law_product_measure
- `3.3.4` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_standard_characteristic_functions; durrett_ch3_integrable_cf_density
- `3.3.5` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_standard_characteristic_functions; durrett_ch3_cf_independent_sums; durrett_ch3_integrable_cf_density
- `3.3.6` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_standard_characteristic_functions; durrett_ch3_cf_independent_sums; durrett_ch3_levy_continuity_theorem
- `3.3.7` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_standard_characteristic_functions; durrett_ch3_levy_continuity_theorem; durrett_ch3_subsequence_principle_weak
- `3.3.8` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_cf_independent_sums; durrett_ch3_levy_continuity_theorem
- `3.3.9` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_cf_independent_sums; durrett_ch3_convergence_in_probability_to_distribution; durrett_ch3_levy_continuity_theorem
- `3.3.10` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_standard_characteristic_functions; durrett_ch3_cf_independent_sums; durrett_ch3_levy_continuity_theorem
- `3.3.11` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_cf_independent_sums; durrett_ch3_characteristic_function_definition
- `3.3.12` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_derivatives_moments; durrett_ch3_standard_characteristic_functions
- `3.3.13` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_characteristic_function_definition; durrett_ch3_levy_continuity_theorem; durrett_ch3_moment_tightness_criterion
- `3.3.14` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_levy_continuity_theorem; durrett_ch3_characteristic_function_definition; durrett_ch3_convergence_in_probability_to_distribution
- `3.3.15` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_characteristic_function_definition; durrett_ch3_cf_inversion_formula
- `3.3.16` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_second_order_cf_expansion; durrett_ch3_derivatives_moments
- `3.3.17` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_levy_continuity_theorem; durrett_ch3_convergence_in_probability_to_distribution
- `3.3.18` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_levy_continuity_theorem; durrett_ch3_cf_independent_sums; durrett_ch3_convergence_in_probability_to_distribution
- `3.3.19` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_polya_criterion; durrett_ch3_characteristic_function_definition
- `3.3.20` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_cf_independent_sums; durrett_ch3_stable_characteristic_exponent; durrett_ch3_levy_continuity_theorem
- `3.3.21` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_characteristic_function_definition; durrett_ch3_standard_characteristic_functions; durrett_ch3_polya_criterion
- `3.3.22` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_cf_independent_sums; durrett_ch3_cf_inversion_formula; durrett_ch3_standard_characteristic_functions
- `3.3.23` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_cf_independent_sums; durrett_ch3_characteristic_function_definition; durrett_ch3_levy_continuity_theorem
- `3.3.24` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_moment_problem_carleman; durrett_ch3_moment_tightness_criterion
- `3.3.25` (3.3): Characteristic functions, inversion, moments, independence, and Levy continuity
  - Methods: characteristic-functions, levy-continuity, moments, inversion, independence
  - Knowledge used: durrett_ch3_moment_problem_carleman; durrett_ch3_derivatives_moments
- `3.4.1` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_iid_clt; durrett_ch3_normal_approximation_continuity_correction
- `3.4.2` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_iid_clt; durrett_ch3_convergence_in_probability_to_distribution; durrett_ch2_borel_cantelli_first
- `3.4.3` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_iid_clt; durrett_ch3_subsequence_principle_weak; durrett_ch3_triangular_array_lindeberg_feller
- `3.4.4` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_iid_clt; durrett_ch3_converging_together_slutsky; durrett_ch3_continuous_mapping_theorem
- `3.4.5` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_iid_clt; durrett_ch3_converging_together_slutsky; durrett_ch3_continuous_mapping_theorem
- `3.4.6` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_random_index_clt; durrett_ch3_iid_clt; durrett_ch3_converging_together_slutsky
- `3.4.7` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_random_index_clt; durrett_ch3_iid_clt; durrett_ch2_renewal_process
- `3.4.8` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_random_index_clt; durrett_ch3_iid_clt; durrett_ch2_kolmogorov_maximal_inequality
- `3.4.9` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_triangular_array_lindeberg_feller; durrett_ch3_iid_clt; durrett_ch3_converging_together_slutsky
- `3.4.10` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_triangular_array_lindeberg_feller; durrett_ch3_lyapunov_condition
- `3.4.11` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_triangular_array_lindeberg_feller; durrett_ch3_lyapunov_condition
- `3.4.12` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_lyapunov_condition; durrett_ch3_triangular_array_lindeberg_feller
- `3.4.13` (3.4): Central limit theorems, triangular arrays, Lindeberg, and normal approximations
  - Methods: clt, lindeberg, lyapunov, triangular-array, random-sums
  - Knowledge used: durrett_ch3_triangular_array_lindeberg_feller; durrett_ch3_levy_continuity_theorem; durrett_ch3_stable_law_domain_attraction
- `3.6.1` (3.6): Total variation, couplings, and maximal coupling construction
  - Methods: coupling, total-variation, maximal-coupling, discrete-measures
  - Knowledge used: durrett_ch3_total_variation_poisson_approximation; durrett_ch3_poisson_triangular_array; durrett_ch3_weak_convergence_definition
- `3.7.1` (3.7): Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings
  - Methods: poisson-process, exponential, thinning, splitting, uniform-spacings
  - Knowledge used: Lack-of-memory property, survival functions, monotone Cauchy equation,
exponential distribution.
- `3.7.2` (3.7): Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings
  - Methods: poisson-process, exponential, thinning, splitting, uniform-spacings
  - Knowledge used: Independence, exponential survival function, competing exponentials.
- `3.7.3` (3.7): Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings
  - Methods: poisson-process, exponential, thinning, splitting, uniform-spacings
  - Knowledge used: Minimum of independent exponentials, joint density, independence by
factorization.
- `3.7.4` (3.7): Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings
  - Methods: poisson-process, exponential, thinning, splitting, uniform-spacings
  - Knowledge used: Poisson thinning, superposition of independent Poisson variables,
tail-integral formula for the mean.
- `3.7.5` (3.7): Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings
  - Methods: poisson-process, exponential, thinning, splitting, uniform-spacings
  - Knowledge used: Poisson splitting, occupancy by Poissonization, independence of thinned
Poisson counts.
- `3.7.6` (3.7): Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings
  - Methods: poisson-process, exponential, thinning, splitting, uniform-spacings
  - Knowledge used: Uniform order statistics, binomial-to-Poisson convergence, Poisson
arrival times, gamma distribution.
- `3.7.7` (3.7): Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings
  - Methods: poisson-process, exponential, thinning, splitting, uniform-spacings
  - Knowledge used: Uniform spacings, Dirichlet spacing distribution, second-moment method,
Chebyshev's inequality.
- `3.7.8` (3.7): Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings
  - Methods: poisson-process, exponential, thinning, splitting, uniform-spacings
  - Knowledge used: Uniform spacings, union bound, second-moment method, extreme spacing
asymptotics.
- `3.7.9` (3.7): Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings
  - Methods: poisson-process, exponential, thinning, splitting, uniform-spacings
  - Knowledge used: Dirichlet distribution of uniform spacings, simplex volume ratios,
minimum spacing limit.
- `3.8.1` (3.8): Stable laws, heavy tails, positive stable laws, and subordination
  - Methods: stable-laws, heavy-tails, regular-variation, laplace-transform, subordination
  - Knowledge used: Stable limit theorem, regular variation, truncated means, Poisson
large-jump representation.
- `3.8.2` (3.8): Stable laws, heavy tails, positive stable laws, and subordination
  - Methods: stable-laws, heavy-tails, regular-variation, laplace-transform, subordination
  - Knowledge used: Central limit theorem, borderline normal attraction, heavy-tail tail
calculation.
- `3.8.3` (3.8): Stable laws, heavy tails, positive stable laws, and subordination
  - Methods: stable-laws, heavy-tails, regular-variation, laplace-transform, subordination
  - Knowledge used: One-sided stable laws, stable limit theorem, absence of centering for
$\alpha<1$.
- `3.8.4` (3.8): Stable laws, heavy tails, positive stable laws, and subordination
  - Methods: stable-laws, heavy-tails, regular-variation, laplace-transform, subordination
  - Knowledge used: Characteristic functions of symmetric stable laws, fractional moments,
stable tail lower bounds, tail-integral formula.
- `3.8.5` (3.8): Stable laws, heavy tails, positive stable laws, and subordination
  - Methods: stable-laws, heavy-tails, regular-variation, laplace-transform, subordination
  - Knowledge used: Stability, regular variation of normalizing constants, centering for
$\alpha<1$.
- `3.8.6` (3.8): Stable laws, heavy tails, positive stable laws, and subordination
  - Methods: stable-laws, heavy-tails, regular-variation, laplace-transform, subordination
  - Knowledge used: Laplace transforms, positive stable laws, stability scaling, continuity
functional equation.
- `3.8.7` (3.8): Stable laws, heavy tails, positive stable laws, and subordination
  - Methods: stable-laws, heavy-tails, regular-variation, laplace-transform, subordination
  - Knowledge used: Characteristic functions, subordination of stable laws, positive
one-half stable density, normal ratio representation of the Cauchy law.
- `3.9.1` (3.9): Infinitely divisible distributions and Levy measures
  - Methods: infinite-divisibility, gamma, levy-khinchin, characteristic-functions, support
  - Knowledge used: Gamma characteristic function, convolution of gamma laws, infinite
divisibility.
- `3.9.2` (3.9): Infinitely divisible distributions and Levy measures
  - Methods: infinite-divisibility, gamma, levy-khinchin, characteristic-functions, support
  - Knowledge used: Infinite divisibility, support of convolutions, variance additivity,
bounded support variance bound.
- `3.9.3` (3.9): Infinitely divisible distributions and Levy measures
  - Methods: infinite-divisibility, gamma, levy-khinchin, characteristic-functions, support
  - Knowledge used: Characteristic functions, symmetrization, infinite divisibility,
continuity theorem.
- `3.9.4` (3.9): Infinitely divisible distributions and Levy measures
  - Methods: infinite-divisibility, gamma, levy-khinchin, characteristic-functions, support
  - Knowledge used: Levy-Khinchin formula, symmetric Levy measures, characteristic exponent
matching.
- `3.10.1` (3.10): Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws
  - Methods: multivariate, marginals, copula, joint-characteristic-function, multivariate-normal
  - Knowledge used: Marginal distributions, continuity from below, multidimensional
distribution functions.
- `3.10.2` (3.10): Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws
  - Methods: multivariate, marginals, copula, joint-characteristic-function, multivariate-normal
  - Knowledge used: Copulas, Frechet construction, mixed derivatives, marginal recovery.
- `3.10.3` (3.10): Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws
  - Methods: multivariate, marginals, copula, joint-characteristic-function, multivariate-normal
  - Knowledge used: Joint density, distribution function, iterated integrals, fundamental
theorem of calculus.
- `3.10.4` (3.10): Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws
  - Methods: multivariate, marginals, copula, joint-characteristic-function, multivariate-normal
  - Knowledge used: Weak convergence in $\mathbb R^d$, coordinate projections, continuous
mapping theorem.
- `3.10.5` (3.10): Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws
  - Methods: multivariate, marginals, copula, joint-characteristic-function, multivariate-normal
  - Knowledge used: Multivariate characteristic functions, diagonal embeddings, uniqueness
of characteristic functions.
- `3.10.6` (3.10): Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws
  - Methods: multivariate, marginals, copula, joint-characteristic-function, multivariate-normal
  - Knowledge used: Characteristic functions, independence, product measures, uniqueness
theorem.
- `3.10.7` (3.10): Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws
  - Methods: multivariate, marginals, copula, joint-characteristic-function, multivariate-normal
  - Knowledge used: Multivariate normal characteristic function, covariance matrix,
independence criterion by characteristic functions.
- `3.10.8` (3.10): Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws
  - Methods: multivariate, marginals, copula, joint-characteristic-function, multivariate-normal
  - Knowledge used: Cramer-Wold viewpoint, linear combinations, multivariate normal
characteristic function, uniqueness theorem.

## New Exercise-Derived Knowledge

### Stirling method for binomial ratios

- ID: `exercise_ch3_stirling_binomial_ratio_method`
- Kind: calculation-template
- Summary: Insert Stirling's formula into factorial probabilities, simplify the polynomial prefactor, and exponentiate logarithmic expansions.
- Use case: Exercises in Section 3.1 involving De Moivre-Laplace or large binomial probabilities.
- Tags: stirling, binomial, asymptotics

### Convert rare-event products to exponentials

- ID: `exercise_ch3_product_to_exponential_method`
- Kind: limit-template
- Summary: For products of factors 1+a_{n,k}, take logs and use log(1+x)=x+o(x) when the maximum factor is small.
- Use case: Birthday, occupancy, no-collision, and geometric waiting-time limits.
- Tags: product-limit, rare-events, log-expansion

### Linear deviations require exponential-rate estimates

- ID: `exercise_ch3_linear_deviation_not_clt`
- Kind: warning
- Summary: When deviations are of order n rather than sqrt(n), normal approximation is usually wrong; use Stirling or large-deviation rates.
- Use case: Binomial or random-walk tail exercises before the large-deviation chapter.
- Tags: large-deviation, normal-approximation, scale

### Buffer events for weak convergence

- ID: `exercise_ch3_buffer_events_for_weak_convergence`
- Kind: proof-template
- Summary: Compare events such as {X_n <= x} with {X <= x +/- epsilon} to pass from convergence in probability to weak convergence.
- Use case: Exercises proving convergence in probability implies distributional convergence or converging-together results.
- Tags: weak-convergence, epsilon-buffer, cdf

### Subsequence principle for identifying limits

- ID: `exercise_ch3_subsequence_principle_for_limits`
- Kind: proof-template
- Summary: Show every subsequence has a further subsequence with the same limit; then the original sequence converges.
- Use case: Tightness and uniqueness arguments in weak convergence exercises.
- Tags: subsequence, tightness, uniqueness

### Tightness from tails or coercive moments

- ID: `exercise_ch3_tightness_by_tail_or_moment_bound`
- Kind: criterion
- Summary: Control sup_n P(|X_n|>K) directly or use Markov's inequality on a function growing to infinity.
- Use case: Weak convergence compactness exercises.
- Tags: tightness, markov, moment-bound

### Converging together and Slutsky template

- ID: `exercise_ch3_converging_together_slutsky_template`
- Kind: proof-template
- Summary: If a main term has a distributional limit and the error goes to zero in probability, use tightness and buffer events to keep the same limit.
- Use case: Exercises where a statistic is approximated by a simpler statistic.
- Tags: slutsky, negligible-error, weak-convergence

### Characteristic-function table matching

- ID: `exercise_ch3_cf_table_matching`
- Kind: calculation-template
- Summary: Recognize transforms such as normal, Cauchy, gamma, Poisson, and uniform; then invoke uniqueness.
- Use case: Distribution identification and transform inversion exercises in Section 3.3.
- Tags: characteristic-functions, transform-table, uniqueness

### Extract moments from characteristic-function Taylor terms

- ID: `exercise_ch3_cf_taylor_moment_extraction`
- Kind: calculation-template
- Summary: Differentiate the characteristic function at zero or compare its Taylor expansion with 1+it EX - t^2 E X^2/2 + ... .
- Use case: Moment and variance calculations from transforms.
- Tags: moments, taylor-expansion, characteristic-functions

### Independence through characteristic-function factorization

- ID: `exercise_ch3_cf_factorization_independence`
- Kind: proof-template
- Summary: A joint characteristic function that factors into marginal characteristic functions identifies the product law.
- Use case: Exercises proving independence from transforms.
- Tags: independence, joint-law, characteristic-functions

### Use inversion to recover probabilities or densities

- ID: `exercise_ch3_inversion_for_lattice_or_density`
- Kind: calculation-template
- Summary: Apply the inversion formula in the form appropriate to densities or lattice probabilities, checking integrability when needed.
- Use case: Characteristic-function inversion exercises.
- Tags: inversion, density, lattice

### Lindeberg check by truncation

- ID: `exercise_ch3_lindeberg_truncation_check`
- Kind: proof-template
- Summary: Bound the contribution of terms exceeding epsilon times the row standard deviation; bounded or uniformly small terms often make the condition immediate.
- Use case: Triangular-array CLT exercises.
- Tags: lindeberg, triangular-array, truncation

### Lyapunov condition as a shortcut to Lindeberg

- ID: `exercise_ch3_lyapunov_shortcut`
- Kind: criterion
- Summary: Verify a higher-moment bound divided by the row variance scale; Lyapunov implies Lindeberg.
- Use case: CLT exercises with available third or higher moments.
- Tags: lyapunov, clt, moments

### Random-index CLT template

- ID: `exercise_ch3_random_index_clt_template`
- Kind: proof-template
- Summary: Condition on the random index or compare it to a deterministic equivalent, then use Slutsky once the index ratio converges.
- Use case: Random sums and stopped-sum CLT exercises.
- Tags: random-index, clt, slutsky

### Poisson and multinomial CLT scaling

- ID: `exercise_ch3_poisson_or_multinomial_clt_scaling`
- Kind: calculation-template
- Summary: Center counts by their means and scale by square roots of variances; dependence in multinomial vectors appears through covariance constraints.
- Use case: Occupancy, count-vector, and Poisson approximation CLT exercises.
- Tags: poisson, multinomial, normal-approximation

### Local limit versus global CLT

- ID: `exercise_ch3_local_limit_vs_global_clt`
- Kind: warning
- Summary: The CLT controls interval probabilities, while a local limit theorem controls individual lattice probabilities at the normal-density scale.
- Use case: Point probability approximations in Section 3.5.
- Tags: local-limit, clt, lattice

### Check lattice span before using a local limit theorem

- ID: `exercise_ch3_lattice_span_check`
- Kind: warning
- Summary: For lattice variables, the correct local approximation includes the span and only applies on reachable lattice points.
- Use case: Local normal approximations for sums of integer-valued variables.
- Tags: lattice, span, local-limit

### Any coupling bounds total variation

- ID: `exercise_ch3_coupling_bounds_total_variation`
- Kind: proof-template
- Summary: For every event A, |P(X in A)-P(Y in A)| is bounded by P(X != Y), so total variation is no larger than mismatch probability.
- Use case: Exercise 3.6.1 and coupling estimates.
- Tags: coupling, total-variation, mismatch

### Maximal coupling by common mass

- ID: `exercise_ch3_maximal_coupling_common_mass`
- Kind: construction-template
- Summary: Couple two discrete laws by first sampling from their overlap min(mu,nu), then sample residuals on disjoint supports.
- Use case: Sharp total variation coupling results.
- Tags: maximal-coupling, common-mass, discrete-law

### Memoryless survival equation

- ID: `exercise_ch3_memoryless_survival_equation`
- Kind: proof-template
- Summary: The lack-of-memory property gives G(s+t)=G(s)G(t); monotonicity and right-continuity force G(t)=exp(-lambda t).
- Use case: Exercise 3.7.1 and exponential waiting-time characterization.
- Tags: memoryless, exponential, survival-function

### Competing exponentials race rule

- ID: `exercise_ch3_competing_exponentials`
- Kind: calculation-template
- Summary: The minimum of independent exponentials has rate equal to the sum of rates, and the winning index has probability proportional to its rate.
- Use case: Exercises 3.7.2 and 3.7.3.
- Tags: exponential, minimum, race

### Infinite-server queue by Poisson thinning

- ID: `exercise_ch3_poisson_thinning_for_infinite_server_queue`
- Kind: calculation-template
- Summary: Calls of age r survive with probability 1-G(r); thinning and superposition give a Poisson number in service with mean lambda integral survival.
- Use case: Exercise 3.7.4.
- Tags: poisson-thinning, queue, tail-integral

### Poisson splitting for occupancy

- ID: `exercise_ch3_poisson_splitting_occupancy`
- Kind: calculation-template
- Summary: A Poisson number of independent categorized observations splits into independent Poisson counts in each category.
- Use case: Exercise 3.7.5 and birthday/occupancy computations.
- Tags: poisson-splitting, occupancy, independence

### Uniform spacings are Dirichlet

- ID: `exercise_ch3_dirichlet_uniform_spacings`
- Kind: distribution-fact
- Summary: The gaps between ordered uniform points, including endpoints, are exchangeable Dirichlet(1,...,1) spacings.
- Use case: Exercises 3.7.7 through 3.7.9.
- Tags: uniform-order-statistics, spacings, dirichlet

### Extreme spacings by first and second moments

- ID: `exercise_ch3_extreme_spacing_second_moment`
- Kind: proof-template
- Summary: Count gaps above a threshold, compute one- and two-gap probabilities from simplex volumes, and use variance control.
- Use case: Largest and smallest uniform spacing limits.
- Tags: extreme-spacing, second-moment, simplex-volume

### No centering for alpha less than one stable limits

- ID: `exercise_ch3_stable_no_centering_alpha_less_than_one`
- Kind: stable-law-fact
- Summary: For alpha<1, small jumps are summable in absolute value under the Levy measure, so the stable limit needs no compensating centering.
- Use case: Exercises 3.8.1, 3.8.3, and 3.8.5.
- Tags: stable-laws, centering, alpha-less-than-one

### Borderline normal attraction has sqrt(n log n) scale

- ID: `exercise_ch3_borderline_normal_log_correction`
- Kind: limit-template
- Summary: A symmetric variable with tail P(|Z|>x) like x^{-2} has infinite variance but still lies in the normal domain with a logarithmic variance correction.
- Use case: Exercise 3.8.2 with p=1/2.
- Tags: normal-attraction, infinite-variance, log-correction

### Stable fractional moment and tail test

- ID: `exercise_ch3_stable_fractional_moment_tail_test`
- Kind: calculation-template
- Summary: Use the integral representation of E|X|^p through 1-Re phi(t) to get finiteness for p<alpha and tail lower bounds to show E|X|^alpha diverges.
- Use case: Exercise 3.8.4.
- Tags: stable-laws, fractional-moments, tails

### Positive stable Laplace functional equation

- ID: `exercise_ch3_positive_stable_laplace_functional_equation`
- Kind: proof-template
- Summary: Stability gives psi(lambda)^n=psi(n^{1/alpha}lambda); continuity turns this into psi(lambda)=exp(-c lambda^alpha).
- Use case: Exercise 3.8.6.
- Tags: positive-stable, laplace-transform, functional-equation

### Stable subordination product rule

- ID: `exercise_ch3_stable_subordination_product_rule`
- Kind: calculation-template
- Summary: Condition on a positive beta-stable Y: E exp(it X Y^{1/alpha}) becomes the Laplace transform of Y at c|t|^alpha, giving index alpha beta.
- Use case: Exercise 3.8.7 and normal-ratio Cauchy derivations.
- Tags: subordination, stable-laws, cauchy

### Gamma infinite divisibility by shape splitting

- ID: `exercise_ch3_gamma_shape_splitting`
- Kind: calculation-template
- Summary: A Gamma(a,lambda) characteristic function is the nth power of the Gamma(a/n,lambda) characteristic function.
- Use case: Exercise 3.9.1.
- Tags: gamma, infinite-divisibility, convolution

### Bounded infinitely divisible laws are degenerate

- ID: `exercise_ch3_bounded_infinitely_divisible_degenerate`
- Kind: proof-template
- Summary: If a bounded law is an n-fold convolution, the summand support diameter is at most 1/n of the total diameter, forcing variance to zero.
- Use case: Exercise 3.9.2.
- Tags: infinite-divisibility, bounded-support, variance

### Infinitely divisible characteristic functions do not vanish

- ID: `exercise_ch3_infinitely_divisible_cf_nonvanishing`
- Kind: proof-template
- Summary: Symmetrize to |phi|^2, take nth convolution roots, and use continuity near zero to contradict a zero at a fixed point.
- Use case: Exercise 3.9.3.
- Tags: characteristic-functions, infinite-divisibility, nonvanishing

### Find Levy measures by matching exponents

- ID: `exercise_ch3_levy_measure_by_exponent_matching`
- Kind: calculation-template
- Summary: Compare the log characteristic function with the Levy-Khinchin integral; symmetry cancels imaginary compensation terms.
- Use case: Exercise 3.9.4.
- Tags: levy-measure, levy-khinchin, symmetric-law

### Recover marginals from a joint CDF

- ID: `exercise_ch3_marginals_from_joint_cdf`
- Kind: definition-use
- Summary: Send all non-target coordinates to infinity and use continuity from below to recover the target coordinate's distribution function.
- Use case: Exercise 3.10.1.
- Tags: marginals, joint-cdf, continuity-from-below

### FGM-type copula density check

- ID: `exercise_ch3_fgm_copula_density_check`
- Kind: construction-template
- Summary: For C(u)=prod u_i + alpha prod u_i(1-u_i), the mixed derivative is 1+alpha prod(1-2u_i), nonnegative for |alpha|<=1.
- Use case: Exercise 3.10.2.
- Tags: copula, joint-distribution, density-check

### Mixed partial derivative recovers joint density

- ID: `exercise_ch3_mixed_partial_recovers_density`
- Kind: calculation-template
- Summary: Write the CDF as an iterated integral of the density and apply the fundamental theorem of calculus successively.
- Use case: Exercise 3.10.3.
- Tags: joint-density, cdf, mixed-partial

### Joint characteristic function factorization

- ID: `exercise_ch3_joint_cf_independence_factorization`
- Kind: proof-template
- Summary: Independence gives product transforms; conversely, a product joint characteristic function matches the product law by uniqueness.
- Use case: Exercise 3.10.6.
- Tags: independence, joint-characteristic-function, uniqueness

### Diagonal covariance gives independent normal coordinates

- ID: `exercise_ch3_multivariate_normal_diagonal_covariance`
- Kind: normal-law-fact
- Summary: For a multivariate normal vector, a diagonal covariance matrix makes the characteristic function factor into one-dimensional normal transforms.
- Use case: Exercise 3.10.7.
- Tags: multivariate-normal, covariance, independence

### Identify multivariate normal laws by all linear combinations

- ID: `exercise_ch3_cramer_wold_normal_identification`
- Kind: proof-template
- Summary: If every t dot X is normal with the right mean and variance, then the joint characteristic function is the multivariate normal transform.
- Use case: Exercise 3.10.8.
- Tags: cramer-wold, multivariate-normal, characteristic-functions

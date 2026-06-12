# Chapter 4 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter4/Chapter4Exercises.tex`
Source PDF: `Probability/Exercises/Chapter4/Chapter4Exercises.pdf`

This dataset turns the solved Chapter 4 exercises into retrieval-ready records, reusable method cards, and exercise-derived knowledge pieces.

## Files

- `chapter4_exercise_records.jsonl`: one record per solved exercise, including question, solution, knowledge used, and method tags.
- `chapter4_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter4_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter4_exercise_method_flashcards.tsv`: flashcard import file for method and new-knowledge cards.
- `chapter4_exercise_viki.md`: human-readable overview.

## Section Method Cards

### 4.1 - Conditional expectation, conditioning identities, and L2 projection

Solved exercise records: 10

Compute conditional expectations by testing against the conditioning sigma-field, then use projection, Jensen, conditioning on partitions, and variance decomposition to simplify identities.

Tags: conditional-expectation, projection, jensen, variance-decomposition

Reusable knowledge: exercise_ch4_conditional_bayes_by_indicator, exercise_ch4_conditional_inequality_from_pointwise_bound, exercise_ch4_l2_projection_pythagorean_conditioning, exercise_ch4_total_variance_random_sum, exercise_ch4_distribution_preserving_conditional_expectation

### 4.2 - Martingales, submartingales, supermartingales, transforms, and upcrossings

Solved exercise records: 10

Check martingale type by conditioning one step ahead; use predictable transforms, stopped processes, upcrossing counts, and product decompositions to prove convergence or construct examples.

Tags: martingale, predictable-transform, stopping, upcrossing, convergence

Reusable knowledge: exercise_ch4_natural_filtration_martingale_reduction, exercise_ch4_deterministic_submartingale_square_supermartingale, exercise_ch4_stopped_upcrossing_localization, exercise_ch4_product_martingale_limit_zero, exercise_ch4_dubins_upcrossing_switching

### 4.3 - Examples of martingales, likelihood-ratio martingales, and branching processes

Solved exercise records: 13

Use concrete martingale examples to isolate hypotheses: likelihood-ratio processes give martingales, additive error bounds give convergence, and branching recursions reduce to fixed-point equations.

Tags: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample

Reusable knowledge: exercise_ch4_bounded_increment_nonmartingale_counterexample, exercise_ch4_additive_error_supermartingale_convergence, exercise_ch4_partition_rn_derivative_martingale, exercise_ch4_bernoulli_product_hellinger_criterion, exercise_ch4_branching_fixed_point_extinction

### 4.4 - Doob inequalities, optional sampling, maximal bounds, and martingale SLLN

Solved exercise records: 11

Apply optional sampling and Doob inequalities to stopped martingales; combine orthogonal increments, quadratic martingales, and Kronecker normalization for L2 and strong-law estimates.

Tags: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law

Reusable knowledge: exercise_ch4_optional_sampling_between_stopping_times, exercise_ch4_doob_l1_log_maximal_bound, exercise_ch4_stopped_quadratic_martingale_exit_bound, exercise_ch4_martingale_increment_orthogonality_sum, exercise_ch4_kronecker_martingale_normalization

### 4.6 - Uniform integrability, Levy theorems, posterior limits, and martingale convergence

Solved exercise records: 7

Recognize when convergence is upgraded by uniform integrability; use Levy upward and zero-one laws to turn conditioning on growing sigma-fields into posterior consistency or absorbing-state conclusions.

Tags: uniform-integrability, levy-upward, zero-one-law, posterior-consistency, bounded-martingale

Reusable knowledge: exercise_ch4_posterior_consistency_by_levy_upward, exercise_ch4_dyadic_conditional_expectation_approximation, exercise_ch4_levy_zero_one_absorption_or_escape, exercise_ch4_bounded_martingale_binary_limit

### 4.7 - Backward martingales, exchangeability, and U-statistic limits

Solved exercise records: 5

Use backward martingale convergence for tail-like sigma-fields, then exploit exchangeability to replace conditional laws by finite-population hypergeometric formulas.

Tags: backward-martingale, exchangeability, hypergeometric, u-statistic, covariance

Reusable knowledge: exercise_ch4_backward_lp_convergence_ui, exercise_ch4_backward_conditional_dct, exercise_ch4_exchangeable_hypergeometric_conditioning, exercise_ch4_exchangeable_pair_covariance_positive, exercise_ch4_u_statistic_pair_square_limit

### 4.8 - Optional stopping applications, Wald identities, random walks, and ruin estimates

Solved exercise records: 11

Choose a martingale matched to the target functional, stop it at bounded levels, justify optional stopping, and pass limits to obtain hitting probabilities, Wald identities, and ruin bounds.

Tags: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale

Reusable knowledge: exercise_ch4_optional_stopping_ui_conditional_form, exercise_ch4_supermartingale_maximal_bound, exercise_ch4_wald_second_equation_stopped_l2, exercise_ch4_gambler_ruin_variance_generation, exercise_ch4_exponential_martingale_ruin_adjustment, exercise_ch4_fourth_moment_exit_time

### 4.9 - Renewal equations and generating functions for random-walk return times

Solved exercise records: 1

Encode first-return decompositions as renewal equations and solve them with generating functions; singular behavior at one reveals recurrence and return-time means.

Tags: renewal-equation, generating-functions, return-time, random-walk

Reusable knowledge: exercise_ch4_return_time_renewal_generating_function

## Exercise Records

- `4.1.1` (4.1): Conditional expectation, conditioning identities, and L2 projection
  - Methods: conditional-expectation, projection, jensen, variance-decomposition
  - Knowledge used: durrett_ch4_conditional_expectation_definition; durrett_ch4_partition_conditioning_formula; durrett_ch4_conditional_expectation_properties
- `4.1.2` (4.1): Conditional expectation, conditioning identities, and L2 projection
  - Methods: conditional-expectation, projection, jensen, variance-decomposition
  - Knowledge used: durrett_ch4_conditional_expectation_definition; durrett_ch4_conditional_expectation_properties
- `4.1.3` (4.1): Conditional expectation, conditioning identities, and L2 projection
  - Methods: conditional-expectation, projection, jensen, variance-decomposition
  - Knowledge used: durrett_ch4_conditional_expectation_properties; durrett_ch4_taking_out_what_is_known; durrett_ch4_conditional_expectation_l2_projection
- `4.1.4` (4.1): Conditional expectation, conditioning identities, and L2 projection
  - Methods: conditional-expectation, projection, jensen, variance-decomposition
  - Knowledge used: durrett_ch4_regular_conditional_distribution; durrett_ch4_conditional_expectation_definition; durrett_ch4_conditional_expectation_properties
- `4.1.5` (4.1): Conditional expectation, conditioning identities, and L2 projection
  - Methods: conditional-expectation, projection, jensen, variance-decomposition
  - Knowledge used: durrett_ch4_partition_conditioning_formula; durrett_ch4_tower_property_smaller_sigma_field_wins
- `4.1.6` (4.1): Conditional expectation, conditioning identities, and L2 projection
  - Methods: conditional-expectation, projection, jensen, variance-decomposition
  - Knowledge used: durrett_ch4_conditional_expectation_l2_projection; durrett_ch4_taking_out_what_is_known; durrett_ch4_tower_property_smaller_sigma_field_wins
- `4.1.7` (4.1): Conditional expectation, conditioning identities, and L2 projection
  - Methods: conditional-expectation, projection, jensen, variance-decomposition
  - Knowledge used: durrett_ch4_conditional_expectation_properties; durrett_ch4_conditional_expectation_l2_projection
- `4.1.8` (4.1): Conditional expectation, conditioning identities, and L2 projection
  - Methods: conditional-expectation, projection, jensen, variance-decomposition
  - Knowledge used: durrett_ch4_independent_conditioning_rule; durrett_ch4_conditional_expectation_properties; durrett_ch4_tower_property_smaller_sigma_field_wins; durrett_ch4_conditional_expectation_l2_projection
- `4.1.9` (4.1): Conditional expectation, conditioning identities, and L2 projection
  - Methods: conditional-expectation, projection, jensen, variance-decomposition
  - Knowledge used: durrett_ch4_conditional_expectation_l2_projection; durrett_ch4_taking_out_what_is_known; durrett_ch4_conditional_expectation_properties
- `4.1.10` (4.1): Conditional expectation, conditioning identities, and L2 projection
  - Methods: conditional-expectation, projection, jensen, variance-decomposition
  - Knowledge used: durrett_ch4_conditional_expectation_properties; durrett_ch4_conditional_jensen_contraction; durrett_ch4_taking_out_what_is_known
- `4.2.1` (4.2): Martingales, submartingales, supermartingales, transforms, and upcrossings
  - Methods: martingale, predictable-transform, stopping, upcrossing, convergence
  - Knowledge used: durrett_ch4_martingale_definition; durrett_ch4_tower_property_smaller_sigma_field_wins; durrett_ch4_multi_step_martingale_property
- `4.2.2` (4.2): Martingales, submartingales, supermartingales, transforms, and upcrossings
  - Methods: martingale, predictable-transform, stopping, upcrossing, convergence
  - Knowledge used: durrett_ch4_martingale_definition; durrett_ch4_conditional_expectation_properties
- `4.2.3` (4.2): Martingales, submartingales, supermartingales, transforms, and upcrossings
  - Methods: martingale, predictable-transform, stopping, upcrossing, convergence
  - Knowledge used: durrett_ch4_martingale_definition; durrett_ch4_conditional_expectation_properties; durrett_ch4_convex_transform_submartingale
- `4.2.4` (4.2): Martingales, submartingales, supermartingales, transforms, and upcrossings
  - Methods: martingale, predictable-transform, stopping, upcrossing, convergence
  - Knowledge used: durrett_ch4_stopped_process_supermartingale; durrett_ch4_upcrossing_inequality; durrett_ch4_martingale_convergence_theorem
- `4.2.5` (4.2): Martingales, submartingales, supermartingales, transforms, and upcrossings
  - Methods: martingale, predictable-transform, stopping, upcrossing, convergence
  - Knowledge used: durrett_ch4_martingale_definition; durrett_ch4_random_walk_martingales
- `4.2.6` (4.2): Martingales, submartingales, supermartingales, transforms, and upcrossings
  - Methods: martingale, predictable-transform, stopping, upcrossing, convergence
  - Knowledge used: durrett_ch4_random_walk_martingales; durrett_ch4_nonnegative_supermartingale_convergence; durrett_ch4_martingale_convergence_theorem
- `4.2.7` (4.2): Martingales, submartingales, supermartingales, transforms, and upcrossings
  - Methods: martingale, predictable-transform, stopping, upcrossing, convergence
  - Knowledge used: durrett_ch4_nonnegative_supermartingale_convergence
- `4.2.8` (4.2): Martingales, submartingales, supermartingales, transforms, and upcrossings
  - Methods: martingale, predictable-transform, stopping, upcrossing, convergence
  - Knowledge used: durrett_ch4_taking_out_what_is_known; durrett_ch4_nonnegative_supermartingale_convergence; durrett_ch4_martingale_definition
- `4.2.9` (4.2): Martingales, submartingales, supermartingales, transforms, and upcrossings
  - Methods: martingale, predictable-transform, stopping, upcrossing, convergence
  - Knowledge used: durrett_ch4_martingale_definition; durrett_ch4_taking_out_what_is_known; durrett_ch4_stopped_process_supermartingale
- `4.2.10` (4.2): Martingales, submartingales, supermartingales, transforms, and upcrossings
  - Methods: martingale, predictable-transform, stopping, upcrossing, convergence
  - Knowledge used: durrett_ch4_nonnegative_supermartingale_convergence; durrett_ch4_upcrossing_inequality; durrett_ch4_martingale_transform_no_gambling_system; durrett_ch4_stopped_process_supermartingale
- `4.3.1` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_bounded_increment_convergence; durrett_ch4_martingale_convergence_theorem
- `4.3.2` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_bounded_increment_convergence; durrett_ch4_martingale_convergence_theorem
- `4.3.3` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_martingale_definition; durrett_ch4_stopped_process_supermartingale; durrett_ch4_nonnegative_supermartingale_convergence
- `4.3.4` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_conditional_borel_cantelli; durrett_ch4_nonnegative_supermartingale_convergence
- `4.3.5` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_conditional_borel_cantelli; durrett_ch4_conditional_expectation_definition
- `4.3.6` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_radon_nikodym_derivative_martingale; durrett_ch4_conditional_expectation_definition; durrett_ch4_partition_conditioning_formula
- `4.3.7` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_radon_nikodym_derivative_martingale; durrett_ch4_nonnegative_supermartingale_convergence; durrett_ch4_conditional_expectation_definition
- `4.3.8` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_radon_nikodym_derivative_martingale; durrett_ch4_conditional_jensen_contraction
- `4.3.9` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_conditional_borel_cantelli; durrett_ch4_radon_nikodym_derivative_martingale
- `4.3.10` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_radon_nikodym_derivative_martingale; durrett_ch4_conditional_jensen_contraction
- `4.3.11` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_branching_process_normalized_martingale; durrett_ch4_nonnegative_supermartingale_convergence
- `4.3.12` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_branching_process_normalized_martingale; durrett_ch4_nonnegative_supermartingale_convergence; durrett_ch4_tower_property_smaller_sigma_field_wins
- `4.3.13` (4.3): Examples of martingales, likelihood-ratio martingales, and branching processes
  - Methods: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample
  - Knowledge used: durrett_ch4_branching_process_normalized_martingale
- `4.4.1` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_bounded_stopping_submartingale_expectation; durrett_ch4_multi_step_martingale_property; durrett_ch4_tower_property_smaller_sigma_field_wins
- `4.4.2` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_bounded_stopping_submartingale_expectation; durrett_ch4_stopped_process_supermartingale; durrett_ch4_martingale_transform_no_gambling_system
- `4.4.3` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_stopped_process_supermartingale; durrett_ch4_bounded_stopping_submartingale_expectation
- `4.4.4` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_bounded_stopping_submartingale_expectation; durrett_ch4_conditional_expectation_definition; durrett_ch4_stopped_process_supermartingale
- `4.4.5` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_conditional_expectation_l2_projection; durrett_ch4_tower_property_smaller_sigma_field_wins; durrett_ch4_taking_out_what_is_known
- `4.4.6` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_random_walk_martingales; durrett_ch4_bounded_stopping_submartingale_expectation; durrett_ch4_conditional_variance_formula_martingales
- `4.4.7` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_doob_maximal_inequality; durrett_ch4_convex_transform_submartingale; durrett_ch4_orthogonal_martingale_increments
- `4.4.8` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_doob_maximal_inequality; durrett_ch4_conditional_expectation_properties
- `4.4.9` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_orthogonal_martingale_increments; durrett_ch4_conditional_variance_formula_martingales
- `4.4.10` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_orthogonal_martingale_increments; durrett_ch4_lp_martingale_convergence; durrett_ch4_conditional_variance_formula_martingales
- `4.4.11` (4.4): Doob inequalities, optional sampling, maximal bounds, and martingale SLLN
  - Methods: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law
  - Knowledge used: durrett_ch4_orthogonal_martingale_increments; durrett_ch4_lp_martingale_convergence; durrett_ch4_martingale_strong_law_from_variances
- `4.6.1` (4.6): Uniform integrability, Levy theorems, posterior limits, and martingale convergence
  - Methods: uniform-integrability, levy-upward, zero-one-law, posterior-consistency, bounded-martingale
  - Knowledge used: durrett_ch4_levy_upward_theorem; durrett_ch4_closed_martingales_ui_equivalence; durrett_ch4_slln_via_backward_martingales
- `4.6.2` (4.6): Uniform integrability, Levy theorems, posterior limits, and martingale convergence
  - Methods: uniform-integrability, levy-upward, zero-one-law, posterior-consistency, bounded-martingale
  - Knowledge used: durrett_ch4_martingale_definition; durrett_ch4_closed_martingales_ui_equivalence; durrett_ch4_levy_upward_theorem
- `4.6.3` (4.6): Uniform integrability, Levy theorems, posterior limits, and martingale convergence
  - Methods: uniform-integrability, levy-upward, zero-one-law, posterior-consistency, bounded-martingale
  - Knowledge used: durrett_ch4_levy_upward_theorem; durrett_ch4_partition_conditioning_formula; durrett_ch4_ui_plus_probability_equals_l1
- `4.6.4` (4.6): Uniform integrability, Levy theorems, posterior limits, and martingale convergence
  - Methods: uniform-integrability, levy-upward, zero-one-law, posterior-consistency, bounded-martingale
  - Knowledge used: durrett_ch4_levy_zero_one_law; durrett_ch4_levy_upward_theorem; durrett_ch4_conditional_expectation_definition
- `4.6.5` (4.6): Uniform integrability, Levy theorems, posterior limits, and martingale convergence
  - Methods: uniform-integrability, levy-upward, zero-one-law, posterior-consistency, bounded-martingale
  - Knowledge used: durrett_ch4_branching_process_normalized_martingale; durrett_ch4_levy_zero_one_law
- `4.6.6` (4.6): Uniform integrability, Levy theorems, posterior limits, and martingale convergence
  - Methods: uniform-integrability, levy-upward, zero-one-law, posterior-consistency, bounded-martingale
  - Knowledge used: durrett_ch4_martingale_definition; durrett_ch4_closed_martingales_ui_equivalence; durrett_ch4_conditional_variance_formula_martingales
- `4.6.7` (4.6): Uniform integrability, Levy theorems, posterior limits, and martingale convergence
  - Methods: uniform-integrability, levy-upward, zero-one-law, posterior-consistency, bounded-martingale
  - Knowledge used: durrett_ch4_levy_upward_theorem; durrett_ch4_conditional_jensen_contraction; durrett_ch4_ui_plus_probability_equals_l1
- `4.7.1` (4.7): Backward martingales, exchangeability, and U-statistic limits
  - Methods: backward-martingale, exchangeability, hypergeometric, u-statistic, covariance
  - Knowledge used: durrett_ch4_backward_martingale_convergence; durrett_ch4_levy_downward_theorem; durrett_ch4_conditional_jensen_contraction; durrett_ch4_uniform_integrability_definition
- `4.7.2` (4.7): Backward martingales, exchangeability, and U-statistic limits
  - Methods: backward-martingale, exchangeability, hypergeometric, u-statistic, covariance
  - Knowledge used: durrett_ch4_levy_downward_theorem; durrett_ch4_conditional_expectation_properties; durrett_ch4_conditional_jensen_contraction
- `4.7.3` (4.7): Backward martingales, exchangeability, and U-statistic limits
  - Methods: backward-martingale, exchangeability, hypergeometric, u-statistic, covariance
  - Knowledge used: durrett_ch4_definetti_theorem; durrett_ch4_backward_martingale_convergence
- `4.7.4` (4.7): Backward martingales, exchangeability, and U-statistic limits
  - Methods: backward-martingale, exchangeability, hypergeometric, u-statistic, covariance
  - Knowledge used: durrett_ch4_definetti_theorem; durrett_ch4_orthogonal_martingale_increments
- `4.7.5` (4.7): Backward martingales, exchangeability, and U-statistic limits
  - Methods: backward-martingale, exchangeability, hypergeometric, u-statistic, covariance
  - Knowledge used: durrett_ch4_backward_martingale_convergence; durrett_ch4_slln_via_backward_martingales; durrett_ch4_hewitt_savage_zero_one
- `4.8.1` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_optional_stopping_ui; durrett_ch4_optional_stopping_integrable_terminal; durrett_ch4_bounded_stopping_submartingale_expectation
- `4.8.2` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_nonnegative_supermartingale_convergence; durrett_ch4_doob_maximal_inequality; durrett_ch4_stopped_process_supermartingale
- `4.8.3` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_random_walk_martingales; durrett_ch4_optional_stopping_integrable_terminal; durrett_ch4_conditional_variance_formula_martingales
- `4.8.4` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_wald_equation; durrett_ch4_random_walk_martingales; durrett_ch4_orthogonal_martingale_increments
- `4.8.5` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_asymmetric_gamblers_ruin; durrett_ch4_wald_equation; durrett_ch4_random_walk_martingales
- `4.8.6` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_asymmetric_gamblers_ruin; durrett_ch4_random_walk_martingales; durrett_ch4_optional_stopping_integrable_terminal
- `4.8.7` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_symmetric_gamblers_ruin; durrett_ch4_random_walk_martingales; durrett_ch4_optional_stopping_integrable_terminal
- `4.8.8` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_insurance_ruin_exponential_bound; durrett_ch4_random_walk_martingales; durrett_ch4_optional_stopping_integrable_terminal
- `4.8.9` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_insurance_ruin_exponential_bound; durrett_ch4_asymmetric_gamblers_ruin; durrett_ch4_random_walk_martingales
- `4.8.10` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_insurance_ruin_exponential_bound; durrett_ch4_asymmetric_gamblers_ruin
- `4.8.11` (4.8): Optional stopping applications, Wald identities, random walks, and ruin estimates
  - Methods: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale
  - Knowledge used: durrett_ch4_insurance_ruin_exponential_bound; durrett_ch4_random_walk_martingales
- `4.9.1` (4.9): Renewal equations and generating functions for random-walk return times
  - Methods: renewal-equation, generating-functions, return-time, random-walk
  - Knowledge used: durrett_ch4_arcsine_laws_random_walk; durrett_ch4_reflection_principle; durrett_ch4_ballot_theorem

## New Exercise-Derived Knowledge

### Conditional Bayes rule from indicator tests

- ID: `exercise_ch4_conditional_bayes_by_indicator`
- Kind: calculation-template
- Summary: To identify E[X | H] on a partition or sub-sigma-field, multiply by indicators of conditioning events and match integrals.
- Use case: Section 4.1 exercises involving conditional probabilities, finite partitions, and conditional densities.
- Tags: conditional-expectation, indicator-test, bayes

### Transfer pointwise inequalities through conditioning

- ID: `exercise_ch4_conditional_inequality_from_pointwise_bound`
- Kind: proof-template
- Summary: If an inequality holds after multiplying by every nonnegative H-measurable test function, it holds for the conditional expectations.
- Use case: Conditional Jensen, conditional Markov bounds, and monotonicity arguments in Section 4.1.
- Tags: conditional-expectation, inequality, test-functions

### L2 projection Pythagorean identity for conditioning

- ID: `exercise_ch4_l2_projection_pythagorean_conditioning`
- Kind: proof-template
- Summary: Use E[(X-E[X|H])Z]=0 for H-measurable Z to split squared errors and prove best-approximation identities.
- Use case: Projection and regression-style conditional expectation exercises.
- Tags: l2-projection, orthogonality, conditional-expectation

### Random-sum variance by conditioning on the count

- ID: `exercise_ch4_total_variance_random_sum`
- Kind: calculation-template
- Summary: Condition on N to compute E[S_N | N] and Var(S_N | N), then add conditional variance plus variance of the conditional mean.
- Use case: Random sums and total-variance exercises in Section 4.1.
- Tags: random-sum, total-variance, conditioning

### Conditional expectation can preserve distribution only under rigidity

- ID: `exercise_ch4_distribution_preserving_conditional_expectation`
- Kind: warning
- Summary: If E[X|H] has the same distribution as X and Jensen is tight for a strictly convex function, then X must already be H-measurable.
- Use case: Exercises where conditioning appears not to reduce randomness.
- Tags: jensen, rigidity, conditional-expectation

### One-step martingale check in the natural filtration

- ID: `exercise_ch4_natural_filtration_martingale_reduction`
- Kind: proof-template
- Summary: For processes built from independent increments, reduce E[X_{n+1}|F_n] to a deterministic function of the current state and one new increment.
- Use case: Section 4.2 martingale, submartingale, and supermartingale verification.
- Tags: martingale, natural-filtration, independent-increments

### Deterministic martingale-type checks reduce to monotonicity

- ID: `exercise_ch4_deterministic_submartingale_square_supermartingale`
- Kind: calculation-template
- Summary: A deterministic adapted process is a submartingale or supermartingale exactly when the underlying sequence is monotone in the corresponding direction.
- Use case: Exercises testing definitions on simple deterministic examples.
- Tags: submartingale, supermartingale, deterministic-process

### Localize upcrossing arguments by stopping at bounded levels

- ID: `exercise_ch4_stopped_upcrossing_localization`
- Kind: proof-template
- Summary: Stop a process before it leaves a bounded range so optional inequalities apply, then let the stopping level increase.
- Use case: Upcrossing and convergence exercises where integrability or boundedness needs to be restored.
- Tags: upcrossing, stopping, localization

### Product martingales may converge to zero by logarithms

- ID: `exercise_ch4_product_martingale_limit_zero`
- Kind: calculation-template
- Summary: For products of independent mean-one factors, examine log factors; a negative accumulated log drift can force almost-sure convergence to zero.
- Use case: Multiplicative martingales and examples where mean is not preserved at the limit.
- Tags: product-martingale, log-transform, almost-sure-limit

### Dubins-style switching creates many upcrossings

- ID: `exercise_ch4_dubins_upcrossing_switching`
- Kind: construction-template
- Summary: Alternate between betting strategies active below one level and above another to convert repeated upcrossings into predictable-transform gains.
- Use case: Exercises connecting upcrossing inequalities with gambling interpretations.
- Tags: upcrossing, predictable-transform, gambling

### Bounded increments alone do not make a martingale

- ID: `exercise_ch4_bounded_increment_nonmartingale_counterexample`
- Kind: counterexample-template
- Summary: Construct an adapted process with bounded steps but nonzero conditional drift to show martingale conclusions need a true drift condition.
- Use case: Section 4.3 exercises checking the exact hypotheses of martingale theorems.
- Tags: counterexample, bounded-increments, conditional-drift

### Summable additive errors preserve convergence

- ID: `exercise_ch4_additive_error_supermartingale_convergence`
- Kind: proof-template
- Summary: Add the tail sum of the error sequence to a near-supermartingale to obtain a genuine supermartingale with the same limiting behavior.
- Use case: Almost-supermartingale convergence arguments.
- Tags: supermartingale, summable-errors, convergence

### Partition likelihood ratios form martingales

- ID: `exercise_ch4_partition_rn_derivative_martingale`
- Kind: calculation-template
- Summary: On a refining finite partition, the ratio Q(A)/P(A) on the cell containing omega is the conditional expectation of dQ/dP.
- Use case: Radon-Nikodym and likelihood-ratio martingale exercises.
- Tags: radon-nikodym, likelihood-ratio, partition

### Bernoulli product likelihood ratios and Hellinger sums

- ID: `exercise_ch4_bernoulli_product_hellinger_criterion`
- Kind: criterion
- Summary: For product Bernoulli laws, square-root likelihood overlaps factor, and convergence or singularity is controlled by a summable squared parameter distance.
- Use case: Exercises comparing infinite product measures.
- Tags: bernoulli-product, hellinger, absolute-continuity

### Branching extinction probabilities are fixed points

- ID: `exercise_ch4_branching_fixed_point_extinction`
- Kind: calculation-template
- Summary: Condition on the first generation to get q = f(q), where f is the offspring generating function; choose the minimal fixed point in [0,1].
- Use case: Branching-process extinction and survival exercises.
- Tags: branching-process, generating-function, fixed-point

### Optional sampling between two stopping times

- ID: `exercise_ch4_optional_sampling_between_stopping_times`
- Kind: proof-template
- Summary: Apply optional sampling to stopped processes at bounded approximations of S and T, then pass to limits using the available integrability control.
- Use case: Section 4.4 exercises with E[M_T | F_S] and S <= T.
- Tags: optional-sampling, stopping-times, conditioning

### Doob L1 logarithmic maximal bound

- ID: `exercise_ch4_doob_l1_log_maximal_bound`
- Kind: inequality-template
- Summary: Integrate the weak L1 maximal inequality over levels and split at a scale where the integral of min(1, X/lambda) is finite.
- Use case: Maximal estimates for nonnegative submartingales without Lp control for p>1.
- Tags: doob-inequality, maximal-bound, logarithmic-moment

### Quadratic martingale exit bounds

- ID: `exercise_ch4_stopped_quadratic_martingale_exit_bound`
- Kind: calculation-template
- Summary: For a martingale with controlled conditional variances, stop M_n^2 minus accumulated variance at the exit time and compare with the boundary size.
- Use case: Exit probability and maximal L2 exercises.
- Tags: quadratic-martingale, exit-time, variance-bound

### Martingale increments are orthogonal in L2

- ID: `exercise_ch4_martingale_increment_orthogonality_sum`
- Kind: proof-template
- Summary: For i<j, E[D_iD_j]=E[D_i E[D_j|F_{j-1}]]=0, so variances of martingale sums add.
- Use case: L2 convergence, square-function, and maximal inequality exercises.
- Tags: orthogonality, martingale-differences, l2

### Kronecker normalization for martingale sums

- ID: `exercise_ch4_kronecker_martingale_normalization`
- Kind: proof-template
- Summary: Show a weighted martingale series converges in L2 or a.s., then apply Kronecker's lemma to get normalized partial-sum convergence.
- Use case: Martingale strong laws and weighted-average exercises.
- Tags: kronecker-lemma, strong-law, martingale-series

### Posterior consistency from Levy upward theorem

- ID: `exercise_ch4_posterior_consistency_by_levy_upward`
- Kind: proof-template
- Summary: Write a posterior probability as E[1_A | F_n]; as observations accumulate and generate A, Levy upward convergence sends it to 1_A.
- Use case: Bayesian consistency and statistical identification exercises.
- Tags: levy-upward, posterior, conditional-probability

### Dyadic conditional expectations approximate the full variable

- ID: `exercise_ch4_dyadic_conditional_expectation_approximation`
- Kind: construction-template
- Summary: Condition on increasingly fine dyadic sigma-fields; the generated sigma-field is the Borel information, so Levy upward gives convergence.
- Use case: Exercises approximating a variable by finite-information conditional expectations.
- Tags: dyadic, conditional-expectation, levy-upward

### Levy zero-one law forces absorption or escape events

- ID: `exercise_ch4_levy_zero_one_absorption_or_escape`
- Kind: proof-template
- Summary: If conditional probabilities of a tail event stay bounded away from the event indicator, Levy's zero-one law gives a contradiction.
- Use case: Random-walk, branching, or Markov-chain exercises with eventual absorption events.
- Tags: levy-zero-one, tail-event, absorption

### Bounded martingales with binary absorbing limits

- ID: `exercise_ch4_bounded_martingale_binary_limit`
- Kind: proof-template
- Summary: A bounded martingale converges a.s.; if the dynamics force every limit to be 0 or 1, the starting value is the probability of limiting at 1.
- Use case: Urn, posterior, and absorbing-state martingale exercises.
- Tags: bounded-martingale, absorbing-state, limit

### Backward martingale Lp convergence by uniform integrability

- ID: `exercise_ch4_backward_lp_convergence_ui`
- Kind: proof-template
- Summary: For p>1, boundedness in Lp gives uniform integrability, so backward martingale convergence improves to L1 and often Lp convergence.
- Use case: Backward conditional expectation exercises in Section 4.7.
- Tags: backward-martingale, lp, uniform-integrability

### Pass limits inside backward conditional expectations carefully

- ID: `exercise_ch4_backward_conditional_dct`
- Kind: warning
- Summary: Use domination or uniform integrability before interchanging conditional expectation limits with ordinary limits.
- Use case: Backward martingale convergence exercises involving approximating functions.
- Tags: conditional-dct, backward-martingale, uniform-integrability

### Exchangeability turns conditioning into hypergeometric sampling

- ID: `exercise_ch4_exchangeable_hypergeometric_conditioning`
- Kind: calculation-template
- Summary: Given the unordered multiset or the total number of successes, exchangeability makes a fixed subcollection have the finite-population hypergeometric law.
- Use case: Exchangeable Bernoulli and finite-sample conditional probability exercises.
- Tags: exchangeability, hypergeometric, conditioning

### Exchangeable pair covariance constraints

- ID: `exercise_ch4_exchangeable_pair_covariance_positive`
- Kind: calculation-template
- Summary: Use Var(sum X_i) >= 0 to derive lower bounds on pair covariances and identify the limiting covariance structure.
- Use case: Exchangeability exercises about correlations and de Finetti-style limits.
- Tags: exchangeability, covariance, variance

### U-statistic square limits by pair classification

- ID: `exercise_ch4_u_statistic_pair_square_limit`
- Kind: calculation-template
- Summary: Expand the square of the U-statistic and classify pairs by overlap pattern; only non-negligible classes contribute in the limit.
- Use case: U-statistic convergence exercises under exchangeability or iid assumptions.
- Tags: u-statistic, second-moment, pair-counting

### Optional stopping with a conditional target

- ID: `exercise_ch4_optional_stopping_ui_conditional_form`
- Kind: proof-template
- Summary: Stop at T wedge n, prove uniform integrability or boundedness, and pass to E[M_T | F_S]=M_S.
- Use case: Random-walk and stopping-time exercises with conditional versions of optional stopping.
- Tags: optional-stopping, uniform-integrability, conditioning

### Maximal bounds for nonnegative supermartingales

- ID: `exercise_ch4_supermartingale_maximal_bound`
- Kind: inequality-template
- Summary: Stop at the first crossing of a level and use the supermartingale property to bound the crossing probability by the initial mean divided by the level.
- Use case: Ruin, hitting, and overshoot probability estimates.
- Tags: supermartingale, maximal-bound, hitting-time

### Wald's second equation from a stopped square martingale

- ID: `exercise_ch4_wald_second_equation_stopped_l2`
- Kind: calculation-template
- Summary: For centered iid increments, S_n^2 - n sigma^2 is a martingale; optional stopping gives E[S_T^2]=sigma^2 E[T] when justified.
- Use case: Expected duration and variance identities for stopped random walks.
- Tags: wald-identity, square-martingale, random-walk

### Generate gambler's ruin moments from martingales

- ID: `exercise_ch4_gambler_ruin_variance_generation`
- Kind: calculation-template
- Summary: Use S_n, S_n^2-n, and higher polynomial martingales stopped at ruin boundaries to solve for hitting probabilities and time moments.
- Use case: Gambler's ruin expected time and variance exercises.
- Tags: gambler-ruin, polynomial-martingales, moments

### Exponential martingale ruin adjustment

- ID: `exercise_ch4_exponential_martingale_ruin_adjustment`
- Kind: calculation-template
- Summary: Find theta with E exp(theta X)=1, stop exp(theta S_n) at a hitting time, and use boundary values to estimate ruin probabilities.
- Use case: Insurance risk, random-walk ruin, and Lundberg-type inequalities.
- Tags: exponential-martingale, ruin-probability, adjustment-coefficient

### Fourth-moment martingales bound exit-time moments

- ID: `exercise_ch4_fourth_moment_exit_time`
- Kind: calculation-template
- Summary: Construct a polynomial martingale involving S_n^4, S_n^2, and n; stopping it at an exit time produces second-moment bounds for T.
- Use case: Random-walk exit-time variance and higher-moment exercises.
- Tags: fourth-moment, exit-time, polynomial-martingale

### Return-time renewal equations via generating functions

- ID: `exercise_ch4_return_time_renewal_generating_function`
- Kind: calculation-template
- Summary: Decompose visits into first return plus future visits, obtaining U(s)=1/(1-F(s)); analyze F(s) near s=1 to read recurrence and expected return time.
- Use case: Section 4.9 random-walk return-time exercise.
- Tags: renewal-equation, generating-functions, return-time

# Chapter 6 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter6/Chapter6Exercises.tex`
Source PDF: `Probability/Exercises/Chapter6/Chapter6Exercises.pdf`

This dataset turns the solved Chapter 6 exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.

## Files

- `chapter6_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.
- `chapter6_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter6_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter6_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.
- `chapter6_exercise_viki.md`: human-readable overview.
- `manifest.json`: dataset metadata.

## Section Method Cards

### 6.1 - Stationarity, invariant events, ergodicity, and measure-preserving examples

Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

Tags: stationarity, invariant-events, ergodicity, shift-model, measure-preserving

### 6.2 - Birkhoff upgrades, moving observables, and maximal inequalities

Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.

Tags: birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality

### 6.3 - Range growth, recurrence, cycle tricks, and stationary renewal bias

Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

Tags: recurrence, range, last-visit, cycle-trick, stationary-renewal

### 6.5 - Applications of subadditivity to LCS, LIS, Poisson paths, and branching

Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

Tags: subadditivity, first-moment, poissonization, branching-martingale, large-deviations

## New Knowledge Pieces

### Invariant sigma-field and invariant random variables

- ID: `ch6_exercise_method_invariant_sigma_field_measurable_functions`
- Kind: exercise-derived-method
- Summary: Show invariant events form a sigma-field by pullback closure; prove an I-measurable random variable is invariant by checking rational cuts, and conversely use invariant inverse images.
- Use case: Exercise 6.1.1; identifying E(X|I) and invariant limits.
- Tags: invariant-sigma-field, measurability, rational-cuts

### Strict representative for almost invariant sets

- ID: `ch6_exercise_method_almost_invariant_strictification`
- Kind: proof-template
- Summary: From an almost invariant set, form a forward pullback union B and then C=intersection phi^{-n}B; C is strictly invariant and differs only by a null set.
- Use case: Exercise 6.1.2; replacing mod-null invariance by exact invariance.
- Tags: almost-invariant, strict-invariance, null-sets

### Direct density proof of irrational rotation ergodicity

- ID: `ch6_exercise_method_direct_irrational_rotation_ergodicity`
- Kind: proof-template
- Summary: Use pigeonhole gaps to prove the irrational orbit is dense, approximate positive-measure sets by high-density intervals, and contradict coexistence of invariant A and A^c with positive measure.
- Use case: Exercise 6.1.3; proving ergodicity without Fourier series.
- Tags: irrational-rotation, density-points, ergodicity

### Two-sided extension of a stationary sequence

- ID: `ch6_exercise_method_two_sided_stationary_extension`
- Kind: construction
- Summary: Define finite-dimensional laws on integer-indexed coordinates by shifting all indices into the nonnegative side, then use stationarity for consistency and Kolmogorov extension.
- Use case: Exercise 6.1.4; return-time and cycle arguments needing negative times.
- Tags: stationary-process, two-sided, kolmogorov-extension

### Stationarity and ergodicity pass to factors

- ID: `ch6_exercise_method_factor_stationarity_ergodicity`
- Kind: proof-template
- Summary: For Y_k=g(X_k,X_{k+1},...), stationarity follows from shifted future laws; invariant events for Y pull back to invariant events for X, so ergodicity passes to Y.
- Use case: Exercise 6.1.5; creating stationary derived processes.
- Tags: factor-map, stationarity, ergodicity

### Random phase makes iid blocks stationary and ergodic

- ID: `ch6_exercise_method_random_phase_iid_blocks`
- Kind: construction
- Summary: Concatenate iid blocks and start at an independent uniform phase; one-step shifts rotate the phase and occasionally shift the iid block sequence, giving stationarity and ergodicity.
- Use case: Exercise 6.1.6; block constructions with stationary output.
- Tags: iid-blocks, random-phase, ergodicity

### Gauss map invariant density by branch telescoping

- ID: `ch6_exercise_method_gauss_map_invariant_density`
- Kind: calculation-template
- Summary: For phi(x)=1/x-floor(1/x), split into branches x=1/(k+y); the transformed density sum telescopes to 1/(1+y).
- Use case: Exercise 6.1.7; verifying the continued-fraction invariant measure.
- Tags: continued-fractions, gauss-map, invariant-density

### Lp upgrade of Birkhoff by truncation

- ID: `ch6_exercise_method_lp_upgrade_by_truncation`
- Kind: proof-template
- Summary: Prove Lp convergence for bounded observables by bounded convergence, then truncate X and control the tail using Jensen plus Lp contraction of conditional expectation.
- Use case: Exercise 6.2.1; upgrading ergodic averages from L1 to Lp.
- Tags: birkhoff, lp, truncation, jensen

### Moving observable ergodic average

- ID: `ch6_exercise_method_moving_observable_ergodic_average`
- Kind: proof-template
- Summary: Decompose averages of g_m(phi^m) into the fixed g average plus errors; control a.s. errors by tail suprema and L1 errors by Cesaro means.
- Use case: Exercise 6.2.2; triangular or time-varying observables in ergodic averages.
- Tags: moving-observable, tail-supremum, cesaro, birkhoff

### Wiener maximal inequality from maximal ergodic lemma

- ID: `ch6_exercise_method_wiener_maximal_from_maximal_ergodic`
- Kind: proof-template
- Summary: Apply the maximal ergodic lemma to Y=X-alpha so the positivity event of the shifted partial sums is exactly {max S_j/j > alpha}.
- Use case: Exercise 6.2.3; deriving maximal probability bounds for ergodic averages.
- Tags: maximal-ergodic-lemma, wiener-inequality, threshold-shift

### Range expectation by last-visit decomposition

- ID: `ch6_exercise_method_range_last_visit_counting`
- Kind: calculation-template
- Summary: Count each visited site by its last visit time; stationarity makes the probability of no future revisit over n-m steps equal to g_{n-m}.
- Use case: Exercise 6.3.1; expected range identities for stationary-increment walks.
- Tags: range, last-visit, stationary-increments

### Positive drift escape probability from range growth

- ID: `ch6_exercise_method_positive_drift_escape_probability`
- Kind: proof-template
- Summary: With ergodic integer increments bounded above by one and positive mean, the range grows at the same rate as the running maximum; Theorem 6.3.1 identifies the rate with P(escape).
- Use case: Exercise 6.3.2; recurrence/escape probabilities under stationary increments.
- Tags: positive-drift, escape-probability, range-growth

### Cycle trick occupation ratio

- ID: `ch6_exercise_method_cycle_trick_occupation_ratio`
- Kind: proof-template
- Summary: Use a two-sided stationary version and partition by the last visit to A before time 0; expected B-occupation in an A-cycle equals P(X0 in B)/P(X0 in A).
- Use case: Exercise 6.3.3; constructing stationary measures from excursions.
- Tags: cycle-trick, occupation-time, two-sided-stationarity

### Stationary renewal first-waiting bias

- ID: `ch6_exercise_method_stationary_renewal_waiting_bias`
- Kind: calculation-template
- Summary: Under conditioning on a renewal at time 0, stationarity of return gaps gives P(T=n)=Pbar(T>=n)/Ebar T for the waiting time seen from a stationary time.
- Use case: Exercise 6.3.4; inspection-paradox and stationary renewal calculations.
- Tags: renewal, waiting-time, kac, stationary-bias

### Arbitrarily slow deterministic subadditive convergence

- ID: `ch6_exercise_method_arbitrarily_slow_subadditive_convergence`
- Kind: counterexample-template
- Summary: Set X_{m,m+k}=f(k) with f(k)/k decreasing; subadditivity follows by comparing both pieces to f(n)/n, so the expectation convergence can be as slow as f(n)/n.
- Use case: Exercise 6.5.1; understanding limits of Fekete-type convergence rates.
- Tags: subadditivity, slow-convergence, fekete

### Longest common subsequence first-moment bounds

- ID: `ch6_exercise_method_lcs_first_moment_bounds`
- Kind: calculation-template
- Summary: Compute small-n expectations for lower bounds and bound P(L_n >= K) by the expected number of matching index-pair subsequences, binom(n,K)^2 2^{-K}.
- Use case: Exercise 6.5.2; bounding LCS constants.
- Tags: longest-common-subsequence, first-moment, entropy-bound

### Poisson greedy path lower bound

- ID: `ch6_exercise_method_poisson_greedy_increasing_path_lower_bound`
- Kind: calculation-template
- Summary: Choose successive Poisson points minimizing x+y in the northeast quadrant; the increment sum has tail exp(-t^2/2), giving mean coordinate step sqrt(pi/8) and gamma >= sqrt(8/pi).
- Use case: Exercise 6.5.3; lower bounds for Hammersley's increasing path constant.
- Tags: poisson-process, greedy-path, lis-lower-bound

### Permutation LIS upper bound by first moment

- ID: `ch6_exercise_method_permutation_lis_first_moment_upper_bound`
- Kind: calculation-template
- Summary: For a fixed k-subset of indices, the values are increasing with probability 1/k!, so E J_k^n=binom(n,k)/k!; Stirling with k~alpha sqrt(n) gives gamma <= e.
- Use case: Exercise 6.5.4; upper bounds for longest increasing subsequences.
- Tags: random-permutation, lis, first-moment, stirling

### Branching Laplace martingale speed bound

- ID: `ch6_exercise_method_branching_laplace_martingale_bound`
- Kind: proof-template
- Summary: Normalize the generation-n Laplace sum by (mu phi(theta))^n to get a nonnegative martingale; Markov's inequality bounds early birth events when exp(-theta a)/(mu phi(theta))>1.
- Use case: Exercise 6.5.5; age-dependent branching speed upper-tail bounds.
- Tags: branching-process, laplace-transform, martingale, large-deviations

## Exercise Record Index

### 6.1 - Stationarity, invariant events, ergodicity, and measure-preserving examples

- Exercise 6.1.1: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_invariant_sigma_field, durrett_ch6_ergodicity_definition, durrett_ch6_measure_preserving_shift_model`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.2: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_invariant_sigma_field, durrett_ch6_measure_preserving_shift_model`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.3: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_circle_rotation_ergodicity, durrett_ch6_ergodicity_definition, durrett_ch6_invariant_sigma_field`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.4: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_stationary_sequence_definition, durrett_ch6_measure_preserving_shift_model`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.5: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_functions_of_stationary_processes, durrett_ch6_stationary_sequence_definition, durrett_ch6_ergodicity_definition`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.6: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_stationary_sequence_definition, durrett_ch6_ergodicity_definition, durrett_ch6_functions_of_stationary_processes, durrett_ch6_iid_shift_ergodic`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.7: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_measure_preserving_shift_model, durrett_ch6_stationary_sequence_definition, durrett_ch6_invariant_sigma_field`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.

### 6.2 - Birkhoff upgrades, moving observables, and maximal inequalities

- Exercise 6.2.1: method tags `birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality`; knowledge used `durrett_ch6_birkhoff_ergodic_theorem, durrett_ch6_lp_upgrade_birkhoff, durrett_ch6_invariant_sigma_field`; new knowledge `ch6_exercise_method_lp_upgrade_by_truncation, ch6_exercise_method_moving_observable_ergodic_average, ch6_exercise_method_wiener_maximal_from_maximal_ergodic`.
- Exercise 6.2.2: method tags `birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality`; knowledge used `durrett_ch6_birkhoff_ergodic_theorem, durrett_ch6_invariant_sigma_field, durrett_ch6_measure_preserving_shift_model`; new knowledge `ch6_exercise_method_lp_upgrade_by_truncation, ch6_exercise_method_moving_observable_ergodic_average, ch6_exercise_method_wiener_maximal_from_maximal_ergodic`.
- Exercise 6.2.3: method tags `birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality`; knowledge used `durrett_ch6_maximal_ergodic_lemma, durrett_ch6_birkhoff_ergodic_theorem`; new knowledge `ch6_exercise_method_lp_upgrade_by_truncation, ch6_exercise_method_moving_observable_ergodic_average, ch6_exercise_method_wiener_maximal_from_maximal_ergodic`.

### 6.3 - Range growth, recurrence, cycle tricks, and stationary renewal bias

- Exercise 6.3.1: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_range_growth_stationary_increments, durrett_ch6_birkhoff_ergodic_theorem`; new knowledge `ch6_exercise_method_range_last_visit_counting, ch6_exercise_method_positive_drift_escape_probability, ch6_exercise_method_cycle_trick_occupation_ratio, ch6_exercise_method_stationary_renewal_waiting_bias`.
- Exercise 6.3.2: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_zero_drift_integer_recurrence, durrett_ch6_range_growth_stationary_increments, durrett_ch6_birkhoff_ergodic_theorem`; new knowledge `ch6_exercise_method_range_last_visit_counting, ch6_exercise_method_positive_drift_escape_probability, ch6_exercise_method_cycle_trick_occupation_ratio, ch6_exercise_method_stationary_renewal_waiting_bias`.
- Exercise 6.3.3: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_stationary_return_times_kac, durrett_ch6_cycle_trick_stationary_measure, durrett_ch6_stationary_sequence_definition`; new knowledge `ch6_exercise_method_range_last_visit_counting, ch6_exercise_method_positive_drift_escape_probability, ch6_exercise_method_cycle_trick_occupation_ratio, ch6_exercise_method_stationary_renewal_waiting_bias`.
- Exercise 6.3.4: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_stationary_return_times_kac, durrett_ch6_stationary_renewal_waiting_time, durrett_ch6_cycle_trick_stationary_measure`; new knowledge `ch6_exercise_method_range_last_visit_counting, ch6_exercise_method_positive_drift_escape_probability, ch6_exercise_method_cycle_trick_occupation_ratio, ch6_exercise_method_stationary_renewal_waiting_bias`.

### 6.5 - Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Exercise 6.5.1: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_subadditive_ergodic_theorem, durrett_ch6_fekete_expectation_step`; new knowledge `ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound`.
- Exercise 6.5.2: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_longest_common_subsequence_limit, durrett_ch6_subadditive_ergodic_theorem`; new knowledge `ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound`.
- Exercise 6.5.3: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_increasing_subsequence_permutation, durrett_ch6_poisson_square_time_change, durrett_ch6_subadditive_ergodic_theorem`; new knowledge `ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound`.
- Exercise 6.5.4: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_increasing_subsequence_permutation, durrett_ch6_poisson_square_time_change`; new knowledge `ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound`.
- Exercise 6.5.5: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_age_dependent_branching_speed, durrett_ch6_branching_speed_large_deviation_formula, durrett_ch6_subadditive_ergodic_theorem`; new knowledge `ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound`.

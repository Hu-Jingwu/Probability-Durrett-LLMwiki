# Chapter 8 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter8/Chapter8Exercises.tex`
Source PDF: `Probability/Exercises/Chapter8/Chapter8Exercises.pdf`

This dataset turns the solved Chapter 8 exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.

## Files

- `chapter8_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.
- `chapter8_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter8_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter8_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.
- `chapter8_exercise_viki.md`: human-readable overview.

## Section Method Cards

### 8.1 - Donsker embedding, random-walk path functionals, and Brownian transfer

Condition on the Skorokhod embedding interval for Brownian exit-time estimates; use Donsker plus continuous mapping for range, maximum, and occupation-type walk functionals.

Tags: donsker, skorokhod-embedding, brownian-exit-time, continuous-mapping, random-walk-range

### 8.3 - Stationary sequence CLTs and martingale/coboundary approximation

Center the statistic, verify finite dependence or projective summability, compute long-run variance from covariances, and identify the martingale approximation term from the proof.

Tags: stationary-clt, m-dependent, long-run-variance, martingale-approximation, head-runs

### 8.4 - Brownian bridge, empirical-process limits, and pinned Brownian calculations

Represent the bridge as Brownian motion pinned at time one; compute bridge probabilities by conditioning transition densities, and prove bridge Markov/martingale properties from its transition kernel.

Tags: brownian-bridge, pinned-brownian-motion, reflection-principle, transition-density, martingale

### 8.5 - Laws of the iterated logarithm and Strassen limit sets

Use tail sums and Borel-Cantelli to show heavy-tailed jumps break LIL scaling; use continuous endpoint evaluation of Strassen's functional limit set for scalar limit points.

Tags: lil, borel-cantelli, heavy-tail, strassen, functional-lil

## New Knowledge Pieces

### Conditional exit-time moment transfer

- ID: `exercise_method_conditional_exit_time_moment_transfer`
- Kind: exercise-derived-method
- Summary: When a Skorokhod embedding is a mixture of Brownian exits from intervals, apply exit-time estimates conditionally on the random interval and then integrate over the mixing law.
- Use case: Exercise 8.1.1; transferring Exercise 7.5.4 bounds to the random time T_{U,V}.
- Tags: skorokhod-embedding, brownian-exit-time, conditioning, moment-bound

### Random-walk range via Donsker

- ID: `exercise_method_random_walk_range_via_donsker`
- Kind: calculation-template
- Summary: For one-dimensional nearest-neighbor walks, visited sites form the interval between running min and max; divide by sqrt(n), apply Donsker to the continuous range functional, and drop the 1/sqrt(n) endpoint correction.
- Use case: Exercise 8.1.2 and random-walk range asymptotics.
- Tags: donsker, range, continuous-mapping, simple-random-walk

### Head-run CLT variance from 1-dependence

- ID: `exercise_method_head_run_long_run_variance`
- Kind: calculation-template
- Summary: For indicators of the pattern HT in fair coin flips, center by mu=1/4 and compute long-run variance as Var(eta_0)+2 Cov(eta_0,eta_1)=1/16 because adjacent HT events are mutually exclusive.
- Use case: Exercise 8.3.1; finite-dependence stationary CLT computations.
- Tags: stationary-clt, m-dependent, long-run-variance, pattern-counting

### Computing Gordin's Y0 in finite-dependence examples

- ID: `exercise_method_gordin_y0_computation`
- Kind: proof-template
- Summary: Use Y0=sum_j>=0(E(X_j|F_0)-E(X_j|F_{-1})); finite dependence kills all but finitely many terms, leaving explicit conditional expectations.
- Use case: Exercise 8.3.1 and martingale approximation examples.
- Tags: gordin, martingale-approximation, conditional-expectation, stationary-clt

### One-sided Brownian bridge tail by conditioned reflection

- ID: `exercise_method_bridge_tail_conditioned_reflection`
- Kind: proof-template
- Summary: Compute P(max bridge > b) by viewing the bridge as Brownian motion conditioned on B_1=0 and using the reflected Brownian density on {T_b<1}.
- Use case: Exercise 8.4.1; bridge extrema and Kolmogorov-Smirnov limit calculations.
- Tags: brownian-bridge, reflection-principle, conditional-density, tail

### Brownian bridge from time-changed Brownian motion

- ID: `exercise_method_bridge_time_change_covariance`
- Kind: construction
- Summary: To prove X_t=(1-t)B(t/(1-t)) is a bridge, show it is centered Gaussian with covariance s(1-t) for s<=t and continuous extension X_1=0.
- Use case: Exercise 8.4.2; recognizing Gaussian process identities.
- Tags: brownian-bridge, time-change, gaussian-process, covariance

### Brownian bridge Markov kernel by density cancellation

- ID: `exercise_method_bridge_markov_kernel_cancellation`
- Kind: proof-template
- Summary: Write pinned finite-dimensional densities as products of Brownian transition densities ending at zero; divide joint densities so all pre-s factors cancel, leaving a kernel depending only on the present state.
- Use case: Exercise 8.4.3; proving Markov property for conditioned Gaussian processes.
- Tags: brownian-bridge, markov-property, transition-density, conditioning

### Bridge divided by remaining time is a martingale

- ID: `exercise_method_bridge_remaining_time_martingale`
- Kind: proof-template
- Summary: Use E(B_t^0|B_s^0)=((1-t)/(1-s))B_s^0 to show B_t^0/(1-t) is a martingale; L2 norms grow like t/(1-t), so it is not L2 bounded.
- Use case: Exercise 8.4.4; bridge martingales and terminal singularity checks.
- Tags: brownian-bridge, martingale, l2-boundedness, transition-kernel

### Heavy-tailed jumps obstruct LIL scaling

- ID: `exercise_method_heavy_tail_jump_obstruction_lil`
- Kind: proof-template
- Summary: If E|X|^alpha is infinite with alpha<2, tail sums at scale n^{1/alpha} diverge; Borel-Cantelli gives infinitely many huge increments, forcing adjacent partial sums above sqrt(n log log n) scale.
- Use case: Exercise 8.5.1 and necessity intuition for finite variance in LIL.
- Tags: lil, heavy-tail, borel-cantelli, large-jumps

### Scalar LIL limit set from Strassen endpoint evaluation

- ID: `exercise_method_strassen_endpoint_limit_set`
- Kind: proof-template
- Summary: Apply the continuous map f -> f(1) to Strassen's compact LIL limit set; Cauchy-Schwarz bounds endpoints by [-1,1], and linear functions f(t)=at realize every endpoint.
- Use case: Exercise 8.5.2; deriving scalar limsup/limit-set results from functional LIL.
- Tags: strassen, functional-lil, endpoint-map, limit-set

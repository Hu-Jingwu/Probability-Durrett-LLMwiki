# Chapter 5 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter5/Chapter5Exercises.tex`
Source PDF: `Probability/Exercises/Chapter5/Chapter5Exercises.pdf`

This dataset turns the solved Chapter 5 exercises into retrieval-ready records, reusable method cards, and exercise-derived knowledge pieces.

Solved sections currently included: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, and 5.8.

## Files

- `chapter5_exercise_records.jsonl`: one record per solved exercise, including question, solution, Viki IDs used, and method tags.
- `chapter5_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter5_exercise_new_knowledge.jsonl`: reusable proof/calculation/classification patterns extracted from the exercises.
- `chapter5_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.
- `chapter5_exercise_viki.md`: human-readable overview.

## Section Method Cards

### 5.1 - Markov-chain examples and transition kernels

Identify the state variable that makes the future depend only on the present; compute transition probabilities by conditioning on the next independent draw, offspring, ball swap, or allele sample.

Tags: markov-property, transition-kernel, example-models, state-choice

### 5.2 - Markov property, stopping, hitting, exit, and martingale equations

Use conditional independence from the Markov property, decompose at first hitting times, and solve finite exit or expected-time problems through harmonic and Poisson equations.

Tags: strong-markov, hitting-time, harmonic-equation, martingale

### 5.3 - Recurrence, transience, birth-death tests, and Lyapunov criteria

Classify recurrence through return sums, finite closed classes, scale functions, and Foster-Lyapunov supermartingales; use asymptotic product tests for birth-death boundaries.

Tags: recurrence, transience, birth-death, lyapunov, scale-function

### 5.4 - Random-walk recurrence and harmonic-function consequences

Use ladder variables, recurrence alternatives, and random-walk visits to convert path behavior into Liouville theorems for superharmonic or bounded harmonic functions.

Tags: random-walk, ladder-variables, liouville, harmonic-functions

### 5.5 - Stationary measures, reversibility, cycle formula, and positive recurrence

Find invariant laws using detailed balance, cycle occupation measures, return-time identities, and drift/regeneration arguments for queues.

Tags: stationary-distribution, detailed-balance, cycle-trick, positive-recurrence

### 5.6 - Convergence to stationarity, coupling rates, and regenerative limit theorems

Prove convergence by coupling, obtain finite-state exponential rates through uniform block coupling, and use regenerative cycles for additive LLNs, CLTs, and ratio limits.

Tags: coupling, ergodic-theorem, regeneration, ratio-limit, clt

### 5.8 - Harris chains, split-chain atoms, GI/G/1 queues, and continuous-state recurrence

Reduce Harris-chain questions to the split-chain atom, transfer countable-state return and stationary-measure arguments, and analyze reflected random walks by drift and path reversal.

Tags: harris-chain, split-chain, atom, gig1, reflected-random-walk

## New Knowledge Pieces

### State sufficiency test for the Markov property

- ID: `exercise_ch5_state_sufficiency_test`
- Kind: diagnostic-template
- Summary: A proposed process is Markov only if the retained state contains all information needed to compute the next-step law; record maxima fail when the current walk location is omitted.
- Use case: Exercises 5.1.1, 5.1.2, 5.1.3, and other state-selection problems.
- Tags: markov-property, state-choice, counterexample

### Compute transitions from the one-step mechanism

- ID: `exercise_ch5_transition_from_one_step_mechanism`
- Kind: calculation-template
- Summary: Given the present state, enumerate the next independent draw, swap, birth, or arrival and translate the possible outcomes into transition probabilities.
- Use case: Coupon, pair-chain, Bernoulli-Laplace, Wright-Fisher, and queue transition computations.
- Tags: transition-matrix, conditioning, examples

### Bayesian predictive state for hidden-parameter chains

- ID: `exercise_ch5_hidden_parameter_predictive_markov`
- Kind: calculation-template
- Summary: When a hidden parameter is shared across trials, update its posterior from a sufficient statistic and use the posterior mean as the next-step predictive probability.
- Use case: Exercise 5.1.6 and temporally inhomogeneous Markov chains from exchangeable coin flips.
- Tags: bayesian-update, sufficient-statistic, inhomogeneous-markov

### Mendelian pair transition matrix

- ID: `exercise_ch5_mendelian_pair_transition`
- Kind: calculation-template
- Summary: For unordered genotype-pair states, compute one-offspring genotype probabilities (p,q,r) and map two independent offspring to probabilities p^2, 2pq, 2pr, q^2, 2qr, r^2.
- Use case: Brother-sister mating transition and absorption computations.
- Tags: genetics, transition-matrix, mendelian

### Past and future conditional independence

- ID: `exercise_ch5_conditional_independence_past_future`
- Kind: proof-template
- Summary: For A in the past and B in the future, condition first on the present sigma-field; the Markov property turns E(1_B|F_n) into a function of X_n.
- Use case: Exercise 5.2.1 and conditional independence arguments.
- Tags: markov-property, conditional-independence, tower-property

### First entrance decomposition

- ID: `exercise_ch5_first_entrance_decomposition`
- Kind: proof-template
- Summary: Partition {X_n=y} by the first positive hitting time T_y=m, then restart from y by the strong Markov property to get p^n(x,y)=sum_m P_x(T_y=m)p^{n-m}(y,y).
- Use case: Exercise 5.2.4 and renewal decompositions for Markov chains.
- Tags: hitting-time, strong-markov, decomposition

### Exit probabilities solve the Dirichlet problem

- ID: `exercise_ch5_exit_probability_dirichlet_problem`
- Kind: proof-template
- Summary: An exit probability h(x)=P_x(V_A<V_B) is harmonic off A union B with boundary values 1 and 0; optional stopping at the exit time proves uniqueness on finite domains.
- Use case: Exercises 5.2.7 and 5.2.8.
- Tags: dirichlet-problem, harmonic, optional-stopping

### Expected hitting times solve a Poisson equation

- ID: `exercise_ch5_expected_hitting_time_poisson_equation`
- Kind: proof-template
- Summary: For g(x)=E_x V_A, first-step analysis gives g=1+Pg off A and g=0 on A; the process g(X_{n∧V_A})+n∧V_A is the uniqueness martingale.
- Use case: Exercises 5.2.11, 5.2.12, and 5.2.13.
- Tags: expected-hitting-time, poisson-equation, martingale

### Absorption probability from martingale value

- ID: `exercise_ch5_absorption_probability_martingale`
- Kind: calculation-template
- Summary: If a bounded martingale is stopped on two absorbing boundary values, the starting value equals the boundary-weighted absorption probability.
- Use case: Exercises 5.2.8, 5.2.9, and 5.2.10.
- Tags: martingale, absorption, optional-stopping

### Iid excursions between recurrent returns

- ID: `exercise_ch5_excursion_iid_cycles`
- Kind: regeneration-template
- Summary: At successive return times to a recurrent state, the strong Markov property makes the interarrival times and path excursions iid.
- Use case: Exercise 5.3.1 and regenerative proofs in Sections 5.5 and 5.6.
- Tags: excursions, regeneration, strong-markov

### Birth-death recurrence by log product asymptotics

- ID: `exercise_ch5_birth_death_log_product_test`
- Kind: asymptotic-template
- Summary: Use log(q_j/p_j) expansions to decide divergence of the birth-death scale sum; for p_j=1/2+C/j the threshold is C=1/4.
- Use case: Exercise 5.3.4 and nearest-neighbor recurrence boundaries.
- Tags: birth-death, recurrence, asymptotics

### Lyapunov function tending to zero proves transience

- ID: `exercise_ch5_lyapunov_to_zero_transience`
- Kind: criterion
- Summary: A positive superharmonic function outside a finite set that tends to zero at infinity contradicts recurrent return to that finite set, hence implies transience in irreducible chains.
- Use case: Exercise 5.3.5 and outward-drift birth-death chains.
- Tags: lyapunov, transience, supermartingale

### Power Lyapunov functions for near-critical birth-death chains

- ID: `exercise_ch5_power_lyapunov_birth_death`
- Kind: calculation-template
- Summary: For p_j-1/2~C/j, Taylor expand E_j X_1^alpha-j^alpha; choosing alpha on the correct side of 1-4C gives recurrence or transience.
- Use case: Exercise 5.3.6.
- Tags: birth-death, lyapunov, taylor-expansion

### Recurrent irreducible chains have only constant nonnegative superharmonic functions

- ID: `exercise_ch5_superharmonic_liouville_chain`
- Kind: liouville-template
- Summary: Stop a nonnegative supermartingale f(X_n) at the hitting time of another state; recurrence forces f(x)>=f(y) and symmetry gives equality.
- Use case: Exercise 5.3.7 and Liouville-type arguments.
- Tags: superharmonic, recurrence, liouville

### Four alternatives for one-dimensional random walks

- ID: `exercise_ch5_one_dimensional_random_walk_alternatives`
- Kind: classification-template
- Summary: Tail zero-one laws and ladder behavior force a one-dimensional random walk to be identically zero, drift to +infinity, drift to -infinity, or oscillate unboundedly both ways.
- Use case: Exercise 5.4.1.
- Tags: random-walk, zero-one-law, classification

### Ascending ladder epochs regenerate record highs

- ID: `exercise_ch5_ladder_epoch_geometric_regeneration`
- Kind: regeneration-template
- Summary: Successive strict ascending ladder epochs repeat the same trial by the strong Markov property; if the first ladder time is defective, only finitely many records occur, otherwise records go to infinity.
- Use case: Exercise 5.4.2.
- Tags: ladder-variables, records, random-walk

### Recurrent random walk implies nonnegative superharmonic Liouville

- ID: `exercise_ch5_recurrent_walk_superharmonic_liouville`
- Kind: liouville-template
- Summary: For recurrent walks in dimensions one and two, f(S_n) is a nonnegative supermartingale and recurrent visits to neighborhoods force all superharmonic values to agree.
- Use case: Exercise 5.4.3.
- Tags: superharmonic, random-walk, liouville

### Bounded harmonic functions via tail zero-one law

- ID: `exercise_ch5_bounded_harmonic_tail_zero_one`
- Kind: proof-template
- Summary: For a bounded harmonic h, h(S_n) is a bounded martingale; its limit is invariant under finite permutations of iid increments, so Hewitt-Savage forces constancy.
- Use case: Exercise 5.4.4.
- Tags: harmonic, hewitt-savage, martingale

### Hypergeometric stationary law for Bernoulli-Laplace

- ID: `exercise_ch5_hypergeometric_detailed_balance`
- Kind: calculation-template
- Summary: The Bernoulli-Laplace diffusion has stationary distribution proportional to binomial choices of black and white balls in the left urn; adjacent detailed balance verifies it.
- Use case: Exercise 5.5.1.
- Tags: bernoulli-laplace, hypergeometric, detailed-balance

### Cycle occupation measure as a hitting-probability ratio

- ID: `exercise_ch5_cycle_measure_hitting_ratio`
- Kind: formula
- Summary: For recurrent x and y in the same class, expected visits to y during one x-cycle equal P_x(T_y<T_x)/P_y(T_x<T_y).
- Use case: Exercise 5.5.2.
- Tags: cycle-trick, hitting-probability, stationary-measure

### Use normalization to compare stationary measures

- ID: `exercise_ch5_stationary_measure_uniqueness_scaling`
- Kind: proof-template
- Summary: In an irreducible recurrent chain, all stationary measures are scalar multiples; evaluate at one state to determine the scalar.
- Use case: Exercises 5.5.3 and 5.5.5.
- Tags: stationary-measure, uniqueness, normalization

### Poisson thinning gives M/M/infinity stationarity

- ID: `exercise_ch5_poisson_thinning_stationarity`
- Kind: calculation-template
- Summary: If X is Poisson(theta), Bernoulli thinning with survival p gives Poisson(p theta), and adding independent Poisson(lambda) arrivals gives Poisson(p theta+lambda).
- Use case: Exercise 5.5.8.
- Tags: poisson, thinning, queue

### Idle fraction from reflected random-walk regulator

- ID: `exercise_ch5_reflected_walk_idle_fraction`
- Kind: queue-template
- Summary: For a stable reflected walk, the regulator increments exactly when the queue is empty and the raw increment is -1; dividing the reflection identity by n gives the long-run idle frequency.
- Use case: Exercise 5.5.7 and M/G/1 stationary mass at zero.
- Tags: reflected-random-walk, queue, stationarity

### Two-state chain convergence via affine recursion

- ID: `exercise_ch5_two_state_affine_recursion`
- Kind: calculation-template
- Summary: Track one coordinate probability q_n; the recursion q_{n+1}=beta+(1-alpha-beta)q_n solves explicitly around its stationary fixed point.
- Use case: Exercise 5.6.1.
- Tags: two-state-chain, stationary-distribution, recursion

### Finite irreducible aperiodic chains have a positive matrix power

- ID: `exercise_ch5_finite_aperiodic_uniform_power`
- Kind: proof-template
- Summary: Use a path from x to y plus sufficiently long return loops at y; finiteness lets one choose a common power m for all pairs.
- Use case: Exercise 5.6.2.
- Tags: finite-chain, aperiodic, positive-power

### Uniform block coupling gives exponential convergence

- ID: `exercise_ch5_block_coupling_exponential_rate`
- Kind: coupling-template
- Summary: If an m-step transition has a uniformly positive chance to send all states to one common state, coupling attempts in independent blocks have geometric tails.
- Use case: Exercise 5.6.3 and finite-state mixing estimates.
- Tags: coupling, exponential-rate, finite-chain

### Regenerative LLN for additive functionals

- ID: `exercise_ch5_regenerative_additive_functional_lln`
- Kind: limit-template
- Summary: Split the path into iid return cycles; reward sums divided by elapsed time converge to expected cycle reward divided by expected cycle length, which equals the stationary average.
- Use case: Exercise 5.6.5.
- Tags: regeneration, ergodic-theorem, lln

### Regenerative CLT for additive functionals

- ID: `exercise_ch5_regenerative_additive_functional_clt`
- Kind: limit-template
- Summary: Apply the iid CLT to centered cycle rewards and random-index by the number of completed cycles; show incomplete-cycle rewards are negligible on sqrt(n) scale.
- Use case: Exercise 5.6.6.
- Tags: regeneration, clt, random-index

### Ratio limits from recurrent cycles

- ID: `exercise_ch5_recurrent_ratio_limit_cycles`
- Kind: limit-template
- Summary: Count visits to z per completed y-cycle and divide by visits to y; the strong law gives the stationary-measure ratio m(z)/m(y).
- Use case: Exercises 5.6.7 and 5.6.8.
- Tags: ratio-limit, recurrent-chain, cycle-measure

### Split-chain recurrence is return-sum divergence at the atom

- ID: `exercise_ch5_split_atom_return_sum`
- Kind: criterion
- Summary: For the artificial atom alpha, the countable-state return criterion applies: recurrence is equivalent to divergence of sum_n pbar^n(alpha,alpha).
- Use case: Exercise 5.8.1.
- Tags: harris-chain, split-chain, recurrence

### Stationary distribution forces Harris recurrence

- ID: `exercise_ch5_harris_stationarity_implies_recurrence`
- Kind: proof-template
- Summary: Lift a stationary distribution to the split chain; positive stationary mass at alpha forces an infinite expected number of alpha visits, hence recurrence.
- Use case: Exercise 5.8.3.
- Tags: harris-chain, stationarity, recurrence

### Harris recurrence does not depend on the small-set pair

- ID: `exercise_ch5_harris_small_set_choice_invariance`
- Kind: proof-template
- Summary: If another Harris set A' is reachable, it has positive lambda measure for the original split chain; Theorem 5.8.8 makes visits to A' occur infinitely often.
- Use case: Exercise 5.8.4.
- Tags: harris-chain, small-set, invariance

### GI/G/1 drift classification

- ID: `exercise_ch5_gig1_drift_classification`
- Kind: queue-template
- Summary: Compare the reflected workload with the raw random walk until the first negative passage: positive drift gives transience, nonpositive drift gives recurrence, negative drift gives positive recurrence.
- Use case: Exercise 5.8.5.
- Tags: gig1, queue, drift

### Reflected random walk equals reversed maximum in law

- ID: `exercise_ch5_reflection_maximum_representation`
- Kind: identity-template
- Summary: The reflected workload satisfies W_n=S_n-min_{j<=n}S_j, which by reversing increments has the same law as the maximum of a length-n random walk.
- Use case: Exercise 5.8.6.
- Tags: reflected-random-walk, path-reversal, maximum

### Multiplicative variance O.U. becomes stable on log scale

- ID: `exercise_ch5_multiplicative_ou_log_recursion`
- Kind: classification-template
- Summary: For Y_{n+1}=beta sqrt(|Y_n|) Z_{n+1}, log|Y_n| follows an AR(1) recursion with coefficient 1/2, yielding a nonzero positive recurrent Harris class plus an absorbing zero.
- Use case: Exercise 5.8.7.
- Tags: ornstein-uhlenbeck, log-recursion, harris-chain

# Durrett Chapter 6 LLM Viki: Ergodic Theorems

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter6.pdf`.

This unified Chapter 6 knowledge base includes textbook knowledge pieces plus exercise-derived method patterns from the solved Chapter 6 exercises.

Exercise source: `Probability/Exercises/Chapter6/Chapter6Exercises.tex` and `Probability/Exercises/Chapter6/Chapter6Exercises.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

## Section Guides

### 6.1 Definitions and Examples

- Goal: Translate stationary sequences into measure-preserving dynamical systems and identify ergodic examples.

- Must master: stationarity, measure-preserving maps, invariant sigma-field, ergodicity, iid shifts, stationary Markov chains, irrational rotations

- Prelim angle: Most Chapter 6 problems start by checking whether the invariant sigma-field is trivial.

### 6.2 Birkhoff's Ergodic Theorem

- Goal: Use Birkhoff's theorem to turn long-run averages into conditional expectations or constants.

- Must master: Birkhoff theorem, maximal ergodic lemma, SLLN as a special case, Markov chain averages, equidistribution

- Prelim angle: This is the high-yield theorem for time averages of dependent stationary data.

### 6.3 Recurrence

- Goal: Apply ergodic averages to range growth, recurrence of stationary-increment walks, and return cycles.

- Must master: range theorem, zero conditional drift recurrence, Kac return-time theorem, cycle trick

- Prelim angle: Good recurrence problems often ask you to identify escape probability or mean return time from stationarity.

### 6.4 A Subadditive Ergodic Theorem

- Goal: Recognize subadditive arrays and prove normalized optimal costs have limits.

- Must master: subadditive array hypotheses, Fekete expectation step, ergodic constant case, range and LCS examples

- Prelim angle: Use when the quantity is an optimal path length, cost, passage time, or negative of a superadditive reward.

### 6.5 Applications

- Goal: See the subadditive theorem in random matrices, random permutations, first-passage percolation, and branching processes.

- Must master: random matrix products, Poissonization, FPP time constant, integrability checks, branching-process speed

- Prelim angle: Applications usually reduce to checking subadditivity plus stationarity and then interpreting the constant.

## Knowledge Pieces

### Stationary sequence

- ID: `durrett_ch6_stationary_sequence_definition`

- Section: 6.1 Definitions and Examples

- Kind: definition

- Summary: A sequence X_0, X_1, ... is stationary when each shifted finite block has the same law as the original block.

- Proof idea: Check equality of all finite-dimensional distributions after shifting by k.

- Exam use: Use as the entry point for ergodic averages, stationary Markov chains, rotations, and stationary increments.

- Pitfall: Stationarity is distributional, not pathwise equality; it does not imply independence.

- Tags: stationarity, finite-dimensional-laws, shift

### Measure-preserving transformation model

- ID: `durrett_ch6_measure_preserving_shift_model`

- Section: 6.1 Definitions and Examples

- Kind: construction

- Summary: Every stationary sequence on a nice state space can be represented as X_n(omega)=X(phi^n omega) for a measure-preserving map phi.

- Proof idea: Put the stationary law on sequence space and let phi be the left shift; stationarity makes the shift preserve probability.

- Exam use: Lets all ergodic-theorem statements be proved for one abstract dynamical system.

- Pitfall: The representation changes the sample space; it preserves laws but not necessarily the user's original probability space.

- Tags: measure-preserving, shift-space, stationary-process

### Invariant events and invariant sigma-field

- ID: `durrett_ch6_invariant_sigma_field`

- Section: 6.1 Definitions and Examples

- Kind: definition

- Summary: An event A is invariant if phi^{-1}A=A up to null sets; the invariant events form the sigma-field I.

- Proof idea: Closure under complements and countable unions follows from pulling sets back through phi^{-1}.

- Exam use: The limit in Birkhoff's theorem is the conditional expectation onto I.

- Pitfall: Invariant means unchanged under the transformation, not merely high probability overlap after one shift.

- Tags: invariant-events, sigma-field, conditional-expectation

### Ergodicity

- ID: `durrett_ch6_ergodicity_definition`

- Section: 6.1 Definitions and Examples

- Kind: definition

- Summary: A measure-preserving transformation is ergodic when every invariant event has probability 0 or 1.

- Proof idea: Interpret nonergodicity as the ability to split the space into invariant pieces of positive probability.

- Exam use: Use ergodicity to turn Birkhoff limits E(X|I) into constants EX.

- Pitfall: Ergodic is stronger than stationary and different from independent; periodic examples can be stationary but not mixing.

- Tags: ergodicity, invariant-events, 0-1-law

### IID shifts are ergodic

- ID: `durrett_ch6_iid_shift_ergodic`

- Section: 6.1 Definitions and Examples

- Kind: example-pattern

- Summary: For an iid sequence, invariant shift events lie in the tail sigma-field, so Kolmogorov's 0-1 law implies ergodicity.

- Proof idea: Iterate shift invariance to show A is measurable with respect to sigma(X_n, X_{n+1}, ...), then intersect over n.

- Exam use: Explains why Birkhoff's theorem recovers the strong law for iid sequences.

- Pitfall: The tail sigma-field argument uses iid independence; it is not automatic for every stationary sequence.

- Tags: iid, tail-sigma-field, ergodic

### Stationary Markov chain ergodicity criterion

- ID: `durrett_ch6_stationary_markov_chain_ergodic`

- Section: 6.1 Definitions and Examples

- Kind: theorem

- Summary: A countable-state Markov chain started in a positive stationary distribution is ergodic exactly when the chain is irreducible.

- Proof idea: Closed irreducible classes give invariant events; conversely the Markov property and recurrence force invariant probabilities to be constant.

- Exam use: Use for time averages of irreducible positive recurrent chains.

- Pitfall: Irreducibility makes I trivial, but periodic chains may still have a nontrivial tail sigma-field.

- Tags: markov-chains, irreducibility, stationary-distribution

### Circle rotation ergodicity

- ID: `durrett_ch6_circle_rotation_ergodicity`

- Section: 6.1 Definitions and Examples

- Kind: example-pattern

- Summary: Rotation x -> x+theta mod 1 is ergodic under Lebesgue measure when theta is irrational and not ergodic when theta is rational.

- Proof idea: For irrational theta, Fourier coefficients of an invariant L2 function satisfy c_k(e^{2 pi i k theta}-1)=0, forcing all nonconstant coefficients to vanish.

- Exam use: The canonical deterministic example where ergodic averages behave like probabilistic averages.

- Pitfall: Rational rotations have finite orbits and many invariant unions of orbit slices.

- Tags: circle-rotation, fourier-series, irrational

### Functions of stationary processes

- ID: `durrett_ch6_functions_of_stationary_processes`

- Section: 6.1 Definitions and Examples

- Kind: fact

- Summary: Measurable functions of the future of a stationary process form another stationary process; ergodicity is inherited under such factors.

- Proof idea: Write Y_k=g(X_k,X_{k+1},...) and compare shifted finite-dimensional distributions.

- Exam use: Useful for creating stationary indicator, block, or return-time processes.

- Pitfall: The function must be applied in a shift-compatible way; arbitrary time-dependent functions can destroy stationarity.

- Tags: stationary-factors, measurable-functions, ergodicity

### Birkhoff ergodic theorem

- ID: `durrett_ch6_birkhoff_ergodic_theorem`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: theorem

- Summary: For X in L1, the time averages n^{-1} sum_{m<n} X(phi^m omega) converge almost surely and in L1 to E(X|I).

- Proof idea: Subtract E(X|I), use the maximal ergodic lemma to rule out positive limsup and negative liminf, then truncate for L1 convergence.

- Exam use: Main tool for replacing long-run empirical averages by conditional or ordinary means.

- Pitfall: Without ergodicity the limit is random: it is E(X|I), not necessarily EX.

- Tags: birkhoff, ergodic-theorem, time-averages

### Maximal ergodic lemma

- ID: `durrett_ch6_maximal_ergodic_lemma`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: lemma

- Summary: For partial sums S_k of X along a measure-preserving orbit and M_k=max(0,S_1,...,S_k), one has E(X; M_k>0) >= 0.

- Proof idea: Compare X(omega)+M_k(phi omega) with each S_j(omega), integrate, and use measure preservation.

- Exam use: The key technical inequality behind Birkhoff's pointwise convergence proof.

- Pitfall: It is an integration inequality, not a direct maximal probability bound; track the set {M_k>0}.

- Tags: maximal-ergodic-lemma, partial-sums, birkhoff-proof

### Strong law as an ergodic theorem

- ID: `durrett_ch6_strong_law_from_birkhoff`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: example-pattern

- Summary: For iid X_m in L1, Birkhoff gives n^{-1} sum_{m<n} X_m -> E X_0 almost surely and in L1.

- Proof idea: The iid shift is ergodic, so E(X_0|I)=E X_0.

- Exam use: Use as a conceptual shortcut from Chapter 2 LLNs to general stationary sequences.

- Pitfall: The theorem needs integrability; for nonintegrable iid variables this conclusion can fail.

- Tags: strong-law, iid, birkhoff

### Stationary Markov chain time averages

- ID: `durrett_ch6_markov_chain_time_average`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: corollary

- Summary: For an irreducible countable-state Markov chain started from its stationary distribution pi, n^{-1} sum_{m<n} f(X_m) -> sum_x f(x) pi(x) for pi-integrable f.

- Proof idea: Apply Birkhoff to f(X_0) and use the irreducible stationary chain's ergodicity.

- Exam use: Recovers the long-run frequency and reward law for positive recurrent Markov chains.

- Pitfall: The statement is under stationarity; nonstationary initial laws need an additional argument.

- Tags: markov-chains, time-averages, stationary-distribution

### Weyl equidistribution from irrational rotation

- ID: `durrett_ch6_weyl_equidistribution`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: theorem

- Summary: For irrational theta, the orbit x+n theta mod 1 visits every interval [a,b) with limiting frequency b-a for every starting x.

- Proof idea: Apply Birkhoff to interval indicators, then remove the exceptional set by approximating intervals from inside and using density.

- Exam use: Use for deterministic averaging and number-theoretic distribution mod 1.

- Pitfall: Birkhoff first gives almost-every starting point; the interval theorem needs extra work for every x.

- Tags: equidistribution, irrational-rotation, intervals

### Benford law for powers

- ID: `durrett_ch6_benford_law_powers`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: example-pattern

- Summary: If log_10 2 is irrational, the first digit of 2^m has limiting frequency log_10((k+1)/k) for digit k.

- Proof idea: First digits correspond to fractional parts of m log_10 2 lying in [log_10 k, log_10(k+1)).

- Exam use: A memorable application of equidistribution to leading-digit asymptotics.

- Pitfall: Benford frequencies describe a limiting distribution, not exact finite-sample frequencies.

- Tags: benford-law, equidistribution, first-digits

### Lp convergence upgrade

- ID: `durrett_ch6_lp_upgrade_birkhoff`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: exercise-pattern

- Summary: If X is in Lp for p>1, the Birkhoff averages converge in Lp as well as almost surely.

- Proof idea: Use maximal or domination arguments for the averages and uniform integrability of powers.

- Exam use: Useful when a problem asks for convergence in norm rather than only almost surely.

- Pitfall: Do not infer Lp convergence from L1 convergence without an Lp bound or uniform integrability.

- Tags: lp-convergence, uniform-integrability, birkhoff

### Range growth for stationary increments

- ID: `durrett_ch6_range_growth_stationary_increments`

- Section: 6.3 Recurrence

- Kind: theorem

- Summary: For a stationary-increment walk S_n, the range R_n=|{S_1,...,S_n}| satisfies R_n/n -> E(1_A|I), where A is the event of never returning to 0 after time 0.

- Proof idea: Bound R_n below by future-noncollision indicators and above by finite-window noncollision indicators, then apply Birkhoff and monotone convergence.

- Exam use: Connects recurrence questions to an ergodic average of escape events.

- Pitfall: The limit is conditional on I; only in ergodic cases does it reduce to P(A).

- Tags: range, stationary-increments, recurrence

### Zero conditional drift implies recurrence on Z

- ID: `durrett_ch6_zero_drift_integer_recurrence`

- Section: 6.3 Recurrence

- Kind: theorem

- Summary: For stationary integer-valued increments with E|X_1|<infinity and E(X_1|I)=0, the walk returns to 0 infinitely often almost surely.

- Proof idea: Birkhoff gives S_n/n -> 0, so the range is sublinear; the range theorem forces escape probability zero, and stationarity then gives infinitely many returns.

- Exam use: Generalizes the Chung-Fuchs recurrence intuition beyond iid increments.

- Pitfall: The condition is E(X_1|I)=0, not merely EX_1=0; mixtures of positive and negative drifts are counterexamples.

- Tags: recurrence, zero-drift, stationary-increments

### Kac return-time theorem

- ID: `durrett_ch6_stationary_return_times_kac`

- Section: 6.3 Recurrence

- Kind: theorem

- Summary: For a stationary process that hits A almost surely, the successive return gaps to A are stationary under P(.|X_0 in A), and E(T_1|X_0 in A)=1/P(X_0 in A).

- Proof idea: Embed the process two-sided, decompose by the last visit before time 0, and sum tail probabilities of the first return.

- Exam use: Turns visits to a set into regenerative cycles and recovers mean return time 1/pi(x) for Markov chains.

- Pitfall: Conditioning on X_0 in A is essential; the first waiting time from an arbitrary stationary time has a length-biased flavor.

- Tags: kac, return-times, stationary-processes

### Cycle trick for stationary measures

- ID: `durrett_ch6_cycle_trick_stationary_measure`

- Section: 6.3 Recurrence

- Kind: exercise-pattern

- Summary: Expected occupation of B during a return cycle to A equals P(X_0 in B)/P(X_0 in A) when A and B are disjoint and A is recurrent.

- Proof idea: Sum indicators over the cycle and use stationarity to convert cycle occupation counts into one-time probabilities.

- Exam use: Useful for constructing stationary measures of Markov chains from excursions.

- Pitfall: The denominator is the stationary mass of A; the formula is not a conditional probability of hitting B before returning.

- Tags: cycle-trick, occupation-times, stationary-measure

### Stationary renewal waiting-time bias

- ID: `durrett_ch6_stationary_renewal_waiting_time`

- Section: 6.3 Recurrence

- Kind: exercise-pattern

- Summary: For a stationary {0,1} process conditioned on X_0=1, the first return law satisfies Pbar(T_1=n)=Pbar(T_1>=n)/Ebar T_1 in the iid-gap renewal case.

- Proof idea: Count which positions inside a renewal interval can serve as the stationary origin.

- Exam use: Explains inspection-paradox corrections in stationary renewal processes.

- Pitfall: The distribution seen from a stationary time differs from the raw interarrival distribution.

- Tags: renewal, return-time, inspection-paradox

### Subadditive ergodic theorem

- ID: `durrett_ch6_subadditive_ergodic_theorem`

- Section: 6.4 A Subadditive Ergodic Theorem

- Kind: theorem

- Summary: For a stationary subadditive array X_{m,n} with integrability and a linear lower expectation bound, X_{0,n}/n converges almost surely and in L1 to a limit with mean inf_m E X_{0,m}/m.

- Proof idea: Use Fekete's lemma for expectations, Birkhoff on block increments for the limsup, then a covering argument for the liminf.

- Exam use: The main tool for limits of optimal costs, passage times, longest subsequences, and products.

- Pitfall: Check the exact stationarity assumptions; Liggett's version is weaker than Kingman's original in useful applications.

- Tags: subadditive-ergodic-theorem, kingman, liggett

### Fekete step for expected subadditive arrays

- ID: `durrett_ch6_fekete_expectation_step`

- Section: 6.4 A Subadditive Ergodic Theorem

- Kind: proof-template

- Summary: If a_n=E X_{0,n} and a_m+a_{n-m}>=a_n, then a_n/n converges to inf_m a_m/m.

- Proof idea: Write n=km+r, iterate subadditivity, divide by n, and let n grow with fixed m.

- Exam use: Use whenever the deterministic expectation part of a subadditive theorem appears.

- Pitfall: The inequality direction is easy to mix up because the array convention is X_{0,m}+X_{m,n}>=X_{0,n}.

- Tags: fekete, expectations, subadditivity

### Birkhoff as the additive special case

- ID: `durrett_ch6_birkhoff_as_additive_case`

- Section: 6.4 A Subadditive Ergodic Theorem

- Kind: example-pattern

- Summary: If X_{m,n}=xi_{m+1}+...+xi_n for a stationary integrable sequence, then the subadditive theorem reduces to Birkhoff.

- Proof idea: The subadditive inequality becomes equality, and block stationarity is inherited from the xi sequence.

- Exam use: A quick consistency check for the hypotheses of the subadditive theorem.

- Pitfall: Do not lose the indexing: X_{m,n} covers increments after m through n.

- Tags: additive-case, stationary-sequence, birkhoff

### Range as a subadditive example

- ID: `durrett_ch6_range_subadditive_example`

- Section: 6.4 A Subadditive Ergodic Theorem

- Kind: example-pattern

- Summary: The number of distinct sites visited between times m+1 and n is subadditive, so the normalized range has an almost sure and L1 limit.

- Proof idea: The union of sites in two adjacent time intervals covers the sites in the whole interval, giving X_{0,m}+X_{m,n}>=X_{0,n}.

- Exam use: Provides a second route to existence of range-growth rates even when the rate is not identified.

- Pitfall: The theorem gives existence of the limit, not the recurrence classification by itself.

- Tags: range, random-walk, subadditivity

### Longest common subsequence limit

- ID: `durrett_ch6_longest_common_subsequence_limit`

- Section: 6.4 A Subadditive Ergodic Theorem

- Kind: example-pattern

- Summary: For two ergodic stationary sequences, the longest common subsequence length L_{0,n} satisfies L_{0,n}/n -> gamma, where gamma=sup_m E L_{0,m}/m.

- Proof idea: Use superadditivity of L over adjacent blocks, or subadditivity of -L, and apply the subadditive ergodic theorem.

- Exam use: Recognize optimization lengths as candidates for subadditive limits.

- Pitfall: The theorem proves existence of gamma but usually not its numerical value.

- Tags: longest-common-subsequence, superadditivity, ergodic-limit

### Products of positive random matrices

- ID: `durrett_ch6_random_matrix_products`

- Section: 6.5 Applications

- Kind: application

- Summary: For stationary positive matrices with integrable log entries, n^{-1} log of product entries converges almost surely to a common growth rate.

- Proof idea: Take minus logs of positive product entries to create a subadditive array; compare entries and norms to transfer the limit.

- Exam use: A probability route to Lyapunov-exponent-type limits.

- Pitfall: Strict positivity and log-integrability matter; zeros or heavy tails can break the logarithmic comparison.

- Tags: random-matrices, lyapunov-exponent, subadditivity

### Increasing subsequences in random permutations

- ID: `durrett_ch6_increasing_subsequence_permutation`

- Section: 6.5 Applications

- Kind: application

- Summary: Poissonizing random permutations and applying subadditivity shows the longest increasing subsequence has an n^{1/2} order limit constant.

- Proof idea: Represent permutations by Poisson points in squares, use superadditivity of increasing paths, then de-Poissonize with the Poisson count law.

- Exam use: A classic example of turning a combinatorial optimization problem into an ergodic limit.

- Pitfall: The subadditive argument gives the existence of the constant; identifying it as 2 requires deeper work.

- Tags: random-permutations, longest-increasing-subsequence, poissonization

### Poisson square time change

- ID: `durrett_ch6_poisson_square_time_change`

- Section: 6.5 Applications

- Kind: lemma

- Summary: If tau(n) is the side length of the square containing the first n points of a rate-one planar Poisson process, then tau(n)/sqrt(n) -> 1 almost surely.

- Proof idea: The number of points in the square of side sqrt(n) is a sum of independent mean-one Poisson increments, so the strong law controls the inverse time.

- Exam use: Used to pass from Poissonized increasing paths back to fixed-size random permutations.

- Pitfall: The scale is sqrt(n) because the square area is t^2.

- Tags: poisson-process, time-change, permutation

### First-passage percolation time constant

- ID: `durrett_ch6_first_passage_percolation_time_constant`

- Section: 6.5 Applications

- Kind: application

- Summary: For iid nonnegative edge passage times on Z^d with suitable integrability, t(0,nu)/n converges almost surely to a deterministic time constant.

- Proof idea: Passage times satisfy t(0,nu)<=t(0,mu)+t(mu,nu), so X_{m,n}=t(mu,nu) is subadditive; tail triviality makes the limit constant.

- Exam use: Core template for metric growth models and random media.

- Pitfall: Finite mean of one edge is sufficient in the simple statement but can be weakened; without integrability the limit may be infinite.

- Tags: first-passage-percolation, time-constant, random-media

### First-passage percolation integrability condition

- ID: `durrett_ch6_fpp_integrability_min_condition`

- Section: 6.5 Applications

- Kind: criterion

- Summary: A weaker useful condition is that the minimum of 2d independent edge times has finite mean, equivalently integral_0^infty (1-F(x))^{2d} dx < infinity.

- Proof idea: Use disjoint neighboring paths to dominate one-step passage times by minima of several edge variables.

- Exam use: Helps check when a finite time constant exists for heavy-tailed edge weights.

- Pitfall: This condition concerns the minimum of several edges, not the edge variable itself.

- Tags: first-passage-percolation, integrability, heavy-tails

### Age-dependent branching process speed

- ID: `durrett_ch6_age_dependent_branching_speed`

- Section: 6.5 Applications

- Kind: application

- Summary: In an age-dependent branching process with no extinction at birth and finite lifetimes, the first birth time in generation n divided by n converges almost surely.

- Proof idea: Define X_{m,n} as the additional time from the first generation-m individual to a generation-n descendant and apply Liggett's subadditive theorem.

- Exam use: Shows why the weaker Liggett hypotheses are useful beyond Kingman's original stationary-array assumptions.

- Pitfall: The stronger all-triples subadditivity can fail because the fastest later descendant need not descend from the fastest earlier individual.

- Tags: branching-process, subadditivity, growth-speed

### Branching speed via lifetime large deviations

- ID: `durrett_ch6_branching_speed_large_deviation_formula`

- Section: 6.5 Applications

- Kind: formula

- Summary: For mean offspring mu and lifetime sums with rate c(a), the asymptotic earliest-generation speed is gamma=inf{a: log mu - c(a)>0}.

- Proof idea: Compare expected counts of generation-n individuals born by time an with branching-process survival when the count grows supercritically.

- Exam use: Connects subadditive limits with large-deviation rate functions.

- Pitfall: The subadditive theorem gives existence; this formula requires additional branching and large-deviation analysis.

- Tags: branching-process, large-deviations, speed

### Invariant sigma-field and invariant random variables

- ID: `ch6_exercise_method_invariant_sigma_field_measurable_functions`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: exercise-pattern

- Summary: Show invariant events form a sigma-field by pullback closure; prove an I-measurable random variable is invariant by checking rational cuts, and conversely use invariant inverse images.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.1; identifying E(X|I) and invariant limits.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: invariant-sigma-field, measurability, rational-cuts

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

### Strict representative for almost invariant sets

- ID: `ch6_exercise_method_almost_invariant_strictification`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: proof-template

- Summary: From an almost invariant set, form a forward pullback union B and then C=intersection phi^{-n}B; C is strictly invariant and differs only by a null set.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.2; replacing mod-null invariance by exact invariance.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: almost-invariant, strict-invariance, null-sets

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

### Direct density proof of irrational rotation ergodicity

- ID: `ch6_exercise_method_direct_irrational_rotation_ergodicity`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: proof-template

- Summary: Use pigeonhole gaps to prove the irrational orbit is dense, approximate positive-measure sets by high-density intervals, and contradict coexistence of invariant A and A^c with positive measure.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.3; proving ergodicity without Fourier series.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: irrational-rotation, density-points, ergodicity

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

### Two-sided extension of a stationary sequence

- ID: `ch6_exercise_method_two_sided_stationary_extension`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: construction

- Summary: Define finite-dimensional laws on integer-indexed coordinates by shifting all indices into the nonnegative side, then use stationarity for consistency and Kolmogorov extension.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.4; return-time and cycle arguments needing negative times.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: stationary-process, two-sided, kolmogorov-extension

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

### Stationarity and ergodicity pass to factors

- ID: `ch6_exercise_method_factor_stationarity_ergodicity`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: proof-template

- Summary: For Y_k=g(X_k,X_{k+1},...), stationarity follows from shifted future laws; invariant events for Y pull back to invariant events for X, so ergodicity passes to Y.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.5; creating stationary derived processes.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: factor-map, stationarity, ergodicity

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

### Random phase makes iid blocks stationary and ergodic

- ID: `ch6_exercise_method_random_phase_iid_blocks`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: construction

- Summary: Concatenate iid blocks and start at an independent uniform phase; one-step shifts rotate the phase and occasionally shift the iid block sequence, giving stationarity and ergodicity.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.6; block constructions with stationary output.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: iid-blocks, random-phase, ergodicity

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

### Gauss map invariant density by branch telescoping

- ID: `ch6_exercise_method_gauss_map_invariant_density`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: calculation-template

- Summary: For phi(x)=1/x-floor(1/x), split into branches x=1/(k+y); the transformed density sum telescopes to 1/(1+y).

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.7; verifying the continued-fraction invariant measure.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: continued-fractions, gauss-map, invariant-density

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

### Lp upgrade of Birkhoff by truncation

- ID: `ch6_exercise_method_lp_upgrade_by_truncation`

- Section: 6.2 Exercises: Birkhoff upgrades, moving observables, and maximal inequalities

- Kind: proof-template

- Summary: Prove Lp convergence for bounded observables by bounded convergence, then truncate X and control the tail using Jensen plus Lp contraction of conditional expectation.

- Proof idea: Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.

- Exam use: Exercise 6.2.1; upgrading ergodic averages from L1 to Lp.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: birkhoff, lp, truncation, jensen

- Source exercises: 6.2.1, 6.2.2, 6.2.3

### Moving observable ergodic average

- ID: `ch6_exercise_method_moving_observable_ergodic_average`

- Section: 6.2 Exercises: Birkhoff upgrades, moving observables, and maximal inequalities

- Kind: proof-template

- Summary: Decompose averages of g_m(phi^m) into the fixed g average plus errors; control a.s. errors by tail suprema and L1 errors by Cesaro means.

- Proof idea: Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.

- Exam use: Exercise 6.2.2; triangular or time-varying observables in ergodic averages.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: moving-observable, tail-supremum, cesaro, birkhoff

- Source exercises: 6.2.1, 6.2.2, 6.2.3

### Wiener maximal inequality from maximal ergodic lemma

- ID: `ch6_exercise_method_wiener_maximal_from_maximal_ergodic`

- Section: 6.2 Exercises: Birkhoff upgrades, moving observables, and maximal inequalities

- Kind: proof-template

- Summary: Apply the maximal ergodic lemma to Y=X-alpha so the positivity event of the shifted partial sums is exactly {max S_j/j > alpha}.

- Proof idea: Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.

- Exam use: Exercise 6.2.3; deriving maximal probability bounds for ergodic averages.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: maximal-ergodic-lemma, wiener-inequality, threshold-shift

- Source exercises: 6.2.1, 6.2.2, 6.2.3

### Range expectation by last-visit decomposition

- ID: `ch6_exercise_method_range_last_visit_counting`

- Section: 6.3 Exercises: Range growth, recurrence, cycle tricks, and stationary renewal bias

- Kind: calculation-template

- Summary: Count each visited site by its last visit time; stationarity makes the probability of no future revisit over n-m steps equal to g_{n-m}.

- Proof idea: Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

- Exam use: Exercise 6.3.1; expected range identities for stationary-increment walks.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: range, last-visit, stationary-increments

- Source exercises: 6.3.1, 6.3.2, 6.3.3, 6.3.4

### Positive drift escape probability from range growth

- ID: `ch6_exercise_method_positive_drift_escape_probability`

- Section: 6.3 Exercises: Range growth, recurrence, cycle tricks, and stationary renewal bias

- Kind: proof-template

- Summary: With ergodic integer increments bounded above by one and positive mean, the range grows at the same rate as the running maximum; Theorem 6.3.1 identifies the rate with P(escape).

- Proof idea: Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

- Exam use: Exercise 6.3.2; recurrence/escape probabilities under stationary increments.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: positive-drift, escape-probability, range-growth

- Source exercises: 6.3.1, 6.3.2, 6.3.3, 6.3.4

### Cycle trick occupation ratio

- ID: `ch6_exercise_method_cycle_trick_occupation_ratio`

- Section: 6.3 Exercises: Range growth, recurrence, cycle tricks, and stationary renewal bias

- Kind: proof-template

- Summary: Use a two-sided stationary version and partition by the last visit to A before time 0; expected B-occupation in an A-cycle equals P(X0 in B)/P(X0 in A).

- Proof idea: Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

- Exam use: Exercise 6.3.3; constructing stationary measures from excursions.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: cycle-trick, occupation-time, two-sided-stationarity

- Source exercises: 6.3.1, 6.3.2, 6.3.3, 6.3.4

### Stationary renewal first-waiting bias

- ID: `ch6_exercise_method_stationary_renewal_waiting_bias`

- Section: 6.3 Exercises: Range growth, recurrence, cycle tricks, and stationary renewal bias

- Kind: calculation-template

- Summary: Under conditioning on a renewal at time 0, stationarity of return gaps gives P(T=n)=Pbar(T>=n)/Ebar T for the waiting time seen from a stationary time.

- Proof idea: Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

- Exam use: Exercise 6.3.4; inspection-paradox and stationary renewal calculations.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: renewal, waiting-time, kac, stationary-bias

- Source exercises: 6.3.1, 6.3.2, 6.3.3, 6.3.4

### Arbitrarily slow deterministic subadditive convergence

- ID: `ch6_exercise_method_arbitrarily_slow_subadditive_convergence`

- Section: 6.5 Exercises: Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Kind: counterexample-template

- Summary: Set X_{m,m+k}=f(k) with f(k)/k decreasing; subadditivity follows by comparing both pieces to f(n)/n, so the expectation convergence can be as slow as f(n)/n.

- Proof idea: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Exam use: Exercise 6.5.1; understanding limits of Fekete-type convergence rates.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: subadditivity, slow-convergence, fekete

- Source exercises: 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5

### Longest common subsequence first-moment bounds

- ID: `ch6_exercise_method_lcs_first_moment_bounds`

- Section: 6.5 Exercises: Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Kind: calculation-template

- Summary: Compute small-n expectations for lower bounds and bound P(L_n >= K) by the expected number of matching index-pair subsequences, binom(n,K)^2 2^{-K}.

- Proof idea: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Exam use: Exercise 6.5.2; bounding LCS constants.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: longest-common-subsequence, first-moment, entropy-bound

- Source exercises: 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5

### Poisson greedy path lower bound

- ID: `ch6_exercise_method_poisson_greedy_increasing_path_lower_bound`

- Section: 6.5 Exercises: Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Kind: calculation-template

- Summary: Choose successive Poisson points minimizing x+y in the northeast quadrant; the increment sum has tail exp(-t^2/2), giving mean coordinate step sqrt(pi/8) and gamma >= sqrt(8/pi).

- Proof idea: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Exam use: Exercise 6.5.3; lower bounds for Hammersley's increasing path constant.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: poisson-process, greedy-path, lis-lower-bound

- Source exercises: 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5

### Permutation LIS upper bound by first moment

- ID: `ch6_exercise_method_permutation_lis_first_moment_upper_bound`

- Section: 6.5 Exercises: Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Kind: calculation-template

- Summary: For a fixed k-subset of indices, the values are increasing with probability 1/k!, so E J_k^n=binom(n,k)/k!; Stirling with k~alpha sqrt(n) gives gamma <= e.

- Proof idea: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Exam use: Exercise 6.5.4; upper bounds for longest increasing subsequences.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: random-permutation, lis, first-moment, stirling

- Source exercises: 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5

### Branching Laplace martingale speed bound

- ID: `ch6_exercise_method_branching_laplace_martingale_bound`

- Section: 6.5 Exercises: Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Kind: proof-template

- Summary: Normalize the generation-n Laplace sum by (mu phi(theta))^n to get a nonnegative martingale; Markov's inequality bounds early birth events when exp(-theta a)/(mu phi(theta))>1.

- Proof idea: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Exam use: Exercise 6.5.5; age-dependent branching speed upper-tail bounds.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: branching-process, laplace-transform, martingale, large-deviations

- Source exercises: 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5

## Exercise Method Cards

### 6.1 Stationarity, invariant events, ergodicity, and measure-preserving examples

- ID: `durrett_ch6_section_6_1_method_card`

- Method: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Tags: stationarity, invariant-events, ergodicity, shift-model, measure-preserving

- New knowledge IDs: ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density

### 6.2 Birkhoff upgrades, moving observables, and maximal inequalities

- ID: `durrett_ch6_section_6_2_method_card`

- Method: Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.

- Tags: birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality

- New knowledge IDs: ch6_exercise_method_lp_upgrade_by_truncation, ch6_exercise_method_moving_observable_ergodic_average, ch6_exercise_method_wiener_maximal_from_maximal_ergodic

### 6.3 Range growth, recurrence, cycle tricks, and stationary renewal bias

- ID: `durrett_ch6_section_6_3_method_card`

- Method: Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

- Tags: recurrence, range, last-visit, cycle-trick, stationary-renewal

- New knowledge IDs: ch6_exercise_method_range_last_visit_counting, ch6_exercise_method_positive_drift_escape_probability, ch6_exercise_method_cycle_trick_occupation_ratio, ch6_exercise_method_stationary_renewal_waiting_bias

### 6.5 Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- ID: `durrett_ch6_section_6_5_method_card`

- Method: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Tags: subadditivity, first-moment, poissonization, branching-martingale, large-deviations

- New knowledge IDs: ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound

## Exercise Record Index

- Exercise 6.1.1: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_invariant_sigma_field, durrett_ch6_ergodicity_definition, durrett_ch6_measure_preserving_shift_model`.
- Exercise 6.1.2: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_invariant_sigma_field, durrett_ch6_measure_preserving_shift_model`.
- Exercise 6.1.3: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_circle_rotation_ergodicity, durrett_ch6_ergodicity_definition, durrett_ch6_invariant_sigma_field`.
- Exercise 6.1.4: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_stationary_sequence_definition, durrett_ch6_measure_preserving_shift_model`.
- Exercise 6.1.5: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_functions_of_stationary_processes, durrett_ch6_stationary_sequence_definition, durrett_ch6_ergodicity_definition`.
- Exercise 6.1.6: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_stationary_sequence_definition, durrett_ch6_ergodicity_definition, durrett_ch6_functions_of_stationary_processes, durrett_ch6_iid_shift_ergodic`.
- Exercise 6.1.7: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_measure_preserving_shift_model, durrett_ch6_stationary_sequence_definition, durrett_ch6_invariant_sigma_field`.
- Exercise 6.2.1: method tags `birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality`; knowledge used `durrett_ch6_birkhoff_ergodic_theorem, durrett_ch6_lp_upgrade_birkhoff, durrett_ch6_invariant_sigma_field`.
- Exercise 6.2.2: method tags `birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality`; knowledge used `durrett_ch6_birkhoff_ergodic_theorem, durrett_ch6_invariant_sigma_field, durrett_ch6_measure_preserving_shift_model`.
- Exercise 6.2.3: method tags `birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality`; knowledge used `durrett_ch6_maximal_ergodic_lemma, durrett_ch6_birkhoff_ergodic_theorem`.
- Exercise 6.3.1: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_range_growth_stationary_increments, durrett_ch6_birkhoff_ergodic_theorem`.
- Exercise 6.3.2: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_zero_drift_integer_recurrence, durrett_ch6_range_growth_stationary_increments, durrett_ch6_birkhoff_ergodic_theorem`.
- Exercise 6.3.3: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_stationary_return_times_kac, durrett_ch6_cycle_trick_stationary_measure, durrett_ch6_stationary_sequence_definition`.
- Exercise 6.3.4: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_stationary_return_times_kac, durrett_ch6_stationary_renewal_waiting_time, durrett_ch6_cycle_trick_stationary_measure`.
- Exercise 6.5.1: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_subadditive_ergodic_theorem, durrett_ch6_fekete_expectation_step`.
- Exercise 6.5.2: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_longest_common_subsequence_limit, durrett_ch6_subadditive_ergodic_theorem`.
- Exercise 6.5.3: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_increasing_subsequence_permutation, durrett_ch6_poisson_square_time_change, durrett_ch6_subadditive_ergodic_theorem`.
- Exercise 6.5.4: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_increasing_subsequence_permutation, durrett_ch6_poisson_square_time_change`.
- Exercise 6.5.5: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_age_dependent_branching_speed, durrett_ch6_branching_speed_large_deviation_formula, durrett_ch6_subadditive_ergodic_theorem`.

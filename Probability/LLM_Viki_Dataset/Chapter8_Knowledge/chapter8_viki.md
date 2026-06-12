# Durrett Chapter 8 LLM Viki: Applications to Random Walk

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter8.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

Exercise-derived records and method cards are also available in this folder:
`chapter8_exercise_records.jsonl`, `chapter8_exercise_method_cards.jsonl`,
`chapter8_exercise_new_knowledge.jsonl`, and `chapter8_exercise_viki.md`.

## Section Guides

### 8.1 Donsker's Theorem

- Goal: Use Skorokhod embedding to derive CLT, Donsker convergence, and random-walk path-functional limits.

- Must master: Skorokhod embedding, Brownian random clock, Donsker theorem, continuous mapping for path functionals, maxima and occupation examples

- Prelim angle: Most useful when a random-walk statistic can be rewritten as a Brownian functional in the limit.

### 8.2 CLTs for Martingales

- Goal: Prove normal and functional limits for martingale arrays using conditional variances and Lindeberg controls.

- Must master: martingale embedding, conditional variance clock, martingale Lindeberg condition, martingale CLT

- Prelim angle: High-yield for dependent sums once the summands have conditional mean zero.

### 8.3 CLTs for Stationary Sequences

- Goal: Reduce dependent stationary CLTs to martingale approximations, finite dependence, Markov-chain decompositions, or mixing estimates.

- Must master: martingale approximation, projective criteria, M-dependent variance, Poisson equation, mixing covariance bounds

- Prelim angle: A toolkit for deciding when dependence is weak enough for a normal limit and how to compute long-run variance.

### 8.4 Empirical Distributions, Brownian Bridge

- Goal: Move from empirical CDF consistency to sqrt(n) empirical-process fluctuations and Brownian bridge limits.

- Must master: Glivenko-Cantelli, empirical process, Brownian bridge, Kolmogorov-Smirnov statistic, killed Brownian density method

- Prelim angle: Connects iid samples, CDF transforms, and Brownian bridge limits used in goodness-of-fit theory.

### 8.5 Laws of the Iterated Logarithm

- Goal: Understand sharp almost-sure fluctuation scales for Brownian motion and iid random walks.

- Must master: Brownian LIL, iid LIL, Borel-Cantelli tail bounds, Strassen functional LIL

- Prelim angle: Use for questions about almost-sure limsup behavior rather than distributional limits.

## Knowledge Pieces

### Skorokhod embedding for one mean-zero variable

- ID: `durrett_ch8_skorokhod_embedding_mean_zero`

- Section: 8.1 Donsker's Theorem

- Kind: theorem

- Summary: If X has mean 0 and finite second moment, then Brownian motion can be stopped at a time T with B_T distributed as X and E T = E X^2.

- Proof idea: Represent the law of X as a mixture of two-point mean-zero laws, then use Brownian first exits from intervals (u,v).

- Exam use: Turns random-walk increments into Brownian increments with matching variance, making Brownian path results available for sums.

- Pitfall: The random interval used in the construction is external randomness; conditioning is what preserves the stopping-time calculations.

- Tags: skorokhod-embedding, brownian-motion, stopping-time, finite-variance

### Embedding iid sums in Brownian motion

- ID: `durrett_ch8_embedded_random_walk`

- Section: 8.1 Donsker's Theorem

- Kind: construction

- Summary: For iid mean-zero variance-one increments, one can choose increasing stopping times T_n so that S_n has the same finite-dimensional law as B(T_n), with iid gaps T_n-T_{n-1}.

- Proof idea: Restart Brownian motion after each stopping time and apply the one-step Skorokhod embedding to each increment.

- Exam use: Useful for proving CLT and invariance principles by comparing S_n to Brownian motion at random times.

- Pitfall: The equality is in distribution for the embedded walk, not necessarily pathwise equality with a preexisting walk.

- Tags: random-walk, embedding, iid, brownian-scaling

### Central limit theorem via random times

- ID: `durrett_ch8_clt_from_embedding`

- Section: 8.1 Donsker's Theorem

- Kind: proof-template

- Summary: Since S_n/sqrt(n) has the same law as B(T_n)/sqrt(n) and T_n/n converges in probability to 1, S_n/sqrt(n) converges to a standard normal variable.

- Proof idea: Use the weak law on the iid stopping-time gaps and Brownian continuity near time 1, then apply converging together.

- Exam use: A clean proof strategy when Brownian embedding is available and finite variance is assumed.

- Pitfall: One still needs tight control of B(t) near t=1; T_n/n -> 1 alone is not a distributional identity.

- Tags: clt, brownian-motion, converging-together, weak-law

### Donsker invariance principle

- ID: `durrett_ch8_donsker_invariance_principle`

- Section: 8.1 Donsker's Theorem

- Kind: theorem

- Summary: The linearly interpolated process S(n t)/sqrt(n), built from iid mean-zero variance-one increments, converges weakly in C[0,1] to standard Brownian motion.

- Proof idea: Show the embedded Brownian time change is uniformly close to deterministic time on [0,1], then use uniform continuity of Brownian paths.

- Exam use: This is the main transfer principle from random walks to Brownian motion for maxima, hitting times, occupations, and path functionals.

- Pitfall: The topology matters: the statement is process-level weak convergence, not only convergence of each fixed time.

- Tags: donsker, invariance-principle, functional-clt, c0-1

### Continuous functional transfer from Donsker

- ID: `durrett_ch8_continuous_functional_transfer`

- Section: 8.1 Donsker's Theorem

- Kind: theorem

- Summary: If a functional on C[0,1] is continuous at Brownian paths with probability one, then applying it to the rescaled random walk converges to applying it to Brownian motion.

- Proof idea: Combine Donsker's theorem with the continuous mapping theorem, allowing discontinuities on Brownian-null path sets.

- Exam use: The default method for deriving asymptotics of path statistics from random-walk convergence.

- Pitfall: Many natural functionals are not everywhere continuous; check Brownian almost-sure continuity rather than ordinary continuity only.

- Tags: continuous-mapping, path-functional, brownian-motion, donsker

### Random-walk maximum limit

- ID: `durrett_ch8_maximum_functional`

- Section: 8.1 Donsker's Theorem

- Kind: example-pattern

- Summary: The normalized maximum max_{m<=n} S_m/sqrt(n) converges to max_{0<=t<=1} B_t, whose tail is 2 P(B_1 >= a).

- Proof idea: Apply Donsker to the continuous maximum functional and use the Brownian reflection principle for the distribution.

- Exam use: Recognize maximum and boundary-crossing limits as Brownian supremum problems.

- Pitfall: The reflection-principle tail formula is for a nonnegative barrier and Brownian motion starting at 0.

- Tags: maximum, reflection-principle, brownian-supremum, random-walk

### Last zero before time n

- ID: `durrett_ch8_last_zero_arcsine`

- Section: 8.1 Donsker's Theorem

- Kind: example-pattern

- Summary: The last sign-change or zero time of a centered finite-variance walk, divided by n, converges to the Brownian last-zero time, which has the arcsine law.

- Proof idea: Show the last-zero functional is continuous at Brownian paths almost surely, then invoke Donsker.

- Exam use: Transfers the arcsine law beyond simple symmetric walks.

- Pitfall: The functional is discontinuous at some deterministic paths, so the Brownian null-set condition is the key point.

- Tags: arcsine-law, last-zero, donsker, brownian-zero-set

### Occupation time of a half-line

- ID: `durrett_ch8_occupation_time_halfline`

- Section: 8.1 Donsker's Theorem

- Kind: example-pattern

- Summary: The fraction of times a centered finite-variance walk spends above a sqrt(n) threshold converges to the Brownian occupation time above that threshold.

- Proof idea: Apply Donsker to the occupation functional and use that Brownian paths spend zero Lebesgue time at any fixed level.

- Exam use: Use for random-walk occupation proportions and arcsine-type limits.

- Pitfall: Discrete-time counts require a small interpolation comparison; do not identify them blindly with continuous occupation time.

- Tags: occupation-time, arcsine-law, brownian-motion, invariance-principle

### Embedding square-integrable martingales

- ID: `durrett_ch8_martingale_sk_embedding`

- Section: 8.2 CLTs for Martingales

- Kind: theorem

- Summary: A square-integrable martingale can be represented in distribution as Brownian motion sampled at increasing stopping times whose conditional expected increments match conditional variances.

- Proof idea: Embed each martingale difference conditionally using a Brownian first-exit construction after the previous stopping time.

- Exam use: Provides the Brownian-time-change route to martingale CLTs.

- Pitfall: The conditional variance process, not deterministic time, controls the Brownian clock.

- Tags: martingale, skorokhod-embedding, conditional-variance, brownian-motion

### Martingale convergence from finite quadratic variation

- ID: `durrett_ch8_martingale_convergence_variance_sum`

- Section: 8.2 CLTs for Martingales

- Kind: theorem

- Summary: A square-integrable martingale with finite total conditional variance has an almost sure finite limit.

- Proof idea: Use L2 boundedness, Doob convergence ideas, and the sum of conditional second moments.

- Exam use: A standard way to separate negligible martingale tails from the main CLT-scale variance.

- Pitfall: Finite expected total variance is stronger than merely having bounded increments.

- Tags: martingale-convergence, quadratic-variation, l2

### Martingale functional CLT by random clock

- ID: `durrett_ch8_martingale_fclt_random_clock`

- Section: 8.2 CLTs for Martingales

- Kind: theorem

- Summary: For a martingale-difference array, if the embedded Brownian clock converges to deterministic time and large jumps vanish, the interpolated martingale converges to Brownian motion.

- Proof idea: Use Skorokhod embedding, control the random time change, and prove the embedded path is close to Brownian motion.

- Exam use: The process-level version of the martingale CLT; use when partial-sum paths rather than only final sums appear.

- Pitfall: The theorem needs both variance-clock convergence and a Lindeberg-type no-large-jumps condition.

- Tags: martingale-fclt, random-clock, lindeberg, brownian-motion

### Lindeberg-Feller condition for martingales

- ID: `durrett_ch8_martingale_lindeberg_feller`

- Section: 8.2 CLTs for Martingales

- Kind: theorem

- Summary: A martingale-difference array has a normal limit when its conditional variances converge to 1 and its conditional large-jump contribution vanishes.

- Proof idea: Truncate the array, embed the truncated martingale, and show the discarded part is negligible.

- Exam use: High-yield theorem for dependent CLTs where conditional means are zero.

- Pitfall: Ordinary variance convergence is not enough; the conditional variance process must stabilize.

- Tags: martingale-clt, lindeberg-condition, conditional-variance, triangular-array

### Martingale central limit theorem

- ID: `durrett_ch8_martingale_clt_final_form`

- Section: 8.2 CLTs for Martingales

- Kind: theorem

- Summary: A martingale-difference sequence normalized by its variance has a normal limit under conditional variance convergence and conditional Lindeberg conditions.

- Proof idea: Reduce the sequence to a triangular array and apply the martingale Lindeberg-Feller theorem.

- Exam use: Use for sums of dependent variables after decomposing them into martingale differences.

- Pitfall: Verify the filtration and conditional mean-zero property before applying the theorem.

- Tags: martingale-clt, normal-limit, filtration, conditional-lindeberg

### Stationary sequence CLT through martingale approximation

- ID: `durrett_ch8_stationary_coboundary_clt`

- Section: 8.3 CLTs for Stationary Sequences

- Kind: theorem

- Summary: For an ergodic stationary square-integrable sequence, a CLT can be proved when the partial sums are well approximated by a martingale with stationary differences.

- Proof idea: Decompose X_n into a martingale difference plus a small coboundary or negligible remainder, then apply the martingale CLT.

- Exam use: Main strategy for dependent stationary sequences on prelim-style problems.

- Pitfall: Ergodicity and square integrability do not by themselves guarantee a CLT; the approximation condition matters.

- Tags: stationary-sequence, martingale-approximation, ergodic, clt

### Projective criterion for stationary CLT

- ID: `durrett_ch8_projective_stationary_clt`

- Section: 8.3 CLTs for Stationary Sequences

- Kind: criterion

- Summary: If conditional projections of future partial sums are summable or suitably controlled, stationary centered sequences satisfy a CLT with variance from the martingale approximation.

- Proof idea: Use conditional expectations relative to the natural filtration to build martingale differences and bound the error.

- Exam use: A practical check for dependent sequences where conditioning on the past becomes small.

- Pitfall: Do not replace the projective condition by ordinary covariance decay unless a theorem justifies it.

- Tags: projective-criterion, stationary, conditional-expectation, clt

### M-dependent stationary CLT

- ID: `durrett_ch8_m_dependent_clt`

- Section: 8.3 CLTs for Stationary Sequences

- Kind: example-pattern

- Summary: For a centered stationary M-dependent sequence, the normalized sum has a normal limit with long-run variance sigma^2 = E X_0^2 + 2 sum_{k=1}^M E X_0 X_k.

- Proof idea: Group variables into blocks or use the stationary martingale approximation theorem; dependence disappears past lag M.

- Exam use: Fast recognition pattern for finite-range dependence problems.

- Pitfall: The limiting variance can be zero; in that case the usual nondegenerate normal limit collapses.

- Tags: m-dependent, stationary, long-run-variance, clt

### Markov-chain CLT via Poisson equation

- ID: `durrett_ch8_markov_chain_poisson_equation_clt`

- Section: 8.3 CLTs for Stationary Sequences

- Kind: example-pattern

- Summary: For a stationary ergodic Markov chain, additive functionals can satisfy a CLT when f is represented through a solution of a Poisson equation, producing a martingale plus a telescoping error.

- Proof idea: Write f = g - P g plus a martingale increment, then show the boundary terms are negligible after sqrt(n) scaling.

- Exam use: Use when a dependent sum is generated by a Markov transition kernel.

- Pitfall: Stationarity or a controlled initial distribution is needed; starting far from equilibrium can add transient terms.

- Tags: markov-chain, poisson-equation, additive-functional, martingale-approximation

### Moving-average process CLT

- ID: `durrett_ch8_moving_average_clt`

- Section: 8.3 CLTs for Stationary Sequences

- Kind: example-pattern

- Summary: Linear moving averages of iid innovations satisfy CLTs under coefficient conditions that make the process square integrable and approximable by finite-dependent truncations.

- Proof idea: Approximate the infinite moving average by an M-dependent one and control the L2 error of the remainder.

- Exam use: A standard dependent but explicit model where long-run variance can often be computed.

- Pitfall: Absolute or square summability assumptions on coefficients are not cosmetic; they justify truncation and variance formulas.

- Tags: moving-average, linear-process, m-dependent-approximation, clt

### Mixing covariance inequality

- ID: `durrett_ch8_mixing_covariance_inequality`

- Section: 8.3.1 Mixing Properties

- Kind: lemma

- Summary: Mixing coefficients bound covariances between variables measurable with respect to separated sigma-fields, with Holder exponents controlling integrability.

- Proof idea: Approximate indicators and apply Holder-type bounds using the distance between joint and product probabilities.

- Exam use: Converts abstract mixing assumptions into summable covariance or projection bounds for CLTs.

- Pitfall: Check the exact mixing coefficient and exponent relation; different texts use different normalizations.

- Tags: mixing, covariance-bound, holder, dependence

### Strong-mixing stationary CLT

- ID: `durrett_ch8_strong_mixing_stationary_clt`

- Section: 8.3.1 Mixing Properties

- Kind: theorem

- Summary: A centered ergodic stationary sequence satisfying suitable moment and summable mixing conditions obeys a CLT with long-run variance given by the covariance series.

- Proof idea: Use the mixing covariance inequality to verify the projective or martingale-approximation criterion.

- Exam use: Use for dependent sequences when decay of dependence is given quantitatively.

- Pitfall: Moment assumptions and summability rates are paired; weakening one often requires strengthening the other.

- Tags: strong-mixing, stationary-clt, long-run-variance, covariance-series

### Glivenko-Cantelli theorem

- ID: `durrett_ch8_glivenko_cantelli_uniform`

- Section: 8.4 Empirical Distributions, Brownian Bridge

- Kind: theorem

- Summary: The empirical distribution function F_n converges uniformly almost surely to the true distribution function F.

- Proof idea: Reduce to the uniform distribution by the probability integral transform, then control finitely many grid intervals and use monotonicity.

- Exam use: The baseline consistency result for empirical CDFs before studying sqrt(n) fluctuations.

- Pitfall: Pointwise LLN is not enough; the theorem gives uniform convergence over all x.

- Tags: empirical-distribution, glivenko-cantelli, uniform-convergence, cdf

### Empirical process convergence to Brownian bridge

- ID: `durrett_ch8_empirical_process_bridge`

- Section: 8.4 Empirical Distributions, Brownian Bridge

- Kind: theorem

- Summary: For uniform samples, sqrt(n)(F_n(t)-t) converges as a process to the Brownian bridge B_t - t B_1.

- Proof idea: Represent F_n through uniform order statistics or multinomial increments and apply Donsker with the endpoint pinned.

- Exam use: Foundation for Kolmogorov-Smirnov statistics and distribution-free empirical-process limits.

- Pitfall: The limit is a bridge, not free Brownian motion, because the empirical CDF is pinned at 0 and 1.

- Tags: empirical-process, brownian-bridge, donsker, uniform-order-statistics

### Kolmogorov-Smirnov statistic limit

- ID: `durrett_ch8_kolmogorov_smirnov_limit`

- Section: 8.4 Empirical Distributions, Brownian Bridge

- Kind: theorem

- Summary: The statistic D_n = sqrt(n) sup_x |F_n(x)-F(x)| converges to sup_{0<=t<=1} |B_t - t B_1| for continuous F.

- Proof idea: Use the probability integral transform and the continuous mapping theorem applied to the empirical process.

- Exam use: Identifies the asymptotic null distribution of the Kolmogorov-Smirnov goodness-of-fit statistic.

- Pitfall: Continuity of F gives distribution-free uniformization; atoms require separate handling.

- Tags: kolmogorov-smirnov, brownian-bridge, empirical-cdf, supremum

### Brownian bridge as pinned Brownian motion

- ID: `durrett_ch8_brownian_bridge_conditioning`

- Section: 8.4 Empirical Distributions, Brownian Bridge

- Kind: construction

- Summary: The Brownian bridge has the same law as B_t - t B_1 on [0,1], equivalently Brownian motion conditioned to return to 0 at time 1.

- Proof idea: Compute Gaussian means and covariances, or use Markov transition densities and conditioning on B_1=0.

- Exam use: Use to compute bridge covariance, Markov transition laws, and empirical-process limits.

- Pitfall: Conditioning on an event of probability zero is shorthand for a regular conditional or limiting density argument.

- Tags: brownian-bridge, gaussian-process, conditioning, empirical-process

### Kolmogorov distribution by killed Brownian motion

- ID: `durrett_ch8_kolmogorov_distribution_method`

- Section: 8.4 Empirical Distributions, Brownian Bridge

- Kind: proof-template

- Summary: The distribution of sup |Brownian bridge| can be computed from Brownian motion killed on exiting an interval and then pinned at time 1.

- Proof idea: Use reflection or eigenfunction expansions for Brownian transition densities with absorbing barriers, then condition to form the bridge.

- Exam use: Useful when an exam asks not just for the KS limit but for its explicit distribution.

- Pitfall: Keep straight whether the boundary event is one-sided or two-sided; the formulas differ.

- Tags: kolmogorov-distribution, killed-brownian-motion, brownian-bridge, reflection-principle

### Law of the iterated logarithm for Brownian motion

- ID: `durrett_ch8_brownian_lil`

- Section: 8.5 Laws of the Iterated Logarithm

- Kind: theorem

- Summary: Brownian motion satisfies limsup_{t->infty} B_t / sqrt(2 t log log t) = 1 almost surely, with the corresponding liminf equal to -1.

- Proof idea: Prove upper and lower bounds on a geometric time grid using Gaussian tails, Borel-Cantelli, and control between grid points.

- Exam use: The Brownian template for LILs of partial sums after embedding or invariance principles.

- Pitfall: The log log term is meaningful only in the eventual range where it is positive; constants are sharp.

- Tags: lil, brownian-motion, borel-cantelli, gaussian-tail

### Law of the iterated logarithm for iid sums

- ID: `durrett_ch8_iid_lil`

- Section: 8.5 Laws of the Iterated Logarithm

- Kind: theorem

- Summary: For iid mean-zero finite-variance increments with variance sigma^2, limsup S_n / sqrt(2 sigma^2 n log log n) = 1 almost surely, and the liminf is -1.

- Proof idea: Embed the random walk in Brownian motion and show the random clock is close enough to n for Brownian LIL scaling.

- Exam use: Use when a problem asks for sharp almost-sure fluctuation size of partial sums.

- Pitfall: A CLT-scale heuristic is too small for limsup behavior; LIL has an extra sqrt(log log n) factor.

- Tags: lil, iid, random-walk, finite-variance

### Strassen invariance principle

- ID: `durrett_ch8_strassen_invariance_principle`

- Section: 8.5 Laws of the Iterated Logarithm

- Kind: theorem

- Summary: The set of subsequential limit points of suitably LIL-rescaled partial-sum paths is the unit ball of absolutely continuous functions with square-integrable derivative.

- Proof idea: Use strong approximation ideas to transfer Brownian compact LIL behavior to partial sums.

- Exam use: A functional strengthening of the scalar LIL; it describes the whole path shape, not just limsup constants.

- Pitfall: The limit set is deterministic and compact in path space; it is not a single limiting process.

- Tags: strassen, functional-lil, invariance-principle, path-limit-set

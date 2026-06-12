# Durrett Chapter 2 LLM Viki: Laws of Large Numbers

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter2.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

## Section Guides

### 2.1 Independence

- Goal: Move fluently between event, random-variable, sigma-field, product-law, and convolution formulations of independence.

- Must master: event independence, sigma-field independence, pi-lambda extension, product joint laws, convolution

- Prelim angle: Independence is the hidden engine behind LLN, Borel-Cantelli, random walks, and large-deviation calculations.

### 2.2 Weak Laws of Large Numbers

- Goal: Prove convergence in probability of averages using Chebyshev, triangular arrays, and truncation.

- Must master: L2 WLLN, iid finite-mean WLLN, triangular arrays, truncation, tail-sum identities, moving centering

- Prelim angle: High-frequency source of proof problems where the key is choosing the right normalization and moment/tail condition.

### 2.3 Borel-Cantelli Lemmas

- Goal: Convert summability or independence of events into almost sure eventual or infinitely-often statements.

- Must master: limsup events, first Borel-Cantelli, second Borel-Cantelli, Kochen-Stone, convergence in probability metric, maxima criteria

- Prelim angle: Often appears as the final almost-sure step after Markov/Chebyshev/exponential estimates.

### 2.4 Strong Law of Large Numbers

- Goal: Understand how maximal inequalities, truncation, and Borel-Cantelli upgrade weak averaging to almost sure averaging.

- Must master: Kolmogorov maximal inequality, variance convergence criterion, iid finite-mean SLLN, renewal reward ratios, log-growth optimization

- Prelim angle: A central theorem and proof template; exams often ask for variants rather than the exact theorem.

### 2.5 Convergence of Random Series

- Goal: Diagnose almost sure convergence of independent random series by separating jumps, drift, and centered fluctuations.

- Must master: three-series theorem, large jumps, truncated means, summable variances, Levy maximal inequality, random power-series radius

- Prelim angle: Useful for series examples, convergence-in-probability upgrades, and recognizing why finite-mean assumptions matter.

### 2.6 Renewal Theory

- Goal: Use LLN ideas in counting processes and solve renewal equations for long-run limits.

- Must master: renewal process, elementary renewal theorem, renewal equation, key renewal theorem, age and residual life, alternating renewal

- Prelim angle: Important for applied long-run rates, waiting-time distributions, availability, and renewal density limits.

### 2.7 Large Deviations

- Goal: Compute exponential decay rates for sums using moment generating functions, Chernoff bounds, and tilting.

- Must master: superadditivity, concavity of gamma, Chernoff bound, exponential tilting, Cramer rate formula, one big jump lower bounds

- Prelim angle: Gives sharp tail exponents and contrasts light-tailed Cramer behavior with heavy-tailed subexponential behavior.

## Knowledge Pieces

### Independence of events

- ID: `durrett_ch2_event_independence`

- Section: 2.1 Independence

- Kind: definition

- Summary: Events A and B are independent when P(A intersect B) = P(A)P(B); finite families require the product formula for every subfamily.

- Proof idea: The definition is designed so multiplication of probabilities replaces intersection probabilities.

- Exam use: Use it as the base language for indicator arguments, Borel-Cantelli, and pairwise-versus-mutual independence examples.

- Pitfall: Pairwise independence does not imply mutual independence; always check all finite subcollections when the statement says independent.

- Tags: independence, events, pairwise-vs-mutual

### Random variables and sigma-field independence

- ID: `durrett_ch2_rv_sigma_independence`

- Section: 2.1 Independence

- Kind: theorem

- Summary: Random variables are independent exactly when their generated sigma-fields are independent; measurable variables inside independent sigma-fields are independent.

- Proof idea: Translate events about X and Y into sets in sigma(X) and sigma(Y), then apply the definition of sigma-field independence.

- Exam use: Lets you move cleanly between event, random-variable, and information-field formulations.

- Pitfall: Do not confuse uncorrelated with independent; zero covariance is far weaker.

- Tags: independence, sigma-field, random-variables

### Indicators encode event independence

- ID: `durrett_ch2_indicator_independence`

- Section: 2.1 Independence

- Kind: fact

- Summary: Events A and B are independent if and only if their indicators 1_A and 1_B are independent random variables.

- Proof idea: The indicators take only values 0 and 1, so checking their joint probabilities reduces to A, B, and complements.

- Exam use: Useful when converting event problems into expectation or covariance calculations.

- Pitfall: Independence of indicators is stronger than merely E[1_A 1_B] being computable; it is equivalent here because the variables are binary.

- Tags: indicators, events, independence

### Pi-lambda independence extension

- ID: `durrett_ch2_pi_lambda_independence`

- Section: 2.1.1 Sufficient Conditions for Independence

- Kind: proof-template

- Summary: If independent collections are pi-systems, then the sigma-fields they generate are independent.

- Proof idea: Fix all but one coordinate and show the class of sets preserving the product formula is a lambda-system; apply the pi-lambda theorem repeatedly.

- Exam use: High-value proof method for showing independence from checking rectangles, half-lines, or finite-dimensional cylinder sets.

- Pitfall: The checked classes must be pi-systems and must generate the desired sigma-fields.

- Tags: pi-lambda, generators, independence

### Independence of blocks

- ID: `durrett_ch2_independent_blocks`

- Section: 2.1.1 Sufficient Conditions for Independence

- Kind: theorem

- Summary: Disjoint blocks built from independent families are independent after taking generated sigma-fields.

- Proof idea: Group variables into sigma-fields generated by each block and use the independence extension theorem.

- Exam use: Use this to show X_1 is independent of functions of X_2,...,X_n, or that future increments are independent of past events.

- Pitfall: The blocks must be formed from disjoint subfamilies of an independent family.

- Tags: blocks, sigma-fields, independent-families

### Functions of independent blocks

- ID: `durrett_ch2_functions_of_independent_blocks`

- Section: 2.1.1 Sufficient Conditions for Independence

- Kind: theorem

- Summary: Measurable functions of disjoint independent blocks remain independent.

- Proof idea: Each function is measurable with respect to the sigma-field generated by its block; independent sigma-fields pass independence to their measurable variables.

- Exam use: Essential for random walks: past maxima and future increments can be separated.

- Pitfall: The functions may be complicated, but they cannot reuse variables from another block.

- Tags: measurable-functions, blocks, random-walk

### Independent variables have product joint law

- ID: `durrett_ch2_joint_law_product_measure`

- Section: 2.1.2 Independence, Distribution, and Expectation

- Kind: theorem

- Summary: If X_1,...,X_n are independent with laws mu_i, then the joint law of the vector is the product measure mu_1 x ... x mu_n.

- Proof idea: Check equality on measurable rectangles and extend by the pi-lambda theorem.

- Exam use: Turns independence questions into product-measure integration questions.

- Pitfall: Matching marginal laws alone never proves independence; the joint law must factor.

- Tags: joint-law, product-measure, independence

### Expectation factorization under independence

- ID: `durrett_ch2_expectation_factorization`

- Section: 2.1.2 Independence, Distribution, and Expectation

- Kind: theorem

- Summary: If X and Y are independent, then E[h(X,Y)] is the product-measure integral; in particular E[f(X)g(Y)] = E[f(X)]E[g(Y)] under nonnegative or integrable hypotheses.

- Proof idea: Use the product joint law and Fubini/Tonelli.

- Exam use: Core tool for variance of sums, covariance checks, moment computations, and LLN proofs.

- Pitfall: The factorization needs independence and integrability/nonnegativity; linearity of expectation alone is not enough for products.

- Tags: expectation, factorization, fubini

### Convolution of distribution functions

- ID: `durrett_ch2_convolution_cdf`

- Section: 2.1.3 Sums of Independent Random Variables

- Kind: formula

- Summary: For independent X and Y with CDFs F and G, P(X+Y <= z) = integral F(z-y) dG(y).

- Proof idea: Integrate the indicator 1{x+y <= z} against the product law and evaluate the inner integral.

- Exam use: Use for distribution of sums when densities are absent or mixed.

- Pitfall: The notation dG means integration with respect to the probability measure induced by G, not ordinary differentiation unless a density exists.

- Tags: convolution, cdf, sum

### Convolution density formula

- ID: `durrett_ch2_convolution_density`

- Section: 2.1.3 Sums of Independent Random Variables

- Kind: formula

- Summary: If X has density f and Y is independent with law G, then X+Y has density h(x)= integral f(x-y)dG(y); if Y has density g, h=f*g.

- Proof idea: Start from the CDF convolution and use Tonelli to identify the derivative/density.

- Exam use: Standard way to compute sums of exponentials, normals, and mixed variables.

- Pitfall: Keep the order x-y straight and check that the variables are independent.

- Tags: convolution, density, sum

### Standard convolution examples

- ID: `durrett_ch2_standard_convolution_examples`

- Section: 2.1.3 Sums of Independent Random Variables

- Kind: example-bank

- Summary: Independent exponentials with the same rate give gamma/Erlang sums; independent normals add means and variances.

- Proof idea: Use the convolution density formula and complete the square for normals.

- Exam use: These are quick recognition patterns for prelim computations and later CLT comparisons.

- Pitfall: Normal parameters vary by text; in Durrett normal(mu,a) uses variance parameter a.

- Tags: normal, exponential, convolution

### Constructing independent random variables

- ID: `durrett_ch2_construct_independent_variables`

- Section: 2.1.4 Constructing Independent Random Variables

- Kind: construction

- Summary: Finite independent variables with prescribed laws live on a product space with coordinate maps; infinite sequences use infinite product measures and cylinder sets.

- Proof idea: Define probabilities on rectangles/cylinders by products of the marginal laws and extend.

- Exam use: Important when a proof begins with 'let X_1,X_2,... be independent with laws ...'; this construction justifies existence.

- Pitfall: Infinite product constructions are subtler than finite products; do not treat all subsets of R^N as measurable.

- Tags: construction, product-space, iid

### L2 weak law of large numbers

- ID: `durrett_ch2_weak_law_l2`

- Section: 2.2.1 L2 Weak Laws

- Kind: theorem

- Summary: For uncorrelated variables with bounded average variance, (S_n - E S_n)/n converges to 0 in L2 and hence in probability.

- Proof idea: Compute Var(S_n) as the sum of variances and apply Chebyshev.

- Exam use: Fastest LLN proof when second moments are available.

- Pitfall: Independence is sufficient but not necessary; uncorrelatedness plus variance control is enough.

- Tags: weak-law, l2, chebyshev

### IID finite variance weak law

- ID: `durrett_ch2_iid_finite_variance_wlln`

- Section: 2.2.1 L2 Weak Laws

- Kind: corollary

- Summary: If X_i are iid with finite variance and mean mu, then S_n/n converges to mu in probability.

- Proof idea: Apply the L2 weak law with Var(S_n/n)=Var(X_1)/n.

- Exam use: The canonical first LLN proof; use it whenever the problem gives second moments.

- Pitfall: This proof does not cover infinite-variance variables, even when the mean exists.

- Tags: iid, finite-variance, weak-law

### Triangular array weak law

- ID: `durrett_ch2_triangular_array_wlln`

- Section: 2.2.2 Triangular Arrays

- Kind: theorem

- Summary: For row-wise independent triangular arrays, convergence of sums follows when row variances are small and large jumps are controlled.

- Proof idea: Use truncation indicators plus Chebyshev on the truncated centered row sum.

- Exam use: This is the flexible form behind many LLN proofs with changing distributions.

- Pitfall: Rows are independent within each n; do not assume one infinite sequence unless the problem states it.

- Tags: triangular-array, weak-law, truncation

### Truncation method for weak laws

- ID: `durrett_ch2_truncation_method`

- Section: 2.2.3 Truncation

- Kind: proof-template

- Summary: Replace X_i by X_i 1{|X_i| <= cutoff}, prove a law for the bounded part, and show discarded large jumps are negligible.

- Proof idea: Bound the probability of any large jump by a union bound and control the truncated variance or expectation.

- Exam use: Main route from finite variance LLN to finite mean LLN.

- Pitfall: Choose the cutoff at the scale of the sum, often n or epsilon n; a fixed cutoff usually proves the wrong statement.

- Tags: truncation, weak-law, large-jumps

### IID finite mean weak law

- ID: `durrett_ch2_iid_finite_mean_wlln`

- Section: 2.2.3 Truncation

- Kind: theorem

- Summary: If X_i are iid with E|X_1| < infinity and mean mu, then S_n/n converges to mu in probability.

- Proof idea: Truncate at scale n, show the truncated centered average has small variance, and show large terms occur with vanishing probability.

- Exam use: This is the weak law most often needed when only integrability is assumed.

- Pitfall: Finite mean is enough for WLLN but the proof requires controlling both tails and centering errors.

- Tags: iid, finite-mean, weak-law

### Maximum term negligibility

- ID: `durrett_ch2_max_negligible_condition`

- Section: 2.2.3 Truncation

- Kind: criterion

- Summary: For iid integrable variables, max_{i<=n}|X_i|/n goes to 0 in probability.

- Proof idea: Use the union bound n P(|X_1| > epsilon n) and the tail property implied by integrability.

- Exam use: Often proves that no single observation can dominate the average.

- Pitfall: The statement can fail for heavy tails without finite first moment.

- Tags: max-term, tail-bound, integrability

### Weak law example patterns

- ID: `durrett_ch2_poissonization_and_wlln_examples`

- Section: 2.2 Weak Laws of Large Numbers

- Kind: example-bank

- Summary: Chapter 2 uses weak laws to control averages, random counts, and approximations where variance estimates or truncation make the error vanish.

- Proof idea: Reduce the target to a normalized sum and apply Chebyshev, triangular arrays, or truncation.

- Exam use: Use this as a mental index for prelim questions asking for convergence in probability.

- Pitfall: First identify the normalization; the wrong scale can make a true statement look false.

- Tags: examples, weak-law, convergence-in-probability

### Weighted Cesaro variance weak law

- ID: `durrett_ch2_weighted_variance_cesaro_wlln`

- Section: 2.2.1 L2 Weak Laws

- Kind: exercise-pattern

- Summary: If uncorrelated variables satisfy var(X_i)/i -> 0, then n^{-2} sum_{i<=n} var(X_i) -> 0, so the centered average converges to 0 in L2.

- Proof idea: Write var(X_i)=i a_i with a_i -> 0 and split the weighted Cesaro average into a finite initial block plus a small tail.

- Exam use: Exercise 2.2.1 pattern: use when variances grow sublinearly rather than being uniformly bounded.

- Pitfall: Do not require identical distributions; the deterministic centering is E S_n/n, not necessarily a fixed mean.

- Tags: weighted-cesaro, variance, weak-law

### Dependent covariance weak law

- ID: `durrett_ch2_dependent_covariance_wlln`

- Section: 2.2.1 L2 Weak Laws

- Kind: exercise-pattern

- Summary: A zero-mean sequence can satisfy a weak law even when dependent, provided lag covariances are bounded above by r(k) with r(k)->0.

- Proof idea: Expand E(S_n^2), group cross terms by lag, and use a finite-lag/tail split before applying Chebyshev.

- Exam use: Exercise 2.2.2 pattern: independence is not the real requirement; small average covariance is.

- Pitfall: The hypothesis is an upper bound without absolute values, so use it to control E(S_n^2) from above rather than proving absolute summability.

- Tags: dependent, covariance, weak-law

### Monte Carlo integration via WLLN

- ID: `durrett_ch2_monte_carlo_integration_wlln`

- Section: 2.2.1 L2 Weak Laws

- Kind: application

- Summary: For iid uniform U_i and integrable f on [0,1], the sample average n^{-1} sum f(U_i) converges in probability to integral_0^1 f.

- Proof idea: Apply the finite-mean weak law to Y_i=f(U_i); if f is square-integrable, Chebyshev gives variance-scale error bounds.

- Exam use: Exercise 2.2.3 pattern: translate numerical integration into an average of iid random variables.

- Pitfall: The finite-variance Chebyshev bound at threshold a/sqrt(n) is order Var(f(U))/a^2, not a vanishing bound unless the threshold is fixed.

- Tags: monte-carlo, integration, chebyshev

### Oscillating heavy tails can have finite effective centering

- ID: `durrett_ch2_oscillating_heavy_tail_centering`

- Section: 2.2.3 Truncation

- Kind: exercise-pattern

- Summary: A distribution may have infinite absolute mean but a convergent truncated mean, allowing S_n/n to converge in probability to a finite constant.

- Proof idea: Verify x P(|X|>x)->0, apply the truncation weak law, then show the truncated means converge, often by an alternating series test.

- Exam use: Exercise 2.2.4 pattern: cancellation in signs can produce a finite weak-law center even when E|X| is infinite.

- Pitfall: Do not call the limiting center EX unless the positive and negative parts are both finite.

- Tags: heavy-tail, truncated-mean, alternating-series

### Diverging truncated-mean weak law

- ID: `durrett_ch2_diverging_truncated_mean_wlln`

- Section: 2.2.3 Truncation

- Kind: exercise-pattern

- Summary: If xP(|X|>x)->0 but EX is infinite, the averages can still satisfy S_n/n - mu_n -> 0 with mu_n=E[X 1{|X|<=n}] diverging.

- Proof idea: The truncation theorem controls fluctuations around the moving center; monotone convergence or tail integration identifies mu_n -> infinity.

- Exam use: Exercise 2.2.5 pattern: separate weak-law concentration from existence of a finite mean.

- Pitfall: A moving centering sequence is not the same as convergence of S_n/n to a finite constant.

- Tags: truncated-mean, infinite-mean, weak-law

### Integer-valued tail-sum moment formulas

- ID: `durrett_ch2_integer_tail_sum_moments`

- Section: 2.2.3 Truncation

- Kind: formula

- Summary: For nonnegative integer-valued X, E X=sum_{n>=1}P(X>=n) and E X^2=sum_{n>=1}(2n-1)P(X>=n).

- Proof idea: Write k as sum_{n<=k}1 and k^2 as sum_{n<=k}(2n-1), then apply Tonelli to indicators.

- Exam use: Exercise 2.2.6 pattern: convert moments into tail sums for discrete heavy-tail checks.

- Pitfall: Use >= n for integer variables; continuous formulas use integrals with P(X>t) or P(X>=t), which differ only on negligible sets in many settings.

- Tags: tail-sum, integer-valued, moments

### General tail integral transform

- ID: `durrett_ch2_general_tail_integral_transform`

- Section: 2.2.3 Truncation

- Kind: formula

- Summary: If H(x)=integral_{(-infty,x]} h(y)dy with h>=0, then E H(X)=integral h(y)P(X>=y)dy.

- Proof idea: Write H(X) as an integral of h(y)1{y<=X} and apply Tonelli.

- Exam use: Exercise 2.2.7 pattern: derive exponential moment and tail identities without differentiating a distribution function.

- Pitfall: Nonnegativity of h is what makes Tonelli immediate; signed h needs integrability checks.

- Tags: tail-integral, tonelli, exponential-moment

### Unfair fair game truncation scale

- ID: `durrett_ch2_unfair_fair_game_truncation_scale`

- Section: 2.2.3 Truncation

- Kind: exercise-pattern

- Summary: For rare payoffs of size 2^k with probabilities about 1/(2^k k^2), truncation at b_n=2^{m(n)} can force S_n/(n/log_2 n) to converge to a negative constant despite EX=0.

- Proof idea: Pick b_n so large jumps are rare and truncated variance is small, then compute the missing positive tail as the dominant negative centering.

- Exam use: Exercise 2.2.8 pattern: a formally fair infinite-mean game can have typical averages far below its expectation.

- Pitfall: The expectation calculation is not enough; the typical scale is determined by truncation and the tail beyond b_n.

- Tags: fair-game, truncation-scale, infinite-mean

### Positive-variable self-normalized weak law

- ID: `durrett_ch2_positive_variable_self_normalized_wlln`

- Section: 2.2.3 Truncation

- Kind: exercise-pattern

- Summary: For nonnegative iid variables, if mu(s)/(s P(X>s))->infinity and b_n solves n mu(b_n)=b_n, then S_n/b_n -> 1 in probability.

- Proof idea: Apply the triangular-array truncation theorem: large jumps vanish by the nu(s) condition, truncated variance is controlled by a tail-integral split, and the truncated mean equals b_n.

- Exam use: Exercise 2.2.9 pattern: choose the normalization from the truncated first moment rather than from a finite mean.

- Pitfall: The proof depends on b_n tending to infinity and on controlling xP(X>x) relative to mu(x); do not assume finite mean.

- Tags: positive-variables, self-normalization, truncation

### First Borel-Cantelli lemma

- ID: `durrett_ch2_borel_cantelli_first`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: theorem

- Summary: If sum P(A_n) < infinity, then P(A_n infinitely often)=0.

- Proof idea: Bound P(union_{n>=m} A_n) by the tail sum and let m go to infinity.

- Exam use: Use to prove almost sure eventual bounds from summable probability estimates.

- Pitfall: No independence is needed for the first lemma.

- Tags: borel-cantelli, summability, almost-sure

### Second Borel-Cantelli lemma

- ID: `durrett_ch2_borel_cantelli_second`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: theorem

- Summary: For independent events, if sum P(A_n)=infinity, then P(A_n infinitely often)=1.

- Proof idea: Use independence to bound the probability that none of A_m,...,A_n occur by a product and then by an exponential of the negative probability sum.

- Exam use: Use to prove infinitely many successes, recurrence-style events, and almost sure lower bounds.

- Pitfall: Independence or a suitable replacement is essential; divergence alone is not enough.

- Tags: borel-cantelli, independence, infinitely-often

### Limsup event interpretation

- ID: `durrett_ch2_limsup_events`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: definition

- Summary: The event {A_n infinitely often} is limsup A_n = intersection_m union_{n>=m} A_n.

- Proof idea: Rewrite 'infinitely often' as 'for every m there exists n>=m' and translate quantifiers to countable set operations.

- Exam use: Needed before applying Borel-Cantelli and for a.s. convergence arguments.

- Pitfall: Do not confuse limsup A_n with union_n A_n; limsup requires infinitely many occurrences.

- Tags: limsup, events, infinitely-often

### Summable tail bounds imply a.s. eventual control

- ID: `durrett_ch2_bc_tail_bounds`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: proof-template

- Summary: If P(|X_n| > a_n) is summable, then |X_n| <= a_n eventually almost surely.

- Proof idea: Apply first Borel-Cantelli to the events {|X_n| > a_n}.

- Exam use: A common one-line finish after Markov, Chebyshev, or exponential bounds.

- Pitfall: Summability of the bound matters; merely tending to zero gives convergence in probability, not a.s. eventual control.

- Tags: tail-bound, almost-sure, eventual-control

### Subsequence plus monotonicity upgrade

- ID: `durrett_ch2_subsequence_bc_upgrade`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: proof-template

- Summary: Prove almost sure convergence along a sparse subsequence using Borel-Cantelli, then control gaps by monotonicity or maximal bounds.

- Proof idea: Choose a subsequence making probabilities summable; bridge between subsequence times with deterministic or probabilistic estimates.

- Exam use: Appears in strong law proofs and renewal estimates.

- Pitfall: The bridge is the hard part; convergence on a subsequence alone usually does not imply full convergence.

- Tags: subsequence, borel-cantelli, strong-law

### Independent trials occur infinitely often

- ID: `durrett_ch2_bc_independent_trials`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: example-pattern

- Summary: For independent events with non-summable probabilities, the events occur infinitely often with probability one.

- Proof idea: Apply the second Borel-Cantelli lemma directly.

- Exam use: Useful for coin-flip patterns, record events, and rare-event recurrence questions.

- Pitfall: Verify mutual independence or an acceptable independent-block structure, not just pairwise independence.

- Tags: independent-events, rare-events, infinitely-often

### Subsequence principle for convergence in probability

- ID: `durrett_ch2_probability_convergence_subsequence_principle`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: proof-template

- Summary: X_n -> X in probability iff every subsequence has a further subsequence converging to X almost surely.

- Proof idea: Choose a further subsequence with summable error probabilities and apply Borel-Cantelli; conversely use the topological subsequence criterion on probabilities.

- Exam use: Exercises 2.3.4-2.3.5 pattern: reduce convergence-in-probability limit theorems to almost sure subsequences.

- Pitfall: The almost sure subsequence depends on the original subsequence; this does not say the whole sequence converges a.s.

- Tags: convergence-in-probability, subsequence, borel-cantelli

### Continuous mapping for convergence in probability

- ID: `durrett_ch2_continuous_mapping_probability`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: If X_n -> X in probability and f is continuous, then f(X_n) -> f(X) in probability.

- Proof idea: Localize X to a compact set with high probability, use uniform continuity there, and control the complement.

- Exam use: Exercise 2.3.2 pattern: prove mapping results directly without invoking subsequences.

- Pitfall: Continuity only gives local uniform continuity after compact localization; global uniform continuity is not required.

- Tags: continuous-mapping, convergence-in-probability, compact-localization

### Fatou and dominated convergence from convergence in probability

- ID: `durrett_ch2_probability_fatou_dominated`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: Fatou and dominated convergence extend from a.s. convergence to convergence in probability by passing to a.s. convergent subsequences.

- Proof idea: Select a subsequence attaining the relevant liminf or violating the target limit, then extract an a.s. convergent further subsequence.

- Exam use: Exercises 2.3.4-2.3.5 pattern: combine subsequence extraction with Fatou, DCT, bounded convergence, or uniform integrability.

- Pitfall: For unbounded dominated-convergence variants, prove uniform integrability; convergence in probability alone is not enough for expectations.

- Tags: fatou, dominated-convergence, uniform-integrability

### Metric and completeness for convergence in probability

- ID: `durrett_ch2_probability_metric_complete`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: The metric E[|X-Y|/(1+|X-Y|)] metrizes convergence in probability, and random variables modulo a.s. equality are complete under it.

- Proof idea: Use the subadditivity of t/(1+t); for completeness choose a subsequence with summable jump probabilities and apply Borel-Cantelli to get an a.s. limit.

- Exam use: Exercises 2.3.6-2.3.7 pattern: turn Cauchy in probability into an a.s. Cauchy subsequence, then pull the whole sequence back by Cauchy control.

- Pitfall: The metric is on equivalence classes modulo a.s. equality; otherwise d(X,Y)=0 is only equality a.s.

- Tags: metric, complete-space, convergence-in-probability

### Kochen-Stone second-moment lower bound

- ID: `durrett_ch2_kochen_stone_second_moment`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: lemma

- Summary: If sum P(A_n)=infinity, then P(A_n i.o.) is bounded below by a limsup ratio of squared expected counts to second moments of event counts.

- Proof idea: Apply the second-moment inequality P(S_n>0) >= (ES_n)^2/E(S_n^2) to tail sums of indicators, then let the tail start go to infinity.

- Exam use: Exercise 2.3.10 pattern: prove lower bounds for infinitely-often events under dependence when full independence is unavailable.

- Pitfall: The denominator uses all pairwise intersections; replacing it by product probabilities is only valid under independence.

- Tags: kochen-stone, second-moment, dependent-events

### Bernoulli convergence via Borel-Cantelli

- ID: `durrett_ch2_bernoulli_bc_convergence`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: For independent Bernoulli variables X_n with P(X_n=1)=p_n, X_n -> 0 in probability iff p_n -> 0, and X_n -> 0 a.s. iff sum p_n < infinity.

- Proof idea: Translate convergence to occurrence of {X_n=1}; use first or second Borel-Cantelli.

- Exam use: Exercise 2.3.11 pattern: reduce binary convergence questions to summability of success probabilities.

- Pitfall: The a.s. direction needs independence for the divergent case.

- Tags: bernoulli, borel-cantelli, convergence

### On countable spaces, convergence in probability implies a.s. convergence

- ID: `durrett_ch2_countable_space_probability_to_as`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: If Omega is countable with all subsets measurable, convergence in probability implies pointwise convergence on all atoms of positive probability, hence almost sure convergence.

- Proof idea: A positive-mass point that fails pointwise convergence would keep an error probability bounded away from zero along a subsequence.

- Exam use: Exercise 2.3.12 pattern: use atoms to upgrade convergence modes.

- Pitfall: This relies on countability; it is false on general probability spaces.

- Tags: countable-space, atoms, convergence

### Arbitrary random variables can be normalized to zero a.s.

- ID: `durrett_ch2_arbitrary_normalization_bc`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: For any random variables X_n, one can choose deterministic c_n -> infinity so that X_n/c_n -> 0 almost surely.

- Proof idea: Pick c_n large enough that tail probabilities at finitely many rational error levels are summable, then diagonalize with Borel-Cantelli.

- Exam use: Exercise 2.3.13 pattern: build a normalization after seeing the sequence rather than using moment assumptions.

- Pitfall: The constants are not canonical and may grow very fast.

- Tags: normalization, diagonalization, borel-cantelli

### Independent supremum finiteness criterion

- ID: `durrett_ch2_independent_sup_finite_criterion`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: criterion

- Summary: For independent X_n, sup_n X_n is finite a.s. iff sum P(X_n>A)<infinity for some finite A.

- Proof idea: Use first Borel-Cantelli for sufficiency and second Borel-Cantelli over integer thresholds for necessity.

- Exam use: Exercise 2.3.14 pattern: characterize boundedness of an independent sequence by summability of one tail level.

- Pitfall: Independence is used only for the divergent necessity direction.

- Tags: supremum, tail-sum, independence

### Exponential maxima live at log n scale

- ID: `durrett_ch2_exponential_maxima_log_scale`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: example-pattern

- Summary: For iid exponential-tail variables with P(X>x)=e^{-x}, limsup X_n/log n=1 and max_{m<=n}X_m/log n -> 1 almost surely.

- Proof idea: Use Borel-Cantelli at thresholds (1+-epsilon)log n and estimate P(M_n <= (1-epsilon)log n) by an exponential bound.

- Exam use: Exercise 2.3.15 pattern: identify extreme-value scales via summable/nonsummable tail probabilities.

- Pitfall: Pointwise limsup and running maximum convergence require slightly different lower-bound arguments.

- Tags: maxima, exponential-tail, log-scale

### Threshold maxima infinitely-often criterion

- ID: `durrett_ch2_threshold_maxima_io`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: criterion

- Summary: For iid X_n and increasing thresholds lambda_n, max_{m<=n}X_m>lambda_n i.o. is equivalent to X_n>lambda_n i.o., hence controlled by sum tail probabilities.

- Proof idea: If individual threshold exceedances are summable, only finitely many observations can drive the maxima over increasing thresholds; if divergent, the individual exceedances occur i.o.

- Exam use: Exercise 2.3.16 pattern: reduce running-maximum events to one-time exceedance events when thresholds increase.

- Pitfall: The monotonicity lambda_n up to infinity is what prevents one early large value from causing infinitely many later exceedances.

- Tags: running-maximum, thresholds, borel-cantelli

### Single observations versus maxima under n-normalization

- ID: `durrett_ch2_iid_normalized_single_vs_max`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: criterion-card

- Summary: For iid Y_n, Y_n/n -> 0 a.s. needs E|Y_1|<infinity, max_{m<=n}Y_m/n -> 0 a.s. needs E(Y_1^+)<infinity, and max convergence in probability needs xP(Y_1>x)->0.

- Proof idea: Apply Borel-Cantelli to |Y_n|>epsilon n or Y_n>epsilon n; for maxima in probability use 1-(1-p_n)^n ->0 iff np_n->0.

- Exam use: Exercise 2.3.17 pattern: distinguish two-sided single-term control from one-sided running-maximum control.

- Pitfall: Almost sure and in-probability maxima have different tail requirements.

- Tags: iid, maxima, normalization

### Monotone variance subsequence a.s. upgrade

- ID: `durrett_ch2_monotone_variance_subsequence_as`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: proof-template

- Summary: For increasing nonnegative X_n with EX_n asymptotic to a n^alpha and variance O(n^beta), beta<2alpha, prove X_n/n^alpha -> a a.s. via sparse subsequences and monotonicity.

- Proof idea: Use Chebyshev on n_k=floor(k^r) with r(2alpha-beta)>1, Borel-Cantelli on the subsequence, then squeeze intermediate n by monotonicity.

- Exam use: Exercise 2.3.18 pattern: turn variance bounds into a.s. asymptotics when monotonicity bridges gaps.

- Pitfall: Without monotonicity, subsequence convergence alone would not control intermediate indices.

- Tags: variance-bound, monotonicity, almost-sure

### Poisson sums strong law with variable means

- ID: `durrett_ch2_poisson_sum_slln_series`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: For independent Poisson X_n with means lambda_n and m_n=sum_{k<=n}lambda_k -> infinity, S_n/m_n -> 1 almost surely.

- Proof idea: Apply the random-series convergence criterion to (X_n-lambda_n)/m_n, using sum lambda_n/m_n^2 < infinity, then Kronecker's lemma.

- Exam use: Exercise 2.3.19 pattern: use variance summability with the natural cumulative-mean scale.

- Pitfall: A naive subsequence proof can fail when the means have large jumps; the series proof handles arbitrary lambda_n.

- Tags: poisson, strong-law, kronecker

### St. Petersburg almost-sure limsup explosion

- ID: `durrett_ch2_st_petersburg_as_limsup`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: example-pattern

- Summary: In the St. Petersburg game, X_n/(n log_2 n) has infinite limsup almost surely, so the in-probability normalization for sums is not an a.s. law.

- Proof idea: For each M, the events {X_n >= M n log_2 n} have divergent probability sum and are independent; apply the second Borel-Cantelli lemma.

- Exam use: Exercise 2.3.20 pattern: rare giant jumps can destroy almost sure convergence even when weak-law scaling works.

- Pitfall: Convergence in probability of S_n/(n log n) does not control limsup behavior.

- Tags: st-petersburg, limsup, giant-jumps

### Kolmogorov maximal inequality

- ID: `durrett_ch2_kolmogorov_maximal_inequality`

- Section: 2.4 Strong Law of Large Numbers

- Kind: inequality

- Summary: For independent mean-zero variables with finite variances, the probability that partial sums exceed a threshold is bounded by the total variance divided by the threshold squared.

- Proof idea: Stop at the first crossing and use independence of the future increment to control E[S_n^2] on crossing events.

- Exam use: Main tool for upgrading variance summability to almost sure control of partial sums.

- Pitfall: The variables must be centered and independent; this is stronger than ordinary Chebyshev for the final sum.

- Tags: maximal-inequality, partial-sums, strong-law

### Kolmogorov convergence criterion

- ID: `durrett_ch2_kolmogorov_convergence_criterion`

- Section: 2.4 Strong Law of Large Numbers

- Kind: theorem

- Summary: If independent mean-zero variables have summable variances, then their series converges almost surely.

- Proof idea: Apply the maximal inequality to tails of the series and use Cauchy convergence almost surely.

- Exam use: Use for convergence of centered random series and as a strong-law building block.

- Pitfall: Summable variances are sufficient, not necessary; do not mistake it for a complete characterization.

- Tags: random-series, summable-variance, almost-sure

### Fourth-moment strong law shortcut

- ID: `durrett_ch2_iid_finite_fourth_slln`

- Section: 2.4 Strong Law of Large Numbers

- Kind: proof-template

- Summary: If iid centered variables have finite fourth moment, then S_n/n -> 0 almost surely by summable fourth-moment bounds.

- Proof idea: Bound E[S_n^4] by a constant times n^2 and sum P(|S_n| > epsilon n) over n.

- Exam use: A quick SLLN proof when high moments are available.

- Pitfall: This proof is convenient but much stronger than needed; finite first moment is enough for the iid SLLN.

- Tags: fourth-moment, strong-law, markov

### IID finite mean strong law

- ID: `durrett_ch2_iid_finite_mean_slln`

- Section: 2.4 Strong Law of Large Numbers

- Kind: theorem

- Summary: If X_i are iid and E|X_1| < infinity with mean mu, then S_n/n -> mu almost surely.

- Proof idea: Truncate variables, prove convergence for bounded/centered parts with maximal inequalities, and show tails are negligible via Borel-Cantelli.

- Exam use: Central theorem of the chapter and a frequent prelim target.

- Pitfall: Almost sure convergence is stronger than convergence in probability; the WLLN proof alone is not enough.

- Tags: strong-law, iid, finite-mean

### Strong law normalization habits

- ID: `durrett_ch2_slln_normalized_sums`

- Section: 2.4 Strong Law of Large Numbers

- Kind: concept-link

- Summary: Strong laws usually show a normalized centered sum tends to zero almost surely, then add back deterministic centering.

- Proof idea: Write S_n/n - mu as n^{-1} sum (X_i - mu) and focus on partial-sum control.

- Exam use: Helps organize proofs for arrays, subsequences, and renewal counting.

- Pitfall: Centering must be finite; if the mean is infinite, S_n/n behaves differently.

- Tags: normalization, centering, strong-law

### Renewal reward ratio via SLLN

- ID: `durrett_ch2_renewal_reward_ratio_slln`

- Section: 2.4 Strong Law of Large Numbers

- Kind: application

- Summary: For cycles with iid working time X_i and downtime Y_i, the long-run working fraction is E X_i/(E X_i+E Y_i).

- Proof idea: Apply the SLLN to cycle lengths X_i+Y_i and rewards X_i, invert cycle time to get N(t)/t, and squeeze the incomplete final cycle.

- Exam use: Exercise 2.4.1 pattern: renewal reward limits are ratios of mean reward to mean cycle length.

- Pitfall: Account for the possible incomplete cycle at time t; its contribution is negligible after division by t.

- Tags: renewal-reward, slln, long-run-fraction

### Multiplicative recursion becomes additive after logs

- ID: `durrett_ch2_multiplicative_recursion_log_slln`

- Section: 2.4 Strong Law of Large Numbers

- Kind: proof-template

- Summary: If a process satisfies |X_n|=product_{k<=n}R_k with iid positive factors and E|log R_1|<infinity, then n^{-1}log|X_n| -> E log R_1 a.s.

- Proof idea: Take logarithms and apply the finite-mean SLLN; compute the constant from the distribution of the radial factor.

- Exam use: Exercise 2.4.2 pattern: random scaling problems reduce to an SLLN for log radii.

- Pitfall: Check integrability near zero before applying the SLLN to logarithms.

- Tags: multiplicative-process, log-transform, slln

### Kelly-style investment growth optimization

- ID: `durrett_ch2_kelly_investment_concavity`

- Section: 2.4 Strong Law of Large Numbers

- Kind: application

- Summary: For fixed portfolio fraction p, long-run log wealth converges to c(p)=E log(ap+(1-p)V); c is concave in p and endpoint derivatives decide whether the optimum is interior.

- Proof idea: Write log wealth as a sum of iid log returns, apply the SLLN, then differentiate c(p) under the expectation and use concavity.

- Exam use: Exercise 2.4.3 pattern: optimize almost-sure exponential growth by maximizing expected log return.

- Pitfall: Maximizing expected wealth and maximizing expected log wealth are different criteria.

- Tags: investment, kelly, expected-log-growth

### Kolmogorov three-series theorem

- ID: `durrett_ch2_three_series_theorem`

- Section: 2.5 Convergence of Random Series

- Kind: theorem

- Summary: For independent variables, convergence of sum X_n is characterized by tail probabilities, truncated means, and truncated variances.

- Proof idea: Split each X_n into large jumps, truncated means, and centered truncated fluctuations; apply Borel-Cantelli and the variance convergence criterion.

- Exam use: The main checklist for almost sure convergence of independent random series.

- Pitfall: The theorem uses a fixed truncation level; changing the cutoff changes the conditions but not the spirit.

- Tags: three-series, random-series, truncation

### Large jumps in random series

- ID: `durrett_ch2_random_series_large_jumps`

- Section: 2.5 Convergence of Random Series

- Kind: criterion

- Summary: A necessary component for series convergence is that large jumps occur only finitely often, typically sum P(|X_n| > c) < infinity.

- Proof idea: If large jumps occur infinitely often, the terms cannot tend to zero; Borel-Cantelli gives the precise almost sure statement.

- Exam use: First diagnostic check in random-series problems.

- Pitfall: Termwise convergence to zero is necessary but not sufficient for series convergence.

- Tags: large-jumps, random-series, borel-cantelli

### Truncated centering in random series

- ID: `durrett_ch2_random_series_centering`

- Section: 2.5 Convergence of Random Series

- Kind: proof-template

- Summary: After removing large jumps, convergence depends on whether the truncated expectations form a convergent deterministic series.

- Proof idea: Separate X_n 1{|X_n| <= c} into its mean plus centered fluctuation.

- Exam use: Prevents hidden deterministic drift from spoiling almost sure convergence.

- Pitfall: A centered variance argument cannot control a divergent sum of means.

- Tags: centering, truncation, random-series

### Rates for random series tails

- ID: `durrett_ch2_series_rate_estimates`

- Section: 2.5.1 Rates of Convergence

- Kind: concept-link

- Summary: Once a random series converges, tail estimates can quantify how fast partial sums approach the limit.

- Proof idea: Combine maximal inequalities with variance or moment bounds on the remaining tail.

- Exam use: Useful when a problem asks not just convergence but an almost sure order estimate.

- Pitfall: A convergence theorem alone may not give the requested rate; track the size of tail variances or probabilities.

- Tags: rates, random-series, tail-estimates

### Infinite mean changes LLN behavior

- ID: `durrett_ch2_infinite_mean_behavior`

- Section: 2.5.2 Infinite Mean

- Kind: concept-link

- Summary: When the mean is infinite or undefined, normalized sums can diverge or be controlled by rare large terms rather than averaging.

- Proof idea: Use truncation to see which tail contribution dominates the normalization.

- Exam use: Important for spotting when a finite-mean LLN theorem cannot be applied.

- Pitfall: Do not center by EX if EX is not finite; the expression may be meaningless.

- Tags: infinite-mean, heavy-tail, truncation

### Renewal process basics

- ID: `durrett_ch2_renewal_process`

- Section: 2.6 Renewal Theory

- Kind: definition

- Summary: With iid positive interarrival times xi_i, renewal times T_n = xi_1+...+xi_n and count N(t)=max{n:T_n<=t} form a renewal process.

- Proof idea: The strong law gives T_n/n -> mu, which inverts to N(t)/t -> 1/mu under finite mean.

- Exam use: Connects laws of large numbers to counting processes and waiting-time problems.

- Pitfall: Be careful with indexing: some formulas use the last renewal before t and the next renewal after t.

- Tags: renewal-process, counting, slln

### Elementary renewal theorem

- ID: `durrett_ch2_elementary_renewal_theorem`

- Section: 2.6 Renewal Theory

- Kind: theorem

- Summary: For iid positive interarrival times with finite mean mu, E[N(t)]/t -> 1/mu.

- Proof idea: Use renewal decompositions and LLN-style bounds to compare the counting process with deterministic time.

- Exam use: Useful for expected counts in long-run systems.

- Pitfall: Almost sure convergence of N(t)/t and convergence of its expectation are related but require different arguments.

- Tags: renewal-theorem, expectation, long-run-rate

### Renewal equation

- ID: `durrett_ch2_renewal_equation`

- Section: 2.6 Renewal Theory

- Kind: formula

- Summary: Many renewal quantities satisfy H(t)=h(t)+ integral_0^t H(t-s)dF(s), where F is the interarrival distribution.

- Proof idea: Condition on the first renewal time; if it occurs at s, restart the process from t-s.

- Exam use: Primary modeling move for renewal reward, age, residual lifetime, and alternating renewal problems.

- Pitfall: The input function h and the renewal function must match the same convention for time zero.

- Tags: renewal-equation, conditioning, restart

### Key renewal theorem

- ID: `durrett_ch2_key_renewal_theorem`

- Section: 2.6 Renewal Theory

- Kind: theorem

- Summary: For nonarithmetic renewals and directly Riemann integrable h, renewal convolutions converge to (1/mu) integral h.

- Proof idea: The theorem refines the renewal equation asymptotically using smoothing properties of the renewal measure.

- Exam use: Use for limiting age, residual lifetime, and renewal reward calculations.

- Pitfall: Arithmetic interarrival distributions have lattice oscillations; the nonarithmetic hypothesis matters.

- Tags: key-renewal-theorem, nonarithmetic, asymptotics

### Superadditivity for large-deviation probabilities

- ID: `durrett_ch2_subadditive_log_probability`

- Section: 2.7 Large Deviations

- Kind: lemma

- Summary: For iid sums, pi_n=P(S_n>=na) satisfies pi_{m+n} >= pi_m pi_n, so log pi_n is superadditive and n^{-1}log pi_n has a limit.

- Proof idea: Use independence of S_m and S_{m+n}-S_m, then apply the superadditive sequence lemma.

- Exam use: Establishes existence of the exponential decay rate before computing it.

- Pitfall: The limit can be zero or negative infinity; existence alone does not guarantee a useful exponential bound.

- Tags: large-deviations, superadditivity, rate

### Chernoff exponential bound

- ID: `durrett_ch2_chernoff_bound`

- Section: 2.7 Large Deviations

- Kind: inequality

- Summary: If phi(theta)=E exp(theta X) is finite, then P(S_n>=na) <= exp(-n(a theta - log phi(theta))).

- Proof idea: Apply Markov's inequality to exp(theta S_n) and use independence to factor the moment generating function.

- Exam use: Main upper-bound engine for large-deviation estimates.

- Pitfall: Optimize over theta>0; a random unoptimized theta may prove decay but not the sharp rate.

- Tags: chernoff, mgf, large-deviations

### Exponential tilting

- ID: `durrett_ch2_exponential_tilting`

- Section: 2.7 Large Deviations

- Kind: construction

- Summary: The tilted law F_theta has density proportional to exp(theta x) relative to F, and its mean is phi'(theta)/phi(theta).

- Proof idea: Normalize exp(theta x)dF by phi(theta); differentiating log phi gives the tilted mean.

- Exam use: Used for the lower bound in Cramer-style large deviations by making the rare event typical.

- Pitfall: Tilting is only valid where the moment generating function is finite.

- Tags: exponential-tilting, mgf, change-of-measure

### Cramer rate formula in the smooth case

- ID: `durrett_ch2_cramer_rate_formula`

- Section: 2.7 Large Deviations

- Kind: theorem

- Summary: When a>mu and there is theta_a with a=phi'(theta_a)/phi(theta_a), n^{-1}log P(S_n>=na) -> -a theta_a + log phi(theta_a).

- Proof idea: Use Chernoff for the upper bound and exponential tilting plus the weak law for the lower bound.

- Exam use: Compute sharp exponential rates for normal, exponential, Bernoulli, and Poisson examples.

- Pitfall: Boundary cases require separate treatment when the optimizing theta is not inside the finite-mgf interval.

- Tags: cramer, rate-function, large-deviations

### Subsequence control upgraded to full control

- ID: `durrett_ch2_subsequence_upgrade`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: proof-template

- Summary: A sparse almost-sure estimate can be upgraded to all times when the gaps are controlled by monotonicity or a maximal inequality.

- Proof idea: Choose a subsequence with summable error probabilities, then compare every intermediate index to the next subsequence point.

- Exam use: Exercise 2.5.1 pattern: prove a rate on n_m=floor(m^alpha), then bridge the gaps.

- Pitfall: Subsequence convergence alone is insufficient; the gap-control step carries the proof.

- Tags: subsequence, maximal-inequality, almost-sure

### Two-series variance criterion

- ID: `durrett_ch2_two_series_theorem`

- Section: 2.5 Convergence of Random Series

- Kind: criterion

- Summary: Independent mean-zero variables with summable variances have an almost surely convergent series.

- Proof idea: Use Kolmogorov's maximal inequality to make the tails Cauchy almost surely.

- Exam use: Quickly solves centered series such as sum X_n sin(n pi t)/n.

- Pitfall: The variables must be independent and centered; otherwise deterministic drift must be treated separately.

- Tags: two-series, variance, random-series

### Independent series variance test

- ID: `durrett_ch2_independent_series_variance_test`

- Section: 2.5 Convergence of Random Series

- Kind: test

- Summary: For independent centered summands, finite total variance is enough for almost-sure convergence.

- Proof idea: Check that the series of variances is bounded by a known summable numerical series.

- Exam use: Exercise 2.5.3 pattern: trigonometric factors are harmless when bounded by 1.

- Pitfall: Do not require identical distributions; only independence, centering, and summable variances.

- Tags: random-series, variance-test, almost-sure

### Kronecker lemma for normalized sums

- ID: `durrett_ch2_kronecker_lemma`

- Section: 2.5 Convergence of Random Series

- Kind: lemma

- Summary: If sum x_n/n converges, then n^{-1} sum_{k<=n} x_k -> 0.

- Proof idea: Apply summation by parts to convert convergence of weighted terms into Cesaro decay of partial sums.

- Exam use: Turns convergence of a random series into a strong law for averages.

- Pitfall: The weights must increase to infinity; here the natural weight is n.

- Tags: kronecker, normalized-sums, series

### Tail-sum moment test

- ID: `durrett_ch2_tail_sum_moment_test`

- Section: 2.2 Weak Laws of Large Numbers

- Kind: criterion

- Summary: For p>0, E|X|^p is finite exactly when the tail probabilities P(|X|^p>n) are summable up to constants.

- Proof idea: Compare the integral of the tail distribution with the integer tail sum.

- Exam use: Exercise 2.5.2 pattern: a.s. term control plus Borel-Cantelli forces finite moments.

- Pitfall: The tail variable is |X|^p, not |X|; keep the normalization consistent.

- Tags: moments, tails, tail-sum

### Random power-series radius

- ID: `durrett_ch2_power_series_radius`

- Section: 2.5 Convergence of Random Series

- Kind: application

- Summary: The radius of sum X_n z^n is 1/limsup |X_n|^{1/n}; for iid coefficients this is decided by E log^+ |X_1|.

- Proof idea: Use the root test and Borel-Cantelli on events log^+|X_n| > epsilon n.

- Exam use: Exercise 2.5.8 pattern: logarithmic tails determine random analytic radius.

- Pitfall: Nonzero coefficients must occur infinitely often to rule out a larger radius.

- Tags: power-series, root-test, log-tail

### Levy maximal inequality for independent increments

- ID: `durrett_ch2_levy_maximal_inequality`

- Section: 2.5 Convergence of Random Series

- Kind: inequality

- Summary: A maximum of partial increments is controlled by the terminal increment times a lower bound on remaining-tail probabilities.

- Proof idea: Stop at the first crossing; if the later tail is small, the full terminal sum must still be large.

- Exam use: Core tool for Levy's theorem and convergence-in-probability to almost-sure convergence upgrades.

- Pitfall: The independence is between the first-crossing event and the future tail increment.

- Tags: levy-inequality, maximal-inequality, independent-increments

### Independent increments in partial sums

- ID: `durrett_ch2_independent_increments`

- Section: 2.5 Convergence of Random Series

- Kind: fact

- Summary: For sums of independent variables, disjoint blocks of increments are independent.

- Proof idea: Events determined by X_{m+1},...,X_j are independent of sums using X_{j+1},...,X_n.

- Exam use: Used inside first-crossing arguments and block decompositions.

- Pitfall: The original variables must be independent; identical distribution is not needed.

- Tags: independent-increments, blocks, partial-sums

### Cauchy criterion in probability

- ID: `durrett_ch2_cauchy_in_probability`

- Section: 2.5 Convergence of Random Series

- Kind: criterion

- Summary: Convergence in probability implies the sequence is Cauchy in probability, uniformly over sufficiently far tails.

- Proof idea: Apply the definition to pairs S_m,S_n after both indices are large.

- Exam use: Starting point for proving Levy's theorem.

- Pitfall: Cauchy in probability alone does not immediately give a.s. convergence without extra structure.

- Tags: convergence-in-probability, cauchy, levy-theorem

### Convergence in probability

- ID: `durrett_ch2_convergence_in_probability`

- Section: 2.2 Weak Laws of Large Numbers

- Kind: definition

- Summary: X_n -> X in probability means P(|X_n-X|>epsilon)->0 for every epsilon>0.

- Proof idea: Translate the target into tail probabilities and show each tends to zero.

- Exam use: Used throughout weak laws, maximal estimates, and large-deviation preliminaries.

- Pitfall: It is weaker than almost-sure convergence and does not by itself control all subsequences pathwise.

- Tags: convergence-in-probability, weak-convergence, tail-probability

### Chebyshev inequality for sums

- ID: `durrett_ch2_chebyshev`

- Section: 2.2 Weak Laws of Large Numbers

- Kind: inequality

- Summary: If a centered sum has finite variance, P(|S|>x) <= Var(S)/x^2.

- Proof idea: Compute or bound the variance, then divide by the square of the target scale.

- Exam use: Exercise 2.5.12 pattern: dyadic Chebyshev bounds become summable with a logarithmic correction.

- Pitfall: Chebyshev gives polynomial bounds; a log factor may be needed for summability.

- Tags: chebyshev, variance, weak-law

### Renewal function

- ID: `durrett_ch2_renewal_function`

- Section: 2.6 Renewal Theory

- Kind: definition

- Summary: The renewal function U(t)=E N_t records the expected number of renewals by time t.

- Proof idea: Relate U(t) to stopped sums of truncated interarrival times.

- Exam use: Exercise 2.6.1 pattern: bound U(t) using E(xi_1 wedge t).

- Pitfall: Indexing conventions for N_t vary; keep the same convention through the proof.

- Tags: renewal-function, expected-count, renewal

### Wald identity with truncated interarrivals

- ID: `durrett_ch2_wald_identity_truncated`

- Section: 2.6 Renewal Theory

- Kind: proof-template

- Summary: For bounded truncated increments xi_i wedge t and a renewal stopping time, the expected stopped sum factors as E increment times E count.

- Proof idea: Truncation makes the increments bounded, then optional-stopping or Wald's identity is safe.

- Exam use: Useful for elementary renewal estimates without assuming second moments.

- Pitfall: Do not apply untruncated Wald blindly when the stopping time or mean may be problematic.

- Tags: wald, truncation, renewal

### Renewal counting strong law

- ID: `durrett_ch2_renewal_slln`

- Section: 2.6 Renewal Theory

- Kind: theorem

- Summary: If interarrival times have finite mean mu, then N(t)/t -> 1/mu almost surely.

- Proof idea: Use T_n/n -> mu and invert the inequalities T_{N(t)} <= t < T_{N(t)+1}.

- Exam use: Converts cycle averages into long-run time rates.

- Pitfall: The inversion requires positive interarrival times and finite mean.

- Tags: renewal, slln, counting-process

### Uniform integrability from L2 bounds

- ID: `durrett_ch2_uniform_integrability`

- Section: 2.6 Renewal Theory

- Kind: criterion

- Summary: A family bounded in L2 is uniformly integrable, so a.s. convergence plus the L2 bound gives convergence of expectations.

- Proof idea: Use Cauchy-Schwarz to control large tails uniformly.

- Exam use: Exercise 2.6.2 pattern: upgrade N(t)/t -> 1/mu a.s. to U(t)/t -> 1/mu.

- Pitfall: Almost-sure convergence alone does not imply convergence of expectations.

- Tags: uniform-integrability, L2, expectations

### Poisson memoryless property

- ID: `durrett_ch2_poisson_memoryless`

- Section: 2.6 Renewal Theory

- Kind: fact

- Summary: After a stopping time independent of future arrivals, the waiting time to the next Poisson arrival is exponential and independent of the past.

- Proof idea: Use independent increments of the Poisson process and the exponential waiting-time law.

- Exam use: Turns accepted arrivals after service completion into a renewal process.

- Pitfall: This finite-time memoryless identity is special to exponential interarrivals.

- Tags: poisson-process, memoryless, renewal

### Renewal reward theorem

- ID: `durrett_ch2_renewal_reward_theorem`

- Section: 2.6 Renewal Theory

- Kind: theorem

- Summary: Long-run reward per unit time equals expected reward per cycle divided by expected cycle length.

- Proof idea: Apply the SLLN separately to rewards and cycle times, then squeeze the incomplete cycle.

- Exam use: Use for server acceptance fractions, machine uptime, and alternating renewal rewards.

- Pitfall: Check the cycle definition: rewards and lengths must correspond to the same cycles.

- Tags: renewal-reward, long-run-average, cycles

### Age and residual lifetime limits

- ID: `durrett_ch2_age_residual_life`

- Section: 2.6 Renewal Theory

- Kind: application

- Summary: The limiting tail for age, residual life, or their joint event is an integrated tail of the interarrival distribution divided by mu.

- Proof idea: Write a renewal equation for the event and apply the key renewal theorem to the forcing function.

- Exam use: Exercises 2.6.4 and 2.6.6 pattern: identify the renewal interval straddling t.

- Pitfall: The age and residual life are not generally independent in the limit.

- Tags: age, residual-life, key-renewal-theorem

### Alternating renewal process

- ID: `durrett_ch2_alternating_renewal_process`

- Section: 2.6 Renewal Theory

- Kind: model

- Summary: A system alternates between on- and off-periods; the long-run on probability is mean on-time divided by mean cycle length.

- Proof idea: Condition on the first on-period and restart after a complete on/off cycle.

- Exam use: Exercise 2.6.7 pattern: machine availability equals mu_on/(mu_on+mu_off).

- Pitfall: The cycle law is the convolution of one on-period and one off-period.

- Tags: alternating-renewal, availability, cycles

### Renewal density

- ID: `durrett_ch2_renewal_density`

- Section: 2.6 Renewal Theory

- Kind: formula

- Summary: If F has density f, the non-initial renewal measure has density v=sum_{n>=1} f^{*n}, satisfying v=f+v*F.

- Proof idea: Separate the first convolution term from the renewal density series.

- Exam use: Exercise 2.6.9 pattern: apply the key renewal theorem to f to get v(t)->1/mu.

- Pitfall: Direct Riemann integrability of f is the hypothesis that permits the limit theorem.

- Tags: renewal-density, convolution, key-renewal-theorem

### Large-deviation exponent gamma

- ID: `durrett_ch2_large_deviation_gamma`

- Section: 2.7 Large Deviations

- Kind: definition

- Summary: gamma(a) is the limiting exponential rate n^{-1} log P(S_n >= na), possibly 0 or -infinity.

- Proof idea: Use superadditivity of log probabilities to prove existence, then compute or bound the rate.

- Exam use: Exercises 2.7.1 and 2.7.2 pattern: analyze the effective domain and concavity of gamma.

- Pitfall: A rate of -infinity corresponds to an impossible event, not merely a very small probability.

- Tags: large-deviations, gamma, rate

### Independent sums factor rare-event probabilities

- ID: `durrett_ch2_independent_sums`

- Section: 2.7 Large Deviations

- Kind: fact

- Summary: For iid sums, events involving disjoint blocks can be multiplied to get lower bounds on large-deviation probabilities.

- Proof idea: Split S_{m+n}=S_m+(S_{m+n}-S_m) and use independence.

- Exam use: Useful for superadditivity and concavity of large-deviation rates.

- Pitfall: The block thresholds must add to the desired total threshold.

- Tags: independence, sums, large-deviations

### Superadditivity lemma

- ID: `durrett_ch2_superadditivity`

- Section: 2.7 Large Deviations

- Kind: lemma

- Summary: If a_{m+n} >= a_m+a_n, then a_n/n has a limit equal to its supremum in the extended real sense.

- Proof idea: Tile a long integer by blocks and control the leftover.

- Exam use: Used to prove existence of gamma(a).

- Pitfall: Signs matter: log probabilities are superadditive here, not subadditive.

- Tags: superadditivity, fekete, large-deviations

### Concavity from block mixing

- ID: `durrett_ch2_concavity`

- Section: 2.7 Large Deviations

- Kind: proof-template

- Summary: Mixing blocks with thresholds a and b proves gamma(lambda a+(1-lambda)b) >= lambda gamma(a)+(1-lambda)gamma(b).

- Proof idea: Use rational lambda first with integer block lengths, then extend by monotonicity.

- Exam use: Exercise 2.7.2 pattern: concavity implies local Lipschitz regularity on the finite domain.

- Pitfall: The extension from rational to real lambda needs monotonicity or another continuity argument.

- Tags: concavity, block-mixing, large-deviations

### Poisson large-deviation rate

- ID: `durrett_ch2_poisson_large_deviation`

- Section: 2.7 Large Deviations

- Kind: example

- Summary: For iid Poisson(1), P(S_n>=na) has exponent -a log a+a-1 for a>1.

- Proof idea: Use the Poisson mgf exp(e^theta-1) and optimize at theta=log a.

- Exam use: Exercise 2.7.3 pattern: compute Cramer rates by solving tilted mean equals a.

- Pitfall: The displayed formula is for upper tails a>1.

- Tags: poisson, cramer, rate-function

### Moment-generating-function upper bounds

- ID: `durrett_ch2_mgf_bounds`

- Section: 2.7 Large Deviations

- Kind: technique

- Summary: Simple analytic inequalities for phi(theta) lead to usable Chernoff bounds even when the exact optimizer is not used.

- Proof idea: Bound log phi(theta), then optimize the quadratic or other simpler expression.

- Exam use: Exercise 2.7.4 pattern: cosh(theta)-1 <= beta theta^2 for theta<=1.

- Pitfall: The bound is only valid over the range where the analytic inequality was proved.

- Tags: mgf, chernoff, tail-bound

### Subgaussian bound for fair coin sums

- ID: `durrett_ch2_subgaussian_coin_flips`

- Section: 2.7 Large Deviations

- Kind: example

- Summary: For Rademacher sums, bounding cosh(theta) by exp(beta theta^2) gives a Gaussian-type upper tail.

- Proof idea: Apply Chernoff and choose theta=a/(2 beta).

- Exam use: Gives a clean exponential estimate P(S_n>=an) <= exp(-n a^2/(4 beta)) for 0<=a<=1.

- Pitfall: This is a valid bound but not the sharp Cramer exponent.

- Tags: rademacher, subgaussian, chernoff

### No positive mgf gives zero exponential rate

- ID: `durrett_ch2_heavy_tail_large_deviation`

- Section: 2.7 Large Deviations

- Kind: principle

- Summary: If all positive exponential moments are infinite, upper large deviations cannot have a strictly negative exponential rate.

- Proof idea: A negative rate would force exponentially bounded positive tails, creating a finite positive mgf.

- Exam use: Exercise 2.7.5 pattern: heavy tails make large deviations subexponential on the logarithmic n-scale.

- Pitfall: This conclusion concerns exponential rate only; probabilities may still tend to zero.

- Tags: heavy-tail, large-deviations, mgf

### One big jump lower bound

- ID: `durrett_ch2_one_big_jump`

- Section: 2.7 Large Deviations

- Kind: proof-template

- Summary: For integrable mean-zero iid sums, P(S_n>=na) is at least asymptotically n P(X_1>=n(a+epsilon)).

- Proof idea: Require exactly one unusually large summand and use the weak law to keep the remaining sum above -n epsilon.

- Exam use: Exercise 2.7.6 pattern: lower-bound heavy-tail large deviations by a single summand.

- Pitfall: Integrability is used to ensure n P(X_1>cn)->0 and to apply the weak law.

- Tags: one-big-jump, heavy-tail, weak-law

### Weak law of large numbers

- ID: `durrett_ch2_weak_law`

- Section: 2.2 Weak Laws of Large Numbers

- Kind: theorem

- Summary: For iid integrable variables with mean mu, S_n/n -> mu in probability.

- Proof idea: Use truncation plus Chebyshev, or invoke the finite-mean weak law.

- Exam use: Supports probability estimates for the contribution of all non-extreme summands.

- Pitfall: Weak convergence controls high-probability behavior, not pathwise eventual behavior.

- Tags: weak-law, iid, finite-mean

### Tail probability normalization

- ID: `durrett_ch2_tail_probability`

- Section: 2.7 Large Deviations

- Kind: technique

- Summary: Compare rare-event probabilities to n times a single-tail probability when one large summand drives the event.

- Proof idea: Use independence, exclusion of multiple large jumps, and a law of large numbers for the remaining terms.

- Exam use: Useful in heavy-tail large-deviation lower bounds.

- Pitfall: The denominator must match the same threshold scale as the constructed big jump.

- Tags: tail-probability, normalization, heavy-tail

### Borel-Cantelli lemmas

- ID: `durrett_ch2_borel_cantelli`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: theorem

- Summary: Summable event probabilities imply only finitely many occurrences; for independent events, divergent probability sums imply infinitely many occurrences.

- Proof idea: The first lemma uses a union bound on the tail union; the second uses independence to control the probability of no future occurrence.

- Exam use: A general retrieval alias for exercises that use either Borel-Cantelli direction.

- Pitfall: The divergent direction requires independence or a suitable substitute.

- Tags: borel-cantelli, almost-sure, limsup

### Cramer theorem

- ID: `durrett_ch2_cramer_theorem`

- Section: 2.7 Large Deviations

- Kind: theorem

- Summary: For light-tailed iid sums, the upper-tail exponential decay rate is the negative Legendre transform of log E exp(theta X).

- Proof idea: Use Chernoff for the upper bound and exponential tilting for the matching lower bound.

- Exam use: A general retrieval alias for Cramer-rate computations such as the Poisson example.

- Pitfall: The theorem requires finiteness of the mgf near the optimizing tilt.

- Tags: cramer, large-deviations, rate-function

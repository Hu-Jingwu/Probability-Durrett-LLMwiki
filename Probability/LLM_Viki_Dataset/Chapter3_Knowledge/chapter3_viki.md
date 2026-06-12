# Durrett Chapter 3 LLM Viki: Central Limit Theorems

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter3.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

## Section Guides

### 3.1 The De Moivre-Laplace Theorem

- Goal: Understand the normal limit first through exact binomial probabilities and Stirling asymptotics.

- Must master: Stirling formula, local binomial approximation, Riemann-sum normal limit, linear-deviation contrast

- Prelim angle: A concrete way to derive normal approximation and avoid using the CLT as a black box.

### 3.2 Weak Convergence

- Goal: Use distributional convergence through continuity points, test functions, mapping theorems, and tightness.

- Must master: weak convergence definition, Portmanteau theorem, continuous mapping, tightness, Helly selection, Slutsky patterns

- Prelim angle: Most limit-theorem problems need these tools to move from transforms to events or transformed variables.

### 3.3 Characteristic Functions

- Goal: Use Fourier transforms to identify laws, prove weak convergence, and extract moment expansions.

- Must master: characteristic functions, inversion, Levy continuity theorem, moment derivatives, standard transform table

- Prelim angle: High-yield method for CLT, Poisson convergence, random sums, and independence checks.

### 3.4 Central Limit Theorems

- Goal: Prove normal limits for iid sequences and triangular arrays, and recognize rate and arithmetic examples.

- Must master: iid CLT, Lindeberg-Feller, Lyapunov condition, random index CLT, Berry-Esseen

- Prelim angle: The central computation theme of Chapter 3; many exam problems are variants with changed normalization or dependence.

### 3.5 Local Limit Theorems

- Goal: Upgrade cumulative CLT statements to point-probability approximations using Fourier inversion.

- Must master: lattice span, local normal approximation, small-t/large-t split

- Prelim angle: Useful when the problem asks for exact mass asymptotics instead of only distributional convergence.

### 3.6 Poisson Convergence

- Goal: Recognize and prove laws of small numbers for rare-event counts, with and without dependence.

- Must master: Bernoulli array theorem, total variation approximation, matching, occupancy

- Prelim angle: Common source of limit-distribution questions where the limit is Poisson rather than normal.

### 3.7 Poisson Processes

- Goal: Move from rare-event counts to continuous-time counting processes, thinning, compounding, and conditioning.

- Must master: independent increments, compound Poisson, thinning, conditional order statistics

- Prelim angle: Connects Chapter 3 convergence tools with stochastic-process modeling.

### 3.8 Stable Laws

- Goal: Understand nonnormal limits for heavy-tailed sums and the role of scaling, skewness, and centering.

- Must master: stable characteristic functions, domain of attraction, regular variation, convergence of types

- Prelim angle: A warning system for infinite-variance problems where sqrt(n) normalization is wrong.

### 3.9 Infinitely Divisible Distributions

- Goal: See normal, Poisson, compound Poisson, and stable laws as members of one triangular-array limit family.

- Must master: infinite divisibility, Levy-Khinchin formula, Levy measure, Gaussian and jump components

- Prelim angle: Less often computational, but excellent for recognizing possible limits of infinitesimal arrays.

### 3.10 Limit Theorems in R^d

- Goal: Extend weak convergence, characteristic functions, and CLT arguments to random vectors.

- Must master: multivariate weak convergence, multivariate characteristic functions, Cramer-Wold, multivariate CLT

- Prelim angle: Joint convergence questions usually reduce to projections and covariance calculations.

## Knowledge Pieces

### Stirling local binomial approximation

- ID: `durrett_ch3_stirling_local_binomial`

- Section: 3.1 The De Moivre-Laplace Theorem

- Kind: formula

- Summary: For a simple symmetric walk, P(S_{2n}=2k) is asymptotic to (pi n)^(-1/2) exp(-x^2/2) when 2k/sqrt(2n) tends to x.

- Proof idea: Insert Stirling's formula into the central binomial coefficient and use (1+c_n)^{a_n} limits.

- Exam use: Use as the prototype local normal approximation before invoking characteristic functions.

- Pitfall: The approximation is local and depends on the lattice parity of S_{2n}.

- Tags: stirling, binomial, local-normal

### De Moivre-Laplace theorem

- ID: `durrett_ch3_demoivre_laplace`

- Section: 3.1 The De Moivre-Laplace Theorem

- Kind: theorem

- Summary: For a simple symmetric random walk, S_m/sqrt(m) converges in distribution to the standard normal law.

- Proof idea: Sum the local binomial approximation over lattice points and identify the resulting Riemann sum with the normal integral.

- Exam use: A concrete CLT model for coin flips, binomial normal approximation, and continuity-correction intuition.

- Pitfall: Do not forget the even/odd lattice issue; the theorem for all m follows after a small parity argument.

- Tags: clt, simple-random-walk, normal-approximation

### Product exponential limit

- ID: `durrett_ch3_product_exponential_limit`

- Section: 3.1 The De Moivre-Laplace Theorem

- Kind: lemma

- Summary: If max_j |c_{j,n}| goes to 0, sum_j c_{j,n} tends to lambda, and the sums of absolute values are bounded, then product_j(1+c_{j,n}) tends to exp(lambda).

- Proof idea: Take logarithms, use log(1+x)=x+o(x) uniformly for small x, and control the total error by the absolute-sum bound.

- Exam use: Fast route for birthday, occupancy, and rare-event product limits.

- Pitfall: The maximum term condition is essential; a single large factor can break the exponential approximation.

- Tags: product-limit, rare-events, asymptotics

### Stirling large-deviation patterns

- ID: `durrett_ch3_large_deviation_stirling_patterns`

- Section: 3.1 The De Moivre-Laplace Theorem

- Kind: example-pattern

- Summary: Stirling's formula also gives exponential rates for binomial and Poisson tails at linear deviations from the mean.

- Proof idea: Approximate the largest relevant mass and show nearby tail terms are geometrically controlled.

- Exam use: Useful when an exam asks for n^{-1} log P(S_n >= n a) before the full large-deviation theorem is available.

- Pitfall: Normal approximation is not valid on linear-deviation scales; use exponential rates instead.

- Tags: large-deviations, stirling, tail-asymptotics

### Weak convergence definition

- ID: `durrett_ch3_weak_convergence_definition`

- Section: 3.2 Weak Convergence

- Kind: definition

- Summary: Distribution functions F_n converge weakly to F when F_n(x) tends to F(x) at every continuity point of F; random variables converge in distribution when their laws do.

- Proof idea: Continuity points are enough because distribution functions are right continuous and have at most countably many jumps.

- Exam use: This is the language used in CLT, Poisson approximation, stable limits, and multivariate limits.

- Pitfall: Convergence at discontinuity points of the limit is not required and can fail even for X+1/n tending to X.

- Tags: weak-convergence, distribution-functions, continuity-points

### Waiting for rare events gives an exponential limit

- ID: `durrett_ch3_rare_geometric_exponential_limit`

- Section: 3.2.1 Examples

- Kind: example-pattern

- Summary: If X_p is geometric with success probability p, then p X_p converges in distribution to an exponential(1) random variable as p tends to 0.

- Proof idea: Use P(p X_p > x)=(1-p)^{floor(x/p)} and the exponential limit lemma.

- Exam use: Recognize geometric waiting times under rare-event scaling.

- Pitfall: The scale is p X_p, not X_p/p; the waiting time itself diverges.

- Tags: geometric, exponential-limit, rare-events

### Birthday collision Rayleigh limit

- ID: `durrett_ch3_birthday_rayleigh_limit`

- Section: 3.2.1 Examples

- Kind: example-pattern

- Summary: For iid uniform draws from N boxes, the first collision time T_N satisfies P(T_N/sqrt(N)>x) tending to exp(-x^2/2).

- Proof idea: Write the no-collision probability as a product of terms 1-(m-1)/N and apply the product exponential limit.

- Exam use: A standard occupancy/collision scaling pattern.

- Pitfall: The natural scale is sqrt(N), not N, because collisions depend on pairs.

- Tags: birthday-problem, occupancy, rayleigh-tail

### Scheffe theorem for densities

- ID: `durrett_ch3_scheffe_theorem`

- Section: 3.2.1 Examples

- Kind: theorem

- Summary: If probability densities f_n converge pointwise to a density f, then the corresponding probability measures converge in total variation, hence weakly.

- Proof idea: Use the identity integral |f_n-f| = 2 integral (f-f_n)^+ and dominated convergence.

- Exam use: Use when a limit distribution is easiest to prove through densities, such as central order statistics.

- Pitfall: Pointwise convergence of densities is stronger than weak convergence and is not necessary.

- Tags: scheffe, densities, total-variation

### Quantile representation for weak convergence

- ID: `durrett_ch3_skorokhod_quantile_representation`

- Section: 3.2.2 Theory

- Kind: theorem

- Summary: If F_n converges weakly to F, one can construct random variables with these laws on (0,1) that converge almost surely.

- Proof idea: Use generalized inverse distribution functions and exclude the countable set of flat-level ambiguities.

- Exam use: Lets proof problems transfer weak convergence into almost sure convergence for bounded continuous mappings.

- Pitfall: The constructed variables need not be the original variables; this is a representation argument.

- Tags: quantile-transform, skorokhod, weak-convergence

### Bounded continuous test function characterization

- ID: `durrett_ch3_bounded_continuous_test_functions`

- Section: 3.2.2 Theory

- Kind: theorem

- Summary: X_n converges in distribution to X iff E g(X_n) tends to E g(X) for every bounded continuous function g.

- Proof idea: One direction uses the almost-sure representation and bounded convergence; the converse approximates indicators of half-lines by continuous cutoffs.

- Exam use: The default way to define weak convergence on general topological spaces.

- Pitfall: Boundedness matters; unbounded continuous functions need extra tightness or uniform integrability.

- Tags: portmanteau, test-functions, bounded-continuous

### Continuous mapping theorem

- ID: `durrett_ch3_continuous_mapping_theorem`

- Section: 3.2.2 Theory

- Kind: theorem

- Summary: If X_n converges in distribution to X and g is measurable with P(X in D_g)=0, then g(X_n) converges in distribution to g(X).

- Proof idea: Represent X_n and X almost surely, then apply pointwise continuity of g off its discontinuity set.

- Exam use: Use for Slutsky-type transformations, maxima maps, ratios away from zero, and normalization changes.

- Pitfall: A discontinuity with positive limit probability can invalidate the conclusion.

- Tags: continuous-mapping, weak-convergence, discontinuity-set

### Portmanteau open-closed criteria

- ID: `durrett_ch3_portmanteau_open_closed`

- Section: 3.2.2 Theory

- Kind: theorem

- Summary: Weak convergence is equivalent to lower bounds on open sets, upper bounds on closed sets, and convergence on Borel sets whose boundary has limit probability zero.

- Proof idea: Use Fatou on indicators after almost-sure representation, then pass between open and closed sets by complements.

- Exam use: Use when events are not intervals but have negligible boundary under the limit.

- Pitfall: The direction of the inequalities is easy to reverse; open sets get liminf lower bounds and closed sets get limsup upper bounds.

- Tags: portmanteau, open-sets, closed-sets

### Helly selection and tightness

- ID: `durrett_ch3_helly_selection_tightness`

- Section: 3.2.2 Theory

- Kind: theorem

- Summary: Every sequence of distribution functions has a vaguely convergent subsequence; subsequential limits are probability laws exactly when mass is tight.

- Proof idea: Use a diagonal subsequence over rational points and then repair right continuity; tightness prevents mass escaping to plus or minus infinity.

- Exam use: Core compactness tool for proving existence of subsequential distributional limits.

- Pitfall: Vague subsequential limits can lose mass, so Helly alone is not enough for weak convergence.

- Tags: helly, tightness, subsequences

### Moment tightness criterion

- ID: `durrett_ch3_moment_tightness_criterion`

- Section: 3.2.2 Theory

- Kind: criterion

- Summary: If sup_n E phi(X_n) is finite for some nonnegative phi with phi(x) tending to infinity as |x| tends to infinity, then the laws of X_n are tight.

- Proof idea: Apply Markov's inequality to phi(X_n) outside large compact intervals.

- Exam use: Fast tightness check using bounded moments or coercive Lyapunov functions.

- Pitfall: A bounded first or second moment gives tightness, but tightness does not require moments.

- Tags: tightness, markov, moment-bound

### Subsequence principle for weak convergence

- ID: `durrett_ch3_subsequence_principle_weak`

- Section: 3.2.2 Theory

- Kind: proof-template

- Summary: If every subsequence has a further subsequence converging weakly to the same law, then the full sequence converges weakly to that law.

- Proof idea: Use the topological subsequence criterion on real numbers F_n(x) at continuity points.

- Exam use: Useful for proving convergence after compactness/tightness arguments.

- Pitfall: The further subsequential limit must be uniquely identified; tightness only gives candidates.

- Tags: subsequence, weak-convergence, uniqueness

### Convergence in probability implies weak convergence

- ID: `durrett_ch3_convergence_in_probability_to_distribution`

- Section: 3.2 Exercises and Consequences

- Kind: fact

- Summary: If X_n tends to X in probability, then X_n converges in distribution to X; if X_n converges in distribution to a constant c, then X_n tends to c in probability.

- Proof idea: Use inclusions between half-line events with epsilon buffers and continuity points, or use bounded continuous test functions.

- Exam use: Often used to replace negligible error terms in limit theorems.

- Pitfall: Weak convergence to a nonconstant random variable does not imply convergence in probability on the original space.

- Tags: convergence-in-probability, weak-convergence, constant-limit

### Converging together and Slutsky patterns

- ID: `durrett_ch3_converging_together_slutsky`

- Section: 3.2 Exercises and Consequences

- Kind: proof-template

- Summary: If X_n converges in distribution to X and Y_n converges in distribution to a constant c, then X_n+Y_n, X_n Y_n, and X_n/Y_n (c not 0) converge to the corresponding transformed limits.

- Proof idea: Upgrade Y_n to convergence in probability, combine with X_n using tightness and continuous mapping.

- Exam use: Indispensable for replacing random normalizers by deterministic limits.

- Pitfall: The denominator case needs the limit constant away from zero.

- Tags: slutsky, converging-together, random-normalization

### Characteristic function basics

- ID: `durrett_ch3_characteristic_function_definition`

- Section: 3.3.1 Definition, Inversion Formula

- Kind: definition

- Summary: The characteristic function of X is phi(t)=E exp(i t X); it is uniformly continuous, positive definite, satisfies phi(0)=1, and determines the distribution.

- Proof idea: Most properties follow from bounded convergence and algebra of complex exponentials.

- Exam use: Main transform language for CLT and distributional convergence.

- Pitfall: A pointwise limit of characteristic functions is a characteristic function only if it is continuous at zero.

- Tags: characteristic-functions, positive-definite, transforms

### Characteristic functions multiply for independent sums

- ID: `durrett_ch3_cf_independent_sums`

- Section: 3.3.1 Definition, Inversion Formula

- Kind: theorem

- Summary: If X and Y are independent, the characteristic function of X+Y is phi_X(t) phi_Y(t).

- Proof idea: Factor E exp(i t X) exp(i t Y) by independence.

- Exam use: Turns sums of independent random variables into products and powers of transforms.

- Pitfall: The product rule requires independence; uncorrelated variables are not enough.

- Tags: independent-sums, characteristic-functions, convolution

### Standard characteristic function table

- ID: `durrett_ch3_standard_characteristic_functions`

- Section: 3.3.1 Definition, Inversion Formula

- Kind: example-bank

- Summary: Coin flip: cos t; Poisson(lambda): exp(lambda(e^{it}-1)); normal(mu,sigma^2): exp(i mu t - sigma^2 t^2/2); uniform(a,b): (e^{itb}-e^{ita})/(it(b-a)); exponential(lambda): lambda/(lambda-it).

- Proof idea: Compute directly from sums or integrals, using independence and completing the square for normals.

- Exam use: Recognition table for prelim transform calculations.

- Pitfall: Check parameter conventions carefully, especially normal variance and exponential rate versus mean.

- Tags: cf-table, normal, poisson, exponential

### Characteristic function inversion formula

- ID: `durrett_ch3_cf_inversion_formula`

- Section: 3.3.1 Definition, Inversion Formula

- Kind: theorem

- Summary: A distribution can be recovered from its characteristic function by integrating (exp(-ita)-exp(-itb))/(it) against phi(t) over symmetric intervals and taking limits at continuity endpoints.

- Proof idea: Apply Fubini to the Fourier integral of interval indicators and let the cutoff grow.

- Exam use: Use to prove uniqueness and to identify distributional limits from transforms.

- Pitfall: Endpoint atoms require care; inversion is cleanest for intervals whose endpoints have zero mass.

- Tags: inversion, fourier, uniqueness

### Integrable characteristic function gives bounded density

- ID: `durrett_ch3_integrable_cf_density`

- Section: 3.3.1 Definition, Inversion Formula

- Kind: theorem

- Summary: If a characteristic function is integrable, the distribution has a bounded continuous density given by Fourier inversion.

- Proof idea: Use dominated convergence to invert the transform and verify that interval probabilities are integrals of the resulting function.

- Exam use: Shows stable or limiting laws have densities when their characteristic functions are integrable.

- Pitfall: Integrability of phi is sufficient, not necessary, for having a density.

- Tags: density, fourier-inversion, integrable-cf

### Levy continuity theorem

- ID: `durrett_ch3_levy_continuity_theorem`

- Section: 3.3.2 Weak Convergence

- Kind: theorem

- Summary: Probability measures converge weakly iff their characteristic functions converge pointwise to a function continuous at zero, in which case the limit is the characteristic function of the weak limit.

- Proof idea: Use tightness plus inversion to identify subsequential limits; continuity at zero prevents mass loss.

- Exam use: The main engine for proving CLT, Poisson limits, stable limits, and multivariate limit theorems.

- Pitfall: Pointwise convergence to a discontinuous-at-zero function does not define a probability limit.

- Tags: levy-continuity, weak-convergence, characteristic-functions

### Moments from characteristic function derivatives

- ID: `durrett_ch3_derivatives_moments`

- Section: 3.3.3 Moments and Derivatives

- Kind: theorem

- Summary: If E|X|^n is finite, then phi has n derivatives and phi^{(k)}(0)=i^k E X^k for k up to n.

- Proof idea: Differentiate under the expectation using domination by |X|^k.

- Exam use: Compute moments and build Taylor expansions for CLT proofs.

- Pitfall: Existence of a few derivatives at zero can be subtler than finite moments unless the theorem's hypotheses are met.

- Tags: moments, derivatives, taylor-expansion

### Second-order characteristic function expansion

- ID: `durrett_ch3_second_order_cf_expansion`

- Section: 3.3.3 Moments and Derivatives

- Kind: formula

- Summary: If EX=0 and EX^2=sigma^2 is finite, then phi(t)=1-sigma^2 t^2/2+o(t^2) as t tends to zero.

- Proof idea: Use the Taylor expansion of exp(itX) and dominate the remainder through finite second moment.

- Exam use: This is the one-line input behind the iid CLT by characteristic functions.

- Pitfall: The expansion is local near zero; do not apply it at fixed nonzero t without scaling.

- Tags: second-moment, cf-expansion, clt

### Polya criterion for characteristic functions

- ID: `durrett_ch3_polya_criterion`

- Section: 3.3.4 Polya's Criterion

- Kind: criterion

- Summary: A real, nonnegative, even, convex-on-positive-rays function with phi(0)=1 and phi(t) tending to 0 at infinity is a characteristic function.

- Proof idea: Approximate phi by polygonal functions that are mixtures of triangular characteristic functions and pass to a weak limit.

- Exam use: Useful for constructing stable-law examples such as exp(-|t|^alpha) for 0<alpha<2.

- Pitfall: The criterion is sufficient, not necessary; many characteristic functions are not nonnegative or convex.

- Tags: polya, construction, stable-laws

### Moment problem and Carleman-type uniqueness

- ID: `durrett_ch3_moment_problem_carleman`

- Section: 3.3.5 The Moment Problem

- Kind: theorem

- Summary: Under suitable growth conditions on even moments, a distribution is determined by its moments.

- Proof idea: Use analytic control of the characteristic function or moment generating series near zero.

- Exam use: Helps decide when matching all moments identifies a law.

- Pitfall: Moment equality alone is not always enough; lognormal-type examples show nonuniqueness can occur.

- Tags: moment-problem, carleman, uniqueness

### IID central limit theorem

- ID: `durrett_ch3_iid_clt`

- Section: 3.4.1 i.i.d. Sequences

- Kind: theorem

- Summary: If X_i are iid with mean mu and variance sigma^2 in (0,infinity), then (S_n-n mu)/(sigma sqrt(n)) converges in distribution to standard normal.

- Proof idea: Center and scale, raise the characteristic function at t/sqrt(n) to the nth power, and use the second-order expansion.

- Exam use: The central theorem for normal approximations and asymptotic distribution calculations.

- Pitfall: Finite nonzero variance is required for this form; infinite variance can lead to nonnormal stable limits.

- Tags: clt, iid, normal-limit

### Normal approximation and continuity correction

- ID: `durrett_ch3_normal_approximation_continuity_correction`

- Section: 3.4.1 i.i.d. Sequences

- Kind: example-pattern

- Summary: For binomial or lattice sums, approximate probabilities by normal intervals and shift interval endpoints by half a lattice step for better accuracy.

- Proof idea: Apply the CLT to centered and scaled sums while accounting for the discrete histogram cell width.

- Exam use: Useful for coin-flip, dice, roulette, binomial, and Poisson approximations.

- Pitfall: The CLT gives large-n accuracy; small tails and lattice endpoints may need correction or sharper bounds.

- Tags: normal-approximation, binomial, continuity-correction

### Lindeberg-Feller central limit theorem

- ID: `durrett_ch3_triangular_array_lindeberg_feller`

- Section: 3.4.2 Triangular Arrays

- Kind: theorem

- Summary: For independent mean-zero triangular arrays with total variance tending to 1, the row sum converges to standard normal iff the Lindeberg condition holds.

- Proof idea: Use characteristic functions, compare products with exponentials, and show large terms are negligible exactly under Lindeberg.

- Exam use: The main CLT for non-identically distributed arrays.

- Pitfall: The condition is row-wise; do not replace it by iid assumptions unless the array is built that way.

- Tags: lindeberg-feller, triangular-array, clt

### Lyapunov condition implies Lindeberg

- ID: `durrett_ch3_lyapunov_condition`

- Section: 3.4.2 Triangular Arrays

- Kind: criterion

- Summary: If a triangular array has normalized (2+delta)-moments whose row sum tends to zero, then the Lindeberg condition holds.

- Proof idea: Bound x^2 1{|x|>epsilon} by epsilon^{-delta}|x|^{2+delta}.

- Exam use: Quick sufficient check for triangular-array CLTs.

- Pitfall: Lyapunov is stronger than Lindeberg; failure of Lyapunov does not rule out a CLT.

- Tags: lyapunov, lindeberg, moment-condition

### Random index CLT

- ID: `durrett_ch3_random_index_clt`

- Section: 3.4.1 i.i.d. Sequences

- Kind: exercise-pattern

- Summary: If N_t/a(t) tends to 1 in probability and iid centered finite-variance sums satisfy the CLT, then S_{N_t}/sqrt(a(t)) has the same normal limit.

- Proof idea: Use maximal inequalities to show the difference between S_{N_t} and S_{a(t)} is negligible on high-probability index windows.

- Exam use: Useful for renewal CLTs and random-sample-size problems.

- Pitfall: The random index must be close on the scale needed by the partial-sum fluctuations.

- Tags: random-index, clt, renewal

### Erdos-Kac central limit theorem

- ID: `durrett_ch3_erdos_kac`

- Section: 3.4.3 Prime Divisors

- Kind: theorem

- Summary: The number of distinct prime divisors of a uniformly chosen integer up to n, after centering and scaling by log log n, converges to the standard normal law.

- Proof idea: Approximate divisibility by small primes with nearly independent Bernoulli variables and control the remaining error.

- Exam use: A landmark example where arithmetic statistics obey a CLT.

- Pitfall: The variance scale is log log n, not log n.

- Tags: erdos-kac, number-theory, bernoulli-approximation

### Berry-Esseen rate

- ID: `durrett_ch3_berry_esseen`

- Section: 3.4.4 Rates of Convergence

- Kind: theorem

- Summary: For iid centered variables with finite third absolute moment and variance one, the normal approximation error in Kolmogorov distance is O(E|X|^3/sqrt(n)).

- Proof idea: Compare characteristic functions through smoothing inequalities and bound the third-order Taylor remainder.

- Exam use: Use when a problem asks for an explicit CLT error rate.

- Pitfall: Finite variance alone gives convergence but not this rate.

- Tags: berry-esseen, rates, kolmogorov-distance

### Lattice span from characteristic functions

- ID: `durrett_ch3_lattice_span`

- Section: 3.5 Local Limit Theorems

- Kind: criterion

- Summary: For a lattice distribution, the set of t with |phi(t)|=1 encodes the lattice spacing; otherwise |phi(t)|<1 away from zero on compact intervals.

- Proof idea: Equality in the triangle inequality forces exp(itX) to be almost surely constant.

- Exam use: Key diagnostic for local limit theorems.

- Pitfall: Local limits differ in lattice and nonlattice cases; the span matters.

- Tags: lattice, characteristic-functions, local-limit

### Local limit theorem

- ID: `durrett_ch3_local_limit_theorem`

- Section: 3.5 Local Limit Theorems

- Kind: theorem

- Summary: Under suitable lattice hypotheses and finite variance, point probabilities of centered sums are approximated by the normal density times the lattice spacing over sqrt(n).

- Proof idea: Use Fourier inversion and split the integral into a small-t CLT region and a large-t region controlled by |phi(t)|<1.

- Exam use: Use when approximating exact probabilities, not just cumulative probabilities.

- Pitfall: The ordinary CLT does not imply local probability estimates by itself.

- Tags: local-limit, lattice, normal-density

### Poisson convergence for rare Bernoulli arrays

- ID: `durrett_ch3_poisson_triangular_array`

- Section: 3.6.1 The Basic Limit Theorem

- Kind: theorem

- Summary: For independent Bernoulli variables in row n, if the maximum success probability tends to zero and the sum of success probabilities tends to lambda, then the row sum converges to Poisson(lambda).

- Proof idea: Multiply Bernoulli characteristic functions and use log(1+z)=z+o(z) uniformly because all probabilities are small.

- Exam use: The standard law of small numbers for rare-event counts.

- Pitfall: The largest individual probability must vanish; total mean convergence alone is not enough.

- Tags: poisson-convergence, law-of-small-numbers, bernoulli-array

### Total variation Poisson approximation

- ID: `durrett_ch3_total_variation_poisson_approximation`

- Section: 3.6.1 The Basic Limit Theorem

- Kind: theorem

- Summary: A sum of independent Bernoulli variables is close in total variation to a Poisson variable with matching mean when the sum of squared success probabilities is small.

- Proof idea: Compare each Bernoulli law with its Poisson approximation, then use product and convolution contraction inequalities.

- Exam use: Gives quantitative Poisson approximation for rare counts.

- Pitfall: Total variation is stronger than weak convergence; the error bound depends on small individual probabilities.

- Tags: total-variation, poisson-approximation, rare-events

### Matching fixed points converge to Poisson

- ID: `durrett_ch3_matching_fixed_points`

- Section: 3.6.2 Two Examples with Dependence

- Kind: example-pattern

- Summary: The number of fixed points in a uniform random permutation converges to Poisson(1).

- Proof idea: Compute factorial moments or use inclusion-exclusion; dependence is weak enough that rare fixed-point events mimic independent Bernoulli events.

- Exam use: Classic dependent rare-event Poisson limit.

- Pitfall: The indicators are not independent, so the basic Bernoulli-array theorem does not apply directly.

- Tags: matching, fixed-points, poisson-limit

### Occupancy empty-box Poisson limit

- ID: `durrett_ch3_occupancy_empty_boxes`

- Section: 3.6.2 Two Examples with Dependence

- Kind: example-pattern

- Summary: When r balls are thrown into n boxes and n exp(-r/n) tends to lambda, the number of empty boxes converges to Poisson(lambda).

- Proof idea: Use inclusion-exclusion or Poissonization to handle dependence among empty-box indicators.

- Exam use: Appears in coupon collector and hashing problems.

- Pitfall: Empty-box events are dependent; independence heuristics need justification.

- Tags: occupancy, empty-boxes, poisson-limit

### Poisson process from independent increments

- ID: `durrett_ch3_poisson_process_increments`

- Section: 3.7 Poisson Processes

- Kind: theorem

- Summary: A counting process with stationary independent increments, no multiple jumps in small intervals, and jump probability asymptotic to lambda h has N(0,t) distributed as Poisson(lambda t).

- Proof idea: Partition [0,t] into many small intervals and apply Poisson convergence to the rare jump indicators.

- Exam use: Foundation for continuous-time rare-event models.

- Pitfall: The small-interval multiple-jump condition is needed to reduce counts to Bernoulli indicators.

- Tags: poisson-process, independent-increments, counting-process

### Compound Poisson process

- ID: `durrett_ch3_compound_poisson`

- Section: 3.7.1 Compound Poisson Processes

- Kind: construction

- Summary: If N is a Poisson process and Y_i are iid jumps independent of N, then sum_{i<=N(t)} Y_i is a compound Poisson process with characteristic function exp(lambda t (E exp(i theta Y)-1)).

- Proof idea: Condition on N(t) and use the iid product rule for characteristic functions.

- Exam use: Models random sums and jump processes with nonunit jump sizes.

- Pitfall: Do not confuse the rate of arrivals with the distribution of jump sizes.

- Tags: compound-poisson, random-sum, jump-process

### Thinning of a Poisson process

- ID: `durrett_ch3_poisson_thinning`

- Section: 3.7.2 Thinning

- Kind: theorem

- Summary: If each point of a rate lambda Poisson process is independently assigned a type j with probability p_j, then the type-specific counting processes are independent Poisson processes with rates lambda p_j.

- Proof idea: Condition on the total count, use multinomial splitting, and identify the joint generating or characteristic function.

- Exam use: Use for marked processes, occupancy via Poissonization, and splitting arrivals into classes.

- Pitfall: Independence of the marks is essential for independent thinned processes.

- Tags: thinning, marked-poisson, independent-poisson

### Poisson arrivals conditional on count are order statistics

- ID: `durrett_ch3_poisson_order_statistics`

- Section: 3.7.3 Conditioning

- Kind: theorem

- Summary: Given N(t)=n in a homogeneous Poisson process, the arrival times in [0,t] have the same joint distribution as the order statistics of n iid uniform(0,t) variables.

- Proof idea: Use the joint density of exponential interarrival times restricted to total arrival time below t and no next arrival before t.

- Exam use: Turns Poisson-process conditioning questions into uniform order-statistic problems.

- Pitfall: This is conditional on the count; unconditionally the arrival times are not a fixed-size sample.

- Tags: poisson-process, conditioning, order-statistics

### Stable law domain of attraction

- ID: `durrett_ch3_stable_law_domain_attraction`

- Section: 3.8 Stable Laws

- Kind: theorem

- Summary: Heavy-tailed iid sums with regularly varying tails of index alpha in (0,2) converge after n^{1/alpha}-type scaling and suitable centering to an alpha-stable law.

- Proof idea: Use triangular-array convergence of small jumps plus Poisson behavior of large jumps encoded through characteristic functions.

- Exam use: Explains nonnormal limits when variance is infinite.

- Pitfall: Centering depends on alpha and tail balance; do not reuse finite-variance CLT normalization.

- Tags: stable-laws, heavy-tails, domain-of-attraction

### Stable characteristic exponent

- ID: `durrett_ch3_stable_characteristic_exponent`

- Section: 3.8 Stable Laws

- Kind: formula

- Summary: Stable laws have characteristic functions with exponent governed by alpha, scale, skewness, and centering parameters; symmetric stable laws have exp(-c |t|^alpha).

- Proof idea: Derive from the limiting Levy measure or from the scaling property of sums.

- Exam use: Recognition tool for identifying stable limits from characteristic functions.

- Pitfall: The alpha=1 case has special logarithmic centering behavior in nonsymmetric cases.

- Tags: stable-laws, characteristic-functions, heavy-tails

### Convergence of types theorem

- ID: `durrett_ch3_convergence_of_types`

- Section: 3.8 Stable Laws

- Kind: theorem

- Summary: If a_n X_n+b_n converges to a nondegenerate limit and c_n X_n+d_n converges to another nondegenerate limit, then c_n/a_n and d_n-b_n c_n/a_n have limits linking the two laws by affine transformation.

- Proof idea: Use tightness and uniqueness of subsequential affine normalizations.

- Exam use: Useful for proving uniqueness of scaling and centering in stable-limit problems.

- Pitfall: The limit must be nondegenerate; constants allow pathological normalization changes.

- Tags: convergence-of-types, normalization, stable-laws

### Infinitely divisible distributions

- ID: `durrett_ch3_infinitely_divisible_definition`

- Section: 3.9 Infinitely Divisible Distributions

- Kind: definition

- Summary: A distribution is infinitely divisible if for every n it can be represented as the law of a sum of n iid random variables.

- Proof idea: Limits of row sums of infinitesimal triangular arrays have this divisibility because each row can be split into many small independent pieces.

- Exam use: Normal, Poisson, compound Poisson, and stable laws are key examples.

- Pitfall: Not every distribution is infinitely divisible; bounded nonconstant laws are not.

- Tags: infinitely-divisible, triangular-arrays, limit-laws

### Levy-Khinchin representation

- ID: `durrett_ch3_levy_khinchin`

- Section: 3.9 Infinitely Divisible Distributions

- Kind: theorem

- Summary: Characteristic functions of infinitely divisible laws have an exponent decomposed into drift, Gaussian variance, and an integral term governed by a Levy measure.

- Proof idea: Analyze limits of triangular-array characteristic exponents and separate small Gaussian fluctuations from jumps.

- Exam use: The master formula unifying normal, Poisson, compound Poisson, and stable laws.

- Pitfall: The Levy measure is not a probability measure; it controls jump intensity and must satisfy an integrability condition near zero.

- Tags: levy-khinchin, infinitely-divisible, levy-measure

### Multivariate weak convergence

- ID: `durrett_ch3_multivariate_weak_convergence`

- Section: 3.10 Limit Theorems in R^d

- Kind: definition

- Summary: Weak convergence in R^d can be defined through bounded continuous test functions, rectangle distribution functions at continuity points, or probability convergence on continuity sets.

- Proof idea: Extend one-dimensional portmanteau and tightness arguments using rectangles that generate the Borel sigma-field.

- Exam use: Needed for joint convergence, random vectors, and multivariate CLT.

- Pitfall: Coordinatewise convergence alone does not imply joint convergence unless dependence is controlled.

- Tags: multivariate, weak-convergence, random-vectors

### Multivariate characteristic function convergence

- ID: `durrett_ch3_multivariate_cf_convergence`

- Section: 3.10 Limit Theorems in R^d

- Kind: theorem

- Summary: Random vectors converge in distribution iff their multivariate characteristic functions converge pointwise to a function continuous at the origin.

- Proof idea: Use multidimensional inversion and tightness, paralleling the one-dimensional Levy continuity theorem.

- Exam use: Primary method for proving joint limit theorems.

- Pitfall: Checking only marginal characteristic functions misses dependence; the full vector transform is needed.

- Tags: multivariate-cf, levy-continuity, joint-convergence

### Cramer-Wold device

- ID: `durrett_ch3_cramer_wold`

- Section: 3.10 Limit Theorems in R^d

- Kind: theorem

- Summary: A sufficient and standard condition for X_n in R^d to converge to X is that theta dot X_n converges in distribution to theta dot X for every theta in R^d.

- Proof idea: Linear projections determine the multivariate characteristic function by phi_X(theta)=E exp(i theta dot X).

- Exam use: Turns multivariate convergence into one-dimensional convergence problems.

- Pitfall: All directions theta are needed; finitely many coordinate projections are not enough.

- Tags: cramer-wold, projections, joint-convergence

### Central limit theorem in R^d

- ID: `durrett_ch3_multivariate_clt`

- Section: 3.10 Limit Theorems in R^d

- Kind: theorem

- Summary: For iid random vectors with mean vector m and covariance matrix Sigma, n^{-1/2} sum (X_i-m) converges to a multivariate normal with covariance Sigma.

- Proof idea: Apply the one-dimensional CLT to theta dot X_i for every theta and then use Cramer-Wold.

- Exam use: Use for joint asymptotic normality and random-walk scaling in higher dimensions.

- Pitfall: A singular covariance matrix still gives a valid degenerate multivariate normal limit.

- Tags: multivariate-clt, normal-vector, covariance

## Exercise Viki Layer

The solved Chapter 3 exercises have a companion retrieval layer:

- `chapter3_exercise_records.jsonl`: 88 solved exercise records with question, solution, knowledge used, method tags, and new-knowledge IDs.
- `chapter3_exercise_method_cards.jsonl`: 10 section-level exercise method cards.
- `chapter3_exercise_new_knowledge.jsonl`: 40 reusable proof/calculation templates extracted from the solved exercises.
- `chapter3_exercise_method_flashcards.tsv`: flashcards for the method cards and new exercise-derived knowledge.
- `chapter3_exercise_viki.md`: human-readable overview of the exercise Viki layer.

# Durrett Chapter 4 LLM Viki: Martingales

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter4.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

## Section Guides

### 4.1 Conditional Expectation

- Goal: Use conditional expectation as an F-measurable Radon-Nikodym object and compute it through partitions, densities, independence, and projection.

- Must master: definition, tower property, taking out what is known, conditional Jensen, L2 projection

- Prelim angle: Nearly every martingale proof is a conditional-expectation proof in disguise.

### 4.2 Martingales, Almost Sure Convergence

- Goal: Build martingales from random walks, stop them, and prove almost sure convergence using upcrossings.

- Must master: martingale definition, random-walk martingales, stopping, upcrossing inequality, a.s. convergence theorem

- Prelim angle: The core toolkit for fair-game and hitting-time problems.

### 4.3 Examples

- Goal: Recognize martingale structures in urns, conditional Borel-Cantelli, likelihood ratios, and branching processes.

- Must master: Doob decomposition, conditional Borel-Cantelli, Polya urn, Radon-Nikodym martingales, branching process martingale

- Prelim angle: Turns abstract convergence theorems into reusable templates for dependent processes.

### 4.4 Doob's Inequality, Convergence in Lp, p>1

- Goal: Control martingale maxima and prove Lp convergence using Doob inequalities.

- Must master: bounded optional sampling, Doob maximal inequality, Lp maximal inequality, Lp convergence, orthogonal increments

- Prelim angle: Use when an exam asks for sup bounds, convergence in Lp, or variance control.

### 4.5 Square Integrable Martingales*

- Goal: Use predictable quadratic variation to prove convergence and strong-law type martingale results.

- Must master: conditional variance, quadratic variation, L2 maximal bounds, martingale strong law

- Prelim angle: A more flexible replacement for independent-increment variance summation.

### 4.6 Uniform Integrability, Convergence in L1

- Goal: Understand when almost sure martingale limits also converge in L1 and preserve expectations.

- Must master: uniform integrability, UI plus probability convergence, closed martingales, Levy upward theorem, Levy 0-1 law

- Prelim angle: This is the checkpoint before using optional stopping at unbounded times.

### 4.7 Backwards Martingales

- Goal: Apply martingale convergence to decreasing filtrations and exchangeable information.

- Must master: backward convergence, Levy downward theorem, SLLN proof, Hewitt-Savage, de Finetti

- Prelim angle: Useful for tail, invariant, and exchangeability questions.

### 4.8 Optional Stopping Theorems

- Goal: Know the hypotheses that make optional stopping valid and apply them to random walks.

- Must master: UI optional stopping, terminal-value criteria, Wald equation, symmetric ruin, biased ruin, exponential bounds

- Prelim angle: One of the highest-yield prelim sections for exact hitting probabilities and expected times.

### 4.9 Combinatorics of Simple Random Walk*

- Goal: Count simple-random-walk paths using reflection, ballot formulas, and arcsine asymptotics.

- Must master: reflection principle, ballot theorem, return probabilities, arcsine laws

- Prelim angle: Provides exact combinatorial alternatives to martingale random-walk arguments.

## Knowledge Pieces

### Conditional expectation as Radon-Nikodym projection

- ID: `durrett_ch4_conditional_expectation_definition`

- Section: 4.1 Conditional Expectation

- Kind: definition

- Summary: E(X|F) is the F-measurable integrable random variable Y satisfying integral_A Y dP = integral_A X dP for every A in F.

- Proof idea: For X >= 0 define a measure nu(A)=integral_A X dP on F and use the Radon-Nikodym theorem; then split X into positive and negative parts.

- Exam use: The starting point for every martingale verification and every conditioning calculation.

- Pitfall: Conditional expectations are only unique up to almost sure equality, so pointwise formulas need version awareness.

- Tags: conditional-expectation, radon-nikodym, sigma-field

### Uniqueness and locality of conditional expectation

- ID: `durrett_ch4_conditional_expectation_uniqueness_locality`

- Section: 4.1 Conditional Expectation

- Kind: theorem

- Summary: Versions of E(X|F) agree almost surely; if X1=X2 on B in F, then their conditional expectations agree on B almost surely.

- Proof idea: Test the positive part of the difference on sets where one candidate exceeds the other by epsilon.

- Exam use: Use locality to compute conditional expectations piecewise on atoms or events known at the conditioning time.

- Pitfall: The event where the variables agree must belong to the conditioning sigma-field.

- Tags: conditional-expectation, locality, versions

### Conditional expectation on a countable partition

- ID: `durrett_ch4_partition_conditioning_formula`

- Section: 4.1.1 Examples

- Kind: formula

- Summary: If F is generated by a countable positive-probability partition, E(X|F) is constant on each atom and equals the average of X over that atom.

- Proof idea: Guess the atomwise average and verify the defining integral identity first on atoms, then by additivity.

- Exam use: Turns abstract conditioning into the familiar finite-state formula used in Bayes and Markov-chain problems.

- Pitfall: Atoms with probability zero cannot be handled by dividing by P(atom).

- Tags: conditioning, partition, bayes

### Conditional density formula

- ID: `durrett_ch4_density_conditioning_formula`

- Section: 4.1.1 Examples

- Kind: formula

- Summary: For a joint density f(x,y), E(g(X)|Y)=h(Y), where h(y) is the conditional-density average of g against f(x,y).

- Proof idea: Write events in sigma(Y) as {Y in B}, integrate over B, and use Fubini to verify the defining identity.

- Exam use: Use for regression-style computations and conditional distribution questions with joint densities.

- Pitfall: Conditioning on Y=y is a density formula, not literal conditioning on a positive-probability event.

- Tags: conditional-density, joint-density, fubini

### Conditioning with independent variables

- ID: `durrett_ch4_independent_conditioning_rule`

- Section: 4.1.1 Examples

- Kind: formula

- Summary: If X and Y are independent and g(x)=E phi(x,Y), then E(phi(X,Y)|X)=g(X).

- Proof idea: Use the product joint law and verify against indicators of events in sigma(X).

- Exam use: A quick way to integrate out fresh independent noise while leaving the present state fixed.

- Pitfall: Do not replace Y by its mean unless phi is linear in Y.

- Tags: independence, conditioning, product-measure

### Linearity, monotonicity, and monotone convergence conditionally

- ID: `durrett_ch4_conditional_expectation_properties`

- Section: 4.1.2 Properties

- Kind: theorem

- Summary: Conditional expectation is linear, preserves order, and respects monotone limits under the same integrability hypotheses as ordinary expectation.

- Proof idea: Verify the defining identity for linearity; for order, test the positive part; for monotone convergence, use ordinary dominated or monotone convergence on each conditioning event.

- Exam use: These are the algebra rules behind almost every martingale manipulation.

- Pitfall: Check integrability hypotheses before using linearity with signed variables.

- Tags: conditional-expectation, linearity, monotone-convergence

### Conditional Jensen and Lp contraction

- ID: `durrett_ch4_conditional_jensen_contraction`

- Section: 4.1.2 Properties

- Kind: theorem

- Summary: For convex phi, phi(E(X|F)) <= E(phi(X)|F); in particular conditional expectation is a contraction on Lp for p >= 1.

- Proof idea: Write a convex function as a supremum of rational affine minorants and apply monotonicity and linearity.

- Exam use: Use to prove submartingale transforms and uniform Lp bounds after conditioning.

- Pitfall: The inequality is almost sure, and the convex function must be integrable after composition.

- Tags: jensen, lp-contraction, conditional-expectation

### Tower property: the smaller sigma-field wins

- ID: `durrett_ch4_tower_property_smaller_sigma_field_wins`

- Section: 4.1.2 Properties

- Kind: theorem

- Summary: If F1 subset F2, then E(E(X|F1)|F2)=E(X|F1) and E(E(X|F2)|F1)=E(X|F1).

- Proof idea: The first identity is measurability; the second verifies the defining identity on sets in F1.

- Exam use: Essential for collapsing repeated conditionings in martingale and Markov arguments.

- Pitfall: The order of unrelated sigma-fields cannot be swapped; nesting is the whole point.

- Tags: tower-property, conditioning, sigma-fields

### Taking out what is known

- ID: `durrett_ch4_taking_out_what_is_known`

- Section: 4.1.2 Properties

- Kind: theorem

- Summary: If X is F-measurable and the products are integrable, then E(XY|F)=X E(Y|F).

- Proof idea: Prove first for indicators in F, extend to simple functions, then use monotone convergence and signed decompositions.

- Exam use: Lets predictable factors pass through conditional expectation in martingale increment calculations.

- Pitfall: The multiplier must be measurable with respect to the conditioning sigma-field.

- Tags: conditioning, measurability, predictable

### Conditional expectation as L2 best predictor

- ID: `durrett_ch4_conditional_expectation_l2_projection`

- Section: 4.1.2 Properties

- Kind: theorem

- Summary: When EX^2 is finite, E(X|F) is the F-measurable square-integrable variable minimizing E(X-Y)^2.

- Proof idea: Show X-E(X|F) is orthogonal to every L2(F) random variable and use the Pythagorean identity.

- Exam use: Useful for variance decompositions and interpreting conditional expectation as optimal prediction.

- Pitfall: The projection picture needs second moments; L1 conditional expectation exists more generally.

- Tags: l2-projection, best-predictor, orthogonality

### Regular conditional distributions

- ID: `durrett_ch4_regular_conditional_distribution`

- Section: 4.1.3 Regular Conditional Probabilities*

- Kind: definition

- Summary: A regular conditional distribution gives a probability kernel whose A-coordinate versions equal P(X in A|G).

- Proof idea: For nice spaces construct conditional distribution functions on rational cut points and extend to measures.

- Exam use: Use when a problem wants conditioning as a genuine conditional law rather than one function at a time.

- Pitfall: Regular conditional probabilities need not exist on arbitrary measurable spaces.

- Tags: regular-conditional-probability, kernels, nice-spaces

### Martingale, submartingale, and supermartingale definitions

- ID: `durrett_ch4_martingale_definition`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: definition

- Summary: An adapted integrable process is a martingale when E(X_{n+1}|F_n)=X_n; replacing equality by >= or <= gives submartingales or supermartingales.

- Proof idea: The definition formalizes fair, favorable, and unfavorable games through one-step conditional means.

- Exam use: Every martingale problem starts by identifying the filtration, integrability, adaptedness, and the one-step conditional expectation.

- Pitfall: The filtration is part of the data; a process can be a martingale for one filtration and not another.

- Tags: martingales, filtration, adapted

### Linear, quadratic, and exponential random-walk martingales

- ID: `durrett_ch4_random_walk_martingales`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: example-bank

- Summary: For iid increments, S_n-n mu, S_n^2-n sigma^2 in the centered finite-variance case, and exp(theta S_n)/phi(theta)^n are martingales under their natural hypotheses.

- Proof idea: Condition on the past and use independence of the next increment, expanding the square or moment generating factor.

- Exam use: These are the main engines for gambler's ruin, hitting probabilities, Wald identities, and exponential tail bounds.

- Pitfall: The exponential martingale requires the moment generating function to be finite at the chosen theta.

- Tags: random-walk, exponential-martingale, quadratic-martingale

### Multi-step conditional expectation property

- ID: `durrett_ch4_multi_step_martingale_property`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: For n>m, martingales satisfy E(X_n|F_m)=X_m; submartingales give >= and supermartingales give <=.

- Proof idea: Iterate the one-step definition using the tower property.

- Exam use: Use whenever a future stopped or terminal value is related back to present information.

- Pitfall: The direction of the inequality reverses between submartingales and supermartingales.

- Tags: martingales, tower-property, filtration

### Convex transforms make submartingales

- ID: `durrett_ch4_convex_transform_submartingale`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: A convex function of a martingale is a submartingale; an increasing convex function of a submartingale is also a submartingale.

- Proof idea: Apply conditional Jensen, then use monotonicity when the input process is only a submartingale.

- Exam use: Build nonnegative submartingales such as |X_n|, X_n^2, and exp(theta X_n) for maximal inequalities.

- Pitfall: The transformed variables must be integrable.

- Tags: jensen, submartingale, convexity

### Martingale transforms and no profitable gambling systems

- ID: `durrett_ch4_martingale_transform_no_gambling_system`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: If H_n is nonnegative predictable and X is a supermartingale, then the gains process sum H_m(X_m-X_{m-1}) is a supermartingale.

- Proof idea: Take conditional expectations term by term, using that H_m is known at time m-1.

- Exam use: Formalizes optional betting strategies and proves stopped supermartingales remain supermartingales.

- Pitfall: Predictability is essential; stakes cannot depend on the next outcome.

- Tags: martingale-transform, predictable, gambling-system

### Stopped processes preserve martingale type

- ID: `durrett_ch4_stopped_process_supermartingale`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: If N is a stopping time and X is a supermartingale, then X_{N wedge n} is a supermartingale; analogous statements hold for martingales and submartingales.

- Proof idea: Represent stopping as a predictable strategy that bets until N and then stops.

- Exam use: Use before applying convergence or inequality theorems to hitting-time stopped processes.

- Pitfall: Stopping alone does not guarantee equality of expectations at unbounded times.

- Tags: stopping-time, stopped-process, optional-stopping

### Doob upcrossing inequality

- ID: `durrett_ch4_upcrossing_inequality`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: For a submartingale, the expected number of upcrossings of [a,b] up to n is bounded by E(X_n-a)^+/(b-a).

- Proof idea: Buy at a and sell at b using a predictable switching strategy, then compare accumulated gains to the positive part of the terminal value.

- Exam use: The key tool for proving almost sure convergence from bounded positive expectations.

- Pitfall: The interval is [a,b] with a<b; upcrossings are completed crossings, not mere visits.

- Tags: upcrossing, submartingale, convergence

### Submartingale almost sure convergence theorem

- ID: `durrett_ch4_martingale_convergence_theorem`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: If X_n is a submartingale with sup_n E X_n^+ finite, then X_n converges almost surely to a finite limit.

- Proof idea: Use the upcrossing inequality to rule out infinitely many oscillations across rational intervals and control the positive tail.

- Exam use: A default convergence theorem for bounded or nonnegative martingales after choosing the right sign.

- Pitfall: Almost sure convergence does not automatically imply L1 convergence or preservation of expectations.

- Tags: martingale-convergence, upcrossing, almost-sure

### Nonnegative supermartingale convergence

- ID: `durrett_ch4_nonnegative_supermartingale_convergence`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: corollary

- Summary: Every nonnegative supermartingale converges almost surely to a finite limit, with finite expected limit bounded by the initial expectation.

- Proof idea: Apply the submartingale convergence theorem to -X_n or use the boundedness of expectations coming from nonnegativity.

- Exam use: Extremely useful for likelihood ratios, branching process normalizations, and stopped random walks.

- Pitfall: The limit can have smaller expectation than X_0; equality needs uniform integrability or stronger optional stopping conditions.

- Tags: nonnegative-supermartingale, almost-sure-convergence, fatou

### Bounded-increment convergence criterion

- ID: `durrett_ch4_bounded_increment_convergence`

- Section: 4.3.1 Bounded Increments

- Kind: criterion

- Summary: A supermartingale with bounded increments cannot keep drifting on a bounded interval without converging; stopping and shifting make it nonnegative.

- Proof idea: Stop on a lower barrier and add a constant, then apply nonnegative supermartingale convergence.

- Exam use: Use for random walks or games where increments are controlled but the process is not globally nonnegative.

- Pitfall: You must first localize so the shifted stopped process is nonnegative.

- Tags: bounded-increments, stopping, convergence

### Doob decomposition

- ID: `durrett_ch4_doob_decomposition`

- Section: 4.3 Examples

- Kind: theorem

- Summary: Every submartingale decomposes uniquely into a martingale plus an increasing predictable process starting at zero.

- Proof idea: Define the compensator increments as E(X_n-X_{n-1}|F_{n-1}) and subtract their cumulative sum.

- Exam use: Separates random fluctuation from predictable drift in counting-process and indicator-sum arguments.

- Pitfall: The compensator is predictable, not optional; its increment is known one step earlier.

- Tags: doob-decomposition, compensator, submartingale

### Conditional Borel-Cantelli lemma

- ID: `durrett_ch4_conditional_borel_cantelli`

- Section: 4.3 Examples

- Kind: theorem

- Summary: For adapted events B_n, occurrence infinitely often is controlled by the divergence or convergence of the conditional probability sums E(1_{B_n}|F_{n-1}).

- Proof idea: Apply martingale convergence to the difference between actual counts and conditional expected counts.

- Exam use: Use for dependent trials where ordinary independence is unavailable but conditional probabilities are tractable.

- Pitfall: The conditioning must be on the past; replacing it by unconditional probabilities loses the theorem's content.

- Tags: borel-cantelli, conditional-probability, martingales

### Polya urn proportion martingale

- ID: `durrett_ch4_polya_urn_martingale`

- Section: 4.3.2 Polya's Urn Scheme

- Kind: example-pattern

- Summary: In Polya's urn, the fraction of balls of one color is a bounded martingale and therefore converges almost surely.

- Proof idea: Condition on the current urn composition to show the next expected proportion equals the current proportion.

- Exam use: A model example for bounded martingale convergence and beta-limit intuition.

- Pitfall: Almost sure convergence alone does not identify the limiting distribution without extra computation.

- Tags: polya-urn, bounded-martingale, beta

### Radon-Nikodym derivative martingales

- ID: `durrett_ch4_radon_nikodym_derivative_martingale`

- Section: 4.3.3 Radon-Nikodym Derivatives

- Kind: theorem

- Summary: If mu_n and nu_n are restrictions to F_n with mu_n absolutely continuous with respect to nu_n, then dmu_n/dnu_n forms a nonnegative martingale under nu.

- Proof idea: Verify the conditional expectation identity by integrating over sets in the smaller sigma-field.

- Exam use: Use to compare infinite product measures and prove absolute-continuity versus singularity alternatives.

- Pitfall: Finite-dimensional absolute continuity does not by itself guarantee infinite-dimensional absolute continuity.

- Tags: radon-nikodym, likelihood-ratio, absolute-continuity

### Branching process normalized martingale

- ID: `durrett_ch4_branching_process_normalized_martingale`

- Section: 4.3.4 Branching Processes

- Kind: example-pattern

- Summary: For a Galton-Watson process with mean mu, Z_n/mu^n is a nonnegative martingale when mu is positive.

- Proof idea: Condition on the current population and use that the next generation is a sum of Z_n iid offspring variables.

- Exam use: The central martingale for extinction, survival, and supercritical growth questions.

- Pitfall: In the supercritical case the martingale limit may still be zero unless an L log L condition holds.

- Tags: branching-process, galton-watson, nonnegative-martingale

### Bounded optional sampling inequality

- ID: `durrett_ch4_bounded_stopping_submartingale_expectation`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: theorem

- Summary: If X is a submartingale and N is a bounded stopping time, then E X_0 <= E X_N <= E X_k for a bound k on N.

- Proof idea: Use the stopped submartingale and monotonicity of expectations over deterministic times.

- Exam use: The bounded-time version of optional sampling used inside maximal inequality proofs.

- Pitfall: Boundedness of the stopping time is doing real work; unbounded stopping can fail.

- Tags: optional-sampling, bounded-stopping, submartingale

### Doob maximal inequality

- ID: `durrett_ch4_doob_maximal_inequality`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: theorem

- Summary: For a submartingale, lambda P(max_{m<=n} X_m >= lambda) is bounded by the expected terminal value on the event that the maximum exceeds lambda.

- Proof idea: Stop the first time the process crosses lambda and apply bounded optional sampling.

- Exam use: Use to control suprema of martingales, derive Kolmogorov inequalities, and prove Lp convergence.

- Pitfall: Apply it to nonnegative submartingales such as |X_n| or X_n^2 when signs are an issue.

- Tags: doob-inequality, maximal-inequality, submartingale

### Doob Lp maximum inequality

- ID: `durrett_ch4_lp_maximum_inequality`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: theorem

- Summary: For p>1, the Lp norm of max_{m<=n} |X_m| is bounded by p/(p-1) times the Lp norm of X_n for martingales and suitable submartingales.

- Proof idea: Integrate Doob's maximal tail bound over lambda and use calculus/Holder-style estimates.

- Exam use: The main route from uniform Lp bounds to almost sure and Lp convergence.

- Pitfall: There is no comparable L1 maximal inequality without extra hypotheses.

- Tags: lp, maximal-inequality, doob

### Lp martingale convergence theorem

- ID: `durrett_ch4_lp_martingale_convergence`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: theorem

- Summary: If a martingale has sup_n E|X_n|^p finite for some p>1, then X_n converges almost surely and in Lp.

- Proof idea: Use submartingale convergence for |X_n| and Doob's Lp maximum inequality for uniform integrability of the tail supremum.

- Exam use: A clean sufficient condition for exchanging martingale limits with p-th moments.

- Pitfall: The theorem needs p>1; L1 convergence requires uniform integrability instead.

- Tags: lp-convergence, martingales, uniform-lp-bound

### Orthogonality of square-integrable martingale increments

- ID: `durrett_ch4_orthogonal_martingale_increments`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: theorem

- Summary: Square-integrable martingale increments are orthogonal, so variances of sums add across increments.

- Proof idea: For i<j, condition the product of the earlier increment with the later increment on F_{j-1}.

- Exam use: Use for L2 bounds, variance computations, and quadratic martingale arguments.

- Pitfall: Orthogonality is not independence; it is a second-moment identity.

- Tags: orthogonality, increments, l2-martingales

### Conditional variance formula for martingales

- ID: `durrett_ch4_conditional_variance_formula_martingales`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: formula

- Summary: For square-integrable martingales, conditional second-moment growth is the sum of conditional variances of increments.

- Proof idea: Expand X_{n+1}^2-X_n^2 and condition on the past so the cross term vanishes.

- Exam use: Use to estimate quadratic variation and prove convergence from summable conditional variances.

- Pitfall: Use conditional variances of increments, not unconditional variances unless independence or identical structure justifies it.

- Tags: conditional-variance, quadratic-variation, l2

### Square-integrable martingales and quadratic variation

- ID: `durrett_ch4_square_integrable_martingale_quadratic_variation`

- Section: 4.5 Square Integrable Martingales*

- Kind: theorem

- Summary: For square-integrable martingales, the predictable accumulated conditional variance A_n governs maximal L2 bounds and convergence.

- Proof idea: Apply Doob's L2 inequality to the stopped martingale and compare E X_n^2 with E A_n.

- Exam use: Use when convergence depends on summability of conditional variances rather than bounded increments.

- Pitfall: The predictable quadratic variation is not the same as the realized squared-increment sum.

- Tags: square-integrable, quadratic-variation, predictable-variation

### Martingale strong-law normalization

- ID: `durrett_ch4_martingale_strong_law_from_variances`

- Section: 4.5 Square Integrable Martingales*

- Kind: criterion

- Summary: If a square-integrable martingale has controlled predictable quadratic variation, then X_n normalized by a suitable increasing function of A_n tends to zero.

- Proof idea: Rescale increments with a predictable factor, show the transformed martingale converges, then undo the normalization.

- Exam use: Generalizes Kolmogorov strong-law arguments to martingale differences.

- Pitfall: Choose a normalization satisfying the required integral/summability condition.

- Tags: strong-law, martingale-differences, normalization

### Uniform integrability

- ID: `durrett_ch4_uniform_integrability_definition`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: definition

- Summary: A family is uniformly integrable when the tail expectations sup E(|X|; |X|>K) go to zero as K goes to infinity.

- Proof idea: Tail control is equivalent to domination by a superlinear Orlicz function and implies L1 tightness of mass.

- Exam use: The exact condition needed to upgrade probability or a.s. convergence to L1 convergence.

- Pitfall: Bounded L1 norms alone do not imply uniform integrability.

- Tags: uniform-integrability, l1, tail-control

### Uniform integrability plus probability convergence gives L1 convergence

- ID: `durrett_ch4_ui_plus_probability_equals_l1`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: theorem

- Summary: If X_n is uniformly integrable and X_n converges in probability to X, then X is integrable and X_n converges to X in L1.

- Proof idea: Split expectations on {|X_n-X| small}, on moderate tails, and on large tails controlled by uniform integrability.

- Exam use: Use after proving almost sure martingale convergence to obtain L1 convergence.

- Pitfall: Convergence in probability without uniform integrability is not enough for L1 convergence.

- Tags: uniform-integrability, l1-convergence, probability-convergence

### Submartingale L1 convergence equivalences

- ID: `durrett_ch4_submartingale_l1_convergence_equivalences`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: theorem

- Summary: For submartingales, uniform integrability is equivalent to almost sure and L1 convergence to an integrable limit under the standard convergence hypotheses.

- Proof idea: Combine submartingale a.s. convergence with the UI-to-L1 theorem and the implication from L1 convergence to uniform integrability.

- Exam use: Decides when the limit preserves first moments.

- Pitfall: Almost sure convergence from Chapter 4.2 by itself is weaker than L1 convergence.

- Tags: submartingale, uniform-integrability, l1-convergence

### Closed martingales and uniform integrability

- ID: `durrett_ch4_closed_martingales_ui_equivalence`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: theorem

- Summary: A martingale is uniformly integrable iff it converges in L1 iff it can be written as X_n=E(X|F_n) for some integrable terminal variable X.

- Proof idea: Use L1 convergence to identify the terminal variable, and use conditional expectation contraction to prove UI for closed martingales.

- Exam use: The main structural test for optional stopping at unbounded times.

- Pitfall: A martingale can converge a.s. but fail to be closed by an L1 terminal variable.

- Tags: closed-martingale, uniform-integrability, l1

### Levy upward theorem

- ID: `durrett_ch4_levy_upward_theorem`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: theorem

- Summary: If F_n increases to F_infinity, then E(X|F_n) converges almost surely and in L1 to E(X|F_infinity).

- Proof idea: Recognize E(X|F_n) as a closed uniformly integrable martingale and identify its limit by testing against the union sigma-field.

- Exam use: Use to prove Levy's 0-1 law and conditional dominated convergence.

- Pitfall: The limiting sigma-field is generated by the increasing union, not simply the pointwise union as a collection.

- Tags: levy-theorem, increasing-filtration, conditional-expectation

### Levy's 0-1 law

- ID: `durrett_ch4_levy_zero_one_law`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: theorem

- Summary: If A belongs to the limiting sigma-field of an increasing filtration, then P(A|F_n) converges almost surely to 1_A.

- Proof idea: Apply Levy's upward theorem to X=1_A.

- Exam use: Use to convert better and better finite information into eventual certainty for tail-like events inside the generated limit.

- Pitfall: This is different from Kolmogorov's 0-1 law, which concerns independent tail sigma-fields.

- Tags: levy-zero-one, conditional-probability, filtration

### Backward martingale convergence

- ID: `durrett_ch4_backward_martingale_convergence`

- Section: 4.7 Backwards Martingales

- Kind: theorem

- Summary: A martingale indexed backward in time, with decreasing sigma-fields, converges almost surely and in L1 to its conditional expectation on the tail intersection.

- Proof idea: Use the upcrossing argument on finite backward windows, then uniform integrability from representation as E(X_0|F_n).

- Exam use: The engine behind the strong law, Hewitt-Savage, and de Finetti-style results.

- Pitfall: The index direction matters: sigma-fields decrease as time moves backward.

- Tags: backward-martingale, tail-sigma-field, l1-convergence

### Levy downward theorem

- ID: `durrett_ch4_levy_downward_theorem`

- Section: 4.7 Backwards Martingales

- Kind: theorem

- Summary: If F_n decreases to F_{-infinity}, then E(Y|F_n) converges almost surely and in L1 to E(Y|F_{-infinity}).

- Proof idea: View the conditional expectations as a backward martingale and identify the limit by testing on the intersection sigma-field.

- Exam use: Use for exchangeability, tail sigma-fields, and reverse filtrations.

- Pitfall: Do not replace the intersection by a limiting union; this is the downward theorem.

- Tags: levy-downward, backward-martingale, conditional-expectation

### Strong law via backward martingales

- ID: `durrett_ch4_slln_via_backward_martingales`

- Section: 4.7 Backwards Martingales

- Kind: example-pattern

- Summary: For iid integrable variables, sample averages can be represented through decreasing symmetric-information sigma-fields and converge to the mean.

- Proof idea: Use exchangeability of finite averages and the backward martingale convergence theorem; the tail/invariant sigma-field is trivial.

- Exam use: A conceptual proof of the strong law that also prepares de Finetti arguments.

- Pitfall: The iid and integrability assumptions are doing the work; this is not a variance proof.

- Tags: strong-law, iid, backward-martingale

### Hewitt-Savage 0-1 law

- ID: `durrett_ch4_hewitt_savage_zero_one`

- Section: 4.7 Backwards Martingales

- Kind: theorem

- Summary: For iid sequences, every event invariant under finite permutations has probability 0 or 1.

- Proof idea: Average conditional indicators over symmetric sigma-fields and use backward martingale convergence to show the event is independent of itself.

- Exam use: Use when an event is exchangeable rather than merely tail-measurable.

- Pitfall: Permutation invariance is stronger/different than tail measurability; check the event carefully.

- Tags: hewitt-savage, zero-one-law, exchangeability

### de Finetti theorem for exchangeable sequences

- ID: `durrett_ch4_definetti_theorem`

- Section: 4.7 Backwards Martingales

- Kind: theorem

- Summary: Exchangeable sequences are conditionally iid given the exchangeable tail information; in the binary case they are mixtures of iid Bernoulli sequences.

- Proof idea: Use backward martingales to identify empirical averages and finite-dimensional conditional laws.

- Exam use: Recognize hidden-random-parameter representations in exchangeable models.

- Pitfall: Exchangeability is weaker than independence but stronger than identical marginal distributions.

- Tags: de-finetti, exchangeability, mixtures

### Optional stopping for uniformly integrable martingales

- ID: `durrett_ch4_optional_stopping_ui`

- Section: 4.8 Optional Stopping Theorems

- Kind: theorem

- Summary: Uniformly integrable martingales satisfy optional sampling for arbitrary stopping times, with stopped values inheriting the martingale inequalities.

- Proof idea: Use L1 convergence of stopped processes and bounded optional sampling on truncated stopping times.

- Exam use: The cleanest condition under which E X_N = E X_0 is valid for unbounded N.

- Pitfall: Without uniform integrability or another sufficient condition, optional stopping can fail dramatically.

- Tags: optional-stopping, uniform-integrability, stopping-time

### Optional stopping with integrable terminal value

- ID: `durrett_ch4_optional_stopping_integrable_terminal`

- Section: 4.8 Optional Stopping Theorems

- Kind: criterion

- Summary: If X_N is integrable and the pre-stopping tails X_n 1_{N>n} are uniformly integrable, then X_{N wedge n} is uniformly integrable and optional stopping applies.

- Proof idea: Decompose X_{N wedge n} into the terminal-on-stopped part and the still-running part, then use UI.

- Exam use: A practical checklist for hitting times where the stopped value is bounded or controlled.

- Pitfall: Finite expectation of N alone is not the same as this UI tail condition, though bounded increments can imply useful variants.

- Tags: optional-stopping, terminal-value, uniform-integrability

### Wald's equation via optional stopping

- ID: `durrett_ch4_wald_equation`

- Section: 4.8 Optional Stopping Theorems

- Kind: theorem

- Summary: For iid integrable increments with mean mu, S_N has expectation mu E N under suitable stopping and integrability conditions.

- Proof idea: Apply optional stopping to the martingale S_n-n mu.

- Exam use: Use for expected sums at stopping times, especially random walks and renewal-style counts.

- Pitfall: Independence of N from increments is not the right general condition; N is often a stopping time, and optional stopping hypotheses must be checked.

- Tags: wald-equation, random-walk, optional-stopping

### Symmetric gambler's ruin via martingales

- ID: `durrett_ch4_symmetric_gamblers_ruin`

- Section: 4.8.1 Applications to Random Walks

- Kind: example-pattern

- Summary: For symmetric simple random walk stopped on hitting a or b, optional stopping of S_n gives linear hitting probabilities and S_n^2-n gives expected hitting times.

- Proof idea: Stop the linear and quadratic martingales at bounded barriers, then solve the resulting algebraic equations.

- Exam use: High-yield prelim template for hitting probabilities and mean exit times.

- Pitfall: For one-sided unbounded hitting times, use truncation or extra arguments before sending the bound to infinity.

- Tags: gambler-ruin, symmetric-random-walk, hitting-time

### Asymmetric gambler's ruin via exponential martingales

- ID: `durrett_ch4_asymmetric_gamblers_ruin`

- Section: 4.8.1 Applications to Random Walks

- Kind: example-pattern

- Summary: For biased simple random walk, an exponential martingale r^{S_n} gives nonlinear hitting probabilities and finite expected hitting times in the drift direction.

- Proof idea: Choose r so E r^{xi}=1 and apply optional stopping at two-sided barriers.

- Exam use: Use when the walk has drift and the harmonic function is exponential rather than linear.

- Pitfall: The symmetric formulas are limiting cases; plugging p=q into biased formulas may require taking a limit.

- Tags: biased-random-walk, exponential-martingale, gambler-ruin

### Insurance ruin exponential bound

- ID: `durrett_ch4_insurance_ruin_exponential_bound`

- Section: 4.8.1 Applications to Random Walks

- Kind: example-pattern

- Summary: If a random walk has a positive adjustment coefficient theta with E exp(theta xi)=1, exponential martingales bound the probability of ever hitting a bad lower level.

- Proof idea: Stop the exponential martingale at ruin or an upper truncation and let the truncation grow.

- Exam use: Use for Cramer-Lundberg style ruin bounds and rare-event hitting estimates.

- Pitfall: The bound needs the exponential moment equation at a positive theta.

- Tags: ruin-probability, exponential-martingale, tail-bound

### Reflection principle

- ID: `durrett_ch4_reflection_principle`

- Section: 4.9 Combinatorics of Simple Random Walk*

- Kind: theorem

- Summary: For simple random walk paths, paths crossing a barrier can be counted by reflecting the path after the first hit.

- Proof idea: Map each bad path bijectively to a reflected path with a shifted endpoint.

- Exam use: Use for exact hitting and maximum distributions without martingale machinery.

- Pitfall: The reflection is a path-counting bijection; keep parity and endpoints consistent.

- Tags: reflection-principle, simple-random-walk, path-counting

### Ballot theorem

- ID: `durrett_ch4_ballot_theorem`

- Section: 4.9 Combinatorics of Simple Random Walk*

- Kind: theorem

- Summary: If one candidate finishes ahead, the probability that they stayed strictly ahead throughout has a simple ratio depending on the final margin.

- Proof idea: Count all paths with a fixed endpoint and subtract those that touch or cross the forbidden boundary using reflection.

- Exam use: Use for positivity-conditioned walks and first-passage combinatorics.

- Pitfall: Strict positivity versus nonnegativity changes the boundary and constants.

- Tags: ballot-theorem, reflection-principle, random-walk

### Arcsine laws for simple random walk

- ID: `durrett_ch4_arcsine_laws_random_walk`

- Section: 4.9 Combinatorics of Simple Random Walk*

- Kind: theorem

- Summary: The last zero time and the occupation time above zero for long symmetric simple random walks have arcsine limiting distributions.

- Proof idea: Factor exact probabilities using return probabilities, then apply central binomial asymptotics to obtain the arcsine density.

- Exam use: Recognize that typical paths spend a surprisingly large fraction of time mostly positive or mostly negative.

- Pitfall: The arcsine density is U-shaped; intuition based on concentration near one half is wrong.

- Tags: arcsine-law, occupation-time, simple-random-walk

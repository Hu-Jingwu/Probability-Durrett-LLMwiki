# Durrett Probability LLM Viki

Source: local Durrett chapter PDFs and solved exercise files under `Probability/`.

This is the unified Probability LLM/Viki knowledge base assembled from the chapter-level viki datasets. It keeps each chapter's original retrieval notes, then appends exercise method viki material where available.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

## Corpus Index

- Chapter 1: Durrett Chapter 1 LLM Viki: Probability Foundations (7 sections, 70 knowledge pieces; 56 solved-exercise records).
- Chapter 2: Durrett Chapter 2 LLM Viki: Laws of Large Numbers (7 sections, 103 knowledge pieces).
- Chapter 3: Durrett Chapter 3 LLM Viki: Central Limit Theorems (10 sections, 53 knowledge pieces; 88 solved-exercise records).
- Chapter 4: Durrett Chapter 4 LLM Viki: Martingales (9 sections, 54 knowledge pieces; 68 solved-exercise records).
- Chapter 5: Durrett Chapter 5 LLM Viki: Markov Chains (8 sections, 50 knowledge pieces; 55 solved-exercise records).
- Chapter 6: Durrett Chapter 6 LLM Viki: Ergodic Theorems (5 sections, 51 knowledge pieces; 19 solved-exercise records).
- Chapter 7: Durrett Chapter 7 LLM Viki: Brownian Motion (6 sections, 45 knowledge pieces; 31 solved-exercise records).
- Chapter 8: Durrett Chapter 8 LLM Viki: Applications to Random Walk (5 sections, 28 knowledge pieces; 9 solved-exercise records).
- Chapter 9: Durrett Chapter 9 LLM Viki: Multidimensional Brownian Motion (8 sections, 69 knowledge pieces; 31 solved-exercise records).

## Unified Files

- `probability_knowledge_pieces.jsonl`: all chapter knowledge pieces.
- `probability_section_guides.jsonl`: all section study guides.
- `probability_exercise_records.jsonl`: all available solved-exercise records.
- `probability_exercise_method_cards.jsonl`: all available exercise method cards.
- `probability_exercise_new_knowledge.jsonl`: all exercise-derived reusable knowledge pieces.
- `probability_flashcards.tsv`: all chapter flashcards.
- `probability_exercise_method_flashcards.tsv`: all exercise method flashcards.
- `manifest.json`: corpus counts and chapter provenance.

## Chapter 1

### Durrett Chapter 1 LLM Viki: Probability Foundations

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter1.pdf`.

This unified Chapter 1 knowledge base includes the original textbook knowledge pieces plus exercise-derived method patterns from the solved Chapter 1 exercises.

Exercise source: `Probability/Exercises/Chapter1/Chapter1Exercises.tex` and `Probability/Exercises/Chapter1/Chapter1Exercises.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

#### Section Guides

##### 1.1 Probability Spaces

- Goal: Speak fluently about events, sigma-fields, probability measures, and extension from simple generating classes.

- Must master: probability space, sigma-field, continuity of measure, Stieltjes measure, semialgebra extension

- Prelim angle: Often appears as proof scaffolding inside convergence, Borel-Cantelli, and distribution problems rather than as a standalone question.

##### 1.2 Distributions

- Goal: Move between laws, CDFs, densities/mass functions, atoms, and transformations.

- Must master: CDF properties, valid CDF to law, atoms as jumps, normal tail bounds

- Prelim angle: Directly relevant to tightness, weak convergence, and characteristic-function problems.

##### 1.3 Random Variables

- Goal: Prove measurability quickly using generators and closure under limits/composition.

- Must master: measurable maps, generator checking, arithmetic and limits of random variables, sigma(X) factorization

- Prelim angle: Needed whenever an exam asks you to justify conditional expectation, filtrations, or convergence events.

##### 1.4 Integration

- Goal: Understand Lebesgue integral construction enough to know why the limit theorems work.

- Must master: simple functions, nonnegative integral, positive/negative parts, linearity

- Prelim angle: Usually supports expectation proofs; less often tested as pure integration construction.

##### 1.5 Properties of the Integral

- Goal: Use Jensen, Holder, Minkowski, Fatou, MCT, DCT, and bounded convergence with exact hypotheses.

- Must master: Jensen, Holder, Minkowski, Fatou, MCT, DCT

- Prelim angle: High-frequency toolkit for bounding probabilities and passing limits under expectations.

##### 1.6 Expected Value

- Goal: Treat expectation as integration and deploy inequalities/change-of-variables confidently.

- Must master: linearity, Markov/Chebyshev, expectation limit theorems, change of variables, tail integral

- Prelim angle: Central to LLN, CLT, martingale, and random-series problems.

##### 1.7 Product Measures, Fubini's Theorem

- Goal: Know when iterated integration is legal and how product measures support joint distributions.

- Must master: product measure, sections, Fubini/Tonelli, product laws

- Prelim angle: Used in expectation swaps, independence calculations, and conditioning foundations.

#### Knowledge Pieces

##### Probability space

- ID: `durrett_ch1_probability_space`

- Section: 1.1 Probability Spaces

- Kind: definition

- Summary: A probability model is a triple (Omega, F, P): outcomes, a sigma-field of events, and a countably additive probability measure with total mass 1.

- Proof idea: Most elementary probability identities are consequences of complement closure, countable union closure, and countable additivity.

- Exam use: Use this as the opening language for proofs involving events, limsup/liminf events, and Borel-Cantelli later in Chapter 2.

- Pitfall: Do not treat arbitrary subsets as events unless F is the full power set; measurability is part of the model.

- Tags: probability-space, sigma-field, measure

##### Sigma-field closure rules

- ID: `durrett_ch1_sigma_field`

- Section: 1.1 Probability Spaces

- Kind: definition

- Summary: A sigma-field is closed under complements and countable unions, hence also under countable intersections and finite set operations.

- Proof idea: Use De Morgan's laws to derive intersection closure from complement and union closure.

- Exam use: When proving a random object is measurable, show that a convenient generating class of inverse images lies in F.

- Pitfall: A countable union is allowed; an arbitrary uncountable union need not be in the sigma-field.

- Tags: sigma-field, closure, measurability

##### Continuity of measure

- ID: `durrett_ch1_measure_continuity`

- Section: 1.1 Probability Spaces

- Kind: theorem

- Summary: For increasing events A_n, P(union A_n) is the limit of P(A_n). For decreasing events A_n with finite first measure, P(intersection A_n) is the limit of P(A_n).

- Proof idea: Write increasing differences as disjoint pieces; for decreasing sets apply the increasing result to complements or differences.

- Exam use: Essential for limits of events, almost sure convergence criteria, and first Borel-Cantelli arguments.

- Pitfall: For decreasing continuity, the finite-measure condition matters for general measures; it is automatic under probability measures.

- Tags: continuity-from-below, continuity-from-above, events

##### Discrete probability spaces

- ID: `durrett_ch1_discrete_probability_space`

- Section: 1.1 Probability Spaces

- Kind: example

- Summary: On a countable sample space, assign nonnegative masses p(omega) summing to 1, and define P(A) as the sum over omega in A.

- Proof idea: Countable additivity reduces to rearranging nonnegative series.

- Exam use: Useful for checking intuition before proving the analogous statement for general measures.

- Pitfall: If the sample space is uncountable, point masses need not determine the whole law.

- Tags: discrete, mass-function, countable

##### Stieltjes measures from distribution-like functions

- ID: `durrett_ch1_stieltjes_measure`

- Section: 1.1 Probability Spaces

- Kind: theorem

- Summary: A nondecreasing right-continuous function with suitable limits defines a unique measure on the Borel line via interval increments.

- Proof idea: First define the measure on intervals, verify finite additivity and continuity, then extend to the generated sigma-field.

- Exam use: This is the bridge from CDFs to probability measures on R.

- Pitfall: Right-continuity is not cosmetic; it pins down the measure on half-infinite intervals and atoms.

- Tags: stieltjes, cdf, borel-measure

##### Extension from semialgebras

- ID: `durrett_ch1_semialgebra_extension`

- Section: 1.1 Probability Spaces

- Kind: proof-template

- Summary: A measure-like set function on a semialgebra can be extended when it has the right countable additivity/continuity behavior on the generating class.

- Proof idea: Pass from semialgebra pieces to finite disjoint unions, then use approximation and countable additivity to extend.

- Exam use: Explains why specifying probabilities on intervals or rectangles is enough in many probability models.

- Pitfall: Do not assume every finitely additive premeasure extends; the countable condition is the serious part.

- Tags: semialgebra, extension, premeasure

##### Multidimensional distribution functions

- ID: `durrett_ch1_product_distribution_function`

- Section: 1.1 Probability Spaces

- Kind: theorem

- Summary: A function on R^d satisfying monotonicity over rectangles, right-continuity, and correct limits defines a probability measure on Borel R^d.

- Proof idea: Use rectangle increments and an extension theorem from a semialgebra of rectangles.

- Exam use: This underlies joint distributions and later independence statements.

- Pitfall: Coordinatewise monotonicity alone is not enough; rectangle probabilities must be nonnegative.

- Tags: joint-distribution, rectangles, borel-rd

##### Distribution function properties

- ID: `durrett_ch1_distribution_function`

- Section: 1.2 Distributions

- Kind: theorem

- Summary: A CDF is nondecreasing, right-continuous, tends to 0 at -infinity, and tends to 1 at +infinity.

- Proof idea: Monotonicity follows from event inclusion; right-continuity follows from continuity of probability for decreasing events.

- Exam use: Use these properties to test whether a proposed function can be a CDF.

- Pitfall: Left-continuity is generally false; jumps represent atoms.

- Tags: cdf, distribution, right-continuity

##### Every valid CDF determines a law

- ID: `durrett_ch1_cdf_to_law`

- Section: 1.2 Distributions

- Kind: theorem

- Summary: Any function with the standard CDF properties is the distribution function of a unique probability measure on R.

- Proof idea: Construct a Stieltjes measure and check that its half-line values match the function.

- Exam use: Lets you prove convergence claims by identifying limiting CDFs, provided the limit is a valid CDF at continuity points.

- Pitfall: A pointwise limit of CDFs may fail to be a CDF if total mass escapes to infinity.

- Tags: cdf, law, tightness

##### Atoms are jumps of the CDF

- ID: `durrett_ch1_atoms_jumps`

- Section: 1.2 Distributions

- Kind: fact

- Summary: For a real random variable, P(X = x) equals the jump F(x) - F(x-) of its distribution function.

- Proof idea: Compare events {X <= x} and {X < x}; use monotone convergence from below for F(x-).

- Exam use: Useful for mixed discrete-continuous examples and for proving a CDF has at most countably many discontinuities.

- Pitfall: A continuous CDF does not imply a density exists; the Cantor distribution is the standard warning.

- Tags: atom, cdf-jump, discontinuity

##### Standard normal tail estimate

- ID: `durrett_ch1_normal_tail_bound`

- Section: 1.2 Distributions

- Kind: inequality

- Summary: The standard normal upper tail has exponential decay comparable to phi(x)/x for positive x.

- Proof idea: Integrate the normal density and compare using monotonicity or one integration-by-parts style bound.

- Exam use: Appears in Brownian motion, LIL-style bounds, and CLT error estimates.

- Pitfall: Keep track of whether a bound is one-sided or two-sided; prelim solutions often lose constants harmlessly but not exponents.

- Tags: normal, tail-bound, inequality

##### Probability integral transform

- ID: `durrett_ch1_probability_integral_transform`

- Section: 1.2 Distributions

- Kind: fact

- Summary: If X has a continuous CDF F, then F(X) is uniform on (0,1) under suitable strictness/continuity conditions.

- Proof idea: Compute P(F(X) <= u) by translating through quantiles; handle flat parts carefully.

- Exam use: Useful for constructing random variables from uniform variables and for distribution transformations.

- Pitfall: Continuity alone needs care when F has flat intervals; use generalized inverses for the clean general statement.

- Tags: cdf-transform, uniform, quantile

##### Random variables as measurable maps

- ID: `durrett_ch1_measurable_map`

- Section: 1.3 Random Variables

- Kind: definition

- Summary: A random variable is a measurable map from the sample space to a measurable state space.

- Proof idea: Check inverse images of measurable target sets.

- Exam use: This is the language needed for sigma(X), conditional expectation, and stochastic processes.

- Pitfall: Do not confuse a random variable with its distribution; different variables may have the same law.

- Tags: random-variable, measurable-map, law

##### Checking measurability on generators

- ID: `durrett_ch1_measurability_generator`

- Section: 1.3 Random Variables

- Kind: theorem

- Summary: To prove X is measurable into a generated sigma-field, it is enough to check inverse images of a generating class.

- Proof idea: The inverse-image operation preserves complements and countable unions, so the checked class expands to a sigma-field.

- Exam use: Use half-lines for real variables and rectangles for vector-valued variables.

- Pitfall: The generator must actually generate the target sigma-field; checking too small a class proves too little.

- Tags: measurability, generator, inverse-image

##### Composition of measurable maps

- ID: `durrett_ch1_composition_measurable`

- Section: 1.3 Random Variables

- Kind: theorem

- Summary: If X is measurable and f is measurable, then f(X) is measurable.

- Proof idea: Inverse images compose: {f(X) in A} equals {X in f^{-1}(A)}.

- Exam use: Use this to justify transformations such as X^2, exp(X), indicators, vectors, sums, limsup, and liminf.

- Pitfall: Continuity is sufficient for Borel measurability, but not necessary.

- Tags: composition, transformation, measurable

##### Arithmetic of random variables

- ID: `durrett_ch1_measurable_arithmetic`

- Section: 1.3 Random Variables

- Kind: theorem

- Summary: Finite sums, products, maxima, minima, and continuous functions of random variables are random variables.

- Proof idea: View (X,Y) as a measurable vector and compose with continuous maps such as addition or multiplication.

- Exam use: Often needed before taking expectations of constructed quantities.

- Pitfall: Do not use arithmetic closure for extended real expressions without checking undefined forms like infinity minus infinity.

- Tags: arithmetic, measurable, random-variables

##### Limits preserve measurability

- ID: `durrett_ch1_limits_measurable`

- Section: 1.3 Random Variables

- Kind: theorem

- Summary: Supremum, infimum, limsup, liminf, and pointwise limits of measurable real functions are measurable.

- Proof idea: Express events such as {sup X_n <= a} or {limsup X_n < a} using countable unions/intersections of measurable events.

- Exam use: Crucial for defining almost sure convergence and stopping-time events.

- Pitfall: The countability of the sequence matters; arbitrary suprema over uncountable families can fail measurability.

- Tags: limsup, liminf, measurability, countability

##### Functions measurable with respect to sigma(X)

- ID: `durrett_ch1_sigma_x_factorization`

- Section: 1.3 Random Variables

- Kind: fact

- Summary: A random variable Y is sigma(X)-measurable exactly when it can be represented as a measurable function of X.

- Proof idea: Approximate Y by simple functions and show each sigma(X)-measurable indicator factors through X.

- Exam use: This is a foundation for conditional expectation as a function of observed information.

- Pitfall: The representing function is only determined up to the distribution of X, not necessarily pointwise everywhere.

- Tags: sigma-x, factorization, conditional-expectation

##### Simple functions

- ID: `durrett_ch1_simple_functions`

- Section: 1.4 Integration

- Kind: definition

- Summary: A simple function takes finitely many values and is the starting point for defining the Lebesgue integral.

- Proof idea: Define the integral as the sum of value times measure over level sets, then extend by monotone approximation.

- Exam use: When stuck on an integral proof, first prove it for indicators, then simple functions, then limits.

- Pitfall: Representations of a simple function are not unique; use canonical level sets to avoid ambiguity.

- Tags: simple-function, lebesgue-integral, proof-template

##### Integral of a nonnegative function

- ID: `durrett_ch1_nonnegative_integral`

- Section: 1.4 Integration

- Kind: definition

- Summary: The integral of a nonnegative measurable function is the supremum of integrals of simple functions bounded above by it.

- Proof idea: Approximate from below by simple functions and use monotone behavior.

- Exam use: This definition makes monotone convergence natural rather than surprising.

- Pitfall: The value may be infinite; do not subtract two infinite nonnegative integrals.

- Tags: nonnegative-integral, approximation, mct

##### Integrable signed functions

- ID: `durrett_ch1_integrable_function`

- Section: 1.4 Integration

- Kind: definition

- Summary: A signed measurable function is integrable when the integrals of its positive and negative parts are finite, equivalently the integral of its absolute value is finite.

- Proof idea: Define integral as integral of positive part minus integral of negative part.

- Exam use: Before using linearity or dominated convergence, check integrability conditions.

- Pitfall: Finite positive and negative parts are needed; infinity minus infinity is not an acceptable value.

- Tags: integrability, positive-part, negative-part

##### Linearity and order properties of the integral

- ID: `durrett_ch1_integral_linearity`

- Section: 1.4 Integration

- Kind: theorem

- Summary: For integrable functions, the integral is linear, monotone, and respects almost-everywhere equality.

- Proof idea: Prove first for simple functions, extend to nonnegative functions, then signed integrable functions.

- Exam use: Use to split expectations, compare nonnegative variables, and justify replacing variables by a.s. equal versions.

- Pitfall: Linearity can fail as a finite statement if one side involves undefined infinities.

- Tags: linearity, monotonicity, almost-everywhere

##### Jensen's inequality for integrals

- ID: `durrett_ch1_jensen_integral`

- Section: 1.5 Properties of the Integral

- Kind: inequality

- Summary: For a convex function phi and a probability measure, phi(integral f) is at most integral phi(f), assuming the quantities are defined.

- Proof idea: Use a supporting line to the convex function at the mean.

- Exam use: Prelim workhorse for Lp comparisons, moment generating bounds, and conditional Jensen later.

- Pitfall: Convexity direction matters; strict equality often encodes almost sure constancy under strict convexity.

- Tags: jensen, convexity, inequality

##### Holder's inequality

- ID: `durrett_ch1_holder_integral`

- Section: 1.5 Properties of the Integral

- Kind: inequality

- Summary: If p and q are conjugate exponents, the integral of |fg| is bounded by the Lp norm of f times the Lq norm of g.

- Proof idea: Normalize the functions and apply Young's inequality; handle zero norms separately.

- Exam use: Used for moment interpolation, uniform integrability checks, and bounding expectations of products.

- Pitfall: Remember the endpoint cases need separate interpretation.

- Tags: holder, lp, inequality

##### Minkowski's inequality

- ID: `durrett_ch1_minkowski`

- Section: 1.5 Properties of the Integral

- Kind: inequality

- Summary: The Lp norm satisfies the triangle inequality for p at least 1.

- Proof idea: Apply Holder to |f+g|^p split as |f+g|^{p-1}|f| plus the analogous term for g.

- Exam use: Use to prove Lp spaces are normed and to control sums of random variables in Lp.

- Pitfall: For p below 1 this is not a norm inequality.

- Tags: minkowski, lp, triangle-inequality

##### Bounded convergence theorem

- ID: `durrett_ch1_bounded_convergence`

- Section: 1.5 Properties of the Integral

- Kind: theorem

- Summary: On a finite-measure space, uniformly bounded functions converging pointwise have integrals converging to the integral of the limit.

- Proof idea: Reduce to dominated convergence with a constant dominating function, or prove using finite measure and small exceptional sets.

- Exam use: Useful for probability spaces when random variables are uniformly bounded.

- Pitfall: Finite measure is essential; bounded pointwise convergence on an infinite measure space need not preserve integrals.

- Tags: bounded-convergence, finite-measure, limit

##### Fatou's lemma

- ID: `durrett_ch1_fatou_integral`

- Section: 1.5 Properties of the Integral

- Kind: theorem

- Summary: For nonnegative functions, the integral of the liminf is at most the liminf of the integrals.

- Proof idea: Let g_n be the infimum over the tail; g_n increases to the liminf and monotone convergence applies.

- Exam use: Use for lower semicontinuity of expectations and to prove integrability of a limit from bounded expectations.

- Pitfall: Fatou gives an inequality, not usually equality.

- Tags: fatou, liminf, nonnegative

##### Monotone convergence theorem

- ID: `durrett_ch1_monotone_convergence`

- Section: 1.5 Properties of the Integral

- Kind: theorem

- Summary: If nonnegative measurable functions increase pointwise to f, then their integrals increase to the integral of f.

- Proof idea: The lower approximation definition of the integral makes the result direct.

- Exam use: Use for exchanging sums and expectations of nonnegative random variables.

- Pitfall: The monotone direction and nonnegativity are not optional unless you shift or dominate carefully.

- Tags: mct, monotone-convergence, nonnegative

##### Dominated convergence theorem

- ID: `durrett_ch1_dominated_convergence`

- Section: 1.5 Properties of the Integral

- Kind: theorem

- Summary: If f_n converges pointwise a.e. to f and |f_n| is bounded by an integrable g, then integrals of f_n converge to the integral of f.

- Proof idea: Apply Fatou to g + f_n and g - f_n, or to |f_n - f| after a standard argument.

- Exam use: The main theorem for passing limits through expectations under a uniform integrable bound.

- Pitfall: Pointwise boundedness is not enough; the dominating function must be integrable and independent of n.

- Tags: dct, dominated-convergence, limit

##### Expected value as Lebesgue integral

- ID: `durrett_ch1_expectation_as_integral`

- Section: 1.6 Expected Value

- Kind: definition

- Summary: Expectation is the integral of a random variable with respect to the probability measure.

- Proof idea: All integral theorems transfer directly to expectations.

- Exam use: This unifies discrete sums, density integrals, and abstract random variables.

- Pitfall: An expectation can be undefined if positive and negative parts are both infinite.

- Tags: expectation, lebesgue-integral, random-variable

##### Linearity and monotonicity of expectation

- ID: `durrett_ch1_expectation_linearity`

- Section: 1.6 Expected Value

- Kind: theorem

- Summary: Expectation is linear for integrable random variables and monotone for ordered random variables.

- Proof idea: Apply integral linearity and monotonicity.

- Exam use: Use constantly in variance, covariance, martingale, and conditioning calculations.

- Pitfall: Linearity does not require independence; product factorization does.

- Tags: expectation, linearity, monotonicity

##### Markov and Chebyshev inequalities

- ID: `durrett_ch1_markov_chebyshev`

- Section: 1.6 Expected Value

- Kind: inequality

- Summary: Markov bounds the probability of a nonnegative variable exceeding a threshold by its expectation over the threshold; Chebyshev applies this to powers or centered moments.

- Proof idea: Use the indicator inequality a 1_{X >= a} <= X for Markov, then specialize with nonnegative functions.

- Exam use: Core tool for convergence in probability, LLN proofs, and variance bounds.

- Pitfall: Check nonnegativity and choose the right moment; a weak moment gives a weak tail bound.

- Tags: markov-inequality, chebyshev, tail-bound

##### Limit theorems for expectation

- ID: `durrett_ch1_expectation_limit_theorems`

- Section: 1.6 Expected Value

- Kind: theorem-card

- Summary: Fatou, monotone convergence, dominated convergence, and bounded convergence all have expectation versions.

- Proof idea: Translate each integral theorem to the probability space.

- Exam use: A prelim proof often hinges on naming exactly the right convergence theorem and verifying its hypotheses.

- Pitfall: Do not cite dominated convergence when you only have bounded expectations; that is a uniform integrability issue, not automatic domination.

- Tags: expectation, fatou, mct, dct

##### Change of variables formula

- ID: `durrett_ch1_change_of_variables`

- Section: 1.6 Expected Value

- Kind: theorem

- Summary: If X has law mu and f is measurable, then E[f(X)] equals the integral of f with respect to mu, when the positive or integrable conditions hold.

- Proof idea: Prove for indicators, extend to simple functions, nonnegative functions, and signed integrable functions.

- Exam use: Lets you compute expectations using the distribution rather than the underlying sample space.

- Pitfall: Do not assume a density exists; the law may be discrete, continuous, singular, or mixed.

- Tags: change-of-variables, law, expectation

##### Tail integral and nonnegative expectations

- ID: `durrett_ch1_tail_sum_nonnegative`

- Section: 1.6 Expected Value

- Kind: formula

- Summary: For nonnegative random variables, expectations can often be computed or bounded through tail probabilities.

- Proof idea: Write X as an integral of indicators {X > t} and apply Fubini/Tonelli.

- Exam use: Important for moment bounds, heavy-tail examples, and Borel-Cantelli estimates.

- Pitfall: Mind strict versus non-strict inequalities only at atoms; the integral is unaffected in many continuous-parameter formulas.

- Tags: tail-integral, nonnegative, fubini

##### Common expectation computations

- ID: `durrett_ch1_common_distributions_expectations`

- Section: 1.6 Expected Value

- Kind: example-bank

- Summary: Chapter 1 reviews expectations for exponential, normal, Bernoulli, Poisson, and geometric distributions.

- Proof idea: Use densities or mass functions plus the change-of-variables formula; use series identities for discrete distributions.

- Exam use: These examples are quick diagnostic checks for later characteristic-function and limit problems.

- Pitfall: Parameterization varies, especially for geometric distributions; state your convention.

- Tags: common-distributions, expectation, examples

##### Inclusion-exclusion and Bonferroni

- ID: `durrett_ch1_inclusion_exclusion`

- Section: 1.6 Expected Value

- Kind: formula

- Summary: The probability of a finite union can be expanded by alternating sums of intersection probabilities, with Bonferroni inequalities for truncations.

- Proof idea: Apply expectation to sums/products of indicator variables.

- Exam use: Useful for event-counting, occupancy-style estimates, and bounding union probabilities more sharply than the union bound.

- Pitfall: The exact formula is finite; infinite versions require additional limiting arguments.

- Tags: inclusion-exclusion, bonferroni, indicators

##### Product measures

- ID: `durrett_ch1_product_measure`

- Section: 1.7 Product Measures, Fubini's Theorem

- Kind: definition

- Summary: Given measure spaces, the product measure is the unique measure on the product sigma-field that agrees with products of measures on measurable rectangles.

- Proof idea: Define on rectangles, verify premeasure properties, and extend.

- Exam use: The measure-theoretic basis for joint distributions and independence.

- Pitfall: A set in the product sigma-field can be much more complicated than a rectangle.

- Tags: product-measure, rectangles, joint-law

##### Measurable sections

- ID: `durrett_ch1_sections_measurable`

- Section: 1.7 Product Measures, Fubini's Theorem

- Kind: lemma

- Summary: For a measurable set in a product space, its x-section is measurable in the second space, and section measures are measurable functions of x.

- Proof idea: Prove first for rectangles, then close the class under monotone operations.

- Exam use: This is the technical engine behind Fubini and Tonelli.

- Pitfall: Do not assume section results for nonmeasurable product subsets.

- Tags: sections, product-space, measurability

##### Fubini and Tonelli theorem

- ID: `durrett_ch1_fubini_tonelli`

- Section: 1.7 Product Measures, Fubini's Theorem

- Kind: theorem

- Summary: For nonnegative functions, iterated integrals and the product integral agree. For signed functions, the same holds when the absolute integral is finite.

- Proof idea: Prove by indicators, simple functions, monotone convergence, then signed decomposition under integrability.

- Exam use: Use to exchange sums/integrals/expectations and compute expectations by conditioning-like iterated integration.

- Pitfall: Tonelli handles nonnegative functions even with infinite value; Fubini for signed functions needs integrability.

- Tags: fubini, tonelli, iterated-integral

##### Product measures as preview of independence

- ID: `durrett_ch1_independence_preview`

- Section: 1.7 Product Measures, Fubini's Theorem

- Kind: concept-link

- Summary: When a joint law factors as a product measure, the coordinates behave independently.

- Proof idea: Rectangular probabilities factor, and extension carries this to generated sigma-fields.

- Exam use: This prepares for Chapter 2 independence and for computing expectations of products.

- Pitfall: Independence is a statement about the joint law, not merely about marginal distributions.

- Tags: product-law, independence, joint-distribution

##### Countable/co-countable probability measure

- ID: `exercise_method_countable_cocountable_measure`

- Section: 1.1 Exercises: Probability spaces, sigma-fields, generators, and set algebras

- Kind: exercise-pattern

- Summary: To verify the countable/co-countable construction, split disjoint families into the cases where all sets are countable or exactly one set is co-countable.

- Proof idea: Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

- Exam use: Exercise 1.1.1 and any probability-space verification on unusual sigma-fields.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: probability-space, countable-additivity, co-countable

- Source exercises: 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5

##### Borel sigma-field from half-open rectangles

- ID: `exercise_method_borel_generated_by_half_open_rectangles`

- Section: 1.1 Exercises: Probability spaces, sigma-fields, generators, and set algebras

- Kind: exercise-pattern

- Summary: Show half-open rectangles are Borel, then express rational open rectangles as countable unions of half-open rectangles; use the countable rational base.

- Proof idea: Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

- Exam use: Exercises 1.1.2 and 1.1.3; product-measure generation arguments.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: borel, generator, rectangles

- Source exercises: 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5

##### Increasing union of sigma-fields can fail countable closure

- ID: `exercise_method_increasing_sigma_fields_not_sigma_field`

- Section: 1.1 Exercises: Probability spaces, sigma-fields, generators, and set algebras

- Kind: counterexample-template

- Summary: Use finite initial-coordinate sigma-fields on N; their union contains every finite set but misses an infinite non-cofinite set such as the evens.

- Proof idea: Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

- Exam use: Exercise 1.1.4; distinguishing algebras from sigma-fields.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: sigma-field, algebra, counterexample

- Source exercises: 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5

##### Block construction for asymptotic density counterexamples

- ID: `exercise_method_asymptotic_density_block_counterexample`

- Section: 1.1 Exercises: Probability spaces, sigma-fields, generators, and set algebras

- Kind: counterexample-template

- Summary: Use rapidly growing blocks so the latest block dominates all previous blocks; alternate behavior by blocks to destroy the density of intersections.

- Proof idea: Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

- Exam use: Exercise 1.1.5 and density/limit counterexamples.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: asymptotic-density, counterexample, blocks

- Source exercises: 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5

##### Piecewise random variable measurability

- ID: `exercise_method_piecewise_random_variable_measurability`

- Section: 1.2 Exercises: Distributions, normal tails, transformations, and density calculations

- Kind: proof-template

- Summary: For Z = X on A and Y on A^c, write {Z <= x} as (A cap {X <= x}) union (A^c cap {Y <= x}).

- Proof idea: Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

- Exam use: Exercise 1.2.1; patching random variables on measurable events.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: measurability, piecewise, random-variable

- Source exercises: 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7

##### Countability of CDF jumps

- ID: `exercise_method_countable_cdf_discontinuities`

- Section: 1.2 Exercises: Distributions, normal tails, transformations, and density calculations

- Kind: proof-template

- Summary: Group jumps by size bigger than 1/m inside bounded intervals; each group is finite because total CDF increase is at most one.

- Proof idea: Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

- Exam use: Exercise 1.2.3; monotone-function discontinuity arguments.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: cdf, jumps, countability

- Source exercises: 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7

##### Monotone density change of variables

- ID: `exercise_method_density_change_of_variables`

- Section: 1.2 Exercises: Distributions, normal tails, transformations, and density calculations

- Kind: calculation-template

- Summary: For Y=g(X) with g increasing, compute F_Y(y)=P(X <= g^{-1}(y)) and differentiate to get f_X(g^{-1}(y))/g'(g^{-1}(y)).

- Proof idea: Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

- Exam use: Exercises 1.2.5 and 1.2.6; lognormal and affine density transforms.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: density, change-of-variables, cdf

- Source exercises: 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7

##### Density of a square transform

- ID: `exercise_method_square_transform_density`

- Section: 1.2 Exercises: Distributions, normal tails, transformations, and density calculations

- Kind: calculation-template

- Summary: For Y=X^2, use F_Y(y)=P(-sqrt(y)<=X<=sqrt(y)) and differentiate to get [f(sqrt(y))+f(-sqrt(y))]/(2sqrt(y)).

- Proof idea: Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

- Exam use: Exercise 1.2.7; chi-square with one degree of freedom.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: density, chi-square, transformation

- Source exercises: 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7

##### Rational cut proof for sum measurability

- ID: `exercise_method_rational_cut_sum_measurability`

- Section: 1.3 Exercises: Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- Kind: proof-template

- Summary: Write {X+Y<x} as the countable union over q in Q of {X<q} cap {Y<x-q}.

- Proof idea: Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

- Exam use: Exercise 1.3.2; direct measurability of sums.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: measurability, rationals, sum

- Source exercises: 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.3.5, 1.3.6, 1.3.7, 1.3.8, 1.3.9

##### Lower semicontinuity via closed sublevel sets

- ID: `exercise_method_closed_sublevel_semicontinuity`

- Section: 1.3 Exercises: Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- Kind: proof-template

- Summary: A function is lower semicontinuous iff all sets {f <= a} are closed; sequential closure proves one direction and contradiction via subsequences proves the other.

- Proof idea: Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

- Exam use: Exercise 1.3.5; proving semicontinuous functions are measurable.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: semicontinuity, closed-sets, measurability

- Source exercises: 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.3.5, 1.3.6, 1.3.7, 1.3.8, 1.3.9

##### Discontinuity set from upper and lower local envelopes

- ID: `exercise_method_oscillation_discontinuity_set`

- Section: 1.3 Exercises: Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- Kind: proof-template

- Summary: Define local sup and inf over balls, take limits as radius decreases, and identify discontinuities as the set where the limiting envelopes differ.

- Proof idea: Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

- Exam use: Exercise 1.3.6; measurability of discontinuity sets.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: discontinuity, oscillation, measurability

- Source exercises: 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.3.5, 1.3.6, 1.3.7, 1.3.8, 1.3.9

##### Constructive representation of sigma(X)-measurable functions

- ID: `exercise_method_constructive_sigma_x_representation`

- Section: 1.3 Exercises: Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- Kind: proof-template

- Summary: Quantize Y into dyadic bins, represent each bin as {X in B}, build Borel simple functions f_n, then take a measurable pointwise limit f with Y=f(X).

- Proof idea: Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

- Exam use: Exercises 1.3.8 and 1.3.9; conditional-expectation foundations.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: sigma-x, factorization, dyadic-approximation

- Source exercises: 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.3.5, 1.3.6, 1.3.7, 1.3.8, 1.3.9

##### Zero integral of nonnegative function implies zero a.e.

- ID: `exercise_method_zero_integral_nonnegative`

- Section: 1.4 Exercises: Lebesgue integration construction and approximation

- Kind: proof-template

- Summary: Use sets {f > 1/n}; each has zero measure because integral dominates (1/n) times its measure, and their union is {f>0}.

- Proof idea: Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

- Exam use: Exercise 1.4.1; null-set proofs.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: nonnegative, zero-integral, a-e

- Source exercises: 1.4.1, 1.4.2, 1.4.3, 1.4.4

##### Dyadic lower simple approximations

- ID: `exercise_method_dyadic_lower_integral_approximation`

- Section: 1.4 Exercises: Lebesgue integration construction and approximation

- Kind: calculation-template

- Summary: Approximate f>=0 by 2^{-n} floor(2^n f); the approximants increase to f and their integrals give monotone sums over dyadic level sets.

- Proof idea: Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

- Exam use: Exercise 1.4.2 and simple-function approximation.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: dyadic, simple-functions, mct

- Source exercises: 1.4.1, 1.4.2, 1.4.3, 1.4.4

##### L1 approximation by continuous functions

- ID: `exercise_method_l1_continuous_approximation`

- Section: 1.4 Exercises: Lebesgue integration construction and approximation

- Kind: proof-template

- Summary: Approximate an integrable function by simple functions, approximate measurable sets by finite interval unions, then round step-function corners.

- Proof idea: Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

- Exam use: Exercise 1.4.3; density of nice functions in L1 on R.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: l1, approximation, continuous-functions

- Source exercises: 1.4.1, 1.4.2, 1.4.3, 1.4.4

##### Riemann-Lebesgue by step-function reduction

- ID: `exercise_method_riemann_lebesgue_step_reduction`

- Section: 1.4 Exercises: Lebesgue integration construction and approximation

- Kind: proof-template

- Summary: Prove oscillatory integral decay for interval indicators explicitly, then approximate any L1 function by a step function.

- Proof idea: Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

- Exam use: Exercise 1.4.4; oscillatory integral estimates.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: riemann-lebesgue, step-functions, oscillation

- Source exercises: 1.4.1, 1.4.2, 1.4.3, 1.4.4

##### Essential supremum bounds integrals

- ID: `exercise_method_essential_supremum_bound`

- Section: 1.5 Exercises: Lp inequalities, convergence theorems, and absolute continuity of the integral

- Kind: proof-template

- Summary: If |g| <= ||g||_infty a.e., then |fg| <= ||g||_infty |f| and integration gives the L1-Linfty Holder endpoint.

- Proof idea: Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

- Exam use: Exercise 1.5.1; endpoint Holder inequalities.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: essential-supremum, holder, linfty

- Source exercises: 1.5.1, 1.5.10, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6, 1.5.7, 1.5.8, 1.5.9

##### Lp norms converge to Linfty on probability spaces

- ID: `exercise_method_lp_to_l_infty_limit`

- Section: 1.5 Exercises: Lp inequalities, convergence theorems, and absolute continuity of the integral

- Kind: proof-template

- Summary: Upper bound by essential supremum; lower bound using sets where |f| exceeds M-epsilon and their positive probability.

- Proof idea: Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

- Exam use: Exercise 1.5.2; norm comparisons.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: lp, linfty, probability-space

- Source exercises: 1.5.1, 1.5.10, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6, 1.5.7, 1.5.8, 1.5.9

##### Simple functions are dense in Lp

- ID: `exercise_method_density_of_simple_functions_in_lp`

- Section: 1.5 Exercises: Lp inequalities, convergence theorems, and absolute continuity of the integral

- Kind: proof-template

- Summary: Use pointwise simple approximations bounded by |f|, then dominated convergence on |phi_n-f|^p.

- Proof idea: Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

- Exam use: Exercise 1.5.9; Lp approximation.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: lp, simple-functions, dct

- Source exercises: 1.5.1, 1.5.10, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6, 1.5.7, 1.5.8, 1.5.9

##### Exchange integral and absolutely summable series

- ID: `exercise_method_absolute_summability_exchange`

- Section: 1.5 Exercises: Lp inequalities, convergence theorems, and absolute continuity of the integral

- Kind: proof-template

- Summary: If sum integral |f_n| is finite, then H=sum |f_n| is integrable; dominated convergence applies to partial sums.

- Proof idea: Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

- Exam use: Exercise 1.5.10 and 1.7.1 corollary.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: series, dct, absolute-convergence

- Source exercises: 1.5.1, 1.5.10, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6, 1.5.7, 1.5.8, 1.5.9

##### Equality case in strict Jensen

- ID: `exercise_method_strict_jensen_equality`

- Section: 1.6 Exercises: Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Kind: proof-template

- Summary: For strictly convex phi, equality in Jensen forces the random variable to be almost surely constant at its mean.

- Proof idea: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Exam use: Exercise 1.6.1; strict convexity equality cases.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: jensen, strict-convexity, equality-case

- Source exercises: 1.6.1, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15, 1.6.16, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9

##### Two-point distributions as Chebyshev extremizers

- ID: `exercise_method_two_point_extremizers`

- Section: 1.6 Exercises: Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Kind: counterexample-template

- Summary: To prove sharpness of moment/tail inequalities, place small mass at boundary points and the rest at a value chosen to match moments.

- Proof idea: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Exam use: Exercises 1.6.3, 1.6.4, and 1.6.5.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: chebyshev, sharpness, two-point

- Source exercises: 1.6.1, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15, 1.6.16, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9

##### Cauchy-Schwarz lower bound for positive probability

- ID: `exercise_method_paley_zygmund_basic`

- Section: 1.6 Exercises: Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Kind: inequality-template

- Summary: For Y>=0, Cauchy-Schwarz applied to Y*1_{Y>0} yields P(Y>0) >= (EY)^2/EY^2.

- Proof idea: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Exam use: Exercise 1.6.6; basic Paley-Zygmund-style estimates.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: cauchy-schwarz, lower-bound, paley-zygmund

- Source exercises: 1.6.1, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15, 1.6.16, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9

##### Tail truncation for expectation limits

- ID: `exercise_method_expectation_tail_truncation`

- Section: 1.6 Exercises: Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Kind: proof-template

- Summary: Control small or large tails by splitting the event and using continuity of probability plus elementary bounds on the integrand.

- Proof idea: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Exam use: Exercise 1.6.14; limits involving y E(1/X; X>y).

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: tail, truncation, expectation

- Source exercises: 1.6.1, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15, 1.6.16, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9

##### Indicator expansion for inclusion-exclusion and Bonferroni

- ID: `exercise_method_inclusion_exclusion_indicators`

- Section: 1.6 Exercises: Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Kind: proof-template

- Summary: Use 1_union = 1 - product_i(1-1_Ai), expand, and take expectations; partial alternating sums give Bonferroni bounds.

- Proof idea: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Exam use: Exercises 1.6.9 and 1.6.10.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: inclusion-exclusion, bonferroni, indicators

- Source exercises: 1.6.1, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15, 1.6.16, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9

##### Layer-cake formula via product sets

- ID: `exercise_method_layer_cake_formula`

- Section: 1.7 Exercises: Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- Kind: proof-template

- Summary: Represent g(x) as the vertical length of {(x,y):0 <= y < g(x)} and apply Tonelli to integrate sections.

- Proof idea: Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

- Exam use: Exercise 1.7.2; tail integrals for nonnegative functions.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: layer-cake, tonelli, tail-integral

- Source exercises: 1.7.1, 1.7.2, 1.7.3, 1.7.4, 1.7.5

##### Stieltjes integration by parts with jump correction

- ID: `exercise_method_stieltjes_integration_by_parts_with_jumps`

- Section: 1.7 Exercises: Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- Kind: proof-template

- Summary: Interpret Stieltjes integrals as product-measure masses of order regions; the diagonal overlap contributes the product of jump masses.

- Proof idea: Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

- Exam use: Exercise 1.7.3.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: stieltjes, integration-by-parts, jumps

- Source exercises: 1.7.1, 1.7.2, 1.7.3, 1.7.4, 1.7.5

##### Sliding interval Fubini identity

- ID: `exercise_method_interval_sliding_fubini`

- Section: 1.7 Exercises: Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- Kind: calculation-template

- Summary: Write F(x+c)-F(x) as mu((x,x+c]), swap integrals, and observe each fixed t is counted for exactly c units of x.

- Proof idea: Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

- Exam use: Exercise 1.7.4.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: fubini, distribution-function, sliding-window

- Source exercises: 1.7.1, 1.7.2, 1.7.3, 1.7.4, 1.7.5

##### Sine integral via Fubini

- ID: `exercise_method_sine_integral_fubini`

- Section: 1.7 Exercises: Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- Kind: calculation-template

- Summary: Represent sin(x)/x as an integral of e^{-xy} sin(x), integrate in x first, and bound the remaining exponentially damped tails.

- Proof idea: Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

- Exam use: Exercise 1.7.5.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: fubini, sine-integral, oscillatory-integral

- Source exercises: 1.7.1, 1.7.2, 1.7.3, 1.7.4, 1.7.5

#### Exercise Method Cards

##### 1.1 Probability spaces, sigma-fields, generators, and set algebras

- ID: `durrett_ch1_section_1_1_method_card`

- Method: Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

- Tags: sigma-field, generator, set-counterexample, measure-foundations

- New knowledge IDs: exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample

##### 1.2 Distributions, normal tails, transformations, and density calculations

- ID: `durrett_ch1_section_1_2_method_card`

- Method: Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

- Tags: cdf, density-transform, normal-tail, probability-integral-transform

- New knowledge IDs: exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density

##### 1.3 Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- ID: `durrett_ch1_section_1_3_method_card`

- Method: Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

- Tags: measurability, generators, semicontinuity, sigma-x-factorization

- New knowledge IDs: exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation

##### 1.4 Lebesgue integration construction and approximation

- ID: `durrett_ch1_section_1_4_method_card`

- Method: Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

- Tags: lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue

- New knowledge IDs: exercise_method_zero_integral_nonnegative, exercise_method_dyadic_lower_integral_approximation, exercise_method_l1_continuous_approximation, exercise_method_riemann_lebesgue_step_reduction

##### 1.5 Lp inequalities, convergence theorems, and absolute continuity of the integral

- ID: `durrett_ch1_section_1_5_method_card`

- Method: Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

- Tags: lp, holder, minkowski, mct, dct, absolute-continuity

- New knowledge IDs: exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange

##### 1.6 Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- ID: `durrett_ch1_section_1_6_method_card`

- Method: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Tags: expectation, jensen, chebyshev, moment-bound, mct, dct

- New knowledge IDs: exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators

##### 1.7 Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- ID: `durrett_ch1_section_1_7_method_card`

- Method: Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

- Tags: fubini, tonelli, product-measure, layer-cake, stieltjes

- New knowledge IDs: exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini

#### Exercise Record Index

##### 1.1 Probability spaces, sigma-fields, generators, and set algebras

- Exercise 1.1.1: method tags `sigma-field, generator, set-counterexample, measure-foundations`; knowledge used `durrett_ch1_probability_space, durrett_ch1_sigma_field, durrett_ch1_measure_continuity`; new knowledge `exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample`.
- Exercise 1.1.2: method tags `sigma-field, generator, set-counterexample, measure-foundations`; knowledge used `durrett_ch1_sigma_field, durrett_ch1_semialgebra_extension, durrett_ch1_product_distribution_function`; new knowledge `exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample`.
- Exercise 1.1.3: method tags `sigma-field, generator, set-counterexample, measure-foundations`; knowledge used `durrett_ch1_sigma_field, durrett_ch1_semialgebra_extension, durrett_ch1_product_distribution_function`; new knowledge `exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample`.
- Exercise 1.1.4: method tags `sigma-field, generator, set-counterexample, measure-foundations`; knowledge used `durrett_ch1_sigma_field`; new knowledge `exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample`.
- Exercise 1.1.5: method tags `sigma-field, generator, set-counterexample, measure-foundations`; knowledge used `durrett_ch1_sigma_field, durrett_ch1_measure_continuity`; new knowledge `exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample`.

##### 1.2 Distributions, normal tails, transformations, and density calculations

- Exercise 1.2.1: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_measurable_map, durrett_ch1_measurability_generator, durrett_ch1_sigma_field`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.2: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_normal_tail_bound, durrett_ch1_distribution_function`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.3: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_distribution_function, durrett_ch1_atoms_jumps, durrett_ch1_measure_continuity`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.4: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_probability_integral_transform, durrett_ch1_distribution_function, durrett_ch1_cdf_to_law`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.5: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_change_of_variables, durrett_ch1_distribution_function, durrett_ch1_cdf_to_law`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.6: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_change_of_variables, durrett_ch1_common_distributions_expectations, durrett_ch1_distribution_function`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.7: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_change_of_variables, durrett_ch1_distribution_function, durrett_ch1_common_distributions_expectations`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.

##### 1.3 Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- Exercise 1.3.1: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_measurability_generator, durrett_ch1_sigma_field, durrett_ch1_measurable_map`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.2: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_measurable_arithmetic, durrett_ch1_measurability_generator, durrett_ch1_sigma_field`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.3: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_composition_measurable, durrett_ch1_limits_measurable`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.4: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_composition_measurable, durrett_ch1_measurability_generator, durrett_ch1_sigma_field`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.5: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_measurability_generator, durrett_ch1_limits_measurable, durrett_ch1_sigma_field`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.6: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_limits_measurable, durrett_ch1_measurability_generator, durrett_ch1_composition_measurable`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.7: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_simple_functions, durrett_ch1_limits_measurable, durrett_ch1_measurable_map`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.8: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_sigma_x_factorization, durrett_ch1_composition_measurable, durrett_ch1_simple_functions`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.9: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_sigma_x_factorization, durrett_ch1_measurability_generator, durrett_ch1_limits_measurable`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.

##### 1.4 Lebesgue integration construction and approximation

- Exercise 1.4.1: method tags `lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue`; knowledge used `durrett_ch1_nonnegative_integral, durrett_ch1_integral_linearity, durrett_ch1_measure_continuity`; new knowledge `exercise_method_zero_integral_nonnegative, exercise_method_dyadic_lower_integral_approximation, exercise_method_l1_continuous_approximation, exercise_method_riemann_lebesgue_step_reduction`.
- Exercise 1.4.2: method tags `lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue`; knowledge used `durrett_ch1_simple_functions, durrett_ch1_nonnegative_integral, durrett_ch1_monotone_convergence`; new knowledge `exercise_method_zero_integral_nonnegative, exercise_method_dyadic_lower_integral_approximation, exercise_method_l1_continuous_approximation, exercise_method_riemann_lebesgue_step_reduction`.
- Exercise 1.4.3: method tags `lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue`; knowledge used `durrett_ch1_integrable_function, durrett_ch1_simple_functions, durrett_ch1_integral_linearity`; new knowledge `exercise_method_zero_integral_nonnegative, exercise_method_dyadic_lower_integral_approximation, exercise_method_l1_continuous_approximation, exercise_method_riemann_lebesgue_step_reduction`.
- Exercise 1.4.4: method tags `lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue`; knowledge used `durrett_ch1_integrable_function, durrett_ch1_integral_linearity, durrett_ch1_dominated_convergence`; new knowledge `exercise_method_zero_integral_nonnegative, exercise_method_dyadic_lower_integral_approximation, exercise_method_l1_continuous_approximation, exercise_method_riemann_lebesgue_step_reduction`.

##### 1.5 Lp inequalities, convergence theorems, and absolute continuity of the integral

- Exercise 1.5.1: method tags `lp, holder, minkowski, mct, dct, absolute-continuity`; knowledge used `durrett_ch1_holder_integral, durrett_ch1_integrable_function, durrett_ch1_integral_linearity`; new knowledge `exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange`.
- Exercise 1.5.2: method tags `lp, holder, minkowski, mct, dct, absolute-continuity`; knowledge used `durrett_ch1_jensen_integral, durrett_ch1_holder_integral, durrett_ch1_monotone_convergence`; new knowledge `exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange`.
- Exercise 1.5.3: method tags `lp, holder, minkowski, mct, dct, absolute-continuity`; knowledge used `durrett_ch1_minkowski, durrett_ch1_holder_integral, durrett_ch1_integral_linearity`; new knowledge `exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange`.
- Exercise 1.5.4: method tags `lp, holder, minkowski, mct, dct, absolute-continuity`; knowledge used `durrett_ch1_integrable_function, durrett_ch1_integral_linearity, durrett_ch1_monotone_convergence`; new knowledge `exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange`.
- Exercise 1.5.5: method tags `lp, holder, minkowski, mct, dct, absolute-continuity`; knowledge used `durrett_ch1_monotone_convergence, durrett_ch1_integrable_function, durrett_ch1_integral_linearity`; new knowledge `exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange`.
- Exercise 1.5.6: method tags `lp, holder, minkowski, mct, dct, absolute-continuity`; knowledge used `durrett_ch1_monotone_convergence, durrett_ch1_nonnegative_integral, durrett_ch1_integral_linearity`; new knowledge `exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange`.
- Exercise 1.5.7: method tags `lp, holder, minkowski, mct, dct, absolute-continuity`; knowledge used `durrett_ch1_monotone_convergence, durrett_ch1_integrable_function, durrett_ch1_integral_linearity`; new knowledge `exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange`.
- Exercise 1.5.8: method tags `lp, holder, minkowski, mct, dct, absolute-continuity`; knowledge used `durrett_ch1_integrable_function, durrett_ch1_integral_linearity, durrett_ch1_dominated_convergence`; new knowledge `exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange`.
- Exercise 1.5.9: method tags `lp, holder, minkowski, mct, dct, absolute-continuity`; knowledge used `durrett_ch1_simple_functions, durrett_ch1_dominated_convergence, durrett_ch1_integrable_function`; new knowledge `exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange`.
- Exercise 1.5.10: method tags `lp, holder, minkowski, mct, dct, absolute-continuity`; knowledge used `durrett_ch1_dominated_convergence, durrett_ch1_monotone_convergence, durrett_ch1_integral_linearity`; new knowledge `exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange`.

##### 1.6 Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Exercise 1.6.1: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_jensen_integral, durrett_ch1_expectation_as_integral`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.2: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_jensen_integral, durrett_ch1_expectation_linearity`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.3: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_markov_chebyshev, durrett_ch1_expectation_limit_theorems`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.4: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_markov_chebyshev, durrett_ch1_expectation_linearity, durrett_ch1_common_distributions_expectations`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.5: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_common_distributions_expectations, durrett_ch1_markov_chebyshev`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.6: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_holder_integral, durrett_ch1_expectation_linearity`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.7: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_expectation_limit_theorems, durrett_ch1_dominated_convergence, durrett_ch1_common_distributions_expectations`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.8: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_change_of_variables, durrett_ch1_expectation_limit_theorems`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.9: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_inclusion_exclusion, durrett_ch1_expectation_linearity`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.10: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_inclusion_exclusion, durrett_ch1_expectation_linearity`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.11: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_jensen_integral, durrett_ch1_holder_integral`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.12: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_jensen_integral, durrett_ch1_common_distributions_expectations`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.13: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_expectation_limit_theorems, durrett_ch1_expectation_linearity`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.14: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_tail_sum_nonnegative, durrett_ch1_expectation_limit_theorems`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.15: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_expectation_limit_theorems, durrett_ch1_fubini_tonelli`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.
- Exercise 1.6.16: method tags `expectation, jensen, chebyshev, moment-bound, mct, dct`; knowledge used `durrett_ch1_expectation_as_integral, durrett_ch1_expectation_linearity, durrett_ch1_expectation_limit_theorems`; new knowledge `exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators`.

##### 1.7 Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- Exercise 1.7.1: method tags `fubini, tonelli, product-measure, layer-cake, stieltjes`; knowledge used `durrett_ch1_product_measure, durrett_ch1_fubini_tonelli, durrett_ch1_integrable_function`; new knowledge `exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini`.
- Exercise 1.7.2: method tags `fubini, tonelli, product-measure, layer-cake, stieltjes`; knowledge used `durrett_ch1_fubini_tonelli, durrett_ch1_sections_measurable, durrett_ch1_tail_sum_nonnegative`; new knowledge `exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini`.
- Exercise 1.7.3: method tags `fubini, tonelli, product-measure, layer-cake, stieltjes`; knowledge used `durrett_ch1_stieltjes_measure, durrett_ch1_product_measure, durrett_ch1_fubini_tonelli`; new knowledge `exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini`.
- Exercise 1.7.4: method tags `fubini, tonelli, product-measure, layer-cake, stieltjes`; knowledge used `durrett_ch1_stieltjes_measure, durrett_ch1_fubini_tonelli, durrett_ch1_integrable_function`; new knowledge `exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini`.
- Exercise 1.7.5: method tags `fubini, tonelli, product-measure, layer-cake, stieltjes`; knowledge used `durrett_ch1_fubini_tonelli, durrett_ch1_integrable_function, durrett_ch1_dominated_convergence`; new knowledge `exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini`.

### Chapter 1 Exercise Viki

#### Chapter 1 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter1/Chapter1Exercises.tex`
Source PDF: `Probability/Exercises/Chapter1/Chapter1Exercises.pdf`

This dataset turns the solved Chapter 1 exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.

##### Files

- `chapter1_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.
- `chapter1_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter1_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter1_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.
- `chapter1_exercise_viki.md`: human-readable overview.
- `manifest.json`: dataset metadata.

##### Section Method Cards

###### 1.1 - Probability spaces, sigma-fields, generators, and set algebras

Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

Tags: sigma-field, generator, set-counterexample, measure-foundations

###### 1.2 - Distributions, normal tails, transformations, and density calculations

Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

Tags: cdf, density-transform, normal-tail, probability-integral-transform

###### 1.3 - Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

Tags: measurability, generators, semicontinuity, sigma-x-factorization

###### 1.4 - Lebesgue integration construction and approximation

Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

Tags: lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue

###### 1.5 - Lp inequalities, convergence theorems, and absolute continuity of the integral

Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

Tags: lp, holder, minkowski, mct, dct, absolute-continuity

###### 1.6 - Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

Tags: expectation, jensen, chebyshev, moment-bound, mct, dct

###### 1.7 - Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

Tags: fubini, tonelli, product-measure, layer-cake, stieltjes

##### New Knowledge Pieces

###### Countable/co-countable probability measure

- ID: `exercise_method_countable_cocountable_measure`
- Kind: exercise-derived-method
- Summary: To verify the countable/co-countable construction, split disjoint families into the cases where all sets are countable or exactly one set is co-countable.
- Use case: Exercise 1.1.1 and any probability-space verification on unusual sigma-fields.
- Tags: probability-space, countable-additivity, co-countable

###### Borel sigma-field from half-open rectangles

- ID: `exercise_method_borel_generated_by_half_open_rectangles`
- Kind: exercise-derived-method
- Summary: Show half-open rectangles are Borel, then express rational open rectangles as countable unions of half-open rectangles; use the countable rational base.
- Use case: Exercises 1.1.2 and 1.1.3; product-measure generation arguments.
- Tags: borel, generator, rectangles

###### Increasing union of sigma-fields can fail countable closure

- ID: `exercise_method_increasing_sigma_fields_not_sigma_field`
- Kind: counterexample-template
- Summary: Use finite initial-coordinate sigma-fields on N; their union contains every finite set but misses an infinite non-cofinite set such as the evens.
- Use case: Exercise 1.1.4; distinguishing algebras from sigma-fields.
- Tags: sigma-field, algebra, counterexample

###### Block construction for asymptotic density counterexamples

- ID: `exercise_method_asymptotic_density_block_counterexample`
- Kind: counterexample-template
- Summary: Use rapidly growing blocks so the latest block dominates all previous blocks; alternate behavior by blocks to destroy the density of intersections.
- Use case: Exercise 1.1.5 and density/limit counterexamples.
- Tags: asymptotic-density, counterexample, blocks

###### Piecewise random variable measurability

- ID: `exercise_method_piecewise_random_variable_measurability`
- Kind: proof-template
- Summary: For Z = X on A and Y on A^c, write {Z <= x} as (A cap {X <= x}) union (A^c cap {Y <= x}).
- Use case: Exercise 1.2.1; patching random variables on measurable events.
- Tags: measurability, piecewise, random-variable

###### Countability of CDF jumps

- ID: `exercise_method_countable_cdf_discontinuities`
- Kind: proof-template
- Summary: Group jumps by size bigger than 1/m inside bounded intervals; each group is finite because total CDF increase is at most one.
- Use case: Exercise 1.2.3; monotone-function discontinuity arguments.
- Tags: cdf, jumps, countability

###### Monotone density change of variables

- ID: `exercise_method_density_change_of_variables`
- Kind: calculation-template
- Summary: For Y=g(X) with g increasing, compute F_Y(y)=P(X <= g^{-1}(y)) and differentiate to get f_X(g^{-1}(y))/g'(g^{-1}(y)).
- Use case: Exercises 1.2.5 and 1.2.6; lognormal and affine density transforms.
- Tags: density, change-of-variables, cdf

###### Density of a square transform

- ID: `exercise_method_square_transform_density`
- Kind: calculation-template
- Summary: For Y=X^2, use F_Y(y)=P(-sqrt(y)<=X<=sqrt(y)) and differentiate to get [f(sqrt(y))+f(-sqrt(y))]/(2sqrt(y)).
- Use case: Exercise 1.2.7; chi-square with one degree of freedom.
- Tags: density, chi-square, transformation

###### Rational cut proof for sum measurability

- ID: `exercise_method_rational_cut_sum_measurability`
- Kind: proof-template
- Summary: Write {X+Y<x} as the countable union over q in Q of {X<q} cap {Y<x-q}.
- Use case: Exercise 1.3.2; direct measurability of sums.
- Tags: measurability, rationals, sum

###### Lower semicontinuity via closed sublevel sets

- ID: `exercise_method_closed_sublevel_semicontinuity`
- Kind: proof-template
- Summary: A function is lower semicontinuous iff all sets {f <= a} are closed; sequential closure proves one direction and contradiction via subsequences proves the other.
- Use case: Exercise 1.3.5; proving semicontinuous functions are measurable.
- Tags: semicontinuity, closed-sets, measurability

###### Discontinuity set from upper and lower local envelopes

- ID: `exercise_method_oscillation_discontinuity_set`
- Kind: proof-template
- Summary: Define local sup and inf over balls, take limits as radius decreases, and identify discontinuities as the set where the limiting envelopes differ.
- Use case: Exercise 1.3.6; measurability of discontinuity sets.
- Tags: discontinuity, oscillation, measurability

###### Constructive representation of sigma(X)-measurable functions

- ID: `exercise_method_constructive_sigma_x_representation`
- Kind: proof-template
- Summary: Quantize Y into dyadic bins, represent each bin as {X in B}, build Borel simple functions f_n, then take a measurable pointwise limit f with Y=f(X).
- Use case: Exercises 1.3.8 and 1.3.9; conditional-expectation foundations.
- Tags: sigma-x, factorization, dyadic-approximation

###### Zero integral of nonnegative function implies zero a.e.

- ID: `exercise_method_zero_integral_nonnegative`
- Kind: proof-template
- Summary: Use sets {f > 1/n}; each has zero measure because integral dominates (1/n) times its measure, and their union is {f>0}.
- Use case: Exercise 1.4.1; null-set proofs.
- Tags: nonnegative, zero-integral, a-e

###### Dyadic lower simple approximations

- ID: `exercise_method_dyadic_lower_integral_approximation`
- Kind: calculation-template
- Summary: Approximate f>=0 by 2^{-n} floor(2^n f); the approximants increase to f and their integrals give monotone sums over dyadic level sets.
- Use case: Exercise 1.4.2 and simple-function approximation.
- Tags: dyadic, simple-functions, mct

###### L1 approximation by continuous functions

- ID: `exercise_method_l1_continuous_approximation`
- Kind: proof-template
- Summary: Approximate an integrable function by simple functions, approximate measurable sets by finite interval unions, then round step-function corners.
- Use case: Exercise 1.4.3; density of nice functions in L1 on R.
- Tags: l1, approximation, continuous-functions

###### Riemann-Lebesgue by step-function reduction

- ID: `exercise_method_riemann_lebesgue_step_reduction`
- Kind: proof-template
- Summary: Prove oscillatory integral decay for interval indicators explicitly, then approximate any L1 function by a step function.
- Use case: Exercise 1.4.4; oscillatory integral estimates.
- Tags: riemann-lebesgue, step-functions, oscillation

###### Essential supremum bounds integrals

- ID: `exercise_method_essential_supremum_bound`
- Kind: proof-template
- Summary: If |g| <= ||g||_infty a.e., then |fg| <= ||g||_infty |f| and integration gives the L1-Linfty Holder endpoint.
- Use case: Exercise 1.5.1; endpoint Holder inequalities.
- Tags: essential-supremum, holder, linfty

###### Lp norms converge to Linfty on probability spaces

- ID: `exercise_method_lp_to_l_infty_limit`
- Kind: proof-template
- Summary: Upper bound by essential supremum; lower bound using sets where |f| exceeds M-epsilon and their positive probability.
- Use case: Exercise 1.5.2; norm comparisons.
- Tags: lp, linfty, probability-space

###### Simple functions are dense in Lp

- ID: `exercise_method_density_of_simple_functions_in_lp`
- Kind: proof-template
- Summary: Use pointwise simple approximations bounded by |f|, then dominated convergence on |phi_n-f|^p.
- Use case: Exercise 1.5.9; Lp approximation.
- Tags: lp, simple-functions, dct

###### Exchange integral and absolutely summable series

- ID: `exercise_method_absolute_summability_exchange`
- Kind: proof-template
- Summary: If sum integral |f_n| is finite, then H=sum |f_n| is integrable; dominated convergence applies to partial sums.
- Use case: Exercise 1.5.10 and 1.7.1 corollary.
- Tags: series, dct, absolute-convergence

###### Equality case in strict Jensen

- ID: `exercise_method_strict_jensen_equality`
- Kind: proof-template
- Summary: For strictly convex phi, equality in Jensen forces the random variable to be almost surely constant at its mean.
- Use case: Exercise 1.6.1; strict convexity equality cases.
- Tags: jensen, strict-convexity, equality-case

###### Two-point distributions as Chebyshev extremizers

- ID: `exercise_method_two_point_extremizers`
- Kind: counterexample-template
- Summary: To prove sharpness of moment/tail inequalities, place small mass at boundary points and the rest at a value chosen to match moments.
- Use case: Exercises 1.6.3, 1.6.4, and 1.6.5.
- Tags: chebyshev, sharpness, two-point

###### Cauchy-Schwarz lower bound for positive probability

- ID: `exercise_method_paley_zygmund_basic`
- Kind: inequality-template
- Summary: For Y>=0, Cauchy-Schwarz applied to Y*1_{Y>0} yields P(Y>0) >= (EY)^2/EY^2.
- Use case: Exercise 1.6.6; basic Paley-Zygmund-style estimates.
- Tags: cauchy-schwarz, lower-bound, paley-zygmund

###### Tail truncation for expectation limits

- ID: `exercise_method_expectation_tail_truncation`
- Kind: proof-template
- Summary: Control small or large tails by splitting the event and using continuity of probability plus elementary bounds on the integrand.
- Use case: Exercise 1.6.14; limits involving y E(1/X; X>y).
- Tags: tail, truncation, expectation

###### Indicator expansion for inclusion-exclusion and Bonferroni

- ID: `exercise_method_inclusion_exclusion_indicators`
- Kind: proof-template
- Summary: Use 1_union = 1 - product_i(1-1_Ai), expand, and take expectations; partial alternating sums give Bonferroni bounds.
- Use case: Exercises 1.6.9 and 1.6.10.
- Tags: inclusion-exclusion, bonferroni, indicators

###### Layer-cake formula via product sets

- ID: `exercise_method_layer_cake_formula`
- Kind: proof-template
- Summary: Represent g(x) as the vertical length of {(x,y):0 <= y < g(x)} and apply Tonelli to integrate sections.
- Use case: Exercise 1.7.2; tail integrals for nonnegative functions.
- Tags: layer-cake, tonelli, tail-integral

###### Stieltjes integration by parts with jump correction

- ID: `exercise_method_stieltjes_integration_by_parts_with_jumps`
- Kind: proof-template
- Summary: Interpret Stieltjes integrals as product-measure masses of order regions; the diagonal overlap contributes the product of jump masses.
- Use case: Exercise 1.7.3.
- Tags: stieltjes, integration-by-parts, jumps

###### Sliding interval Fubini identity

- ID: `exercise_method_interval_sliding_fubini`
- Kind: calculation-template
- Summary: Write F(x+c)-F(x) as mu((x,x+c]), swap integrals, and observe each fixed t is counted for exactly c units of x.
- Use case: Exercise 1.7.4.
- Tags: fubini, distribution-function, sliding-window

###### Sine integral via Fubini

- ID: `exercise_method_sine_integral_fubini`
- Kind: calculation-template
- Summary: Represent sin(x)/x as an integral of e^{-xy} sin(x), integrate in x first, and bound the remaining exponentially damped tails.
- Use case: Exercise 1.7.5.
- Tags: fubini, sine-integral, oscillatory-integral

## Chapter 2

### Durrett Chapter 2 LLM Viki: Laws of Large Numbers

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter2.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

#### Section Guides

##### 2.1 Independence

- Goal: Move fluently between event, random-variable, sigma-field, product-law, and convolution formulations of independence.

- Must master: event independence, sigma-field independence, pi-lambda extension, product joint laws, convolution

- Prelim angle: Independence is the hidden engine behind LLN, Borel-Cantelli, random walks, and large-deviation calculations.

##### 2.2 Weak Laws of Large Numbers

- Goal: Prove convergence in probability of averages using Chebyshev, triangular arrays, and truncation.

- Must master: L2 WLLN, iid finite-mean WLLN, triangular arrays, truncation, tail-sum identities, moving centering

- Prelim angle: High-frequency source of proof problems where the key is choosing the right normalization and moment/tail condition.

##### 2.3 Borel-Cantelli Lemmas

- Goal: Convert summability or independence of events into almost sure eventual or infinitely-often statements.

- Must master: limsup events, first Borel-Cantelli, second Borel-Cantelli, Kochen-Stone, convergence in probability metric, maxima criteria

- Prelim angle: Often appears as the final almost-sure step after Markov/Chebyshev/exponential estimates.

##### 2.4 Strong Law of Large Numbers

- Goal: Understand how maximal inequalities, truncation, and Borel-Cantelli upgrade weak averaging to almost sure averaging.

- Must master: Kolmogorov maximal inequality, variance convergence criterion, iid finite-mean SLLN, renewal reward ratios, log-growth optimization

- Prelim angle: A central theorem and proof template; exams often ask for variants rather than the exact theorem.

##### 2.5 Convergence of Random Series

- Goal: Diagnose almost sure convergence of independent random series by separating jumps, drift, and centered fluctuations.

- Must master: three-series theorem, large jumps, truncated means, summable variances, Levy maximal inequality, random power-series radius

- Prelim angle: Useful for series examples, convergence-in-probability upgrades, and recognizing why finite-mean assumptions matter.

##### 2.6 Renewal Theory

- Goal: Use LLN ideas in counting processes and solve renewal equations for long-run limits.

- Must master: renewal process, elementary renewal theorem, renewal equation, key renewal theorem, age and residual life, alternating renewal

- Prelim angle: Important for applied long-run rates, waiting-time distributions, availability, and renewal density limits.

##### 2.7 Large Deviations

- Goal: Compute exponential decay rates for sums using moment generating functions, Chernoff bounds, and tilting.

- Must master: superadditivity, concavity of gamma, Chernoff bound, exponential tilting, Cramer rate formula, one big jump lower bounds

- Prelim angle: Gives sharp tail exponents and contrasts light-tailed Cramer behavior with heavy-tailed subexponential behavior.

#### Knowledge Pieces

##### Independence of events

- ID: `durrett_ch2_event_independence`

- Section: 2.1 Independence

- Kind: definition

- Summary: Events A and B are independent when P(A intersect B) = P(A)P(B); finite families require the product formula for every subfamily.

- Proof idea: The definition is designed so multiplication of probabilities replaces intersection probabilities.

- Exam use: Use it as the base language for indicator arguments, Borel-Cantelli, and pairwise-versus-mutual independence examples.

- Pitfall: Pairwise independence does not imply mutual independence; always check all finite subcollections when the statement says independent.

- Tags: independence, events, pairwise-vs-mutual

##### Random variables and sigma-field independence

- ID: `durrett_ch2_rv_sigma_independence`

- Section: 2.1 Independence

- Kind: theorem

- Summary: Random variables are independent exactly when their generated sigma-fields are independent; measurable variables inside independent sigma-fields are independent.

- Proof idea: Translate events about X and Y into sets in sigma(X) and sigma(Y), then apply the definition of sigma-field independence.

- Exam use: Lets you move cleanly between event, random-variable, and information-field formulations.

- Pitfall: Do not confuse uncorrelated with independent; zero covariance is far weaker.

- Tags: independence, sigma-field, random-variables

##### Indicators encode event independence

- ID: `durrett_ch2_indicator_independence`

- Section: 2.1 Independence

- Kind: fact

- Summary: Events A and B are independent if and only if their indicators 1_A and 1_B are independent random variables.

- Proof idea: The indicators take only values 0 and 1, so checking their joint probabilities reduces to A, B, and complements.

- Exam use: Useful when converting event problems into expectation or covariance calculations.

- Pitfall: Independence of indicators is stronger than merely E[1_A 1_B] being computable; it is equivalent here because the variables are binary.

- Tags: indicators, events, independence

##### Pi-lambda independence extension

- ID: `durrett_ch2_pi_lambda_independence`

- Section: 2.1.1 Sufficient Conditions for Independence

- Kind: proof-template

- Summary: If independent collections are pi-systems, then the sigma-fields they generate are independent.

- Proof idea: Fix all but one coordinate and show the class of sets preserving the product formula is a lambda-system; apply the pi-lambda theorem repeatedly.

- Exam use: High-value proof method for showing independence from checking rectangles, half-lines, or finite-dimensional cylinder sets.

- Pitfall: The checked classes must be pi-systems and must generate the desired sigma-fields.

- Tags: pi-lambda, generators, independence

##### Independence of blocks

- ID: `durrett_ch2_independent_blocks`

- Section: 2.1.1 Sufficient Conditions for Independence

- Kind: theorem

- Summary: Disjoint blocks built from independent families are independent after taking generated sigma-fields.

- Proof idea: Group variables into sigma-fields generated by each block and use the independence extension theorem.

- Exam use: Use this to show X_1 is independent of functions of X_2,...,X_n, or that future increments are independent of past events.

- Pitfall: The blocks must be formed from disjoint subfamilies of an independent family.

- Tags: blocks, sigma-fields, independent-families

##### Functions of independent blocks

- ID: `durrett_ch2_functions_of_independent_blocks`

- Section: 2.1.1 Sufficient Conditions for Independence

- Kind: theorem

- Summary: Measurable functions of disjoint independent blocks remain independent.

- Proof idea: Each function is measurable with respect to the sigma-field generated by its block; independent sigma-fields pass independence to their measurable variables.

- Exam use: Essential for random walks: past maxima and future increments can be separated.

- Pitfall: The functions may be complicated, but they cannot reuse variables from another block.

- Tags: measurable-functions, blocks, random-walk

##### Independent variables have product joint law

- ID: `durrett_ch2_joint_law_product_measure`

- Section: 2.1.2 Independence, Distribution, and Expectation

- Kind: theorem

- Summary: If X_1,...,X_n are independent with laws mu_i, then the joint law of the vector is the product measure mu_1 x ... x mu_n.

- Proof idea: Check equality on measurable rectangles and extend by the pi-lambda theorem.

- Exam use: Turns independence questions into product-measure integration questions.

- Pitfall: Matching marginal laws alone never proves independence; the joint law must factor.

- Tags: joint-law, product-measure, independence

##### Expectation factorization under independence

- ID: `durrett_ch2_expectation_factorization`

- Section: 2.1.2 Independence, Distribution, and Expectation

- Kind: theorem

- Summary: If X and Y are independent, then E[h(X,Y)] is the product-measure integral; in particular E[f(X)g(Y)] = E[f(X)]E[g(Y)] under nonnegative or integrable hypotheses.

- Proof idea: Use the product joint law and Fubini/Tonelli.

- Exam use: Core tool for variance of sums, covariance checks, moment computations, and LLN proofs.

- Pitfall: The factorization needs independence and integrability/nonnegativity; linearity of expectation alone is not enough for products.

- Tags: expectation, factorization, fubini

##### Convolution of distribution functions

- ID: `durrett_ch2_convolution_cdf`

- Section: 2.1.3 Sums of Independent Random Variables

- Kind: formula

- Summary: For independent X and Y with CDFs F and G, P(X+Y <= z) = integral F(z-y) dG(y).

- Proof idea: Integrate the indicator 1{x+y <= z} against the product law and evaluate the inner integral.

- Exam use: Use for distribution of sums when densities are absent or mixed.

- Pitfall: The notation dG means integration with respect to the probability measure induced by G, not ordinary differentiation unless a density exists.

- Tags: convolution, cdf, sum

##### Convolution density formula

- ID: `durrett_ch2_convolution_density`

- Section: 2.1.3 Sums of Independent Random Variables

- Kind: formula

- Summary: If X has density f and Y is independent with law G, then X+Y has density h(x)= integral f(x-y)dG(y); if Y has density g, h=f*g.

- Proof idea: Start from the CDF convolution and use Tonelli to identify the derivative/density.

- Exam use: Standard way to compute sums of exponentials, normals, and mixed variables.

- Pitfall: Keep the order x-y straight and check that the variables are independent.

- Tags: convolution, density, sum

##### Standard convolution examples

- ID: `durrett_ch2_standard_convolution_examples`

- Section: 2.1.3 Sums of Independent Random Variables

- Kind: example-bank

- Summary: Independent exponentials with the same rate give gamma/Erlang sums; independent normals add means and variances.

- Proof idea: Use the convolution density formula and complete the square for normals.

- Exam use: These are quick recognition patterns for prelim computations and later CLT comparisons.

- Pitfall: Normal parameters vary by text; in Durrett normal(mu,a) uses variance parameter a.

- Tags: normal, exponential, convolution

##### Constructing independent random variables

- ID: `durrett_ch2_construct_independent_variables`

- Section: 2.1.4 Constructing Independent Random Variables

- Kind: construction

- Summary: Finite independent variables with prescribed laws live on a product space with coordinate maps; infinite sequences use infinite product measures and cylinder sets.

- Proof idea: Define probabilities on rectangles/cylinders by products of the marginal laws and extend.

- Exam use: Important when a proof begins with 'let X_1,X_2,... be independent with laws ...'; this construction justifies existence.

- Pitfall: Infinite product constructions are subtler than finite products; do not treat all subsets of R^N as measurable.

- Tags: construction, product-space, iid

##### L2 weak law of large numbers

- ID: `durrett_ch2_weak_law_l2`

- Section: 2.2.1 L2 Weak Laws

- Kind: theorem

- Summary: For uncorrelated variables with bounded average variance, (S_n - E S_n)/n converges to 0 in L2 and hence in probability.

- Proof idea: Compute Var(S_n) as the sum of variances and apply Chebyshev.

- Exam use: Fastest LLN proof when second moments are available.

- Pitfall: Independence is sufficient but not necessary; uncorrelatedness plus variance control is enough.

- Tags: weak-law, l2, chebyshev

##### IID finite variance weak law

- ID: `durrett_ch2_iid_finite_variance_wlln`

- Section: 2.2.1 L2 Weak Laws

- Kind: corollary

- Summary: If X_i are iid with finite variance and mean mu, then S_n/n converges to mu in probability.

- Proof idea: Apply the L2 weak law with Var(S_n/n)=Var(X_1)/n.

- Exam use: The canonical first LLN proof; use it whenever the problem gives second moments.

- Pitfall: This proof does not cover infinite-variance variables, even when the mean exists.

- Tags: iid, finite-variance, weak-law

##### Triangular array weak law

- ID: `durrett_ch2_triangular_array_wlln`

- Section: 2.2.2 Triangular Arrays

- Kind: theorem

- Summary: For row-wise independent triangular arrays, convergence of sums follows when row variances are small and large jumps are controlled.

- Proof idea: Use truncation indicators plus Chebyshev on the truncated centered row sum.

- Exam use: This is the flexible form behind many LLN proofs with changing distributions.

- Pitfall: Rows are independent within each n; do not assume one infinite sequence unless the problem states it.

- Tags: triangular-array, weak-law, truncation

##### Truncation method for weak laws

- ID: `durrett_ch2_truncation_method`

- Section: 2.2.3 Truncation

- Kind: proof-template

- Summary: Replace X_i by X_i 1{|X_i| <= cutoff}, prove a law for the bounded part, and show discarded large jumps are negligible.

- Proof idea: Bound the probability of any large jump by a union bound and control the truncated variance or expectation.

- Exam use: Main route from finite variance LLN to finite mean LLN.

- Pitfall: Choose the cutoff at the scale of the sum, often n or epsilon n; a fixed cutoff usually proves the wrong statement.

- Tags: truncation, weak-law, large-jumps

##### IID finite mean weak law

- ID: `durrett_ch2_iid_finite_mean_wlln`

- Section: 2.2.3 Truncation

- Kind: theorem

- Summary: If X_i are iid with E|X_1| < infinity and mean mu, then S_n/n converges to mu in probability.

- Proof idea: Truncate at scale n, show the truncated centered average has small variance, and show large terms occur with vanishing probability.

- Exam use: This is the weak law most often needed when only integrability is assumed.

- Pitfall: Finite mean is enough for WLLN but the proof requires controlling both tails and centering errors.

- Tags: iid, finite-mean, weak-law

##### Maximum term negligibility

- ID: `durrett_ch2_max_negligible_condition`

- Section: 2.2.3 Truncation

- Kind: criterion

- Summary: For iid integrable variables, max_{i<=n}|X_i|/n goes to 0 in probability.

- Proof idea: Use the union bound n P(|X_1| > epsilon n) and the tail property implied by integrability.

- Exam use: Often proves that no single observation can dominate the average.

- Pitfall: The statement can fail for heavy tails without finite first moment.

- Tags: max-term, tail-bound, integrability

##### Weak law example patterns

- ID: `durrett_ch2_poissonization_and_wlln_examples`

- Section: 2.2 Weak Laws of Large Numbers

- Kind: example-bank

- Summary: Chapter 2 uses weak laws to control averages, random counts, and approximations where variance estimates or truncation make the error vanish.

- Proof idea: Reduce the target to a normalized sum and apply Chebyshev, triangular arrays, or truncation.

- Exam use: Use this as a mental index for prelim questions asking for convergence in probability.

- Pitfall: First identify the normalization; the wrong scale can make a true statement look false.

- Tags: examples, weak-law, convergence-in-probability

##### Weighted Cesaro variance weak law

- ID: `durrett_ch2_weighted_variance_cesaro_wlln`

- Section: 2.2.1 L2 Weak Laws

- Kind: exercise-pattern

- Summary: If uncorrelated variables satisfy var(X_i)/i -> 0, then n^{-2} sum_{i<=n} var(X_i) -> 0, so the centered average converges to 0 in L2.

- Proof idea: Write var(X_i)=i a_i with a_i -> 0 and split the weighted Cesaro average into a finite initial block plus a small tail.

- Exam use: Exercise 2.2.1 pattern: use when variances grow sublinearly rather than being uniformly bounded.

- Pitfall: Do not require identical distributions; the deterministic centering is E S_n/n, not necessarily a fixed mean.

- Tags: weighted-cesaro, variance, weak-law

##### Dependent covariance weak law

- ID: `durrett_ch2_dependent_covariance_wlln`

- Section: 2.2.1 L2 Weak Laws

- Kind: exercise-pattern

- Summary: A zero-mean sequence can satisfy a weak law even when dependent, provided lag covariances are bounded above by r(k) with r(k)->0.

- Proof idea: Expand E(S_n^2), group cross terms by lag, and use a finite-lag/tail split before applying Chebyshev.

- Exam use: Exercise 2.2.2 pattern: independence is not the real requirement; small average covariance is.

- Pitfall: The hypothesis is an upper bound without absolute values, so use it to control E(S_n^2) from above rather than proving absolute summability.

- Tags: dependent, covariance, weak-law

##### Monte Carlo integration via WLLN

- ID: `durrett_ch2_monte_carlo_integration_wlln`

- Section: 2.2.1 L2 Weak Laws

- Kind: application

- Summary: For iid uniform U_i and integrable f on [0,1], the sample average n^{-1} sum f(U_i) converges in probability to integral_0^1 f.

- Proof idea: Apply the finite-mean weak law to Y_i=f(U_i); if f is square-integrable, Chebyshev gives variance-scale error bounds.

- Exam use: Exercise 2.2.3 pattern: translate numerical integration into an average of iid random variables.

- Pitfall: The finite-variance Chebyshev bound at threshold a/sqrt(n) is order Var(f(U))/a^2, not a vanishing bound unless the threshold is fixed.

- Tags: monte-carlo, integration, chebyshev

##### Oscillating heavy tails can have finite effective centering

- ID: `durrett_ch2_oscillating_heavy_tail_centering`

- Section: 2.2.3 Truncation

- Kind: exercise-pattern

- Summary: A distribution may have infinite absolute mean but a convergent truncated mean, allowing S_n/n to converge in probability to a finite constant.

- Proof idea: Verify x P(|X|>x)->0, apply the truncation weak law, then show the truncated means converge, often by an alternating series test.

- Exam use: Exercise 2.2.4 pattern: cancellation in signs can produce a finite weak-law center even when E|X| is infinite.

- Pitfall: Do not call the limiting center EX unless the positive and negative parts are both finite.

- Tags: heavy-tail, truncated-mean, alternating-series

##### Diverging truncated-mean weak law

- ID: `durrett_ch2_diverging_truncated_mean_wlln`

- Section: 2.2.3 Truncation

- Kind: exercise-pattern

- Summary: If xP(|X|>x)->0 but EX is infinite, the averages can still satisfy S_n/n - mu_n -> 0 with mu_n=E[X 1{|X|<=n}] diverging.

- Proof idea: The truncation theorem controls fluctuations around the moving center; monotone convergence or tail integration identifies mu_n -> infinity.

- Exam use: Exercise 2.2.5 pattern: separate weak-law concentration from existence of a finite mean.

- Pitfall: A moving centering sequence is not the same as convergence of S_n/n to a finite constant.

- Tags: truncated-mean, infinite-mean, weak-law

##### Integer-valued tail-sum moment formulas

- ID: `durrett_ch2_integer_tail_sum_moments`

- Section: 2.2.3 Truncation

- Kind: formula

- Summary: For nonnegative integer-valued X, E X=sum_{n>=1}P(X>=n) and E X^2=sum_{n>=1}(2n-1)P(X>=n).

- Proof idea: Write k as sum_{n<=k}1 and k^2 as sum_{n<=k}(2n-1), then apply Tonelli to indicators.

- Exam use: Exercise 2.2.6 pattern: convert moments into tail sums for discrete heavy-tail checks.

- Pitfall: Use >= n for integer variables; continuous formulas use integrals with P(X>t) or P(X>=t), which differ only on negligible sets in many settings.

- Tags: tail-sum, integer-valued, moments

##### General tail integral transform

- ID: `durrett_ch2_general_tail_integral_transform`

- Section: 2.2.3 Truncation

- Kind: formula

- Summary: If H(x)=integral_{(-infty,x]} h(y)dy with h>=0, then E H(X)=integral h(y)P(X>=y)dy.

- Proof idea: Write H(X) as an integral of h(y)1{y<=X} and apply Tonelli.

- Exam use: Exercise 2.2.7 pattern: derive exponential moment and tail identities without differentiating a distribution function.

- Pitfall: Nonnegativity of h is what makes Tonelli immediate; signed h needs integrability checks.

- Tags: tail-integral, tonelli, exponential-moment

##### Unfair fair game truncation scale

- ID: `durrett_ch2_unfair_fair_game_truncation_scale`

- Section: 2.2.3 Truncation

- Kind: exercise-pattern

- Summary: For rare payoffs of size 2^k with probabilities about 1/(2^k k^2), truncation at b_n=2^{m(n)} can force S_n/(n/log_2 n) to converge to a negative constant despite EX=0.

- Proof idea: Pick b_n so large jumps are rare and truncated variance is small, then compute the missing positive tail as the dominant negative centering.

- Exam use: Exercise 2.2.8 pattern: a formally fair infinite-mean game can have typical averages far below its expectation.

- Pitfall: The expectation calculation is not enough; the typical scale is determined by truncation and the tail beyond b_n.

- Tags: fair-game, truncation-scale, infinite-mean

##### Positive-variable self-normalized weak law

- ID: `durrett_ch2_positive_variable_self_normalized_wlln`

- Section: 2.2.3 Truncation

- Kind: exercise-pattern

- Summary: For nonnegative iid variables, if mu(s)/(s P(X>s))->infinity and b_n solves n mu(b_n)=b_n, then S_n/b_n -> 1 in probability.

- Proof idea: Apply the triangular-array truncation theorem: large jumps vanish by the nu(s) condition, truncated variance is controlled by a tail-integral split, and the truncated mean equals b_n.

- Exam use: Exercise 2.2.9 pattern: choose the normalization from the truncated first moment rather than from a finite mean.

- Pitfall: The proof depends on b_n tending to infinity and on controlling xP(X>x) relative to mu(x); do not assume finite mean.

- Tags: positive-variables, self-normalization, truncation

##### First Borel-Cantelli lemma

- ID: `durrett_ch2_borel_cantelli_first`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: theorem

- Summary: If sum P(A_n) < infinity, then P(A_n infinitely often)=0.

- Proof idea: Bound P(union_{n>=m} A_n) by the tail sum and let m go to infinity.

- Exam use: Use to prove almost sure eventual bounds from summable probability estimates.

- Pitfall: No independence is needed for the first lemma.

- Tags: borel-cantelli, summability, almost-sure

##### Second Borel-Cantelli lemma

- ID: `durrett_ch2_borel_cantelli_second`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: theorem

- Summary: For independent events, if sum P(A_n)=infinity, then P(A_n infinitely often)=1.

- Proof idea: Use independence to bound the probability that none of A_m,...,A_n occur by a product and then by an exponential of the negative probability sum.

- Exam use: Use to prove infinitely many successes, recurrence-style events, and almost sure lower bounds.

- Pitfall: Independence or a suitable replacement is essential; divergence alone is not enough.

- Tags: borel-cantelli, independence, infinitely-often

##### Limsup event interpretation

- ID: `durrett_ch2_limsup_events`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: definition

- Summary: The event {A_n infinitely often} is limsup A_n = intersection_m union_{n>=m} A_n.

- Proof idea: Rewrite 'infinitely often' as 'for every m there exists n>=m' and translate quantifiers to countable set operations.

- Exam use: Needed before applying Borel-Cantelli and for a.s. convergence arguments.

- Pitfall: Do not confuse limsup A_n with union_n A_n; limsup requires infinitely many occurrences.

- Tags: limsup, events, infinitely-often

##### Summable tail bounds imply a.s. eventual control

- ID: `durrett_ch2_bc_tail_bounds`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: proof-template

- Summary: If P(|X_n| > a_n) is summable, then |X_n| <= a_n eventually almost surely.

- Proof idea: Apply first Borel-Cantelli to the events {|X_n| > a_n}.

- Exam use: A common one-line finish after Markov, Chebyshev, or exponential bounds.

- Pitfall: Summability of the bound matters; merely tending to zero gives convergence in probability, not a.s. eventual control.

- Tags: tail-bound, almost-sure, eventual-control

##### Subsequence plus monotonicity upgrade

- ID: `durrett_ch2_subsequence_bc_upgrade`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: proof-template

- Summary: Prove almost sure convergence along a sparse subsequence using Borel-Cantelli, then control gaps by monotonicity or maximal bounds.

- Proof idea: Choose a subsequence making probabilities summable; bridge between subsequence times with deterministic or probabilistic estimates.

- Exam use: Appears in strong law proofs and renewal estimates.

- Pitfall: The bridge is the hard part; convergence on a subsequence alone usually does not imply full convergence.

- Tags: subsequence, borel-cantelli, strong-law

##### Independent trials occur infinitely often

- ID: `durrett_ch2_bc_independent_trials`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: example-pattern

- Summary: For independent events with non-summable probabilities, the events occur infinitely often with probability one.

- Proof idea: Apply the second Borel-Cantelli lemma directly.

- Exam use: Useful for coin-flip patterns, record events, and rare-event recurrence questions.

- Pitfall: Verify mutual independence or an acceptable independent-block structure, not just pairwise independence.

- Tags: independent-events, rare-events, infinitely-often

##### Subsequence principle for convergence in probability

- ID: `durrett_ch2_probability_convergence_subsequence_principle`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: proof-template

- Summary: X_n -> X in probability iff every subsequence has a further subsequence converging to X almost surely.

- Proof idea: Choose a further subsequence with summable error probabilities and apply Borel-Cantelli; conversely use the topological subsequence criterion on probabilities.

- Exam use: Exercises 2.3.4-2.3.5 pattern: reduce convergence-in-probability limit theorems to almost sure subsequences.

- Pitfall: The almost sure subsequence depends on the original subsequence; this does not say the whole sequence converges a.s.

- Tags: convergence-in-probability, subsequence, borel-cantelli

##### Continuous mapping for convergence in probability

- ID: `durrett_ch2_continuous_mapping_probability`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: If X_n -> X in probability and f is continuous, then f(X_n) -> f(X) in probability.

- Proof idea: Localize X to a compact set with high probability, use uniform continuity there, and control the complement.

- Exam use: Exercise 2.3.2 pattern: prove mapping results directly without invoking subsequences.

- Pitfall: Continuity only gives local uniform continuity after compact localization; global uniform continuity is not required.

- Tags: continuous-mapping, convergence-in-probability, compact-localization

##### Fatou and dominated convergence from convergence in probability

- ID: `durrett_ch2_probability_fatou_dominated`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: Fatou and dominated convergence extend from a.s. convergence to convergence in probability by passing to a.s. convergent subsequences.

- Proof idea: Select a subsequence attaining the relevant liminf or violating the target limit, then extract an a.s. convergent further subsequence.

- Exam use: Exercises 2.3.4-2.3.5 pattern: combine subsequence extraction with Fatou, DCT, bounded convergence, or uniform integrability.

- Pitfall: For unbounded dominated-convergence variants, prove uniform integrability; convergence in probability alone is not enough for expectations.

- Tags: fatou, dominated-convergence, uniform-integrability

##### Metric and completeness for convergence in probability

- ID: `durrett_ch2_probability_metric_complete`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: The metric E[|X-Y|/(1+|X-Y|)] metrizes convergence in probability, and random variables modulo a.s. equality are complete under it.

- Proof idea: Use the subadditivity of t/(1+t); for completeness choose a subsequence with summable jump probabilities and apply Borel-Cantelli to get an a.s. limit.

- Exam use: Exercises 2.3.6-2.3.7 pattern: turn Cauchy in probability into an a.s. Cauchy subsequence, then pull the whole sequence back by Cauchy control.

- Pitfall: The metric is on equivalence classes modulo a.s. equality; otherwise d(X,Y)=0 is only equality a.s.

- Tags: metric, complete-space, convergence-in-probability

##### Kochen-Stone second-moment lower bound

- ID: `durrett_ch2_kochen_stone_second_moment`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: lemma

- Summary: If sum P(A_n)=infinity, then P(A_n i.o.) is bounded below by a limsup ratio of squared expected counts to second moments of event counts.

- Proof idea: Apply the second-moment inequality P(S_n>0) >= (ES_n)^2/E(S_n^2) to tail sums of indicators, then let the tail start go to infinity.

- Exam use: Exercise 2.3.10 pattern: prove lower bounds for infinitely-often events under dependence when full independence is unavailable.

- Pitfall: The denominator uses all pairwise intersections; replacing it by product probabilities is only valid under independence.

- Tags: kochen-stone, second-moment, dependent-events

##### Bernoulli convergence via Borel-Cantelli

- ID: `durrett_ch2_bernoulli_bc_convergence`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: For independent Bernoulli variables X_n with P(X_n=1)=p_n, X_n -> 0 in probability iff p_n -> 0, and X_n -> 0 a.s. iff sum p_n < infinity.

- Proof idea: Translate convergence to occurrence of {X_n=1}; use first or second Borel-Cantelli.

- Exam use: Exercise 2.3.11 pattern: reduce binary convergence questions to summability of success probabilities.

- Pitfall: The a.s. direction needs independence for the divergent case.

- Tags: bernoulli, borel-cantelli, convergence

##### On countable spaces, convergence in probability implies a.s. convergence

- ID: `durrett_ch2_countable_space_probability_to_as`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: If Omega is countable with all subsets measurable, convergence in probability implies pointwise convergence on all atoms of positive probability, hence almost sure convergence.

- Proof idea: A positive-mass point that fails pointwise convergence would keep an error probability bounded away from zero along a subsequence.

- Exam use: Exercise 2.3.12 pattern: use atoms to upgrade convergence modes.

- Pitfall: This relies on countability; it is false on general probability spaces.

- Tags: countable-space, atoms, convergence

##### Arbitrary random variables can be normalized to zero a.s.

- ID: `durrett_ch2_arbitrary_normalization_bc`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: For any random variables X_n, one can choose deterministic c_n -> infinity so that X_n/c_n -> 0 almost surely.

- Proof idea: Pick c_n large enough that tail probabilities at finitely many rational error levels are summable, then diagonalize with Borel-Cantelli.

- Exam use: Exercise 2.3.13 pattern: build a normalization after seeing the sequence rather than using moment assumptions.

- Pitfall: The constants are not canonical and may grow very fast.

- Tags: normalization, diagonalization, borel-cantelli

##### Independent supremum finiteness criterion

- ID: `durrett_ch2_independent_sup_finite_criterion`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: criterion

- Summary: For independent X_n, sup_n X_n is finite a.s. iff sum P(X_n>A)<infinity for some finite A.

- Proof idea: Use first Borel-Cantelli for sufficiency and second Borel-Cantelli over integer thresholds for necessity.

- Exam use: Exercise 2.3.14 pattern: characterize boundedness of an independent sequence by summability of one tail level.

- Pitfall: Independence is used only for the divergent necessity direction.

- Tags: supremum, tail-sum, independence

##### Exponential maxima live at log n scale

- ID: `durrett_ch2_exponential_maxima_log_scale`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: example-pattern

- Summary: For iid exponential-tail variables with P(X>x)=e^{-x}, limsup X_n/log n=1 and max_{m<=n}X_m/log n -> 1 almost surely.

- Proof idea: Use Borel-Cantelli at thresholds (1+-epsilon)log n and estimate P(M_n <= (1-epsilon)log n) by an exponential bound.

- Exam use: Exercise 2.3.15 pattern: identify extreme-value scales via summable/nonsummable tail probabilities.

- Pitfall: Pointwise limsup and running maximum convergence require slightly different lower-bound arguments.

- Tags: maxima, exponential-tail, log-scale

##### Threshold maxima infinitely-often criterion

- ID: `durrett_ch2_threshold_maxima_io`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: criterion

- Summary: For iid X_n and increasing thresholds lambda_n, max_{m<=n}X_m>lambda_n i.o. is equivalent to X_n>lambda_n i.o., hence controlled by sum tail probabilities.

- Proof idea: If individual threshold exceedances are summable, only finitely many observations can drive the maxima over increasing thresholds; if divergent, the individual exceedances occur i.o.

- Exam use: Exercise 2.3.16 pattern: reduce running-maximum events to one-time exceedance events when thresholds increase.

- Pitfall: The monotonicity lambda_n up to infinity is what prevents one early large value from causing infinitely many later exceedances.

- Tags: running-maximum, thresholds, borel-cantelli

##### Single observations versus maxima under n-normalization

- ID: `durrett_ch2_iid_normalized_single_vs_max`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: criterion-card

- Summary: For iid Y_n, Y_n/n -> 0 a.s. needs E|Y_1|<infinity, max_{m<=n}Y_m/n -> 0 a.s. needs E(Y_1^+)<infinity, and max convergence in probability needs xP(Y_1>x)->0.

- Proof idea: Apply Borel-Cantelli to |Y_n|>epsilon n or Y_n>epsilon n; for maxima in probability use 1-(1-p_n)^n ->0 iff np_n->0.

- Exam use: Exercise 2.3.17 pattern: distinguish two-sided single-term control from one-sided running-maximum control.

- Pitfall: Almost sure and in-probability maxima have different tail requirements.

- Tags: iid, maxima, normalization

##### Monotone variance subsequence a.s. upgrade

- ID: `durrett_ch2_monotone_variance_subsequence_as`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: proof-template

- Summary: For increasing nonnegative X_n with EX_n asymptotic to a n^alpha and variance O(n^beta), beta<2alpha, prove X_n/n^alpha -> a a.s. via sparse subsequences and monotonicity.

- Proof idea: Use Chebyshev on n_k=floor(k^r) with r(2alpha-beta)>1, Borel-Cantelli on the subsequence, then squeeze intermediate n by monotonicity.

- Exam use: Exercise 2.3.18 pattern: turn variance bounds into a.s. asymptotics when monotonicity bridges gaps.

- Pitfall: Without monotonicity, subsequence convergence alone would not control intermediate indices.

- Tags: variance-bound, monotonicity, almost-sure

##### Poisson sums strong law with variable means

- ID: `durrett_ch2_poisson_sum_slln_series`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: exercise-pattern

- Summary: For independent Poisson X_n with means lambda_n and m_n=sum_{k<=n}lambda_k -> infinity, S_n/m_n -> 1 almost surely.

- Proof idea: Apply the random-series convergence criterion to (X_n-lambda_n)/m_n, using sum lambda_n/m_n^2 < infinity, then Kronecker's lemma.

- Exam use: Exercise 2.3.19 pattern: use variance summability with the natural cumulative-mean scale.

- Pitfall: A naive subsequence proof can fail when the means have large jumps; the series proof handles arbitrary lambda_n.

- Tags: poisson, strong-law, kronecker

##### St. Petersburg almost-sure limsup explosion

- ID: `durrett_ch2_st_petersburg_as_limsup`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: example-pattern

- Summary: In the St. Petersburg game, X_n/(n log_2 n) has infinite limsup almost surely, so the in-probability normalization for sums is not an a.s. law.

- Proof idea: For each M, the events {X_n >= M n log_2 n} have divergent probability sum and are independent; apply the second Borel-Cantelli lemma.

- Exam use: Exercise 2.3.20 pattern: rare giant jumps can destroy almost sure convergence even when weak-law scaling works.

- Pitfall: Convergence in probability of S_n/(n log n) does not control limsup behavior.

- Tags: st-petersburg, limsup, giant-jumps

##### Kolmogorov maximal inequality

- ID: `durrett_ch2_kolmogorov_maximal_inequality`

- Section: 2.4 Strong Law of Large Numbers

- Kind: inequality

- Summary: For independent mean-zero variables with finite variances, the probability that partial sums exceed a threshold is bounded by the total variance divided by the threshold squared.

- Proof idea: Stop at the first crossing and use independence of the future increment to control E[S_n^2] on crossing events.

- Exam use: Main tool for upgrading variance summability to almost sure control of partial sums.

- Pitfall: The variables must be centered and independent; this is stronger than ordinary Chebyshev for the final sum.

- Tags: maximal-inequality, partial-sums, strong-law

##### Kolmogorov convergence criterion

- ID: `durrett_ch2_kolmogorov_convergence_criterion`

- Section: 2.4 Strong Law of Large Numbers

- Kind: theorem

- Summary: If independent mean-zero variables have summable variances, then their series converges almost surely.

- Proof idea: Apply the maximal inequality to tails of the series and use Cauchy convergence almost surely.

- Exam use: Use for convergence of centered random series and as a strong-law building block.

- Pitfall: Summable variances are sufficient, not necessary; do not mistake it for a complete characterization.

- Tags: random-series, summable-variance, almost-sure

##### Fourth-moment strong law shortcut

- ID: `durrett_ch2_iid_finite_fourth_slln`

- Section: 2.4 Strong Law of Large Numbers

- Kind: proof-template

- Summary: If iid centered variables have finite fourth moment, then S_n/n -> 0 almost surely by summable fourth-moment bounds.

- Proof idea: Bound E[S_n^4] by a constant times n^2 and sum P(|S_n| > epsilon n) over n.

- Exam use: A quick SLLN proof when high moments are available.

- Pitfall: This proof is convenient but much stronger than needed; finite first moment is enough for the iid SLLN.

- Tags: fourth-moment, strong-law, markov

##### IID finite mean strong law

- ID: `durrett_ch2_iid_finite_mean_slln`

- Section: 2.4 Strong Law of Large Numbers

- Kind: theorem

- Summary: If X_i are iid and E|X_1| < infinity with mean mu, then S_n/n -> mu almost surely.

- Proof idea: Truncate variables, prove convergence for bounded/centered parts with maximal inequalities, and show tails are negligible via Borel-Cantelli.

- Exam use: Central theorem of the chapter and a frequent prelim target.

- Pitfall: Almost sure convergence is stronger than convergence in probability; the WLLN proof alone is not enough.

- Tags: strong-law, iid, finite-mean

##### Strong law normalization habits

- ID: `durrett_ch2_slln_normalized_sums`

- Section: 2.4 Strong Law of Large Numbers

- Kind: concept-link

- Summary: Strong laws usually show a normalized centered sum tends to zero almost surely, then add back deterministic centering.

- Proof idea: Write S_n/n - mu as n^{-1} sum (X_i - mu) and focus on partial-sum control.

- Exam use: Helps organize proofs for arrays, subsequences, and renewal counting.

- Pitfall: Centering must be finite; if the mean is infinite, S_n/n behaves differently.

- Tags: normalization, centering, strong-law

##### Renewal reward ratio via SLLN

- ID: `durrett_ch2_renewal_reward_ratio_slln`

- Section: 2.4 Strong Law of Large Numbers

- Kind: application

- Summary: For cycles with iid working time X_i and downtime Y_i, the long-run working fraction is E X_i/(E X_i+E Y_i).

- Proof idea: Apply the SLLN to cycle lengths X_i+Y_i and rewards X_i, invert cycle time to get N(t)/t, and squeeze the incomplete final cycle.

- Exam use: Exercise 2.4.1 pattern: renewal reward limits are ratios of mean reward to mean cycle length.

- Pitfall: Account for the possible incomplete cycle at time t; its contribution is negligible after division by t.

- Tags: renewal-reward, slln, long-run-fraction

##### Multiplicative recursion becomes additive after logs

- ID: `durrett_ch2_multiplicative_recursion_log_slln`

- Section: 2.4 Strong Law of Large Numbers

- Kind: proof-template

- Summary: If a process satisfies |X_n|=product_{k<=n}R_k with iid positive factors and E|log R_1|<infinity, then n^{-1}log|X_n| -> E log R_1 a.s.

- Proof idea: Take logarithms and apply the finite-mean SLLN; compute the constant from the distribution of the radial factor.

- Exam use: Exercise 2.4.2 pattern: random scaling problems reduce to an SLLN for log radii.

- Pitfall: Check integrability near zero before applying the SLLN to logarithms.

- Tags: multiplicative-process, log-transform, slln

##### Kelly-style investment growth optimization

- ID: `durrett_ch2_kelly_investment_concavity`

- Section: 2.4 Strong Law of Large Numbers

- Kind: application

- Summary: For fixed portfolio fraction p, long-run log wealth converges to c(p)=E log(ap+(1-p)V); c is concave in p and endpoint derivatives decide whether the optimum is interior.

- Proof idea: Write log wealth as a sum of iid log returns, apply the SLLN, then differentiate c(p) under the expectation and use concavity.

- Exam use: Exercise 2.4.3 pattern: optimize almost-sure exponential growth by maximizing expected log return.

- Pitfall: Maximizing expected wealth and maximizing expected log wealth are different criteria.

- Tags: investment, kelly, expected-log-growth

##### Kolmogorov three-series theorem

- ID: `durrett_ch2_three_series_theorem`

- Section: 2.5 Convergence of Random Series

- Kind: theorem

- Summary: For independent variables, convergence of sum X_n is characterized by tail probabilities, truncated means, and truncated variances.

- Proof idea: Split each X_n into large jumps, truncated means, and centered truncated fluctuations; apply Borel-Cantelli and the variance convergence criterion.

- Exam use: The main checklist for almost sure convergence of independent random series.

- Pitfall: The theorem uses a fixed truncation level; changing the cutoff changes the conditions but not the spirit.

- Tags: three-series, random-series, truncation

##### Large jumps in random series

- ID: `durrett_ch2_random_series_large_jumps`

- Section: 2.5 Convergence of Random Series

- Kind: criterion

- Summary: A necessary component for series convergence is that large jumps occur only finitely often, typically sum P(|X_n| > c) < infinity.

- Proof idea: If large jumps occur infinitely often, the terms cannot tend to zero; Borel-Cantelli gives the precise almost sure statement.

- Exam use: First diagnostic check in random-series problems.

- Pitfall: Termwise convergence to zero is necessary but not sufficient for series convergence.

- Tags: large-jumps, random-series, borel-cantelli

##### Truncated centering in random series

- ID: `durrett_ch2_random_series_centering`

- Section: 2.5 Convergence of Random Series

- Kind: proof-template

- Summary: After removing large jumps, convergence depends on whether the truncated expectations form a convergent deterministic series.

- Proof idea: Separate X_n 1{|X_n| <= c} into its mean plus centered fluctuation.

- Exam use: Prevents hidden deterministic drift from spoiling almost sure convergence.

- Pitfall: A centered variance argument cannot control a divergent sum of means.

- Tags: centering, truncation, random-series

##### Rates for random series tails

- ID: `durrett_ch2_series_rate_estimates`

- Section: 2.5.1 Rates of Convergence

- Kind: concept-link

- Summary: Once a random series converges, tail estimates can quantify how fast partial sums approach the limit.

- Proof idea: Combine maximal inequalities with variance or moment bounds on the remaining tail.

- Exam use: Useful when a problem asks not just convergence but an almost sure order estimate.

- Pitfall: A convergence theorem alone may not give the requested rate; track the size of tail variances or probabilities.

- Tags: rates, random-series, tail-estimates

##### Infinite mean changes LLN behavior

- ID: `durrett_ch2_infinite_mean_behavior`

- Section: 2.5.2 Infinite Mean

- Kind: concept-link

- Summary: When the mean is infinite or undefined, normalized sums can diverge or be controlled by rare large terms rather than averaging.

- Proof idea: Use truncation to see which tail contribution dominates the normalization.

- Exam use: Important for spotting when a finite-mean LLN theorem cannot be applied.

- Pitfall: Do not center by EX if EX is not finite; the expression may be meaningless.

- Tags: infinite-mean, heavy-tail, truncation

##### Renewal process basics

- ID: `durrett_ch2_renewal_process`

- Section: 2.6 Renewal Theory

- Kind: definition

- Summary: With iid positive interarrival times xi_i, renewal times T_n = xi_1+...+xi_n and count N(t)=max{n:T_n<=t} form a renewal process.

- Proof idea: The strong law gives T_n/n -> mu, which inverts to N(t)/t -> 1/mu under finite mean.

- Exam use: Connects laws of large numbers to counting processes and waiting-time problems.

- Pitfall: Be careful with indexing: some formulas use the last renewal before t and the next renewal after t.

- Tags: renewal-process, counting, slln

##### Elementary renewal theorem

- ID: `durrett_ch2_elementary_renewal_theorem`

- Section: 2.6 Renewal Theory

- Kind: theorem

- Summary: For iid positive interarrival times with finite mean mu, E[N(t)]/t -> 1/mu.

- Proof idea: Use renewal decompositions and LLN-style bounds to compare the counting process with deterministic time.

- Exam use: Useful for expected counts in long-run systems.

- Pitfall: Almost sure convergence of N(t)/t and convergence of its expectation are related but require different arguments.

- Tags: renewal-theorem, expectation, long-run-rate

##### Renewal equation

- ID: `durrett_ch2_renewal_equation`

- Section: 2.6 Renewal Theory

- Kind: formula

- Summary: Many renewal quantities satisfy H(t)=h(t)+ integral_0^t H(t-s)dF(s), where F is the interarrival distribution.

- Proof idea: Condition on the first renewal time; if it occurs at s, restart the process from t-s.

- Exam use: Primary modeling move for renewal reward, age, residual lifetime, and alternating renewal problems.

- Pitfall: The input function h and the renewal function must match the same convention for time zero.

- Tags: renewal-equation, conditioning, restart

##### Key renewal theorem

- ID: `durrett_ch2_key_renewal_theorem`

- Section: 2.6 Renewal Theory

- Kind: theorem

- Summary: For nonarithmetic renewals and directly Riemann integrable h, renewal convolutions converge to (1/mu) integral h.

- Proof idea: The theorem refines the renewal equation asymptotically using smoothing properties of the renewal measure.

- Exam use: Use for limiting age, residual lifetime, and renewal reward calculations.

- Pitfall: Arithmetic interarrival distributions have lattice oscillations; the nonarithmetic hypothesis matters.

- Tags: key-renewal-theorem, nonarithmetic, asymptotics

##### Superadditivity for large-deviation probabilities

- ID: `durrett_ch2_subadditive_log_probability`

- Section: 2.7 Large Deviations

- Kind: lemma

- Summary: For iid sums, pi_n=P(S_n>=na) satisfies pi_{m+n} >= pi_m pi_n, so log pi_n is superadditive and n^{-1}log pi_n has a limit.

- Proof idea: Use independence of S_m and S_{m+n}-S_m, then apply the superadditive sequence lemma.

- Exam use: Establishes existence of the exponential decay rate before computing it.

- Pitfall: The limit can be zero or negative infinity; existence alone does not guarantee a useful exponential bound.

- Tags: large-deviations, superadditivity, rate

##### Chernoff exponential bound

- ID: `durrett_ch2_chernoff_bound`

- Section: 2.7 Large Deviations

- Kind: inequality

- Summary: If phi(theta)=E exp(theta X) is finite, then P(S_n>=na) <= exp(-n(a theta - log phi(theta))).

- Proof idea: Apply Markov's inequality to exp(theta S_n) and use independence to factor the moment generating function.

- Exam use: Main upper-bound engine for large-deviation estimates.

- Pitfall: Optimize over theta>0; a random unoptimized theta may prove decay but not the sharp rate.

- Tags: chernoff, mgf, large-deviations

##### Exponential tilting

- ID: `durrett_ch2_exponential_tilting`

- Section: 2.7 Large Deviations

- Kind: construction

- Summary: The tilted law F_theta has density proportional to exp(theta x) relative to F, and its mean is phi'(theta)/phi(theta).

- Proof idea: Normalize exp(theta x)dF by phi(theta); differentiating log phi gives the tilted mean.

- Exam use: Used for the lower bound in Cramer-style large deviations by making the rare event typical.

- Pitfall: Tilting is only valid where the moment generating function is finite.

- Tags: exponential-tilting, mgf, change-of-measure

##### Cramer rate formula in the smooth case

- ID: `durrett_ch2_cramer_rate_formula`

- Section: 2.7 Large Deviations

- Kind: theorem

- Summary: When a>mu and there is theta_a with a=phi'(theta_a)/phi(theta_a), n^{-1}log P(S_n>=na) -> -a theta_a + log phi(theta_a).

- Proof idea: Use Chernoff for the upper bound and exponential tilting plus the weak law for the lower bound.

- Exam use: Compute sharp exponential rates for normal, exponential, Bernoulli, and Poisson examples.

- Pitfall: Boundary cases require separate treatment when the optimizing theta is not inside the finite-mgf interval.

- Tags: cramer, rate-function, large-deviations

##### Subsequence control upgraded to full control

- ID: `durrett_ch2_subsequence_upgrade`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: proof-template

- Summary: A sparse almost-sure estimate can be upgraded to all times when the gaps are controlled by monotonicity or a maximal inequality.

- Proof idea: Choose a subsequence with summable error probabilities, then compare every intermediate index to the next subsequence point.

- Exam use: Exercise 2.5.1 pattern: prove a rate on n_m=floor(m^alpha), then bridge the gaps.

- Pitfall: Subsequence convergence alone is insufficient; the gap-control step carries the proof.

- Tags: subsequence, maximal-inequality, almost-sure

##### Two-series variance criterion

- ID: `durrett_ch2_two_series_theorem`

- Section: 2.5 Convergence of Random Series

- Kind: criterion

- Summary: Independent mean-zero variables with summable variances have an almost surely convergent series.

- Proof idea: Use Kolmogorov's maximal inequality to make the tails Cauchy almost surely.

- Exam use: Quickly solves centered series such as sum X_n sin(n pi t)/n.

- Pitfall: The variables must be independent and centered; otherwise deterministic drift must be treated separately.

- Tags: two-series, variance, random-series

##### Independent series variance test

- ID: `durrett_ch2_independent_series_variance_test`

- Section: 2.5 Convergence of Random Series

- Kind: test

- Summary: For independent centered summands, finite total variance is enough for almost-sure convergence.

- Proof idea: Check that the series of variances is bounded by a known summable numerical series.

- Exam use: Exercise 2.5.3 pattern: trigonometric factors are harmless when bounded by 1.

- Pitfall: Do not require identical distributions; only independence, centering, and summable variances.

- Tags: random-series, variance-test, almost-sure

##### Kronecker lemma for normalized sums

- ID: `durrett_ch2_kronecker_lemma`

- Section: 2.5 Convergence of Random Series

- Kind: lemma

- Summary: If sum x_n/n converges, then n^{-1} sum_{k<=n} x_k -> 0.

- Proof idea: Apply summation by parts to convert convergence of weighted terms into Cesaro decay of partial sums.

- Exam use: Turns convergence of a random series into a strong law for averages.

- Pitfall: The weights must increase to infinity; here the natural weight is n.

- Tags: kronecker, normalized-sums, series

##### Tail-sum moment test

- ID: `durrett_ch2_tail_sum_moment_test`

- Section: 2.2 Weak Laws of Large Numbers

- Kind: criterion

- Summary: For p>0, E|X|^p is finite exactly when the tail probabilities P(|X|^p>n) are summable up to constants.

- Proof idea: Compare the integral of the tail distribution with the integer tail sum.

- Exam use: Exercise 2.5.2 pattern: a.s. term control plus Borel-Cantelli forces finite moments.

- Pitfall: The tail variable is |X|^p, not |X|; keep the normalization consistent.

- Tags: moments, tails, tail-sum

##### Random power-series radius

- ID: `durrett_ch2_power_series_radius`

- Section: 2.5 Convergence of Random Series

- Kind: application

- Summary: The radius of sum X_n z^n is 1/limsup |X_n|^{1/n}; for iid coefficients this is decided by E log^+ |X_1|.

- Proof idea: Use the root test and Borel-Cantelli on events log^+|X_n| > epsilon n.

- Exam use: Exercise 2.5.8 pattern: logarithmic tails determine random analytic radius.

- Pitfall: Nonzero coefficients must occur infinitely often to rule out a larger radius.

- Tags: power-series, root-test, log-tail

##### Levy maximal inequality for independent increments

- ID: `durrett_ch2_levy_maximal_inequality`

- Section: 2.5 Convergence of Random Series

- Kind: inequality

- Summary: A maximum of partial increments is controlled by the terminal increment times a lower bound on remaining-tail probabilities.

- Proof idea: Stop at the first crossing; if the later tail is small, the full terminal sum must still be large.

- Exam use: Core tool for Levy's theorem and convergence-in-probability to almost-sure convergence upgrades.

- Pitfall: The independence is between the first-crossing event and the future tail increment.

- Tags: levy-inequality, maximal-inequality, independent-increments

##### Independent increments in partial sums

- ID: `durrett_ch2_independent_increments`

- Section: 2.5 Convergence of Random Series

- Kind: fact

- Summary: For sums of independent variables, disjoint blocks of increments are independent.

- Proof idea: Events determined by X_{m+1},...,X_j are independent of sums using X_{j+1},...,X_n.

- Exam use: Used inside first-crossing arguments and block decompositions.

- Pitfall: The original variables must be independent; identical distribution is not needed.

- Tags: independent-increments, blocks, partial-sums

##### Cauchy criterion in probability

- ID: `durrett_ch2_cauchy_in_probability`

- Section: 2.5 Convergence of Random Series

- Kind: criterion

- Summary: Convergence in probability implies the sequence is Cauchy in probability, uniformly over sufficiently far tails.

- Proof idea: Apply the definition to pairs S_m,S_n after both indices are large.

- Exam use: Starting point for proving Levy's theorem.

- Pitfall: Cauchy in probability alone does not immediately give a.s. convergence without extra structure.

- Tags: convergence-in-probability, cauchy, levy-theorem

##### Convergence in probability

- ID: `durrett_ch2_convergence_in_probability`

- Section: 2.2 Weak Laws of Large Numbers

- Kind: definition

- Summary: X_n -> X in probability means P(|X_n-X|>epsilon)->0 for every epsilon>0.

- Proof idea: Translate the target into tail probabilities and show each tends to zero.

- Exam use: Used throughout weak laws, maximal estimates, and large-deviation preliminaries.

- Pitfall: It is weaker than almost-sure convergence and does not by itself control all subsequences pathwise.

- Tags: convergence-in-probability, weak-convergence, tail-probability

##### Chebyshev inequality for sums

- ID: `durrett_ch2_chebyshev`

- Section: 2.2 Weak Laws of Large Numbers

- Kind: inequality

- Summary: If a centered sum has finite variance, P(|S|>x) <= Var(S)/x^2.

- Proof idea: Compute or bound the variance, then divide by the square of the target scale.

- Exam use: Exercise 2.5.12 pattern: dyadic Chebyshev bounds become summable with a logarithmic correction.

- Pitfall: Chebyshev gives polynomial bounds; a log factor may be needed for summability.

- Tags: chebyshev, variance, weak-law

##### Renewal function

- ID: `durrett_ch2_renewal_function`

- Section: 2.6 Renewal Theory

- Kind: definition

- Summary: The renewal function U(t)=E N_t records the expected number of renewals by time t.

- Proof idea: Relate U(t) to stopped sums of truncated interarrival times.

- Exam use: Exercise 2.6.1 pattern: bound U(t) using E(xi_1 wedge t).

- Pitfall: Indexing conventions for N_t vary; keep the same convention through the proof.

- Tags: renewal-function, expected-count, renewal

##### Wald identity with truncated interarrivals

- ID: `durrett_ch2_wald_identity_truncated`

- Section: 2.6 Renewal Theory

- Kind: proof-template

- Summary: For bounded truncated increments xi_i wedge t and a renewal stopping time, the expected stopped sum factors as E increment times E count.

- Proof idea: Truncation makes the increments bounded, then optional-stopping or Wald's identity is safe.

- Exam use: Useful for elementary renewal estimates without assuming second moments.

- Pitfall: Do not apply untruncated Wald blindly when the stopping time or mean may be problematic.

- Tags: wald, truncation, renewal

##### Renewal counting strong law

- ID: `durrett_ch2_renewal_slln`

- Section: 2.6 Renewal Theory

- Kind: theorem

- Summary: If interarrival times have finite mean mu, then N(t)/t -> 1/mu almost surely.

- Proof idea: Use T_n/n -> mu and invert the inequalities T_{N(t)} <= t < T_{N(t)+1}.

- Exam use: Converts cycle averages into long-run time rates.

- Pitfall: The inversion requires positive interarrival times and finite mean.

- Tags: renewal, slln, counting-process

##### Uniform integrability from L2 bounds

- ID: `durrett_ch2_uniform_integrability`

- Section: 2.6 Renewal Theory

- Kind: criterion

- Summary: A family bounded in L2 is uniformly integrable, so a.s. convergence plus the L2 bound gives convergence of expectations.

- Proof idea: Use Cauchy-Schwarz to control large tails uniformly.

- Exam use: Exercise 2.6.2 pattern: upgrade N(t)/t -> 1/mu a.s. to U(t)/t -> 1/mu.

- Pitfall: Almost-sure convergence alone does not imply convergence of expectations.

- Tags: uniform-integrability, L2, expectations

##### Poisson memoryless property

- ID: `durrett_ch2_poisson_memoryless`

- Section: 2.6 Renewal Theory

- Kind: fact

- Summary: After a stopping time independent of future arrivals, the waiting time to the next Poisson arrival is exponential and independent of the past.

- Proof idea: Use independent increments of the Poisson process and the exponential waiting-time law.

- Exam use: Turns accepted arrivals after service completion into a renewal process.

- Pitfall: This finite-time memoryless identity is special to exponential interarrivals.

- Tags: poisson-process, memoryless, renewal

##### Renewal reward theorem

- ID: `durrett_ch2_renewal_reward_theorem`

- Section: 2.6 Renewal Theory

- Kind: theorem

- Summary: Long-run reward per unit time equals expected reward per cycle divided by expected cycle length.

- Proof idea: Apply the SLLN separately to rewards and cycle times, then squeeze the incomplete cycle.

- Exam use: Use for server acceptance fractions, machine uptime, and alternating renewal rewards.

- Pitfall: Check the cycle definition: rewards and lengths must correspond to the same cycles.

- Tags: renewal-reward, long-run-average, cycles

##### Age and residual lifetime limits

- ID: `durrett_ch2_age_residual_life`

- Section: 2.6 Renewal Theory

- Kind: application

- Summary: The limiting tail for age, residual life, or their joint event is an integrated tail of the interarrival distribution divided by mu.

- Proof idea: Write a renewal equation for the event and apply the key renewal theorem to the forcing function.

- Exam use: Exercises 2.6.4 and 2.6.6 pattern: identify the renewal interval straddling t.

- Pitfall: The age and residual life are not generally independent in the limit.

- Tags: age, residual-life, key-renewal-theorem

##### Alternating renewal process

- ID: `durrett_ch2_alternating_renewal_process`

- Section: 2.6 Renewal Theory

- Kind: model

- Summary: A system alternates between on- and off-periods; the long-run on probability is mean on-time divided by mean cycle length.

- Proof idea: Condition on the first on-period and restart after a complete on/off cycle.

- Exam use: Exercise 2.6.7 pattern: machine availability equals mu_on/(mu_on+mu_off).

- Pitfall: The cycle law is the convolution of one on-period and one off-period.

- Tags: alternating-renewal, availability, cycles

##### Renewal density

- ID: `durrett_ch2_renewal_density`

- Section: 2.6 Renewal Theory

- Kind: formula

- Summary: If F has density f, the non-initial renewal measure has density v=sum_{n>=1} f^{*n}, satisfying v=f+v*F.

- Proof idea: Separate the first convolution term from the renewal density series.

- Exam use: Exercise 2.6.9 pattern: apply the key renewal theorem to f to get v(t)->1/mu.

- Pitfall: Direct Riemann integrability of f is the hypothesis that permits the limit theorem.

- Tags: renewal-density, convolution, key-renewal-theorem

##### Large-deviation exponent gamma

- ID: `durrett_ch2_large_deviation_gamma`

- Section: 2.7 Large Deviations

- Kind: definition

- Summary: gamma(a) is the limiting exponential rate n^{-1} log P(S_n >= na), possibly 0 or -infinity.

- Proof idea: Use superadditivity of log probabilities to prove existence, then compute or bound the rate.

- Exam use: Exercises 2.7.1 and 2.7.2 pattern: analyze the effective domain and concavity of gamma.

- Pitfall: A rate of -infinity corresponds to an impossible event, not merely a very small probability.

- Tags: large-deviations, gamma, rate

##### Independent sums factor rare-event probabilities

- ID: `durrett_ch2_independent_sums`

- Section: 2.7 Large Deviations

- Kind: fact

- Summary: For iid sums, events involving disjoint blocks can be multiplied to get lower bounds on large-deviation probabilities.

- Proof idea: Split S_{m+n}=S_m+(S_{m+n}-S_m) and use independence.

- Exam use: Useful for superadditivity and concavity of large-deviation rates.

- Pitfall: The block thresholds must add to the desired total threshold.

- Tags: independence, sums, large-deviations

##### Superadditivity lemma

- ID: `durrett_ch2_superadditivity`

- Section: 2.7 Large Deviations

- Kind: lemma

- Summary: If a_{m+n} >= a_m+a_n, then a_n/n has a limit equal to its supremum in the extended real sense.

- Proof idea: Tile a long integer by blocks and control the leftover.

- Exam use: Used to prove existence of gamma(a).

- Pitfall: Signs matter: log probabilities are superadditive here, not subadditive.

- Tags: superadditivity, fekete, large-deviations

##### Concavity from block mixing

- ID: `durrett_ch2_concavity`

- Section: 2.7 Large Deviations

- Kind: proof-template

- Summary: Mixing blocks with thresholds a and b proves gamma(lambda a+(1-lambda)b) >= lambda gamma(a)+(1-lambda)gamma(b).

- Proof idea: Use rational lambda first with integer block lengths, then extend by monotonicity.

- Exam use: Exercise 2.7.2 pattern: concavity implies local Lipschitz regularity on the finite domain.

- Pitfall: The extension from rational to real lambda needs monotonicity or another continuity argument.

- Tags: concavity, block-mixing, large-deviations

##### Poisson large-deviation rate

- ID: `durrett_ch2_poisson_large_deviation`

- Section: 2.7 Large Deviations

- Kind: example

- Summary: For iid Poisson(1), P(S_n>=na) has exponent -a log a+a-1 for a>1.

- Proof idea: Use the Poisson mgf exp(e^theta-1) and optimize at theta=log a.

- Exam use: Exercise 2.7.3 pattern: compute Cramer rates by solving tilted mean equals a.

- Pitfall: The displayed formula is for upper tails a>1.

- Tags: poisson, cramer, rate-function

##### Moment-generating-function upper bounds

- ID: `durrett_ch2_mgf_bounds`

- Section: 2.7 Large Deviations

- Kind: technique

- Summary: Simple analytic inequalities for phi(theta) lead to usable Chernoff bounds even when the exact optimizer is not used.

- Proof idea: Bound log phi(theta), then optimize the quadratic or other simpler expression.

- Exam use: Exercise 2.7.4 pattern: cosh(theta)-1 <= beta theta^2 for theta<=1.

- Pitfall: The bound is only valid over the range where the analytic inequality was proved.

- Tags: mgf, chernoff, tail-bound

##### Subgaussian bound for fair coin sums

- ID: `durrett_ch2_subgaussian_coin_flips`

- Section: 2.7 Large Deviations

- Kind: example

- Summary: For Rademacher sums, bounding cosh(theta) by exp(beta theta^2) gives a Gaussian-type upper tail.

- Proof idea: Apply Chernoff and choose theta=a/(2 beta).

- Exam use: Gives a clean exponential estimate P(S_n>=an) <= exp(-n a^2/(4 beta)) for 0<=a<=1.

- Pitfall: This is a valid bound but not the sharp Cramer exponent.

- Tags: rademacher, subgaussian, chernoff

##### No positive mgf gives zero exponential rate

- ID: `durrett_ch2_heavy_tail_large_deviation`

- Section: 2.7 Large Deviations

- Kind: principle

- Summary: If all positive exponential moments are infinite, upper large deviations cannot have a strictly negative exponential rate.

- Proof idea: A negative rate would force exponentially bounded positive tails, creating a finite positive mgf.

- Exam use: Exercise 2.7.5 pattern: heavy tails make large deviations subexponential on the logarithmic n-scale.

- Pitfall: This conclusion concerns exponential rate only; probabilities may still tend to zero.

- Tags: heavy-tail, large-deviations, mgf

##### One big jump lower bound

- ID: `durrett_ch2_one_big_jump`

- Section: 2.7 Large Deviations

- Kind: proof-template

- Summary: For integrable mean-zero iid sums, P(S_n>=na) is at least asymptotically n P(X_1>=n(a+epsilon)).

- Proof idea: Require exactly one unusually large summand and use the weak law to keep the remaining sum above -n epsilon.

- Exam use: Exercise 2.7.6 pattern: lower-bound heavy-tail large deviations by a single summand.

- Pitfall: Integrability is used to ensure n P(X_1>cn)->0 and to apply the weak law.

- Tags: one-big-jump, heavy-tail, weak-law

##### Weak law of large numbers

- ID: `durrett_ch2_weak_law`

- Section: 2.2 Weak Laws of Large Numbers

- Kind: theorem

- Summary: For iid integrable variables with mean mu, S_n/n -> mu in probability.

- Proof idea: Use truncation plus Chebyshev, or invoke the finite-mean weak law.

- Exam use: Supports probability estimates for the contribution of all non-extreme summands.

- Pitfall: Weak convergence controls high-probability behavior, not pathwise eventual behavior.

- Tags: weak-law, iid, finite-mean

##### Tail probability normalization

- ID: `durrett_ch2_tail_probability`

- Section: 2.7 Large Deviations

- Kind: technique

- Summary: Compare rare-event probabilities to n times a single-tail probability when one large summand drives the event.

- Proof idea: Use independence, exclusion of multiple large jumps, and a law of large numbers for the remaining terms.

- Exam use: Useful in heavy-tail large-deviation lower bounds.

- Pitfall: The denominator must match the same threshold scale as the constructed big jump.

- Tags: tail-probability, normalization, heavy-tail

##### Borel-Cantelli lemmas

- ID: `durrett_ch2_borel_cantelli`

- Section: 2.3 Borel-Cantelli Lemmas

- Kind: theorem

- Summary: Summable event probabilities imply only finitely many occurrences; for independent events, divergent probability sums imply infinitely many occurrences.

- Proof idea: The first lemma uses a union bound on the tail union; the second uses independence to control the probability of no future occurrence.

- Exam use: A general retrieval alias for exercises that use either Borel-Cantelli direction.

- Pitfall: The divergent direction requires independence or a suitable substitute.

- Tags: borel-cantelli, almost-sure, limsup

##### Cramer theorem

- ID: `durrett_ch2_cramer_theorem`

- Section: 2.7 Large Deviations

- Kind: theorem

- Summary: For light-tailed iid sums, the upper-tail exponential decay rate is the negative Legendre transform of log E exp(theta X).

- Proof idea: Use Chernoff for the upper bound and exponential tilting for the matching lower bound.

- Exam use: A general retrieval alias for Cramer-rate computations such as the Poisson example.

- Pitfall: The theorem requires finiteness of the mgf near the optimizing tilt.

- Tags: cramer, large-deviations, rate-function

## Chapter 3

### Durrett Chapter 3 LLM Viki: Central Limit Theorems

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter3.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

#### Section Guides

##### 3.1 The De Moivre-Laplace Theorem

- Goal: Understand the normal limit first through exact binomial probabilities and Stirling asymptotics.

- Must master: Stirling formula, local binomial approximation, Riemann-sum normal limit, linear-deviation contrast

- Prelim angle: A concrete way to derive normal approximation and avoid using the CLT as a black box.

##### 3.2 Weak Convergence

- Goal: Use distributional convergence through continuity points, test functions, mapping theorems, and tightness.

- Must master: weak convergence definition, Portmanteau theorem, continuous mapping, tightness, Helly selection, Slutsky patterns

- Prelim angle: Most limit-theorem problems need these tools to move from transforms to events or transformed variables.

##### 3.3 Characteristic Functions

- Goal: Use Fourier transforms to identify laws, prove weak convergence, and extract moment expansions.

- Must master: characteristic functions, inversion, Levy continuity theorem, moment derivatives, standard transform table

- Prelim angle: High-yield method for CLT, Poisson convergence, random sums, and independence checks.

##### 3.4 Central Limit Theorems

- Goal: Prove normal limits for iid sequences and triangular arrays, and recognize rate and arithmetic examples.

- Must master: iid CLT, Lindeberg-Feller, Lyapunov condition, random index CLT, Berry-Esseen

- Prelim angle: The central computation theme of Chapter 3; many exam problems are variants with changed normalization or dependence.

##### 3.5 Local Limit Theorems

- Goal: Upgrade cumulative CLT statements to point-probability approximations using Fourier inversion.

- Must master: lattice span, local normal approximation, small-t/large-t split

- Prelim angle: Useful when the problem asks for exact mass asymptotics instead of only distributional convergence.

##### 3.6 Poisson Convergence

- Goal: Recognize and prove laws of small numbers for rare-event counts, with and without dependence.

- Must master: Bernoulli array theorem, total variation approximation, matching, occupancy

- Prelim angle: Common source of limit-distribution questions where the limit is Poisson rather than normal.

##### 3.7 Poisson Processes

- Goal: Move from rare-event counts to continuous-time counting processes, thinning, compounding, and conditioning.

- Must master: independent increments, compound Poisson, thinning, conditional order statistics

- Prelim angle: Connects Chapter 3 convergence tools with stochastic-process modeling.

##### 3.8 Stable Laws

- Goal: Understand nonnormal limits for heavy-tailed sums and the role of scaling, skewness, and centering.

- Must master: stable characteristic functions, domain of attraction, regular variation, convergence of types

- Prelim angle: A warning system for infinite-variance problems where sqrt(n) normalization is wrong.

##### 3.9 Infinitely Divisible Distributions

- Goal: See normal, Poisson, compound Poisson, and stable laws as members of one triangular-array limit family.

- Must master: infinite divisibility, Levy-Khinchin formula, Levy measure, Gaussian and jump components

- Prelim angle: Less often computational, but excellent for recognizing possible limits of infinitesimal arrays.

##### 3.10 Limit Theorems in R^d

- Goal: Extend weak convergence, characteristic functions, and CLT arguments to random vectors.

- Must master: multivariate weak convergence, multivariate characteristic functions, Cramer-Wold, multivariate CLT

- Prelim angle: Joint convergence questions usually reduce to projections and covariance calculations.

#### Knowledge Pieces

##### Stirling local binomial approximation

- ID: `durrett_ch3_stirling_local_binomial`

- Section: 3.1 The De Moivre-Laplace Theorem

- Kind: formula

- Summary: For a simple symmetric walk, P(S_{2n}=2k) is asymptotic to (pi n)^(-1/2) exp(-x^2/2) when 2k/sqrt(2n) tends to x.

- Proof idea: Insert Stirling's formula into the central binomial coefficient and use (1+c_n)^{a_n} limits.

- Exam use: Use as the prototype local normal approximation before invoking characteristic functions.

- Pitfall: The approximation is local and depends on the lattice parity of S_{2n}.

- Tags: stirling, binomial, local-normal

##### De Moivre-Laplace theorem

- ID: `durrett_ch3_demoivre_laplace`

- Section: 3.1 The De Moivre-Laplace Theorem

- Kind: theorem

- Summary: For a simple symmetric random walk, S_m/sqrt(m) converges in distribution to the standard normal law.

- Proof idea: Sum the local binomial approximation over lattice points and identify the resulting Riemann sum with the normal integral.

- Exam use: A concrete CLT model for coin flips, binomial normal approximation, and continuity-correction intuition.

- Pitfall: Do not forget the even/odd lattice issue; the theorem for all m follows after a small parity argument.

- Tags: clt, simple-random-walk, normal-approximation

##### Product exponential limit

- ID: `durrett_ch3_product_exponential_limit`

- Section: 3.1 The De Moivre-Laplace Theorem

- Kind: lemma

- Summary: If max_j |c_{j,n}| goes to 0, sum_j c_{j,n} tends to lambda, and the sums of absolute values are bounded, then product_j(1+c_{j,n}) tends to exp(lambda).

- Proof idea: Take logarithms, use log(1+x)=x+o(x) uniformly for small x, and control the total error by the absolute-sum bound.

- Exam use: Fast route for birthday, occupancy, and rare-event product limits.

- Pitfall: The maximum term condition is essential; a single large factor can break the exponential approximation.

- Tags: product-limit, rare-events, asymptotics

##### Stirling large-deviation patterns

- ID: `durrett_ch3_large_deviation_stirling_patterns`

- Section: 3.1 The De Moivre-Laplace Theorem

- Kind: example-pattern

- Summary: Stirling's formula also gives exponential rates for binomial and Poisson tails at linear deviations from the mean.

- Proof idea: Approximate the largest relevant mass and show nearby tail terms are geometrically controlled.

- Exam use: Useful when an exam asks for n^{-1} log P(S_n >= n a) before the full large-deviation theorem is available.

- Pitfall: Normal approximation is not valid on linear-deviation scales; use exponential rates instead.

- Tags: large-deviations, stirling, tail-asymptotics

##### Weak convergence definition

- ID: `durrett_ch3_weak_convergence_definition`

- Section: 3.2 Weak Convergence

- Kind: definition

- Summary: Distribution functions F_n converge weakly to F when F_n(x) tends to F(x) at every continuity point of F; random variables converge in distribution when their laws do.

- Proof idea: Continuity points are enough because distribution functions are right continuous and have at most countably many jumps.

- Exam use: This is the language used in CLT, Poisson approximation, stable limits, and multivariate limits.

- Pitfall: Convergence at discontinuity points of the limit is not required and can fail even for X+1/n tending to X.

- Tags: weak-convergence, distribution-functions, continuity-points

##### Waiting for rare events gives an exponential limit

- ID: `durrett_ch3_rare_geometric_exponential_limit`

- Section: 3.2.1 Examples

- Kind: example-pattern

- Summary: If X_p is geometric with success probability p, then p X_p converges in distribution to an exponential(1) random variable as p tends to 0.

- Proof idea: Use P(p X_p > x)=(1-p)^{floor(x/p)} and the exponential limit lemma.

- Exam use: Recognize geometric waiting times under rare-event scaling.

- Pitfall: The scale is p X_p, not X_p/p; the waiting time itself diverges.

- Tags: geometric, exponential-limit, rare-events

##### Birthday collision Rayleigh limit

- ID: `durrett_ch3_birthday_rayleigh_limit`

- Section: 3.2.1 Examples

- Kind: example-pattern

- Summary: For iid uniform draws from N boxes, the first collision time T_N satisfies P(T_N/sqrt(N)>x) tending to exp(-x^2/2).

- Proof idea: Write the no-collision probability as a product of terms 1-(m-1)/N and apply the product exponential limit.

- Exam use: A standard occupancy/collision scaling pattern.

- Pitfall: The natural scale is sqrt(N), not N, because collisions depend on pairs.

- Tags: birthday-problem, occupancy, rayleigh-tail

##### Scheffe theorem for densities

- ID: `durrett_ch3_scheffe_theorem`

- Section: 3.2.1 Examples

- Kind: theorem

- Summary: If probability densities f_n converge pointwise to a density f, then the corresponding probability measures converge in total variation, hence weakly.

- Proof idea: Use the identity integral |f_n-f| = 2 integral (f-f_n)^+ and dominated convergence.

- Exam use: Use when a limit distribution is easiest to prove through densities, such as central order statistics.

- Pitfall: Pointwise convergence of densities is stronger than weak convergence and is not necessary.

- Tags: scheffe, densities, total-variation

##### Quantile representation for weak convergence

- ID: `durrett_ch3_skorokhod_quantile_representation`

- Section: 3.2.2 Theory

- Kind: theorem

- Summary: If F_n converges weakly to F, one can construct random variables with these laws on (0,1) that converge almost surely.

- Proof idea: Use generalized inverse distribution functions and exclude the countable set of flat-level ambiguities.

- Exam use: Lets proof problems transfer weak convergence into almost sure convergence for bounded continuous mappings.

- Pitfall: The constructed variables need not be the original variables; this is a representation argument.

- Tags: quantile-transform, skorokhod, weak-convergence

##### Bounded continuous test function characterization

- ID: `durrett_ch3_bounded_continuous_test_functions`

- Section: 3.2.2 Theory

- Kind: theorem

- Summary: X_n converges in distribution to X iff E g(X_n) tends to E g(X) for every bounded continuous function g.

- Proof idea: One direction uses the almost-sure representation and bounded convergence; the converse approximates indicators of half-lines by continuous cutoffs.

- Exam use: The default way to define weak convergence on general topological spaces.

- Pitfall: Boundedness matters; unbounded continuous functions need extra tightness or uniform integrability.

- Tags: portmanteau, test-functions, bounded-continuous

##### Continuous mapping theorem

- ID: `durrett_ch3_continuous_mapping_theorem`

- Section: 3.2.2 Theory

- Kind: theorem

- Summary: If X_n converges in distribution to X and g is measurable with P(X in D_g)=0, then g(X_n) converges in distribution to g(X).

- Proof idea: Represent X_n and X almost surely, then apply pointwise continuity of g off its discontinuity set.

- Exam use: Use for Slutsky-type transformations, maxima maps, ratios away from zero, and normalization changes.

- Pitfall: A discontinuity with positive limit probability can invalidate the conclusion.

- Tags: continuous-mapping, weak-convergence, discontinuity-set

##### Portmanteau open-closed criteria

- ID: `durrett_ch3_portmanteau_open_closed`

- Section: 3.2.2 Theory

- Kind: theorem

- Summary: Weak convergence is equivalent to lower bounds on open sets, upper bounds on closed sets, and convergence on Borel sets whose boundary has limit probability zero.

- Proof idea: Use Fatou on indicators after almost-sure representation, then pass between open and closed sets by complements.

- Exam use: Use when events are not intervals but have negligible boundary under the limit.

- Pitfall: The direction of the inequalities is easy to reverse; open sets get liminf lower bounds and closed sets get limsup upper bounds.

- Tags: portmanteau, open-sets, closed-sets

##### Helly selection and tightness

- ID: `durrett_ch3_helly_selection_tightness`

- Section: 3.2.2 Theory

- Kind: theorem

- Summary: Every sequence of distribution functions has a vaguely convergent subsequence; subsequential limits are probability laws exactly when mass is tight.

- Proof idea: Use a diagonal subsequence over rational points and then repair right continuity; tightness prevents mass escaping to plus or minus infinity.

- Exam use: Core compactness tool for proving existence of subsequential distributional limits.

- Pitfall: Vague subsequential limits can lose mass, so Helly alone is not enough for weak convergence.

- Tags: helly, tightness, subsequences

##### Moment tightness criterion

- ID: `durrett_ch3_moment_tightness_criterion`

- Section: 3.2.2 Theory

- Kind: criterion

- Summary: If sup_n E phi(X_n) is finite for some nonnegative phi with phi(x) tending to infinity as |x| tends to infinity, then the laws of X_n are tight.

- Proof idea: Apply Markov's inequality to phi(X_n) outside large compact intervals.

- Exam use: Fast tightness check using bounded moments or coercive Lyapunov functions.

- Pitfall: A bounded first or second moment gives tightness, but tightness does not require moments.

- Tags: tightness, markov, moment-bound

##### Subsequence principle for weak convergence

- ID: `durrett_ch3_subsequence_principle_weak`

- Section: 3.2.2 Theory

- Kind: proof-template

- Summary: If every subsequence has a further subsequence converging weakly to the same law, then the full sequence converges weakly to that law.

- Proof idea: Use the topological subsequence criterion on real numbers F_n(x) at continuity points.

- Exam use: Useful for proving convergence after compactness/tightness arguments.

- Pitfall: The further subsequential limit must be uniquely identified; tightness only gives candidates.

- Tags: subsequence, weak-convergence, uniqueness

##### Convergence in probability implies weak convergence

- ID: `durrett_ch3_convergence_in_probability_to_distribution`

- Section: 3.2 Exercises and Consequences

- Kind: fact

- Summary: If X_n tends to X in probability, then X_n converges in distribution to X; if X_n converges in distribution to a constant c, then X_n tends to c in probability.

- Proof idea: Use inclusions between half-line events with epsilon buffers and continuity points, or use bounded continuous test functions.

- Exam use: Often used to replace negligible error terms in limit theorems.

- Pitfall: Weak convergence to a nonconstant random variable does not imply convergence in probability on the original space.

- Tags: convergence-in-probability, weak-convergence, constant-limit

##### Converging together and Slutsky patterns

- ID: `durrett_ch3_converging_together_slutsky`

- Section: 3.2 Exercises and Consequences

- Kind: proof-template

- Summary: If X_n converges in distribution to X and Y_n converges in distribution to a constant c, then X_n+Y_n, X_n Y_n, and X_n/Y_n (c not 0) converge to the corresponding transformed limits.

- Proof idea: Upgrade Y_n to convergence in probability, combine with X_n using tightness and continuous mapping.

- Exam use: Indispensable for replacing random normalizers by deterministic limits.

- Pitfall: The denominator case needs the limit constant away from zero.

- Tags: slutsky, converging-together, random-normalization

##### Characteristic function basics

- ID: `durrett_ch3_characteristic_function_definition`

- Section: 3.3.1 Definition, Inversion Formula

- Kind: definition

- Summary: The characteristic function of X is phi(t)=E exp(i t X); it is uniformly continuous, positive definite, satisfies phi(0)=1, and determines the distribution.

- Proof idea: Most properties follow from bounded convergence and algebra of complex exponentials.

- Exam use: Main transform language for CLT and distributional convergence.

- Pitfall: A pointwise limit of characteristic functions is a characteristic function only if it is continuous at zero.

- Tags: characteristic-functions, positive-definite, transforms

##### Characteristic functions multiply for independent sums

- ID: `durrett_ch3_cf_independent_sums`

- Section: 3.3.1 Definition, Inversion Formula

- Kind: theorem

- Summary: If X and Y are independent, the characteristic function of X+Y is phi_X(t) phi_Y(t).

- Proof idea: Factor E exp(i t X) exp(i t Y) by independence.

- Exam use: Turns sums of independent random variables into products and powers of transforms.

- Pitfall: The product rule requires independence; uncorrelated variables are not enough.

- Tags: independent-sums, characteristic-functions, convolution

##### Standard characteristic function table

- ID: `durrett_ch3_standard_characteristic_functions`

- Section: 3.3.1 Definition, Inversion Formula

- Kind: example-bank

- Summary: Coin flip: cos t; Poisson(lambda): exp(lambda(e^{it}-1)); normal(mu,sigma^2): exp(i mu t - sigma^2 t^2/2); uniform(a,b): (e^{itb}-e^{ita})/(it(b-a)); exponential(lambda): lambda/(lambda-it).

- Proof idea: Compute directly from sums or integrals, using independence and completing the square for normals.

- Exam use: Recognition table for prelim transform calculations.

- Pitfall: Check parameter conventions carefully, especially normal variance and exponential rate versus mean.

- Tags: cf-table, normal, poisson, exponential

##### Characteristic function inversion formula

- ID: `durrett_ch3_cf_inversion_formula`

- Section: 3.3.1 Definition, Inversion Formula

- Kind: theorem

- Summary: A distribution can be recovered from its characteristic function by integrating (exp(-ita)-exp(-itb))/(it) against phi(t) over symmetric intervals and taking limits at continuity endpoints.

- Proof idea: Apply Fubini to the Fourier integral of interval indicators and let the cutoff grow.

- Exam use: Use to prove uniqueness and to identify distributional limits from transforms.

- Pitfall: Endpoint atoms require care; inversion is cleanest for intervals whose endpoints have zero mass.

- Tags: inversion, fourier, uniqueness

##### Integrable characteristic function gives bounded density

- ID: `durrett_ch3_integrable_cf_density`

- Section: 3.3.1 Definition, Inversion Formula

- Kind: theorem

- Summary: If a characteristic function is integrable, the distribution has a bounded continuous density given by Fourier inversion.

- Proof idea: Use dominated convergence to invert the transform and verify that interval probabilities are integrals of the resulting function.

- Exam use: Shows stable or limiting laws have densities when their characteristic functions are integrable.

- Pitfall: Integrability of phi is sufficient, not necessary, for having a density.

- Tags: density, fourier-inversion, integrable-cf

##### Levy continuity theorem

- ID: `durrett_ch3_levy_continuity_theorem`

- Section: 3.3.2 Weak Convergence

- Kind: theorem

- Summary: Probability measures converge weakly iff their characteristic functions converge pointwise to a function continuous at zero, in which case the limit is the characteristic function of the weak limit.

- Proof idea: Use tightness plus inversion to identify subsequential limits; continuity at zero prevents mass loss.

- Exam use: The main engine for proving CLT, Poisson limits, stable limits, and multivariate limit theorems.

- Pitfall: Pointwise convergence to a discontinuous-at-zero function does not define a probability limit.

- Tags: levy-continuity, weak-convergence, characteristic-functions

##### Moments from characteristic function derivatives

- ID: `durrett_ch3_derivatives_moments`

- Section: 3.3.3 Moments and Derivatives

- Kind: theorem

- Summary: If E|X|^n is finite, then phi has n derivatives and phi^{(k)}(0)=i^k E X^k for k up to n.

- Proof idea: Differentiate under the expectation using domination by |X|^k.

- Exam use: Compute moments and build Taylor expansions for CLT proofs.

- Pitfall: Existence of a few derivatives at zero can be subtler than finite moments unless the theorem's hypotheses are met.

- Tags: moments, derivatives, taylor-expansion

##### Second-order characteristic function expansion

- ID: `durrett_ch3_second_order_cf_expansion`

- Section: 3.3.3 Moments and Derivatives

- Kind: formula

- Summary: If EX=0 and EX^2=sigma^2 is finite, then phi(t)=1-sigma^2 t^2/2+o(t^2) as t tends to zero.

- Proof idea: Use the Taylor expansion of exp(itX) and dominate the remainder through finite second moment.

- Exam use: This is the one-line input behind the iid CLT by characteristic functions.

- Pitfall: The expansion is local near zero; do not apply it at fixed nonzero t without scaling.

- Tags: second-moment, cf-expansion, clt

##### Polya criterion for characteristic functions

- ID: `durrett_ch3_polya_criterion`

- Section: 3.3.4 Polya's Criterion

- Kind: criterion

- Summary: A real, nonnegative, even, convex-on-positive-rays function with phi(0)=1 and phi(t) tending to 0 at infinity is a characteristic function.

- Proof idea: Approximate phi by polygonal functions that are mixtures of triangular characteristic functions and pass to a weak limit.

- Exam use: Useful for constructing stable-law examples such as exp(-|t|^alpha) for 0<alpha<2.

- Pitfall: The criterion is sufficient, not necessary; many characteristic functions are not nonnegative or convex.

- Tags: polya, construction, stable-laws

##### Moment problem and Carleman-type uniqueness

- ID: `durrett_ch3_moment_problem_carleman`

- Section: 3.3.5 The Moment Problem

- Kind: theorem

- Summary: Under suitable growth conditions on even moments, a distribution is determined by its moments.

- Proof idea: Use analytic control of the characteristic function or moment generating series near zero.

- Exam use: Helps decide when matching all moments identifies a law.

- Pitfall: Moment equality alone is not always enough; lognormal-type examples show nonuniqueness can occur.

- Tags: moment-problem, carleman, uniqueness

##### IID central limit theorem

- ID: `durrett_ch3_iid_clt`

- Section: 3.4.1 i.i.d. Sequences

- Kind: theorem

- Summary: If X_i are iid with mean mu and variance sigma^2 in (0,infinity), then (S_n-n mu)/(sigma sqrt(n)) converges in distribution to standard normal.

- Proof idea: Center and scale, raise the characteristic function at t/sqrt(n) to the nth power, and use the second-order expansion.

- Exam use: The central theorem for normal approximations and asymptotic distribution calculations.

- Pitfall: Finite nonzero variance is required for this form; infinite variance can lead to nonnormal stable limits.

- Tags: clt, iid, normal-limit

##### Normal approximation and continuity correction

- ID: `durrett_ch3_normal_approximation_continuity_correction`

- Section: 3.4.1 i.i.d. Sequences

- Kind: example-pattern

- Summary: For binomial or lattice sums, approximate probabilities by normal intervals and shift interval endpoints by half a lattice step for better accuracy.

- Proof idea: Apply the CLT to centered and scaled sums while accounting for the discrete histogram cell width.

- Exam use: Useful for coin-flip, dice, roulette, binomial, and Poisson approximations.

- Pitfall: The CLT gives large-n accuracy; small tails and lattice endpoints may need correction or sharper bounds.

- Tags: normal-approximation, binomial, continuity-correction

##### Lindeberg-Feller central limit theorem

- ID: `durrett_ch3_triangular_array_lindeberg_feller`

- Section: 3.4.2 Triangular Arrays

- Kind: theorem

- Summary: For independent mean-zero triangular arrays with total variance tending to 1, the row sum converges to standard normal iff the Lindeberg condition holds.

- Proof idea: Use characteristic functions, compare products with exponentials, and show large terms are negligible exactly under Lindeberg.

- Exam use: The main CLT for non-identically distributed arrays.

- Pitfall: The condition is row-wise; do not replace it by iid assumptions unless the array is built that way.

- Tags: lindeberg-feller, triangular-array, clt

##### Lyapunov condition implies Lindeberg

- ID: `durrett_ch3_lyapunov_condition`

- Section: 3.4.2 Triangular Arrays

- Kind: criterion

- Summary: If a triangular array has normalized (2+delta)-moments whose row sum tends to zero, then the Lindeberg condition holds.

- Proof idea: Bound x^2 1{|x|>epsilon} by epsilon^{-delta}|x|^{2+delta}.

- Exam use: Quick sufficient check for triangular-array CLTs.

- Pitfall: Lyapunov is stronger than Lindeberg; failure of Lyapunov does not rule out a CLT.

- Tags: lyapunov, lindeberg, moment-condition

##### Random index CLT

- ID: `durrett_ch3_random_index_clt`

- Section: 3.4.1 i.i.d. Sequences

- Kind: exercise-pattern

- Summary: If N_t/a(t) tends to 1 in probability and iid centered finite-variance sums satisfy the CLT, then S_{N_t}/sqrt(a(t)) has the same normal limit.

- Proof idea: Use maximal inequalities to show the difference between S_{N_t} and S_{a(t)} is negligible on high-probability index windows.

- Exam use: Useful for renewal CLTs and random-sample-size problems.

- Pitfall: The random index must be close on the scale needed by the partial-sum fluctuations.

- Tags: random-index, clt, renewal

##### Erdos-Kac central limit theorem

- ID: `durrett_ch3_erdos_kac`

- Section: 3.4.3 Prime Divisors

- Kind: theorem

- Summary: The number of distinct prime divisors of a uniformly chosen integer up to n, after centering and scaling by log log n, converges to the standard normal law.

- Proof idea: Approximate divisibility by small primes with nearly independent Bernoulli variables and control the remaining error.

- Exam use: A landmark example where arithmetic statistics obey a CLT.

- Pitfall: The variance scale is log log n, not log n.

- Tags: erdos-kac, number-theory, bernoulli-approximation

##### Berry-Esseen rate

- ID: `durrett_ch3_berry_esseen`

- Section: 3.4.4 Rates of Convergence

- Kind: theorem

- Summary: For iid centered variables with finite third absolute moment and variance one, the normal approximation error in Kolmogorov distance is O(E|X|^3/sqrt(n)).

- Proof idea: Compare characteristic functions through smoothing inequalities and bound the third-order Taylor remainder.

- Exam use: Use when a problem asks for an explicit CLT error rate.

- Pitfall: Finite variance alone gives convergence but not this rate.

- Tags: berry-esseen, rates, kolmogorov-distance

##### Lattice span from characteristic functions

- ID: `durrett_ch3_lattice_span`

- Section: 3.5 Local Limit Theorems

- Kind: criterion

- Summary: For a lattice distribution, the set of t with |phi(t)|=1 encodes the lattice spacing; otherwise |phi(t)|<1 away from zero on compact intervals.

- Proof idea: Equality in the triangle inequality forces exp(itX) to be almost surely constant.

- Exam use: Key diagnostic for local limit theorems.

- Pitfall: Local limits differ in lattice and nonlattice cases; the span matters.

- Tags: lattice, characteristic-functions, local-limit

##### Local limit theorem

- ID: `durrett_ch3_local_limit_theorem`

- Section: 3.5 Local Limit Theorems

- Kind: theorem

- Summary: Under suitable lattice hypotheses and finite variance, point probabilities of centered sums are approximated by the normal density times the lattice spacing over sqrt(n).

- Proof idea: Use Fourier inversion and split the integral into a small-t CLT region and a large-t region controlled by |phi(t)|<1.

- Exam use: Use when approximating exact probabilities, not just cumulative probabilities.

- Pitfall: The ordinary CLT does not imply local probability estimates by itself.

- Tags: local-limit, lattice, normal-density

##### Poisson convergence for rare Bernoulli arrays

- ID: `durrett_ch3_poisson_triangular_array`

- Section: 3.6.1 The Basic Limit Theorem

- Kind: theorem

- Summary: For independent Bernoulli variables in row n, if the maximum success probability tends to zero and the sum of success probabilities tends to lambda, then the row sum converges to Poisson(lambda).

- Proof idea: Multiply Bernoulli characteristic functions and use log(1+z)=z+o(z) uniformly because all probabilities are small.

- Exam use: The standard law of small numbers for rare-event counts.

- Pitfall: The largest individual probability must vanish; total mean convergence alone is not enough.

- Tags: poisson-convergence, law-of-small-numbers, bernoulli-array

##### Total variation Poisson approximation

- ID: `durrett_ch3_total_variation_poisson_approximation`

- Section: 3.6.1 The Basic Limit Theorem

- Kind: theorem

- Summary: A sum of independent Bernoulli variables is close in total variation to a Poisson variable with matching mean when the sum of squared success probabilities is small.

- Proof idea: Compare each Bernoulli law with its Poisson approximation, then use product and convolution contraction inequalities.

- Exam use: Gives quantitative Poisson approximation for rare counts.

- Pitfall: Total variation is stronger than weak convergence; the error bound depends on small individual probabilities.

- Tags: total-variation, poisson-approximation, rare-events

##### Matching fixed points converge to Poisson

- ID: `durrett_ch3_matching_fixed_points`

- Section: 3.6.2 Two Examples with Dependence

- Kind: example-pattern

- Summary: The number of fixed points in a uniform random permutation converges to Poisson(1).

- Proof idea: Compute factorial moments or use inclusion-exclusion; dependence is weak enough that rare fixed-point events mimic independent Bernoulli events.

- Exam use: Classic dependent rare-event Poisson limit.

- Pitfall: The indicators are not independent, so the basic Bernoulli-array theorem does not apply directly.

- Tags: matching, fixed-points, poisson-limit

##### Occupancy empty-box Poisson limit

- ID: `durrett_ch3_occupancy_empty_boxes`

- Section: 3.6.2 Two Examples with Dependence

- Kind: example-pattern

- Summary: When r balls are thrown into n boxes and n exp(-r/n) tends to lambda, the number of empty boxes converges to Poisson(lambda).

- Proof idea: Use inclusion-exclusion or Poissonization to handle dependence among empty-box indicators.

- Exam use: Appears in coupon collector and hashing problems.

- Pitfall: Empty-box events are dependent; independence heuristics need justification.

- Tags: occupancy, empty-boxes, poisson-limit

##### Poisson process from independent increments

- ID: `durrett_ch3_poisson_process_increments`

- Section: 3.7 Poisson Processes

- Kind: theorem

- Summary: A counting process with stationary independent increments, no multiple jumps in small intervals, and jump probability asymptotic to lambda h has N(0,t) distributed as Poisson(lambda t).

- Proof idea: Partition [0,t] into many small intervals and apply Poisson convergence to the rare jump indicators.

- Exam use: Foundation for continuous-time rare-event models.

- Pitfall: The small-interval multiple-jump condition is needed to reduce counts to Bernoulli indicators.

- Tags: poisson-process, independent-increments, counting-process

##### Compound Poisson process

- ID: `durrett_ch3_compound_poisson`

- Section: 3.7.1 Compound Poisson Processes

- Kind: construction

- Summary: If N is a Poisson process and Y_i are iid jumps independent of N, then sum_{i<=N(t)} Y_i is a compound Poisson process with characteristic function exp(lambda t (E exp(i theta Y)-1)).

- Proof idea: Condition on N(t) and use the iid product rule for characteristic functions.

- Exam use: Models random sums and jump processes with nonunit jump sizes.

- Pitfall: Do not confuse the rate of arrivals with the distribution of jump sizes.

- Tags: compound-poisson, random-sum, jump-process

##### Thinning of a Poisson process

- ID: `durrett_ch3_poisson_thinning`

- Section: 3.7.2 Thinning

- Kind: theorem

- Summary: If each point of a rate lambda Poisson process is independently assigned a type j with probability p_j, then the type-specific counting processes are independent Poisson processes with rates lambda p_j.

- Proof idea: Condition on the total count, use multinomial splitting, and identify the joint generating or characteristic function.

- Exam use: Use for marked processes, occupancy via Poissonization, and splitting arrivals into classes.

- Pitfall: Independence of the marks is essential for independent thinned processes.

- Tags: thinning, marked-poisson, independent-poisson

##### Poisson arrivals conditional on count are order statistics

- ID: `durrett_ch3_poisson_order_statistics`

- Section: 3.7.3 Conditioning

- Kind: theorem

- Summary: Given N(t)=n in a homogeneous Poisson process, the arrival times in [0,t] have the same joint distribution as the order statistics of n iid uniform(0,t) variables.

- Proof idea: Use the joint density of exponential interarrival times restricted to total arrival time below t and no next arrival before t.

- Exam use: Turns Poisson-process conditioning questions into uniform order-statistic problems.

- Pitfall: This is conditional on the count; unconditionally the arrival times are not a fixed-size sample.

- Tags: poisson-process, conditioning, order-statistics

##### Stable law domain of attraction

- ID: `durrett_ch3_stable_law_domain_attraction`

- Section: 3.8 Stable Laws

- Kind: theorem

- Summary: Heavy-tailed iid sums with regularly varying tails of index alpha in (0,2) converge after n^{1/alpha}-type scaling and suitable centering to an alpha-stable law.

- Proof idea: Use triangular-array convergence of small jumps plus Poisson behavior of large jumps encoded through characteristic functions.

- Exam use: Explains nonnormal limits when variance is infinite.

- Pitfall: Centering depends on alpha and tail balance; do not reuse finite-variance CLT normalization.

- Tags: stable-laws, heavy-tails, domain-of-attraction

##### Stable characteristic exponent

- ID: `durrett_ch3_stable_characteristic_exponent`

- Section: 3.8 Stable Laws

- Kind: formula

- Summary: Stable laws have characteristic functions with exponent governed by alpha, scale, skewness, and centering parameters; symmetric stable laws have exp(-c |t|^alpha).

- Proof idea: Derive from the limiting Levy measure or from the scaling property of sums.

- Exam use: Recognition tool for identifying stable limits from characteristic functions.

- Pitfall: The alpha=1 case has special logarithmic centering behavior in nonsymmetric cases.

- Tags: stable-laws, characteristic-functions, heavy-tails

##### Convergence of types theorem

- ID: `durrett_ch3_convergence_of_types`

- Section: 3.8 Stable Laws

- Kind: theorem

- Summary: If a_n X_n+b_n converges to a nondegenerate limit and c_n X_n+d_n converges to another nondegenerate limit, then c_n/a_n and d_n-b_n c_n/a_n have limits linking the two laws by affine transformation.

- Proof idea: Use tightness and uniqueness of subsequential affine normalizations.

- Exam use: Useful for proving uniqueness of scaling and centering in stable-limit problems.

- Pitfall: The limit must be nondegenerate; constants allow pathological normalization changes.

- Tags: convergence-of-types, normalization, stable-laws

##### Infinitely divisible distributions

- ID: `durrett_ch3_infinitely_divisible_definition`

- Section: 3.9 Infinitely Divisible Distributions

- Kind: definition

- Summary: A distribution is infinitely divisible if for every n it can be represented as the law of a sum of n iid random variables.

- Proof idea: Limits of row sums of infinitesimal triangular arrays have this divisibility because each row can be split into many small independent pieces.

- Exam use: Normal, Poisson, compound Poisson, and stable laws are key examples.

- Pitfall: Not every distribution is infinitely divisible; bounded nonconstant laws are not.

- Tags: infinitely-divisible, triangular-arrays, limit-laws

##### Levy-Khinchin representation

- ID: `durrett_ch3_levy_khinchin`

- Section: 3.9 Infinitely Divisible Distributions

- Kind: theorem

- Summary: Characteristic functions of infinitely divisible laws have an exponent decomposed into drift, Gaussian variance, and an integral term governed by a Levy measure.

- Proof idea: Analyze limits of triangular-array characteristic exponents and separate small Gaussian fluctuations from jumps.

- Exam use: The master formula unifying normal, Poisson, compound Poisson, and stable laws.

- Pitfall: The Levy measure is not a probability measure; it controls jump intensity and must satisfy an integrability condition near zero.

- Tags: levy-khinchin, infinitely-divisible, levy-measure

##### Multivariate weak convergence

- ID: `durrett_ch3_multivariate_weak_convergence`

- Section: 3.10 Limit Theorems in R^d

- Kind: definition

- Summary: Weak convergence in R^d can be defined through bounded continuous test functions, rectangle distribution functions at continuity points, or probability convergence on continuity sets.

- Proof idea: Extend one-dimensional portmanteau and tightness arguments using rectangles that generate the Borel sigma-field.

- Exam use: Needed for joint convergence, random vectors, and multivariate CLT.

- Pitfall: Coordinatewise convergence alone does not imply joint convergence unless dependence is controlled.

- Tags: multivariate, weak-convergence, random-vectors

##### Multivariate characteristic function convergence

- ID: `durrett_ch3_multivariate_cf_convergence`

- Section: 3.10 Limit Theorems in R^d

- Kind: theorem

- Summary: Random vectors converge in distribution iff their multivariate characteristic functions converge pointwise to a function continuous at the origin.

- Proof idea: Use multidimensional inversion and tightness, paralleling the one-dimensional Levy continuity theorem.

- Exam use: Primary method for proving joint limit theorems.

- Pitfall: Checking only marginal characteristic functions misses dependence; the full vector transform is needed.

- Tags: multivariate-cf, levy-continuity, joint-convergence

##### Cramer-Wold device

- ID: `durrett_ch3_cramer_wold`

- Section: 3.10 Limit Theorems in R^d

- Kind: theorem

- Summary: A sufficient and standard condition for X_n in R^d to converge to X is that theta dot X_n converges in distribution to theta dot X for every theta in R^d.

- Proof idea: Linear projections determine the multivariate characteristic function by phi_X(theta)=E exp(i theta dot X).

- Exam use: Turns multivariate convergence into one-dimensional convergence problems.

- Pitfall: All directions theta are needed; finitely many coordinate projections are not enough.

- Tags: cramer-wold, projections, joint-convergence

##### Central limit theorem in R^d

- ID: `durrett_ch3_multivariate_clt`

- Section: 3.10 Limit Theorems in R^d

- Kind: theorem

- Summary: For iid random vectors with mean vector m and covariance matrix Sigma, n^{-1/2} sum (X_i-m) converges to a multivariate normal with covariance Sigma.

- Proof idea: Apply the one-dimensional CLT to theta dot X_i for every theta and then use Cramer-Wold.

- Exam use: Use for joint asymptotic normality and random-walk scaling in higher dimensions.

- Pitfall: A singular covariance matrix still gives a valid degenerate multivariate normal limit.

- Tags: multivariate-clt, normal-vector, covariance

#### Exercise Viki Layer

The solved Chapter 3 exercises have a companion retrieval layer:

- `chapter3_exercise_records.jsonl`: 88 solved exercise records with question, solution, knowledge used, method tags, and new-knowledge IDs.
- `chapter3_exercise_method_cards.jsonl`: 10 section-level exercise method cards.
- `chapter3_exercise_new_knowledge.jsonl`: 40 reusable proof/calculation templates extracted from the solved exercises.
- `chapter3_exercise_method_flashcards.tsv`: flashcards for the method cards and new exercise-derived knowledge.
- `chapter3_exercise_viki.md`: human-readable overview of the exercise Viki layer.

### Chapter 3 Exercise Viki

#### Chapter 3 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter3/Chapter3Exercises.tex`
Source PDF: `Probability/Exercises/Chapter3/Chapter3Exercises.pdf`

This dataset turns the solved Chapter 3 exercises into retrieval-ready records, reusable method cards, and exercise-derived knowledge pieces.

##### Files

- `chapter3_exercise_records.jsonl`: one record per solved exercise, including question, solution, knowledge used, and method tags.
- `chapter3_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter3_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter3_exercise_method_flashcards.tsv`: flashcard import file for method and new-knowledge cards.
- `chapter3_exercise_viki.md`: human-readable overview.

##### Section Method Cards

###### 3.1 - De Moivre-Laplace theorem, Stirling asymptotics, and binomial normal approximation

Solved exercise records: 4

Use Stirling's formula and product-log expansions to turn exact binomial or rare-event probabilities into normal or exponential limits.

Tags: stirling, binomial, product-limit, normal-approximation

Reusable knowledge: exercise_ch3_stirling_binomial_ratio_method, exercise_ch3_product_to_exponential_method, exercise_ch3_linear_deviation_not_clt

###### 3.2 - Weak convergence, Portmanteau criteria, tightness, and continuous mapping

Solved exercise records: 17

Translate weak convergence into CDF continuity-point checks, bounded continuous test functions, open/closed set bounds, tightness, and continuous mappings.

Tags: weak-convergence, portmanteau, tightness, continuous-mapping, slutsky

Reusable knowledge: exercise_ch3_buffer_events_for_weak_convergence, exercise_ch3_subsequence_principle_for_limits, exercise_ch3_tightness_by_tail_or_moment_bound, exercise_ch3_converging_together_slutsky_template

###### 3.3 - Characteristic functions, inversion, moments, independence, and Levy continuity

Solved exercise records: 25

Identify distributions and limits through characteristic functions; use transform tables, Taylor expansions at zero, inversion, and factorization.

Tags: characteristic-functions, levy-continuity, moments, inversion, independence

Reusable knowledge: exercise_ch3_cf_table_matching, exercise_ch3_cf_taylor_moment_extraction, exercise_ch3_cf_factorization_independence, exercise_ch3_inversion_for_lattice_or_density

###### 3.4 - Central limit theorems, triangular arrays, Lindeberg, and normal approximations

Solved exercise records: 13

Choose the correct normalization, verify Lindeberg or Lyapunov conditions, and reduce random-index or triangular-array sums to known CLT forms.

Tags: clt, lindeberg, lyapunov, triangular-array, random-sums

Reusable knowledge: exercise_ch3_lindeberg_truncation_check, exercise_ch3_lyapunov_shortcut, exercise_ch3_random_index_clt_template, exercise_ch3_poisson_or_multinomial_clt_scaling

###### 3.5 - Local limit theorems and lattice-level normal approximation

Solved exercise records: 0

Use local limit theorem thinking when a problem asks for point probabilities or lattice-scale approximations rather than only distributional convergence.

Tags: local-limit, lattice, point-probability, normal-density

Reusable knowledge: exercise_ch3_local_limit_vs_global_clt, exercise_ch3_lattice_span_check

###### 3.6 - Total variation, couplings, and maximal coupling construction

Solved exercise records: 1

Prove total variation bounds by coupling, and prove sharpness by constructing a maximal coupling from the common mass of two measures.

Tags: coupling, total-variation, maximal-coupling, discrete-measures

Reusable knowledge: exercise_ch3_coupling_bounds_total_variation, exercise_ch3_maximal_coupling_common_mass

###### 3.7 - Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings

Solved exercise records: 9

Exploit exponential survival functions, Poisson thinning/splitting, and Dirichlet uniform spacings to solve process and occupancy limits.

Tags: poisson-process, exponential, thinning, splitting, uniform-spacings

Reusable knowledge: exercise_ch3_memoryless_survival_equation, exercise_ch3_competing_exponentials, exercise_ch3_poisson_thinning_for_infinite_server_queue, exercise_ch3_poisson_splitting_occupancy, exercise_ch3_dirichlet_uniform_spacings, exercise_ch3_extreme_spacing_second_moment

###### 3.8 - Stable laws, heavy tails, positive stable laws, and subordination

Solved exercise records: 7

Read stable-law questions through scaling, regular variation, tail integrals, Laplace transforms, and conditioning on positive stable subordinators.

Tags: stable-laws, heavy-tails, regular-variation, laplace-transform, subordination

Reusable knowledge: exercise_ch3_stable_no_centering_alpha_less_than_one, exercise_ch3_borderline_normal_log_correction, exercise_ch3_stable_fractional_moment_tail_test, exercise_ch3_positive_stable_laplace_functional_equation, exercise_ch3_stable_subordination_product_rule

###### 3.9 - Infinitely divisible distributions and Levy measures

Solved exercise records: 4

Use convolution roots, support diameter, symmetrized characteristic functions, and Levy-Khinchin exponent matching for infinite divisibility problems.

Tags: infinite-divisibility, gamma, levy-khinchin, characteristic-functions, support

Reusable knowledge: exercise_ch3_gamma_shape_splitting, exercise_ch3_bounded_infinitely_divisible_degenerate, exercise_ch3_infinitely_divisible_cf_nonvanishing, exercise_ch3_levy_measure_by_exponent_matching

###### 3.10 - Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws

Solved exercise records: 8

Recover marginals by sending coordinates to infinity, build joint laws with copulas, and prove independence or normality by multivariate characteristic functions.

Tags: multivariate, marginals, copula, joint-characteristic-function, multivariate-normal

Reusable knowledge: exercise_ch3_marginals_from_joint_cdf, exercise_ch3_fgm_copula_density_check, exercise_ch3_mixed_partial_recovers_density, exercise_ch3_joint_cf_independence_factorization, exercise_ch3_multivariate_normal_diagonal_covariance, exercise_ch3_cramer_wold_normal_identification

##### Exercise Records

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

##### New Exercise-Derived Knowledge

###### Stirling method for binomial ratios

- ID: `exercise_ch3_stirling_binomial_ratio_method`
- Kind: calculation-template
- Summary: Insert Stirling's formula into factorial probabilities, simplify the polynomial prefactor, and exponentiate logarithmic expansions.
- Use case: Exercises in Section 3.1 involving De Moivre-Laplace or large binomial probabilities.
- Tags: stirling, binomial, asymptotics

###### Convert rare-event products to exponentials

- ID: `exercise_ch3_product_to_exponential_method`
- Kind: limit-template
- Summary: For products of factors 1+a_{n,k}, take logs and use log(1+x)=x+o(x) when the maximum factor is small.
- Use case: Birthday, occupancy, no-collision, and geometric waiting-time limits.
- Tags: product-limit, rare-events, log-expansion

###### Linear deviations require exponential-rate estimates

- ID: `exercise_ch3_linear_deviation_not_clt`
- Kind: warning
- Summary: When deviations are of order n rather than sqrt(n), normal approximation is usually wrong; use Stirling or large-deviation rates.
- Use case: Binomial or random-walk tail exercises before the large-deviation chapter.
- Tags: large-deviation, normal-approximation, scale

###### Buffer events for weak convergence

- ID: `exercise_ch3_buffer_events_for_weak_convergence`
- Kind: proof-template
- Summary: Compare events such as {X_n <= x} with {X <= x +/- epsilon} to pass from convergence in probability to weak convergence.
- Use case: Exercises proving convergence in probability implies distributional convergence or converging-together results.
- Tags: weak-convergence, epsilon-buffer, cdf

###### Subsequence principle for identifying limits

- ID: `exercise_ch3_subsequence_principle_for_limits`
- Kind: proof-template
- Summary: Show every subsequence has a further subsequence with the same limit; then the original sequence converges.
- Use case: Tightness and uniqueness arguments in weak convergence exercises.
- Tags: subsequence, tightness, uniqueness

###### Tightness from tails or coercive moments

- ID: `exercise_ch3_tightness_by_tail_or_moment_bound`
- Kind: criterion
- Summary: Control sup_n P(|X_n|>K) directly or use Markov's inequality on a function growing to infinity.
- Use case: Weak convergence compactness exercises.
- Tags: tightness, markov, moment-bound

###### Converging together and Slutsky template

- ID: `exercise_ch3_converging_together_slutsky_template`
- Kind: proof-template
- Summary: If a main term has a distributional limit and the error goes to zero in probability, use tightness and buffer events to keep the same limit.
- Use case: Exercises where a statistic is approximated by a simpler statistic.
- Tags: slutsky, negligible-error, weak-convergence

###### Characteristic-function table matching

- ID: `exercise_ch3_cf_table_matching`
- Kind: calculation-template
- Summary: Recognize transforms such as normal, Cauchy, gamma, Poisson, and uniform; then invoke uniqueness.
- Use case: Distribution identification and transform inversion exercises in Section 3.3.
- Tags: characteristic-functions, transform-table, uniqueness

###### Extract moments from characteristic-function Taylor terms

- ID: `exercise_ch3_cf_taylor_moment_extraction`
- Kind: calculation-template
- Summary: Differentiate the characteristic function at zero or compare its Taylor expansion with 1+it EX - t^2 E X^2/2 + ... .
- Use case: Moment and variance calculations from transforms.
- Tags: moments, taylor-expansion, characteristic-functions

###### Independence through characteristic-function factorization

- ID: `exercise_ch3_cf_factorization_independence`
- Kind: proof-template
- Summary: A joint characteristic function that factors into marginal characteristic functions identifies the product law.
- Use case: Exercises proving independence from transforms.
- Tags: independence, joint-law, characteristic-functions

###### Use inversion to recover probabilities or densities

- ID: `exercise_ch3_inversion_for_lattice_or_density`
- Kind: calculation-template
- Summary: Apply the inversion formula in the form appropriate to densities or lattice probabilities, checking integrability when needed.
- Use case: Characteristic-function inversion exercises.
- Tags: inversion, density, lattice

###### Lindeberg check by truncation

- ID: `exercise_ch3_lindeberg_truncation_check`
- Kind: proof-template
- Summary: Bound the contribution of terms exceeding epsilon times the row standard deviation; bounded or uniformly small terms often make the condition immediate.
- Use case: Triangular-array CLT exercises.
- Tags: lindeberg, triangular-array, truncation

###### Lyapunov condition as a shortcut to Lindeberg

- ID: `exercise_ch3_lyapunov_shortcut`
- Kind: criterion
- Summary: Verify a higher-moment bound divided by the row variance scale; Lyapunov implies Lindeberg.
- Use case: CLT exercises with available third or higher moments.
- Tags: lyapunov, clt, moments

###### Random-index CLT template

- ID: `exercise_ch3_random_index_clt_template`
- Kind: proof-template
- Summary: Condition on the random index or compare it to a deterministic equivalent, then use Slutsky once the index ratio converges.
- Use case: Random sums and stopped-sum CLT exercises.
- Tags: random-index, clt, slutsky

###### Poisson and multinomial CLT scaling

- ID: `exercise_ch3_poisson_or_multinomial_clt_scaling`
- Kind: calculation-template
- Summary: Center counts by their means and scale by square roots of variances; dependence in multinomial vectors appears through covariance constraints.
- Use case: Occupancy, count-vector, and Poisson approximation CLT exercises.
- Tags: poisson, multinomial, normal-approximation

###### Local limit versus global CLT

- ID: `exercise_ch3_local_limit_vs_global_clt`
- Kind: warning
- Summary: The CLT controls interval probabilities, while a local limit theorem controls individual lattice probabilities at the normal-density scale.
- Use case: Point probability approximations in Section 3.5.
- Tags: local-limit, clt, lattice

###### Check lattice span before using a local limit theorem

- ID: `exercise_ch3_lattice_span_check`
- Kind: warning
- Summary: For lattice variables, the correct local approximation includes the span and only applies on reachable lattice points.
- Use case: Local normal approximations for sums of integer-valued variables.
- Tags: lattice, span, local-limit

###### Any coupling bounds total variation

- ID: `exercise_ch3_coupling_bounds_total_variation`
- Kind: proof-template
- Summary: For every event A, |P(X in A)-P(Y in A)| is bounded by P(X != Y), so total variation is no larger than mismatch probability.
- Use case: Exercise 3.6.1 and coupling estimates.
- Tags: coupling, total-variation, mismatch

###### Maximal coupling by common mass

- ID: `exercise_ch3_maximal_coupling_common_mass`
- Kind: construction-template
- Summary: Couple two discrete laws by first sampling from their overlap min(mu,nu), then sample residuals on disjoint supports.
- Use case: Sharp total variation coupling results.
- Tags: maximal-coupling, common-mass, discrete-law

###### Memoryless survival equation

- ID: `exercise_ch3_memoryless_survival_equation`
- Kind: proof-template
- Summary: The lack-of-memory property gives G(s+t)=G(s)G(t); monotonicity and right-continuity force G(t)=exp(-lambda t).
- Use case: Exercise 3.7.1 and exponential waiting-time characterization.
- Tags: memoryless, exponential, survival-function

###### Competing exponentials race rule

- ID: `exercise_ch3_competing_exponentials`
- Kind: calculation-template
- Summary: The minimum of independent exponentials has rate equal to the sum of rates, and the winning index has probability proportional to its rate.
- Use case: Exercises 3.7.2 and 3.7.3.
- Tags: exponential, minimum, race

###### Infinite-server queue by Poisson thinning

- ID: `exercise_ch3_poisson_thinning_for_infinite_server_queue`
- Kind: calculation-template
- Summary: Calls of age r survive with probability 1-G(r); thinning and superposition give a Poisson number in service with mean lambda integral survival.
- Use case: Exercise 3.7.4.
- Tags: poisson-thinning, queue, tail-integral

###### Poisson splitting for occupancy

- ID: `exercise_ch3_poisson_splitting_occupancy`
- Kind: calculation-template
- Summary: A Poisson number of independent categorized observations splits into independent Poisson counts in each category.
- Use case: Exercise 3.7.5 and birthday/occupancy computations.
- Tags: poisson-splitting, occupancy, independence

###### Uniform spacings are Dirichlet

- ID: `exercise_ch3_dirichlet_uniform_spacings`
- Kind: distribution-fact
- Summary: The gaps between ordered uniform points, including endpoints, are exchangeable Dirichlet(1,...,1) spacings.
- Use case: Exercises 3.7.7 through 3.7.9.
- Tags: uniform-order-statistics, spacings, dirichlet

###### Extreme spacings by first and second moments

- ID: `exercise_ch3_extreme_spacing_second_moment`
- Kind: proof-template
- Summary: Count gaps above a threshold, compute one- and two-gap probabilities from simplex volumes, and use variance control.
- Use case: Largest and smallest uniform spacing limits.
- Tags: extreme-spacing, second-moment, simplex-volume

###### No centering for alpha less than one stable limits

- ID: `exercise_ch3_stable_no_centering_alpha_less_than_one`
- Kind: stable-law-fact
- Summary: For alpha<1, small jumps are summable in absolute value under the Levy measure, so the stable limit needs no compensating centering.
- Use case: Exercises 3.8.1, 3.8.3, and 3.8.5.
- Tags: stable-laws, centering, alpha-less-than-one

###### Borderline normal attraction has sqrt(n log n) scale

- ID: `exercise_ch3_borderline_normal_log_correction`
- Kind: limit-template
- Summary: A symmetric variable with tail P(|Z|>x) like x^{-2} has infinite variance but still lies in the normal domain with a logarithmic variance correction.
- Use case: Exercise 3.8.2 with p=1/2.
- Tags: normal-attraction, infinite-variance, log-correction

###### Stable fractional moment and tail test

- ID: `exercise_ch3_stable_fractional_moment_tail_test`
- Kind: calculation-template
- Summary: Use the integral representation of E|X|^p through 1-Re phi(t) to get finiteness for p<alpha and tail lower bounds to show E|X|^alpha diverges.
- Use case: Exercise 3.8.4.
- Tags: stable-laws, fractional-moments, tails

###### Positive stable Laplace functional equation

- ID: `exercise_ch3_positive_stable_laplace_functional_equation`
- Kind: proof-template
- Summary: Stability gives psi(lambda)^n=psi(n^{1/alpha}lambda); continuity turns this into psi(lambda)=exp(-c lambda^alpha).
- Use case: Exercise 3.8.6.
- Tags: positive-stable, laplace-transform, functional-equation

###### Stable subordination product rule

- ID: `exercise_ch3_stable_subordination_product_rule`
- Kind: calculation-template
- Summary: Condition on a positive beta-stable Y: E exp(it X Y^{1/alpha}) becomes the Laplace transform of Y at c|t|^alpha, giving index alpha beta.
- Use case: Exercise 3.8.7 and normal-ratio Cauchy derivations.
- Tags: subordination, stable-laws, cauchy

###### Gamma infinite divisibility by shape splitting

- ID: `exercise_ch3_gamma_shape_splitting`
- Kind: calculation-template
- Summary: A Gamma(a,lambda) characteristic function is the nth power of the Gamma(a/n,lambda) characteristic function.
- Use case: Exercise 3.9.1.
- Tags: gamma, infinite-divisibility, convolution

###### Bounded infinitely divisible laws are degenerate

- ID: `exercise_ch3_bounded_infinitely_divisible_degenerate`
- Kind: proof-template
- Summary: If a bounded law is an n-fold convolution, the summand support diameter is at most 1/n of the total diameter, forcing variance to zero.
- Use case: Exercise 3.9.2.
- Tags: infinite-divisibility, bounded-support, variance

###### Infinitely divisible characteristic functions do not vanish

- ID: `exercise_ch3_infinitely_divisible_cf_nonvanishing`
- Kind: proof-template
- Summary: Symmetrize to |phi|^2, take nth convolution roots, and use continuity near zero to contradict a zero at a fixed point.
- Use case: Exercise 3.9.3.
- Tags: characteristic-functions, infinite-divisibility, nonvanishing

###### Find Levy measures by matching exponents

- ID: `exercise_ch3_levy_measure_by_exponent_matching`
- Kind: calculation-template
- Summary: Compare the log characteristic function with the Levy-Khinchin integral; symmetry cancels imaginary compensation terms.
- Use case: Exercise 3.9.4.
- Tags: levy-measure, levy-khinchin, symmetric-law

###### Recover marginals from a joint CDF

- ID: `exercise_ch3_marginals_from_joint_cdf`
- Kind: definition-use
- Summary: Send all non-target coordinates to infinity and use continuity from below to recover the target coordinate's distribution function.
- Use case: Exercise 3.10.1.
- Tags: marginals, joint-cdf, continuity-from-below

###### FGM-type copula density check

- ID: `exercise_ch3_fgm_copula_density_check`
- Kind: construction-template
- Summary: For C(u)=prod u_i + alpha prod u_i(1-u_i), the mixed derivative is 1+alpha prod(1-2u_i), nonnegative for |alpha|<=1.
- Use case: Exercise 3.10.2.
- Tags: copula, joint-distribution, density-check

###### Mixed partial derivative recovers joint density

- ID: `exercise_ch3_mixed_partial_recovers_density`
- Kind: calculation-template
- Summary: Write the CDF as an iterated integral of the density and apply the fundamental theorem of calculus successively.
- Use case: Exercise 3.10.3.
- Tags: joint-density, cdf, mixed-partial

###### Joint characteristic function factorization

- ID: `exercise_ch3_joint_cf_independence_factorization`
- Kind: proof-template
- Summary: Independence gives product transforms; conversely, a product joint characteristic function matches the product law by uniqueness.
- Use case: Exercise 3.10.6.
- Tags: independence, joint-characteristic-function, uniqueness

###### Diagonal covariance gives independent normal coordinates

- ID: `exercise_ch3_multivariate_normal_diagonal_covariance`
- Kind: normal-law-fact
- Summary: For a multivariate normal vector, a diagonal covariance matrix makes the characteristic function factor into one-dimensional normal transforms.
- Use case: Exercise 3.10.7.
- Tags: multivariate-normal, covariance, independence

###### Identify multivariate normal laws by all linear combinations

- ID: `exercise_ch3_cramer_wold_normal_identification`
- Kind: proof-template
- Summary: If every t dot X is normal with the right mean and variance, then the joint characteristic function is the multivariate normal transform.
- Use case: Exercise 3.10.8.
- Tags: cramer-wold, multivariate-normal, characteristic-functions

## Chapter 4

### Durrett Chapter 4 LLM Viki: Martingales

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter4.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

#### Section Guides

##### 4.1 Conditional Expectation

- Goal: Use conditional expectation as an F-measurable Radon-Nikodym object and compute it through partitions, densities, independence, and projection.

- Must master: definition, tower property, taking out what is known, conditional Jensen, L2 projection

- Prelim angle: Nearly every martingale proof is a conditional-expectation proof in disguise.

##### 4.2 Martingales, Almost Sure Convergence

- Goal: Build martingales from random walks, stop them, and prove almost sure convergence using upcrossings.

- Must master: martingale definition, random-walk martingales, stopping, upcrossing inequality, a.s. convergence theorem

- Prelim angle: The core toolkit for fair-game and hitting-time problems.

##### 4.3 Examples

- Goal: Recognize martingale structures in urns, conditional Borel-Cantelli, likelihood ratios, and branching processes.

- Must master: Doob decomposition, conditional Borel-Cantelli, Polya urn, Radon-Nikodym martingales, branching process martingale

- Prelim angle: Turns abstract convergence theorems into reusable templates for dependent processes.

##### 4.4 Doob's Inequality, Convergence in Lp, p>1

- Goal: Control martingale maxima and prove Lp convergence using Doob inequalities.

- Must master: bounded optional sampling, Doob maximal inequality, Lp maximal inequality, Lp convergence, orthogonal increments

- Prelim angle: Use when an exam asks for sup bounds, convergence in Lp, or variance control.

##### 4.5 Square Integrable Martingales*

- Goal: Use predictable quadratic variation to prove convergence and strong-law type martingale results.

- Must master: conditional variance, quadratic variation, L2 maximal bounds, martingale strong law

- Prelim angle: A more flexible replacement for independent-increment variance summation.

##### 4.6 Uniform Integrability, Convergence in L1

- Goal: Understand when almost sure martingale limits also converge in L1 and preserve expectations.

- Must master: uniform integrability, UI plus probability convergence, closed martingales, Levy upward theorem, Levy 0-1 law

- Prelim angle: This is the checkpoint before using optional stopping at unbounded times.

##### 4.7 Backwards Martingales

- Goal: Apply martingale convergence to decreasing filtrations and exchangeable information.

- Must master: backward convergence, Levy downward theorem, SLLN proof, Hewitt-Savage, de Finetti

- Prelim angle: Useful for tail, invariant, and exchangeability questions.

##### 4.8 Optional Stopping Theorems

- Goal: Know the hypotheses that make optional stopping valid and apply them to random walks.

- Must master: UI optional stopping, terminal-value criteria, Wald equation, symmetric ruin, biased ruin, exponential bounds

- Prelim angle: One of the highest-yield prelim sections for exact hitting probabilities and expected times.

##### 4.9 Combinatorics of Simple Random Walk*

- Goal: Count simple-random-walk paths using reflection, ballot formulas, and arcsine asymptotics.

- Must master: reflection principle, ballot theorem, return probabilities, arcsine laws

- Prelim angle: Provides exact combinatorial alternatives to martingale random-walk arguments.

#### Knowledge Pieces

##### Conditional expectation as Radon-Nikodym projection

- ID: `durrett_ch4_conditional_expectation_definition`

- Section: 4.1 Conditional Expectation

- Kind: definition

- Summary: E(X|F) is the F-measurable integrable random variable Y satisfying integral_A Y dP = integral_A X dP for every A in F.

- Proof idea: For X >= 0 define a measure nu(A)=integral_A X dP on F and use the Radon-Nikodym theorem; then split X into positive and negative parts.

- Exam use: The starting point for every martingale verification and every conditioning calculation.

- Pitfall: Conditional expectations are only unique up to almost sure equality, so pointwise formulas need version awareness.

- Tags: conditional-expectation, radon-nikodym, sigma-field

##### Uniqueness and locality of conditional expectation

- ID: `durrett_ch4_conditional_expectation_uniqueness_locality`

- Section: 4.1 Conditional Expectation

- Kind: theorem

- Summary: Versions of E(X|F) agree almost surely; if X1=X2 on B in F, then their conditional expectations agree on B almost surely.

- Proof idea: Test the positive part of the difference on sets where one candidate exceeds the other by epsilon.

- Exam use: Use locality to compute conditional expectations piecewise on atoms or events known at the conditioning time.

- Pitfall: The event where the variables agree must belong to the conditioning sigma-field.

- Tags: conditional-expectation, locality, versions

##### Conditional expectation on a countable partition

- ID: `durrett_ch4_partition_conditioning_formula`

- Section: 4.1.1 Examples

- Kind: formula

- Summary: If F is generated by a countable positive-probability partition, E(X|F) is constant on each atom and equals the average of X over that atom.

- Proof idea: Guess the atomwise average and verify the defining integral identity first on atoms, then by additivity.

- Exam use: Turns abstract conditioning into the familiar finite-state formula used in Bayes and Markov-chain problems.

- Pitfall: Atoms with probability zero cannot be handled by dividing by P(atom).

- Tags: conditioning, partition, bayes

##### Conditional density formula

- ID: `durrett_ch4_density_conditioning_formula`

- Section: 4.1.1 Examples

- Kind: formula

- Summary: For a joint density f(x,y), E(g(X)|Y)=h(Y), where h(y) is the conditional-density average of g against f(x,y).

- Proof idea: Write events in sigma(Y) as {Y in B}, integrate over B, and use Fubini to verify the defining identity.

- Exam use: Use for regression-style computations and conditional distribution questions with joint densities.

- Pitfall: Conditioning on Y=y is a density formula, not literal conditioning on a positive-probability event.

- Tags: conditional-density, joint-density, fubini

##### Conditioning with independent variables

- ID: `durrett_ch4_independent_conditioning_rule`

- Section: 4.1.1 Examples

- Kind: formula

- Summary: If X and Y are independent and g(x)=E phi(x,Y), then E(phi(X,Y)|X)=g(X).

- Proof idea: Use the product joint law and verify against indicators of events in sigma(X).

- Exam use: A quick way to integrate out fresh independent noise while leaving the present state fixed.

- Pitfall: Do not replace Y by its mean unless phi is linear in Y.

- Tags: independence, conditioning, product-measure

##### Linearity, monotonicity, and monotone convergence conditionally

- ID: `durrett_ch4_conditional_expectation_properties`

- Section: 4.1.2 Properties

- Kind: theorem

- Summary: Conditional expectation is linear, preserves order, and respects monotone limits under the same integrability hypotheses as ordinary expectation.

- Proof idea: Verify the defining identity for linearity; for order, test the positive part; for monotone convergence, use ordinary dominated or monotone convergence on each conditioning event.

- Exam use: These are the algebra rules behind almost every martingale manipulation.

- Pitfall: Check integrability hypotheses before using linearity with signed variables.

- Tags: conditional-expectation, linearity, monotone-convergence

##### Conditional Jensen and Lp contraction

- ID: `durrett_ch4_conditional_jensen_contraction`

- Section: 4.1.2 Properties

- Kind: theorem

- Summary: For convex phi, phi(E(X|F)) <= E(phi(X)|F); in particular conditional expectation is a contraction on Lp for p >= 1.

- Proof idea: Write a convex function as a supremum of rational affine minorants and apply monotonicity and linearity.

- Exam use: Use to prove submartingale transforms and uniform Lp bounds after conditioning.

- Pitfall: The inequality is almost sure, and the convex function must be integrable after composition.

- Tags: jensen, lp-contraction, conditional-expectation

##### Tower property: the smaller sigma-field wins

- ID: `durrett_ch4_tower_property_smaller_sigma_field_wins`

- Section: 4.1.2 Properties

- Kind: theorem

- Summary: If F1 subset F2, then E(E(X|F1)|F2)=E(X|F1) and E(E(X|F2)|F1)=E(X|F1).

- Proof idea: The first identity is measurability; the second verifies the defining identity on sets in F1.

- Exam use: Essential for collapsing repeated conditionings in martingale and Markov arguments.

- Pitfall: The order of unrelated sigma-fields cannot be swapped; nesting is the whole point.

- Tags: tower-property, conditioning, sigma-fields

##### Taking out what is known

- ID: `durrett_ch4_taking_out_what_is_known`

- Section: 4.1.2 Properties

- Kind: theorem

- Summary: If X is F-measurable and the products are integrable, then E(XY|F)=X E(Y|F).

- Proof idea: Prove first for indicators in F, extend to simple functions, then use monotone convergence and signed decompositions.

- Exam use: Lets predictable factors pass through conditional expectation in martingale increment calculations.

- Pitfall: The multiplier must be measurable with respect to the conditioning sigma-field.

- Tags: conditioning, measurability, predictable

##### Conditional expectation as L2 best predictor

- ID: `durrett_ch4_conditional_expectation_l2_projection`

- Section: 4.1.2 Properties

- Kind: theorem

- Summary: When EX^2 is finite, E(X|F) is the F-measurable square-integrable variable minimizing E(X-Y)^2.

- Proof idea: Show X-E(X|F) is orthogonal to every L2(F) random variable and use the Pythagorean identity.

- Exam use: Useful for variance decompositions and interpreting conditional expectation as optimal prediction.

- Pitfall: The projection picture needs second moments; L1 conditional expectation exists more generally.

- Tags: l2-projection, best-predictor, orthogonality

##### Regular conditional distributions

- ID: `durrett_ch4_regular_conditional_distribution`

- Section: 4.1.3 Regular Conditional Probabilities*

- Kind: definition

- Summary: A regular conditional distribution gives a probability kernel whose A-coordinate versions equal P(X in A|G).

- Proof idea: For nice spaces construct conditional distribution functions on rational cut points and extend to measures.

- Exam use: Use when a problem wants conditioning as a genuine conditional law rather than one function at a time.

- Pitfall: Regular conditional probabilities need not exist on arbitrary measurable spaces.

- Tags: regular-conditional-probability, kernels, nice-spaces

##### Martingale, submartingale, and supermartingale definitions

- ID: `durrett_ch4_martingale_definition`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: definition

- Summary: An adapted integrable process is a martingale when E(X_{n+1}|F_n)=X_n; replacing equality by >= or <= gives submartingales or supermartingales.

- Proof idea: The definition formalizes fair, favorable, and unfavorable games through one-step conditional means.

- Exam use: Every martingale problem starts by identifying the filtration, integrability, adaptedness, and the one-step conditional expectation.

- Pitfall: The filtration is part of the data; a process can be a martingale for one filtration and not another.

- Tags: martingales, filtration, adapted

##### Linear, quadratic, and exponential random-walk martingales

- ID: `durrett_ch4_random_walk_martingales`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: example-bank

- Summary: For iid increments, S_n-n mu, S_n^2-n sigma^2 in the centered finite-variance case, and exp(theta S_n)/phi(theta)^n are martingales under their natural hypotheses.

- Proof idea: Condition on the past and use independence of the next increment, expanding the square or moment generating factor.

- Exam use: These are the main engines for gambler's ruin, hitting probabilities, Wald identities, and exponential tail bounds.

- Pitfall: The exponential martingale requires the moment generating function to be finite at the chosen theta.

- Tags: random-walk, exponential-martingale, quadratic-martingale

##### Multi-step conditional expectation property

- ID: `durrett_ch4_multi_step_martingale_property`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: For n>m, martingales satisfy E(X_n|F_m)=X_m; submartingales give >= and supermartingales give <=.

- Proof idea: Iterate the one-step definition using the tower property.

- Exam use: Use whenever a future stopped or terminal value is related back to present information.

- Pitfall: The direction of the inequality reverses between submartingales and supermartingales.

- Tags: martingales, tower-property, filtration

##### Convex transforms make submartingales

- ID: `durrett_ch4_convex_transform_submartingale`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: A convex function of a martingale is a submartingale; an increasing convex function of a submartingale is also a submartingale.

- Proof idea: Apply conditional Jensen, then use monotonicity when the input process is only a submartingale.

- Exam use: Build nonnegative submartingales such as |X_n|, X_n^2, and exp(theta X_n) for maximal inequalities.

- Pitfall: The transformed variables must be integrable.

- Tags: jensen, submartingale, convexity

##### Martingale transforms and no profitable gambling systems

- ID: `durrett_ch4_martingale_transform_no_gambling_system`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: If H_n is nonnegative predictable and X is a supermartingale, then the gains process sum H_m(X_m-X_{m-1}) is a supermartingale.

- Proof idea: Take conditional expectations term by term, using that H_m is known at time m-1.

- Exam use: Formalizes optional betting strategies and proves stopped supermartingales remain supermartingales.

- Pitfall: Predictability is essential; stakes cannot depend on the next outcome.

- Tags: martingale-transform, predictable, gambling-system

##### Stopped processes preserve martingale type

- ID: `durrett_ch4_stopped_process_supermartingale`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: If N is a stopping time and X is a supermartingale, then X_{N wedge n} is a supermartingale; analogous statements hold for martingales and submartingales.

- Proof idea: Represent stopping as a predictable strategy that bets until N and then stops.

- Exam use: Use before applying convergence or inequality theorems to hitting-time stopped processes.

- Pitfall: Stopping alone does not guarantee equality of expectations at unbounded times.

- Tags: stopping-time, stopped-process, optional-stopping

##### Doob upcrossing inequality

- ID: `durrett_ch4_upcrossing_inequality`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: For a submartingale, the expected number of upcrossings of [a,b] up to n is bounded by E(X_n-a)^+/(b-a).

- Proof idea: Buy at a and sell at b using a predictable switching strategy, then compare accumulated gains to the positive part of the terminal value.

- Exam use: The key tool for proving almost sure convergence from bounded positive expectations.

- Pitfall: The interval is [a,b] with a<b; upcrossings are completed crossings, not mere visits.

- Tags: upcrossing, submartingale, convergence

##### Submartingale almost sure convergence theorem

- ID: `durrett_ch4_martingale_convergence_theorem`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: theorem

- Summary: If X_n is a submartingale with sup_n E X_n^+ finite, then X_n converges almost surely to a finite limit.

- Proof idea: Use the upcrossing inequality to rule out infinitely many oscillations across rational intervals and control the positive tail.

- Exam use: A default convergence theorem for bounded or nonnegative martingales after choosing the right sign.

- Pitfall: Almost sure convergence does not automatically imply L1 convergence or preservation of expectations.

- Tags: martingale-convergence, upcrossing, almost-sure

##### Nonnegative supermartingale convergence

- ID: `durrett_ch4_nonnegative_supermartingale_convergence`

- Section: 4.2 Martingales, Almost Sure Convergence

- Kind: corollary

- Summary: Every nonnegative supermartingale converges almost surely to a finite limit, with finite expected limit bounded by the initial expectation.

- Proof idea: Apply the submartingale convergence theorem to -X_n or use the boundedness of expectations coming from nonnegativity.

- Exam use: Extremely useful for likelihood ratios, branching process normalizations, and stopped random walks.

- Pitfall: The limit can have smaller expectation than X_0; equality needs uniform integrability or stronger optional stopping conditions.

- Tags: nonnegative-supermartingale, almost-sure-convergence, fatou

##### Bounded-increment convergence criterion

- ID: `durrett_ch4_bounded_increment_convergence`

- Section: 4.3.1 Bounded Increments

- Kind: criterion

- Summary: A supermartingale with bounded increments cannot keep drifting on a bounded interval without converging; stopping and shifting make it nonnegative.

- Proof idea: Stop on a lower barrier and add a constant, then apply nonnegative supermartingale convergence.

- Exam use: Use for random walks or games where increments are controlled but the process is not globally nonnegative.

- Pitfall: You must first localize so the shifted stopped process is nonnegative.

- Tags: bounded-increments, stopping, convergence

##### Doob decomposition

- ID: `durrett_ch4_doob_decomposition`

- Section: 4.3 Examples

- Kind: theorem

- Summary: Every submartingale decomposes uniquely into a martingale plus an increasing predictable process starting at zero.

- Proof idea: Define the compensator increments as E(X_n-X_{n-1}|F_{n-1}) and subtract their cumulative sum.

- Exam use: Separates random fluctuation from predictable drift in counting-process and indicator-sum arguments.

- Pitfall: The compensator is predictable, not optional; its increment is known one step earlier.

- Tags: doob-decomposition, compensator, submartingale

##### Conditional Borel-Cantelli lemma

- ID: `durrett_ch4_conditional_borel_cantelli`

- Section: 4.3 Examples

- Kind: theorem

- Summary: For adapted events B_n, occurrence infinitely often is controlled by the divergence or convergence of the conditional probability sums E(1_{B_n}|F_{n-1}).

- Proof idea: Apply martingale convergence to the difference between actual counts and conditional expected counts.

- Exam use: Use for dependent trials where ordinary independence is unavailable but conditional probabilities are tractable.

- Pitfall: The conditioning must be on the past; replacing it by unconditional probabilities loses the theorem's content.

- Tags: borel-cantelli, conditional-probability, martingales

##### Polya urn proportion martingale

- ID: `durrett_ch4_polya_urn_martingale`

- Section: 4.3.2 Polya's Urn Scheme

- Kind: example-pattern

- Summary: In Polya's urn, the fraction of balls of one color is a bounded martingale and therefore converges almost surely.

- Proof idea: Condition on the current urn composition to show the next expected proportion equals the current proportion.

- Exam use: A model example for bounded martingale convergence and beta-limit intuition.

- Pitfall: Almost sure convergence alone does not identify the limiting distribution without extra computation.

- Tags: polya-urn, bounded-martingale, beta

##### Radon-Nikodym derivative martingales

- ID: `durrett_ch4_radon_nikodym_derivative_martingale`

- Section: 4.3.3 Radon-Nikodym Derivatives

- Kind: theorem

- Summary: If mu_n and nu_n are restrictions to F_n with mu_n absolutely continuous with respect to nu_n, then dmu_n/dnu_n forms a nonnegative martingale under nu.

- Proof idea: Verify the conditional expectation identity by integrating over sets in the smaller sigma-field.

- Exam use: Use to compare infinite product measures and prove absolute-continuity versus singularity alternatives.

- Pitfall: Finite-dimensional absolute continuity does not by itself guarantee infinite-dimensional absolute continuity.

- Tags: radon-nikodym, likelihood-ratio, absolute-continuity

##### Branching process normalized martingale

- ID: `durrett_ch4_branching_process_normalized_martingale`

- Section: 4.3.4 Branching Processes

- Kind: example-pattern

- Summary: For a Galton-Watson process with mean mu, Z_n/mu^n is a nonnegative martingale when mu is positive.

- Proof idea: Condition on the current population and use that the next generation is a sum of Z_n iid offspring variables.

- Exam use: The central martingale for extinction, survival, and supercritical growth questions.

- Pitfall: In the supercritical case the martingale limit may still be zero unless an L log L condition holds.

- Tags: branching-process, galton-watson, nonnegative-martingale

##### Bounded optional sampling inequality

- ID: `durrett_ch4_bounded_stopping_submartingale_expectation`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: theorem

- Summary: If X is a submartingale and N is a bounded stopping time, then E X_0 <= E X_N <= E X_k for a bound k on N.

- Proof idea: Use the stopped submartingale and monotonicity of expectations over deterministic times.

- Exam use: The bounded-time version of optional sampling used inside maximal inequality proofs.

- Pitfall: Boundedness of the stopping time is doing real work; unbounded stopping can fail.

- Tags: optional-sampling, bounded-stopping, submartingale

##### Doob maximal inequality

- ID: `durrett_ch4_doob_maximal_inequality`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: theorem

- Summary: For a submartingale, lambda P(max_{m<=n} X_m >= lambda) is bounded by the expected terminal value on the event that the maximum exceeds lambda.

- Proof idea: Stop the first time the process crosses lambda and apply bounded optional sampling.

- Exam use: Use to control suprema of martingales, derive Kolmogorov inequalities, and prove Lp convergence.

- Pitfall: Apply it to nonnegative submartingales such as |X_n| or X_n^2 when signs are an issue.

- Tags: doob-inequality, maximal-inequality, submartingale

##### Doob Lp maximum inequality

- ID: `durrett_ch4_lp_maximum_inequality`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: theorem

- Summary: For p>1, the Lp norm of max_{m<=n} |X_m| is bounded by p/(p-1) times the Lp norm of X_n for martingales and suitable submartingales.

- Proof idea: Integrate Doob's maximal tail bound over lambda and use calculus/Holder-style estimates.

- Exam use: The main route from uniform Lp bounds to almost sure and Lp convergence.

- Pitfall: There is no comparable L1 maximal inequality without extra hypotheses.

- Tags: lp, maximal-inequality, doob

##### Lp martingale convergence theorem

- ID: `durrett_ch4_lp_martingale_convergence`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: theorem

- Summary: If a martingale has sup_n E|X_n|^p finite for some p>1, then X_n converges almost surely and in Lp.

- Proof idea: Use submartingale convergence for |X_n| and Doob's Lp maximum inequality for uniform integrability of the tail supremum.

- Exam use: A clean sufficient condition for exchanging martingale limits with p-th moments.

- Pitfall: The theorem needs p>1; L1 convergence requires uniform integrability instead.

- Tags: lp-convergence, martingales, uniform-lp-bound

##### Orthogonality of square-integrable martingale increments

- ID: `durrett_ch4_orthogonal_martingale_increments`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: theorem

- Summary: Square-integrable martingale increments are orthogonal, so variances of sums add across increments.

- Proof idea: For i<j, condition the product of the earlier increment with the later increment on F_{j-1}.

- Exam use: Use for L2 bounds, variance computations, and quadratic martingale arguments.

- Pitfall: Orthogonality is not independence; it is a second-moment identity.

- Tags: orthogonality, increments, l2-martingales

##### Conditional variance formula for martingales

- ID: `durrett_ch4_conditional_variance_formula_martingales`

- Section: 4.4 Doob's Inequality, Convergence in Lp, p>1

- Kind: formula

- Summary: For square-integrable martingales, conditional second-moment growth is the sum of conditional variances of increments.

- Proof idea: Expand X_{n+1}^2-X_n^2 and condition on the past so the cross term vanishes.

- Exam use: Use to estimate quadratic variation and prove convergence from summable conditional variances.

- Pitfall: Use conditional variances of increments, not unconditional variances unless independence or identical structure justifies it.

- Tags: conditional-variance, quadratic-variation, l2

##### Square-integrable martingales and quadratic variation

- ID: `durrett_ch4_square_integrable_martingale_quadratic_variation`

- Section: 4.5 Square Integrable Martingales*

- Kind: theorem

- Summary: For square-integrable martingales, the predictable accumulated conditional variance A_n governs maximal L2 bounds and convergence.

- Proof idea: Apply Doob's L2 inequality to the stopped martingale and compare E X_n^2 with E A_n.

- Exam use: Use when convergence depends on summability of conditional variances rather than bounded increments.

- Pitfall: The predictable quadratic variation is not the same as the realized squared-increment sum.

- Tags: square-integrable, quadratic-variation, predictable-variation

##### Martingale strong-law normalization

- ID: `durrett_ch4_martingale_strong_law_from_variances`

- Section: 4.5 Square Integrable Martingales*

- Kind: criterion

- Summary: If a square-integrable martingale has controlled predictable quadratic variation, then X_n normalized by a suitable increasing function of A_n tends to zero.

- Proof idea: Rescale increments with a predictable factor, show the transformed martingale converges, then undo the normalization.

- Exam use: Generalizes Kolmogorov strong-law arguments to martingale differences.

- Pitfall: Choose a normalization satisfying the required integral/summability condition.

- Tags: strong-law, martingale-differences, normalization

##### Uniform integrability

- ID: `durrett_ch4_uniform_integrability_definition`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: definition

- Summary: A family is uniformly integrable when the tail expectations sup E(|X|; |X|>K) go to zero as K goes to infinity.

- Proof idea: Tail control is equivalent to domination by a superlinear Orlicz function and implies L1 tightness of mass.

- Exam use: The exact condition needed to upgrade probability or a.s. convergence to L1 convergence.

- Pitfall: Bounded L1 norms alone do not imply uniform integrability.

- Tags: uniform-integrability, l1, tail-control

##### Uniform integrability plus probability convergence gives L1 convergence

- ID: `durrett_ch4_ui_plus_probability_equals_l1`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: theorem

- Summary: If X_n is uniformly integrable and X_n converges in probability to X, then X is integrable and X_n converges to X in L1.

- Proof idea: Split expectations on {|X_n-X| small}, on moderate tails, and on large tails controlled by uniform integrability.

- Exam use: Use after proving almost sure martingale convergence to obtain L1 convergence.

- Pitfall: Convergence in probability without uniform integrability is not enough for L1 convergence.

- Tags: uniform-integrability, l1-convergence, probability-convergence

##### Submartingale L1 convergence equivalences

- ID: `durrett_ch4_submartingale_l1_convergence_equivalences`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: theorem

- Summary: For submartingales, uniform integrability is equivalent to almost sure and L1 convergence to an integrable limit under the standard convergence hypotheses.

- Proof idea: Combine submartingale a.s. convergence with the UI-to-L1 theorem and the implication from L1 convergence to uniform integrability.

- Exam use: Decides when the limit preserves first moments.

- Pitfall: Almost sure convergence from Chapter 4.2 by itself is weaker than L1 convergence.

- Tags: submartingale, uniform-integrability, l1-convergence

##### Closed martingales and uniform integrability

- ID: `durrett_ch4_closed_martingales_ui_equivalence`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: theorem

- Summary: A martingale is uniformly integrable iff it converges in L1 iff it can be written as X_n=E(X|F_n) for some integrable terminal variable X.

- Proof idea: Use L1 convergence to identify the terminal variable, and use conditional expectation contraction to prove UI for closed martingales.

- Exam use: The main structural test for optional stopping at unbounded times.

- Pitfall: A martingale can converge a.s. but fail to be closed by an L1 terminal variable.

- Tags: closed-martingale, uniform-integrability, l1

##### Levy upward theorem

- ID: `durrett_ch4_levy_upward_theorem`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: theorem

- Summary: If F_n increases to F_infinity, then E(X|F_n) converges almost surely and in L1 to E(X|F_infinity).

- Proof idea: Recognize E(X|F_n) as a closed uniformly integrable martingale and identify its limit by testing against the union sigma-field.

- Exam use: Use to prove Levy's 0-1 law and conditional dominated convergence.

- Pitfall: The limiting sigma-field is generated by the increasing union, not simply the pointwise union as a collection.

- Tags: levy-theorem, increasing-filtration, conditional-expectation

##### Levy's 0-1 law

- ID: `durrett_ch4_levy_zero_one_law`

- Section: 4.6 Uniform Integrability, Convergence in L1

- Kind: theorem

- Summary: If A belongs to the limiting sigma-field of an increasing filtration, then P(A|F_n) converges almost surely to 1_A.

- Proof idea: Apply Levy's upward theorem to X=1_A.

- Exam use: Use to convert better and better finite information into eventual certainty for tail-like events inside the generated limit.

- Pitfall: This is different from Kolmogorov's 0-1 law, which concerns independent tail sigma-fields.

- Tags: levy-zero-one, conditional-probability, filtration

##### Backward martingale convergence

- ID: `durrett_ch4_backward_martingale_convergence`

- Section: 4.7 Backwards Martingales

- Kind: theorem

- Summary: A martingale indexed backward in time, with decreasing sigma-fields, converges almost surely and in L1 to its conditional expectation on the tail intersection.

- Proof idea: Use the upcrossing argument on finite backward windows, then uniform integrability from representation as E(X_0|F_n).

- Exam use: The engine behind the strong law, Hewitt-Savage, and de Finetti-style results.

- Pitfall: The index direction matters: sigma-fields decrease as time moves backward.

- Tags: backward-martingale, tail-sigma-field, l1-convergence

##### Levy downward theorem

- ID: `durrett_ch4_levy_downward_theorem`

- Section: 4.7 Backwards Martingales

- Kind: theorem

- Summary: If F_n decreases to F_{-infinity}, then E(Y|F_n) converges almost surely and in L1 to E(Y|F_{-infinity}).

- Proof idea: View the conditional expectations as a backward martingale and identify the limit by testing on the intersection sigma-field.

- Exam use: Use for exchangeability, tail sigma-fields, and reverse filtrations.

- Pitfall: Do not replace the intersection by a limiting union; this is the downward theorem.

- Tags: levy-downward, backward-martingale, conditional-expectation

##### Strong law via backward martingales

- ID: `durrett_ch4_slln_via_backward_martingales`

- Section: 4.7 Backwards Martingales

- Kind: example-pattern

- Summary: For iid integrable variables, sample averages can be represented through decreasing symmetric-information sigma-fields and converge to the mean.

- Proof idea: Use exchangeability of finite averages and the backward martingale convergence theorem; the tail/invariant sigma-field is trivial.

- Exam use: A conceptual proof of the strong law that also prepares de Finetti arguments.

- Pitfall: The iid and integrability assumptions are doing the work; this is not a variance proof.

- Tags: strong-law, iid, backward-martingale

##### Hewitt-Savage 0-1 law

- ID: `durrett_ch4_hewitt_savage_zero_one`

- Section: 4.7 Backwards Martingales

- Kind: theorem

- Summary: For iid sequences, every event invariant under finite permutations has probability 0 or 1.

- Proof idea: Average conditional indicators over symmetric sigma-fields and use backward martingale convergence to show the event is independent of itself.

- Exam use: Use when an event is exchangeable rather than merely tail-measurable.

- Pitfall: Permutation invariance is stronger/different than tail measurability; check the event carefully.

- Tags: hewitt-savage, zero-one-law, exchangeability

##### de Finetti theorem for exchangeable sequences

- ID: `durrett_ch4_definetti_theorem`

- Section: 4.7 Backwards Martingales

- Kind: theorem

- Summary: Exchangeable sequences are conditionally iid given the exchangeable tail information; in the binary case they are mixtures of iid Bernoulli sequences.

- Proof idea: Use backward martingales to identify empirical averages and finite-dimensional conditional laws.

- Exam use: Recognize hidden-random-parameter representations in exchangeable models.

- Pitfall: Exchangeability is weaker than independence but stronger than identical marginal distributions.

- Tags: de-finetti, exchangeability, mixtures

##### Optional stopping for uniformly integrable martingales

- ID: `durrett_ch4_optional_stopping_ui`

- Section: 4.8 Optional Stopping Theorems

- Kind: theorem

- Summary: Uniformly integrable martingales satisfy optional sampling for arbitrary stopping times, with stopped values inheriting the martingale inequalities.

- Proof idea: Use L1 convergence of stopped processes and bounded optional sampling on truncated stopping times.

- Exam use: The cleanest condition under which E X_N = E X_0 is valid for unbounded N.

- Pitfall: Without uniform integrability or another sufficient condition, optional stopping can fail dramatically.

- Tags: optional-stopping, uniform-integrability, stopping-time

##### Optional stopping with integrable terminal value

- ID: `durrett_ch4_optional_stopping_integrable_terminal`

- Section: 4.8 Optional Stopping Theorems

- Kind: criterion

- Summary: If X_N is integrable and the pre-stopping tails X_n 1_{N>n} are uniformly integrable, then X_{N wedge n} is uniformly integrable and optional stopping applies.

- Proof idea: Decompose X_{N wedge n} into the terminal-on-stopped part and the still-running part, then use UI.

- Exam use: A practical checklist for hitting times where the stopped value is bounded or controlled.

- Pitfall: Finite expectation of N alone is not the same as this UI tail condition, though bounded increments can imply useful variants.

- Tags: optional-stopping, terminal-value, uniform-integrability

##### Wald's equation via optional stopping

- ID: `durrett_ch4_wald_equation`

- Section: 4.8 Optional Stopping Theorems

- Kind: theorem

- Summary: For iid integrable increments with mean mu, S_N has expectation mu E N under suitable stopping and integrability conditions.

- Proof idea: Apply optional stopping to the martingale S_n-n mu.

- Exam use: Use for expected sums at stopping times, especially random walks and renewal-style counts.

- Pitfall: Independence of N from increments is not the right general condition; N is often a stopping time, and optional stopping hypotheses must be checked.

- Tags: wald-equation, random-walk, optional-stopping

##### Symmetric gambler's ruin via martingales

- ID: `durrett_ch4_symmetric_gamblers_ruin`

- Section: 4.8.1 Applications to Random Walks

- Kind: example-pattern

- Summary: For symmetric simple random walk stopped on hitting a or b, optional stopping of S_n gives linear hitting probabilities and S_n^2-n gives expected hitting times.

- Proof idea: Stop the linear and quadratic martingales at bounded barriers, then solve the resulting algebraic equations.

- Exam use: High-yield prelim template for hitting probabilities and mean exit times.

- Pitfall: For one-sided unbounded hitting times, use truncation or extra arguments before sending the bound to infinity.

- Tags: gambler-ruin, symmetric-random-walk, hitting-time

##### Asymmetric gambler's ruin via exponential martingales

- ID: `durrett_ch4_asymmetric_gamblers_ruin`

- Section: 4.8.1 Applications to Random Walks

- Kind: example-pattern

- Summary: For biased simple random walk, an exponential martingale r^{S_n} gives nonlinear hitting probabilities and finite expected hitting times in the drift direction.

- Proof idea: Choose r so E r^{xi}=1 and apply optional stopping at two-sided barriers.

- Exam use: Use when the walk has drift and the harmonic function is exponential rather than linear.

- Pitfall: The symmetric formulas are limiting cases; plugging p=q into biased formulas may require taking a limit.

- Tags: biased-random-walk, exponential-martingale, gambler-ruin

##### Insurance ruin exponential bound

- ID: `durrett_ch4_insurance_ruin_exponential_bound`

- Section: 4.8.1 Applications to Random Walks

- Kind: example-pattern

- Summary: If a random walk has a positive adjustment coefficient theta with E exp(theta xi)=1, exponential martingales bound the probability of ever hitting a bad lower level.

- Proof idea: Stop the exponential martingale at ruin or an upper truncation and let the truncation grow.

- Exam use: Use for Cramer-Lundberg style ruin bounds and rare-event hitting estimates.

- Pitfall: The bound needs the exponential moment equation at a positive theta.

- Tags: ruin-probability, exponential-martingale, tail-bound

##### Reflection principle

- ID: `durrett_ch4_reflection_principle`

- Section: 4.9 Combinatorics of Simple Random Walk*

- Kind: theorem

- Summary: For simple random walk paths, paths crossing a barrier can be counted by reflecting the path after the first hit.

- Proof idea: Map each bad path bijectively to a reflected path with a shifted endpoint.

- Exam use: Use for exact hitting and maximum distributions without martingale machinery.

- Pitfall: The reflection is a path-counting bijection; keep parity and endpoints consistent.

- Tags: reflection-principle, simple-random-walk, path-counting

##### Ballot theorem

- ID: `durrett_ch4_ballot_theorem`

- Section: 4.9 Combinatorics of Simple Random Walk*

- Kind: theorem

- Summary: If one candidate finishes ahead, the probability that they stayed strictly ahead throughout has a simple ratio depending on the final margin.

- Proof idea: Count all paths with a fixed endpoint and subtract those that touch or cross the forbidden boundary using reflection.

- Exam use: Use for positivity-conditioned walks and first-passage combinatorics.

- Pitfall: Strict positivity versus nonnegativity changes the boundary and constants.

- Tags: ballot-theorem, reflection-principle, random-walk

##### Arcsine laws for simple random walk

- ID: `durrett_ch4_arcsine_laws_random_walk`

- Section: 4.9 Combinatorics of Simple Random Walk*

- Kind: theorem

- Summary: The last zero time and the occupation time above zero for long symmetric simple random walks have arcsine limiting distributions.

- Proof idea: Factor exact probabilities using return probabilities, then apply central binomial asymptotics to obtain the arcsine density.

- Exam use: Recognize that typical paths spend a surprisingly large fraction of time mostly positive or mostly negative.

- Pitfall: The arcsine density is U-shaped; intuition based on concentration near one half is wrong.

- Tags: arcsine-law, occupation-time, simple-random-walk

### Chapter 4 Exercise Viki

#### Chapter 4 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter4/Chapter4Exercises.tex`
Source PDF: `Probability/Exercises/Chapter4/Chapter4Exercises.pdf`

This dataset turns the solved Chapter 4 exercises into retrieval-ready records, reusable method cards, and exercise-derived knowledge pieces.

##### Files

- `chapter4_exercise_records.jsonl`: one record per solved exercise, including question, solution, knowledge used, and method tags.
- `chapter4_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter4_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter4_exercise_method_flashcards.tsv`: flashcard import file for method and new-knowledge cards.
- `chapter4_exercise_viki.md`: human-readable overview.

##### Section Method Cards

###### 4.1 - Conditional expectation, conditioning identities, and L2 projection

Solved exercise records: 10

Compute conditional expectations by testing against the conditioning sigma-field, then use projection, Jensen, conditioning on partitions, and variance decomposition to simplify identities.

Tags: conditional-expectation, projection, jensen, variance-decomposition

Reusable knowledge: exercise_ch4_conditional_bayes_by_indicator, exercise_ch4_conditional_inequality_from_pointwise_bound, exercise_ch4_l2_projection_pythagorean_conditioning, exercise_ch4_total_variance_random_sum, exercise_ch4_distribution_preserving_conditional_expectation

###### 4.2 - Martingales, submartingales, supermartingales, transforms, and upcrossings

Solved exercise records: 10

Check martingale type by conditioning one step ahead; use predictable transforms, stopped processes, upcrossing counts, and product decompositions to prove convergence or construct examples.

Tags: martingale, predictable-transform, stopping, upcrossing, convergence

Reusable knowledge: exercise_ch4_natural_filtration_martingale_reduction, exercise_ch4_deterministic_submartingale_square_supermartingale, exercise_ch4_stopped_upcrossing_localization, exercise_ch4_product_martingale_limit_zero, exercise_ch4_dubins_upcrossing_switching

###### 4.3 - Examples of martingales, likelihood-ratio martingales, and branching processes

Solved exercise records: 13

Use concrete martingale examples to isolate hypotheses: likelihood-ratio processes give martingales, additive error bounds give convergence, and branching recursions reduce to fixed-point equations.

Tags: examples, likelihood-ratio, radon-nikodym, branching-process, counterexample

Reusable knowledge: exercise_ch4_bounded_increment_nonmartingale_counterexample, exercise_ch4_additive_error_supermartingale_convergence, exercise_ch4_partition_rn_derivative_martingale, exercise_ch4_bernoulli_product_hellinger_criterion, exercise_ch4_branching_fixed_point_extinction

###### 4.4 - Doob inequalities, optional sampling, maximal bounds, and martingale SLLN

Solved exercise records: 11

Apply optional sampling and Doob inequalities to stopped martingales; combine orthogonal increments, quadratic martingales, and Kronecker normalization for L2 and strong-law estimates.

Tags: doob-inequality, optional-sampling, quadratic-martingale, orthogonal-increments, strong-law

Reusable knowledge: exercise_ch4_optional_sampling_between_stopping_times, exercise_ch4_doob_l1_log_maximal_bound, exercise_ch4_stopped_quadratic_martingale_exit_bound, exercise_ch4_martingale_increment_orthogonality_sum, exercise_ch4_kronecker_martingale_normalization

###### 4.6 - Uniform integrability, Levy theorems, posterior limits, and martingale convergence

Solved exercise records: 7

Recognize when convergence is upgraded by uniform integrability; use Levy upward and zero-one laws to turn conditioning on growing sigma-fields into posterior consistency or absorbing-state conclusions.

Tags: uniform-integrability, levy-upward, zero-one-law, posterior-consistency, bounded-martingale

Reusable knowledge: exercise_ch4_posterior_consistency_by_levy_upward, exercise_ch4_dyadic_conditional_expectation_approximation, exercise_ch4_levy_zero_one_absorption_or_escape, exercise_ch4_bounded_martingale_binary_limit

###### 4.7 - Backward martingales, exchangeability, and U-statistic limits

Solved exercise records: 5

Use backward martingale convergence for tail-like sigma-fields, then exploit exchangeability to replace conditional laws by finite-population hypergeometric formulas.

Tags: backward-martingale, exchangeability, hypergeometric, u-statistic, covariance

Reusable knowledge: exercise_ch4_backward_lp_convergence_ui, exercise_ch4_backward_conditional_dct, exercise_ch4_exchangeable_hypergeometric_conditioning, exercise_ch4_exchangeable_pair_covariance_positive, exercise_ch4_u_statistic_pair_square_limit

###### 4.8 - Optional stopping applications, Wald identities, random walks, and ruin estimates

Solved exercise records: 11

Choose a martingale matched to the target functional, stop it at bounded levels, justify optional stopping, and pass limits to obtain hitting probabilities, Wald identities, and ruin bounds.

Tags: optional-stopping, random-walk, wald-identity, gambler-ruin, exponential-martingale

Reusable knowledge: exercise_ch4_optional_stopping_ui_conditional_form, exercise_ch4_supermartingale_maximal_bound, exercise_ch4_wald_second_equation_stopped_l2, exercise_ch4_gambler_ruin_variance_generation, exercise_ch4_exponential_martingale_ruin_adjustment, exercise_ch4_fourth_moment_exit_time

###### 4.9 - Renewal equations and generating functions for random-walk return times

Solved exercise records: 1

Encode first-return decompositions as renewal equations and solve them with generating functions; singular behavior at one reveals recurrence and return-time means.

Tags: renewal-equation, generating-functions, return-time, random-walk

Reusable knowledge: exercise_ch4_return_time_renewal_generating_function

##### Exercise Records

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

##### New Exercise-Derived Knowledge

###### Conditional Bayes rule from indicator tests

- ID: `exercise_ch4_conditional_bayes_by_indicator`
- Kind: calculation-template
- Summary: To identify E[X | H] on a partition or sub-sigma-field, multiply by indicators of conditioning events and match integrals.
- Use case: Section 4.1 exercises involving conditional probabilities, finite partitions, and conditional densities.
- Tags: conditional-expectation, indicator-test, bayes

###### Transfer pointwise inequalities through conditioning

- ID: `exercise_ch4_conditional_inequality_from_pointwise_bound`
- Kind: proof-template
- Summary: If an inequality holds after multiplying by every nonnegative H-measurable test function, it holds for the conditional expectations.
- Use case: Conditional Jensen, conditional Markov bounds, and monotonicity arguments in Section 4.1.
- Tags: conditional-expectation, inequality, test-functions

###### L2 projection Pythagorean identity for conditioning

- ID: `exercise_ch4_l2_projection_pythagorean_conditioning`
- Kind: proof-template
- Summary: Use E[(X-E[X|H])Z]=0 for H-measurable Z to split squared errors and prove best-approximation identities.
- Use case: Projection and regression-style conditional expectation exercises.
- Tags: l2-projection, orthogonality, conditional-expectation

###### Random-sum variance by conditioning on the count

- ID: `exercise_ch4_total_variance_random_sum`
- Kind: calculation-template
- Summary: Condition on N to compute E[S_N | N] and Var(S_N | N), then add conditional variance plus variance of the conditional mean.
- Use case: Random sums and total-variance exercises in Section 4.1.
- Tags: random-sum, total-variance, conditioning

###### Conditional expectation can preserve distribution only under rigidity

- ID: `exercise_ch4_distribution_preserving_conditional_expectation`
- Kind: warning
- Summary: If E[X|H] has the same distribution as X and Jensen is tight for a strictly convex function, then X must already be H-measurable.
- Use case: Exercises where conditioning appears not to reduce randomness.
- Tags: jensen, rigidity, conditional-expectation

###### One-step martingale check in the natural filtration

- ID: `exercise_ch4_natural_filtration_martingale_reduction`
- Kind: proof-template
- Summary: For processes built from independent increments, reduce E[X_{n+1}|F_n] to a deterministic function of the current state and one new increment.
- Use case: Section 4.2 martingale, submartingale, and supermartingale verification.
- Tags: martingale, natural-filtration, independent-increments

###### Deterministic martingale-type checks reduce to monotonicity

- ID: `exercise_ch4_deterministic_submartingale_square_supermartingale`
- Kind: calculation-template
- Summary: A deterministic adapted process is a submartingale or supermartingale exactly when the underlying sequence is monotone in the corresponding direction.
- Use case: Exercises testing definitions on simple deterministic examples.
- Tags: submartingale, supermartingale, deterministic-process

###### Localize upcrossing arguments by stopping at bounded levels

- ID: `exercise_ch4_stopped_upcrossing_localization`
- Kind: proof-template
- Summary: Stop a process before it leaves a bounded range so optional inequalities apply, then let the stopping level increase.
- Use case: Upcrossing and convergence exercises where integrability or boundedness needs to be restored.
- Tags: upcrossing, stopping, localization

###### Product martingales may converge to zero by logarithms

- ID: `exercise_ch4_product_martingale_limit_zero`
- Kind: calculation-template
- Summary: For products of independent mean-one factors, examine log factors; a negative accumulated log drift can force almost-sure convergence to zero.
- Use case: Multiplicative martingales and examples where mean is not preserved at the limit.
- Tags: product-martingale, log-transform, almost-sure-limit

###### Dubins-style switching creates many upcrossings

- ID: `exercise_ch4_dubins_upcrossing_switching`
- Kind: construction-template
- Summary: Alternate between betting strategies active below one level and above another to convert repeated upcrossings into predictable-transform gains.
- Use case: Exercises connecting upcrossing inequalities with gambling interpretations.
- Tags: upcrossing, predictable-transform, gambling

###### Bounded increments alone do not make a martingale

- ID: `exercise_ch4_bounded_increment_nonmartingale_counterexample`
- Kind: counterexample-template
- Summary: Construct an adapted process with bounded steps but nonzero conditional drift to show martingale conclusions need a true drift condition.
- Use case: Section 4.3 exercises checking the exact hypotheses of martingale theorems.
- Tags: counterexample, bounded-increments, conditional-drift

###### Summable additive errors preserve convergence

- ID: `exercise_ch4_additive_error_supermartingale_convergence`
- Kind: proof-template
- Summary: Add the tail sum of the error sequence to a near-supermartingale to obtain a genuine supermartingale with the same limiting behavior.
- Use case: Almost-supermartingale convergence arguments.
- Tags: supermartingale, summable-errors, convergence

###### Partition likelihood ratios form martingales

- ID: `exercise_ch4_partition_rn_derivative_martingale`
- Kind: calculation-template
- Summary: On a refining finite partition, the ratio Q(A)/P(A) on the cell containing omega is the conditional expectation of dQ/dP.
- Use case: Radon-Nikodym and likelihood-ratio martingale exercises.
- Tags: radon-nikodym, likelihood-ratio, partition

###### Bernoulli product likelihood ratios and Hellinger sums

- ID: `exercise_ch4_bernoulli_product_hellinger_criterion`
- Kind: criterion
- Summary: For product Bernoulli laws, square-root likelihood overlaps factor, and convergence or singularity is controlled by a summable squared parameter distance.
- Use case: Exercises comparing infinite product measures.
- Tags: bernoulli-product, hellinger, absolute-continuity

###### Branching extinction probabilities are fixed points

- ID: `exercise_ch4_branching_fixed_point_extinction`
- Kind: calculation-template
- Summary: Condition on the first generation to get q = f(q), where f is the offspring generating function; choose the minimal fixed point in [0,1].
- Use case: Branching-process extinction and survival exercises.
- Tags: branching-process, generating-function, fixed-point

###### Optional sampling between two stopping times

- ID: `exercise_ch4_optional_sampling_between_stopping_times`
- Kind: proof-template
- Summary: Apply optional sampling to stopped processes at bounded approximations of S and T, then pass to limits using the available integrability control.
- Use case: Section 4.4 exercises with E[M_T | F_S] and S <= T.
- Tags: optional-sampling, stopping-times, conditioning

###### Doob L1 logarithmic maximal bound

- ID: `exercise_ch4_doob_l1_log_maximal_bound`
- Kind: inequality-template
- Summary: Integrate the weak L1 maximal inequality over levels and split at a scale where the integral of min(1, X/lambda) is finite.
- Use case: Maximal estimates for nonnegative submartingales without Lp control for p>1.
- Tags: doob-inequality, maximal-bound, logarithmic-moment

###### Quadratic martingale exit bounds

- ID: `exercise_ch4_stopped_quadratic_martingale_exit_bound`
- Kind: calculation-template
- Summary: For a martingale with controlled conditional variances, stop M_n^2 minus accumulated variance at the exit time and compare with the boundary size.
- Use case: Exit probability and maximal L2 exercises.
- Tags: quadratic-martingale, exit-time, variance-bound

###### Martingale increments are orthogonal in L2

- ID: `exercise_ch4_martingale_increment_orthogonality_sum`
- Kind: proof-template
- Summary: For i<j, E[D_iD_j]=E[D_i E[D_j|F_{j-1}]]=0, so variances of martingale sums add.
- Use case: L2 convergence, square-function, and maximal inequality exercises.
- Tags: orthogonality, martingale-differences, l2

###### Kronecker normalization for martingale sums

- ID: `exercise_ch4_kronecker_martingale_normalization`
- Kind: proof-template
- Summary: Show a weighted martingale series converges in L2 or a.s., then apply Kronecker's lemma to get normalized partial-sum convergence.
- Use case: Martingale strong laws and weighted-average exercises.
- Tags: kronecker-lemma, strong-law, martingale-series

###### Posterior consistency from Levy upward theorem

- ID: `exercise_ch4_posterior_consistency_by_levy_upward`
- Kind: proof-template
- Summary: Write a posterior probability as E[1_A | F_n]; as observations accumulate and generate A, Levy upward convergence sends it to 1_A.
- Use case: Bayesian consistency and statistical identification exercises.
- Tags: levy-upward, posterior, conditional-probability

###### Dyadic conditional expectations approximate the full variable

- ID: `exercise_ch4_dyadic_conditional_expectation_approximation`
- Kind: construction-template
- Summary: Condition on increasingly fine dyadic sigma-fields; the generated sigma-field is the Borel information, so Levy upward gives convergence.
- Use case: Exercises approximating a variable by finite-information conditional expectations.
- Tags: dyadic, conditional-expectation, levy-upward

###### Levy zero-one law forces absorption or escape events

- ID: `exercise_ch4_levy_zero_one_absorption_or_escape`
- Kind: proof-template
- Summary: If conditional probabilities of a tail event stay bounded away from the event indicator, Levy's zero-one law gives a contradiction.
- Use case: Random-walk, branching, or Markov-chain exercises with eventual absorption events.
- Tags: levy-zero-one, tail-event, absorption

###### Bounded martingales with binary absorbing limits

- ID: `exercise_ch4_bounded_martingale_binary_limit`
- Kind: proof-template
- Summary: A bounded martingale converges a.s.; if the dynamics force every limit to be 0 or 1, the starting value is the probability of limiting at 1.
- Use case: Urn, posterior, and absorbing-state martingale exercises.
- Tags: bounded-martingale, absorbing-state, limit

###### Backward martingale Lp convergence by uniform integrability

- ID: `exercise_ch4_backward_lp_convergence_ui`
- Kind: proof-template
- Summary: For p>1, boundedness in Lp gives uniform integrability, so backward martingale convergence improves to L1 and often Lp convergence.
- Use case: Backward conditional expectation exercises in Section 4.7.
- Tags: backward-martingale, lp, uniform-integrability

###### Pass limits inside backward conditional expectations carefully

- ID: `exercise_ch4_backward_conditional_dct`
- Kind: warning
- Summary: Use domination or uniform integrability before interchanging conditional expectation limits with ordinary limits.
- Use case: Backward martingale convergence exercises involving approximating functions.
- Tags: conditional-dct, backward-martingale, uniform-integrability

###### Exchangeability turns conditioning into hypergeometric sampling

- ID: `exercise_ch4_exchangeable_hypergeometric_conditioning`
- Kind: calculation-template
- Summary: Given the unordered multiset or the total number of successes, exchangeability makes a fixed subcollection have the finite-population hypergeometric law.
- Use case: Exchangeable Bernoulli and finite-sample conditional probability exercises.
- Tags: exchangeability, hypergeometric, conditioning

###### Exchangeable pair covariance constraints

- ID: `exercise_ch4_exchangeable_pair_covariance_positive`
- Kind: calculation-template
- Summary: Use Var(sum X_i) >= 0 to derive lower bounds on pair covariances and identify the limiting covariance structure.
- Use case: Exchangeability exercises about correlations and de Finetti-style limits.
- Tags: exchangeability, covariance, variance

###### U-statistic square limits by pair classification

- ID: `exercise_ch4_u_statistic_pair_square_limit`
- Kind: calculation-template
- Summary: Expand the square of the U-statistic and classify pairs by overlap pattern; only non-negligible classes contribute in the limit.
- Use case: U-statistic convergence exercises under exchangeability or iid assumptions.
- Tags: u-statistic, second-moment, pair-counting

###### Optional stopping with a conditional target

- ID: `exercise_ch4_optional_stopping_ui_conditional_form`
- Kind: proof-template
- Summary: Stop at T wedge n, prove uniform integrability or boundedness, and pass to E[M_T | F_S]=M_S.
- Use case: Random-walk and stopping-time exercises with conditional versions of optional stopping.
- Tags: optional-stopping, uniform-integrability, conditioning

###### Maximal bounds for nonnegative supermartingales

- ID: `exercise_ch4_supermartingale_maximal_bound`
- Kind: inequality-template
- Summary: Stop at the first crossing of a level and use the supermartingale property to bound the crossing probability by the initial mean divided by the level.
- Use case: Ruin, hitting, and overshoot probability estimates.
- Tags: supermartingale, maximal-bound, hitting-time

###### Wald's second equation from a stopped square martingale

- ID: `exercise_ch4_wald_second_equation_stopped_l2`
- Kind: calculation-template
- Summary: For centered iid increments, S_n^2 - n sigma^2 is a martingale; optional stopping gives E[S_T^2]=sigma^2 E[T] when justified.
- Use case: Expected duration and variance identities for stopped random walks.
- Tags: wald-identity, square-martingale, random-walk

###### Generate gambler's ruin moments from martingales

- ID: `exercise_ch4_gambler_ruin_variance_generation`
- Kind: calculation-template
- Summary: Use S_n, S_n^2-n, and higher polynomial martingales stopped at ruin boundaries to solve for hitting probabilities and time moments.
- Use case: Gambler's ruin expected time and variance exercises.
- Tags: gambler-ruin, polynomial-martingales, moments

###### Exponential martingale ruin adjustment

- ID: `exercise_ch4_exponential_martingale_ruin_adjustment`
- Kind: calculation-template
- Summary: Find theta with E exp(theta X)=1, stop exp(theta S_n) at a hitting time, and use boundary values to estimate ruin probabilities.
- Use case: Insurance risk, random-walk ruin, and Lundberg-type inequalities.
- Tags: exponential-martingale, ruin-probability, adjustment-coefficient

###### Fourth-moment martingales bound exit-time moments

- ID: `exercise_ch4_fourth_moment_exit_time`
- Kind: calculation-template
- Summary: Construct a polynomial martingale involving S_n^4, S_n^2, and n; stopping it at an exit time produces second-moment bounds for T.
- Use case: Random-walk exit-time variance and higher-moment exercises.
- Tags: fourth-moment, exit-time, polynomial-martingale

###### Return-time renewal equations via generating functions

- ID: `exercise_ch4_return_time_renewal_generating_function`
- Kind: calculation-template
- Summary: Decompose visits into first return plus future visits, obtaining U(s)=1/(1-F(s)); analyze F(s) near s=1 to read recurrence and expected return time.
- Use case: Section 4.9 random-walk return-time exercise.
- Tags: renewal-equation, generating-functions, return-time

## Chapter 5

### Durrett Chapter 5 LLM Viki: Markov Chains

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter5.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

#### Section Guides

##### 5.1 Examples

- Goal: Recognize Markov structure in standard models and compute their transition probabilities.

- Must master: Markov property, transition matrix, random walk, branching process, Ehrenfest, Wright-Fisher, M/G/1 queue

- Prelim angle: Many exam problems start by asking whether a process is Markov and what its transition law is.

##### 5.2 Construction, Markov Properties

- Goal: Use kernels, path-space construction, Markov property, Chapman-Kolmogorov, and strong Markov property.

- Must master: transition kernels, finite-dimensional distributions, shifted Markov property, Chapman-Kolmogorov, strong Markov property, hitting times

- Prelim angle: Strong Markov arguments power almost every hitting-time and recurrence calculation.

##### 5.3 Recurrence and Transience

- Goal: Classify states and classes using visits, communication, closed classes, and Lyapunov/scale tools.

- Must master: recurrent vs transient, communication classes, decomposition theorem, Foster criterion, birth-death scale functions

- Prelim angle: Expect problems asking whether a chain returns, escapes, or has recurrent classes.

##### 5.4 Recurrence of Random Walks Starred Section

- Goal: Understand dimension-dependent random-walk recurrence through Green functions, limits, and Fourier criteria.

- Must master: Green-function sums, simple random walk by dimension, Chung-Fuchs, Fourier recurrence tests

- Prelim angle: The d<=2 versus d>=3 classification is very high-yield, even if the starred Fourier details are less tested.

##### 5.5 Stationary Measures

- Goal: Construct and identify invariant measures, stationary distributions, reversibility, and positive recurrence.

- Must master: stationary measure, detailed balance, cycle condition, return-cycle occupation measure, positive recurrence, mean return time

- Prelim angle: Equilibrium computations usually reduce to detailed balance, normalization, or mean return times.

##### 5.6 Asymptotic Behavior

- Goal: Connect recurrence and stationarity to long-run transition probabilities and ergodic averages.

- Must master: renewal limits, period, aperiodic convergence, coupling, additive functional LLN

- Prelim angle: Use irreducible + positive recurrent + aperiodic as the main convergence-to-stationarity checklist.

##### 5.7 Periodicity, Tail Sigma-Field Starred Section

- Goal: Handle periodic chains by cyclic classes and understand tail-event zero-one behavior.

- Must master: cyclic classes, periodic convergence, tail sigma-field, coupling zero-one arguments

- Prelim angle: Periodicity is the standard hidden reason a stationary chain does not have ordinary p^n convergence.

##### 5.8 General State Space Starred Section

- Goal: Translate countable-state recurrence, stationarity, and convergence to Harris chains.

- Must master: Harris recurrence, small sets, split chain, sigma-finite invariant measure, Harris convergence, GI/G/1 queue

- Prelim angle: Useful for advanced problems with continuous state spaces or queueing recursions.

#### Knowledge Pieces

##### Countable-state Markov property

- ID: `durrett_ch5_markov_property_countable`

- Section: 5.1 Examples

- Kind: definition

- Summary: A temporally homogeneous countable-state Markov chain satisfies P(X_{n+1}=j | X_n=i, past)=P(X_{n+1}=j | X_n=i)=p(i,j).

- Proof idea: The current state is a sufficient statistic for predicting the next state, so the transition matrix contains all one-step dynamics.

- Exam use: Use this as the first diagnostic for deciding whether a proposed process is Markov and for computing transition probabilities.

- Pitfall: A function of a Markov chain need not be Markov unless the retained state contains enough information.

- Tags: markov-property, transition-matrix, countable-state

##### Random walk as a Markov chain

- ID: `durrett_ch5_random_walk_chain`

- Section: 5.1 Examples

- Kind: example-pattern

- Summary: If X_n=X_0+xi_1+...+xi_n with iid increments on Z^d, then p(i,j)=mu({j-i}).

- Proof idea: Condition on X_n; the next state is obtained by adding the independent increment xi_{n+1}.

- Exam use: Use whenever increments are independent and stationary; transition probabilities depend only on displacement.

- Pitfall: A random walk often has no finite equilibrium on infinite groups even though it is Markov.

- Tags: random-walk, increments, translation-invariance

##### Branching process transition kernel

- ID: `durrett_ch5_branching_process_chain`

- Section: 5.1 Examples

- Kind: example-pattern

- Summary: For a Galton-Watson process, p(i,j)=P(xi_1+...+xi_i=j), where each current individual independently produces offspring.

- Proof idea: Given X_n=i, the next generation is the sum of i iid offspring counts.

- Exam use: Recognize absorbing extinction state 0 and use generating functions for transition calculations.

- Pitfall: The process is Markov in the population size, but it typically does not converge to a nontrivial equilibrium.

- Tags: branching-process, offspring, absorbing-state

##### Ehrenfest urn chain

- ID: `durrett_ch5_ehrenfest_chain`

- Section: 5.1 Examples

- Kind: example-pattern

- Summary: With r balls and state k equal to the number in the first urn, p(k,k+1)=(r-k)/r and p(k,k-1)=k/r.

- Proof idea: One randomly selected ball changes urns, increasing or decreasing k according to which urn the ball came from.

- Exam use: A canonical finite birth-death chain for reversibility, stationary distributions, and periodicity.

- Pitfall: The chain alternates parity, so convergence of p^n(k,j) must account for period 2 unless laziness is added.

- Tags: ehrenfest, birth-death, finite-chain, periodicity

##### Wright-Fisher transition law

- ID: `durrett_ch5_wright_fisher_chain`

- Section: 5.1 Examples

- Kind: example-pattern

- Summary: In a population of N genes, the number of A alleles has binomial transition p(i,j)=C(N,j) rho_i^j(1-rho_i)^{N-j}; without mutation rho_i=i/N, with mutation rho_i=(i/N)(1-u)+((N-i)/N)v.

- Proof idea: The next generation is sampled with replacement from the current generation, with mutation modifying the success probability.

- Exam use: Use for absorption/fixation problems, martingale hitting probabilities, and finite-chain equilibrium with mutation.

- Pitfall: Without mutation, 0 and N are absorbing; with positive mutation rates they are not.

- Tags: wright-fisher, binomial-transition, mutation, absorption

##### M/G/1 embedded queue chain

- ID: `durrett_ch5_mg1_queue_chain`

- Section: 5.1 Examples

- Kind: example-pattern

- Summary: At service-start epochs, X_{n+1}=(X_n+xi_{n+1})^+, where P(xi=k-1)=a_k and a_k is the chance k arrivals occur during one service time.

- Proof idea: Between service starts, arrivals during the service time add customers while the served customer leaves; the positive part handles an empty queue.

- Exam use: Use drift E xi=mean arrivals per service minus 1 to classify recurrence and stability.

- Pitfall: Do not confuse the continuous-time queue with the embedded discrete chain at service-start times.

- Tags: queue, mg1, reflected-random-walk, drift

##### General transition probability

- ID: `durrett_ch5_general_transition_probability`

- Section: 5.2 Construction, Markov Properties

- Kind: definition

- Summary: On a measurable state space, p(x,A) is a transition probability when A -> p(x,A) is a probability measure and x -> p(x,A) is measurable.

- Proof idea: The two requirements make integration over paths well-defined and allow conditioning on X_n.

- Exam use: Use this language for chains beyond countable state spaces, including queues and continuous densities.

- Pitfall: For general spaces, p(x,y) is usually not a number; the kernel is p(x,A).

- Tags: transition-kernel, measurable-space, general-state-space

##### Finite-dimensional construction of a chain

- ID: `durrett_ch5_finite_dimensional_construction`

- Section: 5.2 Construction, Markov Properties

- Kind: construction

- Summary: Given initial law mu and kernel p, the finite-dimensional laws are iterated integrals mu(dx_0)p(x_0,dx_1)...p(x_{n-1},dx_n).

- Proof idea: The consistency of these marginals lets the extension theorem create a path-space process.

- Exam use: Justifies statements that a Markov chain with a specified initial distribution and transition kernel exists.

- Pitfall: The formula gives path probabilities only for measurable cylinder events, then extension supplies the full path law.

- Tags: construction, finite-dimensional-distributions, path-space

##### Transition operator notation

- ID: `durrett_ch5_expectation_operator_notation`

- Section: 5.2 Construction, Markov Properties

- Kind: notation

- Summary: For bounded measurable f, Pf(x)=E_x f(X_1)=integral f(y)p(x,dy); iterates P^n describe n-step expectations.

- Proof idea: Integrating one step at a time turns the transition kernel into a linear operator.

- Exam use: Useful for harmonic equations, hitting probabilities, expected hitting times, and martingale checks.

- Pitfall: The same symbol p may denote a kernel or a matrix; P as an operator acts on functions.

- Tags: transition-operator, expectation, harmonic-functions

##### Markov property with path shifts

- ID: `durrett_ch5_markov_property_shift`

- Section: 5.2 Construction, Markov Properties

- Kind: theorem

- Summary: For bounded future functionals Y, E_x[Y o theta_n | F_n]=E_{X_n}Y.

- Proof idea: Check cylinder future events, extend by a monotone-class argument, and use the construction formula.

- Exam use: Transforms future-path questions after time n into a fresh chain started at X_n.

- Pitfall: The future functional must be evaluated on the shifted path; forgetting the shift changes the event.

- Tags: markov-property, shift-operator, monotone-class

##### Chapman-Kolmogorov equations

- ID: `durrett_ch5_chapman_kolmogorov`

- Section: 5.2 Construction, Markov Properties

- Kind: theorem

- Summary: The n-step kernels satisfy p^{m+n}(x,z)=sum_y p^m(x,y)p^n(y,z) in countable spaces, with the analogous integral formula in general spaces.

- Proof idea: Condition on the state at the intermediate time m and apply the Markov property.

- Exam use: Compute multi-step transitions, prove communication, and derive renewal decompositions for return probabilities.

- Pitfall: For general spaces, replace sums over y by integration against p^m(x,dy).

- Tags: chapman-kolmogorov, n-step-transition, semigroup

##### Strong Markov property

- ID: `durrett_ch5_strong_markov_property`

- Section: 5.2 Construction, Markov Properties

- Kind: theorem

- Summary: At a stopping time T, the post-T process behaves like a fresh chain started from X_T on the event T<infinity.

- Proof idea: Approximate the stopping time by its atoms {T=n}, apply the ordinary Markov property on each atom, and sum.

- Exam use: The main engine for hitting-time decompositions, renewal arguments, recurrence proofs, and reflection arguments.

- Pitfall: T must be a stopping time; optional-looking random times that see the future do not qualify.

- Tags: strong-markov, stopping-time, hitting-times

##### Hitting and return time decomposition

- ID: `durrett_ch5_hitting_return_decomposition`

- Section: 5.2 Construction, Markov Properties

- Kind: proof-template

- Summary: Events involving visits to a state or set can be decomposed at the first hitting time and restarted by the strong Markov property.

- Proof idea: Split according to T_y=k or T_A=k, then apply the strong Markov property to the shifted future.

- Exam use: Use for equations like P_x(T_z<infinity) >= P_x(T_y<infinity)P_y(T_z<infinity) and for first-step analysis.

- Pitfall: Use T_y=inf{n>=1:X_n=y} for returns and V_A=inf{n>=0:X_n in A} for entrance; the indexing matters.

- Tags: hitting-time, return-time, first-step-analysis

##### Reflection principle for symmetric random walk

- ID: `durrett_ch5_reflection_principle`

- Section: 5.2 Construction, Markov Properties

- Kind: theorem

- Summary: For one-dimensional simple symmetric random walk, paths crossing a level can be reflected after the first hitting time to convert maximum events into endpoint events.

- Proof idea: Stop at the first hit of the barrier and flip the signs of all later increments, giving a bijection of path sets.

- Exam use: Fast route to distributions of maxima and hitting probabilities for simple random walk.

- Pitfall: The clean reflection bijection uses symmetry and nearest-neighbor increments; it does not transfer unchanged to arbitrary walks.

- Tags: reflection-principle, simple-random-walk, maximum

##### Expected visits criterion

- ID: `durrett_ch5_recurrence_visit_criterion`

- Section: 5.3 Recurrence and Transience

- Kind: theorem

- Summary: A state y is recurrent iff E_y N(y)=sum_n p^n(y,y)=infinity; if transient this expected visit count is finite.

- Proof idea: After each return to y, the strong Markov property restarts the process, so the number of returns has a geometric structure.

- Exam use: Use Green-function sums to classify states, especially for random walks.

- Pitfall: The criterion is for visits starting from y; from another x, accessibility must be handled separately.

- Tags: recurrence, transience, green-function, return-count

##### Recurrence transfers through communication

- ID: `durrett_ch5_communication_recurrence_transfer`

- Section: 5.3 Recurrence and Transience

- Kind: theorem

- Summary: If x is recurrent and rho_xy>0, then y is recurrent and rho_yx=1.

- Proof idea: A recurrent x is visited infinitely often; successful excursions from x to y eventually occur, and returning to x forces y to communicate back.

- Exam use: Shows recurrence is a class property inside communicating classes.

- Pitfall: Accessibility in only one direction is not symmetric unless recurrence is known.

- Tags: communication, recurrence-class, irreducibility

##### Finite closed classes contain recurrent states

- ID: `durrett_ch5_finite_closed_recurrent_class`

- Section: 5.3 Recurrence and Transience

- Kind: theorem

- Summary: Every finite closed set contains a recurrent state; if the finite closed set is irreducible, all its states are recurrent.

- Proof idea: A chain trapped in a finite set must visit at least one state infinitely often, then recurrence transfers through communication.

- Exam use: Use to classify finite Markov chains and prove absorbing/recurrent structure.

- Pitfall: The set must be closed; otherwise the chain can leave and never return.

- Tags: finite-chain, closed-class, recurrence

##### Decomposition theorem

- ID: `durrett_ch5_decomposition_theorem`

- Section: 5.3 Recurrence and Transience

- Kind: theorem

- Summary: The recurrent states split into disjoint irreducible closed classes, while every transient state is visited only finitely often almost surely.

- Proof idea: Use communication equivalence for recurrent states and the finite expected visits criterion for transients.

- Exam use: Organizes the long-run behavior of countable chains before stationary distributions enter.

- Pitfall: Closed recurrent classes need not be finite; irreducibility is within each class, not necessarily the whole state space.

- Tags: decomposition, recurrent-classes, transient-states

##### Foster-type recurrence criterion

- ID: `durrett_ch5_foster_supermartingale_recurrence`

- Section: 5.3 Recurrence and Transience

- Kind: criterion

- Summary: For an irreducible chain, a nonnegative function phi with E_x phi(X_1)<=phi(x) off a finite set and phi(x)->infinity can force recurrence.

- Proof idea: Stop phi(X_n) on leaving large finite regions and use optional-stopping/supermartingale estimates to prevent escape to infinity.

- Exam use: A powerful recurrence test for birth-death chains, queues, and chains with inward drift.

- Pitfall: Check the direction of drift carefully; superharmonic behavior outside a finite set is the recurrence signal.

- Tags: foster-criterion, supermartingale, lyapunov, recurrence

##### Birth-death scale function

- ID: `durrett_ch5_birth_death_scale_function`

- Section: 5.3 Recurrence and Transience

- Kind: formula

- Summary: For a birth-death chain, harmonic scale functions solve p_x h(x+1)+q_x h(x-1)=h(x) and give explicit two-sided hitting probabilities.

- Proof idea: Rewrite the harmonic equation in first differences so ratios telescope as products q_i/p_i.

- Exam use: Use for gambler's ruin probabilities and recurrence tests on {0,1,2,...}.

- Pitfall: Boundary conventions at 0 matter; write the model's p_0 and q_0 before applying formulas.

- Tags: birth-death, scale-function, hitting-probability

##### Birth-death recurrence test

- ID: `durrett_ch5_birth_death_recurrence_test`

- Section: 5.3 Recurrence and Transience

- Kind: criterion

- Summary: For a birth-death chain on nonnegative integers, recurrence of 0 is determined by divergence of the scale sum built from products q_i/p_i.

- Proof idea: Let the upper boundary M tend to infinity in the two-sided hitting formula.

- Exam use: High-yield test for nearest-neighbor chains with state-dependent drift.

- Pitfall: Small asymptotic drift terms such as C/j can decide the boundary between recurrence and transience.

- Tags: birth-death, recurrence-test, scale-sum

##### Recurrent values form a closed subgroup

- ID: `durrett_ch5_random_walk_recurrent_values`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: For a random walk on R^d, the set of recurrent values is either empty or a closed subgroup of R^d.

- Proof idea: Use independence and translation invariance to show the set is closed under differences and limits.

- Exam use: Clarifies what recurrence can mean outside lattice state spaces.

- Pitfall: Returning near a value is a topological notion in R^d, not necessarily exact equality.

- Tags: random-walk, recurrent-values, closed-subgroup

##### Equivalent random-walk recurrence criteria

- ID: `durrett_ch5_random_walk_recurrence_equivalences`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: For random walks, recurrence can be characterized by infinitely many visits to neighborhoods, divergence of occupation sums, and Green-function criteria.

- Proof idea: Relate neighborhood visits to the Markov property and use zero-one/renewal arguments.

- Exam use: Choose the criterion that matches the data: local probabilities, characteristic functions, or limit theorems.

- Pitfall: The exact form differs between lattice and nonlattice settings; keep the state-space topology visible.

- Tags: random-walk, recurrence-criteria, green-function

##### Simple random walk recurrence by dimension

- ID: `durrett_ch5_simple_random_walk_dimension`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: Simple random walk is recurrent in dimensions 1 and 2 and transient in dimensions 3 and higher.

- Proof idea: Estimate the return probabilities: they behave like n^{-d/2}, whose series diverges for d<=2 and converges for d>=3.

- Exam use: A central classification result and a common comparison model for Markov-chain recurrence.

- Pitfall: Parity affects exact return times but not the convergence/divergence classification.

- Tags: simple-random-walk, dimension, recurrence, transience

##### Chung-Fuchs one-dimensional recurrence pattern

- ID: `durrett_ch5_chung_fuchs_one_dimension`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: In one dimension, centered weak-law behavior is the key condition behind recurrence for broad random walks.

- Proof idea: Use truncation and characteristic-function/Fourier criteria to control occupation near the origin.

- Exam use: Use when increments are not nearest-neighbor but have no drift on the natural scale.

- Pitfall: Nonzero drift typically pushes the walk to infinity and destroys recurrence.

- Tags: chung-fuchs, one-dimensional-random-walk, drift

##### Two-dimensional normal-limit recurrence

- ID: `durrett_ch5_two_dimensional_normal_recurrence`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: A two-dimensional random walk with S_n/sqrt(n) converging to a nondegenerate normal law is recurrent.

- Proof idea: Use the local/weak normal approximation to show enough mass returns to fixed neighborhoods for the occupation sum to diverge.

- Exam use: Recognize recurrence for centered finite-variance planar walks.

- Pitfall: A degenerate limiting covariance needs separate lower-dimensional analysis.

- Tags: two-dimensional-random-walk, normal-limit, recurrence

##### Fourier recurrence criterion

- ID: `durrett_ch5_fourier_recurrence_criterion`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: criterion

- Summary: Random-walk recurrence can be tested through integrals involving 1/(1-phi(t)), where phi is the increment characteristic function.

- Proof idea: Parseval-type identities convert occupation sums into Fourier integrals over powers of phi.

- Exam use: Useful for non-nearest-neighbor walks and for proving no truly three-dimensional walk is recurrent.

- Pitfall: The singularity near t=0 is decisive; away from zero the integral is usually harmless.

- Tags: fourier, characteristic-functions, recurrence

##### No truly three-dimensional recurrent random walk

- ID: `durrett_ch5_no_truly_three_dimensional_recurrence`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: A random walk with genuinely three-dimensional increment support cannot be recurrent.

- Proof idea: Near the origin, the Fourier denominator behaves too singularly in dimension 3 for recurrence-compatible divergence.

- Exam use: Use as a broad transience result beyond simple random walk.

- Pitfall: If the walk actually lives in a lower-dimensional subgroup, reduce the dimension before applying the theorem.

- Tags: three-dimensional, random-walk, transience, fourier

##### Stationary measures and distributions

- ID: `durrett_ch5_stationary_measure_definition`

- Section: 5.5 Stationary Measures

- Kind: definition

- Summary: A measure mu is stationary when mu p=mu; if mu(S)=1 it is a stationary distribution.

- Proof idea: Stationarity says one transition step leaves the law unchanged.

- Exam use: Find equilibria, normalize invariant measures, and connect long-run proportions to return times.

- Pitfall: An infinite stationary measure need not be a probability distribution and does not by itself imply equilibrium probabilities.

- Tags: stationary-measure, invariant-measure, equilibrium

##### Reversibility and detailed balance

- ID: `durrett_ch5_reversibility_detailed_balance`

- Section: 5.5 Stationary Measures

- Kind: criterion

- Summary: If mu(x)p(x,y)=mu(y)p(y,x) for all x,y, then mu is stationary and the chain is reversible under mu.

- Proof idea: Sum the detailed-balance identity over x to get stationarity; path probabilities are unchanged by time reversal.

- Exam use: The fastest way to find stationary distributions for birth-death, Ehrenfest, and many urn chains.

- Pitfall: Detailed balance is sufficient but not necessary for stationarity unless reversibility is required.

- Tags: reversibility, detailed-balance, stationary-distribution

##### Kolmogorov cycle condition

- ID: `durrett_ch5_kolmogorov_cycle_condition`

- Section: 5.5 Stationary Measures

- Kind: theorem

- Summary: For an irreducible chain, reversibility is characterized by equality of transition-probability products around every directed cycle and its reverse.

- Proof idea: Multiply detailed-balance equations around a cycle for necessity; construct ratios along paths for sufficiency.

- Exam use: Use to test whether a proposed chain can be reversible without solving for pi first.

- Pitfall: The condition is about all cycles; checking only two-state moves can miss circulation.

- Tags: kolmogorov-cycle, reversibility, cycles

##### Stationary measure from one recurrent cycle

- ID: `durrett_ch5_stationary_measure_from_returns`

- Section: 5.5 Stationary Measures

- Kind: theorem

- Summary: If x is recurrent and T_x is the first positive return time, then expected occupation counts before T_x define a stationary measure with mass 1 at x.

- Proof idea: Use the strong Markov property to balance expected exits and entries over a regenerative cycle.

- Exam use: Construct invariant measures for recurrent irreducible chains without guessing.

- Pitfall: The measure may have infinite total mass when the chain is null recurrent.

- Tags: occupation-measure, regeneration, stationary-measure, return-time

##### Uniqueness of stationary measure in irreducible recurrent chains

- ID: `durrett_ch5_stationary_measure_uniqueness_recurrent`

- Section: 5.5 Stationary Measures

- Kind: theorem

- Summary: For an irreducible recurrent countable chain, the stationary measure is unique up to constant multiples.

- Proof idea: Compare any invariant measure with the regenerative occupation measure normalized at one state.

- Exam use: Lets you identify all invariant measures once one candidate is found.

- Pitfall: Uniqueness up to scale does not mean a stationary distribution exists; total mass may be infinite.

- Tags: irreducible, recurrent, stationary-measure, uniqueness

##### Stationary probability and mean return time

- ID: `durrett_ch5_positive_recurrence_return_time`

- Section: 5.5 Stationary Measures

- Kind: theorem

- Summary: For an irreducible chain with stationary distribution pi, pi(y)=1/E_y T_y, so states with finite mean return time are positive recurrent.

- Proof idea: Apply the regenerative stationary measure over one return cycle and normalize by its total expected length.

- Exam use: Compute stationary probabilities through expected return times and classify positive versus null recurrence.

- Pitfall: Recurrence only says T_y is finite almost surely; positive recurrence requires finite expectation.

- Tags: positive-recurrence, mean-return-time, stationary-distribution

##### Positive recurrence equivalences

- ID: `durrett_ch5_positive_recurrence_equivalences`

- Section: 5.5 Stationary Measures

- Kind: theorem

- Summary: For an irreducible chain, existence of a stationary distribution, finite mean return times, and positive recurrence are equivalent.

- Proof idea: Normalize the recurrent-cycle stationary measure when its total mass is finite; conversely use stationarity to derive finite return times.

- Exam use: A standard checklist for proving an irreducible chain has an equilibrium law.

- Pitfall: In infinite state spaces, irreducible recurrent chains can be null recurrent and fail to have a stationary distribution.

- Tags: positive-recurrence, stationary-distribution, return-times

##### Birth-death stationary distribution

- ID: `durrett_ch5_birth_death_stationary_distribution`

- Section: 5.5 Stationary Measures

- Kind: formula

- Summary: For birth-death chains, detailed balance gives pi(x) proportional to products of birth rates divided by death rates, if the normalizing sum is finite.

- Proof idea: Solve pi(x)p_x=pi(x+1)q_{x+1} recursively and normalize.

- Exam use: Fast equilibrium computation for queues, Ehrenfest-type chains, and one-dimensional population models.

- Pitfall: The unnormalized weights may define an invariant measure even when their sum diverges.

- Tags: birth-death, stationary-distribution, detailed-balance

##### M/G/1 stability and stationarity

- ID: `durrett_ch5_mg1_stability_stationarity`

- Section: 5.5 Stationary Measures

- Kind: example-pattern

- Summary: For the embedded M/G/1 queue, stability/positive recurrence occurs when the mean number of arrivals during one service time is less than 1.

- Proof idea: Compare the reflected queue length to a random walk with drift E xi=mu-1 and use recurrence/return-time arguments.

- Exam use: Use drift less than zero as the queue stability condition.

- Pitfall: Recurrence and stationary behavior fail at or above critical load in different ways; do not treat mu=1 as stable.

- Tags: mg1, queue-stability, positive-recurrence, drift

##### Renewal limit for return probabilities

- ID: `durrett_ch5_renewal_limit_return_probabilities`

- Section: 5.6 Asymptotic Behavior

- Kind: theorem

- Summary: If y is recurrent, then p^n(y,y) has asymptotics governed by the renewal theorem for the return-time distribution; positive recurrence gives limits tied to 1/E_y T_y.

- Proof idea: Decompose visits to y into renewals generated by successive return times.

- Exam use: Explains why return-time periods and mean cycle lengths control long-run transition probabilities.

- Pitfall: Periodicity can force p^n(y,y)=0 on many n, so limits may only exist along arithmetic subsequences.

- Tags: renewal-theorem, return-probabilities, asymptotics

##### Period of a state

- ID: `durrett_ch5_period_definition`

- Section: 5.6 Asymptotic Behavior

- Kind: definition

- Summary: The period of state x is the greatest common divisor of {n>=1:p^n(x,x)>0}; irreducible communicating states share the same period.

- Proof idea: Use concatenation of paths and communication to transfer possible return-time arithmetic between states.

- Exam use: Check whether convergence to stationarity can hold at every time or only along residue classes.

- Pitfall: A chain can be irreducible and positive recurrent but still fail ordinary convergence because of period greater than 1.

- Tags: periodicity, aperiodic, irreducibility

##### Aperiodic convergence theorem

- ID: `durrett_ch5_aperiodic_convergence_theorem`

- Section: 5.6 Asymptotic Behavior

- Kind: theorem

- Summary: If a countable chain is irreducible, aperiodic, and has stationary distribution pi, then p^n(x,y) -> pi(y).

- Proof idea: Couple two independent chains through the product chain and show they meet with probability tending to one.

- Exam use: Main equilibrium convergence theorem for prelim Markov-chain problems.

- Pitfall: Irreducible and stationary are not enough; without aperiodicity the raw n-step probabilities may oscillate.

- Tags: convergence-to-stationarity, aperiodic, coupling, positive-recurrence

##### Coupling bound for convergence

- ID: `durrett_ch5_coupling_for_finite_chains`

- Section: 5.6 Asymptotic Behavior

- Kind: proof-template

- Summary: If two copies of a Markov chain are run together after meeting, then total variation distance is bounded by the probability their coupling time exceeds n.

- Proof idea: Construct the product chain, make the two coordinates coalesce at the diagonal, and compare events before and after meeting.

- Exam use: Use for finite irreducible aperiodic chains and for quantitative convergence estimates.

- Pitfall: The coupling must preserve the correct marginal transition law for each coordinate.

- Tags: coupling, total-variation, mixing

##### Strong law for additive functionals

- ID: `durrett_ch5_additive_functional_lln`

- Section: 5.6 Asymptotic Behavior

- Kind: theorem

- Summary: For an irreducible positive recurrent chain with stationary law pi, time averages of suitable f(X_n) converge to sum_x pi(x)f(x).

- Proof idea: Break the path into regenerative cycles between visits to a reference state and apply iid cycle laws.

- Exam use: Use to turn long-run sample averages into stationary expectations.

- Pitfall: Integrability under pi is essential; positive recurrence alone does not control arbitrary unbounded rewards.

- Tags: ergodic-theorem, additive-functional, time-average

##### Periodic cyclic classes

- ID: `durrett_ch5_periodic_convergence_classes`

- Section: 5.7 Periodicity, Tail Sigma-Field Starred Section

- Kind: theorem

- Summary: For an irreducible recurrent chain of period d, the state space splits into d cyclic classes and the d-step chain on each class is aperiodic.

- Proof idea: Group states according to hitting-time residues modulo d and use the gcd definition of period.

- Exam use: Use to repair convergence statements for periodic chains by passing to subsequences n congruent to r mod d.

- Pitfall: The stationary distribution is still a distribution on all states, but mass is visited cyclically rather than approached at all times.

- Tags: periodicity, cyclic-classes, periodic-convergence

##### Periodic convergence theorem

- ID: `durrett_ch5_periodic_convergence_theorem`

- Section: 5.7 Periodicity, Tail Sigma-Field Starred Section

- Kind: theorem

- Summary: For irreducible positive recurrent chains with period d, p^n(x,y) converges along the compatible residue class to d*pi(y) and is zero on incompatible residues.

- Proof idea: Apply the aperiodic convergence theorem to the d-step chain on the cyclic class containing y.

- Exam use: Use when examples such as simple random walk on bipartite graphs oscillate forever.

- Pitfall: The factor d appears because the d-step chain's stationary law is pi restricted to one cyclic class and renormalized.

- Tags: periodic-convergence, cyclic-classes, stationary-distribution

##### Tail sigma-field triviality via coupling

- ID: `durrett_ch5_tail_sigma_field_triviality_pattern`

- Section: 5.7 Periodicity, Tail Sigma-Field Starred Section

- Kind: proof-template

- Summary: For suitable irreducible recurrent chains, tail events have probability 0 or 1 because coupled copies eventually share the same future behavior.

- Proof idea: Represent two copies, couple them after a meeting or cyclic alignment, and observe that tail events are unchanged by finite initial segments.

- Exam use: Use for zero-one laws about eventual behavior of recurrent Markov chains and simple random walk.

- Pitfall: Tail events are not the same as invariant events at a fixed time; they ignore every finite prefix.

- Tags: tail-sigma-field, zero-one-law, coupling

##### Harris recurrence

- ID: `durrett_ch5_harris_recurrence`

- Section: 5.8 General State Space Starred Section

- Kind: definition

- Summary: A general-state Markov chain is Harris recurrent when it repeatedly hits every set of positive reference measure from relevant starting points.

- Proof idea: A reference measure replaces countable-state point accessibility, letting recurrence be stated for measurable sets.

- Exam use: Use as the general-state analogue of irreducible recurrence.

- Pitfall: In continuous spaces, single points often have probability zero, so point-return definitions are too strong or meaningless.

- Tags: harris-recurrence, general-state-space, reference-measure

##### Small sets and split-chain idea

- ID: `durrett_ch5_small_set_split_chain`

- Section: 5.8 General State Space Starred Section

- Kind: construction

- Summary: A small set has a minorization that lets one split transitions into regeneration attempts and residual motion.

- Proof idea: Use the minorization to add an artificial atom, reducing parts of the general-state chain to countable-style regeneration.

- Exam use: The conceptual bridge from countable recurrent-chain proofs to Harris-chain stationary and convergence theorems.

- Pitfall: Minorization is a structural condition; it is not just positive probability of hitting a set.

- Tags: small-set, minorization, split-chain, regeneration

##### Stationary measure for recurrent Harris chains

- ID: `durrett_ch5_harris_stationary_measure`

- Section: 5.8 General State Space Starred Section

- Kind: theorem

- Summary: In the recurrent Harris setting, there is a sigma-finite stationary measure, and it is unique up to scale under the appropriate irreducibility assumptions.

- Proof idea: Construct a regenerative stationary measure using the split chain and then project back to the original chain.

- Exam use: Generalizes countable-state invariant-measure construction to continuous state spaces.

- Pitfall: Sigma-finite stationary measure is not automatically a stationary distribution; total mass decides positive recurrence.

- Tags: harris-chain, stationary-measure, sigma-finite, regeneration

##### Aperiodic Harris convergence theorem

- ID: `durrett_ch5_harris_convergence_theorem`

- Section: 5.8 General State Space Starred Section

- Kind: theorem

- Summary: An aperiodic positive recurrent Harris chain with stationary distribution converges to that stationary distribution in total variation from suitable starting laws.

- Proof idea: Use split-chain regeneration and coupling, paralleling the countable-state aperiodic convergence proof.

- Exam use: Use for continuous-state Markov models where transition densities make pointwise matrix methods unavailable.

- Pitfall: The theorem requires Harris recurrence and aperiodicity; a stationary density alone may not give convergence from every start.

- Tags: harris-chain, total-variation, convergence, aperiodic

##### GI/G/1 queue as a reflected random walk

- ID: `durrett_ch5_gig1_queue_storage_model`

- Section: 5.8 General State Space Starred Section

- Kind: example-pattern

- Summary: The waiting-time recursion W_{n+1}=(W_n+eta_n-zeta_n)^+ is a general-state Markov chain and storage model.

- Proof idea: Service requirements add workload and interarrival times subtract available service time, with reflection at zero.

- Exam use: Use drift E eta < E zeta for stability and Harris-chain tools for stationary waiting-time distributions.

- Pitfall: The embedded workload is continuous-state, so countable transition-matrix formulas do not apply directly.

- Tags: gig1, storage-model, reflected-random-walk, harris-chain

### Chapter 5 Exercise Viki

#### Chapter 5 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter5/Chapter5Exercises.tex`
Source PDF: `Probability/Exercises/Chapter5/Chapter5Exercises.pdf`

This dataset turns the solved Chapter 5 exercises into retrieval-ready records, reusable method cards, and exercise-derived knowledge pieces.

Solved sections currently included: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, and 5.8.

##### Files

- `chapter5_exercise_records.jsonl`: one record per solved exercise, including question, solution, Viki IDs used, and method tags.
- `chapter5_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter5_exercise_new_knowledge.jsonl`: reusable proof/calculation/classification patterns extracted from the exercises.
- `chapter5_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.
- `chapter5_exercise_viki.md`: human-readable overview.

##### Section Method Cards

###### 5.1 - Markov-chain examples and transition kernels

Identify the state variable that makes the future depend only on the present; compute transition probabilities by conditioning on the next independent draw, offspring, ball swap, or allele sample.

Tags: markov-property, transition-kernel, example-models, state-choice

###### 5.2 - Markov property, stopping, hitting, exit, and martingale equations

Use conditional independence from the Markov property, decompose at first hitting times, and solve finite exit or expected-time problems through harmonic and Poisson equations.

Tags: strong-markov, hitting-time, harmonic-equation, martingale

###### 5.3 - Recurrence, transience, birth-death tests, and Lyapunov criteria

Classify recurrence through return sums, finite closed classes, scale functions, and Foster-Lyapunov supermartingales; use asymptotic product tests for birth-death boundaries.

Tags: recurrence, transience, birth-death, lyapunov, scale-function

###### 5.4 - Random-walk recurrence and harmonic-function consequences

Use ladder variables, recurrence alternatives, and random-walk visits to convert path behavior into Liouville theorems for superharmonic or bounded harmonic functions.

Tags: random-walk, ladder-variables, liouville, harmonic-functions

###### 5.5 - Stationary measures, reversibility, cycle formula, and positive recurrence

Find invariant laws using detailed balance, cycle occupation measures, return-time identities, and drift/regeneration arguments for queues.

Tags: stationary-distribution, detailed-balance, cycle-trick, positive-recurrence

###### 5.6 - Convergence to stationarity, coupling rates, and regenerative limit theorems

Prove convergence by coupling, obtain finite-state exponential rates through uniform block coupling, and use regenerative cycles for additive LLNs, CLTs, and ratio limits.

Tags: coupling, ergodic-theorem, regeneration, ratio-limit, clt

###### 5.8 - Harris chains, split-chain atoms, GI/G/1 queues, and continuous-state recurrence

Reduce Harris-chain questions to the split-chain atom, transfer countable-state return and stationary-measure arguments, and analyze reflected random walks by drift and path reversal.

Tags: harris-chain, split-chain, atom, gig1, reflected-random-walk

##### New Knowledge Pieces

###### State sufficiency test for the Markov property

- ID: `exercise_ch5_state_sufficiency_test`
- Kind: diagnostic-template
- Summary: A proposed process is Markov only if the retained state contains all information needed to compute the next-step law; record maxima fail when the current walk location is omitted.
- Use case: Exercises 5.1.1, 5.1.2, 5.1.3, and other state-selection problems.
- Tags: markov-property, state-choice, counterexample

###### Compute transitions from the one-step mechanism

- ID: `exercise_ch5_transition_from_one_step_mechanism`
- Kind: calculation-template
- Summary: Given the present state, enumerate the next independent draw, swap, birth, or arrival and translate the possible outcomes into transition probabilities.
- Use case: Coupon, pair-chain, Bernoulli-Laplace, Wright-Fisher, and queue transition computations.
- Tags: transition-matrix, conditioning, examples

###### Bayesian predictive state for hidden-parameter chains

- ID: `exercise_ch5_hidden_parameter_predictive_markov`
- Kind: calculation-template
- Summary: When a hidden parameter is shared across trials, update its posterior from a sufficient statistic and use the posterior mean as the next-step predictive probability.
- Use case: Exercise 5.1.6 and temporally inhomogeneous Markov chains from exchangeable coin flips.
- Tags: bayesian-update, sufficient-statistic, inhomogeneous-markov

###### Mendelian pair transition matrix

- ID: `exercise_ch5_mendelian_pair_transition`
- Kind: calculation-template
- Summary: For unordered genotype-pair states, compute one-offspring genotype probabilities (p,q,r) and map two independent offspring to probabilities p^2, 2pq, 2pr, q^2, 2qr, r^2.
- Use case: Brother-sister mating transition and absorption computations.
- Tags: genetics, transition-matrix, mendelian

###### Past and future conditional independence

- ID: `exercise_ch5_conditional_independence_past_future`
- Kind: proof-template
- Summary: For A in the past and B in the future, condition first on the present sigma-field; the Markov property turns E(1_B|F_n) into a function of X_n.
- Use case: Exercise 5.2.1 and conditional independence arguments.
- Tags: markov-property, conditional-independence, tower-property

###### First entrance decomposition

- ID: `exercise_ch5_first_entrance_decomposition`
- Kind: proof-template
- Summary: Partition {X_n=y} by the first positive hitting time T_y=m, then restart from y by the strong Markov property to get p^n(x,y)=sum_m P_x(T_y=m)p^{n-m}(y,y).
- Use case: Exercise 5.2.4 and renewal decompositions for Markov chains.
- Tags: hitting-time, strong-markov, decomposition

###### Exit probabilities solve the Dirichlet problem

- ID: `exercise_ch5_exit_probability_dirichlet_problem`
- Kind: proof-template
- Summary: An exit probability h(x)=P_x(V_A<V_B) is harmonic off A union B with boundary values 1 and 0; optional stopping at the exit time proves uniqueness on finite domains.
- Use case: Exercises 5.2.7 and 5.2.8.
- Tags: dirichlet-problem, harmonic, optional-stopping

###### Expected hitting times solve a Poisson equation

- ID: `exercise_ch5_expected_hitting_time_poisson_equation`
- Kind: proof-template
- Summary: For g(x)=E_x V_A, first-step analysis gives g=1+Pg off A and g=0 on A; the process g(X_{n∧V_A})+n∧V_A is the uniqueness martingale.
- Use case: Exercises 5.2.11, 5.2.12, and 5.2.13.
- Tags: expected-hitting-time, poisson-equation, martingale

###### Absorption probability from martingale value

- ID: `exercise_ch5_absorption_probability_martingale`
- Kind: calculation-template
- Summary: If a bounded martingale is stopped on two absorbing boundary values, the starting value equals the boundary-weighted absorption probability.
- Use case: Exercises 5.2.8, 5.2.9, and 5.2.10.
- Tags: martingale, absorption, optional-stopping

###### Iid excursions between recurrent returns

- ID: `exercise_ch5_excursion_iid_cycles`
- Kind: regeneration-template
- Summary: At successive return times to a recurrent state, the strong Markov property makes the interarrival times and path excursions iid.
- Use case: Exercise 5.3.1 and regenerative proofs in Sections 5.5 and 5.6.
- Tags: excursions, regeneration, strong-markov

###### Birth-death recurrence by log product asymptotics

- ID: `exercise_ch5_birth_death_log_product_test`
- Kind: asymptotic-template
- Summary: Use log(q_j/p_j) expansions to decide divergence of the birth-death scale sum; for p_j=1/2+C/j the threshold is C=1/4.
- Use case: Exercise 5.3.4 and nearest-neighbor recurrence boundaries.
- Tags: birth-death, recurrence, asymptotics

###### Lyapunov function tending to zero proves transience

- ID: `exercise_ch5_lyapunov_to_zero_transience`
- Kind: criterion
- Summary: A positive superharmonic function outside a finite set that tends to zero at infinity contradicts recurrent return to that finite set, hence implies transience in irreducible chains.
- Use case: Exercise 5.3.5 and outward-drift birth-death chains.
- Tags: lyapunov, transience, supermartingale

###### Power Lyapunov functions for near-critical birth-death chains

- ID: `exercise_ch5_power_lyapunov_birth_death`
- Kind: calculation-template
- Summary: For p_j-1/2~C/j, Taylor expand E_j X_1^alpha-j^alpha; choosing alpha on the correct side of 1-4C gives recurrence or transience.
- Use case: Exercise 5.3.6.
- Tags: birth-death, lyapunov, taylor-expansion

###### Recurrent irreducible chains have only constant nonnegative superharmonic functions

- ID: `exercise_ch5_superharmonic_liouville_chain`
- Kind: liouville-template
- Summary: Stop a nonnegative supermartingale f(X_n) at the hitting time of another state; recurrence forces f(x)>=f(y) and symmetry gives equality.
- Use case: Exercise 5.3.7 and Liouville-type arguments.
- Tags: superharmonic, recurrence, liouville

###### Four alternatives for one-dimensional random walks

- ID: `exercise_ch5_one_dimensional_random_walk_alternatives`
- Kind: classification-template
- Summary: Tail zero-one laws and ladder behavior force a one-dimensional random walk to be identically zero, drift to +infinity, drift to -infinity, or oscillate unboundedly both ways.
- Use case: Exercise 5.4.1.
- Tags: random-walk, zero-one-law, classification

###### Ascending ladder epochs regenerate record highs

- ID: `exercise_ch5_ladder_epoch_geometric_regeneration`
- Kind: regeneration-template
- Summary: Successive strict ascending ladder epochs repeat the same trial by the strong Markov property; if the first ladder time is defective, only finitely many records occur, otherwise records go to infinity.
- Use case: Exercise 5.4.2.
- Tags: ladder-variables, records, random-walk

###### Recurrent random walk implies nonnegative superharmonic Liouville

- ID: `exercise_ch5_recurrent_walk_superharmonic_liouville`
- Kind: liouville-template
- Summary: For recurrent walks in dimensions one and two, f(S_n) is a nonnegative supermartingale and recurrent visits to neighborhoods force all superharmonic values to agree.
- Use case: Exercise 5.4.3.
- Tags: superharmonic, random-walk, liouville

###### Bounded harmonic functions via tail zero-one law

- ID: `exercise_ch5_bounded_harmonic_tail_zero_one`
- Kind: proof-template
- Summary: For a bounded harmonic h, h(S_n) is a bounded martingale; its limit is invariant under finite permutations of iid increments, so Hewitt-Savage forces constancy.
- Use case: Exercise 5.4.4.
- Tags: harmonic, hewitt-savage, martingale

###### Hypergeometric stationary law for Bernoulli-Laplace

- ID: `exercise_ch5_hypergeometric_detailed_balance`
- Kind: calculation-template
- Summary: The Bernoulli-Laplace diffusion has stationary distribution proportional to binomial choices of black and white balls in the left urn; adjacent detailed balance verifies it.
- Use case: Exercise 5.5.1.
- Tags: bernoulli-laplace, hypergeometric, detailed-balance

###### Cycle occupation measure as a hitting-probability ratio

- ID: `exercise_ch5_cycle_measure_hitting_ratio`
- Kind: formula
- Summary: For recurrent x and y in the same class, expected visits to y during one x-cycle equal P_x(T_y<T_x)/P_y(T_x<T_y).
- Use case: Exercise 5.5.2.
- Tags: cycle-trick, hitting-probability, stationary-measure

###### Use normalization to compare stationary measures

- ID: `exercise_ch5_stationary_measure_uniqueness_scaling`
- Kind: proof-template
- Summary: In an irreducible recurrent chain, all stationary measures are scalar multiples; evaluate at one state to determine the scalar.
- Use case: Exercises 5.5.3 and 5.5.5.
- Tags: stationary-measure, uniqueness, normalization

###### Poisson thinning gives M/M/infinity stationarity

- ID: `exercise_ch5_poisson_thinning_stationarity`
- Kind: calculation-template
- Summary: If X is Poisson(theta), Bernoulli thinning with survival p gives Poisson(p theta), and adding independent Poisson(lambda) arrivals gives Poisson(p theta+lambda).
- Use case: Exercise 5.5.8.
- Tags: poisson, thinning, queue

###### Idle fraction from reflected random-walk regulator

- ID: `exercise_ch5_reflected_walk_idle_fraction`
- Kind: queue-template
- Summary: For a stable reflected walk, the regulator increments exactly when the queue is empty and the raw increment is -1; dividing the reflection identity by n gives the long-run idle frequency.
- Use case: Exercise 5.5.7 and M/G/1 stationary mass at zero.
- Tags: reflected-random-walk, queue, stationarity

###### Two-state chain convergence via affine recursion

- ID: `exercise_ch5_two_state_affine_recursion`
- Kind: calculation-template
- Summary: Track one coordinate probability q_n; the recursion q_{n+1}=beta+(1-alpha-beta)q_n solves explicitly around its stationary fixed point.
- Use case: Exercise 5.6.1.
- Tags: two-state-chain, stationary-distribution, recursion

###### Finite irreducible aperiodic chains have a positive matrix power

- ID: `exercise_ch5_finite_aperiodic_uniform_power`
- Kind: proof-template
- Summary: Use a path from x to y plus sufficiently long return loops at y; finiteness lets one choose a common power m for all pairs.
- Use case: Exercise 5.6.2.
- Tags: finite-chain, aperiodic, positive-power

###### Uniform block coupling gives exponential convergence

- ID: `exercise_ch5_block_coupling_exponential_rate`
- Kind: coupling-template
- Summary: If an m-step transition has a uniformly positive chance to send all states to one common state, coupling attempts in independent blocks have geometric tails.
- Use case: Exercise 5.6.3 and finite-state mixing estimates.
- Tags: coupling, exponential-rate, finite-chain

###### Regenerative LLN for additive functionals

- ID: `exercise_ch5_regenerative_additive_functional_lln`
- Kind: limit-template
- Summary: Split the path into iid return cycles; reward sums divided by elapsed time converge to expected cycle reward divided by expected cycle length, which equals the stationary average.
- Use case: Exercise 5.6.5.
- Tags: regeneration, ergodic-theorem, lln

###### Regenerative CLT for additive functionals

- ID: `exercise_ch5_regenerative_additive_functional_clt`
- Kind: limit-template
- Summary: Apply the iid CLT to centered cycle rewards and random-index by the number of completed cycles; show incomplete-cycle rewards are negligible on sqrt(n) scale.
- Use case: Exercise 5.6.6.
- Tags: regeneration, clt, random-index

###### Ratio limits from recurrent cycles

- ID: `exercise_ch5_recurrent_ratio_limit_cycles`
- Kind: limit-template
- Summary: Count visits to z per completed y-cycle and divide by visits to y; the strong law gives the stationary-measure ratio m(z)/m(y).
- Use case: Exercises 5.6.7 and 5.6.8.
- Tags: ratio-limit, recurrent-chain, cycle-measure

###### Split-chain recurrence is return-sum divergence at the atom

- ID: `exercise_ch5_split_atom_return_sum`
- Kind: criterion
- Summary: For the artificial atom alpha, the countable-state return criterion applies: recurrence is equivalent to divergence of sum_n pbar^n(alpha,alpha).
- Use case: Exercise 5.8.1.
- Tags: harris-chain, split-chain, recurrence

###### Stationary distribution forces Harris recurrence

- ID: `exercise_ch5_harris_stationarity_implies_recurrence`
- Kind: proof-template
- Summary: Lift a stationary distribution to the split chain; positive stationary mass at alpha forces an infinite expected number of alpha visits, hence recurrence.
- Use case: Exercise 5.8.3.
- Tags: harris-chain, stationarity, recurrence

###### Harris recurrence does not depend on the small-set pair

- ID: `exercise_ch5_harris_small_set_choice_invariance`
- Kind: proof-template
- Summary: If another Harris set A' is reachable, it has positive lambda measure for the original split chain; Theorem 5.8.8 makes visits to A' occur infinitely often.
- Use case: Exercise 5.8.4.
- Tags: harris-chain, small-set, invariance

###### GI/G/1 drift classification

- ID: `exercise_ch5_gig1_drift_classification`
- Kind: queue-template
- Summary: Compare the reflected workload with the raw random walk until the first negative passage: positive drift gives transience, nonpositive drift gives recurrence, negative drift gives positive recurrence.
- Use case: Exercise 5.8.5.
- Tags: gig1, queue, drift

###### Reflected random walk equals reversed maximum in law

- ID: `exercise_ch5_reflection_maximum_representation`
- Kind: identity-template
- Summary: The reflected workload satisfies W_n=S_n-min_{j<=n}S_j, which by reversing increments has the same law as the maximum of a length-n random walk.
- Use case: Exercise 5.8.6.
- Tags: reflected-random-walk, path-reversal, maximum

###### Multiplicative variance O.U. becomes stable on log scale

- ID: `exercise_ch5_multiplicative_ou_log_recursion`
- Kind: classification-template
- Summary: For Y_{n+1}=beta sqrt(|Y_n|) Z_{n+1}, log|Y_n| follows an AR(1) recursion with coefficient 1/2, yielding a nonzero positive recurrent Harris class plus an absorbing zero.
- Use case: Exercise 5.8.7.
- Tags: ornstein-uhlenbeck, log-recursion, harris-chain

## Chapter 6

### Durrett Chapter 6 LLM Viki: Ergodic Theorems

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter6.pdf`.

This unified Chapter 6 knowledge base includes textbook knowledge pieces plus exercise-derived method patterns from the solved Chapter 6 exercises.

Exercise source: `Probability/Exercises/Chapter6/Chapter6Exercises.tex` and `Probability/Exercises/Chapter6/Chapter6Exercises.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

#### Section Guides

##### 6.1 Definitions and Examples

- Goal: Translate stationary sequences into measure-preserving dynamical systems and identify ergodic examples.

- Must master: stationarity, measure-preserving maps, invariant sigma-field, ergodicity, iid shifts, stationary Markov chains, irrational rotations

- Prelim angle: Most Chapter 6 problems start by checking whether the invariant sigma-field is trivial.

##### 6.2 Birkhoff's Ergodic Theorem

- Goal: Use Birkhoff's theorem to turn long-run averages into conditional expectations or constants.

- Must master: Birkhoff theorem, maximal ergodic lemma, SLLN as a special case, Markov chain averages, equidistribution

- Prelim angle: This is the high-yield theorem for time averages of dependent stationary data.

##### 6.3 Recurrence

- Goal: Apply ergodic averages to range growth, recurrence of stationary-increment walks, and return cycles.

- Must master: range theorem, zero conditional drift recurrence, Kac return-time theorem, cycle trick

- Prelim angle: Good recurrence problems often ask you to identify escape probability or mean return time from stationarity.

##### 6.4 A Subadditive Ergodic Theorem

- Goal: Recognize subadditive arrays and prove normalized optimal costs have limits.

- Must master: subadditive array hypotheses, Fekete expectation step, ergodic constant case, range and LCS examples

- Prelim angle: Use when the quantity is an optimal path length, cost, passage time, or negative of a superadditive reward.

##### 6.5 Applications

- Goal: See the subadditive theorem in random matrices, random permutations, first-passage percolation, and branching processes.

- Must master: random matrix products, Poissonization, FPP time constant, integrability checks, branching-process speed

- Prelim angle: Applications usually reduce to checking subadditivity plus stationarity and then interpreting the constant.

#### Knowledge Pieces

##### Stationary sequence

- ID: `durrett_ch6_stationary_sequence_definition`

- Section: 6.1 Definitions and Examples

- Kind: definition

- Summary: A sequence X_0, X_1, ... is stationary when each shifted finite block has the same law as the original block.

- Proof idea: Check equality of all finite-dimensional distributions after shifting by k.

- Exam use: Use as the entry point for ergodic averages, stationary Markov chains, rotations, and stationary increments.

- Pitfall: Stationarity is distributional, not pathwise equality; it does not imply independence.

- Tags: stationarity, finite-dimensional-laws, shift

##### Measure-preserving transformation model

- ID: `durrett_ch6_measure_preserving_shift_model`

- Section: 6.1 Definitions and Examples

- Kind: construction

- Summary: Every stationary sequence on a nice state space can be represented as X_n(omega)=X(phi^n omega) for a measure-preserving map phi.

- Proof idea: Put the stationary law on sequence space and let phi be the left shift; stationarity makes the shift preserve probability.

- Exam use: Lets all ergodic-theorem statements be proved for one abstract dynamical system.

- Pitfall: The representation changes the sample space; it preserves laws but not necessarily the user's original probability space.

- Tags: measure-preserving, shift-space, stationary-process

##### Invariant events and invariant sigma-field

- ID: `durrett_ch6_invariant_sigma_field`

- Section: 6.1 Definitions and Examples

- Kind: definition

- Summary: An event A is invariant if phi^{-1}A=A up to null sets; the invariant events form the sigma-field I.

- Proof idea: Closure under complements and countable unions follows from pulling sets back through phi^{-1}.

- Exam use: The limit in Birkhoff's theorem is the conditional expectation onto I.

- Pitfall: Invariant means unchanged under the transformation, not merely high probability overlap after one shift.

- Tags: invariant-events, sigma-field, conditional-expectation

##### Ergodicity

- ID: `durrett_ch6_ergodicity_definition`

- Section: 6.1 Definitions and Examples

- Kind: definition

- Summary: A measure-preserving transformation is ergodic when every invariant event has probability 0 or 1.

- Proof idea: Interpret nonergodicity as the ability to split the space into invariant pieces of positive probability.

- Exam use: Use ergodicity to turn Birkhoff limits E(X|I) into constants EX.

- Pitfall: Ergodic is stronger than stationary and different from independent; periodic examples can be stationary but not mixing.

- Tags: ergodicity, invariant-events, 0-1-law

##### IID shifts are ergodic

- ID: `durrett_ch6_iid_shift_ergodic`

- Section: 6.1 Definitions and Examples

- Kind: example-pattern

- Summary: For an iid sequence, invariant shift events lie in the tail sigma-field, so Kolmogorov's 0-1 law implies ergodicity.

- Proof idea: Iterate shift invariance to show A is measurable with respect to sigma(X_n, X_{n+1}, ...), then intersect over n.

- Exam use: Explains why Birkhoff's theorem recovers the strong law for iid sequences.

- Pitfall: The tail sigma-field argument uses iid independence; it is not automatic for every stationary sequence.

- Tags: iid, tail-sigma-field, ergodic

##### Stationary Markov chain ergodicity criterion

- ID: `durrett_ch6_stationary_markov_chain_ergodic`

- Section: 6.1 Definitions and Examples

- Kind: theorem

- Summary: A countable-state Markov chain started in a positive stationary distribution is ergodic exactly when the chain is irreducible.

- Proof idea: Closed irreducible classes give invariant events; conversely the Markov property and recurrence force invariant probabilities to be constant.

- Exam use: Use for time averages of irreducible positive recurrent chains.

- Pitfall: Irreducibility makes I trivial, but periodic chains may still have a nontrivial tail sigma-field.

- Tags: markov-chains, irreducibility, stationary-distribution

##### Circle rotation ergodicity

- ID: `durrett_ch6_circle_rotation_ergodicity`

- Section: 6.1 Definitions and Examples

- Kind: example-pattern

- Summary: Rotation x -> x+theta mod 1 is ergodic under Lebesgue measure when theta is irrational and not ergodic when theta is rational.

- Proof idea: For irrational theta, Fourier coefficients of an invariant L2 function satisfy c_k(e^{2 pi i k theta}-1)=0, forcing all nonconstant coefficients to vanish.

- Exam use: The canonical deterministic example where ergodic averages behave like probabilistic averages.

- Pitfall: Rational rotations have finite orbits and many invariant unions of orbit slices.

- Tags: circle-rotation, fourier-series, irrational

##### Functions of stationary processes

- ID: `durrett_ch6_functions_of_stationary_processes`

- Section: 6.1 Definitions and Examples

- Kind: fact

- Summary: Measurable functions of the future of a stationary process form another stationary process; ergodicity is inherited under such factors.

- Proof idea: Write Y_k=g(X_k,X_{k+1},...) and compare shifted finite-dimensional distributions.

- Exam use: Useful for creating stationary indicator, block, or return-time processes.

- Pitfall: The function must be applied in a shift-compatible way; arbitrary time-dependent functions can destroy stationarity.

- Tags: stationary-factors, measurable-functions, ergodicity

##### Birkhoff ergodic theorem

- ID: `durrett_ch6_birkhoff_ergodic_theorem`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: theorem

- Summary: For X in L1, the time averages n^{-1} sum_{m<n} X(phi^m omega) converge almost surely and in L1 to E(X|I).

- Proof idea: Subtract E(X|I), use the maximal ergodic lemma to rule out positive limsup and negative liminf, then truncate for L1 convergence.

- Exam use: Main tool for replacing long-run empirical averages by conditional or ordinary means.

- Pitfall: Without ergodicity the limit is random: it is E(X|I), not necessarily EX.

- Tags: birkhoff, ergodic-theorem, time-averages

##### Maximal ergodic lemma

- ID: `durrett_ch6_maximal_ergodic_lemma`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: lemma

- Summary: For partial sums S_k of X along a measure-preserving orbit and M_k=max(0,S_1,...,S_k), one has E(X; M_k>0) >= 0.

- Proof idea: Compare X(omega)+M_k(phi omega) with each S_j(omega), integrate, and use measure preservation.

- Exam use: The key technical inequality behind Birkhoff's pointwise convergence proof.

- Pitfall: It is an integration inequality, not a direct maximal probability bound; track the set {M_k>0}.

- Tags: maximal-ergodic-lemma, partial-sums, birkhoff-proof

##### Strong law as an ergodic theorem

- ID: `durrett_ch6_strong_law_from_birkhoff`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: example-pattern

- Summary: For iid X_m in L1, Birkhoff gives n^{-1} sum_{m<n} X_m -> E X_0 almost surely and in L1.

- Proof idea: The iid shift is ergodic, so E(X_0|I)=E X_0.

- Exam use: Use as a conceptual shortcut from Chapter 2 LLNs to general stationary sequences.

- Pitfall: The theorem needs integrability; for nonintegrable iid variables this conclusion can fail.

- Tags: strong-law, iid, birkhoff

##### Stationary Markov chain time averages

- ID: `durrett_ch6_markov_chain_time_average`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: corollary

- Summary: For an irreducible countable-state Markov chain started from its stationary distribution pi, n^{-1} sum_{m<n} f(X_m) -> sum_x f(x) pi(x) for pi-integrable f.

- Proof idea: Apply Birkhoff to f(X_0) and use the irreducible stationary chain's ergodicity.

- Exam use: Recovers the long-run frequency and reward law for positive recurrent Markov chains.

- Pitfall: The statement is under stationarity; nonstationary initial laws need an additional argument.

- Tags: markov-chains, time-averages, stationary-distribution

##### Weyl equidistribution from irrational rotation

- ID: `durrett_ch6_weyl_equidistribution`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: theorem

- Summary: For irrational theta, the orbit x+n theta mod 1 visits every interval [a,b) with limiting frequency b-a for every starting x.

- Proof idea: Apply Birkhoff to interval indicators, then remove the exceptional set by approximating intervals from inside and using density.

- Exam use: Use for deterministic averaging and number-theoretic distribution mod 1.

- Pitfall: Birkhoff first gives almost-every starting point; the interval theorem needs extra work for every x.

- Tags: equidistribution, irrational-rotation, intervals

##### Benford law for powers

- ID: `durrett_ch6_benford_law_powers`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: example-pattern

- Summary: If log_10 2 is irrational, the first digit of 2^m has limiting frequency log_10((k+1)/k) for digit k.

- Proof idea: First digits correspond to fractional parts of m log_10 2 lying in [log_10 k, log_10(k+1)).

- Exam use: A memorable application of equidistribution to leading-digit asymptotics.

- Pitfall: Benford frequencies describe a limiting distribution, not exact finite-sample frequencies.

- Tags: benford-law, equidistribution, first-digits

##### Lp convergence upgrade

- ID: `durrett_ch6_lp_upgrade_birkhoff`

- Section: 6.2 Birkhoff's Ergodic Theorem

- Kind: exercise-pattern

- Summary: If X is in Lp for p>1, the Birkhoff averages converge in Lp as well as almost surely.

- Proof idea: Use maximal or domination arguments for the averages and uniform integrability of powers.

- Exam use: Useful when a problem asks for convergence in norm rather than only almost surely.

- Pitfall: Do not infer Lp convergence from L1 convergence without an Lp bound or uniform integrability.

- Tags: lp-convergence, uniform-integrability, birkhoff

##### Range growth for stationary increments

- ID: `durrett_ch6_range_growth_stationary_increments`

- Section: 6.3 Recurrence

- Kind: theorem

- Summary: For a stationary-increment walk S_n, the range R_n=|{S_1,...,S_n}| satisfies R_n/n -> E(1_A|I), where A is the event of never returning to 0 after time 0.

- Proof idea: Bound R_n below by future-noncollision indicators and above by finite-window noncollision indicators, then apply Birkhoff and monotone convergence.

- Exam use: Connects recurrence questions to an ergodic average of escape events.

- Pitfall: The limit is conditional on I; only in ergodic cases does it reduce to P(A).

- Tags: range, stationary-increments, recurrence

##### Zero conditional drift implies recurrence on Z

- ID: `durrett_ch6_zero_drift_integer_recurrence`

- Section: 6.3 Recurrence

- Kind: theorem

- Summary: For stationary integer-valued increments with E|X_1|<infinity and E(X_1|I)=0, the walk returns to 0 infinitely often almost surely.

- Proof idea: Birkhoff gives S_n/n -> 0, so the range is sublinear; the range theorem forces escape probability zero, and stationarity then gives infinitely many returns.

- Exam use: Generalizes the Chung-Fuchs recurrence intuition beyond iid increments.

- Pitfall: The condition is E(X_1|I)=0, not merely EX_1=0; mixtures of positive and negative drifts are counterexamples.

- Tags: recurrence, zero-drift, stationary-increments

##### Kac return-time theorem

- ID: `durrett_ch6_stationary_return_times_kac`

- Section: 6.3 Recurrence

- Kind: theorem

- Summary: For a stationary process that hits A almost surely, the successive return gaps to A are stationary under P(.|X_0 in A), and E(T_1|X_0 in A)=1/P(X_0 in A).

- Proof idea: Embed the process two-sided, decompose by the last visit before time 0, and sum tail probabilities of the first return.

- Exam use: Turns visits to a set into regenerative cycles and recovers mean return time 1/pi(x) for Markov chains.

- Pitfall: Conditioning on X_0 in A is essential; the first waiting time from an arbitrary stationary time has a length-biased flavor.

- Tags: kac, return-times, stationary-processes

##### Cycle trick for stationary measures

- ID: `durrett_ch6_cycle_trick_stationary_measure`

- Section: 6.3 Recurrence

- Kind: exercise-pattern

- Summary: Expected occupation of B during a return cycle to A equals P(X_0 in B)/P(X_0 in A) when A and B are disjoint and A is recurrent.

- Proof idea: Sum indicators over the cycle and use stationarity to convert cycle occupation counts into one-time probabilities.

- Exam use: Useful for constructing stationary measures of Markov chains from excursions.

- Pitfall: The denominator is the stationary mass of A; the formula is not a conditional probability of hitting B before returning.

- Tags: cycle-trick, occupation-times, stationary-measure

##### Stationary renewal waiting-time bias

- ID: `durrett_ch6_stationary_renewal_waiting_time`

- Section: 6.3 Recurrence

- Kind: exercise-pattern

- Summary: For a stationary {0,1} process conditioned on X_0=1, the first return law satisfies Pbar(T_1=n)=Pbar(T_1>=n)/Ebar T_1 in the iid-gap renewal case.

- Proof idea: Count which positions inside a renewal interval can serve as the stationary origin.

- Exam use: Explains inspection-paradox corrections in stationary renewal processes.

- Pitfall: The distribution seen from a stationary time differs from the raw interarrival distribution.

- Tags: renewal, return-time, inspection-paradox

##### Subadditive ergodic theorem

- ID: `durrett_ch6_subadditive_ergodic_theorem`

- Section: 6.4 A Subadditive Ergodic Theorem

- Kind: theorem

- Summary: For a stationary subadditive array X_{m,n} with integrability and a linear lower expectation bound, X_{0,n}/n converges almost surely and in L1 to a limit with mean inf_m E X_{0,m}/m.

- Proof idea: Use Fekete's lemma for expectations, Birkhoff on block increments for the limsup, then a covering argument for the liminf.

- Exam use: The main tool for limits of optimal costs, passage times, longest subsequences, and products.

- Pitfall: Check the exact stationarity assumptions; Liggett's version is weaker than Kingman's original in useful applications.

- Tags: subadditive-ergodic-theorem, kingman, liggett

##### Fekete step for expected subadditive arrays

- ID: `durrett_ch6_fekete_expectation_step`

- Section: 6.4 A Subadditive Ergodic Theorem

- Kind: proof-template

- Summary: If a_n=E X_{0,n} and a_m+a_{n-m}>=a_n, then a_n/n converges to inf_m a_m/m.

- Proof idea: Write n=km+r, iterate subadditivity, divide by n, and let n grow with fixed m.

- Exam use: Use whenever the deterministic expectation part of a subadditive theorem appears.

- Pitfall: The inequality direction is easy to mix up because the array convention is X_{0,m}+X_{m,n}>=X_{0,n}.

- Tags: fekete, expectations, subadditivity

##### Birkhoff as the additive special case

- ID: `durrett_ch6_birkhoff_as_additive_case`

- Section: 6.4 A Subadditive Ergodic Theorem

- Kind: example-pattern

- Summary: If X_{m,n}=xi_{m+1}+...+xi_n for a stationary integrable sequence, then the subadditive theorem reduces to Birkhoff.

- Proof idea: The subadditive inequality becomes equality, and block stationarity is inherited from the xi sequence.

- Exam use: A quick consistency check for the hypotheses of the subadditive theorem.

- Pitfall: Do not lose the indexing: X_{m,n} covers increments after m through n.

- Tags: additive-case, stationary-sequence, birkhoff

##### Range as a subadditive example

- ID: `durrett_ch6_range_subadditive_example`

- Section: 6.4 A Subadditive Ergodic Theorem

- Kind: example-pattern

- Summary: The number of distinct sites visited between times m+1 and n is subadditive, so the normalized range has an almost sure and L1 limit.

- Proof idea: The union of sites in two adjacent time intervals covers the sites in the whole interval, giving X_{0,m}+X_{m,n}>=X_{0,n}.

- Exam use: Provides a second route to existence of range-growth rates even when the rate is not identified.

- Pitfall: The theorem gives existence of the limit, not the recurrence classification by itself.

- Tags: range, random-walk, subadditivity

##### Longest common subsequence limit

- ID: `durrett_ch6_longest_common_subsequence_limit`

- Section: 6.4 A Subadditive Ergodic Theorem

- Kind: example-pattern

- Summary: For two ergodic stationary sequences, the longest common subsequence length L_{0,n} satisfies L_{0,n}/n -> gamma, where gamma=sup_m E L_{0,m}/m.

- Proof idea: Use superadditivity of L over adjacent blocks, or subadditivity of -L, and apply the subadditive ergodic theorem.

- Exam use: Recognize optimization lengths as candidates for subadditive limits.

- Pitfall: The theorem proves existence of gamma but usually not its numerical value.

- Tags: longest-common-subsequence, superadditivity, ergodic-limit

##### Products of positive random matrices

- ID: `durrett_ch6_random_matrix_products`

- Section: 6.5 Applications

- Kind: application

- Summary: For stationary positive matrices with integrable log entries, n^{-1} log of product entries converges almost surely to a common growth rate.

- Proof idea: Take minus logs of positive product entries to create a subadditive array; compare entries and norms to transfer the limit.

- Exam use: A probability route to Lyapunov-exponent-type limits.

- Pitfall: Strict positivity and log-integrability matter; zeros or heavy tails can break the logarithmic comparison.

- Tags: random-matrices, lyapunov-exponent, subadditivity

##### Increasing subsequences in random permutations

- ID: `durrett_ch6_increasing_subsequence_permutation`

- Section: 6.5 Applications

- Kind: application

- Summary: Poissonizing random permutations and applying subadditivity shows the longest increasing subsequence has an n^{1/2} order limit constant.

- Proof idea: Represent permutations by Poisson points in squares, use superadditivity of increasing paths, then de-Poissonize with the Poisson count law.

- Exam use: A classic example of turning a combinatorial optimization problem into an ergodic limit.

- Pitfall: The subadditive argument gives the existence of the constant; identifying it as 2 requires deeper work.

- Tags: random-permutations, longest-increasing-subsequence, poissonization

##### Poisson square time change

- ID: `durrett_ch6_poisson_square_time_change`

- Section: 6.5 Applications

- Kind: lemma

- Summary: If tau(n) is the side length of the square containing the first n points of a rate-one planar Poisson process, then tau(n)/sqrt(n) -> 1 almost surely.

- Proof idea: The number of points in the square of side sqrt(n) is a sum of independent mean-one Poisson increments, so the strong law controls the inverse time.

- Exam use: Used to pass from Poissonized increasing paths back to fixed-size random permutations.

- Pitfall: The scale is sqrt(n) because the square area is t^2.

- Tags: poisson-process, time-change, permutation

##### First-passage percolation time constant

- ID: `durrett_ch6_first_passage_percolation_time_constant`

- Section: 6.5 Applications

- Kind: application

- Summary: For iid nonnegative edge passage times on Z^d with suitable integrability, t(0,nu)/n converges almost surely to a deterministic time constant.

- Proof idea: Passage times satisfy t(0,nu)<=t(0,mu)+t(mu,nu), so X_{m,n}=t(mu,nu) is subadditive; tail triviality makes the limit constant.

- Exam use: Core template for metric growth models and random media.

- Pitfall: Finite mean of one edge is sufficient in the simple statement but can be weakened; without integrability the limit may be infinite.

- Tags: first-passage-percolation, time-constant, random-media

##### First-passage percolation integrability condition

- ID: `durrett_ch6_fpp_integrability_min_condition`

- Section: 6.5 Applications

- Kind: criterion

- Summary: A weaker useful condition is that the minimum of 2d independent edge times has finite mean, equivalently integral_0^infty (1-F(x))^{2d} dx < infinity.

- Proof idea: Use disjoint neighboring paths to dominate one-step passage times by minima of several edge variables.

- Exam use: Helps check when a finite time constant exists for heavy-tailed edge weights.

- Pitfall: This condition concerns the minimum of several edges, not the edge variable itself.

- Tags: first-passage-percolation, integrability, heavy-tails

##### Age-dependent branching process speed

- ID: `durrett_ch6_age_dependent_branching_speed`

- Section: 6.5 Applications

- Kind: application

- Summary: In an age-dependent branching process with no extinction at birth and finite lifetimes, the first birth time in generation n divided by n converges almost surely.

- Proof idea: Define X_{m,n} as the additional time from the first generation-m individual to a generation-n descendant and apply Liggett's subadditive theorem.

- Exam use: Shows why the weaker Liggett hypotheses are useful beyond Kingman's original stationary-array assumptions.

- Pitfall: The stronger all-triples subadditivity can fail because the fastest later descendant need not descend from the fastest earlier individual.

- Tags: branching-process, subadditivity, growth-speed

##### Branching speed via lifetime large deviations

- ID: `durrett_ch6_branching_speed_large_deviation_formula`

- Section: 6.5 Applications

- Kind: formula

- Summary: For mean offspring mu and lifetime sums with rate c(a), the asymptotic earliest-generation speed is gamma=inf{a: log mu - c(a)>0}.

- Proof idea: Compare expected counts of generation-n individuals born by time an with branching-process survival when the count grows supercritically.

- Exam use: Connects subadditive limits with large-deviation rate functions.

- Pitfall: The subadditive theorem gives existence; this formula requires additional branching and large-deviation analysis.

- Tags: branching-process, large-deviations, speed

##### Invariant sigma-field and invariant random variables

- ID: `ch6_exercise_method_invariant_sigma_field_measurable_functions`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: exercise-pattern

- Summary: Show invariant events form a sigma-field by pullback closure; prove an I-measurable random variable is invariant by checking rational cuts, and conversely use invariant inverse images.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.1; identifying E(X|I) and invariant limits.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: invariant-sigma-field, measurability, rational-cuts

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

##### Strict representative for almost invariant sets

- ID: `ch6_exercise_method_almost_invariant_strictification`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: proof-template

- Summary: From an almost invariant set, form a forward pullback union B and then C=intersection phi^{-n}B; C is strictly invariant and differs only by a null set.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.2; replacing mod-null invariance by exact invariance.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: almost-invariant, strict-invariance, null-sets

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

##### Direct density proof of irrational rotation ergodicity

- ID: `ch6_exercise_method_direct_irrational_rotation_ergodicity`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: proof-template

- Summary: Use pigeonhole gaps to prove the irrational orbit is dense, approximate positive-measure sets by high-density intervals, and contradict coexistence of invariant A and A^c with positive measure.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.3; proving ergodicity without Fourier series.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: irrational-rotation, density-points, ergodicity

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

##### Two-sided extension of a stationary sequence

- ID: `ch6_exercise_method_two_sided_stationary_extension`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: construction

- Summary: Define finite-dimensional laws on integer-indexed coordinates by shifting all indices into the nonnegative side, then use stationarity for consistency and Kolmogorov extension.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.4; return-time and cycle arguments needing negative times.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: stationary-process, two-sided, kolmogorov-extension

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

##### Stationarity and ergodicity pass to factors

- ID: `ch6_exercise_method_factor_stationarity_ergodicity`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: proof-template

- Summary: For Y_k=g(X_k,X_{k+1},...), stationarity follows from shifted future laws; invariant events for Y pull back to invariant events for X, so ergodicity passes to Y.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.5; creating stationary derived processes.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: factor-map, stationarity, ergodicity

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

##### Random phase makes iid blocks stationary and ergodic

- ID: `ch6_exercise_method_random_phase_iid_blocks`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: construction

- Summary: Concatenate iid blocks and start at an independent uniform phase; one-step shifts rotate the phase and occasionally shift the iid block sequence, giving stationarity and ergodicity.

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.6; block constructions with stationary output.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: iid-blocks, random-phase, ergodicity

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

##### Gauss map invariant density by branch telescoping

- ID: `ch6_exercise_method_gauss_map_invariant_density`

- Section: 6.1 Exercises: Stationarity, invariant events, ergodicity, and measure-preserving examples

- Kind: calculation-template

- Summary: For phi(x)=1/x-floor(1/x), split into branches x=1/(k+y); the transformed density sum telescopes to 1/(1+y).

- Proof idea: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Exam use: Exercise 6.1.7; verifying the continued-fraction invariant measure.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: continued-fractions, gauss-map, invariant-density

- Source exercises: 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.1.7

##### Lp upgrade of Birkhoff by truncation

- ID: `ch6_exercise_method_lp_upgrade_by_truncation`

- Section: 6.2 Exercises: Birkhoff upgrades, moving observables, and maximal inequalities

- Kind: proof-template

- Summary: Prove Lp convergence for bounded observables by bounded convergence, then truncate X and control the tail using Jensen plus Lp contraction of conditional expectation.

- Proof idea: Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.

- Exam use: Exercise 6.2.1; upgrading ergodic averages from L1 to Lp.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: birkhoff, lp, truncation, jensen

- Source exercises: 6.2.1, 6.2.2, 6.2.3

##### Moving observable ergodic average

- ID: `ch6_exercise_method_moving_observable_ergodic_average`

- Section: 6.2 Exercises: Birkhoff upgrades, moving observables, and maximal inequalities

- Kind: proof-template

- Summary: Decompose averages of g_m(phi^m) into the fixed g average plus errors; control a.s. errors by tail suprema and L1 errors by Cesaro means.

- Proof idea: Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.

- Exam use: Exercise 6.2.2; triangular or time-varying observables in ergodic averages.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: moving-observable, tail-supremum, cesaro, birkhoff

- Source exercises: 6.2.1, 6.2.2, 6.2.3

##### Wiener maximal inequality from maximal ergodic lemma

- ID: `ch6_exercise_method_wiener_maximal_from_maximal_ergodic`

- Section: 6.2 Exercises: Birkhoff upgrades, moving observables, and maximal inequalities

- Kind: proof-template

- Summary: Apply the maximal ergodic lemma to Y=X-alpha so the positivity event of the shifted partial sums is exactly {max S_j/j > alpha}.

- Proof idea: Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.

- Exam use: Exercise 6.2.3; deriving maximal probability bounds for ergodic averages.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: maximal-ergodic-lemma, wiener-inequality, threshold-shift

- Source exercises: 6.2.1, 6.2.2, 6.2.3

##### Range expectation by last-visit decomposition

- ID: `ch6_exercise_method_range_last_visit_counting`

- Section: 6.3 Exercises: Range growth, recurrence, cycle tricks, and stationary renewal bias

- Kind: calculation-template

- Summary: Count each visited site by its last visit time; stationarity makes the probability of no future revisit over n-m steps equal to g_{n-m}.

- Proof idea: Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

- Exam use: Exercise 6.3.1; expected range identities for stationary-increment walks.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: range, last-visit, stationary-increments

- Source exercises: 6.3.1, 6.3.2, 6.3.3, 6.3.4

##### Positive drift escape probability from range growth

- ID: `ch6_exercise_method_positive_drift_escape_probability`

- Section: 6.3 Exercises: Range growth, recurrence, cycle tricks, and stationary renewal bias

- Kind: proof-template

- Summary: With ergodic integer increments bounded above by one and positive mean, the range grows at the same rate as the running maximum; Theorem 6.3.1 identifies the rate with P(escape).

- Proof idea: Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

- Exam use: Exercise 6.3.2; recurrence/escape probabilities under stationary increments.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: positive-drift, escape-probability, range-growth

- Source exercises: 6.3.1, 6.3.2, 6.3.3, 6.3.4

##### Cycle trick occupation ratio

- ID: `ch6_exercise_method_cycle_trick_occupation_ratio`

- Section: 6.3 Exercises: Range growth, recurrence, cycle tricks, and stationary renewal bias

- Kind: proof-template

- Summary: Use a two-sided stationary version and partition by the last visit to A before time 0; expected B-occupation in an A-cycle equals P(X0 in B)/P(X0 in A).

- Proof idea: Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

- Exam use: Exercise 6.3.3; constructing stationary measures from excursions.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: cycle-trick, occupation-time, two-sided-stationarity

- Source exercises: 6.3.1, 6.3.2, 6.3.3, 6.3.4

##### Stationary renewal first-waiting bias

- ID: `ch6_exercise_method_stationary_renewal_waiting_bias`

- Section: 6.3 Exercises: Range growth, recurrence, cycle tricks, and stationary renewal bias

- Kind: calculation-template

- Summary: Under conditioning on a renewal at time 0, stationarity of return gaps gives P(T=n)=Pbar(T>=n)/Ebar T for the waiting time seen from a stationary time.

- Proof idea: Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

- Exam use: Exercise 6.3.4; inspection-paradox and stationary renewal calculations.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: renewal, waiting-time, kac, stationary-bias

- Source exercises: 6.3.1, 6.3.2, 6.3.3, 6.3.4

##### Arbitrarily slow deterministic subadditive convergence

- ID: `ch6_exercise_method_arbitrarily_slow_subadditive_convergence`

- Section: 6.5 Exercises: Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Kind: counterexample-template

- Summary: Set X_{m,m+k}=f(k) with f(k)/k decreasing; subadditivity follows by comparing both pieces to f(n)/n, so the expectation convergence can be as slow as f(n)/n.

- Proof idea: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Exam use: Exercise 6.5.1; understanding limits of Fekete-type convergence rates.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: subadditivity, slow-convergence, fekete

- Source exercises: 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5

##### Longest common subsequence first-moment bounds

- ID: `ch6_exercise_method_lcs_first_moment_bounds`

- Section: 6.5 Exercises: Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Kind: calculation-template

- Summary: Compute small-n expectations for lower bounds and bound P(L_n >= K) by the expected number of matching index-pair subsequences, binom(n,K)^2 2^{-K}.

- Proof idea: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Exam use: Exercise 6.5.2; bounding LCS constants.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: longest-common-subsequence, first-moment, entropy-bound

- Source exercises: 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5

##### Poisson greedy path lower bound

- ID: `ch6_exercise_method_poisson_greedy_increasing_path_lower_bound`

- Section: 6.5 Exercises: Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Kind: calculation-template

- Summary: Choose successive Poisson points minimizing x+y in the northeast quadrant; the increment sum has tail exp(-t^2/2), giving mean coordinate step sqrt(pi/8) and gamma >= sqrt(8/pi).

- Proof idea: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Exam use: Exercise 6.5.3; lower bounds for Hammersley's increasing path constant.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: poisson-process, greedy-path, lis-lower-bound

- Source exercises: 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5

##### Permutation LIS upper bound by first moment

- ID: `ch6_exercise_method_permutation_lis_first_moment_upper_bound`

- Section: 6.5 Exercises: Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Kind: calculation-template

- Summary: For a fixed k-subset of indices, the values are increasing with probability 1/k!, so E J_k^n=binom(n,k)/k!; Stirling with k~alpha sqrt(n) gives gamma <= e.

- Proof idea: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Exam use: Exercise 6.5.4; upper bounds for longest increasing subsequences.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: random-permutation, lis, first-moment, stirling

- Source exercises: 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5

##### Branching Laplace martingale speed bound

- ID: `ch6_exercise_method_branching_laplace_martingale_bound`

- Section: 6.5 Exercises: Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Kind: proof-template

- Summary: Normalize the generation-n Laplace sum by (mu phi(theta))^n to get a nonnegative martingale; Markov's inequality bounds early birth events when exp(-theta a)/(mu phi(theta))>1.

- Proof idea: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Exam use: Exercise 6.5.5; age-dependent branching speed upper-tail bounds.

- Pitfall: Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.

- Tags: branching-process, laplace-transform, martingale, large-deviations

- Source exercises: 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5

#### Exercise Method Cards

##### 6.1 Stationarity, invariant events, ergodicity, and measure-preserving examples

- ID: `durrett_ch6_section_6_1_method_card`

- Method: Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

- Tags: stationarity, invariant-events, ergodicity, shift-model, measure-preserving

- New knowledge IDs: ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density

##### 6.2 Birkhoff upgrades, moving observables, and maximal inequalities

- ID: `durrett_ch6_section_6_2_method_card`

- Method: Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.

- Tags: birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality

- New knowledge IDs: ch6_exercise_method_lp_upgrade_by_truncation, ch6_exercise_method_moving_observable_ergodic_average, ch6_exercise_method_wiener_maximal_from_maximal_ergodic

##### 6.3 Range growth, recurrence, cycle tricks, and stationary renewal bias

- ID: `durrett_ch6_section_6_3_method_card`

- Method: Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

- Tags: recurrence, range, last-visit, cycle-trick, stationary-renewal

- New knowledge IDs: ch6_exercise_method_range_last_visit_counting, ch6_exercise_method_positive_drift_escape_probability, ch6_exercise_method_cycle_trick_occupation_ratio, ch6_exercise_method_stationary_renewal_waiting_bias

##### 6.5 Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- ID: `durrett_ch6_section_6_5_method_card`

- Method: Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

- Tags: subadditivity, first-moment, poissonization, branching-martingale, large-deviations

- New knowledge IDs: ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound

#### Exercise Record Index

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

### Chapter 6 Exercise Viki

#### Chapter 6 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter6/Chapter6Exercises.tex`
Source PDF: `Probability/Exercises/Chapter6/Chapter6Exercises.pdf`

This dataset turns the solved Chapter 6 exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.

##### Files

- `chapter6_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.
- `chapter6_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter6_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter6_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.
- `chapter6_exercise_viki.md`: human-readable overview.
- `manifest.json`: dataset metadata.

##### Section Method Cards

###### 6.1 - Stationarity, invariant events, ergodicity, and measure-preserving examples

Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.

Tags: stationarity, invariant-events, ergodicity, shift-model, measure-preserving

###### 6.2 - Birkhoff upgrades, moving observables, and maximal inequalities

Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.

Tags: birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality

###### 6.3 - Range growth, recurrence, cycle tricks, and stationary renewal bias

Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.

Tags: recurrence, range, last-visit, cycle-trick, stationary-renewal

###### 6.5 - Applications of subadditivity to LCS, LIS, Poisson paths, and branching

Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.

Tags: subadditivity, first-moment, poissonization, branching-martingale, large-deviations

##### New Knowledge Pieces

###### Invariant sigma-field and invariant random variables

- ID: `ch6_exercise_method_invariant_sigma_field_measurable_functions`
- Kind: exercise-derived-method
- Summary: Show invariant events form a sigma-field by pullback closure; prove an I-measurable random variable is invariant by checking rational cuts, and conversely use invariant inverse images.
- Use case: Exercise 6.1.1; identifying E(X|I) and invariant limits.
- Tags: invariant-sigma-field, measurability, rational-cuts

###### Strict representative for almost invariant sets

- ID: `ch6_exercise_method_almost_invariant_strictification`
- Kind: proof-template
- Summary: From an almost invariant set, form a forward pullback union B and then C=intersection phi^{-n}B; C is strictly invariant and differs only by a null set.
- Use case: Exercise 6.1.2; replacing mod-null invariance by exact invariance.
- Tags: almost-invariant, strict-invariance, null-sets

###### Direct density proof of irrational rotation ergodicity

- ID: `ch6_exercise_method_direct_irrational_rotation_ergodicity`
- Kind: proof-template
- Summary: Use pigeonhole gaps to prove the irrational orbit is dense, approximate positive-measure sets by high-density intervals, and contradict coexistence of invariant A and A^c with positive measure.
- Use case: Exercise 6.1.3; proving ergodicity without Fourier series.
- Tags: irrational-rotation, density-points, ergodicity

###### Two-sided extension of a stationary sequence

- ID: `ch6_exercise_method_two_sided_stationary_extension`
- Kind: construction
- Summary: Define finite-dimensional laws on integer-indexed coordinates by shifting all indices into the nonnegative side, then use stationarity for consistency and Kolmogorov extension.
- Use case: Exercise 6.1.4; return-time and cycle arguments needing negative times.
- Tags: stationary-process, two-sided, kolmogorov-extension

###### Stationarity and ergodicity pass to factors

- ID: `ch6_exercise_method_factor_stationarity_ergodicity`
- Kind: proof-template
- Summary: For Y_k=g(X_k,X_{k+1},...), stationarity follows from shifted future laws; invariant events for Y pull back to invariant events for X, so ergodicity passes to Y.
- Use case: Exercise 6.1.5; creating stationary derived processes.
- Tags: factor-map, stationarity, ergodicity

###### Random phase makes iid blocks stationary and ergodic

- ID: `ch6_exercise_method_random_phase_iid_blocks`
- Kind: construction
- Summary: Concatenate iid blocks and start at an independent uniform phase; one-step shifts rotate the phase and occasionally shift the iid block sequence, giving stationarity and ergodicity.
- Use case: Exercise 6.1.6; block constructions with stationary output.
- Tags: iid-blocks, random-phase, ergodicity

###### Gauss map invariant density by branch telescoping

- ID: `ch6_exercise_method_gauss_map_invariant_density`
- Kind: calculation-template
- Summary: For phi(x)=1/x-floor(1/x), split into branches x=1/(k+y); the transformed density sum telescopes to 1/(1+y).
- Use case: Exercise 6.1.7; verifying the continued-fraction invariant measure.
- Tags: continued-fractions, gauss-map, invariant-density

###### Lp upgrade of Birkhoff by truncation

- ID: `ch6_exercise_method_lp_upgrade_by_truncation`
- Kind: proof-template
- Summary: Prove Lp convergence for bounded observables by bounded convergence, then truncate X and control the tail using Jensen plus Lp contraction of conditional expectation.
- Use case: Exercise 6.2.1; upgrading ergodic averages from L1 to Lp.
- Tags: birkhoff, lp, truncation, jensen

###### Moving observable ergodic average

- ID: `ch6_exercise_method_moving_observable_ergodic_average`
- Kind: proof-template
- Summary: Decompose averages of g_m(phi^m) into the fixed g average plus errors; control a.s. errors by tail suprema and L1 errors by Cesaro means.
- Use case: Exercise 6.2.2; triangular or time-varying observables in ergodic averages.
- Tags: moving-observable, tail-supremum, cesaro, birkhoff

###### Wiener maximal inequality from maximal ergodic lemma

- ID: `ch6_exercise_method_wiener_maximal_from_maximal_ergodic`
- Kind: proof-template
- Summary: Apply the maximal ergodic lemma to Y=X-alpha so the positivity event of the shifted partial sums is exactly {max S_j/j > alpha}.
- Use case: Exercise 6.2.3; deriving maximal probability bounds for ergodic averages.
- Tags: maximal-ergodic-lemma, wiener-inequality, threshold-shift

###### Range expectation by last-visit decomposition

- ID: `ch6_exercise_method_range_last_visit_counting`
- Kind: calculation-template
- Summary: Count each visited site by its last visit time; stationarity makes the probability of no future revisit over n-m steps equal to g_{n-m}.
- Use case: Exercise 6.3.1; expected range identities for stationary-increment walks.
- Tags: range, last-visit, stationary-increments

###### Positive drift escape probability from range growth

- ID: `ch6_exercise_method_positive_drift_escape_probability`
- Kind: proof-template
- Summary: With ergodic integer increments bounded above by one and positive mean, the range grows at the same rate as the running maximum; Theorem 6.3.1 identifies the rate with P(escape).
- Use case: Exercise 6.3.2; recurrence/escape probabilities under stationary increments.
- Tags: positive-drift, escape-probability, range-growth

###### Cycle trick occupation ratio

- ID: `ch6_exercise_method_cycle_trick_occupation_ratio`
- Kind: proof-template
- Summary: Use a two-sided stationary version and partition by the last visit to A before time 0; expected B-occupation in an A-cycle equals P(X0 in B)/P(X0 in A).
- Use case: Exercise 6.3.3; constructing stationary measures from excursions.
- Tags: cycle-trick, occupation-time, two-sided-stationarity

###### Stationary renewal first-waiting bias

- ID: `ch6_exercise_method_stationary_renewal_waiting_bias`
- Kind: calculation-template
- Summary: Under conditioning on a renewal at time 0, stationarity of return gaps gives P(T=n)=Pbar(T>=n)/Ebar T for the waiting time seen from a stationary time.
- Use case: Exercise 6.3.4; inspection-paradox and stationary renewal calculations.
- Tags: renewal, waiting-time, kac, stationary-bias

###### Arbitrarily slow deterministic subadditive convergence

- ID: `ch6_exercise_method_arbitrarily_slow_subadditive_convergence`
- Kind: counterexample-template
- Summary: Set X_{m,m+k}=f(k) with f(k)/k decreasing; subadditivity follows by comparing both pieces to f(n)/n, so the expectation convergence can be as slow as f(n)/n.
- Use case: Exercise 6.5.1; understanding limits of Fekete-type convergence rates.
- Tags: subadditivity, slow-convergence, fekete

###### Longest common subsequence first-moment bounds

- ID: `ch6_exercise_method_lcs_first_moment_bounds`
- Kind: calculation-template
- Summary: Compute small-n expectations for lower bounds and bound P(L_n >= K) by the expected number of matching index-pair subsequences, binom(n,K)^2 2^{-K}.
- Use case: Exercise 6.5.2; bounding LCS constants.
- Tags: longest-common-subsequence, first-moment, entropy-bound

###### Poisson greedy path lower bound

- ID: `ch6_exercise_method_poisson_greedy_increasing_path_lower_bound`
- Kind: calculation-template
- Summary: Choose successive Poisson points minimizing x+y in the northeast quadrant; the increment sum has tail exp(-t^2/2), giving mean coordinate step sqrt(pi/8) and gamma >= sqrt(8/pi).
- Use case: Exercise 6.5.3; lower bounds for Hammersley's increasing path constant.
- Tags: poisson-process, greedy-path, lis-lower-bound

###### Permutation LIS upper bound by first moment

- ID: `ch6_exercise_method_permutation_lis_first_moment_upper_bound`
- Kind: calculation-template
- Summary: For a fixed k-subset of indices, the values are increasing with probability 1/k!, so E J_k^n=binom(n,k)/k!; Stirling with k~alpha sqrt(n) gives gamma <= e.
- Use case: Exercise 6.5.4; upper bounds for longest increasing subsequences.
- Tags: random-permutation, lis, first-moment, stirling

###### Branching Laplace martingale speed bound

- ID: `ch6_exercise_method_branching_laplace_martingale_bound`
- Kind: proof-template
- Summary: Normalize the generation-n Laplace sum by (mu phi(theta))^n to get a nonnegative martingale; Markov's inequality bounds early birth events when exp(-theta a)/(mu phi(theta))>1.
- Use case: Exercise 6.5.5; age-dependent branching speed upper-tail bounds.
- Tags: branching-process, laplace-transform, martingale, large-deviations

##### Exercise Record Index

###### 6.1 - Stationarity, invariant events, ergodicity, and measure-preserving examples

- Exercise 6.1.1: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_invariant_sigma_field, durrett_ch6_ergodicity_definition, durrett_ch6_measure_preserving_shift_model`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.2: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_invariant_sigma_field, durrett_ch6_measure_preserving_shift_model`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.3: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_circle_rotation_ergodicity, durrett_ch6_ergodicity_definition, durrett_ch6_invariant_sigma_field`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.4: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_stationary_sequence_definition, durrett_ch6_measure_preserving_shift_model`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.5: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_functions_of_stationary_processes, durrett_ch6_stationary_sequence_definition, durrett_ch6_ergodicity_definition`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.6: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_stationary_sequence_definition, durrett_ch6_ergodicity_definition, durrett_ch6_functions_of_stationary_processes, durrett_ch6_iid_shift_ergodic`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.
- Exercise 6.1.7: method tags `stationarity, invariant-events, ergodicity, shift-model, measure-preserving`; knowledge used `durrett_ch6_measure_preserving_shift_model, durrett_ch6_stationary_sequence_definition, durrett_ch6_invariant_sigma_field`; new knowledge `ch6_exercise_method_invariant_sigma_field_measurable_functions, ch6_exercise_method_almost_invariant_strictification, ch6_exercise_method_direct_irrational_rotation_ergodicity, ch6_exercise_method_two_sided_stationary_extension, ch6_exercise_method_factor_stationarity_ergodicity, ch6_exercise_method_random_phase_iid_blocks, ch6_exercise_method_gauss_map_invariant_density`.

###### 6.2 - Birkhoff upgrades, moving observables, and maximal inequalities

- Exercise 6.2.1: method tags `birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality`; knowledge used `durrett_ch6_birkhoff_ergodic_theorem, durrett_ch6_lp_upgrade_birkhoff, durrett_ch6_invariant_sigma_field`; new knowledge `ch6_exercise_method_lp_upgrade_by_truncation, ch6_exercise_method_moving_observable_ergodic_average, ch6_exercise_method_wiener_maximal_from_maximal_ergodic`.
- Exercise 6.2.2: method tags `birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality`; knowledge used `durrett_ch6_birkhoff_ergodic_theorem, durrett_ch6_invariant_sigma_field, durrett_ch6_measure_preserving_shift_model`; new knowledge `ch6_exercise_method_lp_upgrade_by_truncation, ch6_exercise_method_moving_observable_ergodic_average, ch6_exercise_method_wiener_maximal_from_maximal_ergodic`.
- Exercise 6.2.3: method tags `birkhoff, lp-convergence, truncation, moving-observable, maximal-inequality`; knowledge used `durrett_ch6_maximal_ergodic_lemma, durrett_ch6_birkhoff_ergodic_theorem`; new knowledge `ch6_exercise_method_lp_upgrade_by_truncation, ch6_exercise_method_moving_observable_ergodic_average, ch6_exercise_method_wiener_maximal_from_maximal_ergodic`.

###### 6.3 - Range growth, recurrence, cycle tricks, and stationary renewal bias

- Exercise 6.3.1: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_range_growth_stationary_increments, durrett_ch6_birkhoff_ergodic_theorem`; new knowledge `ch6_exercise_method_range_last_visit_counting, ch6_exercise_method_positive_drift_escape_probability, ch6_exercise_method_cycle_trick_occupation_ratio, ch6_exercise_method_stationary_renewal_waiting_bias`.
- Exercise 6.3.2: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_zero_drift_integer_recurrence, durrett_ch6_range_growth_stationary_increments, durrett_ch6_birkhoff_ergodic_theorem`; new knowledge `ch6_exercise_method_range_last_visit_counting, ch6_exercise_method_positive_drift_escape_probability, ch6_exercise_method_cycle_trick_occupation_ratio, ch6_exercise_method_stationary_renewal_waiting_bias`.
- Exercise 6.3.3: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_stationary_return_times_kac, durrett_ch6_cycle_trick_stationary_measure, durrett_ch6_stationary_sequence_definition`; new knowledge `ch6_exercise_method_range_last_visit_counting, ch6_exercise_method_positive_drift_escape_probability, ch6_exercise_method_cycle_trick_occupation_ratio, ch6_exercise_method_stationary_renewal_waiting_bias`.
- Exercise 6.3.4: method tags `recurrence, range, last-visit, cycle-trick, stationary-renewal`; knowledge used `durrett_ch6_stationary_return_times_kac, durrett_ch6_stationary_renewal_waiting_time, durrett_ch6_cycle_trick_stationary_measure`; new knowledge `ch6_exercise_method_range_last_visit_counting, ch6_exercise_method_positive_drift_escape_probability, ch6_exercise_method_cycle_trick_occupation_ratio, ch6_exercise_method_stationary_renewal_waiting_bias`.

###### 6.5 - Applications of subadditivity to LCS, LIS, Poisson paths, and branching

- Exercise 6.5.1: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_subadditive_ergodic_theorem, durrett_ch6_fekete_expectation_step`; new knowledge `ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound`.
- Exercise 6.5.2: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_longest_common_subsequence_limit, durrett_ch6_subadditive_ergodic_theorem`; new knowledge `ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound`.
- Exercise 6.5.3: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_increasing_subsequence_permutation, durrett_ch6_poisson_square_time_change, durrett_ch6_subadditive_ergodic_theorem`; new knowledge `ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound`.
- Exercise 6.5.4: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_increasing_subsequence_permutation, durrett_ch6_poisson_square_time_change`; new knowledge `ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound`.
- Exercise 6.5.5: method tags `subadditivity, first-moment, poissonization, branching-martingale, large-deviations`; knowledge used `durrett_ch6_age_dependent_branching_speed, durrett_ch6_branching_speed_large_deviation_formula, durrett_ch6_subadditive_ergodic_theorem`; new knowledge `ch6_exercise_method_arbitrarily_slow_subadditive_convergence, ch6_exercise_method_lcs_first_moment_bounds, ch6_exercise_method_poisson_greedy_increasing_path_lower_bound, ch6_exercise_method_permutation_lis_first_moment_upper_bound, ch6_exercise_method_branching_laplace_martingale_bound`.

## Chapter 7

### Durrett Chapter 7 LLM Viki: Brownian Motion

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter7.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

#### Section Guides

##### 7.1 Definition and Construction

- Goal: Define Brownian motion rigorously, construct it, and understand the first layer of path regularity.

- Must master: independent Gaussian increments, Brownian scaling, Gaussian covariance characterization, Kolmogorov continuity criterion, Holder continuity below 1/2, nowhere differentiability, quadratic variation intuition

- Prelim angle: This section supplies the definitions and scaling heuristics behind nearly every Brownian calculation.

##### 7.2 Markov Property, Blumenthal's 0-1 Law

- Goal: Restart Brownian motion at deterministic times and use 0-1 laws for immediate and tail behavior.

- Must master: Markov property, Blumenthal 0-1 law, immediate hitting, time inversion, tail 0-1 law, one-dimensional recurrence

- Prelim angle: These tools turn qualitative path behavior into short rigorous arguments.

##### 7.3 Stopping Times, Strong Markov Property

- Goal: Formalize random times and prove that Brownian motion can be restarted at them.

- Must master: stopping time definitions, hitting times of open and closed sets, F_S, B_S measurability, strong Markov property

- Prelim angle: Most Brownian hitting-time and reflection-principle problems depend on this section.

##### 7.4 Path Properties

- Goal: Use strong Markov arguments to analyze zeros, first passage times, reflection, and arcsine laws.

- Must master: zero set structure, hitting-time increments, hitting-time scaling, reflection principle, first-passage density, arcsine law

- Prelim angle: This section is the computational core for Brownian maxima and barrier-crossing questions.

##### 7.5 Martingales

- Goal: Use Brownian martingales and optional stopping to compute exit probabilities, exit times, and Laplace transforms.

- Must master: optional stopping, B_t martingale, B_t^2-t martingale, exponential martingale, heat-equation martingales, exit-time formulas

- Prelim angle: The fastest route to most exact Brownian interval and hitting-time computations.

##### 7.6 Ito's Formula*

- Goal: Replace ordinary calculus with Ito calculus for Brownian paths and connect stochastic calculus to PDE/martingale methods.

- Must master: one-dimensional Ito formula, stochastic integral martingale property, time-space Ito formula, exponential Brownian motion, multidimensional Ito formula

- Prelim angle: Even if starred, Ito's formula explains why Brownian martingales and heat equations fit together.

#### Knowledge Pieces

##### Brownian motion definition

- ID: `durrett_ch7_brownian_definition`

- Section: 7.1 Definition and Construction

- Kind: definition

- Summary: A Brownian motion has independent increments, Gaussian increments B(s+t)-B(s) with mean 0 and variance t, and almost surely continuous sample paths.

- Proof idea: The definition encodes CLT scaling for small displacements while adding continuity to rule out arbitrary versions with the same finite-dimensional laws.

- Exam use: Use as the base checklist whenever a process is claimed to be Brownian.

- Pitfall: Independent Gaussian increments alone do not automatically give continuous paths unless a continuous modification is specified.

- Tags: brownian-motion, gaussian-increments, continuous-paths

##### Translation invariance of increments

- ID: `durrett_ch7_translation_invariance`

- Section: 7.1 Definition and Construction

- Kind: fact

- Summary: The process {B_t-B_0:t>=0} is independent of B_0 and has the law of Brownian motion started at 0.

- Proof idea: Use independence of the initial value and subsequent increments, then extend from finite-dimensional cylinder events by a pi-lambda argument.

- Exam use: Lets hitting and exit calculations reduce to a Brownian motion started at 0 or at the current location.

- Pitfall: This is spatial translation of the starting point, not time-shift Markov conditioning.

- Tags: translation-invariance, increments, starting-point

##### Brownian scaling

- ID: `durrett_ch7_brownian_scaling`

- Section: 7.1 Definition and Construction

- Kind: formula

- Summary: For c>0 and B_0=0, {B_{cs}:s>=0} has the same finite-dimensional distributions as {sqrt(c) B_s:s>=0}.

- Proof idea: Check the one-dimensional normal variance and then use independent increments for all finite-dimensional distributions.

- Exam use: High-yield tool for hitting-time laws, path regularity, and rescaling exit probabilities.

- Pitfall: Scaling changes time by c and space by sqrt(c); reversing these powers is a common error.

- Tags: scaling, self-similarity, finite-dimensional-distributions

##### Gaussian process characterization

- ID: `durrett_ch7_gaussian_process_characterization`

- Section: 7.1 Definition and Construction

- Kind: theorem

- Summary: A continuous Gaussian process with mean 0 and covariance E[B_s B_t]=s wedge t is Brownian motion started at 0.

- Proof idea: The covariance matrix determines all finite-dimensional Gaussian laws and matches the independent-increment construction.

- Exam use: Use to prove transformed processes are Brownian, especially time inversion.

- Pitfall: The covariance condition alone is not enough without the Gaussian finite-dimensional law and continuity.

- Tags: gaussian-process, covariance, characterization

##### Kolmogorov extension construction

- ID: `durrett_ch7_kolmogorov_extension_construction`

- Section: 7.1 Definition and Construction

- Kind: construction

- Summary: Brownian finite-dimensional distributions are built from Gaussian transition densities and then extended consistently to a path-space probability law.

- Proof idea: Verify consistency of the transition-density integrals and apply Kolmogorov extension; then move to continuous paths through a modification/extension argument.

- Exam use: Explains why the formal process exists before path properties are studied.

- Pitfall: The raw product path space can make continuity nonmeasurable; the continuous-path space fixes the measurable model.

- Tags: construction, kolmogorov-extension, transition-density

##### Kolmogorov continuity criterion

- ID: `durrett_ch7_kolmogorov_continuity_criterion`

- Section: 7.1 Definition and Construction

- Kind: theorem

- Summary: If E|X_t-X_s|^beta <= K|t-s|^{1+alpha}, then dyadic paths admit a Holder-continuous version of any exponent gamma<alpha/beta.

- Proof idea: Control dyadic increments by Chebyshev and Borel-Cantelli, then chain dyadic intervals to bound arbitrary dyadic pairs.

- Exam use: Use moment bounds to prove sample-path continuity for Gaussian and process constructions.

- Pitfall: The exponent comes from alpha/beta, not beta/alpha; endpoint exponents are usually not obtained.

- Tags: kolmogorov-continuity, holder, borel-cantelli

##### Brownian Holder continuity below one half

- ID: `durrett_ch7_brownian_holder_half`

- Section: 7.1 Definition and Construction

- Kind: theorem

- Summary: Brownian paths are almost surely Holder continuous on compact intervals for every exponent gamma<1/2.

- Proof idea: Use Gaussian even moments E|B_t-B_s|^{2m}=C_m|t-s|^m in the Kolmogorov criterion and let m grow.

- Exam use: Useful for justifying pathwise approximations while remembering Brownian paths are rough.

- Pitfall: The exponent 1/2 itself is not included.

- Tags: holder, path-regularity, gaussian-moments

- Related: `durrett_ch7_kolmogorov_continuity_criterion`

##### Brownian paths are nowhere differentiable

- ID: `durrett_ch7_brownian_nowhere_differentiable`

- Section: 7.1 Definition and Construction

- Kind: theorem

- Summary: With probability one, Brownian paths are not Lipschitz continuous, and hence not differentiable, at any time.

- Proof idea: If a path were locally Lipschitz, several nearby small increments would all be tiny; Gaussian small-ball estimates make this probability vanish after covering.

- Exam use: Prevents calculus-style manipulation of B_t and motivates quadratic variation and Ito calculus.

- Pitfall: Continuity does not imply bounded variation or differentiability; Brownian paths are continuous but very rough.

- Tags: nondifferentiability, rough-paths, path-regularity

- Related: `durrett_ch7_brownian_holder_half`

##### Dyadic quadratic variation

- ID: `durrett_ch7_quadratic_variation_hint`

- Section: 7.1 Definition and Construction

- Kind: fact

- Summary: Along dyadic partitions of [0,t], the sum of squared Brownian increments converges to t in the sense used later for Ito's formula.

- Proof idea: Independence and Gaussian fourth-moment estimates show the mean is t and the variance of the sum goes to 0.

- Exam use: Core intuition behind the extra (1/2)f'' term in Ito's formula.

- Pitfall: This is about squared increments; ordinary total variation behaves very differently.

- Tags: quadratic-variation, dyadic-partitions, ito

##### Multidimensional Brownian motion

- ID: `durrett_ch7_d_dimensional_brownian`

- Section: 7.1 Definition and Construction

- Kind: definition

- Summary: A d-dimensional Brownian motion has independent one-dimensional Brownian coordinates and Gaussian transition density (2 pi t)^(-d/2) exp(-|y-x|^2/(2t)).

- Proof idea: Independence of coordinates factors the finite-dimensional distributions and gives the Euclidean Gaussian kernel.

- Exam use: Use for vector Ito formulas and multidimensional hitting or transition-density computations.

- Pitfall: Do not replace coordinate independence by merely matching each marginal coordinate law.

- Tags: multidimensional, transition-density, gaussian-kernel

##### Brownian Markov property

- ID: `durrett_ch7_markov_property`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: Conditioned on the present, the shifted future of Brownian motion has the law of Brownian motion started from the current state and is independent of the past.

- Proof idea: Prove first for bounded cylinder functions of the future using Gaussian transition densities, then extend by the monotone class theorem.

- Exam use: Use to restart Brownian motion at deterministic times and compute conditional expectations.

- Pitfall: The conditioning sigma-field is the completed right-continuous past; using an informal past can hide null-set issues.

- Tags: markov-property, conditional-expectation, shift

##### Right-continuous germ conditioning

- ID: `durrett_ch7_germ_field_equivalence`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: technical-fact

- Summary: For bounded path functionals, conditioning on F_s^+ agrees almost surely with conditioning on the raw past F_s^0.

- Proof idea: Approximate functionals by finite-dimensional ones and use the Markov property plus right-continuity of Brownian paths.

- Exam use: Clarifies why immediate-future events can be handled cleanly at time 0.

- Pitfall: This is an almost-sure equality of conditional expectations, not equality of all raw sigma-fields literally.

- Tags: germ-field, right-continuity, conditioning

##### Blumenthal's 0-1 law

- ID: `durrett_ch7_blumenthal_zero_one`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: Every event in the Brownian germ sigma-field F_0^+ has probability 0 or 1 under a fixed starting point.

- Proof idea: Condition the event on the raw time-zero sigma-field, which is trivial once the starting point is fixed.

- Exam use: Use for immediate hitting, local oscillation, and path behavior as t downarrow 0.

- Pitfall: The probability may depend on the starting point; the law is not automatically uniform in x.

- Tags: zero-one-law, germ-field, local-behavior

##### Immediate crossing at the origin

- ID: `durrett_ch7_immediate_positive_negative_hits`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: Starting from 0, Brownian motion hits (0,infinity), hits (-infinity,0), and returns to 0 immediately with probability one.

- Proof idea: Each event has positive probability at arbitrarily small times by normal symmetry; Blumenthal's law upgrades positive probability to probability one.

- Exam use: Useful when proving the zero set has no isolated points and when reasoning about local extrema.

- Pitfall: The return time is inf{t>0:B_t=0}; allowing t=0 would make the statement trivial.

- Tags: immediate-hitting, zero-set, blumenthal

- Related: `durrett_ch7_blumenthal_zero_one`

##### Brownian time inversion

- ID: `durrett_ch7_time_inversion`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: If B starts at 0, then X_0=0 and X_t=t B_{1/t} for t>0 is again Brownian motion.

- Proof idea: Check Gaussian finite-dimensional distributions and covariance, then prove continuity at 0 from B_u/u -> 0 as u -> infinity.

- Exam use: Transfers small-time Brownian statements into large-time statements.

- Pitfall: The transform is t B_{1/t}, not B_{1/t}/t.

- Tags: time-inversion, gaussian-characterization, large-time

- Related: `durrett_ch7_gaussian_process_characterization`

##### Brownian tail 0-1 law

- ID: `durrett_ch7_brownian_tail_zero_one`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: Events determined by the arbitrarily far future have probability identically 0 or identically 1 for all starting states.

- Proof idea: Time inversion turns a tail event into a germ event; the Markov property removes dependence on the starting point.

- Exam use: Use for recurrence and unbounded oscillation at infinity.

- Pitfall: This is stronger than the germ law because the conclusion is uniform in the starting state.

- Tags: tail-sigma-field, zero-one-law, time-inversion

- Related: `durrett_ch7_time_inversion`, `durrett_ch7_blumenthal_zero_one`

##### Large-time oscillation

- ID: `durrett_ch7_limsup_liminf_unbounded`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: One-dimensional Brownian motion satisfies limsup B_t/sqrt(t)=infinity and liminf B_t/sqrt(t)=-infinity almost surely.

- Proof idea: Discrete times have positive probability of exceeding any fixed multiple of sqrt(n) infinitely often; the tail 0-1 law upgrades this to probability one.

- Exam use: Quick route to recurrence and repeated level-crossing arguments.

- Pitfall: This is weaker than the law of the iterated logarithm but enough for recurrence.

- Tags: oscillation, tail-zero-one, recurrence

- Related: `durrett_ch7_brownian_tail_zero_one`

##### One-dimensional Brownian recurrence

- ID: `durrett_ch7_one_dimensional_recurrence`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: For every starting point, one-dimensional Brownian motion hits 0 infinitely often at arbitrarily large times almost surely.

- Proof idea: Large positive and negative oscillations plus path continuity force repeated crossings of 0.

- Exam use: Use whenever hitting times of points are assumed finite or when restarting at returns.

- Pitfall: Recurrence in one dimension does not generalize unchanged to higher-dimensional hitting of points.

- Tags: recurrence, hitting, one-dimensional

- Related: `durrett_ch7_limsup_liminf_unbounded`

##### Stopping time definition

- ID: `durrett_ch7_stopping_time_definition`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: definition

- Summary: A random time S is a stopping time when {S<t} is in F_t for every t; for right-continuous filtrations this is equivalent to using {S<=t}.

- Proof idea: The equivalence follows by countable unions/intersections and right-continuity of the filtration.

- Exam use: Use to verify that hitting, exit, minima, and approximating times are legitimate restart times.

- Pitfall: The definition is about information available by time t, not about whether S has a density or finite expectation.

- Tags: stopping-times, filtration, right-continuity

##### Open and closed hitting times are stopping times

- ID: `durrett_ch7_hitting_times_open_closed`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: theorem

- Summary: For continuous Brownian paths, the first hitting time of an open set or a closed set is a stopping time.

- Proof idea: Open sets use rational times before t; closed sets are obtained as increasing limits of hitting times of shrinking open neighborhoods.

- Exam use: Use to justify applying strong Markov property to level hitting and interval exit times.

- Pitfall: For general Borel sets the statement is true but much harder; do not use the open/closed proof blindly.

- Tags: hitting-times, open-sets, closed-sets

- Related: `durrett_ch7_stopping_time_definition`

##### Limits of stopping times

- ID: `durrett_ch7_stopping_time_limits`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: closure-property

- Summary: Increasing and decreasing limits of stopping times are stopping times in a right-continuous filtration.

- Proof idea: Write events for the limiting time as countable unions or intersections of the corresponding events for the approximating times.

- Exam use: Useful for proving complicated first-entry times by approximation.

- Pitfall: Right-continuity matters for some <= formulations.

- Tags: stopping-times, limits, approximation

##### Random shift and information at a stopping time

- ID: `durrett_ch7_random_shift_and_F_S`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: definition

- Summary: The shift theta_S removes the path before S and restarts time at S; F_S contains events whose restriction to {S<=t} is F_t-measurable for every t.

- Proof idea: These definitions formalize what is known at a random time and how to view the post-S path.

- Exam use: Needed to state the strong Markov property and optional stopping cleanly.

- Pitfall: F_S is not simply F_t with t replaced by a random variable; it has its own measurability definition.

- Tags: random-shift, stopped-sigma-field, strong-markov

##### Stopped value is known at the stopping time

- ID: `durrett_ch7_B_S_measurable`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: theorem

- Summary: If S is a stopping time, then B_S is F_S-measurable.

- Proof idea: Approximate S from above by dyadic stopping times, note each approximating value is measurable at the approximating time, and pass to the limit by path continuity.

- Exam use: Lets conditional expectations at stopping times depend on the random current position B_S.

- Pitfall: This uses continuity and the completed/right-continuous filtration setup.

- Tags: stopped-process, measurability, dyadic-approximation

##### Strong Markov property

- ID: `durrett_ch7_strong_markov_property`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: theorem

- Summary: Given a stopping time S, the post-S Brownian path conditioned on F_S has the law of Brownian motion started at B_S, on {S<infinity}.

- Proof idea: First prove it for discrete-valued stopping times, approximate a general S from above by dyadic stopping times, then extend by monotone class.

- Exam use: The central engine for reflection principle, hitting-time increments, recurrence refinements, and exit calculations.

- Pitfall: Always check S is a stopping time and restrict or control the event {S<infinity}.

- Tags: strong-markov, stopping-times, restart

- Related: `durrett_ch7_random_shift_and_F_S`, `durrett_ch7_B_S_measurable`

##### Brownian zero set structure

- ID: `durrett_ch7_zero_set_structure`

- Section: 7.4 Path Properties

- Kind: fact

- Summary: The zero set of one-dimensional Brownian motion is almost surely closed, has no isolated points, is uncountable, and has Lebesgue measure zero.

- Proof idea: Continuity gives closedness; recurrence plus immediate return and strong Markov give no isolated zeros; Fubini gives zero Lebesgue measure.

- Exam use: Good conceptual anchor for path-property problems involving returns to zero.

- Pitfall: Uncountable does not imply positive Lebesgue measure.

- Tags: zero-set, perfect-set, measure-zero

- Related: `durrett_ch7_immediate_positive_negative_hits`, `durrett_ch7_strong_markov_property`

##### Level hitting times have stationary independent increments

- ID: `durrett_ch7_hitting_time_subordinator`

- Section: 7.4 Path Properties

- Kind: theorem

- Summary: Under P_0, the process {T_a:a>=0}, where T_a=inf{t:B_t=a}, has stationary independent increments as a function of the level a.

- Proof idea: After hitting level a, the strong Markov property and translation invariance identify T_b-T_a with a fresh copy of T_{b-a}.

- Exam use: Use to recognize hitting times as a stable subordinator of index 1/2.

- Pitfall: The parameter is the spatial level a, not the Brownian time parameter.

- Tags: hitting-times, subordinator, stationary-independent-increments

- Related: `durrett_ch7_strong_markov_property`, `durrett_ch7_translation_invariance`

##### Hitting-time scaling

- ID: `durrett_ch7_hitting_time_scaling`

- Section: 7.4 Path Properties

- Kind: formula

- Summary: For a>0, T_a has the same distribution as a^2 T_1.

- Proof idea: Apply Brownian scaling: hitting a in the original process corresponds to hitting 1 after rescaling space by a and time by a^2.

- Exam use: Quickly reduces level-dependent hitting-time questions to the case a=1.

- Pitfall: The square on a is essential; hitting times scale like distance squared.

- Tags: hitting-times, scaling, stable-law

- Related: `durrett_ch7_brownian_scaling`

##### Hitting-time Laplace transform shape

- ID: `durrett_ch7_hitting_time_laplace_shape`

- Section: 7.4 Path Properties

- Kind: formula

- Summary: The Laplace transform phi_a(lambda)=E_0 exp(-lambda T_a) has the exponential form exp(-a c(lambda)), and eventually c(lambda)=sqrt(2 lambda).

- Proof idea: Stationary independent increments give multiplicativity in the level; scaling forces c(lambda) to be proportional to sqrt(lambda).

- Exam use: Use before or after exponential martingales to compute exact transforms.

- Pitfall: The constant sqrt(2) requires the martingale calculation; scaling alone gives only proportionality.

- Tags: laplace-transform, hitting-times, scaling

- Related: `durrett_ch7_hitting_time_subordinator`, `durrett_ch7_hitting_time_scaling`

##### Reflection principle

- ID: `durrett_ch7_reflection_principle`

- Section: 7.4 Path Properties

- Kind: theorem

- Summary: For a>0, P_0(T_a<t)=2 P_0(B_t>=a), where T_a is the first hitting time of level a.

- Proof idea: After the first hit of a, reflect the remaining path; rigorously, apply the strong Markov property and symmetry at T_a.

- Exam use: Essential for maxima distributions, hitting-time densities, and barrier-crossing probabilities.

- Pitfall: The result is for Brownian motion without drift and with a one-sided level; drift or two-sided barriers need changes.

- Tags: reflection-principle, maximum, hitting-times

- Related: `durrett_ch7_strong_markov_property`

##### First hitting-time density

- ID: `durrett_ch7_hitting_time_density`

- Section: 7.4 Path Properties

- Kind: formula

- Summary: For a>0, T_a has density a (2 pi s^3)^(-1/2) exp(-a^2/(2s)) on s>0.

- Proof idea: Differentiate the reflection-principle distribution after a change of variables in the normal tail.

- Exam use: Use for explicit integrals involving first passage times.

- Pitfall: This density has heavy tail and infinite mean; do not apply finite-mean intuition.

- Tags: hitting-time-density, reflection-principle, first-passage

- Related: `durrett_ch7_reflection_principle`

##### Arcsine law for the last zero before one

- ID: `durrett_ch7_arcsine_last_zero`

- Section: 7.4 Path Properties

- Kind: example-pattern

- Summary: If L=sup{t<=1:B_t=0}, then P_0(L<=s)=(2/pi) arcsin(sqrt(s)) for 0<s<1.

- Proof idea: Condition at time s, use the Markov property and the hitting-time survival probability, then evaluate the integral.

- Exam use: Classic Brownian path distribution and a bridge to random-walk arcsine laws.

- Pitfall: The density blows up near 0 and 1; the last zero is not concentrated near 1/2.

- Tags: arcsine-law, last-zero, path-distribution

- Related: `durrett_ch7_hitting_time_density`

##### Optional stopping for bounded stopping times

- ID: `durrett_ch7_optional_stopping_bounded`

- Section: 7.5 Martingales

- Kind: theorem

- Summary: A right-continuous martingale stopped at a bounded stopping time has the same expectation as at time 0.

- Proof idea: Approximate the stopping time from above by dyadic times and pass to the limit using right-continuity of the martingale and sigma-fields.

- Exam use: Foundation for Brownian exit probabilities and expected exit times.

- Pitfall: Boundedness or another valid stopping hypothesis is required; optional stopping is not automatic for unbounded times.

- Tags: optional-stopping, martingales, bounded-stopping-time

##### Brownian motion is a martingale

- ID: `durrett_ch7_brownian_martingale`

- Section: 7.5 Martingales

- Kind: theorem

- Summary: B_t is a martingale with respect to the Brownian filtration.

- Proof idea: The Markov property gives E_x[B_t|F_s]=E_{B_s}[B_{t-s}]=B_s.

- Exam use: Use with optional stopping to compute two-sided hitting probabilities.

- Pitfall: Requires integrability and the correct filtration.

- Tags: martingale, brownian-motion, markov-property

- Related: `durrett_ch7_markov_property`

##### Two-sided exit probability

- ID: `durrett_ch7_two_sided_exit_probability`

- Section: 7.5 Martingales

- Kind: formula

- Summary: For a<x<b, P_x(T_a<T_b)=(b-x)/(b-a).

- Proof idea: Stop the martingale B_t at T_a wedge T_b and solve x=a p+b(1-p).

- Exam use: High-yield gambler's-ruin analogue for Brownian motion.

- Pitfall: First show or know the exit time is finite; then justify the stopping/localization step.

- Tags: exit-probability, optional-stopping, gambler-ruin

- Related: `durrett_ch7_brownian_martingale`, `durrett_ch7_optional_stopping_bounded`

##### Square martingale

- ID: `durrett_ch7_square_martingale`

- Section: 7.5 Martingales

- Kind: theorem

- Summary: B_t^2-t is a martingale.

- Proof idea: Expand B_t=B_s+(B_t-B_s), use independence, mean zero, and Var(B_t-B_s)=t-s.

- Exam use: Use to compute expected exit times and quadratic variation intuition.

- Pitfall: B_t^2 alone is a submartingale, not a martingale.

- Tags: martingale, quadratic-variation, second-moment

##### Expected exit time from an interval

- ID: `durrett_ch7_expected_interval_exit_time`

- Section: 7.5 Martingales

- Kind: formula

- Summary: If T=inf{t:B_t notin (a,b)} with a<0<b and B_0=0, then E_0 T=-ab.

- Proof idea: Stop B_t^2-t at T wedge t, pass to the limit, and use the exit probabilities to compute E[B_T^2].

- Exam use: Standard computation for Brownian mean exit time from a bounded interval.

- Pitfall: Do not confuse exit from (a,b) with hitting a single level; the one-sided hitting time has infinite mean.

- Tags: exit-time, square-martingale, optional-stopping

- Related: `durrett_ch7_square_martingale`, `durrett_ch7_two_sided_exit_probability`

##### Exponential Brownian martingale

- ID: `durrett_ch7_exponential_martingale`

- Section: 7.5 Martingales

- Kind: theorem

- Summary: For real theta, exp(theta B_t - theta^2 t/2) is a martingale.

- Proof idea: Condition on F_s, factor out exp(theta B_s), and use the normal moment generating function for the independent increment.

- Exam use: Use for Laplace transforms of hitting times and drift/barrier calculations.

- Pitfall: The compensator is theta^2 t/2; missing the factor 1/2 breaks the martingale.

- Tags: exponential-martingale, laplace-transform, gaussian-mgf

##### Exact Laplace transform of a hitting time

- ID: `durrett_ch7_hitting_time_laplace_exact`

- Section: 7.5 Martingales

- Kind: formula

- Summary: For T_a=inf{t:B_t=a} and a>0, E_0 exp(-lambda T_a)=exp(-a sqrt(2 lambda)).

- Proof idea: Stop the exponential martingale with theta=sqrt(2 lambda) at T_a wedge t and pass to the limit.

- Exam use: Fastest exact calculation for first-passage Laplace transforms.

- Pitfall: The formula is for one-sided hitting from 0 to a>0; signs and starting points need translation.

- Tags: hitting-times, laplace-transform, exponential-martingale

- Related: `durrett_ch7_exponential_martingale`, `durrett_ch7_hitting_time_laplace_shape`

##### Heat-equation martingales

- ID: `durrett_ch7_heat_equation_martingales`

- Section: 7.5 Martingales

- Kind: theorem

- Summary: If u_t+(1/2)u_xx=0 for a suitable polynomial u(t,x), then u(t,B_t) is a martingale.

- Proof idea: Use Brownian transition densities and the heat equation to show the conditional expectation is unchanged over time.

- Exam use: Generates polynomial martingales such as B_t^3-3tB_t and B_t^4-6tB_t^2+3t^2.

- Pitfall: The sign is the backward heat equation sign; check whether the time variable is forward or backward in a problem.

- Tags: heat-equation, polynomial-martingales, brownian-martingales

##### Second moment of symmetric exit time

- ID: `durrett_ch7_symmetric_exit_second_moment`

- Section: 7.5 Martingales

- Kind: formula

- Summary: For T=inf{t:B_t notin (-a,a)}, E[T^2]=5a^4/3.

- Proof idea: Apply optional stopping to the fourth-degree polynomial martingale and combine with E[T]=a^2.

- Exam use: Useful template for computing higher exit-time moments via polynomial martingales.

- Pitfall: In nonsymmetric intervals, T and B_T^2 need not be independent, so the same shortcut fails.

- Tags: exit-time-moments, polynomial-martingales, optional-stopping

- Related: `durrett_ch7_heat_equation_martingales`, `durrett_ch7_expected_interval_exit_time`

##### One-dimensional Ito formula

- ID: `durrett_ch7_ito_formula_one_dimensional`

- Section: 7.6 Ito's Formula*

- Kind: theorem

- Summary: For f in C^2, f(B_t)-f(B_0)=int_0^t f'(B_s)dB_s + (1/2)int_0^t f''(B_s)ds.

- Proof idea: Taylor expand over partitions; first-order terms define the stochastic integral and squared increments converge to elapsed time.

- Exam use: The central calculus rule for functions of Brownian motion.

- Pitfall: Ordinary chain rule misses the second-derivative correction.

- Tags: ito-formula, stochastic-calculus, quadratic-variation

- Related: `durrett_ch7_quadratic_variation_hint`

##### Stochastic integral martingale criterion

- ID: `durrett_ch7_stochastic_integral_is_martingale`

- Section: 7.6 Ito's Formula*

- Kind: theorem

- Summary: If g is continuous and E int_0^t |g(B_s)|^2 ds is finite, then int_0^t g(B_s)dB_s is a continuous martingale.

- Proof idea: Approximate by adapted step sums, use conditional mean zero and L2 bounds, then pass to limits.

- Exam use: Lets Ito formula immediately produce martingales when the drift term vanishes.

- Pitfall: Square-integrability is the hypothesis that keeps the stochastic integral controlled.

- Tags: stochastic-integral, martingale, square-integrability

##### Time-space Ito formula

- ID: `durrett_ch7_ito_formula_time_space`

- Section: 7.6 Ito's Formula*

- Kind: theorem

- Summary: For f in C^2 in time and space, df(t,B_t)=f_t(t,B_t)dt+f_x(t,B_t)dB_t+(1/2)f_xx(t,B_t)dt.

- Proof idea: Apply the one-dimensional formula with an added deterministic time increment and keep only first-order dt plus quadratic Brownian terms.

- Exam use: Use to connect Brownian martingales with PDEs and exponential models.

- Pitfall: There is no term involving dt dB_t or (dt)^2 in the limit.

- Tags: ito-formula, pde, time-space

- Related: `durrett_ch7_ito_formula_one_dimensional`

##### Ito formula for exponential Brownian motion

- ID: `durrett_ch7_exponential_brownian_ito`

- Section: 7.6 Ito's Formula*

- Kind: example-pattern

- Summary: For X_t=exp(mu t+sigma B_t), Ito's formula gives dX_t=(mu+sigma^2/2)X_t dt+sigma X_t dB_t.

- Proof idea: Differentiate u(t,x)=exp(mu t+sigma x) and insert u_t, u_x, and u_xx into the time-space Ito formula.

- Exam use: Common model pattern for geometric Brownian motion and for checking exponential martingales.

- Pitfall: The drift of exp(mu t+sigma B_t) is mu+sigma^2/2, not just mu.

- Tags: geometric-brownian-motion, ito-formula, exponential

- Related: `durrett_ch7_ito_formula_time_space`

##### Multidimensional Ito formula

- ID: `durrett_ch7_multidimensional_ito_formula`

- Section: 7.6 Ito's Formula*

- Kind: theorem

- Summary: For d-dimensional Brownian motion, df(t,B_t)=f_t dt+sum_i f_i dB_t^i+(1/2)sum_i f_{ii} dt.

- Proof idea: Second-order Taylor expansion keeps only diagonal quadratic variations; cross terms vanish for independent coordinates.

- Exam use: Use for radial processes, harmonic functions, and multidimensional martingales.

- Pitfall: The Laplacian term appears with factor 1/2; mixed second derivatives do not contribute for standard independent Brownian coordinates.

- Tags: multidimensional-ito, laplacian, brownian-motion

- Related: `durrett_ch7_d_dimensional_brownian`, `durrett_ch7_ito_formula_time_space`

### Chapter 7 Exercise Viki

#### Chapter 7 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter7/Chapter7Exercises.tex`
Source PDF: `Probability/Exercises/Chapter7/Chapter7Exercises.pdf`

This dataset turns the solved Chapter 7 Brownian motion exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.

##### Files

- `chapter7_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.
- `chapter7_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter7_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter7_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.
- `chapter7_exercise_viki.md`: human-readable overview.
- `manifest.json`: dataset metadata.

##### Section Method Cards

###### 7.1 - Brownian construction, Gaussian calculations, path roughness, and quadratic variation

Reduce finite-dimensional Brownian questions to independent Gaussian increments; use rotational normal geometry, Gaussian linear functionals, small-increment estimates, and Borel-Cantelli for path regularity.

Tags: brownian-definition, gaussian-increments, holder, quadratic-variation

###### 7.2 - Markov property, Blumenthal 0-1 law, immediate behavior, and recurrence patterns

Condition on Brownian position at a deterministic time, translate future hitting events into fresh Brownian probabilities, and use germ 0-1 laws to upgrade positive-probability local behavior to almost sure behavior.

Tags: markov-property, blumenthal, germ-field, recurrence

###### 7.3 - Stopping-time closure and stopped sigma-fields

Prove stopping-time claims by rewriting events with countable unions over rational times, use open/closed hitting-time facts, and apply the definition of F_S through restrictions to {S <= t}.

Tags: stopping-times, stopped-sigma-field, rational-time, closure-properties

###### 7.4 - Brownian path properties, reflection, hitting-time densities, and arcsine-type laws

Combine strong Markov, reflection, hitting-time densities, and conditioning at fixed times to compute distributions of returns, maxima, endpoints, and zero-set events.

Tags: reflection-principle, hitting-times, cauchy, zero-set, arcsine

###### 7.5 - Brownian martingales, optional stopping, exit transforms, and moment computations

Choose martingales tailored to the target: cosh/exponential martingales for Laplace transforms, heat-polynomial martingales for exit moments, and maximal inequalities for almost-sure growth bounds.

Tags: martingales, optional-stopping, laplace-transform, exit-times, polynomial-martingales

###### 7.6 - Ito formula, stochastic integral martingales, and Brownian moment/radial identities

Apply one-dimensional, time-space, and multidimensional Ito formulas; identify drift terms, turn zero drift into martingales, and take expectations to get moment recursions.

Tags: ito-formula, stochastic-integral, moments, radial-process, bessel

##### New Knowledge Pieces

###### Two-time Brownian sign probability by Gaussian wedge angle

- ID: `exercise_method_ch7_gaussian_wedge_probability`
- Kind: calculation-template
- Summary: Write B_t as B_s plus an independent increment, standardize to a rotationally symmetric bivariate normal, and compute the sector angle cut out by the two half-planes.
- Use case: Exercise 7.1.1; probabilities involving signs of correlated Brownian values.
- Tags: brownian, gaussian-geometry, sign-probability

###### Brownian polynomial moments by independent increment expansion

- ID: `exercise_method_ch7_increment_expansion_moments`
- Kind: calculation-template
- Summary: Represent B_1, B_2, B_3 through independent unit Gaussian increments, expand the polynomial, and discard terms with centered odd factors.
- Use case: Exercise 7.1.2; low-order Brownian moment computations.
- Tags: brownian-moments, independent-increments, gaussian

###### Deterministic Brownian integrals are Gaussian

- ID: `exercise_method_ch7_brownian_integral_gaussian`
- Kind: calculation-template
- Summary: Approximate an integral of B_s against deterministic ds by Riemann sums; each sum is Gaussian, and the variance is the double integral of r wedge s.
- Use case: Exercise 7.1.3; integrated Brownian motion and Gaussian linear functionals.
- Tags: gaussian-process, brownian-integral, covariance

###### Events in raw path sigma-field depend on countably many coordinates

- ID: `exercise_method_ch7_countable_coordinate_sigma_field`
- Kind: proof-template
- Summary: Show the class of events depending on a countable coordinate list is a sigma-field containing all finite-dimensional cylinders.
- Use case: Exercise 7.1.4; path-space measurability and cylinder sigma-fields.
- Tags: path-space, sigma-field, coordinates

###### K-increment obstruction to Brownian Holder regularity

- ID: `exercise_method_ch7_k_increment_holder_obstruction`
- Kind: proof-template
- Summary: If a Holder point exists, a nearby block of k Gaussian increments must all be unusually small; union bound gives probability O(n^{1+k(1/2-gamma)}).
- Use case: Exercise 7.1.5; proving no Holder points above exponent 1/2.
- Tags: holder, small-increments, brownian-roughness

###### Dyadic quadratic variation by L2 plus Borel-Cantelli

- ID: `exercise_method_ch7_dyadic_quadratic_variation_borel_cantelli`
- Kind: proof-template
- Summary: Compute variance of the dyadic squared-increment sum as 2t^2 2^{-n}, apply Chebyshev, and sum over n to get almost sure convergence.
- Use case: Exercise 7.1.6; Brownian quadratic variation along dyadic partitions.
- Tags: quadratic-variation, borel-cantelli, chebyshev

###### Deterministic-time Markov conditioning for hitting survival

- ID: `exercise_method_ch7_markov_conditioning_hitting_survival`
- Kind: proof-template
- Summary: Condition on B_s=y, replace the future event by a hitting probability for Brownian motion started at y, and integrate against the transition density.
- Use case: Exercises 7.2.1 and 7.2.2; return-time and last-zero decompositions.
- Tags: markov-property, hitting-time, transition-density

###### Last-zero event as no future hit after conditioning

- ID: `exercise_method_ch7_last_zero_markov_decomposition`
- Kind: calculation-template
- Summary: The event L <= t is equivalent to no zero in (t,1]; after conditioning on B_t, this becomes P_y(T_0 > 1-t).
- Use case: Exercise 7.2.2 and arcsine-law calculations.
- Tags: last-zero, markov-property, survival-probability

###### Dense local maxima from immediate two-sided crossing

- ID: `exercise_method_ch7_dense_local_maxima_from_immediate_crossing`
- Kind: proof-template
- Summary: Take shrinking deterministic intervals, use continuity to get a maximum, and use immediate crossing forward and backward to rule out endpoints.
- Use case: Exercise 7.2.3; path-local extremum arguments.
- Tags: local-maxima, immediate-crossing, brownian-paths

###### Germ-field limsup constants via Blumenthal 0-1

- ID: `exercise_method_ch7_germ_limsup_constant`
- Kind: proof-template
- Summary: For a small-time limsup L, events {L <= r} lie in the germ sigma-field; 0-1 probabilities force L to be almost surely constant.
- Use case: Exercise 7.2.4(i); local Brownian growth rates.
- Tags: blumenthal, limsup, germ-field

###### Brownian paths are not 1/2-Holder at a fixed time

- ID: `exercise_method_ch7_sqrt_time_not_holder_half`
- Kind: proof-template
- Summary: Use B_delta/sqrt(delta) standard normal to get positive probability of arbitrarily large normalized values, then apply Blumenthal 0-1.
- Use case: Exercise 7.2.4(ii); critical Brownian Holder exponent.
- Tags: holder, blumenthal, sqrt-time

###### F-sigma hitting times as infima of closed hitting times

- ID: `exercise_method_ch7_fsigma_hitting_time`
- Kind: proof-template
- Summary: Write the F-sigma set as a countable union of closed sets, use closed-set hitting times, and express {inf T_n < t} as a countable union.
- Use case: Exercise 7.3.1; proving first-entry times are stopping times.
- Tags: stopping-time, hitting-time, f-sigma

###### Sum of stopping times via rational split

- ID: `exercise_method_ch7_sum_stopping_time_rational_split`
- Kind: proof-template
- Summary: Write {S+T<t} as the union over rational q<t of {S<q} cap {T<t-q}.
- Use case: Exercise 7.3.2; closure properties for stopping times.
- Tags: stopping-time, rationals, closure

###### Supremum and infimum of stopping times

- ID: `exercise_method_ch7_sup_inf_stopping_times`
- Kind: proof-template
- Summary: Use {inf T_n<t}=union {T_n<t} and {sup T_n<=t}=intersection {T_n<=t}, then build liminf and limsup from sup/inf combinations.
- Use case: Exercise 7.3.3; stopping-time sequence operations.
- Tags: stopping-time, supremum, infimum

###### Use F_S by restricting to {S <= t}

- ID: `exercise_method_ch7_stopped_event_restriction`
- Kind: proof-template
- Summary: To prove an event-defined random time is a stopping time, intersect the event A in F_S with {S <= t} and use the definition of F_S.
- Use case: Exercise 7.3.4; killing a stopping time on an event.
- Tags: stopped-sigma-field, stopping-time, restriction

###### Comparison events for stopping times are known at either time

- ID: `exercise_method_ch7_compare_stopping_times_in_stopped_fields`
- Kind: proof-template
- Summary: Represent {S<T} or {S>T} on {S<t} using countable rational cuts, then repeat with S and T interchanged.
- Use case: Exercise 7.3.5; stopped sigma-field comparison events.
- Tags: stopped-sigma-field, rational-cuts, comparison

###### Stopped sigma-field at S wedge T

- ID: `exercise_method_ch7_meet_stopped_sigma_field`
- Kind: proof-template
- Summary: Use S wedge T <= S,T for one inclusion; for the reverse, decompose A cap {S wedge T <= t} into the union of A cap {S <= t} and A cap {T <= t}.
- Use case: Exercise 7.3.6; identities among stopped sigma-fields.
- Tags: stopped-sigma-field, minimum, filtration

###### Planar Brownian level hitting gives Cauchy law

- ID: `exercise_method_ch7_planar_hitting_cauchy`
- Kind: calculation-template
- Summary: Condition the first coordinate on the second-coordinate hitting time, then use the hitting-time Laplace transform to get characteristic function exp(-a|u|).
- Use case: Exercise 7.4.1; Cauchy distribution from Brownian hitting.
- Tags: cauchy, planar-brownian, hitting-time

###### Return-time density by mixing first-hit densities

- ID: `exercise_method_ch7_return_time_density_mixture`
- Kind: calculation-template
- Summary: Condition on B_1=y and integrate the first-hitting density from y to 0 against the N(0,1) density.
- Use case: Exercise 7.4.2; density of the next zero after time 1.
- Tags: return-time, density, markov-property

###### Endpoint subdensity after barrier crossing

- ID: `exercise_method_ch7_reflected_endpoint_subdensity`
- Kind: calculation-template
- Summary: Reflect paths after the first hit of level a to identify P(T_a<t, B_t in dx) below a with the free Brownian density at 2a-x.
- Use case: Exercise 7.4.3(a,b); reflection-principle refinements.
- Tags: reflection-principle, subdensity, barrier

###### Joint density of Brownian maximum and endpoint

- ID: `exercise_method_ch7_joint_max_endpoint_density`
- Kind: calculation-template
- Summary: Use {M_t>a}={T_a<t}, write the reflected endpoint subdensity, and differentiate the tail probability in the maximum level a.
- Use case: Exercise 7.4.3(c); Brownian maximum-endpoint joint law.
- Tags: maximum, joint-density, reflection

###### Zero-in-interval probability by hitting-time density integral

- ID: `exercise_method_ch7_zero_interval_arccos_integral`
- Kind: calculation-template
- Summary: Condition on B_s, integrate the first-hit density over [0,t-s], swap integrals, and use u=sqrt(r/s) to get an arccos formula.
- Use case: Exercise 7.4.4; zero-set interval probabilities.
- Tags: zero-set, hitting-density, arccos

###### Cosh martingale for symmetric interval exit Laplace transforms

- ID: `exercise_method_ch7_cosh_martingale_exit_laplace`
- Kind: calculation-template
- Summary: Average the plus and minus exponential Brownian martingales to get e^{-lambda t} cosh(sqrt(2lambda) B_t), then stop at +/-a.
- Use case: Exercise 7.5.1; symmetric two-sided exit transform.
- Tags: cosh, exponential-martingale, exit-time

###### Drifted Brownian hitting via exponential martingale

- ID: `exercise_method_ch7_drift_hitting_exponential_martingale`
- Kind: calculation-template
- Summary: Choose theta solving theta^2/2 - b theta = lambda, stop exp(theta B_t - theta^2 t/2) at the linear boundary hitting time, and let the cutoff go to infinity.
- Use case: Exercise 7.5.2; Brownian motion with drift hitting a level.
- Tags: drift, hitting-time, exponential-martingale

###### Interval exit Laplace transforms from strong Markov linear equations

- ID: `exercise_method_ch7_interval_exit_laplace_linear_system`
- Kind: calculation-template
- Summary: Decompose one-sided hitting transforms by whether the interval exit occurs at a or b, then solve the two equations using exp(-sqrt(2lambda) distance).
- Use case: Exercise 7.5.3; killed Brownian exit transforms.
- Tags: strong-markov, laplace-transform, linear-system

###### Exit-moment comparison using Cauchy-Schwarz

- ID: `exercise_method_ch7_cauchy_schwarz_exit_moment_comparison`
- Kind: inequality-template
- Summary: Stop the fourth-degree Brownian polynomial martingale, then bound E(T B_T^2) by sqrt(E T^2) sqrt(E B_T^4).
- Use case: Exercise 7.5.4; nonsymmetric interval exit moments.
- Tags: cauchy-schwarz, exit-time, polynomial-martingale

###### Sixth-degree heat polynomial for third exit-time moment

- ID: `exercise_method_ch7_sixth_degree_exit_moment`
- Kind: calculation-template
- Summary: Solve u_t+u_xx/2=0 for x^6-c1 t x^4+c2 t^2 x^2-c3 t^3, stop at +/-a, and insert lower exit moments.
- Use case: Exercise 7.5.5; higher moments of symmetric Brownian exit times.
- Tags: polynomial-martingale, exit-time-moments, heat-equation

###### Exponential-square martingale plus maximal inequality

- ID: `exercise_method_ch7_exponential_square_maximal_borel_cantelli`
- Kind: proof-template
- Summary: Use (1+t)^(-1/2) exp(B_t^2/(2(1+t))) as a positive martingale, apply Doob over exponential time blocks, and sum probabilities.
- Use case: Exercise 7.5.6; almost-sure Brownian growth upper bounds.
- Tags: maximal-inequality, borel-cantelli, growth-bound

###### Ito drift test for f(B_t) martingales

- ID: `exercise_method_ch7_ito_affine_martingale_characterization`
- Kind: proof-template
- Summary: Ito's formula shows f(B_t) has drift (1/2)f''(B_t)dt; martingality forces the finite-variation drift to vanish, hence f''=0.
- Use case: Exercise 7.6.1; characterizing functions of Brownian motion that are martingales.
- Tags: ito-formula, martingale, affine

###### Cubic Brownian martingales from Ito formula

- ID: `exercise_method_ch7_cubic_ito_martingales`
- Kind: calculation-template
- Summary: Use u(t,x)=x^3-3tx for a time-space martingale, or apply Ito to x^3 and subtract the drift integral.
- Use case: Exercise 7.6.2; polynomial Brownian martingales.
- Tags: ito-formula, cubic, polynomial-martingale

###### Even Brownian moments by Ito recursion

- ID: `exercise_method_ch7_even_moment_ito_recursion`
- Kind: calculation-template
- Summary: Apply Ito to x^{2k}, take expectations, and solve beta_{2k}'(t)=k(2k-1) beta_{2k-2}(t) with beta_0=1.
- Use case: Exercise 7.6.3; deriving Gaussian even moments.
- Tags: moments, ito-formula, gaussian

###### Radial Brownian Ito formula and Bessel drift

- ID: `exercise_method_ch7_radial_ito_bessel_form`
- Kind: calculation-template
- Summary: Approximate |x| near 0, use gradient x/|x| and Laplacian (d-1)/|x| away from 0, and identify the radial martingale part.
- Use case: Exercise 7.6.4; radial Brownian motion and Bessel processes.
- Tags: radial-process, bessel, multidimensional-ito

###### Squared Brownian norm has dimension drift

- ID: `exercise_method_ch7_squared_norm_ito_dimension_drift`
- Kind: calculation-template
- Summary: Apply multidimensional Ito to |x|^2; the martingale part is 2 sum_i int B_s^i dB_s^i and the drift is d t.
- Use case: Exercise 7.6.5; computing E|B_t|^2 in R^d.
- Tags: multidimensional-ito, second-moment, dimension

## Chapter 8

### Durrett Chapter 8 LLM Viki: Applications to Random Walk

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter8.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

Exercise-derived records and method cards are also available in this folder:
`chapter8_exercise_records.jsonl`, `chapter8_exercise_method_cards.jsonl`,
`chapter8_exercise_new_knowledge.jsonl`, and `chapter8_exercise_viki.md`.

#### Section Guides

##### 8.1 Donsker's Theorem

- Goal: Use Skorokhod embedding to derive CLT, Donsker convergence, and random-walk path-functional limits.

- Must master: Skorokhod embedding, Brownian random clock, Donsker theorem, continuous mapping for path functionals, maxima and occupation examples

- Prelim angle: Most useful when a random-walk statistic can be rewritten as a Brownian functional in the limit.

##### 8.2 CLTs for Martingales

- Goal: Prove normal and functional limits for martingale arrays using conditional variances and Lindeberg controls.

- Must master: martingale embedding, conditional variance clock, martingale Lindeberg condition, martingale CLT

- Prelim angle: High-yield for dependent sums once the summands have conditional mean zero.

##### 8.3 CLTs for Stationary Sequences

- Goal: Reduce dependent stationary CLTs to martingale approximations, finite dependence, Markov-chain decompositions, or mixing estimates.

- Must master: martingale approximation, projective criteria, M-dependent variance, Poisson equation, mixing covariance bounds

- Prelim angle: A toolkit for deciding when dependence is weak enough for a normal limit and how to compute long-run variance.

##### 8.4 Empirical Distributions, Brownian Bridge

- Goal: Move from empirical CDF consistency to sqrt(n) empirical-process fluctuations and Brownian bridge limits.

- Must master: Glivenko-Cantelli, empirical process, Brownian bridge, Kolmogorov-Smirnov statistic, killed Brownian density method

- Prelim angle: Connects iid samples, CDF transforms, and Brownian bridge limits used in goodness-of-fit theory.

##### 8.5 Laws of the Iterated Logarithm

- Goal: Understand sharp almost-sure fluctuation scales for Brownian motion and iid random walks.

- Must master: Brownian LIL, iid LIL, Borel-Cantelli tail bounds, Strassen functional LIL

- Prelim angle: Use for questions about almost-sure limsup behavior rather than distributional limits.

#### Knowledge Pieces

##### Skorokhod embedding for one mean-zero variable

- ID: `durrett_ch8_skorokhod_embedding_mean_zero`

- Section: 8.1 Donsker's Theorem

- Kind: theorem

- Summary: If X has mean 0 and finite second moment, then Brownian motion can be stopped at a time T with B_T distributed as X and E T = E X^2.

- Proof idea: Represent the law of X as a mixture of two-point mean-zero laws, then use Brownian first exits from intervals (u,v).

- Exam use: Turns random-walk increments into Brownian increments with matching variance, making Brownian path results available for sums.

- Pitfall: The random interval used in the construction is external randomness; conditioning is what preserves the stopping-time calculations.

- Tags: skorokhod-embedding, brownian-motion, stopping-time, finite-variance

##### Embedding iid sums in Brownian motion

- ID: `durrett_ch8_embedded_random_walk`

- Section: 8.1 Donsker's Theorem

- Kind: construction

- Summary: For iid mean-zero variance-one increments, one can choose increasing stopping times T_n so that S_n has the same finite-dimensional law as B(T_n), with iid gaps T_n-T_{n-1}.

- Proof idea: Restart Brownian motion after each stopping time and apply the one-step Skorokhod embedding to each increment.

- Exam use: Useful for proving CLT and invariance principles by comparing S_n to Brownian motion at random times.

- Pitfall: The equality is in distribution for the embedded walk, not necessarily pathwise equality with a preexisting walk.

- Tags: random-walk, embedding, iid, brownian-scaling

##### Central limit theorem via random times

- ID: `durrett_ch8_clt_from_embedding`

- Section: 8.1 Donsker's Theorem

- Kind: proof-template

- Summary: Since S_n/sqrt(n) has the same law as B(T_n)/sqrt(n) and T_n/n converges in probability to 1, S_n/sqrt(n) converges to a standard normal variable.

- Proof idea: Use the weak law on the iid stopping-time gaps and Brownian continuity near time 1, then apply converging together.

- Exam use: A clean proof strategy when Brownian embedding is available and finite variance is assumed.

- Pitfall: One still needs tight control of B(t) near t=1; T_n/n -> 1 alone is not a distributional identity.

- Tags: clt, brownian-motion, converging-together, weak-law

##### Donsker invariance principle

- ID: `durrett_ch8_donsker_invariance_principle`

- Section: 8.1 Donsker's Theorem

- Kind: theorem

- Summary: The linearly interpolated process S(n t)/sqrt(n), built from iid mean-zero variance-one increments, converges weakly in C[0,1] to standard Brownian motion.

- Proof idea: Show the embedded Brownian time change is uniformly close to deterministic time on [0,1], then use uniform continuity of Brownian paths.

- Exam use: This is the main transfer principle from random walks to Brownian motion for maxima, hitting times, occupations, and path functionals.

- Pitfall: The topology matters: the statement is process-level weak convergence, not only convergence of each fixed time.

- Tags: donsker, invariance-principle, functional-clt, c0-1

##### Continuous functional transfer from Donsker

- ID: `durrett_ch8_continuous_functional_transfer`

- Section: 8.1 Donsker's Theorem

- Kind: theorem

- Summary: If a functional on C[0,1] is continuous at Brownian paths with probability one, then applying it to the rescaled random walk converges to applying it to Brownian motion.

- Proof idea: Combine Donsker's theorem with the continuous mapping theorem, allowing discontinuities on Brownian-null path sets.

- Exam use: The default method for deriving asymptotics of path statistics from random-walk convergence.

- Pitfall: Many natural functionals are not everywhere continuous; check Brownian almost-sure continuity rather than ordinary continuity only.

- Tags: continuous-mapping, path-functional, brownian-motion, donsker

##### Random-walk maximum limit

- ID: `durrett_ch8_maximum_functional`

- Section: 8.1 Donsker's Theorem

- Kind: example-pattern

- Summary: The normalized maximum max_{m<=n} S_m/sqrt(n) converges to max_{0<=t<=1} B_t, whose tail is 2 P(B_1 >= a).

- Proof idea: Apply Donsker to the continuous maximum functional and use the Brownian reflection principle for the distribution.

- Exam use: Recognize maximum and boundary-crossing limits as Brownian supremum problems.

- Pitfall: The reflection-principle tail formula is for a nonnegative barrier and Brownian motion starting at 0.

- Tags: maximum, reflection-principle, brownian-supremum, random-walk

##### Last zero before time n

- ID: `durrett_ch8_last_zero_arcsine`

- Section: 8.1 Donsker's Theorem

- Kind: example-pattern

- Summary: The last sign-change or zero time of a centered finite-variance walk, divided by n, converges to the Brownian last-zero time, which has the arcsine law.

- Proof idea: Show the last-zero functional is continuous at Brownian paths almost surely, then invoke Donsker.

- Exam use: Transfers the arcsine law beyond simple symmetric walks.

- Pitfall: The functional is discontinuous at some deterministic paths, so the Brownian null-set condition is the key point.

- Tags: arcsine-law, last-zero, donsker, brownian-zero-set

##### Occupation time of a half-line

- ID: `durrett_ch8_occupation_time_halfline`

- Section: 8.1 Donsker's Theorem

- Kind: example-pattern

- Summary: The fraction of times a centered finite-variance walk spends above a sqrt(n) threshold converges to the Brownian occupation time above that threshold.

- Proof idea: Apply Donsker to the occupation functional and use that Brownian paths spend zero Lebesgue time at any fixed level.

- Exam use: Use for random-walk occupation proportions and arcsine-type limits.

- Pitfall: Discrete-time counts require a small interpolation comparison; do not identify them blindly with continuous occupation time.

- Tags: occupation-time, arcsine-law, brownian-motion, invariance-principle

##### Embedding square-integrable martingales

- ID: `durrett_ch8_martingale_sk_embedding`

- Section: 8.2 CLTs for Martingales

- Kind: theorem

- Summary: A square-integrable martingale can be represented in distribution as Brownian motion sampled at increasing stopping times whose conditional expected increments match conditional variances.

- Proof idea: Embed each martingale difference conditionally using a Brownian first-exit construction after the previous stopping time.

- Exam use: Provides the Brownian-time-change route to martingale CLTs.

- Pitfall: The conditional variance process, not deterministic time, controls the Brownian clock.

- Tags: martingale, skorokhod-embedding, conditional-variance, brownian-motion

##### Martingale convergence from finite quadratic variation

- ID: `durrett_ch8_martingale_convergence_variance_sum`

- Section: 8.2 CLTs for Martingales

- Kind: theorem

- Summary: A square-integrable martingale with finite total conditional variance has an almost sure finite limit.

- Proof idea: Use L2 boundedness, Doob convergence ideas, and the sum of conditional second moments.

- Exam use: A standard way to separate negligible martingale tails from the main CLT-scale variance.

- Pitfall: Finite expected total variance is stronger than merely having bounded increments.

- Tags: martingale-convergence, quadratic-variation, l2

##### Martingale functional CLT by random clock

- ID: `durrett_ch8_martingale_fclt_random_clock`

- Section: 8.2 CLTs for Martingales

- Kind: theorem

- Summary: For a martingale-difference array, if the embedded Brownian clock converges to deterministic time and large jumps vanish, the interpolated martingale converges to Brownian motion.

- Proof idea: Use Skorokhod embedding, control the random time change, and prove the embedded path is close to Brownian motion.

- Exam use: The process-level version of the martingale CLT; use when partial-sum paths rather than only final sums appear.

- Pitfall: The theorem needs both variance-clock convergence and a Lindeberg-type no-large-jumps condition.

- Tags: martingale-fclt, random-clock, lindeberg, brownian-motion

##### Lindeberg-Feller condition for martingales

- ID: `durrett_ch8_martingale_lindeberg_feller`

- Section: 8.2 CLTs for Martingales

- Kind: theorem

- Summary: A martingale-difference array has a normal limit when its conditional variances converge to 1 and its conditional large-jump contribution vanishes.

- Proof idea: Truncate the array, embed the truncated martingale, and show the discarded part is negligible.

- Exam use: High-yield theorem for dependent CLTs where conditional means are zero.

- Pitfall: Ordinary variance convergence is not enough; the conditional variance process must stabilize.

- Tags: martingale-clt, lindeberg-condition, conditional-variance, triangular-array

##### Martingale central limit theorem

- ID: `durrett_ch8_martingale_clt_final_form`

- Section: 8.2 CLTs for Martingales

- Kind: theorem

- Summary: A martingale-difference sequence normalized by its variance has a normal limit under conditional variance convergence and conditional Lindeberg conditions.

- Proof idea: Reduce the sequence to a triangular array and apply the martingale Lindeberg-Feller theorem.

- Exam use: Use for sums of dependent variables after decomposing them into martingale differences.

- Pitfall: Verify the filtration and conditional mean-zero property before applying the theorem.

- Tags: martingale-clt, normal-limit, filtration, conditional-lindeberg

##### Stationary sequence CLT through martingale approximation

- ID: `durrett_ch8_stationary_coboundary_clt`

- Section: 8.3 CLTs for Stationary Sequences

- Kind: theorem

- Summary: For an ergodic stationary square-integrable sequence, a CLT can be proved when the partial sums are well approximated by a martingale with stationary differences.

- Proof idea: Decompose X_n into a martingale difference plus a small coboundary or negligible remainder, then apply the martingale CLT.

- Exam use: Main strategy for dependent stationary sequences on prelim-style problems.

- Pitfall: Ergodicity and square integrability do not by themselves guarantee a CLT; the approximation condition matters.

- Tags: stationary-sequence, martingale-approximation, ergodic, clt

##### Projective criterion for stationary CLT

- ID: `durrett_ch8_projective_stationary_clt`

- Section: 8.3 CLTs for Stationary Sequences

- Kind: criterion

- Summary: If conditional projections of future partial sums are summable or suitably controlled, stationary centered sequences satisfy a CLT with variance from the martingale approximation.

- Proof idea: Use conditional expectations relative to the natural filtration to build martingale differences and bound the error.

- Exam use: A practical check for dependent sequences where conditioning on the past becomes small.

- Pitfall: Do not replace the projective condition by ordinary covariance decay unless a theorem justifies it.

- Tags: projective-criterion, stationary, conditional-expectation, clt

##### M-dependent stationary CLT

- ID: `durrett_ch8_m_dependent_clt`

- Section: 8.3 CLTs for Stationary Sequences

- Kind: example-pattern

- Summary: For a centered stationary M-dependent sequence, the normalized sum has a normal limit with long-run variance sigma^2 = E X_0^2 + 2 sum_{k=1}^M E X_0 X_k.

- Proof idea: Group variables into blocks or use the stationary martingale approximation theorem; dependence disappears past lag M.

- Exam use: Fast recognition pattern for finite-range dependence problems.

- Pitfall: The limiting variance can be zero; in that case the usual nondegenerate normal limit collapses.

- Tags: m-dependent, stationary, long-run-variance, clt

##### Markov-chain CLT via Poisson equation

- ID: `durrett_ch8_markov_chain_poisson_equation_clt`

- Section: 8.3 CLTs for Stationary Sequences

- Kind: example-pattern

- Summary: For a stationary ergodic Markov chain, additive functionals can satisfy a CLT when f is represented through a solution of a Poisson equation, producing a martingale plus a telescoping error.

- Proof idea: Write f = g - P g plus a martingale increment, then show the boundary terms are negligible after sqrt(n) scaling.

- Exam use: Use when a dependent sum is generated by a Markov transition kernel.

- Pitfall: Stationarity or a controlled initial distribution is needed; starting far from equilibrium can add transient terms.

- Tags: markov-chain, poisson-equation, additive-functional, martingale-approximation

##### Moving-average process CLT

- ID: `durrett_ch8_moving_average_clt`

- Section: 8.3 CLTs for Stationary Sequences

- Kind: example-pattern

- Summary: Linear moving averages of iid innovations satisfy CLTs under coefficient conditions that make the process square integrable and approximable by finite-dependent truncations.

- Proof idea: Approximate the infinite moving average by an M-dependent one and control the L2 error of the remainder.

- Exam use: A standard dependent but explicit model where long-run variance can often be computed.

- Pitfall: Absolute or square summability assumptions on coefficients are not cosmetic; they justify truncation and variance formulas.

- Tags: moving-average, linear-process, m-dependent-approximation, clt

##### Mixing covariance inequality

- ID: `durrett_ch8_mixing_covariance_inequality`

- Section: 8.3.1 Mixing Properties

- Kind: lemma

- Summary: Mixing coefficients bound covariances between variables measurable with respect to separated sigma-fields, with Holder exponents controlling integrability.

- Proof idea: Approximate indicators and apply Holder-type bounds using the distance between joint and product probabilities.

- Exam use: Converts abstract mixing assumptions into summable covariance or projection bounds for CLTs.

- Pitfall: Check the exact mixing coefficient and exponent relation; different texts use different normalizations.

- Tags: mixing, covariance-bound, holder, dependence

##### Strong-mixing stationary CLT

- ID: `durrett_ch8_strong_mixing_stationary_clt`

- Section: 8.3.1 Mixing Properties

- Kind: theorem

- Summary: A centered ergodic stationary sequence satisfying suitable moment and summable mixing conditions obeys a CLT with long-run variance given by the covariance series.

- Proof idea: Use the mixing covariance inequality to verify the projective or martingale-approximation criterion.

- Exam use: Use for dependent sequences when decay of dependence is given quantitatively.

- Pitfall: Moment assumptions and summability rates are paired; weakening one often requires strengthening the other.

- Tags: strong-mixing, stationary-clt, long-run-variance, covariance-series

##### Glivenko-Cantelli theorem

- ID: `durrett_ch8_glivenko_cantelli_uniform`

- Section: 8.4 Empirical Distributions, Brownian Bridge

- Kind: theorem

- Summary: The empirical distribution function F_n converges uniformly almost surely to the true distribution function F.

- Proof idea: Reduce to the uniform distribution by the probability integral transform, then control finitely many grid intervals and use monotonicity.

- Exam use: The baseline consistency result for empirical CDFs before studying sqrt(n) fluctuations.

- Pitfall: Pointwise LLN is not enough; the theorem gives uniform convergence over all x.

- Tags: empirical-distribution, glivenko-cantelli, uniform-convergence, cdf

##### Empirical process convergence to Brownian bridge

- ID: `durrett_ch8_empirical_process_bridge`

- Section: 8.4 Empirical Distributions, Brownian Bridge

- Kind: theorem

- Summary: For uniform samples, sqrt(n)(F_n(t)-t) converges as a process to the Brownian bridge B_t - t B_1.

- Proof idea: Represent F_n through uniform order statistics or multinomial increments and apply Donsker with the endpoint pinned.

- Exam use: Foundation for Kolmogorov-Smirnov statistics and distribution-free empirical-process limits.

- Pitfall: The limit is a bridge, not free Brownian motion, because the empirical CDF is pinned at 0 and 1.

- Tags: empirical-process, brownian-bridge, donsker, uniform-order-statistics

##### Kolmogorov-Smirnov statistic limit

- ID: `durrett_ch8_kolmogorov_smirnov_limit`

- Section: 8.4 Empirical Distributions, Brownian Bridge

- Kind: theorem

- Summary: The statistic D_n = sqrt(n) sup_x |F_n(x)-F(x)| converges to sup_{0<=t<=1} |B_t - t B_1| for continuous F.

- Proof idea: Use the probability integral transform and the continuous mapping theorem applied to the empirical process.

- Exam use: Identifies the asymptotic null distribution of the Kolmogorov-Smirnov goodness-of-fit statistic.

- Pitfall: Continuity of F gives distribution-free uniformization; atoms require separate handling.

- Tags: kolmogorov-smirnov, brownian-bridge, empirical-cdf, supremum

##### Brownian bridge as pinned Brownian motion

- ID: `durrett_ch8_brownian_bridge_conditioning`

- Section: 8.4 Empirical Distributions, Brownian Bridge

- Kind: construction

- Summary: The Brownian bridge has the same law as B_t - t B_1 on [0,1], equivalently Brownian motion conditioned to return to 0 at time 1.

- Proof idea: Compute Gaussian means and covariances, or use Markov transition densities and conditioning on B_1=0.

- Exam use: Use to compute bridge covariance, Markov transition laws, and empirical-process limits.

- Pitfall: Conditioning on an event of probability zero is shorthand for a regular conditional or limiting density argument.

- Tags: brownian-bridge, gaussian-process, conditioning, empirical-process

##### Kolmogorov distribution by killed Brownian motion

- ID: `durrett_ch8_kolmogorov_distribution_method`

- Section: 8.4 Empirical Distributions, Brownian Bridge

- Kind: proof-template

- Summary: The distribution of sup |Brownian bridge| can be computed from Brownian motion killed on exiting an interval and then pinned at time 1.

- Proof idea: Use reflection or eigenfunction expansions for Brownian transition densities with absorbing barriers, then condition to form the bridge.

- Exam use: Useful when an exam asks not just for the KS limit but for its explicit distribution.

- Pitfall: Keep straight whether the boundary event is one-sided or two-sided; the formulas differ.

- Tags: kolmogorov-distribution, killed-brownian-motion, brownian-bridge, reflection-principle

##### Law of the iterated logarithm for Brownian motion

- ID: `durrett_ch8_brownian_lil`

- Section: 8.5 Laws of the Iterated Logarithm

- Kind: theorem

- Summary: Brownian motion satisfies limsup_{t->infty} B_t / sqrt(2 t log log t) = 1 almost surely, with the corresponding liminf equal to -1.

- Proof idea: Prove upper and lower bounds on a geometric time grid using Gaussian tails, Borel-Cantelli, and control between grid points.

- Exam use: The Brownian template for LILs of partial sums after embedding or invariance principles.

- Pitfall: The log log term is meaningful only in the eventual range where it is positive; constants are sharp.

- Tags: lil, brownian-motion, borel-cantelli, gaussian-tail

##### Law of the iterated logarithm for iid sums

- ID: `durrett_ch8_iid_lil`

- Section: 8.5 Laws of the Iterated Logarithm

- Kind: theorem

- Summary: For iid mean-zero finite-variance increments with variance sigma^2, limsup S_n / sqrt(2 sigma^2 n log log n) = 1 almost surely, and the liminf is -1.

- Proof idea: Embed the random walk in Brownian motion and show the random clock is close enough to n for Brownian LIL scaling.

- Exam use: Use when a problem asks for sharp almost-sure fluctuation size of partial sums.

- Pitfall: A CLT-scale heuristic is too small for limsup behavior; LIL has an extra sqrt(log log n) factor.

- Tags: lil, iid, random-walk, finite-variance

##### Strassen invariance principle

- ID: `durrett_ch8_strassen_invariance_principle`

- Section: 8.5 Laws of the Iterated Logarithm

- Kind: theorem

- Summary: The set of subsequential limit points of suitably LIL-rescaled partial-sum paths is the unit ball of absolutely continuous functions with square-integrable derivative.

- Proof idea: Use strong approximation ideas to transfer Brownian compact LIL behavior to partial sums.

- Exam use: A functional strengthening of the scalar LIL; it describes the whole path shape, not just limsup constants.

- Pitfall: The limit set is deterministic and compact in path space; it is not a single limiting process.

- Tags: strassen, functional-lil, invariance-principle, path-limit-set

### Chapter 8 Exercise Viki

#### Chapter 8 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter8/Chapter8Exercises.tex`
Source PDF: `Probability/Exercises/Chapter8/Chapter8Exercises.pdf`

This dataset turns the solved Chapter 8 exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.

##### Files

- `chapter8_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.
- `chapter8_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter8_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter8_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.
- `chapter8_exercise_viki.md`: human-readable overview.

##### Section Method Cards

###### 8.1 - Donsker embedding, random-walk path functionals, and Brownian transfer

Condition on the Skorokhod embedding interval for Brownian exit-time estimates; use Donsker plus continuous mapping for range, maximum, and occupation-type walk functionals.

Tags: donsker, skorokhod-embedding, brownian-exit-time, continuous-mapping, random-walk-range

###### 8.3 - Stationary sequence CLTs and martingale/coboundary approximation

Center the statistic, verify finite dependence or projective summability, compute long-run variance from covariances, and identify the martingale approximation term from the proof.

Tags: stationary-clt, m-dependent, long-run-variance, martingale-approximation, head-runs

###### 8.4 - Brownian bridge, empirical-process limits, and pinned Brownian calculations

Represent the bridge as Brownian motion pinned at time one; compute bridge probabilities by conditioning transition densities, and prove bridge Markov/martingale properties from its transition kernel.

Tags: brownian-bridge, pinned-brownian-motion, reflection-principle, transition-density, martingale

###### 8.5 - Laws of the iterated logarithm and Strassen limit sets

Use tail sums and Borel-Cantelli to show heavy-tailed jumps break LIL scaling; use continuous endpoint evaluation of Strassen's functional limit set for scalar limit points.

Tags: lil, borel-cantelli, heavy-tail, strassen, functional-lil

##### New Knowledge Pieces

###### Conditional exit-time moment transfer

- ID: `exercise_method_conditional_exit_time_moment_transfer`
- Kind: exercise-derived-method
- Summary: When a Skorokhod embedding is a mixture of Brownian exits from intervals, apply exit-time estimates conditionally on the random interval and then integrate over the mixing law.
- Use case: Exercise 8.1.1; transferring Exercise 7.5.4 bounds to the random time T_{U,V}.
- Tags: skorokhod-embedding, brownian-exit-time, conditioning, moment-bound

###### Random-walk range via Donsker

- ID: `exercise_method_random_walk_range_via_donsker`
- Kind: calculation-template
- Summary: For one-dimensional nearest-neighbor walks, visited sites form the interval between running min and max; divide by sqrt(n), apply Donsker to the continuous range functional, and drop the 1/sqrt(n) endpoint correction.
- Use case: Exercise 8.1.2 and random-walk range asymptotics.
- Tags: donsker, range, continuous-mapping, simple-random-walk

###### Head-run CLT variance from 1-dependence

- ID: `exercise_method_head_run_long_run_variance`
- Kind: calculation-template
- Summary: For indicators of the pattern HT in fair coin flips, center by mu=1/4 and compute long-run variance as Var(eta_0)+2 Cov(eta_0,eta_1)=1/16 because adjacent HT events are mutually exclusive.
- Use case: Exercise 8.3.1; finite-dependence stationary CLT computations.
- Tags: stationary-clt, m-dependent, long-run-variance, pattern-counting

###### Computing Gordin's Y0 in finite-dependence examples

- ID: `exercise_method_gordin_y0_computation`
- Kind: proof-template
- Summary: Use Y0=sum_j>=0(E(X_j|F_0)-E(X_j|F_{-1})); finite dependence kills all but finitely many terms, leaving explicit conditional expectations.
- Use case: Exercise 8.3.1 and martingale approximation examples.
- Tags: gordin, martingale-approximation, conditional-expectation, stationary-clt

###### One-sided Brownian bridge tail by conditioned reflection

- ID: `exercise_method_bridge_tail_conditioned_reflection`
- Kind: proof-template
- Summary: Compute P(max bridge > b) by viewing the bridge as Brownian motion conditioned on B_1=0 and using the reflected Brownian density on {T_b<1}.
- Use case: Exercise 8.4.1; bridge extrema and Kolmogorov-Smirnov limit calculations.
- Tags: brownian-bridge, reflection-principle, conditional-density, tail

###### Brownian bridge from time-changed Brownian motion

- ID: `exercise_method_bridge_time_change_covariance`
- Kind: construction
- Summary: To prove X_t=(1-t)B(t/(1-t)) is a bridge, show it is centered Gaussian with covariance s(1-t) for s<=t and continuous extension X_1=0.
- Use case: Exercise 8.4.2; recognizing Gaussian process identities.
- Tags: brownian-bridge, time-change, gaussian-process, covariance

###### Brownian bridge Markov kernel by density cancellation

- ID: `exercise_method_bridge_markov_kernel_cancellation`
- Kind: proof-template
- Summary: Write pinned finite-dimensional densities as products of Brownian transition densities ending at zero; divide joint densities so all pre-s factors cancel, leaving a kernel depending only on the present state.
- Use case: Exercise 8.4.3; proving Markov property for conditioned Gaussian processes.
- Tags: brownian-bridge, markov-property, transition-density, conditioning

###### Bridge divided by remaining time is a martingale

- ID: `exercise_method_bridge_remaining_time_martingale`
- Kind: proof-template
- Summary: Use E(B_t^0|B_s^0)=((1-t)/(1-s))B_s^0 to show B_t^0/(1-t) is a martingale; L2 norms grow like t/(1-t), so it is not L2 bounded.
- Use case: Exercise 8.4.4; bridge martingales and terminal singularity checks.
- Tags: brownian-bridge, martingale, l2-boundedness, transition-kernel

###### Heavy-tailed jumps obstruct LIL scaling

- ID: `exercise_method_heavy_tail_jump_obstruction_lil`
- Kind: proof-template
- Summary: If E|X|^alpha is infinite with alpha<2, tail sums at scale n^{1/alpha} diverge; Borel-Cantelli gives infinitely many huge increments, forcing adjacent partial sums above sqrt(n log log n) scale.
- Use case: Exercise 8.5.1 and necessity intuition for finite variance in LIL.
- Tags: lil, heavy-tail, borel-cantelli, large-jumps

###### Scalar LIL limit set from Strassen endpoint evaluation

- ID: `exercise_method_strassen_endpoint_limit_set`
- Kind: proof-template
- Summary: Apply the continuous map f -> f(1) to Strassen's compact LIL limit set; Cauchy-Schwarz bounds endpoints by [-1,1], and linear functions f(t)=at realize every endpoint.
- Use case: Exercise 8.5.2; deriving scalar limsup/limit-set results from functional LIL.
- Tags: strassen, functional-lil, endpoint-map, limit-set

## Chapter 9

### Durrett Chapter 9 LLM Viki: Multidimensional Brownian Motion

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter9.pdf`.

This unified Chapter 9 knowledge base includes textbook knowledge pieces plus exercise-derived method patterns from the solved Chapter 9 exercises.

Exercise source: `Probability/Exercises/Chapter9/Chapter9Exercises.tex` and `Probability/Exercises/Chapter9/Chapter9Exercises.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

#### Section Guides

##### 9.1 Martingales

- Goal: Use Ito's formula and optional stopping to compute multidimensional Brownian hitting probabilities and recurrence/transience facts.

- Must master: Ito-Laplacian martingale, radial harmonic functions, annulus hitting, d=2 recurrence, d>=3 transience

- Prelim angle: Most computations reduce to choosing the right harmonic function and stopping at sphere hitting times.

##### 9.2 Heat Equation

- Goal: Represent bounded heat-equation solutions as Brownian expectations and connect them to Gaussian kernels.

- Must master: backward martingale, heat kernel, initial continuity, smoothing

- Prelim angle: A standard way to turn PDE uniqueness and existence into a martingale argument.

##### 9.3 Inhomogeneous Heat Equation

- Goal: Handle source terms through Brownian occupation integrals.

- Must master: Duhamel formula, source-term martingale, Holder regularity

- Prelim angle: Recognize integral_0^t g(B_s) ds as the probabilistic form of a forcing term.

##### 9.4 Feynman-Kac Formula

- Goal: Use exponential weights to solve heat equations with multiplicative potentials.

- Must master: weighted martingale, sign convention, boundedness, Holder smoothness

- Prelim angle: Converts PDEs with c(x)u terms into expectations of exponential occupation functionals.

##### 9.5 Dirichlet Problem

- Goal: Represent harmonic boundary-value problems with Brownian exit distributions and understand boundary regularity.

- Must master: harmonic measure, regular boundary points, cone condition, Poisson kernels

- Prelim angle: Boundary behavior is often the hidden issue; regular points are the right probabilistic condition.

##### 9.6 Green's Functions and Potential Kernels

- Goal: Interpret Green functions as Brownian occupation densities.

- Must master: potential kernel, killed Green function, occupation density

- Prelim angle: Green functions make expected time spent in a set into an integral kernel calculation.

##### 9.7 Poisson's Equation

- Goal: Solve Poisson equations using occupation times and Green functions.

- Must master: Poisson representation, expected exit time, regular boundary zero condition, reflection/Kelvin formulas

- Prelim angle: Expected exit times and occupation times are usually Poisson-equation problems in disguise.

##### 9.8 Schrodinger Equation

- Goal: Solve elliptic equations with potentials using exponential weights and gauge integrability.

- Must master: weighted martingale, gauge function, finite-gauge theorem, interval eigenvalue threshold

- Prelim angle: The main exam trap is assuming exponential exit-time expectations are finite without checking the gauge.

#### Knowledge Pieces

##### Ito-Laplacian martingale for Brownian motion

- ID: `durrett_ch9_ito_laplacian_martingale`

- Section: 9.1 Martingales

- Kind: theorem

- Summary: If v is C2 and the stochastic integral is square-integrable, then v(B_t)-1/2 integral_0^t Delta v(B_s) ds is a continuous martingale.

- Proof idea: Apply Ito's formula to v(B_t); the drift is exactly 1/2 Delta v and the gradient term is a martingale.

- Exam use: The one-line engine behind harmonic functions, optional stopping, PDE uniqueness, and Green function computations.

- Pitfall: The integrability/localization condition is not decoration; without it the stochastic integral may only be local.

- Tags: brownian-motion, ito-formula, laplacian, martingale

##### Mean exit time from a ball

- ID: `durrett_ch9_exit_time_ball_mean`

- Section: 9.1 Martingales

- Kind: formula

- Summary: For d-dimensional Brownian motion started at |x|<R, the hitting time S_R of the sphere of radius R has E_x S_R=(R^2-|x|^2)/d.

- Proof idea: Stop the martingale |B_t|^2-dt at S_R wedge t and let t go to infinity.

- Exam use: Use for expected lifetime in balls and as a quick check for Poisson-equation solutions.

- Pitfall: The dimension appears in the denominator because |B_t|^2-dt is summed over d coordinates.

- Tags: exit-time, ball, optional-stopping

##### Radial harmonic test functions

- ID: `durrett_ch9_radial_harmonic_functions`

- Section: 9.1 Martingales

- Kind: formula

- Summary: The radial functions phi(x)=log|x| in d=2 and phi(x)=|x|^(2-d) in d>=3 are harmonic off the origin.

- Proof idea: Differentiate radial functions or use the radial Laplacian formula g''(r)+(d-1)g'(r)/r.

- Exam use: They convert annulus hitting probabilities into algebra.

- Pitfall: They are singular at zero, so stop before hitting the inner radius and localize with smooth compact modifications.

- Tags: harmonic, radial, annulus

##### Annulus hitting probability

- ID: `durrett_ch9_annulus_hitting_probability`

- Section: 9.1 Martingales

- Kind: formula

- Summary: For r<|x|<R, P_x(S_r<S_R)=[phi(R)-phi(x)]/[phi(R)-phi(r)], with phi radial harmonic as above.

- Proof idea: Optional stopping gives phi(x)=phi(r)P_x(S_r<S_R)+phi(R)P_x(S_R<S_r); solve the linear equation.

- Exam use: This is the standard computation for recurrence in d=2 and transience in d>=3.

- Pitfall: Use the correct dimension-specific phi; the logarithmic d=2 case is a frequent source of wrong powers.

- Tags: annulus, hitting-probability, recurrence, transience

##### Two-dimensional Brownian recurrence

- ID: `durrett_ch9_two_dimensional_recurrence`

- Section: 9.1 Martingales

- Kind: theorem

- Summary: In d=2, Brownian motion hits every circle around the origin almost surely and visits every nonempty open set infinitely often.

- Proof idea: In the annulus formula, fix r and let R go to infinity; the logarithmic ratio tends to one.

- Exam use: Use to decide whether planar Brownian motion returns to neighborhoods, not to exact points.

- Pitfall: Recurrence of neighborhoods does not mean hitting a prescribed point at positive time.

- Tags: dimension-two, recurrence, hitting

##### Points are polar in dimensions at least two

- ID: `durrett_ch9_points_polar_in_d_ge_2`

- Section: 9.1 Martingales

- Kind: fact

- Summary: For d>=2, Brownian motion does not hit a fixed point at a positive time, even when started from that point.

- Proof idea: In d=2, let the inner radius shrink to zero in the annulus formula; in higher dimensions reduce or compare by projection.

- Exam use: Prevents confusing recurrence in d=2 with point recurrence; important for punctured-domain examples.

- Pitfall: The definition of hitting zero uses t>0, so starting at zero is not a counterexample.

- Tags: polar-sets, hitting-points, dimension

##### Transience in dimensions at least three

- ID: `durrett_ch9_higher_dimensional_transience`

- Section: 9.1 Martingales

- Kind: theorem

- Summary: For d>=3, P_x(S_r<infinity)=(r/|x|)^(d-2) when |x|>r, and |B_t| tends to infinity almost surely.

- Proof idea: Let the outer radius go to infinity in the annulus formula, then use the strong Markov property over growing spheres.

- Exam use: Use whenever a problem asks whether Brownian motion returns to bounded sets in high dimension.

- Pitfall: The limit |B_t| to infinity is almost sure but does not imply monotone radial motion.

- Tags: transience, dimension-three, radial-process

##### Dvoretsky-Erdos lower envelope test

- ID: `durrett_ch9_dvoresky_erdos_test`

- Section: 9.1 Martingales

- Kind: theorem

- Summary: For d>=3 and positive decreasing g, P_0(|B_t|<=g(t)sqrt(t) infinitely often) is one or zero according as integral g(t)^(d-2) dt/t diverges or converges.

- Proof idea: This sharpens transience by testing repeated returns to shrinking multiples of sqrt(t).

- Exam use: Useful as a recognition result for Brownian escape rates in advanced prelim-style questions.

- Pitfall: It concerns infinitely often behavior near infinity, not fixed-time Gaussian tails.

- Tags: lower-envelope, transience, zero-one-law

##### Backward heat-equation martingale

- ID: `durrett_ch9_heat_backward_martingale`

- Section: 9.2 Heat Equation

- Kind: theorem

- Summary: If u_t=1/2 Delta u, then M_s=u(t-s,B_s) is a local martingale on 0<=s<=t.

- Proof idea: Apply Ito's formula to the space-time process (t-s,B_s); the time derivative cancels the Brownian drift.

- Exam use: This is the probabilistic uniqueness mechanism for the heat equation.

- Pitfall: The backward time t-s is essential; using t+s changes the sign.

- Tags: heat-equation, space-time, martingale

##### Heat equation solution by Brownian expectation

- ID: `durrett_ch9_heat_equation_solution`

- Section: 9.2 Heat Equation

- Kind: theorem

- Summary: The bounded solution with initial condition f is v(t,x)=E_x f(B_t), equivalently convolution with the Gaussian heat kernel.

- Proof idea: Boundedness makes the backward martingale uniformly integrable, so u(t,x)=E_x u(0,B_t).

- Exam use: Use to solve Cauchy heat problems and identify semigroup smoothing.

- Pitfall: Continuity at t=0 requires continuity of f; boundedness alone is not enough for the boundary condition.

- Tags: heat-kernel, brownian-semigroup, uniqueness

##### Gaussian heat kernel smoothing

- ID: `durrett_ch9_heat_kernel_smoothing`

- Section: 9.2 Heat Equation

- Kind: regularity

- Summary: For bounded continuous f, v(t,x)=integral (2 pi t)^(-d/2) exp(-|x-y|^2/(2t)) f(y) dy is C1,2 for t>0.

- Proof idea: Differentiate the Gaussian kernel under the integral for positive times.

- Exam use: Turns probabilistic representation into an actual classical solution.

- Pitfall: The smoothing is for t>0; behavior at t=0 is controlled by the initial data.

- Tags: regularity, heat-kernel, smoothing

##### Duhamel representation for inhomogeneous heat equation

- ID: `durrett_ch9_duhamel_inhomogeneous_heat`

- Section: 9.3 Inhomogeneous Heat Equation

- Kind: formula

- Summary: For u_t=1/2 Delta u+g with zero initial data, the bounded solution is v(t,x)=E_x integral_0^t g(B_s) ds.

- Proof idea: Ito's formula shows u(t-s,B_s)+integral_0^s g(B_r)dr is a local martingale; stop at s=t.

- Exam use: Use for heat equations with source terms and for occupation-time interpretations.

- Pitfall: With nonzero f, add the homogeneous solution E_x f(B_t).

- Tags: inhomogeneous-heat, duhamel, occupation-time

##### Holder source gives C1,2 inhomogeneous solution

- ID: `durrett_ch9_inhomogeneous_heat_regularity`

- Section: 9.3 Inhomogeneous Heat Equation

- Kind: regularity

- Summary: If g is Holder continuous, then v(t,x)=E_x integral_0^t g(B_s) ds is C1,2 and solves the inhomogeneous heat equation.

- Proof idea: Write v as integration of heat kernels against g and use parabolic regularity estimates.

- Exam use: A checklist item: representation plus Holder regularity gives a classical PDE solution.

- Pitfall: Continuity of g is natural, but Holder regularity is the clean sufficient condition used here.

- Tags: holder-continuity, regularity, inhomogeneous-heat

##### Feynman-Kac formula for the heat equation with potential

- ID: `durrett_ch9_feynman_kac_forward`

- Section: 9.4 Feynman-Kac Formula

- Kind: theorem

- Summary: For u_t=1/2 Delta u+c(x)u and initial f, the bounded solution is v(t,x)=E_x[f(B_t) exp(integral_0^t c(B_s)ds)].

- Proof idea: Use Ito plus the product rule on u(t-s,B_s) exp(integral_0^s c(B_r)dr); the drift cancels.

- Exam use: Use for heat equations with growth/decay potential and moment-generating questions for occupation integrals.

- Pitfall: Check the sign convention: the chapter's plus c u corresponds to exp(+ integral c).

- Tags: feynman-kac, potential, heat-equation

##### Feynman-Kac smoothness via reduction

- ID: `durrett_ch9_feynman_kac_smoothness`

- Section: 9.4 Feynman-Kac Formula

- Kind: proof-template

- Summary: If f and c are Holder continuous, the Feynman-Kac representation is C1,2 and solves the PDE.

- Proof idea: Split the representation into a heat part and an inhomogeneous heat part with source c(x)v(t,x).

- Exam use: Use when asked to justify that a probabilistic formula is a classical solution.

- Pitfall: Boundedness gives a representation; regularity needs additional assumptions.

- Tags: regularity, feynman-kac, holder-continuity

##### Dirichlet problem representation

- ID: `durrett_ch9_dirichlet_problem_representation`

- Section: 9.5 Dirichlet Problem

- Kind: theorem

- Summary: For a domain G with exit time tau, any bounded harmonic solution with boundary data f must be v(x)=E_x f(B_tau).

- Proof idea: Run u(B_t) until exit, use bounded martingale convergence, and identify the terminal boundary value.

- Exam use: The central Brownian representation for harmonic measure and boundary-value problems.

- Pitfall: The formula can fail to satisfy the boundary condition at irregular boundary points.

- Tags: dirichlet-problem, harmonic-measure, exit-time

##### Mean-value property implies harmonicity

- ID: `durrett_ch9_mean_value_harmonicity`

- Section: 9.5 Dirichlet Problem

- Kind: proof-template

- Summary: If v(x)=E_x v(B_tau_B) for every small ball B around x and v is C2, then Delta v(x)=0.

- Proof idea: Use Taylor expansion at x and the symmetry of the exit distribution from a ball.

- Exam use: Use to move from Brownian representations to Laplace's equation without stochastic calculus.

- Pitfall: The ball must be compactly contained in the domain.

- Tags: mean-value-property, harmonic, laplace-equation

##### Interior smoothness of Brownian harmonic functions

- ID: `durrett_ch9_interior_smoothness_harmonic`

- Section: 9.5 Dirichlet Problem

- Kind: regularity

- Summary: The Brownian Dirichlet solution v(x)=E_x f(B_tau) is C-infinity inside G.

- Proof idea: Inside a ball, v equals an average over the sphere with the smooth Poisson kernel, so differentiation is allowed.

- Exam use: Lets you assert interior classical harmonicity even with only bounded boundary data.

- Pitfall: Interior smoothness says nothing by itself about boundary continuity.

- Tags: harmonic-functions, smoothness, poisson-kernel

##### Regular boundary point

- ID: `durrett_ch9_regular_boundary_point`

- Section: 9.5 Dirichlet Problem

- Kind: definition

- Summary: A boundary point y is regular for G if Brownian motion started at y exits G immediately: P_y(tau=0)=1.

- Proof idea: Regularity is characterized probabilistically by immediate contact with the complement.

- Exam use: Use to decide where the Brownian Dirichlet solution attains the prescribed boundary value.

- Pitfall: A boundary point can be topologically present but probabilistically invisible.

- Tags: regular-boundary, dirichlet-problem, brownian-exit

##### Boundary continuity at regular points

- ID: `durrett_ch9_boundary_continuity_regular_points`

- Section: 9.5 Dirichlet Problem

- Kind: theorem

- Summary: If f is bounded continuous and y is a regular boundary point, then E_x f(B_tau) tends to f(y) as x in G tends to y.

- Proof idea: Lower semicontinuity of x -> P_x(tau<=t) plus Brownian path continuity forces exits near y with high probability.

- Exam use: This is the precise condition for the Dirichlet representation to satisfy the boundary data.

- Pitfall: Do not claim boundary convergence at every boundary point without checking regularity.

- Tags: boundary-continuity, regular-point, dirichlet-problem

##### Cone condition for regularity

- ID: `durrett_ch9_cone_condition`

- Section: 9.5 Dirichlet Problem

- Kind: criterion

- Summary: If the complement of G contains a cone with vertex y inside some small ball, then y is a regular boundary point.

- Proof idea: Brownian motion hits such exterior cones immediately enough to force tau=0 from the boundary.

- Exam use: A practical geometric sufficient condition for boundary regularity.

- Pitfall: It is sufficient, not necessary; failure of a cone condition does not automatically mean irregularity.

- Tags: cone-condition, regular-boundary, geometry

##### Punctured-domain boundary warning

- ID: `durrett_ch9_punctured_domain_warning`

- Section: 9.5 Dirichlet Problem

- Kind: example-pattern

- Summary: Thin removed sets can fail to influence Brownian exit, so a bounded harmonic representation may ignore assigned values on those sets.

- Proof idea: Use polarity of points or lines in higher dimensions to see that Brownian motion almost surely misses the thin set.

- Exam use: Explains why Dirichlet boundary data must be paired with regularity assumptions.

- Pitfall: A discontinuity of the probabilistic solution at an irregular point is not a contradiction of uniqueness inside G.

- Tags: irregular-boundary, polar-sets, examples

##### Half-space Poisson kernel

- ID: `durrett_ch9_half_space_poisson_kernel`

- Section: 9.5.1 Exit Distributions

- Kind: formula

- Summary: For the upper half-space H, the exit distribution on the boundary has density C_d y/(|x-theta|^2+y^2)^(d/2).

- Proof idea: Check the kernel is harmonic in H, normalizes to one, and approximates boundary data as y down to zero.

- Exam use: Use to compute Brownian exit distributions from a half-space; in d=2 it gives the Cauchy density.

- Pitfall: Track dimension conventions: the boundary variable theta lives in d-1 dimensions.

- Tags: poisson-kernel, half-space, exit-distribution

##### Unit-ball Poisson kernel

- ID: `durrett_ch9_ball_poisson_kernel`

- Section: 9.5.1 Exit Distributions

- Kind: formula

- Summary: For the unit ball D, E_x f(B_tau)=integral_{partial D} [(1-|x|^2)/|x-y|^d] f(y) pi(dy).

- Proof idea: Show the kernel is harmonic in x and reproduces the boundary data as x approaches regular boundary points.

- Exam use: Use to solve explicit Dirichlet problems in balls.

- Pitfall: The surface measure pi is normalized to be a probability measure in the chapter's formula.

- Tags: poisson-kernel, ball, harmonic-measure

##### Brownian potential kernel in R^d

- ID: `durrett_ch9_newtonian_potential_kernel`

- Section: 9.6 Green's Functions and Potential Kernels

- Kind: formula

- Summary: The expected occupation density of Brownian motion is the potential kernel G(x,y), proportional to |x-y|^(2-d) for d>=3 and to -log|x-y| in d=2 after domain adjustment.

- Proof idea: Integrate the Gaussian transition density over time and evaluate the resulting radial integral.

- Exam use: Use to turn occupation-time expectations into spatial integrals.

- Pitfall: In recurrent dimensions the full-space occupation integral can diverge, so constants and killed domains matter.

- Tags: green-function, potential-kernel, occupation-density

##### Killed-domain Green function

- ID: `durrett_ch9_green_function_killed_domain`

- Section: 9.6 Green's Functions and Potential Kernels

- Kind: definition

- Summary: For Brownian motion killed on leaving D, G_D(x,y) is the density satisfying E_x integral_0^tau f(B_t)dt = integral_D G_D(x,y)f(y)dy.

- Proof idea: Subtract the expected potential contributed after exit from the full-space potential.

- Exam use: The bridge between Brownian occupation times and Poisson's equation.

- Pitfall: The Green function depends on the domain and boundary killing, not only on |x-y|.

- Tags: green-function, killed-brownian-motion, occupation-time

##### Poisson equation representation

- ID: `durrett_ch9_poisson_equation_representation`

- Section: 9.7 Poisson's Equation

- Kind: theorem

- Summary: For 1/2 Delta u=-g in G with zero boundary data, any bounded solution must be v(x)=E_x integral_0^tau g(B_t)dt.

- Proof idea: The process u(B_t)+integral_0^t g(B_s)ds is a local martingale up to tau; stop and let t approach tau.

- Exam use: Use for expected occupation times, expected exit times, and source-term boundary problems.

- Pitfall: Sign conventions vary; here the PDE is 1/2 Delta u=-g for a positive occupation formula.

- Tags: poisson-equation, occupation-time, exit-time

##### Expected exit time solves Poisson's equation

- ID: `durrett_ch9_expected_exit_time_poisson`

- Section: 9.7 Poisson's Equation

- Kind: example-pattern

- Summary: Taking g=1 gives v(x)=E_x tau, which solves 1/2 Delta v=-1 in G with zero boundary values at regular points.

- Proof idea: This is the Poisson representation specialized to unit source.

- Exam use: A common prelim computation: guess radial v in a ball and verify by Laplacian and boundary values.

- Pitfall: Finite expectation needs domain control; unbounded domains may have infinite exit time.

- Tags: expected-exit-time, poisson-equation, radial-solution

##### Poisson solution vanishes at regular boundary points

- ID: `durrett_ch9_poisson_boundary_regular`

- Section: 9.7 Poisson's Equation

- Kind: theorem

- Summary: If G and g are bounded and y is a regular boundary point, then v(x)=E_x integral_0^tau g(B_t)dt tends to zero as x tends to y from inside G.

- Proof idea: Regularity makes tau small with high probability; boundedness controls the remaining tail.

- Exam use: Use to verify the zero boundary condition for occupation-time solutions.

- Pitfall: Regularity and boundedness assumptions are doing real work here.

- Tags: boundary-condition, poisson-equation, regular-point

##### Half-space Green function by reflection

- ID: `durrett_ch9_green_function_half_space`

- Section: 9.7.1 Occupation Times

- Kind: formula

- Summary: For the half-space, the killed Green function equals the full-space potential at y minus the full-space potential at the reflected point y_bar.

- Proof idea: Use the reflection principle/image method so the difference vanishes on the boundary.

- Exam use: Compute occupation times before exiting a half-space.

- Pitfall: The reflected term has the same singularity mirrored across the boundary, not at the original y.

- Tags: green-function, reflection-principle, half-space

##### Ball Green function by Kelvin transform

- ID: `durrett_ch9_green_function_ball_kelvin`

- Section: 9.7.1 Occupation Times

- Kind: formula

- Summary: For the unit ball in d>=3, G_D(x,y)=G(x,y)-|y|^(2-d)G(x,y/|y|^2); a logarithmic analog holds in d=2.

- Proof idea: The Kelvin-reflected singularity makes the boundary value cancel on |x|=1.

- Exam use: Use for explicit occupation densities in balls.

- Pitfall: The formula has a singular-looking y=0 case that must be handled by a limit or separately.

- Tags: green-function, unit-ball, kelvin-transform

##### Schrodinger boundary-value martingale

- ID: `durrett_ch9_schrodinger_martingale`

- Section: 9.8 Schrodinger Equation

- Kind: theorem

- Summary: For 1/2 Delta u+c(x)u=0 in G, u(B_t) exp(integral_0^t c(B_s)ds) is a local martingale up to the exit time.

- Proof idea: Apply Ito's formula and the product rule; the PDE cancels the drift after weighting by the exponential potential.

- Exam use: Foundation for boundary Feynman-Kac formulas and exponential exit-time moments.

- Pitfall: The sign of c controls integrability; positive c can make the expectation infinite.

- Tags: schrodinger-equation, feynman-kac, local-martingale

##### Positive potential can destroy bounded representation

- ID: `durrett_ch9_schrodinger_nonuniqueness_warning`

- Section: 9.8 Schrodinger Equation

- Kind: example-pattern

- Summary: For G=(-a,a), c=gamma>0, and boundary value 1, the ODE solution exists only away from eigenvalue obstructions and exponential exit moments can blow up.

- Proof idea: Solve 1/2 u''+gamma u=0 with boundary values and inspect zeros of cos(a sqrt(2 gamma)).

- Exam use: Use as a warning that Feynman-Kac with positive potential needs integrability assumptions.

- Pitfall: Bounded c does not automatically imply E_x exp(integral_0^tau c(B_s)ds) is finite.

- Tags: schrodinger-equation, eigenvalues, integrability

##### Gauge function for exponential lifetime integrability

- ID: `durrett_ch9_gauge_function`

- Section: 9.8 Schrodinger Equation

- Kind: definition

- Summary: The gauge w(x)=E_x exp(integral_0^tau c(B_s)ds) measures whether the Schrodinger Feynman-Kac representation is finite.

- Proof idea: Local exponential exit-time bounds plus a covering argument propagate finiteness through connected domains.

- Exam use: Check this before asserting uniqueness or boundary representations with exponential weights.

- Pitfall: Finiteness at one point and boundedness over the domain require separate hypotheses in the chapter.

- Tags: gauge, exponential-moment, schrodinger-equation

##### Small-set exponential exit bound

- ID: `durrett_ch9_small_set_exponential_exit_bound`

- Section: 9.8 Schrodinger Equation

- Kind: lemma

- Summary: For each theta>0, sufficiently small open sets H have uniformly bounded E_x exp(theta tau_H).

- Proof idea: Use occupation-time/tail bounds for Brownian exit from small-measure sets and sum the exponential series.

- Exam use: Technical tool that makes the gauge theorem work.

- Pitfall: Small Lebesgue measure is the key condition, not merely small diameter in the statement.

- Tags: exit-time, exponential-moment, small-set

##### Gauge finiteness propagates on connected domains

- ID: `durrett_ch9_gauge_theorem_connected_domain`

- Section: 9.8 Schrodinger Equation

- Kind: theorem

- Summary: If G is connected and the gauge w is not identically infinite, then w(x)<infinity for every x in G; if |G|<infinity, w is bounded.

- Proof idea: Local comparison across balls gives openness of the finite set, and connectedness plus small-set control gives closed propagation.

- Exam use: Use to justify uniform integrability in Schrodinger uniqueness proofs.

- Pitfall: Connectedness matters; separate components need separate checks.

- Tags: gauge-theorem, connected-domain, boundedness

##### Schrodinger Dirichlet representation

- ID: `durrett_ch9_schrodinger_dirichlet_representation`

- Section: 9.8 Schrodinger Equation

- Kind: theorem

- Summary: Under bounded connected domain, bounded continuous f and c, and finite gauge, the bounded solution is v(x)=E_x[f(B_tau) exp(integral_0^tau c(B_s)ds)].

- Proof idea: Stop the weighted martingale, use boundedness of the gauge for uniform integrability, and pass to the exit time.

- Exam use: Use for boundary-value problems with killing or creation potentials.

- Pitfall: Without the finite-gauge assumption, the formula may be infinite or uniqueness may fail.

- Tags: schrodinger-equation, dirichlet-problem, feynman-kac

##### Schrodinger boundary condition at regular points

- ID: `durrett_ch9_schrodinger_boundary_regular`

- Section: 9.8 Schrodinger Equation

- Kind: theorem

- Summary: At regular boundary points, the Schrodinger representation tends to the boundary value f(y).

- Proof idea: Split paths by small exit time and nearby exit location, then control the remaining event with bounded gauge.

- Exam use: Use to finish verification of boundary data for the weighted representation.

- Pitfall: The exponential weight adds a tail-control requirement absent from the plain Dirichlet problem.

- Tags: boundary-condition, regular-point, schrodinger-equation

##### Holder potential gives C2 Schrodinger solution

- ID: `durrett_ch9_schrodinger_smoothness`

- Section: 9.8 Schrodinger Equation

- Kind: regularity

- Summary: With the chapter's bounded-domain/gauge assumptions and Holder continuous c, the Schrodinger representation is C2 and solves 1/2 Delta v+c v=0.

- Proof idea: Reduce locally to Poisson-equation regularity with source c(x)v(x).

- Exam use: Use to upgrade the probabilistic representation to a classical solution.

- Pitfall: Smoothness is interior; boundary regularity is a separate issue.

- Tags: regularity, holder-continuity, schrodinger-equation

##### Exponential exit moment from an interval

- ID: `durrett_ch9_interval_exponential_exit_moment`

- Section: 9.8 Schrodinger Equation

- Kind: formula

- Summary: For tau exiting (-a,a), E_x exp(gamma tau)=cos(x sqrt(2 gamma))/cos(a sqrt(2 gamma)) when 0<gamma<pi^2/(8a^2), and is infinite at or above the threshold.

- Proof idea: Solve the ODE 1/2 u''+gamma u=0 with boundary value one and use the gauge/uniqueness result below the first eigenvalue.

- Exam use: A high-yield explicit computation connecting Brownian exit times with eigenvalues.

- Pitfall: The threshold is the first Dirichlet eigenvalue for the interval; at the threshold the denominator vanishes.

- Tags: exit-time, exponential-moment, eigenvalue, interval

##### Backward heat martingale template

- ID: `ch9_exercise_method_backward_heat_martingale_template`

- Section: 9.2 Exercises: Heat equation, Brownian semigroup, and heat-kernel smoothing

- Kind: exercise-pattern

- Summary: For u_t=(1/2)Delta u, apply Ito to u(t-s,B_s); the time derivative cancels the Brownian drift and leaves a local martingale.

- Proof idea: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Exam use: Section 9.2 martingale checks and any backward parabolic uniqueness argument.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: heat-equation, ito-formula, backward-time, martingale

- Source exercises: 9.2.A, 9.2.B, 9.2.C, 9.2.D

##### Bounded heat solution uniqueness by terminal martingale

- ID: `ch9_exercise_method_bounded_heat_uniqueness`

- Section: 9.2 Exercises: Heat equation, Brownian semigroup, and heat-kernel smoothing

- Kind: exercise-pattern

- Summary: Boundedness upgrades the backward local martingale to a uniformly integrable martingale; sending s up to t identifies u(t,x) with E_x f(B_t).

- Proof idea: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Exam use: Heat equation uniqueness and bounded parabolic Cauchy problems.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: heat-equation, uniqueness, uniform-integrability

- Source exercises: 9.2.A, 9.2.B, 9.2.C, 9.2.D

##### Gaussian approximate identity at t=0

- ID: `ch9_exercise_method_gaussian_approximate_identity`

- Section: 9.2 Exercises: Heat equation, Brownian semigroup, and heat-kernel smoothing

- Kind: exercise-pattern

- Summary: Write B_t as sqrt(t)Z; bounded convergence proves E f(x_n+sqrt(t_n)Z) tends to f(x) when f is bounded continuous.

- Proof idea: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Exam use: Initial-condition verification for heat and Feynman-Kac formulas.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: heat-kernel, initial-condition, bounded-convergence

- Source exercises: 9.2.A, 9.2.B, 9.2.C, 9.2.D

##### Heat-kernel derivative majorants

- ID: `ch9_exercise_method_heat_kernel_derivative_majorants`

- Section: 9.2 Exercises: Heat equation, Brownian semigroup, and heat-kernel smoothing

- Kind: exercise-pattern

- Summary: On t bounded away from zero, derivatives of the Gaussian kernel are polynomial times a Gaussian, giving integrable majorants for differentiating under the integral.

- Proof idea: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Exam use: Proving C^{1,2} smoothing for heat semigroups.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: heat-kernel, regularity, dominated-convergence

- Source exercises: 9.2.A, 9.2.B, 9.2.C, 9.2.D

##### Source-term martingale for inhomogeneous heat equations

- ID: `ch9_exercise_method_source_term_martingale`

- Section: 9.3 Exercises: Inhomogeneous heat equation and Duhamel occupation formulas

- Kind: exercise-pattern

- Summary: For u_t=(1/2)Delta u+g, add integral_0^s g(B_r)dr to u(t-s,B_s) so the drift cancels.

- Proof idea: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Exam use: Duhamel representation and source-term uniqueness.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: duhamel, source-term, martingale

- Source exercises: 9.3.A, 9.3.B, 9.3.C, 9.3.D, 9.3.E

##### Duhamel uniqueness from bounded martingales

- ID: `ch9_exercise_method_duhamel_uniqueness`

- Section: 9.3 Exercises: Inhomogeneous heat equation and Duhamel occupation formulas

- Kind: exercise-pattern

- Summary: A bounded inhomogeneous heat solution with zero initial data equals E_x integral_0^t g(B_s)ds by stopping the source-term martingale at s=t.

- Proof idea: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Exam use: Identifying source-forced heat solutions and occupation integrals.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: duhamel, uniqueness, occupation-integral

- Source exercises: 9.3.A, 9.3.B, 9.3.C, 9.3.D, 9.3.E

##### Short-time Markov-property PDE verification

- ID: `ch9_exercise_method_markov_property_pde_verification`

- Section: 9.3 Exercises: Inhomogeneous heat equation and Duhamel occupation formulas

- Kind: exercise-pattern

- Summary: Use v(t+h,x)=E_x[v(t,B_h)+short-time reward], Taylor expand v(t,B_h), divide by h, and let h down to zero.

- Proof idea: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Exam use: Showing smooth Brownian representations solve heat, Poisson, and Feynman-Kac PDEs.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: markov-property, taylor-expansion, pde-verification

- Source exercises: 9.3.A, 9.3.B, 9.3.C, 9.3.D, 9.3.E

##### Holder cancellation for singular heat-source kernels

- ID: `ch9_exercise_method_holder_cancels_kernel_singularity`

- Section: 9.3 Exercises: Inhomogeneous heat equation and Duhamel occupation formulas

- Kind: exercise-pattern

- Summary: Subtract g(x) inside P_s g(x)-g(x); Holder continuity gives O(s^{alpha/2}), offsetting the small-time singularity.

- Proof idea: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Exam use: Regularity of inhomogeneous heat and potential-kernel formulas.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: holder-continuity, regularity, singular-kernel

- Source exercises: 9.3.A, 9.3.B, 9.3.C, 9.3.D, 9.3.E

##### Exponential potential weight martingale

- ID: `ch9_exercise_method_exponential_weight_martingale`

- Section: 9.4 Exercises: Feynman-Kac formula for heat equations with potentials

- Kind: exercise-pattern

- Summary: Multiply by exp(integral c(B_s)ds); the finite-variation product rule adds exactly the c u drift needed for cancellation.

- Proof idea: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Exam use: Feynman-Kac and Schrodinger martingale derivations.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: feynman-kac, exponential-weight, martingale

- Source exercises: 9.4.A, 9.4.B, 9.4.C, 9.4.D, 9.4.E

##### Bounded Feynman-Kac uniqueness

- ID: `ch9_exercise_method_feynman_kac_bounded_uniqueness`

- Section: 9.4 Exercises: Feynman-Kac formula for heat equations with potentials

- Kind: exercise-pattern

- Summary: If c and u are bounded on finite time intervals, the weighted martingale is bounded; stopping at t gives u(t,x)=E_x[f(B_t)exp(integral_0^t c(B_s)ds)].

- Proof idea: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Exam use: Parabolic PDEs with bounded multiplicative potentials.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: feynman-kac, boundedness, uniqueness

- Source exercises: 9.4.A, 9.4.B, 9.4.C, 9.4.D, 9.4.E

##### Smooth Feynman-Kac short-time check

- ID: `ch9_exercise_method_smooth_feynman_kac_short_time_check`

- Section: 9.4 Exercises: Feynman-Kac formula for heat equations with potentials

- Kind: exercise-pattern

- Summary: Use v(t+h,x)=E_x[e^{int_0^h c(B_s)ds}v(t,B_h)], then expand the Brownian move and the exponential to get v_t=(1/2)Delta v+c v.

- Proof idea: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Exam use: Verifying smooth Feynman-Kac representations solve the PDE.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: feynman-kac, short-time, pde-verification

- Source exercises: 9.4.A, 9.4.B, 9.4.C, 9.4.D, 9.4.E

##### Feynman-Kac smoothness by Duhamel reduction

- ID: `ch9_exercise_method_feynman_kac_duhamel_reduction`

- Section: 9.4 Exercises: Feynman-Kac formula for heat equations with potentials

- Kind: exercise-pattern

- Summary: Use e^{A_t}-1=integral_0^t c(B_s)e^{A_t-A_s}ds to decompose v into a heat solution plus an inhomogeneous heat solution with source c v.

- Proof idea: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Exam use: Regularity proofs for Feynman-Kac formulas with Holder f and c.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: feynman-kac, duhamel, regularity

- Source exercises: 9.4.A, 9.4.B, 9.4.C, 9.4.D, 9.4.E

##### Liouville theorem via heat semigroup flattening

- ID: `ch9_exercise_method_heat_semigroup_liouville`

- Section: 9.5 Exercises: Dirichlet problem, Liouville principles, and boundary regularity

- Kind: exercise-pattern

- Summary: A bounded harmonic h satisfies h(x)=E h(x+B_t); as t grows, two Gaussian laws with fixed mean separation have vanishing total variation distance, so h(x)=h(y).

- Proof idea: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Exam use: Bounded harmonic functions on all of R^d.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: liouville, harmonic-functions, heat-semigroup

- Source exercises: 9.5.1, 9.5.2, 9.5.3, 9.5.4, 9.5.5

##### Recurrent Brownian motion forces nonnegative superharmonic functions constant

- ID: `ch9_exercise_method_recurrent_superharmonic_constancy`

- Section: 9.5 Exercises: Dirichlet problem, Liouville principles, and boundary regularity

- Kind: exercise-pattern

- Summary: Nonnegative superharmonic functions yield supermartingales; in d=1,2 Brownian motion hits every small neighborhood, so optional stopping gives f(x)>=f(y) and symmetry gives equality.

- Proof idea: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Exam use: Superharmonic Liouville-type exercises in recurrent dimensions.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: superharmonic, recurrence, optional-stopping

- Source exercises: 9.5.1, 9.5.2, 9.5.3, 9.5.4, 9.5.5

##### Radial superharmonic examples in high dimension

- ID: `ch9_exercise_method_radial_superharmonic_high_dimension`

- Section: 9.5 Exercises: Dirichlet problem, Liouville principles, and boundary regularity

- Kind: example-pattern

- Summary: Use the radial Laplacian g''(r)+(d-1)g'(r)/r; functions such as (1+r^2)^{-(d-2)/2} are smooth nonconstant nonnegative superharmonic for d>=3.

- Proof idea: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Exam use: Constructing counterexamples to recurrent-dimensional constancy in transient dimensions.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: radial-laplacian, superharmonic, dimension

- Source exercises: 9.5.1, 9.5.2, 9.5.3, 9.5.4, 9.5.5

##### Escape probability is the nonuniqueness direction

- ID: `ch9_exercise_method_escape_probability_nonuniqueness`

- Section: 9.5 Exercises: Dirichlet problem, Liouville principles, and boundary regularity

- Kind: exercise-pattern

- Summary: When Brownian motion can avoid exiting G, q(x)=P_x(tau=infinity) is a bounded zero-boundary harmonic function; all bounded zero-boundary solutions differ by c q.

- Proof idea: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Exam use: Dirichlet problems in domains where exit is not almost sure.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: dirichlet-problem, nonuniqueness, escape-probability

- Source exercises: 9.5.1, 9.5.2, 9.5.3, 9.5.4, 9.5.5

##### Flat cone boundary regularity

- ID: `ch9_exercise_method_flat_cone_regular_boundary`

- Section: 9.5 Exercises: Dirichlet problem, Liouville principles, and boundary regularity

- Kind: exercise-pattern

- Summary: Use zeros of the perpendicular Brownian coordinate and the induced Cauchy trace on the hyperplane to show Brownian motion immediately hits a flat exterior cone.

- Proof idea: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Exam use: Checking regular boundary points under weaker geometric exterior conditions.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: regular-boundary, cone-condition, brownian-trace

- Source exercises: 9.5.1, 9.5.2, 9.5.3, 9.5.4, 9.5.5

##### Infinite ball occupation in recurrent dimensions

- ID: `ch9_exercise_method_recurrent_ball_occupation_infinite`

- Section: 9.6 Exercises: Green functions, occupation densities, and potential-kernel normalization

- Kind: exercise-pattern

- Summary: Use recurrence to get infinitely many returns to a ball and the strong Markov property to sum positive occupation increments.

- Proof idea: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Exam use: Occupation-time dichotomy for Brownian motion in d<=2.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: occupation-time, recurrence, strong-markov-property

- Source exercises: 9.6.A, 9.6.B, 9.6.C, 9.6.D, 9.6.E

##### Gamma change of variables for transient potential kernels

- ID: `ch9_exercise_method_transient_potential_kernel_gamma`

- Section: 9.6 Exercises: Green functions, occupation densities, and potential-kernel normalization

- Kind: exercise-pattern

- Summary: For d>=3, integrate the heat kernel over time and use s=|x-y|^2/(2t) to get Gamma(d/2-1)/(2 pi^{d/2}) |x-y|^{2-d}.

- Proof idea: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Exam use: Green-function and expected occupation-density calculations.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: potential-kernel, gamma-function, transience

- Source exercises: 9.6.A, 9.6.B, 9.6.C, 9.6.D, 9.6.E

##### Modified potential kernels in recurrent dimensions

- ID: `ch9_exercise_method_recurrent_modified_potential_kernel`

- Section: 9.6 Exercises: Green functions, occupation densities, and potential-kernel normalization

- Kind: exercise-pattern

- Summary: Subtract a reference heat kernel before integrating over time; in d=1 this gives -|x-y| and in d=2 gives -(1/pi)log|x-y|.

- Proof idea: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Exam use: Using potential kernels when the full-space occupation integral diverges.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: potential-kernel, recurrent-dimensions, renormalization

- Source exercises: 9.6.A, 9.6.B, 9.6.C, 9.6.D, 9.6.E

##### Frullani integral for the two-dimensional log kernel

- ID: `ch9_exercise_method_frullani_log_kernel`

- Section: 9.6 Exercises: Green functions, occupation densities, and potential-kernel normalization

- Kind: exercise-pattern

- Summary: After u=1/(2t), the difference of two planar heat kernels becomes integral_0^infty (e^{-a^2u}-e^{-u})du/u=-2log a.

- Proof idea: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Exam use: Deriving the d=2 logarithmic potential kernel.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: frullani, log-kernel, dimension-two

- Source exercises: 9.6.A, 9.6.B, 9.6.C, 9.6.D, 9.6.E

##### Distributional delta normalization of Green kernels

- ID: `ch9_exercise_method_distributional_delta_normalization`

- Section: 9.6 Exercises: Green functions, occupation densities, and potential-kernel normalization

- Kind: exercise-pattern

- Summary: Integrate by parts outside a small ball and let the radius shrink; the boundary flux fixes the constant so (1/2)Delta G=-delta_0.

- Proof idea: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Exam use: Checking Green-function constants and fundamental solutions.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: distributional-laplacian, green-function, flux

- Source exercises: 9.6.A, 9.6.B, 9.6.C, 9.6.D, 9.6.E

##### Exit-time moment recursion

- ID: `ch9_exercise_method_exit_time_moment_recursion`

- Section: 9.7 Exercises: Poisson equation and exit-time moment recursions

- Kind: exercise-pattern

- Summary: For m_n(x)=E_x tau^n, the Markov property or Dynkin formula gives (1/2)Delta m_n=-n m_{n-1} with zero boundary values.

- Proof idea: Identify exit-time moments by applying the Poisson representation recursively: the nth moment solves a Poisson equation with source n times the previous moment.

- Exam use: Computing higher moments of Brownian exit times.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: exit-time, moment-recursion, poisson-equation

- Source exercises: 9.7.1

##### Second exit-time moment Poisson system

- ID: `ch9_exercise_method_second_moment_poisson_system`

- Section: 9.7 Exercises: Poisson equation and exit-time moment recursions

- Kind: exercise-pattern

- Summary: First solve (1/2)Delta v=-1 for v=E tau; then solve (1/2)Delta w=-2v for w=E tau^2, both with zero boundary values.

- Proof idea: Identify exit-time moments by applying the Poisson representation recursively: the nth moment solves a Poisson equation with source n times the previous moment.

- Exam use: Exercise 9.7.1 and second-moment exit-time computations.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: exit-time, second-moment, poisson-equation

- Source exercises: 9.7.1

##### Schrodinger weighted martingale

- ID: `ch9_exercise_method_schrodinger_weighted_martingale`

- Section: 9.8 Exercises: Schrodinger equation, gauge integrability, and exponential exit moments

- Kind: exercise-pattern

- Summary: For (1/2)Delta u+c u=0, Ito plus the finite-variation product rule makes u(B_t)exp(integral_0^t c(B_s)ds) a local martingale before exit.

- Proof idea: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Exam use: Boundary Feynman-Kac formulas for elliptic equations with potential.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: schrodinger-equation, feynman-kac, martingale

- Source exercises: 9.8.A, 9.8.B, 9.8.C, 9.8.D, 9.8.E, 9.8.F

##### Gauge integrability condition

- ID: `ch9_exercise_method_gauge_integrability_condition`

- Section: 9.8 Exercises: Schrodinger equation, gauge integrability, and exponential exit moments

- Kind: criterion

- Summary: Before applying boundary Feynman-Kac with positive potential, check w(x)=E_x exp(integral_0^tau c(B_s)ds); bounded c alone does not ensure finiteness.

- Proof idea: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Exam use: Avoiding false Schrodinger Feynman-Kac representations.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: gauge, integrability, positive-potential

- Source exercises: 9.8.A, 9.8.B, 9.8.C, 9.8.D, 9.8.E, 9.8.F

##### Interval eigenvalue threshold for exponential exit times

- ID: `ch9_exercise_method_interval_eigenvalue_threshold`

- Section: 9.8 Exercises: Schrodinger equation, gauge integrability, and exponential exit moments

- Kind: exercise-pattern

- Summary: For tau exiting (-a,a), solve (1/2)u''+gamma u=0 with boundary value one; finiteness holds exactly below gamma=pi^2/(8a^2).

- Proof idea: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Exam use: Explicit exponential exit-time moments and gauge blow-up examples.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: exit-time, eigenvalue, interval

- Source exercises: 9.8.A, 9.8.B, 9.8.C, 9.8.D, 9.8.E, 9.8.F

##### Finite-gauge boundary Feynman-Kac uniqueness

- ID: `ch9_exercise_method_finite_gauge_boundary_feynman_kac`

- Section: 9.8 Exercises: Schrodinger equation, gauge integrability, and exponential exit moments

- Kind: exercise-pattern

- Summary: Finite bounded gauge controls the terminal exponential weight and kills the tail term, giving u(x)=E_x[f(B_tau)exp(integral_0^tau c(B_s)ds)].

- Proof idea: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Exam use: Uniqueness of bounded Schrodinger Dirichlet solutions.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: finite-gauge, dirichlet-problem, feynman-kac

- Source exercises: 9.8.A, 9.8.B, 9.8.C, 9.8.D, 9.8.E, 9.8.F

##### Local exit expansion for smooth Schrodinger representations

- ID: `ch9_exercise_method_smooth_schrodinger_local_exit_expansion`

- Section: 9.8 Exercises: Schrodinger equation, gauge integrability, and exponential exit moments

- Kind: exercise-pattern

- Summary: Stop at a small ball, expand v(B_sigma) and exp(integral_0^sigma c(B_s)ds), then divide by E sigma to get (1/2)Delta v+c v=0.

- Proof idea: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Exam use: Verifying smooth Schrodinger Feynman-Kac formulas solve the PDE.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: schrodinger-equation, local-exit, taylor-expansion

- Source exercises: 9.8.A, 9.8.B, 9.8.C, 9.8.D, 9.8.E, 9.8.F

#### Exercise Method Cards

##### 9.2 Heat equation, Brownian semigroup, and heat-kernel smoothing

- ID: `durrett_ch9_section_9_2_method_card`

- Method: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- New knowledge IDs: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

##### 9.3 Inhomogeneous heat equation and Duhamel occupation formulas

- ID: `durrett_ch9_section_9_3_method_card`

- Method: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Tags: duhamel, source-term, occupation-integral, holder-regularity

- New knowledge IDs: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

##### 9.4 Feynman-Kac formula for heat equations with potentials

- ID: `durrett_ch9_section_9_4_method_card`

- Method: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Tags: feynman-kac, exponential-weight, potential, regularity-reduction

- New knowledge IDs: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

##### 9.5 Dirichlet problem, Liouville principles, and boundary regularity

- ID: `durrett_ch9_section_9_5_method_card`

- Method: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- New knowledge IDs: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

##### 9.6 Green functions, occupation densities, and potential-kernel normalization

- ID: `durrett_ch9_section_9_6_method_card`

- Method: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- New knowledge IDs: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

##### 9.7 Poisson equation and exit-time moment recursions

- ID: `durrett_ch9_section_9_7_method_card`

- Method: Identify exit-time moments by applying the Poisson representation recursively: the nth moment solves a Poisson equation with source n times the previous moment.

- Tags: poisson-equation, exit-time-moments, moment-recursion

- New knowledge IDs: ch9_exercise_method_exit_time_moment_recursion, ch9_exercise_method_second_moment_poisson_system

##### 9.8 Schrodinger equation, gauge integrability, and exponential exit moments

- ID: `durrett_ch9_section_9_8_method_card`

- Method: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- New knowledge IDs: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

#### Exercise Record Index

##### 9.2 Heat equation, Brownian semigroup, and heat-kernel smoothing

- Exercise 9.2.A: method tags `heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness`; knowledge used `durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants`.
- Exercise 9.2.B: method tags `heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness`; knowledge used `durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants`.
- Exercise 9.2.C: method tags `heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness`; knowledge used `durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants`.
- Exercise 9.2.D: method tags `heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness`; knowledge used `durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants`.

##### 9.3 Inhomogeneous heat equation and Duhamel occupation formulas

- Exercise 9.3.A: method tags `duhamel, source-term, occupation-integral, holder-regularity`; knowledge used `durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity`.
- Exercise 9.3.B: method tags `duhamel, source-term, occupation-integral, holder-regularity`; knowledge used `durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity`.
- Exercise 9.3.C: method tags `duhamel, source-term, occupation-integral, holder-regularity`; knowledge used `durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity`.
- Exercise 9.3.D: method tags `duhamel, source-term, occupation-integral, holder-regularity`; knowledge used `durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity`.
- Exercise 9.3.E: method tags `duhamel, source-term, occupation-integral, holder-regularity`; knowledge used `durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity`.

##### 9.4 Feynman-Kac formula for heat equations with potentials

- Exercise 9.4.A: method tags `feynman-kac, exponential-weight, potential, regularity-reduction`; knowledge used `durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat`; new knowledge `ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction`.
- Exercise 9.4.B: method tags `feynman-kac, exponential-weight, potential, regularity-reduction`; knowledge used `durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat`; new knowledge `ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction`.
- Exercise 9.4.C: method tags `feynman-kac, exponential-weight, potential, regularity-reduction`; knowledge used `durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat`; new knowledge `ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction`.
- Exercise 9.4.D: method tags `feynman-kac, exponential-weight, potential, regularity-reduction`; knowledge used `durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat`; new knowledge `ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction`.
- Exercise 9.4.E: method tags `feynman-kac, exponential-weight, potential, regularity-reduction`; knowledge used `durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat`; new knowledge `ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction`.

##### 9.5 Dirichlet problem, Liouville principles, and boundary regularity

- Exercise 9.5.1: method tags `dirichlet-problem, harmonic-functions, regular-boundary, escape-probability`; knowledge used `durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition`; new knowledge `ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary`.
- Exercise 9.5.2: method tags `dirichlet-problem, harmonic-functions, regular-boundary, escape-probability`; knowledge used `durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition`; new knowledge `ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary`.
- Exercise 9.5.3: method tags `dirichlet-problem, harmonic-functions, regular-boundary, escape-probability`; knowledge used `durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition`; new knowledge `ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary`.
- Exercise 9.5.4: method tags `dirichlet-problem, harmonic-functions, regular-boundary, escape-probability`; knowledge used `durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition`; new knowledge `ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary`.
- Exercise 9.5.5: method tags `dirichlet-problem, harmonic-functions, regular-boundary, escape-probability`; knowledge used `durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition`; new knowledge `ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary`.

##### 9.6 Green functions, occupation densities, and potential-kernel normalization

- Exercise 9.6.A: method tags `green-function, potential-kernel, occupation-time, distributional-laplacian`; knowledge used `durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions`; new knowledge `ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization`.
- Exercise 9.6.B: method tags `green-function, potential-kernel, occupation-time, distributional-laplacian`; knowledge used `durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions`; new knowledge `ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization`.
- Exercise 9.6.C: method tags `green-function, potential-kernel, occupation-time, distributional-laplacian`; knowledge used `durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions`; new knowledge `ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization`.
- Exercise 9.6.D: method tags `green-function, potential-kernel, occupation-time, distributional-laplacian`; knowledge used `durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions`; new knowledge `ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization`.
- Exercise 9.6.E: method tags `green-function, potential-kernel, occupation-time, distributional-laplacian`; knowledge used `durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions`; new knowledge `ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization`.

##### 9.7 Poisson equation and exit-time moment recursions

- Exercise 9.7.1: method tags `poisson-equation, exit-time-moments, moment-recursion`; knowledge used `durrett_ch9_poisson_equation_representation, durrett_ch9_expected_exit_time_poisson, durrett_ch9_poisson_boundary_regular`; new knowledge `ch9_exercise_method_exit_time_moment_recursion, ch9_exercise_method_second_moment_poisson_system`.

##### 9.8 Schrodinger equation, gauge integrability, and exponential exit moments

- Exercise 9.8.A: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.
- Exercise 9.8.B: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.
- Exercise 9.8.C: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.
- Exercise 9.8.D: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.
- Exercise 9.8.E: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.
- Exercise 9.8.F: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.

### Chapter 9 Exercise Viki

#### Durrett Chapter 9 Exercise LLM Viki

Source: `Probability/Exercises/Chapter9/Chapter9Exercises.tex` and compiled PDF.

These records are derived from the solved Chapter 9 exercises and verification tasks, with reusable method patterns for LLM retrieval.

##### Method Cards

###### 9.2 Heat equation, Brownian semigroup, and heat-kernel smoothing

- ID: `durrett_ch9_section_9_2_method_card`

- Method: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- Knowledge used: durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing

- Exercise-derived knowledge: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

###### 9.3 Inhomogeneous heat equation and Duhamel occupation formulas

- ID: `durrett_ch9_section_9_3_method_card`

- Method: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- Exercise-derived knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

###### 9.4 Feynman-Kac formula for heat equations with potentials

- ID: `durrett_ch9_section_9_4_method_card`

- Method: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- Exercise-derived knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

###### 9.5 Dirichlet problem, Liouville principles, and boundary regularity

- ID: `durrett_ch9_section_9_5_method_card`

- Method: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- Exercise-derived knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

###### 9.6 Green functions, occupation densities, and potential-kernel normalization

- ID: `durrett_ch9_section_9_6_method_card`

- Method: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- Exercise-derived knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

###### 9.7 Poisson equation and exit-time moment recursions

- ID: `durrett_ch9_section_9_7_method_card`

- Method: Identify exit-time moments by applying the Poisson representation recursively: the nth moment solves a Poisson equation with source n times the previous moment.

- Tags: poisson-equation, exit-time-moments, moment-recursion

- Knowledge used: durrett_ch9_poisson_equation_representation, durrett_ch9_expected_exit_time_poisson, durrett_ch9_poisson_boundary_regular

- Exercise-derived knowledge: ch9_exercise_method_exit_time_moment_recursion, ch9_exercise_method_second_moment_poisson_system

###### 9.8 Schrodinger equation, gauge integrability, and exponential exit moments

- ID: `durrett_ch9_section_9_8_method_card`

- Method: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- Exercise-derived knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

##### New Knowledge

###### Backward heat martingale template

- ID: `ch9_exercise_method_backward_heat_martingale_template`

- Kind: proof-template

- Summary: For u_t=(1/2)Delta u, apply Ito to u(t-s,B_s); the time derivative cancels the Brownian drift and leaves a local martingale.

- Use case: Section 9.2 martingale checks and any backward parabolic uniqueness argument.

- Tags: heat-equation, ito-formula, backward-time, martingale

###### Bounded heat solution uniqueness by terminal martingale

- ID: `ch9_exercise_method_bounded_heat_uniqueness`

- Kind: proof-template

- Summary: Boundedness upgrades the backward local martingale to a uniformly integrable martingale; sending s up to t identifies u(t,x) with E_x f(B_t).

- Use case: Heat equation uniqueness and bounded parabolic Cauchy problems.

- Tags: heat-equation, uniqueness, uniform-integrability

###### Gaussian approximate identity at t=0

- ID: `ch9_exercise_method_gaussian_approximate_identity`

- Kind: calculation-template

- Summary: Write B_t as sqrt(t)Z; bounded convergence proves E f(x_n+sqrt(t_n)Z) tends to f(x) when f is bounded continuous.

- Use case: Initial-condition verification for heat and Feynman-Kac formulas.

- Tags: heat-kernel, initial-condition, bounded-convergence

###### Heat-kernel derivative majorants

- ID: `ch9_exercise_method_heat_kernel_derivative_majorants`

- Kind: regularity-template

- Summary: On t bounded away from zero, derivatives of the Gaussian kernel are polynomial times a Gaussian, giving integrable majorants for differentiating under the integral.

- Use case: Proving C^{1,2} smoothing for heat semigroups.

- Tags: heat-kernel, regularity, dominated-convergence

###### Source-term martingale for inhomogeneous heat equations

- ID: `ch9_exercise_method_source_term_martingale`

- Kind: proof-template

- Summary: For u_t=(1/2)Delta u+g, add integral_0^s g(B_r)dr to u(t-s,B_s) so the drift cancels.

- Use case: Duhamel representation and source-term uniqueness.

- Tags: duhamel, source-term, martingale

###### Duhamel uniqueness from bounded martingales

- ID: `ch9_exercise_method_duhamel_uniqueness`

- Kind: proof-template

- Summary: A bounded inhomogeneous heat solution with zero initial data equals E_x integral_0^t g(B_s)ds by stopping the source-term martingale at s=t.

- Use case: Identifying source-forced heat solutions and occupation integrals.

- Tags: duhamel, uniqueness, occupation-integral

###### Short-time Markov-property PDE verification

- ID: `ch9_exercise_method_markov_property_pde_verification`

- Kind: calculation-template

- Summary: Use v(t+h,x)=E_x[v(t,B_h)+short-time reward], Taylor expand v(t,B_h), divide by h, and let h down to zero.

- Use case: Showing smooth Brownian representations solve heat, Poisson, and Feynman-Kac PDEs.

- Tags: markov-property, taylor-expansion, pde-verification

###### Holder cancellation for singular heat-source kernels

- ID: `ch9_exercise_method_holder_cancels_kernel_singularity`

- Kind: regularity-template

- Summary: Subtract g(x) inside P_s g(x)-g(x); Holder continuity gives O(s^{alpha/2}), offsetting the small-time singularity.

- Use case: Regularity of inhomogeneous heat and potential-kernel formulas.

- Tags: holder-continuity, regularity, singular-kernel

###### Exponential potential weight martingale

- ID: `ch9_exercise_method_exponential_weight_martingale`

- Kind: proof-template

- Summary: Multiply by exp(integral c(B_s)ds); the finite-variation product rule adds exactly the c u drift needed for cancellation.

- Use case: Feynman-Kac and Schrodinger martingale derivations.

- Tags: feynman-kac, exponential-weight, martingale

###### Bounded Feynman-Kac uniqueness

- ID: `ch9_exercise_method_feynman_kac_bounded_uniqueness`

- Kind: proof-template

- Summary: If c and u are bounded on finite time intervals, the weighted martingale is bounded; stopping at t gives u(t,x)=E_x[f(B_t)exp(integral_0^t c(B_s)ds)].

- Use case: Parabolic PDEs with bounded multiplicative potentials.

- Tags: feynman-kac, boundedness, uniqueness

###### Smooth Feynman-Kac short-time check

- ID: `ch9_exercise_method_smooth_feynman_kac_short_time_check`

- Kind: calculation-template

- Summary: Use v(t+h,x)=E_x[e^{int_0^h c(B_s)ds}v(t,B_h)], then expand the Brownian move and the exponential to get v_t=(1/2)Delta v+c v.

- Use case: Verifying smooth Feynman-Kac representations solve the PDE.

- Tags: feynman-kac, short-time, pde-verification

###### Feynman-Kac smoothness by Duhamel reduction

- ID: `ch9_exercise_method_feynman_kac_duhamel_reduction`

- Kind: regularity-template

- Summary: Use e^{A_t}-1=integral_0^t c(B_s)e^{A_t-A_s}ds to decompose v into a heat solution plus an inhomogeneous heat solution with source c v.

- Use case: Regularity proofs for Feynman-Kac formulas with Holder f and c.

- Tags: feynman-kac, duhamel, regularity

###### Liouville theorem via heat semigroup flattening

- ID: `ch9_exercise_method_heat_semigroup_liouville`

- Kind: proof-template

- Summary: A bounded harmonic h satisfies h(x)=E h(x+B_t); as t grows, two Gaussian laws with fixed mean separation have vanishing total variation distance, so h(x)=h(y).

- Use case: Bounded harmonic functions on all of R^d.

- Tags: liouville, harmonic-functions, heat-semigroup

###### Recurrent Brownian motion forces nonnegative superharmonic functions constant

- ID: `ch9_exercise_method_recurrent_superharmonic_constancy`

- Kind: proof-template

- Summary: Nonnegative superharmonic functions yield supermartingales; in d=1,2 Brownian motion hits every small neighborhood, so optional stopping gives f(x)>=f(y) and symmetry gives equality.

- Use case: Superharmonic Liouville-type exercises in recurrent dimensions.

- Tags: superharmonic, recurrence, optional-stopping

###### Radial superharmonic examples in high dimension

- ID: `ch9_exercise_method_radial_superharmonic_high_dimension`

- Kind: example-pattern

- Summary: Use the radial Laplacian g''(r)+(d-1)g'(r)/r; functions such as (1+r^2)^{-(d-2)/2} are smooth nonconstant nonnegative superharmonic for d>=3.

- Use case: Constructing counterexamples to recurrent-dimensional constancy in transient dimensions.

- Tags: radial-laplacian, superharmonic, dimension

###### Escape probability is the nonuniqueness direction

- ID: `ch9_exercise_method_escape_probability_nonuniqueness`

- Kind: proof-template

- Summary: When Brownian motion can avoid exiting G, q(x)=P_x(tau=infinity) is a bounded zero-boundary harmonic function; all bounded zero-boundary solutions differ by c q.

- Use case: Dirichlet problems in domains where exit is not almost sure.

- Tags: dirichlet-problem, nonuniqueness, escape-probability

###### Flat cone boundary regularity

- ID: `ch9_exercise_method_flat_cone_regular_boundary`

- Kind: proof-template

- Summary: Use zeros of the perpendicular Brownian coordinate and the induced Cauchy trace on the hyperplane to show Brownian motion immediately hits a flat exterior cone.

- Use case: Checking regular boundary points under weaker geometric exterior conditions.

- Tags: regular-boundary, cone-condition, brownian-trace

###### Infinite ball occupation in recurrent dimensions

- ID: `ch9_exercise_method_recurrent_ball_occupation_infinite`

- Kind: proof-template

- Summary: Use recurrence to get infinitely many returns to a ball and the strong Markov property to sum positive occupation increments.

- Use case: Occupation-time dichotomy for Brownian motion in d<=2.

- Tags: occupation-time, recurrence, strong-markov-property

###### Gamma change of variables for transient potential kernels

- ID: `ch9_exercise_method_transient_potential_kernel_gamma`

- Kind: calculation-template

- Summary: For d>=3, integrate the heat kernel over time and use s=|x-y|^2/(2t) to get Gamma(d/2-1)/(2 pi^{d/2}) |x-y|^{2-d}.

- Use case: Green-function and expected occupation-density calculations.

- Tags: potential-kernel, gamma-function, transience

###### Modified potential kernels in recurrent dimensions

- ID: `ch9_exercise_method_recurrent_modified_potential_kernel`

- Kind: calculation-template

- Summary: Subtract a reference heat kernel before integrating over time; in d=1 this gives -|x-y| and in d=2 gives -(1/pi)log|x-y|.

- Use case: Using potential kernels when the full-space occupation integral diverges.

- Tags: potential-kernel, recurrent-dimensions, renormalization

###### Frullani integral for the two-dimensional log kernel

- ID: `ch9_exercise_method_frullani_log_kernel`

- Kind: calculation-template

- Summary: After u=1/(2t), the difference of two planar heat kernels becomes integral_0^infty (e^{-a^2u}-e^{-u})du/u=-2log a.

- Use case: Deriving the d=2 logarithmic potential kernel.

- Tags: frullani, log-kernel, dimension-two

###### Distributional delta normalization of Green kernels

- ID: `ch9_exercise_method_distributional_delta_normalization`

- Kind: proof-template

- Summary: Integrate by parts outside a small ball and let the radius shrink; the boundary flux fixes the constant so (1/2)Delta G=-delta_0.

- Use case: Checking Green-function constants and fundamental solutions.

- Tags: distributional-laplacian, green-function, flux

###### Exit-time moment recursion

- ID: `ch9_exercise_method_exit_time_moment_recursion`

- Kind: proof-template

- Summary: For m_n(x)=E_x tau^n, the Markov property or Dynkin formula gives (1/2)Delta m_n=-n m_{n-1} with zero boundary values.

- Use case: Computing higher moments of Brownian exit times.

- Tags: exit-time, moment-recursion, poisson-equation

###### Second exit-time moment Poisson system

- ID: `ch9_exercise_method_second_moment_poisson_system`

- Kind: calculation-template

- Summary: First solve (1/2)Delta v=-1 for v=E tau; then solve (1/2)Delta w=-2v for w=E tau^2, both with zero boundary values.

- Use case: Exercise 9.7.1 and second-moment exit-time computations.

- Tags: exit-time, second-moment, poisson-equation

###### Schrodinger weighted martingale

- ID: `ch9_exercise_method_schrodinger_weighted_martingale`

- Kind: proof-template

- Summary: For (1/2)Delta u+c u=0, Ito plus the finite-variation product rule makes u(B_t)exp(integral_0^t c(B_s)ds) a local martingale before exit.

- Use case: Boundary Feynman-Kac formulas for elliptic equations with potential.

- Tags: schrodinger-equation, feynman-kac, martingale

###### Gauge integrability condition

- ID: `ch9_exercise_method_gauge_integrability_condition`

- Kind: criterion

- Summary: Before applying boundary Feynman-Kac with positive potential, check w(x)=E_x exp(integral_0^tau c(B_s)ds); bounded c alone does not ensure finiteness.

- Use case: Avoiding false Schrodinger Feynman-Kac representations.

- Tags: gauge, integrability, positive-potential

###### Interval eigenvalue threshold for exponential exit times

- ID: `ch9_exercise_method_interval_eigenvalue_threshold`

- Kind: calculation-template

- Summary: For tau exiting (-a,a), solve (1/2)u''+gamma u=0 with boundary value one; finiteness holds exactly below gamma=pi^2/(8a^2).

- Use case: Explicit exponential exit-time moments and gauge blow-up examples.

- Tags: exit-time, eigenvalue, interval

###### Finite-gauge boundary Feynman-Kac uniqueness

- ID: `ch9_exercise_method_finite_gauge_boundary_feynman_kac`

- Kind: proof-template

- Summary: Finite bounded gauge controls the terminal exponential weight and kills the tail term, giving u(x)=E_x[f(B_tau)exp(integral_0^tau c(B_s)ds)].

- Use case: Uniqueness of bounded Schrodinger Dirichlet solutions.

- Tags: finite-gauge, dirichlet-problem, feynman-kac

###### Local exit expansion for smooth Schrodinger representations

- ID: `ch9_exercise_method_smooth_schrodinger_local_exit_expansion`

- Kind: calculation-template

- Summary: Stop at a small ball, expand v(B_sigma) and exp(integral_0^sigma c(B_s)ds), then divide by E sigma to get (1/2)Delta v+c v=0.

- Use case: Verifying smooth Schrodinger Feynman-Kac formulas solve the PDE.

- Tags: schrodinger-equation, local-exit, taylor-expansion

##### Exercise Records

###### 9.2 Heat equation, Brownian semigroup, and heat-kernel smoothing

####### 9.2.A the backward heat martingale

- ID: `durrett_ch9_exercise_9_2_A`

- Method tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- Knowledge used: durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

####### 9.2.B uniqueness of bounded heat solutions

- ID: `durrett_ch9_exercise_9_2_B`

- Method tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- Knowledge used: durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

####### 9.2.C the initial condition for the Brownian formula

- ID: `durrett_ch9_exercise_9_2_C`

- Method tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- Knowledge used: durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

####### 9.2.D heat-kernel smoothing and the PDE

- ID: `durrett_ch9_exercise_9_2_D`

- Method tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- Knowledge used: durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

###### 9.3 Inhomogeneous heat equation and Duhamel occupation formulas

####### 9.3.A the source-term martingale

- ID: `durrett_ch9_exercise_9_3_A`

- Method tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

####### 9.3.B uniqueness and Duhamel's formula

- ID: `durrett_ch9_exercise_9_3_B`

- Method tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

####### 9.3.C smooth formula implies the PDE

- ID: `durrett_ch9_exercise_9_3_C`

- Method tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

####### 9.3.D initial condition

- ID: `durrett_ch9_exercise_9_3_D`

- Method tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

####### 9.3.E kernel form and regularity

- ID: `durrett_ch9_exercise_9_3_E`

- Method tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

###### 9.4 Feynman-Kac formula for heat equations with potentials

####### 9.4.A the weighted martingale

- ID: `durrett_ch9_exercise_9_4_A`

- Method tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- New knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

####### 9.4.B uniqueness and the Feynman-Kac formula

- ID: `durrett_ch9_exercise_9_4_B`

- Method tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- New knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

####### 9.4.C a smooth Feynman-Kac formula solves the PDE

- ID: `durrett_ch9_exercise_9_4_C`

- Method tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- New knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

####### 9.4.D initial condition

- ID: `durrett_ch9_exercise_9_4_D`

- Method tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- New knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

####### 9.4.E reducing smoothness to Sections 9.2 and 9.3

- ID: `durrett_ch9_exercise_9_4_E`

- Method tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- New knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

###### 9.5 Dirichlet problem, Liouville principles, and boundary regularity

####### 9.5.1 Exercise 9.5.1

- ID: `durrett_ch9_exercise_9_5_1`

- Method tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- New knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

####### 9.5.2 Exercise 9.5.2

- ID: `durrett_ch9_exercise_9_5_2`

- Method tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- New knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

####### 9.5.3 Exercise 9.5.3

- ID: `durrett_ch9_exercise_9_5_3`

- Method tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- New knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

####### 9.5.4 Exercise 9.5.4

- ID: `durrett_ch9_exercise_9_5_4`

- Method tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- New knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

####### 9.5.5 Exercise 9.5.5

- ID: `durrett_ch9_exercise_9_5_5`

- Method tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- New knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

###### 9.6 Green functions, occupation densities, and potential-kernel normalization

####### 9.6.A occupation time of a ball

- ID: `durrett_ch9_exercise_9_6_A`

- Method tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- New knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

####### 9.6.B the potential kernel in $d\ge3$

- ID: `durrett_ch9_exercise_9_6_B`

- Method tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- New knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

####### 9.6.C the modified kernel in $d=1$

- ID: `durrett_ch9_exercise_9_6_C`

- Method tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- New knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

####### 9.6.D the modified kernel in $d=2$

- ID: `durrett_ch9_exercise_9_6_D`

- Method tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- New knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

####### 9.6.E distributional normalization

- ID: `durrett_ch9_exercise_9_6_E`

- Method tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- New knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

###### 9.7 Poisson equation and exit-time moment recursions

####### 9.7.1 Exercise 9.7.1

- ID: `durrett_ch9_exercise_9_7_1`

- Method tags: poisson-equation, exit-time-moments, moment-recursion

- Knowledge used: durrett_ch9_poisson_equation_representation, durrett_ch9_expected_exit_time_poisson, durrett_ch9_poisson_boundary_regular

- New knowledge: ch9_exercise_method_exit_time_moment_recursion, ch9_exercise_method_second_moment_poisson_system

###### 9.8 Schrodinger equation, gauge integrability, and exponential exit moments

####### 9.8.A the Schrodinger martingale

- ID: `durrett_ch9_exercise_9_8_A`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

####### 9.8.B why boundedness alone is not enough

- ID: `durrett_ch9_exercise_9_8_B`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

####### 9.8.C the gauge and finite-gauge uniqueness

- ID: `durrett_ch9_exercise_9_8_C`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

####### 9.8.D the smooth representation solves the PDE

- ID: `durrett_ch9_exercise_9_8_D`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

####### 9.8.E boundary condition at regular points

- ID: `durrett_ch9_exercise_9_8_E`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

####### 9.8.F exponential exit time from an interval

- ID: `durrett_ch9_exercise_9_8_F`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

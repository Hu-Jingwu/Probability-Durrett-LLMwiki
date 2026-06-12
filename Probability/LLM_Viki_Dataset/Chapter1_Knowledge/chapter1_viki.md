# Durrett Chapter 1 LLM Viki: Probability Foundations

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter1.pdf`.

This unified Chapter 1 knowledge base includes the original textbook knowledge pieces plus exercise-derived method patterns from the solved Chapter 1 exercises.

Exercise source: `Probability/Exercises/Chapter1/Chapter1Exercises.tex` and `Probability/Exercises/Chapter1/Chapter1Exercises.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

## Section Guides

### 1.1 Probability Spaces

- Goal: Speak fluently about events, sigma-fields, probability measures, and extension from simple generating classes.

- Must master: probability space, sigma-field, continuity of measure, Stieltjes measure, semialgebra extension

- Prelim angle: Often appears as proof scaffolding inside convergence, Borel-Cantelli, and distribution problems rather than as a standalone question.

### 1.2 Distributions

- Goal: Move between laws, CDFs, densities/mass functions, atoms, and transformations.

- Must master: CDF properties, valid CDF to law, atoms as jumps, normal tail bounds

- Prelim angle: Directly relevant to tightness, weak convergence, and characteristic-function problems.

### 1.3 Random Variables

- Goal: Prove measurability quickly using generators and closure under limits/composition.

- Must master: measurable maps, generator checking, arithmetic and limits of random variables, sigma(X) factorization

- Prelim angle: Needed whenever an exam asks you to justify conditional expectation, filtrations, or convergence events.

### 1.4 Integration

- Goal: Understand Lebesgue integral construction enough to know why the limit theorems work.

- Must master: simple functions, nonnegative integral, positive/negative parts, linearity

- Prelim angle: Usually supports expectation proofs; less often tested as pure integration construction.

### 1.5 Properties of the Integral

- Goal: Use Jensen, Holder, Minkowski, Fatou, MCT, DCT, and bounded convergence with exact hypotheses.

- Must master: Jensen, Holder, Minkowski, Fatou, MCT, DCT

- Prelim angle: High-frequency toolkit for bounding probabilities and passing limits under expectations.

### 1.6 Expected Value

- Goal: Treat expectation as integration and deploy inequalities/change-of-variables confidently.

- Must master: linearity, Markov/Chebyshev, expectation limit theorems, change of variables, tail integral

- Prelim angle: Central to LLN, CLT, martingale, and random-series problems.

### 1.7 Product Measures, Fubini's Theorem

- Goal: Know when iterated integration is legal and how product measures support joint distributions.

- Must master: product measure, sections, Fubini/Tonelli, product laws

- Prelim angle: Used in expectation swaps, independence calculations, and conditioning foundations.

## Knowledge Pieces

### Probability space

- ID: `durrett_ch1_probability_space`

- Section: 1.1 Probability Spaces

- Kind: definition

- Summary: A probability model is a triple (Omega, F, P): outcomes, a sigma-field of events, and a countably additive probability measure with total mass 1.

- Proof idea: Most elementary probability identities are consequences of complement closure, countable union closure, and countable additivity.

- Exam use: Use this as the opening language for proofs involving events, limsup/liminf events, and Borel-Cantelli later in Chapter 2.

- Pitfall: Do not treat arbitrary subsets as events unless F is the full power set; measurability is part of the model.

- Tags: probability-space, sigma-field, measure

### Sigma-field closure rules

- ID: `durrett_ch1_sigma_field`

- Section: 1.1 Probability Spaces

- Kind: definition

- Summary: A sigma-field is closed under complements and countable unions, hence also under countable intersections and finite set operations.

- Proof idea: Use De Morgan's laws to derive intersection closure from complement and union closure.

- Exam use: When proving a random object is measurable, show that a convenient generating class of inverse images lies in F.

- Pitfall: A countable union is allowed; an arbitrary uncountable union need not be in the sigma-field.

- Tags: sigma-field, closure, measurability

### Continuity of measure

- ID: `durrett_ch1_measure_continuity`

- Section: 1.1 Probability Spaces

- Kind: theorem

- Summary: For increasing events A_n, P(union A_n) is the limit of P(A_n). For decreasing events A_n with finite first measure, P(intersection A_n) is the limit of P(A_n).

- Proof idea: Write increasing differences as disjoint pieces; for decreasing sets apply the increasing result to complements or differences.

- Exam use: Essential for limits of events, almost sure convergence criteria, and first Borel-Cantelli arguments.

- Pitfall: For decreasing continuity, the finite-measure condition matters for general measures; it is automatic under probability measures.

- Tags: continuity-from-below, continuity-from-above, events

### Discrete probability spaces

- ID: `durrett_ch1_discrete_probability_space`

- Section: 1.1 Probability Spaces

- Kind: example

- Summary: On a countable sample space, assign nonnegative masses p(omega) summing to 1, and define P(A) as the sum over omega in A.

- Proof idea: Countable additivity reduces to rearranging nonnegative series.

- Exam use: Useful for checking intuition before proving the analogous statement for general measures.

- Pitfall: If the sample space is uncountable, point masses need not determine the whole law.

- Tags: discrete, mass-function, countable

### Stieltjes measures from distribution-like functions

- ID: `durrett_ch1_stieltjes_measure`

- Section: 1.1 Probability Spaces

- Kind: theorem

- Summary: A nondecreasing right-continuous function with suitable limits defines a unique measure on the Borel line via interval increments.

- Proof idea: First define the measure on intervals, verify finite additivity and continuity, then extend to the generated sigma-field.

- Exam use: This is the bridge from CDFs to probability measures on R.

- Pitfall: Right-continuity is not cosmetic; it pins down the measure on half-infinite intervals and atoms.

- Tags: stieltjes, cdf, borel-measure

### Extension from semialgebras

- ID: `durrett_ch1_semialgebra_extension`

- Section: 1.1 Probability Spaces

- Kind: proof-template

- Summary: A measure-like set function on a semialgebra can be extended when it has the right countable additivity/continuity behavior on the generating class.

- Proof idea: Pass from semialgebra pieces to finite disjoint unions, then use approximation and countable additivity to extend.

- Exam use: Explains why specifying probabilities on intervals or rectangles is enough in many probability models.

- Pitfall: Do not assume every finitely additive premeasure extends; the countable condition is the serious part.

- Tags: semialgebra, extension, premeasure

### Multidimensional distribution functions

- ID: `durrett_ch1_product_distribution_function`

- Section: 1.1 Probability Spaces

- Kind: theorem

- Summary: A function on R^d satisfying monotonicity over rectangles, right-continuity, and correct limits defines a probability measure on Borel R^d.

- Proof idea: Use rectangle increments and an extension theorem from a semialgebra of rectangles.

- Exam use: This underlies joint distributions and later independence statements.

- Pitfall: Coordinatewise monotonicity alone is not enough; rectangle probabilities must be nonnegative.

- Tags: joint-distribution, rectangles, borel-rd

### Distribution function properties

- ID: `durrett_ch1_distribution_function`

- Section: 1.2 Distributions

- Kind: theorem

- Summary: A CDF is nondecreasing, right-continuous, tends to 0 at -infinity, and tends to 1 at +infinity.

- Proof idea: Monotonicity follows from event inclusion; right-continuity follows from continuity of probability for decreasing events.

- Exam use: Use these properties to test whether a proposed function can be a CDF.

- Pitfall: Left-continuity is generally false; jumps represent atoms.

- Tags: cdf, distribution, right-continuity

### Every valid CDF determines a law

- ID: `durrett_ch1_cdf_to_law`

- Section: 1.2 Distributions

- Kind: theorem

- Summary: Any function with the standard CDF properties is the distribution function of a unique probability measure on R.

- Proof idea: Construct a Stieltjes measure and check that its half-line values match the function.

- Exam use: Lets you prove convergence claims by identifying limiting CDFs, provided the limit is a valid CDF at continuity points.

- Pitfall: A pointwise limit of CDFs may fail to be a CDF if total mass escapes to infinity.

- Tags: cdf, law, tightness

### Atoms are jumps of the CDF

- ID: `durrett_ch1_atoms_jumps`

- Section: 1.2 Distributions

- Kind: fact

- Summary: For a real random variable, P(X = x) equals the jump F(x) - F(x-) of its distribution function.

- Proof idea: Compare events {X <= x} and {X < x}; use monotone convergence from below for F(x-).

- Exam use: Useful for mixed discrete-continuous examples and for proving a CDF has at most countably many discontinuities.

- Pitfall: A continuous CDF does not imply a density exists; the Cantor distribution is the standard warning.

- Tags: atom, cdf-jump, discontinuity

### Standard normal tail estimate

- ID: `durrett_ch1_normal_tail_bound`

- Section: 1.2 Distributions

- Kind: inequality

- Summary: The standard normal upper tail has exponential decay comparable to phi(x)/x for positive x.

- Proof idea: Integrate the normal density and compare using monotonicity or one integration-by-parts style bound.

- Exam use: Appears in Brownian motion, LIL-style bounds, and CLT error estimates.

- Pitfall: Keep track of whether a bound is one-sided or two-sided; prelim solutions often lose constants harmlessly but not exponents.

- Tags: normal, tail-bound, inequality

### Probability integral transform

- ID: `durrett_ch1_probability_integral_transform`

- Section: 1.2 Distributions

- Kind: fact

- Summary: If X has a continuous CDF F, then F(X) is uniform on (0,1) under suitable strictness/continuity conditions.

- Proof idea: Compute P(F(X) <= u) by translating through quantiles; handle flat parts carefully.

- Exam use: Useful for constructing random variables from uniform variables and for distribution transformations.

- Pitfall: Continuity alone needs care when F has flat intervals; use generalized inverses for the clean general statement.

- Tags: cdf-transform, uniform, quantile

### Random variables as measurable maps

- ID: `durrett_ch1_measurable_map`

- Section: 1.3 Random Variables

- Kind: definition

- Summary: A random variable is a measurable map from the sample space to a measurable state space.

- Proof idea: Check inverse images of measurable target sets.

- Exam use: This is the language needed for sigma(X), conditional expectation, and stochastic processes.

- Pitfall: Do not confuse a random variable with its distribution; different variables may have the same law.

- Tags: random-variable, measurable-map, law

### Checking measurability on generators

- ID: `durrett_ch1_measurability_generator`

- Section: 1.3 Random Variables

- Kind: theorem

- Summary: To prove X is measurable into a generated sigma-field, it is enough to check inverse images of a generating class.

- Proof idea: The inverse-image operation preserves complements and countable unions, so the checked class expands to a sigma-field.

- Exam use: Use half-lines for real variables and rectangles for vector-valued variables.

- Pitfall: The generator must actually generate the target sigma-field; checking too small a class proves too little.

- Tags: measurability, generator, inverse-image

### Composition of measurable maps

- ID: `durrett_ch1_composition_measurable`

- Section: 1.3 Random Variables

- Kind: theorem

- Summary: If X is measurable and f is measurable, then f(X) is measurable.

- Proof idea: Inverse images compose: {f(X) in A} equals {X in f^{-1}(A)}.

- Exam use: Use this to justify transformations such as X^2, exp(X), indicators, vectors, sums, limsup, and liminf.

- Pitfall: Continuity is sufficient for Borel measurability, but not necessary.

- Tags: composition, transformation, measurable

### Arithmetic of random variables

- ID: `durrett_ch1_measurable_arithmetic`

- Section: 1.3 Random Variables

- Kind: theorem

- Summary: Finite sums, products, maxima, minima, and continuous functions of random variables are random variables.

- Proof idea: View (X,Y) as a measurable vector and compose with continuous maps such as addition or multiplication.

- Exam use: Often needed before taking expectations of constructed quantities.

- Pitfall: Do not use arithmetic closure for extended real expressions without checking undefined forms like infinity minus infinity.

- Tags: arithmetic, measurable, random-variables

### Limits preserve measurability

- ID: `durrett_ch1_limits_measurable`

- Section: 1.3 Random Variables

- Kind: theorem

- Summary: Supremum, infimum, limsup, liminf, and pointwise limits of measurable real functions are measurable.

- Proof idea: Express events such as {sup X_n <= a} or {limsup X_n < a} using countable unions/intersections of measurable events.

- Exam use: Crucial for defining almost sure convergence and stopping-time events.

- Pitfall: The countability of the sequence matters; arbitrary suprema over uncountable families can fail measurability.

- Tags: limsup, liminf, measurability, countability

### Functions measurable with respect to sigma(X)

- ID: `durrett_ch1_sigma_x_factorization`

- Section: 1.3 Random Variables

- Kind: fact

- Summary: A random variable Y is sigma(X)-measurable exactly when it can be represented as a measurable function of X.

- Proof idea: Approximate Y by simple functions and show each sigma(X)-measurable indicator factors through X.

- Exam use: This is a foundation for conditional expectation as a function of observed information.

- Pitfall: The representing function is only determined up to the distribution of X, not necessarily pointwise everywhere.

- Tags: sigma-x, factorization, conditional-expectation

### Simple functions

- ID: `durrett_ch1_simple_functions`

- Section: 1.4 Integration

- Kind: definition

- Summary: A simple function takes finitely many values and is the starting point for defining the Lebesgue integral.

- Proof idea: Define the integral as the sum of value times measure over level sets, then extend by monotone approximation.

- Exam use: When stuck on an integral proof, first prove it for indicators, then simple functions, then limits.

- Pitfall: Representations of a simple function are not unique; use canonical level sets to avoid ambiguity.

- Tags: simple-function, lebesgue-integral, proof-template

### Integral of a nonnegative function

- ID: `durrett_ch1_nonnegative_integral`

- Section: 1.4 Integration

- Kind: definition

- Summary: The integral of a nonnegative measurable function is the supremum of integrals of simple functions bounded above by it.

- Proof idea: Approximate from below by simple functions and use monotone behavior.

- Exam use: This definition makes monotone convergence natural rather than surprising.

- Pitfall: The value may be infinite; do not subtract two infinite nonnegative integrals.

- Tags: nonnegative-integral, approximation, mct

### Integrable signed functions

- ID: `durrett_ch1_integrable_function`

- Section: 1.4 Integration

- Kind: definition

- Summary: A signed measurable function is integrable when the integrals of its positive and negative parts are finite, equivalently the integral of its absolute value is finite.

- Proof idea: Define integral as integral of positive part minus integral of negative part.

- Exam use: Before using linearity or dominated convergence, check integrability conditions.

- Pitfall: Finite positive and negative parts are needed; infinity minus infinity is not an acceptable value.

- Tags: integrability, positive-part, negative-part

### Linearity and order properties of the integral

- ID: `durrett_ch1_integral_linearity`

- Section: 1.4 Integration

- Kind: theorem

- Summary: For integrable functions, the integral is linear, monotone, and respects almost-everywhere equality.

- Proof idea: Prove first for simple functions, extend to nonnegative functions, then signed integrable functions.

- Exam use: Use to split expectations, compare nonnegative variables, and justify replacing variables by a.s. equal versions.

- Pitfall: Linearity can fail as a finite statement if one side involves undefined infinities.

- Tags: linearity, monotonicity, almost-everywhere

### Jensen's inequality for integrals

- ID: `durrett_ch1_jensen_integral`

- Section: 1.5 Properties of the Integral

- Kind: inequality

- Summary: For a convex function phi and a probability measure, phi(integral f) is at most integral phi(f), assuming the quantities are defined.

- Proof idea: Use a supporting line to the convex function at the mean.

- Exam use: Prelim workhorse for Lp comparisons, moment generating bounds, and conditional Jensen later.

- Pitfall: Convexity direction matters; strict equality often encodes almost sure constancy under strict convexity.

- Tags: jensen, convexity, inequality

### Holder's inequality

- ID: `durrett_ch1_holder_integral`

- Section: 1.5 Properties of the Integral

- Kind: inequality

- Summary: If p and q are conjugate exponents, the integral of |fg| is bounded by the Lp norm of f times the Lq norm of g.

- Proof idea: Normalize the functions and apply Young's inequality; handle zero norms separately.

- Exam use: Used for moment interpolation, uniform integrability checks, and bounding expectations of products.

- Pitfall: Remember the endpoint cases need separate interpretation.

- Tags: holder, lp, inequality

### Minkowski's inequality

- ID: `durrett_ch1_minkowski`

- Section: 1.5 Properties of the Integral

- Kind: inequality

- Summary: The Lp norm satisfies the triangle inequality for p at least 1.

- Proof idea: Apply Holder to |f+g|^p split as |f+g|^{p-1}|f| plus the analogous term for g.

- Exam use: Use to prove Lp spaces are normed and to control sums of random variables in Lp.

- Pitfall: For p below 1 this is not a norm inequality.

- Tags: minkowski, lp, triangle-inequality

### Bounded convergence theorem

- ID: `durrett_ch1_bounded_convergence`

- Section: 1.5 Properties of the Integral

- Kind: theorem

- Summary: On a finite-measure space, uniformly bounded functions converging pointwise have integrals converging to the integral of the limit.

- Proof idea: Reduce to dominated convergence with a constant dominating function, or prove using finite measure and small exceptional sets.

- Exam use: Useful for probability spaces when random variables are uniformly bounded.

- Pitfall: Finite measure is essential; bounded pointwise convergence on an infinite measure space need not preserve integrals.

- Tags: bounded-convergence, finite-measure, limit

### Fatou's lemma

- ID: `durrett_ch1_fatou_integral`

- Section: 1.5 Properties of the Integral

- Kind: theorem

- Summary: For nonnegative functions, the integral of the liminf is at most the liminf of the integrals.

- Proof idea: Let g_n be the infimum over the tail; g_n increases to the liminf and monotone convergence applies.

- Exam use: Use for lower semicontinuity of expectations and to prove integrability of a limit from bounded expectations.

- Pitfall: Fatou gives an inequality, not usually equality.

- Tags: fatou, liminf, nonnegative

### Monotone convergence theorem

- ID: `durrett_ch1_monotone_convergence`

- Section: 1.5 Properties of the Integral

- Kind: theorem

- Summary: If nonnegative measurable functions increase pointwise to f, then their integrals increase to the integral of f.

- Proof idea: The lower approximation definition of the integral makes the result direct.

- Exam use: Use for exchanging sums and expectations of nonnegative random variables.

- Pitfall: The monotone direction and nonnegativity are not optional unless you shift or dominate carefully.

- Tags: mct, monotone-convergence, nonnegative

### Dominated convergence theorem

- ID: `durrett_ch1_dominated_convergence`

- Section: 1.5 Properties of the Integral

- Kind: theorem

- Summary: If f_n converges pointwise a.e. to f and |f_n| is bounded by an integrable g, then integrals of f_n converge to the integral of f.

- Proof idea: Apply Fatou to g + f_n and g - f_n, or to |f_n - f| after a standard argument.

- Exam use: The main theorem for passing limits through expectations under a uniform integrable bound.

- Pitfall: Pointwise boundedness is not enough; the dominating function must be integrable and independent of n.

- Tags: dct, dominated-convergence, limit

### Expected value as Lebesgue integral

- ID: `durrett_ch1_expectation_as_integral`

- Section: 1.6 Expected Value

- Kind: definition

- Summary: Expectation is the integral of a random variable with respect to the probability measure.

- Proof idea: All integral theorems transfer directly to expectations.

- Exam use: This unifies discrete sums, density integrals, and abstract random variables.

- Pitfall: An expectation can be undefined if positive and negative parts are both infinite.

- Tags: expectation, lebesgue-integral, random-variable

### Linearity and monotonicity of expectation

- ID: `durrett_ch1_expectation_linearity`

- Section: 1.6 Expected Value

- Kind: theorem

- Summary: Expectation is linear for integrable random variables and monotone for ordered random variables.

- Proof idea: Apply integral linearity and monotonicity.

- Exam use: Use constantly in variance, covariance, martingale, and conditioning calculations.

- Pitfall: Linearity does not require independence; product factorization does.

- Tags: expectation, linearity, monotonicity

### Markov and Chebyshev inequalities

- ID: `durrett_ch1_markov_chebyshev`

- Section: 1.6 Expected Value

- Kind: inequality

- Summary: Markov bounds the probability of a nonnegative variable exceeding a threshold by its expectation over the threshold; Chebyshev applies this to powers or centered moments.

- Proof idea: Use the indicator inequality a 1_{X >= a} <= X for Markov, then specialize with nonnegative functions.

- Exam use: Core tool for convergence in probability, LLN proofs, and variance bounds.

- Pitfall: Check nonnegativity and choose the right moment; a weak moment gives a weak tail bound.

- Tags: markov-inequality, chebyshev, tail-bound

### Limit theorems for expectation

- ID: `durrett_ch1_expectation_limit_theorems`

- Section: 1.6 Expected Value

- Kind: theorem-card

- Summary: Fatou, monotone convergence, dominated convergence, and bounded convergence all have expectation versions.

- Proof idea: Translate each integral theorem to the probability space.

- Exam use: A prelim proof often hinges on naming exactly the right convergence theorem and verifying its hypotheses.

- Pitfall: Do not cite dominated convergence when you only have bounded expectations; that is a uniform integrability issue, not automatic domination.

- Tags: expectation, fatou, mct, dct

### Change of variables formula

- ID: `durrett_ch1_change_of_variables`

- Section: 1.6 Expected Value

- Kind: theorem

- Summary: If X has law mu and f is measurable, then E[f(X)] equals the integral of f with respect to mu, when the positive or integrable conditions hold.

- Proof idea: Prove for indicators, extend to simple functions, nonnegative functions, and signed integrable functions.

- Exam use: Lets you compute expectations using the distribution rather than the underlying sample space.

- Pitfall: Do not assume a density exists; the law may be discrete, continuous, singular, or mixed.

- Tags: change-of-variables, law, expectation

### Tail integral and nonnegative expectations

- ID: `durrett_ch1_tail_sum_nonnegative`

- Section: 1.6 Expected Value

- Kind: formula

- Summary: For nonnegative random variables, expectations can often be computed or bounded through tail probabilities.

- Proof idea: Write X as an integral of indicators {X > t} and apply Fubini/Tonelli.

- Exam use: Important for moment bounds, heavy-tail examples, and Borel-Cantelli estimates.

- Pitfall: Mind strict versus non-strict inequalities only at atoms; the integral is unaffected in many continuous-parameter formulas.

- Tags: tail-integral, nonnegative, fubini

### Common expectation computations

- ID: `durrett_ch1_common_distributions_expectations`

- Section: 1.6 Expected Value

- Kind: example-bank

- Summary: Chapter 1 reviews expectations for exponential, normal, Bernoulli, Poisson, and geometric distributions.

- Proof idea: Use densities or mass functions plus the change-of-variables formula; use series identities for discrete distributions.

- Exam use: These examples are quick diagnostic checks for later characteristic-function and limit problems.

- Pitfall: Parameterization varies, especially for geometric distributions; state your convention.

- Tags: common-distributions, expectation, examples

### Inclusion-exclusion and Bonferroni

- ID: `durrett_ch1_inclusion_exclusion`

- Section: 1.6 Expected Value

- Kind: formula

- Summary: The probability of a finite union can be expanded by alternating sums of intersection probabilities, with Bonferroni inequalities for truncations.

- Proof idea: Apply expectation to sums/products of indicator variables.

- Exam use: Useful for event-counting, occupancy-style estimates, and bounding union probabilities more sharply than the union bound.

- Pitfall: The exact formula is finite; infinite versions require additional limiting arguments.

- Tags: inclusion-exclusion, bonferroni, indicators

### Product measures

- ID: `durrett_ch1_product_measure`

- Section: 1.7 Product Measures, Fubini's Theorem

- Kind: definition

- Summary: Given measure spaces, the product measure is the unique measure on the product sigma-field that agrees with products of measures on measurable rectangles.

- Proof idea: Define on rectangles, verify premeasure properties, and extend.

- Exam use: The measure-theoretic basis for joint distributions and independence.

- Pitfall: A set in the product sigma-field can be much more complicated than a rectangle.

- Tags: product-measure, rectangles, joint-law

### Measurable sections

- ID: `durrett_ch1_sections_measurable`

- Section: 1.7 Product Measures, Fubini's Theorem

- Kind: lemma

- Summary: For a measurable set in a product space, its x-section is measurable in the second space, and section measures are measurable functions of x.

- Proof idea: Prove first for rectangles, then close the class under monotone operations.

- Exam use: This is the technical engine behind Fubini and Tonelli.

- Pitfall: Do not assume section results for nonmeasurable product subsets.

- Tags: sections, product-space, measurability

### Fubini and Tonelli theorem

- ID: `durrett_ch1_fubini_tonelli`

- Section: 1.7 Product Measures, Fubini's Theorem

- Kind: theorem

- Summary: For nonnegative functions, iterated integrals and the product integral agree. For signed functions, the same holds when the absolute integral is finite.

- Proof idea: Prove by indicators, simple functions, monotone convergence, then signed decomposition under integrability.

- Exam use: Use to exchange sums/integrals/expectations and compute expectations by conditioning-like iterated integration.

- Pitfall: Tonelli handles nonnegative functions even with infinite value; Fubini for signed functions needs integrability.

- Tags: fubini, tonelli, iterated-integral

### Product measures as preview of independence

- ID: `durrett_ch1_independence_preview`

- Section: 1.7 Product Measures, Fubini's Theorem

- Kind: concept-link

- Summary: When a joint law factors as a product measure, the coordinates behave independently.

- Proof idea: Rectangular probabilities factor, and extension carries this to generated sigma-fields.

- Exam use: This prepares for Chapter 2 independence and for computing expectations of products.

- Pitfall: Independence is a statement about the joint law, not merely about marginal distributions.

- Tags: product-law, independence, joint-distribution

### Countable/co-countable probability measure

- ID: `exercise_method_countable_cocountable_measure`

- Section: 1.1 Exercises: Probability spaces, sigma-fields, generators, and set algebras

- Kind: exercise-pattern

- Summary: To verify the countable/co-countable construction, split disjoint families into the cases where all sets are countable or exactly one set is co-countable.

- Proof idea: Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

- Exam use: Exercise 1.1.1 and any probability-space verification on unusual sigma-fields.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: probability-space, countable-additivity, co-countable

- Source exercises: 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5

### Borel sigma-field from half-open rectangles

- ID: `exercise_method_borel_generated_by_half_open_rectangles`

- Section: 1.1 Exercises: Probability spaces, sigma-fields, generators, and set algebras

- Kind: exercise-pattern

- Summary: Show half-open rectangles are Borel, then express rational open rectangles as countable unions of half-open rectangles; use the countable rational base.

- Proof idea: Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

- Exam use: Exercises 1.1.2 and 1.1.3; product-measure generation arguments.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: borel, generator, rectangles

- Source exercises: 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5

### Increasing union of sigma-fields can fail countable closure

- ID: `exercise_method_increasing_sigma_fields_not_sigma_field`

- Section: 1.1 Exercises: Probability spaces, sigma-fields, generators, and set algebras

- Kind: counterexample-template

- Summary: Use finite initial-coordinate sigma-fields on N; their union contains every finite set but misses an infinite non-cofinite set such as the evens.

- Proof idea: Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

- Exam use: Exercise 1.1.4; distinguishing algebras from sigma-fields.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: sigma-field, algebra, counterexample

- Source exercises: 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5

### Block construction for asymptotic density counterexamples

- ID: `exercise_method_asymptotic_density_block_counterexample`

- Section: 1.1 Exercises: Probability spaces, sigma-fields, generators, and set algebras

- Kind: counterexample-template

- Summary: Use rapidly growing blocks so the latest block dominates all previous blocks; alternate behavior by blocks to destroy the density of intersections.

- Proof idea: Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

- Exam use: Exercise 1.1.5 and density/limit counterexamples.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: asymptotic-density, counterexample, blocks

- Source exercises: 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5

### Piecewise random variable measurability

- ID: `exercise_method_piecewise_random_variable_measurability`

- Section: 1.2 Exercises: Distributions, normal tails, transformations, and density calculations

- Kind: proof-template

- Summary: For Z = X on A and Y on A^c, write {Z <= x} as (A cap {X <= x}) union (A^c cap {Y <= x}).

- Proof idea: Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

- Exam use: Exercise 1.2.1; patching random variables on measurable events.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: measurability, piecewise, random-variable

- Source exercises: 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7

### Countability of CDF jumps

- ID: `exercise_method_countable_cdf_discontinuities`

- Section: 1.2 Exercises: Distributions, normal tails, transformations, and density calculations

- Kind: proof-template

- Summary: Group jumps by size bigger than 1/m inside bounded intervals; each group is finite because total CDF increase is at most one.

- Proof idea: Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

- Exam use: Exercise 1.2.3; monotone-function discontinuity arguments.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: cdf, jumps, countability

- Source exercises: 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7

### Monotone density change of variables

- ID: `exercise_method_density_change_of_variables`

- Section: 1.2 Exercises: Distributions, normal tails, transformations, and density calculations

- Kind: calculation-template

- Summary: For Y=g(X) with g increasing, compute F_Y(y)=P(X <= g^{-1}(y)) and differentiate to get f_X(g^{-1}(y))/g'(g^{-1}(y)).

- Proof idea: Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

- Exam use: Exercises 1.2.5 and 1.2.6; lognormal and affine density transforms.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: density, change-of-variables, cdf

- Source exercises: 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7

### Density of a square transform

- ID: `exercise_method_square_transform_density`

- Section: 1.2 Exercises: Distributions, normal tails, transformations, and density calculations

- Kind: calculation-template

- Summary: For Y=X^2, use F_Y(y)=P(-sqrt(y)<=X<=sqrt(y)) and differentiate to get [f(sqrt(y))+f(-sqrt(y))]/(2sqrt(y)).

- Proof idea: Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

- Exam use: Exercise 1.2.7; chi-square with one degree of freedom.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: density, chi-square, transformation

- Source exercises: 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7

### Rational cut proof for sum measurability

- ID: `exercise_method_rational_cut_sum_measurability`

- Section: 1.3 Exercises: Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- Kind: proof-template

- Summary: Write {X+Y<x} as the countable union over q in Q of {X<q} cap {Y<x-q}.

- Proof idea: Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

- Exam use: Exercise 1.3.2; direct measurability of sums.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: measurability, rationals, sum

- Source exercises: 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.3.5, 1.3.6, 1.3.7, 1.3.8, 1.3.9

### Lower semicontinuity via closed sublevel sets

- ID: `exercise_method_closed_sublevel_semicontinuity`

- Section: 1.3 Exercises: Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- Kind: proof-template

- Summary: A function is lower semicontinuous iff all sets {f <= a} are closed; sequential closure proves one direction and contradiction via subsequences proves the other.

- Proof idea: Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

- Exam use: Exercise 1.3.5; proving semicontinuous functions are measurable.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: semicontinuity, closed-sets, measurability

- Source exercises: 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.3.5, 1.3.6, 1.3.7, 1.3.8, 1.3.9

### Discontinuity set from upper and lower local envelopes

- ID: `exercise_method_oscillation_discontinuity_set`

- Section: 1.3 Exercises: Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- Kind: proof-template

- Summary: Define local sup and inf over balls, take limits as radius decreases, and identify discontinuities as the set where the limiting envelopes differ.

- Proof idea: Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

- Exam use: Exercise 1.3.6; measurability of discontinuity sets.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: discontinuity, oscillation, measurability

- Source exercises: 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.3.5, 1.3.6, 1.3.7, 1.3.8, 1.3.9

### Constructive representation of sigma(X)-measurable functions

- ID: `exercise_method_constructive_sigma_x_representation`

- Section: 1.3 Exercises: Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- Kind: proof-template

- Summary: Quantize Y into dyadic bins, represent each bin as {X in B}, build Borel simple functions f_n, then take a measurable pointwise limit f with Y=f(X).

- Proof idea: Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

- Exam use: Exercises 1.3.8 and 1.3.9; conditional-expectation foundations.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: sigma-x, factorization, dyadic-approximation

- Source exercises: 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.3.5, 1.3.6, 1.3.7, 1.3.8, 1.3.9

### Zero integral of nonnegative function implies zero a.e.

- ID: `exercise_method_zero_integral_nonnegative`

- Section: 1.4 Exercises: Lebesgue integration construction and approximation

- Kind: proof-template

- Summary: Use sets {f > 1/n}; each has zero measure because integral dominates (1/n) times its measure, and their union is {f>0}.

- Proof idea: Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

- Exam use: Exercise 1.4.1; null-set proofs.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: nonnegative, zero-integral, a-e

- Source exercises: 1.4.1, 1.4.2, 1.4.3, 1.4.4

### Dyadic lower simple approximations

- ID: `exercise_method_dyadic_lower_integral_approximation`

- Section: 1.4 Exercises: Lebesgue integration construction and approximation

- Kind: calculation-template

- Summary: Approximate f>=0 by 2^{-n} floor(2^n f); the approximants increase to f and their integrals give monotone sums over dyadic level sets.

- Proof idea: Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

- Exam use: Exercise 1.4.2 and simple-function approximation.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: dyadic, simple-functions, mct

- Source exercises: 1.4.1, 1.4.2, 1.4.3, 1.4.4

### L1 approximation by continuous functions

- ID: `exercise_method_l1_continuous_approximation`

- Section: 1.4 Exercises: Lebesgue integration construction and approximation

- Kind: proof-template

- Summary: Approximate an integrable function by simple functions, approximate measurable sets by finite interval unions, then round step-function corners.

- Proof idea: Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

- Exam use: Exercise 1.4.3; density of nice functions in L1 on R.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: l1, approximation, continuous-functions

- Source exercises: 1.4.1, 1.4.2, 1.4.3, 1.4.4

### Riemann-Lebesgue by step-function reduction

- ID: `exercise_method_riemann_lebesgue_step_reduction`

- Section: 1.4 Exercises: Lebesgue integration construction and approximation

- Kind: proof-template

- Summary: Prove oscillatory integral decay for interval indicators explicitly, then approximate any L1 function by a step function.

- Proof idea: Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

- Exam use: Exercise 1.4.4; oscillatory integral estimates.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: riemann-lebesgue, step-functions, oscillation

- Source exercises: 1.4.1, 1.4.2, 1.4.3, 1.4.4

### Essential supremum bounds integrals

- ID: `exercise_method_essential_supremum_bound`

- Section: 1.5 Exercises: Lp inequalities, convergence theorems, and absolute continuity of the integral

- Kind: proof-template

- Summary: If |g| <= ||g||_infty a.e., then |fg| <= ||g||_infty |f| and integration gives the L1-Linfty Holder endpoint.

- Proof idea: Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

- Exam use: Exercise 1.5.1; endpoint Holder inequalities.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: essential-supremum, holder, linfty

- Source exercises: 1.5.1, 1.5.10, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6, 1.5.7, 1.5.8, 1.5.9

### Lp norms converge to Linfty on probability spaces

- ID: `exercise_method_lp_to_l_infty_limit`

- Section: 1.5 Exercises: Lp inequalities, convergence theorems, and absolute continuity of the integral

- Kind: proof-template

- Summary: Upper bound by essential supremum; lower bound using sets where |f| exceeds M-epsilon and their positive probability.

- Proof idea: Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

- Exam use: Exercise 1.5.2; norm comparisons.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: lp, linfty, probability-space

- Source exercises: 1.5.1, 1.5.10, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6, 1.5.7, 1.5.8, 1.5.9

### Simple functions are dense in Lp

- ID: `exercise_method_density_of_simple_functions_in_lp`

- Section: 1.5 Exercises: Lp inequalities, convergence theorems, and absolute continuity of the integral

- Kind: proof-template

- Summary: Use pointwise simple approximations bounded by |f|, then dominated convergence on |phi_n-f|^p.

- Proof idea: Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

- Exam use: Exercise 1.5.9; Lp approximation.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: lp, simple-functions, dct

- Source exercises: 1.5.1, 1.5.10, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6, 1.5.7, 1.5.8, 1.5.9

### Exchange integral and absolutely summable series

- ID: `exercise_method_absolute_summability_exchange`

- Section: 1.5 Exercises: Lp inequalities, convergence theorems, and absolute continuity of the integral

- Kind: proof-template

- Summary: If sum integral |f_n| is finite, then H=sum |f_n| is integrable; dominated convergence applies to partial sums.

- Proof idea: Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

- Exam use: Exercise 1.5.10 and 1.7.1 corollary.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: series, dct, absolute-convergence

- Source exercises: 1.5.1, 1.5.10, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6, 1.5.7, 1.5.8, 1.5.9

### Equality case in strict Jensen

- ID: `exercise_method_strict_jensen_equality`

- Section: 1.6 Exercises: Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Kind: proof-template

- Summary: For strictly convex phi, equality in Jensen forces the random variable to be almost surely constant at its mean.

- Proof idea: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Exam use: Exercise 1.6.1; strict convexity equality cases.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: jensen, strict-convexity, equality-case

- Source exercises: 1.6.1, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15, 1.6.16, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9

### Two-point distributions as Chebyshev extremizers

- ID: `exercise_method_two_point_extremizers`

- Section: 1.6 Exercises: Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Kind: counterexample-template

- Summary: To prove sharpness of moment/tail inequalities, place small mass at boundary points and the rest at a value chosen to match moments.

- Proof idea: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Exam use: Exercises 1.6.3, 1.6.4, and 1.6.5.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: chebyshev, sharpness, two-point

- Source exercises: 1.6.1, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15, 1.6.16, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9

### Cauchy-Schwarz lower bound for positive probability

- ID: `exercise_method_paley_zygmund_basic`

- Section: 1.6 Exercises: Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Kind: inequality-template

- Summary: For Y>=0, Cauchy-Schwarz applied to Y*1_{Y>0} yields P(Y>0) >= (EY)^2/EY^2.

- Proof idea: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Exam use: Exercise 1.6.6; basic Paley-Zygmund-style estimates.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: cauchy-schwarz, lower-bound, paley-zygmund

- Source exercises: 1.6.1, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15, 1.6.16, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9

### Tail truncation for expectation limits

- ID: `exercise_method_expectation_tail_truncation`

- Section: 1.6 Exercises: Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Kind: proof-template

- Summary: Control small or large tails by splitting the event and using continuity of probability plus elementary bounds on the integrand.

- Proof idea: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Exam use: Exercise 1.6.14; limits involving y E(1/X; X>y).

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: tail, truncation, expectation

- Source exercises: 1.6.1, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15, 1.6.16, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9

### Indicator expansion for inclusion-exclusion and Bonferroni

- ID: `exercise_method_inclusion_exclusion_indicators`

- Section: 1.6 Exercises: Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- Kind: proof-template

- Summary: Use 1_union = 1 - product_i(1-1_Ai), expand, and take expectations; partial alternating sums give Bonferroni bounds.

- Proof idea: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Exam use: Exercises 1.6.9 and 1.6.10.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: inclusion-exclusion, bonferroni, indicators

- Source exercises: 1.6.1, 1.6.10, 1.6.11, 1.6.12, 1.6.13, 1.6.14, 1.6.15, 1.6.16, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9

### Layer-cake formula via product sets

- ID: `exercise_method_layer_cake_formula`

- Section: 1.7 Exercises: Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- Kind: proof-template

- Summary: Represent g(x) as the vertical length of {(x,y):0 <= y < g(x)} and apply Tonelli to integrate sections.

- Proof idea: Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

- Exam use: Exercise 1.7.2; tail integrals for nonnegative functions.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: layer-cake, tonelli, tail-integral

- Source exercises: 1.7.1, 1.7.2, 1.7.3, 1.7.4, 1.7.5

### Stieltjes integration by parts with jump correction

- ID: `exercise_method_stieltjes_integration_by_parts_with_jumps`

- Section: 1.7 Exercises: Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- Kind: proof-template

- Summary: Interpret Stieltjes integrals as product-measure masses of order regions; the diagonal overlap contributes the product of jump masses.

- Proof idea: Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

- Exam use: Exercise 1.7.3.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: stieltjes, integration-by-parts, jumps

- Source exercises: 1.7.1, 1.7.2, 1.7.3, 1.7.4, 1.7.5

### Sliding interval Fubini identity

- ID: `exercise_method_interval_sliding_fubini`

- Section: 1.7 Exercises: Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- Kind: calculation-template

- Summary: Write F(x+c)-F(x) as mu((x,x+c]), swap integrals, and observe each fixed t is counted for exactly c units of x.

- Proof idea: Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

- Exam use: Exercise 1.7.4.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: fubini, distribution-function, sliding-window

- Source exercises: 1.7.1, 1.7.2, 1.7.3, 1.7.4, 1.7.5

### Sine integral via Fubini

- ID: `exercise_method_sine_integral_fubini`

- Section: 1.7 Exercises: Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- Kind: calculation-template

- Summary: Represent sin(x)/x as an integral of e^{-xy} sin(x), integrate in x first, and bound the remaining exponentially damped tails.

- Proof idea: Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

- Exam use: Exercise 1.7.5.

- Pitfall: Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.

- Tags: fubini, sine-integral, oscillatory-integral

- Source exercises: 1.7.1, 1.7.2, 1.7.3, 1.7.4, 1.7.5

## Exercise Method Cards

### 1.1 Probability spaces, sigma-fields, generators, and set algebras

- ID: `durrett_ch1_section_1_1_method_card`

- Method: Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

- Tags: sigma-field, generator, set-counterexample, measure-foundations

- New knowledge IDs: exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample

### 1.2 Distributions, normal tails, transformations, and density calculations

- ID: `durrett_ch1_section_1_2_method_card`

- Method: Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

- Tags: cdf, density-transform, normal-tail, probability-integral-transform

- New knowledge IDs: exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density

### 1.3 Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- ID: `durrett_ch1_section_1_3_method_card`

- Method: Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

- Tags: measurability, generators, semicontinuity, sigma-x-factorization

- New knowledge IDs: exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation

### 1.4 Lebesgue integration construction and approximation

- ID: `durrett_ch1_section_1_4_method_card`

- Method: Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

- Tags: lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue

- New knowledge IDs: exercise_method_zero_integral_nonnegative, exercise_method_dyadic_lower_integral_approximation, exercise_method_l1_continuous_approximation, exercise_method_riemann_lebesgue_step_reduction

### 1.5 Lp inequalities, convergence theorems, and absolute continuity of the integral

- ID: `durrett_ch1_section_1_5_method_card`

- Method: Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

- Tags: lp, holder, minkowski, mct, dct, absolute-continuity

- New knowledge IDs: exercise_method_essential_supremum_bound, exercise_method_lp_to_l_infty_limit, exercise_method_density_of_simple_functions_in_lp, exercise_method_absolute_summability_exchange

### 1.6 Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

- ID: `durrett_ch1_section_1_6_method_card`

- Method: Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

- Tags: expectation, jensen, chebyshev, moment-bound, mct, dct

- New knowledge IDs: exercise_method_strict_jensen_equality, exercise_method_two_point_extremizers, exercise_method_paley_zygmund_basic, exercise_method_expectation_tail_truncation, exercise_method_inclusion_exclusion_indicators

### 1.7 Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- ID: `durrett_ch1_section_1_7_method_card`

- Method: Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

- Tags: fubini, tonelli, product-measure, layer-cake, stieltjes

- New knowledge IDs: exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini

## Exercise Record Index

### 1.1 Probability spaces, sigma-fields, generators, and set algebras

- Exercise 1.1.1: method tags `sigma-field, generator, set-counterexample, measure-foundations`; knowledge used `durrett_ch1_probability_space, durrett_ch1_sigma_field, durrett_ch1_measure_continuity`; new knowledge `exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample`.
- Exercise 1.1.2: method tags `sigma-field, generator, set-counterexample, measure-foundations`; knowledge used `durrett_ch1_sigma_field, durrett_ch1_semialgebra_extension, durrett_ch1_product_distribution_function`; new knowledge `exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample`.
- Exercise 1.1.3: method tags `sigma-field, generator, set-counterexample, measure-foundations`; knowledge used `durrett_ch1_sigma_field, durrett_ch1_semialgebra_extension, durrett_ch1_product_distribution_function`; new knowledge `exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample`.
- Exercise 1.1.4: method tags `sigma-field, generator, set-counterexample, measure-foundations`; knowledge used `durrett_ch1_sigma_field`; new knowledge `exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample`.
- Exercise 1.1.5: method tags `sigma-field, generator, set-counterexample, measure-foundations`; knowledge used `durrett_ch1_sigma_field, durrett_ch1_measure_continuity`; new knowledge `exercise_method_countable_cocountable_measure, exercise_method_borel_generated_by_half_open_rectangles, exercise_method_increasing_sigma_fields_not_sigma_field, exercise_method_asymptotic_density_block_counterexample`.

### 1.2 Distributions, normal tails, transformations, and density calculations

- Exercise 1.2.1: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_measurable_map, durrett_ch1_measurability_generator, durrett_ch1_sigma_field`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.2: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_normal_tail_bound, durrett_ch1_distribution_function`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.3: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_distribution_function, durrett_ch1_atoms_jumps, durrett_ch1_measure_continuity`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.4: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_probability_integral_transform, durrett_ch1_distribution_function, durrett_ch1_cdf_to_law`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.5: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_change_of_variables, durrett_ch1_distribution_function, durrett_ch1_cdf_to_law`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.6: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_change_of_variables, durrett_ch1_common_distributions_expectations, durrett_ch1_distribution_function`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.
- Exercise 1.2.7: method tags `cdf, density-transform, normal-tail, probability-integral-transform`; knowledge used `durrett_ch1_change_of_variables, durrett_ch1_distribution_function, durrett_ch1_common_distributions_expectations`; new knowledge `exercise_method_piecewise_random_variable_measurability, exercise_method_countable_cdf_discontinuities, exercise_method_density_change_of_variables, exercise_method_square_transform_density`.

### 1.3 Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

- Exercise 1.3.1: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_measurability_generator, durrett_ch1_sigma_field, durrett_ch1_measurable_map`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.2: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_measurable_arithmetic, durrett_ch1_measurability_generator, durrett_ch1_sigma_field`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.3: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_composition_measurable, durrett_ch1_limits_measurable`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.4: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_composition_measurable, durrett_ch1_measurability_generator, durrett_ch1_sigma_field`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.5: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_measurability_generator, durrett_ch1_limits_measurable, durrett_ch1_sigma_field`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.6: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_limits_measurable, durrett_ch1_measurability_generator, durrett_ch1_composition_measurable`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.7: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_simple_functions, durrett_ch1_limits_measurable, durrett_ch1_measurable_map`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.8: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_sigma_x_factorization, durrett_ch1_composition_measurable, durrett_ch1_simple_functions`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.
- Exercise 1.3.9: method tags `measurability, generators, semicontinuity, sigma-x-factorization`; knowledge used `durrett_ch1_sigma_x_factorization, durrett_ch1_measurability_generator, durrett_ch1_limits_measurable`; new knowledge `exercise_method_rational_cut_sum_measurability, exercise_method_closed_sublevel_semicontinuity, exercise_method_oscillation_discontinuity_set, exercise_method_constructive_sigma_x_representation`.

### 1.4 Lebesgue integration construction and approximation

- Exercise 1.4.1: method tags `lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue`; knowledge used `durrett_ch1_nonnegative_integral, durrett_ch1_integral_linearity, durrett_ch1_measure_continuity`; new knowledge `exercise_method_zero_integral_nonnegative, exercise_method_dyadic_lower_integral_approximation, exercise_method_l1_continuous_approximation, exercise_method_riemann_lebesgue_step_reduction`.
- Exercise 1.4.2: method tags `lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue`; knowledge used `durrett_ch1_simple_functions, durrett_ch1_nonnegative_integral, durrett_ch1_monotone_convergence`; new knowledge `exercise_method_zero_integral_nonnegative, exercise_method_dyadic_lower_integral_approximation, exercise_method_l1_continuous_approximation, exercise_method_riemann_lebesgue_step_reduction`.
- Exercise 1.4.3: method tags `lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue`; knowledge used `durrett_ch1_integrable_function, durrett_ch1_simple_functions, durrett_ch1_integral_linearity`; new knowledge `exercise_method_zero_integral_nonnegative, exercise_method_dyadic_lower_integral_approximation, exercise_method_l1_continuous_approximation, exercise_method_riemann_lebesgue_step_reduction`.
- Exercise 1.4.4: method tags `lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue`; knowledge used `durrett_ch1_integrable_function, durrett_ch1_integral_linearity, durrett_ch1_dominated_convergence`; new knowledge `exercise_method_zero_integral_nonnegative, exercise_method_dyadic_lower_integral_approximation, exercise_method_l1_continuous_approximation, exercise_method_riemann_lebesgue_step_reduction`.

### 1.5 Lp inequalities, convergence theorems, and absolute continuity of the integral

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

### 1.6 Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

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

### 1.7 Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

- Exercise 1.7.1: method tags `fubini, tonelli, product-measure, layer-cake, stieltjes`; knowledge used `durrett_ch1_product_measure, durrett_ch1_fubini_tonelli, durrett_ch1_integrable_function`; new knowledge `exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini`.
- Exercise 1.7.2: method tags `fubini, tonelli, product-measure, layer-cake, stieltjes`; knowledge used `durrett_ch1_fubini_tonelli, durrett_ch1_sections_measurable, durrett_ch1_tail_sum_nonnegative`; new knowledge `exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini`.
- Exercise 1.7.3: method tags `fubini, tonelli, product-measure, layer-cake, stieltjes`; knowledge used `durrett_ch1_stieltjes_measure, durrett_ch1_product_measure, durrett_ch1_fubini_tonelli`; new knowledge `exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini`.
- Exercise 1.7.4: method tags `fubini, tonelli, product-measure, layer-cake, stieltjes`; knowledge used `durrett_ch1_stieltjes_measure, durrett_ch1_fubini_tonelli, durrett_ch1_integrable_function`; new knowledge `exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini`.
- Exercise 1.7.5: method tags `fubini, tonelli, product-measure, layer-cake, stieltjes`; knowledge used `durrett_ch1_fubini_tonelli, durrett_ch1_integrable_function, durrett_ch1_dominated_convergence`; new knowledge `exercise_method_layer_cake_formula, exercise_method_stieltjes_integration_by_parts_with_jumps, exercise_method_interval_sliding_fubini, exercise_method_sine_integral_fubini`.

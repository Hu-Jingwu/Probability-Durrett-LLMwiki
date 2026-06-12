# Chapter 1 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter1/Chapter1Exercises.tex`
Source PDF: `Probability/Exercises/Chapter1/Chapter1Exercises.pdf`

This dataset turns the solved Chapter 1 exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.

## Files

- `chapter1_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.
- `chapter1_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter1_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter1_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.
- `chapter1_exercise_viki.md`: human-readable overview.
- `manifest.json`: dataset metadata.

## Section Method Cards

### 1.1 - Probability spaces, sigma-fields, generators, and set algebras

Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.

Tags: sigma-field, generator, set-counterexample, measure-foundations

### 1.2 - Distributions, normal tails, transformations, and density calculations

Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.

Tags: cdf, density-transform, normal-tail, probability-integral-transform

### 1.3 - Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization

Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.

Tags: measurability, generators, semicontinuity, sigma-x-factorization

### 1.4 - Lebesgue integration construction and approximation

Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.

Tags: lebesgue-integral, simple-approximation, l1-approximation, riemann-lebesgue

### 1.5 - Lp inequalities, convergence theorems, and absolute continuity of the integral

Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.

Tags: lp, holder, minkowski, mct, dct, absolute-continuity

### 1.6 - Expectation, Jensen/Chebyshev, moment bounds, and expectation limits

Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.

Tags: expectation, jensen, chebyshev, moment-bound, mct, dct

### 1.7 - Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration

Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.

Tags: fubini, tonelli, product-measure, layer-cake, stieltjes

## New Knowledge Pieces

### Countable/co-countable probability measure

- ID: `exercise_method_countable_cocountable_measure`
- Kind: exercise-derived-method
- Summary: To verify the countable/co-countable construction, split disjoint families into the cases where all sets are countable or exactly one set is co-countable.
- Use case: Exercise 1.1.1 and any probability-space verification on unusual sigma-fields.
- Tags: probability-space, countable-additivity, co-countable

### Borel sigma-field from half-open rectangles

- ID: `exercise_method_borel_generated_by_half_open_rectangles`
- Kind: exercise-derived-method
- Summary: Show half-open rectangles are Borel, then express rational open rectangles as countable unions of half-open rectangles; use the countable rational base.
- Use case: Exercises 1.1.2 and 1.1.3; product-measure generation arguments.
- Tags: borel, generator, rectangles

### Increasing union of sigma-fields can fail countable closure

- ID: `exercise_method_increasing_sigma_fields_not_sigma_field`
- Kind: counterexample-template
- Summary: Use finite initial-coordinate sigma-fields on N; their union contains every finite set but misses an infinite non-cofinite set such as the evens.
- Use case: Exercise 1.1.4; distinguishing algebras from sigma-fields.
- Tags: sigma-field, algebra, counterexample

### Block construction for asymptotic density counterexamples

- ID: `exercise_method_asymptotic_density_block_counterexample`
- Kind: counterexample-template
- Summary: Use rapidly growing blocks so the latest block dominates all previous blocks; alternate behavior by blocks to destroy the density of intersections.
- Use case: Exercise 1.1.5 and density/limit counterexamples.
- Tags: asymptotic-density, counterexample, blocks

### Piecewise random variable measurability

- ID: `exercise_method_piecewise_random_variable_measurability`
- Kind: proof-template
- Summary: For Z = X on A and Y on A^c, write {Z <= x} as (A cap {X <= x}) union (A^c cap {Y <= x}).
- Use case: Exercise 1.2.1; patching random variables on measurable events.
- Tags: measurability, piecewise, random-variable

### Countability of CDF jumps

- ID: `exercise_method_countable_cdf_discontinuities`
- Kind: proof-template
- Summary: Group jumps by size bigger than 1/m inside bounded intervals; each group is finite because total CDF increase is at most one.
- Use case: Exercise 1.2.3; monotone-function discontinuity arguments.
- Tags: cdf, jumps, countability

### Monotone density change of variables

- ID: `exercise_method_density_change_of_variables`
- Kind: calculation-template
- Summary: For Y=g(X) with g increasing, compute F_Y(y)=P(X <= g^{-1}(y)) and differentiate to get f_X(g^{-1}(y))/g'(g^{-1}(y)).
- Use case: Exercises 1.2.5 and 1.2.6; lognormal and affine density transforms.
- Tags: density, change-of-variables, cdf

### Density of a square transform

- ID: `exercise_method_square_transform_density`
- Kind: calculation-template
- Summary: For Y=X^2, use F_Y(y)=P(-sqrt(y)<=X<=sqrt(y)) and differentiate to get [f(sqrt(y))+f(-sqrt(y))]/(2sqrt(y)).
- Use case: Exercise 1.2.7; chi-square with one degree of freedom.
- Tags: density, chi-square, transformation

### Rational cut proof for sum measurability

- ID: `exercise_method_rational_cut_sum_measurability`
- Kind: proof-template
- Summary: Write {X+Y<x} as the countable union over q in Q of {X<q} cap {Y<x-q}.
- Use case: Exercise 1.3.2; direct measurability of sums.
- Tags: measurability, rationals, sum

### Lower semicontinuity via closed sublevel sets

- ID: `exercise_method_closed_sublevel_semicontinuity`
- Kind: proof-template
- Summary: A function is lower semicontinuous iff all sets {f <= a} are closed; sequential closure proves one direction and contradiction via subsequences proves the other.
- Use case: Exercise 1.3.5; proving semicontinuous functions are measurable.
- Tags: semicontinuity, closed-sets, measurability

### Discontinuity set from upper and lower local envelopes

- ID: `exercise_method_oscillation_discontinuity_set`
- Kind: proof-template
- Summary: Define local sup and inf over balls, take limits as radius decreases, and identify discontinuities as the set where the limiting envelopes differ.
- Use case: Exercise 1.3.6; measurability of discontinuity sets.
- Tags: discontinuity, oscillation, measurability

### Constructive representation of sigma(X)-measurable functions

- ID: `exercise_method_constructive_sigma_x_representation`
- Kind: proof-template
- Summary: Quantize Y into dyadic bins, represent each bin as {X in B}, build Borel simple functions f_n, then take a measurable pointwise limit f with Y=f(X).
- Use case: Exercises 1.3.8 and 1.3.9; conditional-expectation foundations.
- Tags: sigma-x, factorization, dyadic-approximation

### Zero integral of nonnegative function implies zero a.e.

- ID: `exercise_method_zero_integral_nonnegative`
- Kind: proof-template
- Summary: Use sets {f > 1/n}; each has zero measure because integral dominates (1/n) times its measure, and their union is {f>0}.
- Use case: Exercise 1.4.1; null-set proofs.
- Tags: nonnegative, zero-integral, a-e

### Dyadic lower simple approximations

- ID: `exercise_method_dyadic_lower_integral_approximation`
- Kind: calculation-template
- Summary: Approximate f>=0 by 2^{-n} floor(2^n f); the approximants increase to f and their integrals give monotone sums over dyadic level sets.
- Use case: Exercise 1.4.2 and simple-function approximation.
- Tags: dyadic, simple-functions, mct

### L1 approximation by continuous functions

- ID: `exercise_method_l1_continuous_approximation`
- Kind: proof-template
- Summary: Approximate an integrable function by simple functions, approximate measurable sets by finite interval unions, then round step-function corners.
- Use case: Exercise 1.4.3; density of nice functions in L1 on R.
- Tags: l1, approximation, continuous-functions

### Riemann-Lebesgue by step-function reduction

- ID: `exercise_method_riemann_lebesgue_step_reduction`
- Kind: proof-template
- Summary: Prove oscillatory integral decay for interval indicators explicitly, then approximate any L1 function by a step function.
- Use case: Exercise 1.4.4; oscillatory integral estimates.
- Tags: riemann-lebesgue, step-functions, oscillation

### Essential supremum bounds integrals

- ID: `exercise_method_essential_supremum_bound`
- Kind: proof-template
- Summary: If |g| <= ||g||_infty a.e., then |fg| <= ||g||_infty |f| and integration gives the L1-Linfty Holder endpoint.
- Use case: Exercise 1.5.1; endpoint Holder inequalities.
- Tags: essential-supremum, holder, linfty

### Lp norms converge to Linfty on probability spaces

- ID: `exercise_method_lp_to_l_infty_limit`
- Kind: proof-template
- Summary: Upper bound by essential supremum; lower bound using sets where |f| exceeds M-epsilon and their positive probability.
- Use case: Exercise 1.5.2; norm comparisons.
- Tags: lp, linfty, probability-space

### Simple functions are dense in Lp

- ID: `exercise_method_density_of_simple_functions_in_lp`
- Kind: proof-template
- Summary: Use pointwise simple approximations bounded by |f|, then dominated convergence on |phi_n-f|^p.
- Use case: Exercise 1.5.9; Lp approximation.
- Tags: lp, simple-functions, dct

### Exchange integral and absolutely summable series

- ID: `exercise_method_absolute_summability_exchange`
- Kind: proof-template
- Summary: If sum integral |f_n| is finite, then H=sum |f_n| is integrable; dominated convergence applies to partial sums.
- Use case: Exercise 1.5.10 and 1.7.1 corollary.
- Tags: series, dct, absolute-convergence

### Equality case in strict Jensen

- ID: `exercise_method_strict_jensen_equality`
- Kind: proof-template
- Summary: For strictly convex phi, equality in Jensen forces the random variable to be almost surely constant at its mean.
- Use case: Exercise 1.6.1; strict convexity equality cases.
- Tags: jensen, strict-convexity, equality-case

### Two-point distributions as Chebyshev extremizers

- ID: `exercise_method_two_point_extremizers`
- Kind: counterexample-template
- Summary: To prove sharpness of moment/tail inequalities, place small mass at boundary points and the rest at a value chosen to match moments.
- Use case: Exercises 1.6.3, 1.6.4, and 1.6.5.
- Tags: chebyshev, sharpness, two-point

### Cauchy-Schwarz lower bound for positive probability

- ID: `exercise_method_paley_zygmund_basic`
- Kind: inequality-template
- Summary: For Y>=0, Cauchy-Schwarz applied to Y*1_{Y>0} yields P(Y>0) >= (EY)^2/EY^2.
- Use case: Exercise 1.6.6; basic Paley-Zygmund-style estimates.
- Tags: cauchy-schwarz, lower-bound, paley-zygmund

### Tail truncation for expectation limits

- ID: `exercise_method_expectation_tail_truncation`
- Kind: proof-template
- Summary: Control small or large tails by splitting the event and using continuity of probability plus elementary bounds on the integrand.
- Use case: Exercise 1.6.14; limits involving y E(1/X; X>y).
- Tags: tail, truncation, expectation

### Indicator expansion for inclusion-exclusion and Bonferroni

- ID: `exercise_method_inclusion_exclusion_indicators`
- Kind: proof-template
- Summary: Use 1_union = 1 - product_i(1-1_Ai), expand, and take expectations; partial alternating sums give Bonferroni bounds.
- Use case: Exercises 1.6.9 and 1.6.10.
- Tags: inclusion-exclusion, bonferroni, indicators

### Layer-cake formula via product sets

- ID: `exercise_method_layer_cake_formula`
- Kind: proof-template
- Summary: Represent g(x) as the vertical length of {(x,y):0 <= y < g(x)} and apply Tonelli to integrate sections.
- Use case: Exercise 1.7.2; tail integrals for nonnegative functions.
- Tags: layer-cake, tonelli, tail-integral

### Stieltjes integration by parts with jump correction

- ID: `exercise_method_stieltjes_integration_by_parts_with_jumps`
- Kind: proof-template
- Summary: Interpret Stieltjes integrals as product-measure masses of order regions; the diagonal overlap contributes the product of jump masses.
- Use case: Exercise 1.7.3.
- Tags: stieltjes, integration-by-parts, jumps

### Sliding interval Fubini identity

- ID: `exercise_method_interval_sliding_fubini`
- Kind: calculation-template
- Summary: Write F(x+c)-F(x) as mu((x,x+c]), swap integrals, and observe each fixed t is counted for exactly c units of x.
- Use case: Exercise 1.7.4.
- Tags: fubini, distribution-function, sliding-window

### Sine integral via Fubini

- ID: `exercise_method_sine_integral_fubini`
- Kind: calculation-template
- Summary: Represent sin(x)/x as an integral of e^{-xy} sin(x), integrate in x first, and bound the remaining exponentially damped tails.
- Use case: Exercise 1.7.5.
- Tags: fubini, sine-integral, oscillatory-integral

# Chapter 7 Exercise Viki Dataset

Source TeX: `Probability/Exercises/Chapter7/Chapter7Exercises.tex`
Source PDF: `Probability/Exercises/Chapter7/Chapter7Exercises.pdf`

This dataset turns the solved Chapter 7 Brownian motion exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.

## Files

- `chapter7_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.
- `chapter7_exercise_method_cards.jsonl`: section-level method summaries.
- `chapter7_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.
- `chapter7_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.
- `chapter7_exercise_viki.md`: human-readable overview.
- `manifest.json`: dataset metadata.

## Section Method Cards

### 7.1 - Brownian construction, Gaussian calculations, path roughness, and quadratic variation

Reduce finite-dimensional Brownian questions to independent Gaussian increments; use rotational normal geometry, Gaussian linear functionals, small-increment estimates, and Borel-Cantelli for path regularity.

Tags: brownian-definition, gaussian-increments, holder, quadratic-variation

### 7.2 - Markov property, Blumenthal 0-1 law, immediate behavior, and recurrence patterns

Condition on Brownian position at a deterministic time, translate future hitting events into fresh Brownian probabilities, and use germ 0-1 laws to upgrade positive-probability local behavior to almost sure behavior.

Tags: markov-property, blumenthal, germ-field, recurrence

### 7.3 - Stopping-time closure and stopped sigma-fields

Prove stopping-time claims by rewriting events with countable unions over rational times, use open/closed hitting-time facts, and apply the definition of F_S through restrictions to {S <= t}.

Tags: stopping-times, stopped-sigma-field, rational-time, closure-properties

### 7.4 - Brownian path properties, reflection, hitting-time densities, and arcsine-type laws

Combine strong Markov, reflection, hitting-time densities, and conditioning at fixed times to compute distributions of returns, maxima, endpoints, and zero-set events.

Tags: reflection-principle, hitting-times, cauchy, zero-set, arcsine

### 7.5 - Brownian martingales, optional stopping, exit transforms, and moment computations

Choose martingales tailored to the target: cosh/exponential martingales for Laplace transforms, heat-polynomial martingales for exit moments, and maximal inequalities for almost-sure growth bounds.

Tags: martingales, optional-stopping, laplace-transform, exit-times, polynomial-martingales

### 7.6 - Ito formula, stochastic integral martingales, and Brownian moment/radial identities

Apply one-dimensional, time-space, and multidimensional Ito formulas; identify drift terms, turn zero drift into martingales, and take expectations to get moment recursions.

Tags: ito-formula, stochastic-integral, moments, radial-process, bessel

## New Knowledge Pieces

### Two-time Brownian sign probability by Gaussian wedge angle

- ID: `exercise_method_ch7_gaussian_wedge_probability`
- Kind: calculation-template
- Summary: Write B_t as B_s plus an independent increment, standardize to a rotationally symmetric bivariate normal, and compute the sector angle cut out by the two half-planes.
- Use case: Exercise 7.1.1; probabilities involving signs of correlated Brownian values.
- Tags: brownian, gaussian-geometry, sign-probability

### Brownian polynomial moments by independent increment expansion

- ID: `exercise_method_ch7_increment_expansion_moments`
- Kind: calculation-template
- Summary: Represent B_1, B_2, B_3 through independent unit Gaussian increments, expand the polynomial, and discard terms with centered odd factors.
- Use case: Exercise 7.1.2; low-order Brownian moment computations.
- Tags: brownian-moments, independent-increments, gaussian

### Deterministic Brownian integrals are Gaussian

- ID: `exercise_method_ch7_brownian_integral_gaussian`
- Kind: calculation-template
- Summary: Approximate an integral of B_s against deterministic ds by Riemann sums; each sum is Gaussian, and the variance is the double integral of r wedge s.
- Use case: Exercise 7.1.3; integrated Brownian motion and Gaussian linear functionals.
- Tags: gaussian-process, brownian-integral, covariance

### Events in raw path sigma-field depend on countably many coordinates

- ID: `exercise_method_ch7_countable_coordinate_sigma_field`
- Kind: proof-template
- Summary: Show the class of events depending on a countable coordinate list is a sigma-field containing all finite-dimensional cylinders.
- Use case: Exercise 7.1.4; path-space measurability and cylinder sigma-fields.
- Tags: path-space, sigma-field, coordinates

### K-increment obstruction to Brownian Holder regularity

- ID: `exercise_method_ch7_k_increment_holder_obstruction`
- Kind: proof-template
- Summary: If a Holder point exists, a nearby block of k Gaussian increments must all be unusually small; union bound gives probability O(n^{1+k(1/2-gamma)}).
- Use case: Exercise 7.1.5; proving no Holder points above exponent 1/2.
- Tags: holder, small-increments, brownian-roughness

### Dyadic quadratic variation by L2 plus Borel-Cantelli

- ID: `exercise_method_ch7_dyadic_quadratic_variation_borel_cantelli`
- Kind: proof-template
- Summary: Compute variance of the dyadic squared-increment sum as 2t^2 2^{-n}, apply Chebyshev, and sum over n to get almost sure convergence.
- Use case: Exercise 7.1.6; Brownian quadratic variation along dyadic partitions.
- Tags: quadratic-variation, borel-cantelli, chebyshev

### Deterministic-time Markov conditioning for hitting survival

- ID: `exercise_method_ch7_markov_conditioning_hitting_survival`
- Kind: proof-template
- Summary: Condition on B_s=y, replace the future event by a hitting probability for Brownian motion started at y, and integrate against the transition density.
- Use case: Exercises 7.2.1 and 7.2.2; return-time and last-zero decompositions.
- Tags: markov-property, hitting-time, transition-density

### Last-zero event as no future hit after conditioning

- ID: `exercise_method_ch7_last_zero_markov_decomposition`
- Kind: calculation-template
- Summary: The event L <= t is equivalent to no zero in (t,1]; after conditioning on B_t, this becomes P_y(T_0 > 1-t).
- Use case: Exercise 7.2.2 and arcsine-law calculations.
- Tags: last-zero, markov-property, survival-probability

### Dense local maxima from immediate two-sided crossing

- ID: `exercise_method_ch7_dense_local_maxima_from_immediate_crossing`
- Kind: proof-template
- Summary: Take shrinking deterministic intervals, use continuity to get a maximum, and use immediate crossing forward and backward to rule out endpoints.
- Use case: Exercise 7.2.3; path-local extremum arguments.
- Tags: local-maxima, immediate-crossing, brownian-paths

### Germ-field limsup constants via Blumenthal 0-1

- ID: `exercise_method_ch7_germ_limsup_constant`
- Kind: proof-template
- Summary: For a small-time limsup L, events {L <= r} lie in the germ sigma-field; 0-1 probabilities force L to be almost surely constant.
- Use case: Exercise 7.2.4(i); local Brownian growth rates.
- Tags: blumenthal, limsup, germ-field

### Brownian paths are not 1/2-Holder at a fixed time

- ID: `exercise_method_ch7_sqrt_time_not_holder_half`
- Kind: proof-template
- Summary: Use B_delta/sqrt(delta) standard normal to get positive probability of arbitrarily large normalized values, then apply Blumenthal 0-1.
- Use case: Exercise 7.2.4(ii); critical Brownian Holder exponent.
- Tags: holder, blumenthal, sqrt-time

### F-sigma hitting times as infima of closed hitting times

- ID: `exercise_method_ch7_fsigma_hitting_time`
- Kind: proof-template
- Summary: Write the F-sigma set as a countable union of closed sets, use closed-set hitting times, and express {inf T_n < t} as a countable union.
- Use case: Exercise 7.3.1; proving first-entry times are stopping times.
- Tags: stopping-time, hitting-time, f-sigma

### Sum of stopping times via rational split

- ID: `exercise_method_ch7_sum_stopping_time_rational_split`
- Kind: proof-template
- Summary: Write {S+T<t} as the union over rational q<t of {S<q} cap {T<t-q}.
- Use case: Exercise 7.3.2; closure properties for stopping times.
- Tags: stopping-time, rationals, closure

### Supremum and infimum of stopping times

- ID: `exercise_method_ch7_sup_inf_stopping_times`
- Kind: proof-template
- Summary: Use {inf T_n<t}=union {T_n<t} and {sup T_n<=t}=intersection {T_n<=t}, then build liminf and limsup from sup/inf combinations.
- Use case: Exercise 7.3.3; stopping-time sequence operations.
- Tags: stopping-time, supremum, infimum

### Use F_S by restricting to {S <= t}

- ID: `exercise_method_ch7_stopped_event_restriction`
- Kind: proof-template
- Summary: To prove an event-defined random time is a stopping time, intersect the event A in F_S with {S <= t} and use the definition of F_S.
- Use case: Exercise 7.3.4; killing a stopping time on an event.
- Tags: stopped-sigma-field, stopping-time, restriction

### Comparison events for stopping times are known at either time

- ID: `exercise_method_ch7_compare_stopping_times_in_stopped_fields`
- Kind: proof-template
- Summary: Represent {S<T} or {S>T} on {S<t} using countable rational cuts, then repeat with S and T interchanged.
- Use case: Exercise 7.3.5; stopped sigma-field comparison events.
- Tags: stopped-sigma-field, rational-cuts, comparison

### Stopped sigma-field at S wedge T

- ID: `exercise_method_ch7_meet_stopped_sigma_field`
- Kind: proof-template
- Summary: Use S wedge T <= S,T for one inclusion; for the reverse, decompose A cap {S wedge T <= t} into the union of A cap {S <= t} and A cap {T <= t}.
- Use case: Exercise 7.3.6; identities among stopped sigma-fields.
- Tags: stopped-sigma-field, minimum, filtration

### Planar Brownian level hitting gives Cauchy law

- ID: `exercise_method_ch7_planar_hitting_cauchy`
- Kind: calculation-template
- Summary: Condition the first coordinate on the second-coordinate hitting time, then use the hitting-time Laplace transform to get characteristic function exp(-a|u|).
- Use case: Exercise 7.4.1; Cauchy distribution from Brownian hitting.
- Tags: cauchy, planar-brownian, hitting-time

### Return-time density by mixing first-hit densities

- ID: `exercise_method_ch7_return_time_density_mixture`
- Kind: calculation-template
- Summary: Condition on B_1=y and integrate the first-hitting density from y to 0 against the N(0,1) density.
- Use case: Exercise 7.4.2; density of the next zero after time 1.
- Tags: return-time, density, markov-property

### Endpoint subdensity after barrier crossing

- ID: `exercise_method_ch7_reflected_endpoint_subdensity`
- Kind: calculation-template
- Summary: Reflect paths after the first hit of level a to identify P(T_a<t, B_t in dx) below a with the free Brownian density at 2a-x.
- Use case: Exercise 7.4.3(a,b); reflection-principle refinements.
- Tags: reflection-principle, subdensity, barrier

### Joint density of Brownian maximum and endpoint

- ID: `exercise_method_ch7_joint_max_endpoint_density`
- Kind: calculation-template
- Summary: Use {M_t>a}={T_a<t}, write the reflected endpoint subdensity, and differentiate the tail probability in the maximum level a.
- Use case: Exercise 7.4.3(c); Brownian maximum-endpoint joint law.
- Tags: maximum, joint-density, reflection

### Zero-in-interval probability by hitting-time density integral

- ID: `exercise_method_ch7_zero_interval_arccos_integral`
- Kind: calculation-template
- Summary: Condition on B_s, integrate the first-hit density over [0,t-s], swap integrals, and use u=sqrt(r/s) to get an arccos formula.
- Use case: Exercise 7.4.4; zero-set interval probabilities.
- Tags: zero-set, hitting-density, arccos

### Cosh martingale for symmetric interval exit Laplace transforms

- ID: `exercise_method_ch7_cosh_martingale_exit_laplace`
- Kind: calculation-template
- Summary: Average the plus and minus exponential Brownian martingales to get e^{-lambda t} cosh(sqrt(2lambda) B_t), then stop at +/-a.
- Use case: Exercise 7.5.1; symmetric two-sided exit transform.
- Tags: cosh, exponential-martingale, exit-time

### Drifted Brownian hitting via exponential martingale

- ID: `exercise_method_ch7_drift_hitting_exponential_martingale`
- Kind: calculation-template
- Summary: Choose theta solving theta^2/2 - b theta = lambda, stop exp(theta B_t - theta^2 t/2) at the linear boundary hitting time, and let the cutoff go to infinity.
- Use case: Exercise 7.5.2; Brownian motion with drift hitting a level.
- Tags: drift, hitting-time, exponential-martingale

### Interval exit Laplace transforms from strong Markov linear equations

- ID: `exercise_method_ch7_interval_exit_laplace_linear_system`
- Kind: calculation-template
- Summary: Decompose one-sided hitting transforms by whether the interval exit occurs at a or b, then solve the two equations using exp(-sqrt(2lambda) distance).
- Use case: Exercise 7.5.3; killed Brownian exit transforms.
- Tags: strong-markov, laplace-transform, linear-system

### Exit-moment comparison using Cauchy-Schwarz

- ID: `exercise_method_ch7_cauchy_schwarz_exit_moment_comparison`
- Kind: inequality-template
- Summary: Stop the fourth-degree Brownian polynomial martingale, then bound E(T B_T^2) by sqrt(E T^2) sqrt(E B_T^4).
- Use case: Exercise 7.5.4; nonsymmetric interval exit moments.
- Tags: cauchy-schwarz, exit-time, polynomial-martingale

### Sixth-degree heat polynomial for third exit-time moment

- ID: `exercise_method_ch7_sixth_degree_exit_moment`
- Kind: calculation-template
- Summary: Solve u_t+u_xx/2=0 for x^6-c1 t x^4+c2 t^2 x^2-c3 t^3, stop at +/-a, and insert lower exit moments.
- Use case: Exercise 7.5.5; higher moments of symmetric Brownian exit times.
- Tags: polynomial-martingale, exit-time-moments, heat-equation

### Exponential-square martingale plus maximal inequality

- ID: `exercise_method_ch7_exponential_square_maximal_borel_cantelli`
- Kind: proof-template
- Summary: Use (1+t)^(-1/2) exp(B_t^2/(2(1+t))) as a positive martingale, apply Doob over exponential time blocks, and sum probabilities.
- Use case: Exercise 7.5.6; almost-sure Brownian growth upper bounds.
- Tags: maximal-inequality, borel-cantelli, growth-bound

### Ito drift test for f(B_t) martingales

- ID: `exercise_method_ch7_ito_affine_martingale_characterization`
- Kind: proof-template
- Summary: Ito's formula shows f(B_t) has drift (1/2)f''(B_t)dt; martingality forces the finite-variation drift to vanish, hence f''=0.
- Use case: Exercise 7.6.1; characterizing functions of Brownian motion that are martingales.
- Tags: ito-formula, martingale, affine

### Cubic Brownian martingales from Ito formula

- ID: `exercise_method_ch7_cubic_ito_martingales`
- Kind: calculation-template
- Summary: Use u(t,x)=x^3-3tx for a time-space martingale, or apply Ito to x^3 and subtract the drift integral.
- Use case: Exercise 7.6.2; polynomial Brownian martingales.
- Tags: ito-formula, cubic, polynomial-martingale

### Even Brownian moments by Ito recursion

- ID: `exercise_method_ch7_even_moment_ito_recursion`
- Kind: calculation-template
- Summary: Apply Ito to x^{2k}, take expectations, and solve beta_{2k}'(t)=k(2k-1) beta_{2k-2}(t) with beta_0=1.
- Use case: Exercise 7.6.3; deriving Gaussian even moments.
- Tags: moments, ito-formula, gaussian

### Radial Brownian Ito formula and Bessel drift

- ID: `exercise_method_ch7_radial_ito_bessel_form`
- Kind: calculation-template
- Summary: Approximate |x| near 0, use gradient x/|x| and Laplacian (d-1)/|x| away from 0, and identify the radial martingale part.
- Use case: Exercise 7.6.4; radial Brownian motion and Bessel processes.
- Tags: radial-process, bessel, multidimensional-ito

### Squared Brownian norm has dimension drift

- ID: `exercise_method_ch7_squared_norm_ito_dimension_drift`
- Kind: calculation-template
- Summary: Apply multidimensional Ito to |x|^2; the martingale part is 2 sum_i int B_s^i dB_s^i and the drift is d t.
- Use case: Exercise 7.6.5; computing E|B_t|^2 in R^d.
- Tags: multidimensional-ito, second-moment, dimension

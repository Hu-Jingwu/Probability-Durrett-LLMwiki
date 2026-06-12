# Durrett Chapter 7 LLM Viki: Brownian Motion

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter7.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

## Section Guides

### 7.1 Definition and Construction

- Goal: Define Brownian motion rigorously, construct it, and understand the first layer of path regularity.

- Must master: independent Gaussian increments, Brownian scaling, Gaussian covariance characterization, Kolmogorov continuity criterion, Holder continuity below 1/2, nowhere differentiability, quadratic variation intuition

- Prelim angle: This section supplies the definitions and scaling heuristics behind nearly every Brownian calculation.

### 7.2 Markov Property, Blumenthal's 0-1 Law

- Goal: Restart Brownian motion at deterministic times and use 0-1 laws for immediate and tail behavior.

- Must master: Markov property, Blumenthal 0-1 law, immediate hitting, time inversion, tail 0-1 law, one-dimensional recurrence

- Prelim angle: These tools turn qualitative path behavior into short rigorous arguments.

### 7.3 Stopping Times, Strong Markov Property

- Goal: Formalize random times and prove that Brownian motion can be restarted at them.

- Must master: stopping time definitions, hitting times of open and closed sets, F_S, B_S measurability, strong Markov property

- Prelim angle: Most Brownian hitting-time and reflection-principle problems depend on this section.

### 7.4 Path Properties

- Goal: Use strong Markov arguments to analyze zeros, first passage times, reflection, and arcsine laws.

- Must master: zero set structure, hitting-time increments, hitting-time scaling, reflection principle, first-passage density, arcsine law

- Prelim angle: This section is the computational core for Brownian maxima and barrier-crossing questions.

### 7.5 Martingales

- Goal: Use Brownian martingales and optional stopping to compute exit probabilities, exit times, and Laplace transforms.

- Must master: optional stopping, B_t martingale, B_t^2-t martingale, exponential martingale, heat-equation martingales, exit-time formulas

- Prelim angle: The fastest route to most exact Brownian interval and hitting-time computations.

### 7.6 Ito's Formula*

- Goal: Replace ordinary calculus with Ito calculus for Brownian paths and connect stochastic calculus to PDE/martingale methods.

- Must master: one-dimensional Ito formula, stochastic integral martingale property, time-space Ito formula, exponential Brownian motion, multidimensional Ito formula

- Prelim angle: Even if starred, Ito's formula explains why Brownian martingales and heat equations fit together.

## Knowledge Pieces

### Brownian motion definition

- ID: `durrett_ch7_brownian_definition`

- Section: 7.1 Definition and Construction

- Kind: definition

- Summary: A Brownian motion has independent increments, Gaussian increments B(s+t)-B(s) with mean 0 and variance t, and almost surely continuous sample paths.

- Proof idea: The definition encodes CLT scaling for small displacements while adding continuity to rule out arbitrary versions with the same finite-dimensional laws.

- Exam use: Use as the base checklist whenever a process is claimed to be Brownian.

- Pitfall: Independent Gaussian increments alone do not automatically give continuous paths unless a continuous modification is specified.

- Tags: brownian-motion, gaussian-increments, continuous-paths

### Translation invariance of increments

- ID: `durrett_ch7_translation_invariance`

- Section: 7.1 Definition and Construction

- Kind: fact

- Summary: The process {B_t-B_0:t>=0} is independent of B_0 and has the law of Brownian motion started at 0.

- Proof idea: Use independence of the initial value and subsequent increments, then extend from finite-dimensional cylinder events by a pi-lambda argument.

- Exam use: Lets hitting and exit calculations reduce to a Brownian motion started at 0 or at the current location.

- Pitfall: This is spatial translation of the starting point, not time-shift Markov conditioning.

- Tags: translation-invariance, increments, starting-point

### Brownian scaling

- ID: `durrett_ch7_brownian_scaling`

- Section: 7.1 Definition and Construction

- Kind: formula

- Summary: For c>0 and B_0=0, {B_{cs}:s>=0} has the same finite-dimensional distributions as {sqrt(c) B_s:s>=0}.

- Proof idea: Check the one-dimensional normal variance and then use independent increments for all finite-dimensional distributions.

- Exam use: High-yield tool for hitting-time laws, path regularity, and rescaling exit probabilities.

- Pitfall: Scaling changes time by c and space by sqrt(c); reversing these powers is a common error.

- Tags: scaling, self-similarity, finite-dimensional-distributions

### Gaussian process characterization

- ID: `durrett_ch7_gaussian_process_characterization`

- Section: 7.1 Definition and Construction

- Kind: theorem

- Summary: A continuous Gaussian process with mean 0 and covariance E[B_s B_t]=s wedge t is Brownian motion started at 0.

- Proof idea: The covariance matrix determines all finite-dimensional Gaussian laws and matches the independent-increment construction.

- Exam use: Use to prove transformed processes are Brownian, especially time inversion.

- Pitfall: The covariance condition alone is not enough without the Gaussian finite-dimensional law and continuity.

- Tags: gaussian-process, covariance, characterization

### Kolmogorov extension construction

- ID: `durrett_ch7_kolmogorov_extension_construction`

- Section: 7.1 Definition and Construction

- Kind: construction

- Summary: Brownian finite-dimensional distributions are built from Gaussian transition densities and then extended consistently to a path-space probability law.

- Proof idea: Verify consistency of the transition-density integrals and apply Kolmogorov extension; then move to continuous paths through a modification/extension argument.

- Exam use: Explains why the formal process exists before path properties are studied.

- Pitfall: The raw product path space can make continuity nonmeasurable; the continuous-path space fixes the measurable model.

- Tags: construction, kolmogorov-extension, transition-density

### Kolmogorov continuity criterion

- ID: `durrett_ch7_kolmogorov_continuity_criterion`

- Section: 7.1 Definition and Construction

- Kind: theorem

- Summary: If E|X_t-X_s|^beta <= K|t-s|^{1+alpha}, then dyadic paths admit a Holder-continuous version of any exponent gamma<alpha/beta.

- Proof idea: Control dyadic increments by Chebyshev and Borel-Cantelli, then chain dyadic intervals to bound arbitrary dyadic pairs.

- Exam use: Use moment bounds to prove sample-path continuity for Gaussian and process constructions.

- Pitfall: The exponent comes from alpha/beta, not beta/alpha; endpoint exponents are usually not obtained.

- Tags: kolmogorov-continuity, holder, borel-cantelli

### Brownian Holder continuity below one half

- ID: `durrett_ch7_brownian_holder_half`

- Section: 7.1 Definition and Construction

- Kind: theorem

- Summary: Brownian paths are almost surely Holder continuous on compact intervals for every exponent gamma<1/2.

- Proof idea: Use Gaussian even moments E|B_t-B_s|^{2m}=C_m|t-s|^m in the Kolmogorov criterion and let m grow.

- Exam use: Useful for justifying pathwise approximations while remembering Brownian paths are rough.

- Pitfall: The exponent 1/2 itself is not included.

- Tags: holder, path-regularity, gaussian-moments

- Related: `durrett_ch7_kolmogorov_continuity_criterion`

### Brownian paths are nowhere differentiable

- ID: `durrett_ch7_brownian_nowhere_differentiable`

- Section: 7.1 Definition and Construction

- Kind: theorem

- Summary: With probability one, Brownian paths are not Lipschitz continuous, and hence not differentiable, at any time.

- Proof idea: If a path were locally Lipschitz, several nearby small increments would all be tiny; Gaussian small-ball estimates make this probability vanish after covering.

- Exam use: Prevents calculus-style manipulation of B_t and motivates quadratic variation and Ito calculus.

- Pitfall: Continuity does not imply bounded variation or differentiability; Brownian paths are continuous but very rough.

- Tags: nondifferentiability, rough-paths, path-regularity

- Related: `durrett_ch7_brownian_holder_half`

### Dyadic quadratic variation

- ID: `durrett_ch7_quadratic_variation_hint`

- Section: 7.1 Definition and Construction

- Kind: fact

- Summary: Along dyadic partitions of [0,t], the sum of squared Brownian increments converges to t in the sense used later for Ito's formula.

- Proof idea: Independence and Gaussian fourth-moment estimates show the mean is t and the variance of the sum goes to 0.

- Exam use: Core intuition behind the extra (1/2)f'' term in Ito's formula.

- Pitfall: This is about squared increments; ordinary total variation behaves very differently.

- Tags: quadratic-variation, dyadic-partitions, ito

### Multidimensional Brownian motion

- ID: `durrett_ch7_d_dimensional_brownian`

- Section: 7.1 Definition and Construction

- Kind: definition

- Summary: A d-dimensional Brownian motion has independent one-dimensional Brownian coordinates and Gaussian transition density (2 pi t)^(-d/2) exp(-|y-x|^2/(2t)).

- Proof idea: Independence of coordinates factors the finite-dimensional distributions and gives the Euclidean Gaussian kernel.

- Exam use: Use for vector Ito formulas and multidimensional hitting or transition-density computations.

- Pitfall: Do not replace coordinate independence by merely matching each marginal coordinate law.

- Tags: multidimensional, transition-density, gaussian-kernel

### Brownian Markov property

- ID: `durrett_ch7_markov_property`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: Conditioned on the present, the shifted future of Brownian motion has the law of Brownian motion started from the current state and is independent of the past.

- Proof idea: Prove first for bounded cylinder functions of the future using Gaussian transition densities, then extend by the monotone class theorem.

- Exam use: Use to restart Brownian motion at deterministic times and compute conditional expectations.

- Pitfall: The conditioning sigma-field is the completed right-continuous past; using an informal past can hide null-set issues.

- Tags: markov-property, conditional-expectation, shift

### Right-continuous germ conditioning

- ID: `durrett_ch7_germ_field_equivalence`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: technical-fact

- Summary: For bounded path functionals, conditioning on F_s^+ agrees almost surely with conditioning on the raw past F_s^0.

- Proof idea: Approximate functionals by finite-dimensional ones and use the Markov property plus right-continuity of Brownian paths.

- Exam use: Clarifies why immediate-future events can be handled cleanly at time 0.

- Pitfall: This is an almost-sure equality of conditional expectations, not equality of all raw sigma-fields literally.

- Tags: germ-field, right-continuity, conditioning

### Blumenthal's 0-1 law

- ID: `durrett_ch7_blumenthal_zero_one`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: Every event in the Brownian germ sigma-field F_0^+ has probability 0 or 1 under a fixed starting point.

- Proof idea: Condition the event on the raw time-zero sigma-field, which is trivial once the starting point is fixed.

- Exam use: Use for immediate hitting, local oscillation, and path behavior as t downarrow 0.

- Pitfall: The probability may depend on the starting point; the law is not automatically uniform in x.

- Tags: zero-one-law, germ-field, local-behavior

### Immediate crossing at the origin

- ID: `durrett_ch7_immediate_positive_negative_hits`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: Starting from 0, Brownian motion hits (0,infinity), hits (-infinity,0), and returns to 0 immediately with probability one.

- Proof idea: Each event has positive probability at arbitrarily small times by normal symmetry; Blumenthal's law upgrades positive probability to probability one.

- Exam use: Useful when proving the zero set has no isolated points and when reasoning about local extrema.

- Pitfall: The return time is inf{t>0:B_t=0}; allowing t=0 would make the statement trivial.

- Tags: immediate-hitting, zero-set, blumenthal

- Related: `durrett_ch7_blumenthal_zero_one`

### Brownian time inversion

- ID: `durrett_ch7_time_inversion`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: If B starts at 0, then X_0=0 and X_t=t B_{1/t} for t>0 is again Brownian motion.

- Proof idea: Check Gaussian finite-dimensional distributions and covariance, then prove continuity at 0 from B_u/u -> 0 as u -> infinity.

- Exam use: Transfers small-time Brownian statements into large-time statements.

- Pitfall: The transform is t B_{1/t}, not B_{1/t}/t.

- Tags: time-inversion, gaussian-characterization, large-time

- Related: `durrett_ch7_gaussian_process_characterization`

### Brownian tail 0-1 law

- ID: `durrett_ch7_brownian_tail_zero_one`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: Events determined by the arbitrarily far future have probability identically 0 or identically 1 for all starting states.

- Proof idea: Time inversion turns a tail event into a germ event; the Markov property removes dependence on the starting point.

- Exam use: Use for recurrence and unbounded oscillation at infinity.

- Pitfall: This is stronger than the germ law because the conclusion is uniform in the starting state.

- Tags: tail-sigma-field, zero-one-law, time-inversion

- Related: `durrett_ch7_time_inversion`, `durrett_ch7_blumenthal_zero_one`

### Large-time oscillation

- ID: `durrett_ch7_limsup_liminf_unbounded`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: One-dimensional Brownian motion satisfies limsup B_t/sqrt(t)=infinity and liminf B_t/sqrt(t)=-infinity almost surely.

- Proof idea: Discrete times have positive probability of exceeding any fixed multiple of sqrt(n) infinitely often; the tail 0-1 law upgrades this to probability one.

- Exam use: Quick route to recurrence and repeated level-crossing arguments.

- Pitfall: This is weaker than the law of the iterated logarithm but enough for recurrence.

- Tags: oscillation, tail-zero-one, recurrence

- Related: `durrett_ch7_brownian_tail_zero_one`

### One-dimensional Brownian recurrence

- ID: `durrett_ch7_one_dimensional_recurrence`

- Section: 7.2 Markov Property, Blumenthal's 0-1 Law

- Kind: theorem

- Summary: For every starting point, one-dimensional Brownian motion hits 0 infinitely often at arbitrarily large times almost surely.

- Proof idea: Large positive and negative oscillations plus path continuity force repeated crossings of 0.

- Exam use: Use whenever hitting times of points are assumed finite or when restarting at returns.

- Pitfall: Recurrence in one dimension does not generalize unchanged to higher-dimensional hitting of points.

- Tags: recurrence, hitting, one-dimensional

- Related: `durrett_ch7_limsup_liminf_unbounded`

### Stopping time definition

- ID: `durrett_ch7_stopping_time_definition`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: definition

- Summary: A random time S is a stopping time when {S<t} is in F_t for every t; for right-continuous filtrations this is equivalent to using {S<=t}.

- Proof idea: The equivalence follows by countable unions/intersections and right-continuity of the filtration.

- Exam use: Use to verify that hitting, exit, minima, and approximating times are legitimate restart times.

- Pitfall: The definition is about information available by time t, not about whether S has a density or finite expectation.

- Tags: stopping-times, filtration, right-continuity

### Open and closed hitting times are stopping times

- ID: `durrett_ch7_hitting_times_open_closed`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: theorem

- Summary: For continuous Brownian paths, the first hitting time of an open set or a closed set is a stopping time.

- Proof idea: Open sets use rational times before t; closed sets are obtained as increasing limits of hitting times of shrinking open neighborhoods.

- Exam use: Use to justify applying strong Markov property to level hitting and interval exit times.

- Pitfall: For general Borel sets the statement is true but much harder; do not use the open/closed proof blindly.

- Tags: hitting-times, open-sets, closed-sets

- Related: `durrett_ch7_stopping_time_definition`

### Limits of stopping times

- ID: `durrett_ch7_stopping_time_limits`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: closure-property

- Summary: Increasing and decreasing limits of stopping times are stopping times in a right-continuous filtration.

- Proof idea: Write events for the limiting time as countable unions or intersections of the corresponding events for the approximating times.

- Exam use: Useful for proving complicated first-entry times by approximation.

- Pitfall: Right-continuity matters for some <= formulations.

- Tags: stopping-times, limits, approximation

### Random shift and information at a stopping time

- ID: `durrett_ch7_random_shift_and_F_S`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: definition

- Summary: The shift theta_S removes the path before S and restarts time at S; F_S contains events whose restriction to {S<=t} is F_t-measurable for every t.

- Proof idea: These definitions formalize what is known at a random time and how to view the post-S path.

- Exam use: Needed to state the strong Markov property and optional stopping cleanly.

- Pitfall: F_S is not simply F_t with t replaced by a random variable; it has its own measurability definition.

- Tags: random-shift, stopped-sigma-field, strong-markov

### Stopped value is known at the stopping time

- ID: `durrett_ch7_B_S_measurable`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: theorem

- Summary: If S is a stopping time, then B_S is F_S-measurable.

- Proof idea: Approximate S from above by dyadic stopping times, note each approximating value is measurable at the approximating time, and pass to the limit by path continuity.

- Exam use: Lets conditional expectations at stopping times depend on the random current position B_S.

- Pitfall: This uses continuity and the completed/right-continuous filtration setup.

- Tags: stopped-process, measurability, dyadic-approximation

### Strong Markov property

- ID: `durrett_ch7_strong_markov_property`

- Section: 7.3 Stopping Times, Strong Markov Property

- Kind: theorem

- Summary: Given a stopping time S, the post-S Brownian path conditioned on F_S has the law of Brownian motion started at B_S, on {S<infinity}.

- Proof idea: First prove it for discrete-valued stopping times, approximate a general S from above by dyadic stopping times, then extend by monotone class.

- Exam use: The central engine for reflection principle, hitting-time increments, recurrence refinements, and exit calculations.

- Pitfall: Always check S is a stopping time and restrict or control the event {S<infinity}.

- Tags: strong-markov, stopping-times, restart

- Related: `durrett_ch7_random_shift_and_F_S`, `durrett_ch7_B_S_measurable`

### Brownian zero set structure

- ID: `durrett_ch7_zero_set_structure`

- Section: 7.4 Path Properties

- Kind: fact

- Summary: The zero set of one-dimensional Brownian motion is almost surely closed, has no isolated points, is uncountable, and has Lebesgue measure zero.

- Proof idea: Continuity gives closedness; recurrence plus immediate return and strong Markov give no isolated zeros; Fubini gives zero Lebesgue measure.

- Exam use: Good conceptual anchor for path-property problems involving returns to zero.

- Pitfall: Uncountable does not imply positive Lebesgue measure.

- Tags: zero-set, perfect-set, measure-zero

- Related: `durrett_ch7_immediate_positive_negative_hits`, `durrett_ch7_strong_markov_property`

### Level hitting times have stationary independent increments

- ID: `durrett_ch7_hitting_time_subordinator`

- Section: 7.4 Path Properties

- Kind: theorem

- Summary: Under P_0, the process {T_a:a>=0}, where T_a=inf{t:B_t=a}, has stationary independent increments as a function of the level a.

- Proof idea: After hitting level a, the strong Markov property and translation invariance identify T_b-T_a with a fresh copy of T_{b-a}.

- Exam use: Use to recognize hitting times as a stable subordinator of index 1/2.

- Pitfall: The parameter is the spatial level a, not the Brownian time parameter.

- Tags: hitting-times, subordinator, stationary-independent-increments

- Related: `durrett_ch7_strong_markov_property`, `durrett_ch7_translation_invariance`

### Hitting-time scaling

- ID: `durrett_ch7_hitting_time_scaling`

- Section: 7.4 Path Properties

- Kind: formula

- Summary: For a>0, T_a has the same distribution as a^2 T_1.

- Proof idea: Apply Brownian scaling: hitting a in the original process corresponds to hitting 1 after rescaling space by a and time by a^2.

- Exam use: Quickly reduces level-dependent hitting-time questions to the case a=1.

- Pitfall: The square on a is essential; hitting times scale like distance squared.

- Tags: hitting-times, scaling, stable-law

- Related: `durrett_ch7_brownian_scaling`

### Hitting-time Laplace transform shape

- ID: `durrett_ch7_hitting_time_laplace_shape`

- Section: 7.4 Path Properties

- Kind: formula

- Summary: The Laplace transform phi_a(lambda)=E_0 exp(-lambda T_a) has the exponential form exp(-a c(lambda)), and eventually c(lambda)=sqrt(2 lambda).

- Proof idea: Stationary independent increments give multiplicativity in the level; scaling forces c(lambda) to be proportional to sqrt(lambda).

- Exam use: Use before or after exponential martingales to compute exact transforms.

- Pitfall: The constant sqrt(2) requires the martingale calculation; scaling alone gives only proportionality.

- Tags: laplace-transform, hitting-times, scaling

- Related: `durrett_ch7_hitting_time_subordinator`, `durrett_ch7_hitting_time_scaling`

### Reflection principle

- ID: `durrett_ch7_reflection_principle`

- Section: 7.4 Path Properties

- Kind: theorem

- Summary: For a>0, P_0(T_a<t)=2 P_0(B_t>=a), where T_a is the first hitting time of level a.

- Proof idea: After the first hit of a, reflect the remaining path; rigorously, apply the strong Markov property and symmetry at T_a.

- Exam use: Essential for maxima distributions, hitting-time densities, and barrier-crossing probabilities.

- Pitfall: The result is for Brownian motion without drift and with a one-sided level; drift or two-sided barriers need changes.

- Tags: reflection-principle, maximum, hitting-times

- Related: `durrett_ch7_strong_markov_property`

### First hitting-time density

- ID: `durrett_ch7_hitting_time_density`

- Section: 7.4 Path Properties

- Kind: formula

- Summary: For a>0, T_a has density a (2 pi s^3)^(-1/2) exp(-a^2/(2s)) on s>0.

- Proof idea: Differentiate the reflection-principle distribution after a change of variables in the normal tail.

- Exam use: Use for explicit integrals involving first passage times.

- Pitfall: This density has heavy tail and infinite mean; do not apply finite-mean intuition.

- Tags: hitting-time-density, reflection-principle, first-passage

- Related: `durrett_ch7_reflection_principle`

### Arcsine law for the last zero before one

- ID: `durrett_ch7_arcsine_last_zero`

- Section: 7.4 Path Properties

- Kind: example-pattern

- Summary: If L=sup{t<=1:B_t=0}, then P_0(L<=s)=(2/pi) arcsin(sqrt(s)) for 0<s<1.

- Proof idea: Condition at time s, use the Markov property and the hitting-time survival probability, then evaluate the integral.

- Exam use: Classic Brownian path distribution and a bridge to random-walk arcsine laws.

- Pitfall: The density blows up near 0 and 1; the last zero is not concentrated near 1/2.

- Tags: arcsine-law, last-zero, path-distribution

- Related: `durrett_ch7_hitting_time_density`

### Optional stopping for bounded stopping times

- ID: `durrett_ch7_optional_stopping_bounded`

- Section: 7.5 Martingales

- Kind: theorem

- Summary: A right-continuous martingale stopped at a bounded stopping time has the same expectation as at time 0.

- Proof idea: Approximate the stopping time from above by dyadic times and pass to the limit using right-continuity of the martingale and sigma-fields.

- Exam use: Foundation for Brownian exit probabilities and expected exit times.

- Pitfall: Boundedness or another valid stopping hypothesis is required; optional stopping is not automatic for unbounded times.

- Tags: optional-stopping, martingales, bounded-stopping-time

### Brownian motion is a martingale

- ID: `durrett_ch7_brownian_martingale`

- Section: 7.5 Martingales

- Kind: theorem

- Summary: B_t is a martingale with respect to the Brownian filtration.

- Proof idea: The Markov property gives E_x[B_t|F_s]=E_{B_s}[B_{t-s}]=B_s.

- Exam use: Use with optional stopping to compute two-sided hitting probabilities.

- Pitfall: Requires integrability and the correct filtration.

- Tags: martingale, brownian-motion, markov-property

- Related: `durrett_ch7_markov_property`

### Two-sided exit probability

- ID: `durrett_ch7_two_sided_exit_probability`

- Section: 7.5 Martingales

- Kind: formula

- Summary: For a<x<b, P_x(T_a<T_b)=(b-x)/(b-a).

- Proof idea: Stop the martingale B_t at T_a wedge T_b and solve x=a p+b(1-p).

- Exam use: High-yield gambler's-ruin analogue for Brownian motion.

- Pitfall: First show or know the exit time is finite; then justify the stopping/localization step.

- Tags: exit-probability, optional-stopping, gambler-ruin

- Related: `durrett_ch7_brownian_martingale`, `durrett_ch7_optional_stopping_bounded`

### Square martingale

- ID: `durrett_ch7_square_martingale`

- Section: 7.5 Martingales

- Kind: theorem

- Summary: B_t^2-t is a martingale.

- Proof idea: Expand B_t=B_s+(B_t-B_s), use independence, mean zero, and Var(B_t-B_s)=t-s.

- Exam use: Use to compute expected exit times and quadratic variation intuition.

- Pitfall: B_t^2 alone is a submartingale, not a martingale.

- Tags: martingale, quadratic-variation, second-moment

### Expected exit time from an interval

- ID: `durrett_ch7_expected_interval_exit_time`

- Section: 7.5 Martingales

- Kind: formula

- Summary: If T=inf{t:B_t notin (a,b)} with a<0<b and B_0=0, then E_0 T=-ab.

- Proof idea: Stop B_t^2-t at T wedge t, pass to the limit, and use the exit probabilities to compute E[B_T^2].

- Exam use: Standard computation for Brownian mean exit time from a bounded interval.

- Pitfall: Do not confuse exit from (a,b) with hitting a single level; the one-sided hitting time has infinite mean.

- Tags: exit-time, square-martingale, optional-stopping

- Related: `durrett_ch7_square_martingale`, `durrett_ch7_two_sided_exit_probability`

### Exponential Brownian martingale

- ID: `durrett_ch7_exponential_martingale`

- Section: 7.5 Martingales

- Kind: theorem

- Summary: For real theta, exp(theta B_t - theta^2 t/2) is a martingale.

- Proof idea: Condition on F_s, factor out exp(theta B_s), and use the normal moment generating function for the independent increment.

- Exam use: Use for Laplace transforms of hitting times and drift/barrier calculations.

- Pitfall: The compensator is theta^2 t/2; missing the factor 1/2 breaks the martingale.

- Tags: exponential-martingale, laplace-transform, gaussian-mgf

### Exact Laplace transform of a hitting time

- ID: `durrett_ch7_hitting_time_laplace_exact`

- Section: 7.5 Martingales

- Kind: formula

- Summary: For T_a=inf{t:B_t=a} and a>0, E_0 exp(-lambda T_a)=exp(-a sqrt(2 lambda)).

- Proof idea: Stop the exponential martingale with theta=sqrt(2 lambda) at T_a wedge t and pass to the limit.

- Exam use: Fastest exact calculation for first-passage Laplace transforms.

- Pitfall: The formula is for one-sided hitting from 0 to a>0; signs and starting points need translation.

- Tags: hitting-times, laplace-transform, exponential-martingale

- Related: `durrett_ch7_exponential_martingale`, `durrett_ch7_hitting_time_laplace_shape`

### Heat-equation martingales

- ID: `durrett_ch7_heat_equation_martingales`

- Section: 7.5 Martingales

- Kind: theorem

- Summary: If u_t+(1/2)u_xx=0 for a suitable polynomial u(t,x), then u(t,B_t) is a martingale.

- Proof idea: Use Brownian transition densities and the heat equation to show the conditional expectation is unchanged over time.

- Exam use: Generates polynomial martingales such as B_t^3-3tB_t and B_t^4-6tB_t^2+3t^2.

- Pitfall: The sign is the backward heat equation sign; check whether the time variable is forward or backward in a problem.

- Tags: heat-equation, polynomial-martingales, brownian-martingales

### Second moment of symmetric exit time

- ID: `durrett_ch7_symmetric_exit_second_moment`

- Section: 7.5 Martingales

- Kind: formula

- Summary: For T=inf{t:B_t notin (-a,a)}, E[T^2]=5a^4/3.

- Proof idea: Apply optional stopping to the fourth-degree polynomial martingale and combine with E[T]=a^2.

- Exam use: Useful template for computing higher exit-time moments via polynomial martingales.

- Pitfall: In nonsymmetric intervals, T and B_T^2 need not be independent, so the same shortcut fails.

- Tags: exit-time-moments, polynomial-martingales, optional-stopping

- Related: `durrett_ch7_heat_equation_martingales`, `durrett_ch7_expected_interval_exit_time`

### One-dimensional Ito formula

- ID: `durrett_ch7_ito_formula_one_dimensional`

- Section: 7.6 Ito's Formula*

- Kind: theorem

- Summary: For f in C^2, f(B_t)-f(B_0)=int_0^t f'(B_s)dB_s + (1/2)int_0^t f''(B_s)ds.

- Proof idea: Taylor expand over partitions; first-order terms define the stochastic integral and squared increments converge to elapsed time.

- Exam use: The central calculus rule for functions of Brownian motion.

- Pitfall: Ordinary chain rule misses the second-derivative correction.

- Tags: ito-formula, stochastic-calculus, quadratic-variation

- Related: `durrett_ch7_quadratic_variation_hint`

### Stochastic integral martingale criterion

- ID: `durrett_ch7_stochastic_integral_is_martingale`

- Section: 7.6 Ito's Formula*

- Kind: theorem

- Summary: If g is continuous and E int_0^t |g(B_s)|^2 ds is finite, then int_0^t g(B_s)dB_s is a continuous martingale.

- Proof idea: Approximate by adapted step sums, use conditional mean zero and L2 bounds, then pass to limits.

- Exam use: Lets Ito formula immediately produce martingales when the drift term vanishes.

- Pitfall: Square-integrability is the hypothesis that keeps the stochastic integral controlled.

- Tags: stochastic-integral, martingale, square-integrability

### Time-space Ito formula

- ID: `durrett_ch7_ito_formula_time_space`

- Section: 7.6 Ito's Formula*

- Kind: theorem

- Summary: For f in C^2 in time and space, df(t,B_t)=f_t(t,B_t)dt+f_x(t,B_t)dB_t+(1/2)f_xx(t,B_t)dt.

- Proof idea: Apply the one-dimensional formula with an added deterministic time increment and keep only first-order dt plus quadratic Brownian terms.

- Exam use: Use to connect Brownian martingales with PDEs and exponential models.

- Pitfall: There is no term involving dt dB_t or (dt)^2 in the limit.

- Tags: ito-formula, pde, time-space

- Related: `durrett_ch7_ito_formula_one_dimensional`

### Ito formula for exponential Brownian motion

- ID: `durrett_ch7_exponential_brownian_ito`

- Section: 7.6 Ito's Formula*

- Kind: example-pattern

- Summary: For X_t=exp(mu t+sigma B_t), Ito's formula gives dX_t=(mu+sigma^2/2)X_t dt+sigma X_t dB_t.

- Proof idea: Differentiate u(t,x)=exp(mu t+sigma x) and insert u_t, u_x, and u_xx into the time-space Ito formula.

- Exam use: Common model pattern for geometric Brownian motion and for checking exponential martingales.

- Pitfall: The drift of exp(mu t+sigma B_t) is mu+sigma^2/2, not just mu.

- Tags: geometric-brownian-motion, ito-formula, exponential

- Related: `durrett_ch7_ito_formula_time_space`

### Multidimensional Ito formula

- ID: `durrett_ch7_multidimensional_ito_formula`

- Section: 7.6 Ito's Formula*

- Kind: theorem

- Summary: For d-dimensional Brownian motion, df(t,B_t)=f_t dt+sum_i f_i dB_t^i+(1/2)sum_i f_{ii} dt.

- Proof idea: Second-order Taylor expansion keeps only diagonal quadratic variations; cross terms vanish for independent coordinates.

- Exam use: Use for radial processes, harmonic functions, and multidimensional martingales.

- Pitfall: The Laplacian term appears with factor 1/2; mixed second derivatives do not contribute for standard independent Brownian coordinates.

- Tags: multidimensional-ito, laplacian, brownian-motion

- Related: `durrett_ch7_d_dimensional_brownian`, `durrett_ch7_ito_formula_time_space`

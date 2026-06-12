# Durrett Chapter 9 LLM Viki: Multidimensional Brownian Motion

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter9.pdf`.

This unified Chapter 9 knowledge base includes textbook knowledge pieces plus exercise-derived method patterns from the solved Chapter 9 exercises.

Exercise source: `Probability/Exercises/Chapter9/Chapter9Exercises.tex` and `Probability/Exercises/Chapter9/Chapter9Exercises.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

## Section Guides

### 9.1 Martingales

- Goal: Use Ito's formula and optional stopping to compute multidimensional Brownian hitting probabilities and recurrence/transience facts.

- Must master: Ito-Laplacian martingale, radial harmonic functions, annulus hitting, d=2 recurrence, d>=3 transience

- Prelim angle: Most computations reduce to choosing the right harmonic function and stopping at sphere hitting times.

### 9.2 Heat Equation

- Goal: Represent bounded heat-equation solutions as Brownian expectations and connect them to Gaussian kernels.

- Must master: backward martingale, heat kernel, initial continuity, smoothing

- Prelim angle: A standard way to turn PDE uniqueness and existence into a martingale argument.

### 9.3 Inhomogeneous Heat Equation

- Goal: Handle source terms through Brownian occupation integrals.

- Must master: Duhamel formula, source-term martingale, Holder regularity

- Prelim angle: Recognize integral_0^t g(B_s) ds as the probabilistic form of a forcing term.

### 9.4 Feynman-Kac Formula

- Goal: Use exponential weights to solve heat equations with multiplicative potentials.

- Must master: weighted martingale, sign convention, boundedness, Holder smoothness

- Prelim angle: Converts PDEs with c(x)u terms into expectations of exponential occupation functionals.

### 9.5 Dirichlet Problem

- Goal: Represent harmonic boundary-value problems with Brownian exit distributions and understand boundary regularity.

- Must master: harmonic measure, regular boundary points, cone condition, Poisson kernels

- Prelim angle: Boundary behavior is often the hidden issue; regular points are the right probabilistic condition.

### 9.6 Green's Functions and Potential Kernels

- Goal: Interpret Green functions as Brownian occupation densities.

- Must master: potential kernel, killed Green function, occupation density

- Prelim angle: Green functions make expected time spent in a set into an integral kernel calculation.

### 9.7 Poisson's Equation

- Goal: Solve Poisson equations using occupation times and Green functions.

- Must master: Poisson representation, expected exit time, regular boundary zero condition, reflection/Kelvin formulas

- Prelim angle: Expected exit times and occupation times are usually Poisson-equation problems in disguise.

### 9.8 Schrodinger Equation

- Goal: Solve elliptic equations with potentials using exponential weights and gauge integrability.

- Must master: weighted martingale, gauge function, finite-gauge theorem, interval eigenvalue threshold

- Prelim angle: The main exam trap is assuming exponential exit-time expectations are finite without checking the gauge.

## Knowledge Pieces

### Ito-Laplacian martingale for Brownian motion

- ID: `durrett_ch9_ito_laplacian_martingale`

- Section: 9.1 Martingales

- Kind: theorem

- Summary: If v is C2 and the stochastic integral is square-integrable, then v(B_t)-1/2 integral_0^t Delta v(B_s) ds is a continuous martingale.

- Proof idea: Apply Ito's formula to v(B_t); the drift is exactly 1/2 Delta v and the gradient term is a martingale.

- Exam use: The one-line engine behind harmonic functions, optional stopping, PDE uniqueness, and Green function computations.

- Pitfall: The integrability/localization condition is not decoration; without it the stochastic integral may only be local.

- Tags: brownian-motion, ito-formula, laplacian, martingale

### Mean exit time from a ball

- ID: `durrett_ch9_exit_time_ball_mean`

- Section: 9.1 Martingales

- Kind: formula

- Summary: For d-dimensional Brownian motion started at |x|<R, the hitting time S_R of the sphere of radius R has E_x S_R=(R^2-|x|^2)/d.

- Proof idea: Stop the martingale |B_t|^2-dt at S_R wedge t and let t go to infinity.

- Exam use: Use for expected lifetime in balls and as a quick check for Poisson-equation solutions.

- Pitfall: The dimension appears in the denominator because |B_t|^2-dt is summed over d coordinates.

- Tags: exit-time, ball, optional-stopping

### Radial harmonic test functions

- ID: `durrett_ch9_radial_harmonic_functions`

- Section: 9.1 Martingales

- Kind: formula

- Summary: The radial functions phi(x)=log|x| in d=2 and phi(x)=|x|^(2-d) in d>=3 are harmonic off the origin.

- Proof idea: Differentiate radial functions or use the radial Laplacian formula g''(r)+(d-1)g'(r)/r.

- Exam use: They convert annulus hitting probabilities into algebra.

- Pitfall: They are singular at zero, so stop before hitting the inner radius and localize with smooth compact modifications.

- Tags: harmonic, radial, annulus

### Annulus hitting probability

- ID: `durrett_ch9_annulus_hitting_probability`

- Section: 9.1 Martingales

- Kind: formula

- Summary: For r<|x|<R, P_x(S_r<S_R)=[phi(R)-phi(x)]/[phi(R)-phi(r)], with phi radial harmonic as above.

- Proof idea: Optional stopping gives phi(x)=phi(r)P_x(S_r<S_R)+phi(R)P_x(S_R<S_r); solve the linear equation.

- Exam use: This is the standard computation for recurrence in d=2 and transience in d>=3.

- Pitfall: Use the correct dimension-specific phi; the logarithmic d=2 case is a frequent source of wrong powers.

- Tags: annulus, hitting-probability, recurrence, transience

### Two-dimensional Brownian recurrence

- ID: `durrett_ch9_two_dimensional_recurrence`

- Section: 9.1 Martingales

- Kind: theorem

- Summary: In d=2, Brownian motion hits every circle around the origin almost surely and visits every nonempty open set infinitely often.

- Proof idea: In the annulus formula, fix r and let R go to infinity; the logarithmic ratio tends to one.

- Exam use: Use to decide whether planar Brownian motion returns to neighborhoods, not to exact points.

- Pitfall: Recurrence of neighborhoods does not mean hitting a prescribed point at positive time.

- Tags: dimension-two, recurrence, hitting

### Points are polar in dimensions at least two

- ID: `durrett_ch9_points_polar_in_d_ge_2`

- Section: 9.1 Martingales

- Kind: fact

- Summary: For d>=2, Brownian motion does not hit a fixed point at a positive time, even when started from that point.

- Proof idea: In d=2, let the inner radius shrink to zero in the annulus formula; in higher dimensions reduce or compare by projection.

- Exam use: Prevents confusing recurrence in d=2 with point recurrence; important for punctured-domain examples.

- Pitfall: The definition of hitting zero uses t>0, so starting at zero is not a counterexample.

- Tags: polar-sets, hitting-points, dimension

### Transience in dimensions at least three

- ID: `durrett_ch9_higher_dimensional_transience`

- Section: 9.1 Martingales

- Kind: theorem

- Summary: For d>=3, P_x(S_r<infinity)=(r/|x|)^(d-2) when |x|>r, and |B_t| tends to infinity almost surely.

- Proof idea: Let the outer radius go to infinity in the annulus formula, then use the strong Markov property over growing spheres.

- Exam use: Use whenever a problem asks whether Brownian motion returns to bounded sets in high dimension.

- Pitfall: The limit |B_t| to infinity is almost sure but does not imply monotone radial motion.

- Tags: transience, dimension-three, radial-process

### Dvoretsky-Erdos lower envelope test

- ID: `durrett_ch9_dvoresky_erdos_test`

- Section: 9.1 Martingales

- Kind: theorem

- Summary: For d>=3 and positive decreasing g, P_0(|B_t|<=g(t)sqrt(t) infinitely often) is one or zero according as integral g(t)^(d-2) dt/t diverges or converges.

- Proof idea: This sharpens transience by testing repeated returns to shrinking multiples of sqrt(t).

- Exam use: Useful as a recognition result for Brownian escape rates in advanced prelim-style questions.

- Pitfall: It concerns infinitely often behavior near infinity, not fixed-time Gaussian tails.

- Tags: lower-envelope, transience, zero-one-law

### Backward heat-equation martingale

- ID: `durrett_ch9_heat_backward_martingale`

- Section: 9.2 Heat Equation

- Kind: theorem

- Summary: If u_t=1/2 Delta u, then M_s=u(t-s,B_s) is a local martingale on 0<=s<=t.

- Proof idea: Apply Ito's formula to the space-time process (t-s,B_s); the time derivative cancels the Brownian drift.

- Exam use: This is the probabilistic uniqueness mechanism for the heat equation.

- Pitfall: The backward time t-s is essential; using t+s changes the sign.

- Tags: heat-equation, space-time, martingale

### Heat equation solution by Brownian expectation

- ID: `durrett_ch9_heat_equation_solution`

- Section: 9.2 Heat Equation

- Kind: theorem

- Summary: The bounded solution with initial condition f is v(t,x)=E_x f(B_t), equivalently convolution with the Gaussian heat kernel.

- Proof idea: Boundedness makes the backward martingale uniformly integrable, so u(t,x)=E_x u(0,B_t).

- Exam use: Use to solve Cauchy heat problems and identify semigroup smoothing.

- Pitfall: Continuity at t=0 requires continuity of f; boundedness alone is not enough for the boundary condition.

- Tags: heat-kernel, brownian-semigroup, uniqueness

### Gaussian heat kernel smoothing

- ID: `durrett_ch9_heat_kernel_smoothing`

- Section: 9.2 Heat Equation

- Kind: regularity

- Summary: For bounded continuous f, v(t,x)=integral (2 pi t)^(-d/2) exp(-|x-y|^2/(2t)) f(y) dy is C1,2 for t>0.

- Proof idea: Differentiate the Gaussian kernel under the integral for positive times.

- Exam use: Turns probabilistic representation into an actual classical solution.

- Pitfall: The smoothing is for t>0; behavior at t=0 is controlled by the initial data.

- Tags: regularity, heat-kernel, smoothing

### Duhamel representation for inhomogeneous heat equation

- ID: `durrett_ch9_duhamel_inhomogeneous_heat`

- Section: 9.3 Inhomogeneous Heat Equation

- Kind: formula

- Summary: For u_t=1/2 Delta u+g with zero initial data, the bounded solution is v(t,x)=E_x integral_0^t g(B_s) ds.

- Proof idea: Ito's formula shows u(t-s,B_s)+integral_0^s g(B_r)dr is a local martingale; stop at s=t.

- Exam use: Use for heat equations with source terms and for occupation-time interpretations.

- Pitfall: With nonzero f, add the homogeneous solution E_x f(B_t).

- Tags: inhomogeneous-heat, duhamel, occupation-time

### Holder source gives C1,2 inhomogeneous solution

- ID: `durrett_ch9_inhomogeneous_heat_regularity`

- Section: 9.3 Inhomogeneous Heat Equation

- Kind: regularity

- Summary: If g is Holder continuous, then v(t,x)=E_x integral_0^t g(B_s) ds is C1,2 and solves the inhomogeneous heat equation.

- Proof idea: Write v as integration of heat kernels against g and use parabolic regularity estimates.

- Exam use: A checklist item: representation plus Holder regularity gives a classical PDE solution.

- Pitfall: Continuity of g is natural, but Holder regularity is the clean sufficient condition used here.

- Tags: holder-continuity, regularity, inhomogeneous-heat

### Feynman-Kac formula for the heat equation with potential

- ID: `durrett_ch9_feynman_kac_forward`

- Section: 9.4 Feynman-Kac Formula

- Kind: theorem

- Summary: For u_t=1/2 Delta u+c(x)u and initial f, the bounded solution is v(t,x)=E_x[f(B_t) exp(integral_0^t c(B_s)ds)].

- Proof idea: Use Ito plus the product rule on u(t-s,B_s) exp(integral_0^s c(B_r)dr); the drift cancels.

- Exam use: Use for heat equations with growth/decay potential and moment-generating questions for occupation integrals.

- Pitfall: Check the sign convention: the chapter's plus c u corresponds to exp(+ integral c).

- Tags: feynman-kac, potential, heat-equation

### Feynman-Kac smoothness via reduction

- ID: `durrett_ch9_feynman_kac_smoothness`

- Section: 9.4 Feynman-Kac Formula

- Kind: proof-template

- Summary: If f and c are Holder continuous, the Feynman-Kac representation is C1,2 and solves the PDE.

- Proof idea: Split the representation into a heat part and an inhomogeneous heat part with source c(x)v(t,x).

- Exam use: Use when asked to justify that a probabilistic formula is a classical solution.

- Pitfall: Boundedness gives a representation; regularity needs additional assumptions.

- Tags: regularity, feynman-kac, holder-continuity

### Dirichlet problem representation

- ID: `durrett_ch9_dirichlet_problem_representation`

- Section: 9.5 Dirichlet Problem

- Kind: theorem

- Summary: For a domain G with exit time tau, any bounded harmonic solution with boundary data f must be v(x)=E_x f(B_tau).

- Proof idea: Run u(B_t) until exit, use bounded martingale convergence, and identify the terminal boundary value.

- Exam use: The central Brownian representation for harmonic measure and boundary-value problems.

- Pitfall: The formula can fail to satisfy the boundary condition at irregular boundary points.

- Tags: dirichlet-problem, harmonic-measure, exit-time

### Mean-value property implies harmonicity

- ID: `durrett_ch9_mean_value_harmonicity`

- Section: 9.5 Dirichlet Problem

- Kind: proof-template

- Summary: If v(x)=E_x v(B_tau_B) for every small ball B around x and v is C2, then Delta v(x)=0.

- Proof idea: Use Taylor expansion at x and the symmetry of the exit distribution from a ball.

- Exam use: Use to move from Brownian representations to Laplace's equation without stochastic calculus.

- Pitfall: The ball must be compactly contained in the domain.

- Tags: mean-value-property, harmonic, laplace-equation

### Interior smoothness of Brownian harmonic functions

- ID: `durrett_ch9_interior_smoothness_harmonic`

- Section: 9.5 Dirichlet Problem

- Kind: regularity

- Summary: The Brownian Dirichlet solution v(x)=E_x f(B_tau) is C-infinity inside G.

- Proof idea: Inside a ball, v equals an average over the sphere with the smooth Poisson kernel, so differentiation is allowed.

- Exam use: Lets you assert interior classical harmonicity even with only bounded boundary data.

- Pitfall: Interior smoothness says nothing by itself about boundary continuity.

- Tags: harmonic-functions, smoothness, poisson-kernel

### Regular boundary point

- ID: `durrett_ch9_regular_boundary_point`

- Section: 9.5 Dirichlet Problem

- Kind: definition

- Summary: A boundary point y is regular for G if Brownian motion started at y exits G immediately: P_y(tau=0)=1.

- Proof idea: Regularity is characterized probabilistically by immediate contact with the complement.

- Exam use: Use to decide where the Brownian Dirichlet solution attains the prescribed boundary value.

- Pitfall: A boundary point can be topologically present but probabilistically invisible.

- Tags: regular-boundary, dirichlet-problem, brownian-exit

### Boundary continuity at regular points

- ID: `durrett_ch9_boundary_continuity_regular_points`

- Section: 9.5 Dirichlet Problem

- Kind: theorem

- Summary: If f is bounded continuous and y is a regular boundary point, then E_x f(B_tau) tends to f(y) as x in G tends to y.

- Proof idea: Lower semicontinuity of x -> P_x(tau<=t) plus Brownian path continuity forces exits near y with high probability.

- Exam use: This is the precise condition for the Dirichlet representation to satisfy the boundary data.

- Pitfall: Do not claim boundary convergence at every boundary point without checking regularity.

- Tags: boundary-continuity, regular-point, dirichlet-problem

### Cone condition for regularity

- ID: `durrett_ch9_cone_condition`

- Section: 9.5 Dirichlet Problem

- Kind: criterion

- Summary: If the complement of G contains a cone with vertex y inside some small ball, then y is a regular boundary point.

- Proof idea: Brownian motion hits such exterior cones immediately enough to force tau=0 from the boundary.

- Exam use: A practical geometric sufficient condition for boundary regularity.

- Pitfall: It is sufficient, not necessary; failure of a cone condition does not automatically mean irregularity.

- Tags: cone-condition, regular-boundary, geometry

### Punctured-domain boundary warning

- ID: `durrett_ch9_punctured_domain_warning`

- Section: 9.5 Dirichlet Problem

- Kind: example-pattern

- Summary: Thin removed sets can fail to influence Brownian exit, so a bounded harmonic representation may ignore assigned values on those sets.

- Proof idea: Use polarity of points or lines in higher dimensions to see that Brownian motion almost surely misses the thin set.

- Exam use: Explains why Dirichlet boundary data must be paired with regularity assumptions.

- Pitfall: A discontinuity of the probabilistic solution at an irregular point is not a contradiction of uniqueness inside G.

- Tags: irregular-boundary, polar-sets, examples

### Half-space Poisson kernel

- ID: `durrett_ch9_half_space_poisson_kernel`

- Section: 9.5.1 Exit Distributions

- Kind: formula

- Summary: For the upper half-space H, the exit distribution on the boundary has density C_d y/(|x-theta|^2+y^2)^(d/2).

- Proof idea: Check the kernel is harmonic in H, normalizes to one, and approximates boundary data as y down to zero.

- Exam use: Use to compute Brownian exit distributions from a half-space; in d=2 it gives the Cauchy density.

- Pitfall: Track dimension conventions: the boundary variable theta lives in d-1 dimensions.

- Tags: poisson-kernel, half-space, exit-distribution

### Unit-ball Poisson kernel

- ID: `durrett_ch9_ball_poisson_kernel`

- Section: 9.5.1 Exit Distributions

- Kind: formula

- Summary: For the unit ball D, E_x f(B_tau)=integral_{partial D} [(1-|x|^2)/|x-y|^d] f(y) pi(dy).

- Proof idea: Show the kernel is harmonic in x and reproduces the boundary data as x approaches regular boundary points.

- Exam use: Use to solve explicit Dirichlet problems in balls.

- Pitfall: The surface measure pi is normalized to be a probability measure in the chapter's formula.

- Tags: poisson-kernel, ball, harmonic-measure

### Brownian potential kernel in R^d

- ID: `durrett_ch9_newtonian_potential_kernel`

- Section: 9.6 Green's Functions and Potential Kernels

- Kind: formula

- Summary: The expected occupation density of Brownian motion is the potential kernel G(x,y), proportional to |x-y|^(2-d) for d>=3 and to -log|x-y| in d=2 after domain adjustment.

- Proof idea: Integrate the Gaussian transition density over time and evaluate the resulting radial integral.

- Exam use: Use to turn occupation-time expectations into spatial integrals.

- Pitfall: In recurrent dimensions the full-space occupation integral can diverge, so constants and killed domains matter.

- Tags: green-function, potential-kernel, occupation-density

### Killed-domain Green function

- ID: `durrett_ch9_green_function_killed_domain`

- Section: 9.6 Green's Functions and Potential Kernels

- Kind: definition

- Summary: For Brownian motion killed on leaving D, G_D(x,y) is the density satisfying E_x integral_0^tau f(B_t)dt = integral_D G_D(x,y)f(y)dy.

- Proof idea: Subtract the expected potential contributed after exit from the full-space potential.

- Exam use: The bridge between Brownian occupation times and Poisson's equation.

- Pitfall: The Green function depends on the domain and boundary killing, not only on |x-y|.

- Tags: green-function, killed-brownian-motion, occupation-time

### Poisson equation representation

- ID: `durrett_ch9_poisson_equation_representation`

- Section: 9.7 Poisson's Equation

- Kind: theorem

- Summary: For 1/2 Delta u=-g in G with zero boundary data, any bounded solution must be v(x)=E_x integral_0^tau g(B_t)dt.

- Proof idea: The process u(B_t)+integral_0^t g(B_s)ds is a local martingale up to tau; stop and let t approach tau.

- Exam use: Use for expected occupation times, expected exit times, and source-term boundary problems.

- Pitfall: Sign conventions vary; here the PDE is 1/2 Delta u=-g for a positive occupation formula.

- Tags: poisson-equation, occupation-time, exit-time

### Expected exit time solves Poisson's equation

- ID: `durrett_ch9_expected_exit_time_poisson`

- Section: 9.7 Poisson's Equation

- Kind: example-pattern

- Summary: Taking g=1 gives v(x)=E_x tau, which solves 1/2 Delta v=-1 in G with zero boundary values at regular points.

- Proof idea: This is the Poisson representation specialized to unit source.

- Exam use: A common prelim computation: guess radial v in a ball and verify by Laplacian and boundary values.

- Pitfall: Finite expectation needs domain control; unbounded domains may have infinite exit time.

- Tags: expected-exit-time, poisson-equation, radial-solution

### Poisson solution vanishes at regular boundary points

- ID: `durrett_ch9_poisson_boundary_regular`

- Section: 9.7 Poisson's Equation

- Kind: theorem

- Summary: If G and g are bounded and y is a regular boundary point, then v(x)=E_x integral_0^tau g(B_t)dt tends to zero as x tends to y from inside G.

- Proof idea: Regularity makes tau small with high probability; boundedness controls the remaining tail.

- Exam use: Use to verify the zero boundary condition for occupation-time solutions.

- Pitfall: Regularity and boundedness assumptions are doing real work here.

- Tags: boundary-condition, poisson-equation, regular-point

### Half-space Green function by reflection

- ID: `durrett_ch9_green_function_half_space`

- Section: 9.7.1 Occupation Times

- Kind: formula

- Summary: For the half-space, the killed Green function equals the full-space potential at y minus the full-space potential at the reflected point y_bar.

- Proof idea: Use the reflection principle/image method so the difference vanishes on the boundary.

- Exam use: Compute occupation times before exiting a half-space.

- Pitfall: The reflected term has the same singularity mirrored across the boundary, not at the original y.

- Tags: green-function, reflection-principle, half-space

### Ball Green function by Kelvin transform

- ID: `durrett_ch9_green_function_ball_kelvin`

- Section: 9.7.1 Occupation Times

- Kind: formula

- Summary: For the unit ball in d>=3, G_D(x,y)=G(x,y)-|y|^(2-d)G(x,y/|y|^2); a logarithmic analog holds in d=2.

- Proof idea: The Kelvin-reflected singularity makes the boundary value cancel on |x|=1.

- Exam use: Use for explicit occupation densities in balls.

- Pitfall: The formula has a singular-looking y=0 case that must be handled by a limit or separately.

- Tags: green-function, unit-ball, kelvin-transform

### Schrodinger boundary-value martingale

- ID: `durrett_ch9_schrodinger_martingale`

- Section: 9.8 Schrodinger Equation

- Kind: theorem

- Summary: For 1/2 Delta u+c(x)u=0 in G, u(B_t) exp(integral_0^t c(B_s)ds) is a local martingale up to the exit time.

- Proof idea: Apply Ito's formula and the product rule; the PDE cancels the drift after weighting by the exponential potential.

- Exam use: Foundation for boundary Feynman-Kac formulas and exponential exit-time moments.

- Pitfall: The sign of c controls integrability; positive c can make the expectation infinite.

- Tags: schrodinger-equation, feynman-kac, local-martingale

### Positive potential can destroy bounded representation

- ID: `durrett_ch9_schrodinger_nonuniqueness_warning`

- Section: 9.8 Schrodinger Equation

- Kind: example-pattern

- Summary: For G=(-a,a), c=gamma>0, and boundary value 1, the ODE solution exists only away from eigenvalue obstructions and exponential exit moments can blow up.

- Proof idea: Solve 1/2 u''+gamma u=0 with boundary values and inspect zeros of cos(a sqrt(2 gamma)).

- Exam use: Use as a warning that Feynman-Kac with positive potential needs integrability assumptions.

- Pitfall: Bounded c does not automatically imply E_x exp(integral_0^tau c(B_s)ds) is finite.

- Tags: schrodinger-equation, eigenvalues, integrability

### Gauge function for exponential lifetime integrability

- ID: `durrett_ch9_gauge_function`

- Section: 9.8 Schrodinger Equation

- Kind: definition

- Summary: The gauge w(x)=E_x exp(integral_0^tau c(B_s)ds) measures whether the Schrodinger Feynman-Kac representation is finite.

- Proof idea: Local exponential exit-time bounds plus a covering argument propagate finiteness through connected domains.

- Exam use: Check this before asserting uniqueness or boundary representations with exponential weights.

- Pitfall: Finiteness at one point and boundedness over the domain require separate hypotheses in the chapter.

- Tags: gauge, exponential-moment, schrodinger-equation

### Small-set exponential exit bound

- ID: `durrett_ch9_small_set_exponential_exit_bound`

- Section: 9.8 Schrodinger Equation

- Kind: lemma

- Summary: For each theta>0, sufficiently small open sets H have uniformly bounded E_x exp(theta tau_H).

- Proof idea: Use occupation-time/tail bounds for Brownian exit from small-measure sets and sum the exponential series.

- Exam use: Technical tool that makes the gauge theorem work.

- Pitfall: Small Lebesgue measure is the key condition, not merely small diameter in the statement.

- Tags: exit-time, exponential-moment, small-set

### Gauge finiteness propagates on connected domains

- ID: `durrett_ch9_gauge_theorem_connected_domain`

- Section: 9.8 Schrodinger Equation

- Kind: theorem

- Summary: If G is connected and the gauge w is not identically infinite, then w(x)<infinity for every x in G; if |G|<infinity, w is bounded.

- Proof idea: Local comparison across balls gives openness of the finite set, and connectedness plus small-set control gives closed propagation.

- Exam use: Use to justify uniform integrability in Schrodinger uniqueness proofs.

- Pitfall: Connectedness matters; separate components need separate checks.

- Tags: gauge-theorem, connected-domain, boundedness

### Schrodinger Dirichlet representation

- ID: `durrett_ch9_schrodinger_dirichlet_representation`

- Section: 9.8 Schrodinger Equation

- Kind: theorem

- Summary: Under bounded connected domain, bounded continuous f and c, and finite gauge, the bounded solution is v(x)=E_x[f(B_tau) exp(integral_0^tau c(B_s)ds)].

- Proof idea: Stop the weighted martingale, use boundedness of the gauge for uniform integrability, and pass to the exit time.

- Exam use: Use for boundary-value problems with killing or creation potentials.

- Pitfall: Without the finite-gauge assumption, the formula may be infinite or uniqueness may fail.

- Tags: schrodinger-equation, dirichlet-problem, feynman-kac

### Schrodinger boundary condition at regular points

- ID: `durrett_ch9_schrodinger_boundary_regular`

- Section: 9.8 Schrodinger Equation

- Kind: theorem

- Summary: At regular boundary points, the Schrodinger representation tends to the boundary value f(y).

- Proof idea: Split paths by small exit time and nearby exit location, then control the remaining event with bounded gauge.

- Exam use: Use to finish verification of boundary data for the weighted representation.

- Pitfall: The exponential weight adds a tail-control requirement absent from the plain Dirichlet problem.

- Tags: boundary-condition, regular-point, schrodinger-equation

### Holder potential gives C2 Schrodinger solution

- ID: `durrett_ch9_schrodinger_smoothness`

- Section: 9.8 Schrodinger Equation

- Kind: regularity

- Summary: With the chapter's bounded-domain/gauge assumptions and Holder continuous c, the Schrodinger representation is C2 and solves 1/2 Delta v+c v=0.

- Proof idea: Reduce locally to Poisson-equation regularity with source c(x)v(x).

- Exam use: Use to upgrade the probabilistic representation to a classical solution.

- Pitfall: Smoothness is interior; boundary regularity is a separate issue.

- Tags: regularity, holder-continuity, schrodinger-equation

### Exponential exit moment from an interval

- ID: `durrett_ch9_interval_exponential_exit_moment`

- Section: 9.8 Schrodinger Equation

- Kind: formula

- Summary: For tau exiting (-a,a), E_x exp(gamma tau)=cos(x sqrt(2 gamma))/cos(a sqrt(2 gamma)) when 0<gamma<pi^2/(8a^2), and is infinite at or above the threshold.

- Proof idea: Solve the ODE 1/2 u''+gamma u=0 with boundary value one and use the gauge/uniqueness result below the first eigenvalue.

- Exam use: A high-yield explicit computation connecting Brownian exit times with eigenvalues.

- Pitfall: The threshold is the first Dirichlet eigenvalue for the interval; at the threshold the denominator vanishes.

- Tags: exit-time, exponential-moment, eigenvalue, interval

### Backward heat martingale template

- ID: `ch9_exercise_method_backward_heat_martingale_template`

- Section: 9.2 Exercises: Heat equation, Brownian semigroup, and heat-kernel smoothing

- Kind: exercise-pattern

- Summary: For u_t=(1/2)Delta u, apply Ito to u(t-s,B_s); the time derivative cancels the Brownian drift and leaves a local martingale.

- Proof idea: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Exam use: Section 9.2 martingale checks and any backward parabolic uniqueness argument.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: heat-equation, ito-formula, backward-time, martingale

- Source exercises: 9.2.A, 9.2.B, 9.2.C, 9.2.D

### Bounded heat solution uniqueness by terminal martingale

- ID: `ch9_exercise_method_bounded_heat_uniqueness`

- Section: 9.2 Exercises: Heat equation, Brownian semigroup, and heat-kernel smoothing

- Kind: exercise-pattern

- Summary: Boundedness upgrades the backward local martingale to a uniformly integrable martingale; sending s up to t identifies u(t,x) with E_x f(B_t).

- Proof idea: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Exam use: Heat equation uniqueness and bounded parabolic Cauchy problems.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: heat-equation, uniqueness, uniform-integrability

- Source exercises: 9.2.A, 9.2.B, 9.2.C, 9.2.D

### Gaussian approximate identity at t=0

- ID: `ch9_exercise_method_gaussian_approximate_identity`

- Section: 9.2 Exercises: Heat equation, Brownian semigroup, and heat-kernel smoothing

- Kind: exercise-pattern

- Summary: Write B_t as sqrt(t)Z; bounded convergence proves E f(x_n+sqrt(t_n)Z) tends to f(x) when f is bounded continuous.

- Proof idea: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Exam use: Initial-condition verification for heat and Feynman-Kac formulas.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: heat-kernel, initial-condition, bounded-convergence

- Source exercises: 9.2.A, 9.2.B, 9.2.C, 9.2.D

### Heat-kernel derivative majorants

- ID: `ch9_exercise_method_heat_kernel_derivative_majorants`

- Section: 9.2 Exercises: Heat equation, Brownian semigroup, and heat-kernel smoothing

- Kind: exercise-pattern

- Summary: On t bounded away from zero, derivatives of the Gaussian kernel are polynomial times a Gaussian, giving integrable majorants for differentiating under the integral.

- Proof idea: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Exam use: Proving C^{1,2} smoothing for heat semigroups.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: heat-kernel, regularity, dominated-convergence

- Source exercises: 9.2.A, 9.2.B, 9.2.C, 9.2.D

### Source-term martingale for inhomogeneous heat equations

- ID: `ch9_exercise_method_source_term_martingale`

- Section: 9.3 Exercises: Inhomogeneous heat equation and Duhamel occupation formulas

- Kind: exercise-pattern

- Summary: For u_t=(1/2)Delta u+g, add integral_0^s g(B_r)dr to u(t-s,B_s) so the drift cancels.

- Proof idea: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Exam use: Duhamel representation and source-term uniqueness.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: duhamel, source-term, martingale

- Source exercises: 9.3.A, 9.3.B, 9.3.C, 9.3.D, 9.3.E

### Duhamel uniqueness from bounded martingales

- ID: `ch9_exercise_method_duhamel_uniqueness`

- Section: 9.3 Exercises: Inhomogeneous heat equation and Duhamel occupation formulas

- Kind: exercise-pattern

- Summary: A bounded inhomogeneous heat solution with zero initial data equals E_x integral_0^t g(B_s)ds by stopping the source-term martingale at s=t.

- Proof idea: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Exam use: Identifying source-forced heat solutions and occupation integrals.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: duhamel, uniqueness, occupation-integral

- Source exercises: 9.3.A, 9.3.B, 9.3.C, 9.3.D, 9.3.E

### Short-time Markov-property PDE verification

- ID: `ch9_exercise_method_markov_property_pde_verification`

- Section: 9.3 Exercises: Inhomogeneous heat equation and Duhamel occupation formulas

- Kind: exercise-pattern

- Summary: Use v(t+h,x)=E_x[v(t,B_h)+short-time reward], Taylor expand v(t,B_h), divide by h, and let h down to zero.

- Proof idea: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Exam use: Showing smooth Brownian representations solve heat, Poisson, and Feynman-Kac PDEs.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: markov-property, taylor-expansion, pde-verification

- Source exercises: 9.3.A, 9.3.B, 9.3.C, 9.3.D, 9.3.E

### Holder cancellation for singular heat-source kernels

- ID: `ch9_exercise_method_holder_cancels_kernel_singularity`

- Section: 9.3 Exercises: Inhomogeneous heat equation and Duhamel occupation formulas

- Kind: exercise-pattern

- Summary: Subtract g(x) inside P_s g(x)-g(x); Holder continuity gives O(s^{alpha/2}), offsetting the small-time singularity.

- Proof idea: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Exam use: Regularity of inhomogeneous heat and potential-kernel formulas.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: holder-continuity, regularity, singular-kernel

- Source exercises: 9.3.A, 9.3.B, 9.3.C, 9.3.D, 9.3.E

### Exponential potential weight martingale

- ID: `ch9_exercise_method_exponential_weight_martingale`

- Section: 9.4 Exercises: Feynman-Kac formula for heat equations with potentials

- Kind: exercise-pattern

- Summary: Multiply by exp(integral c(B_s)ds); the finite-variation product rule adds exactly the c u drift needed for cancellation.

- Proof idea: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Exam use: Feynman-Kac and Schrodinger martingale derivations.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: feynman-kac, exponential-weight, martingale

- Source exercises: 9.4.A, 9.4.B, 9.4.C, 9.4.D, 9.4.E

### Bounded Feynman-Kac uniqueness

- ID: `ch9_exercise_method_feynman_kac_bounded_uniqueness`

- Section: 9.4 Exercises: Feynman-Kac formula for heat equations with potentials

- Kind: exercise-pattern

- Summary: If c and u are bounded on finite time intervals, the weighted martingale is bounded; stopping at t gives u(t,x)=E_x[f(B_t)exp(integral_0^t c(B_s)ds)].

- Proof idea: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Exam use: Parabolic PDEs with bounded multiplicative potentials.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: feynman-kac, boundedness, uniqueness

- Source exercises: 9.4.A, 9.4.B, 9.4.C, 9.4.D, 9.4.E

### Smooth Feynman-Kac short-time check

- ID: `ch9_exercise_method_smooth_feynman_kac_short_time_check`

- Section: 9.4 Exercises: Feynman-Kac formula for heat equations with potentials

- Kind: exercise-pattern

- Summary: Use v(t+h,x)=E_x[e^{int_0^h c(B_s)ds}v(t,B_h)], then expand the Brownian move and the exponential to get v_t=(1/2)Delta v+c v.

- Proof idea: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Exam use: Verifying smooth Feynman-Kac representations solve the PDE.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: feynman-kac, short-time, pde-verification

- Source exercises: 9.4.A, 9.4.B, 9.4.C, 9.4.D, 9.4.E

### Feynman-Kac smoothness by Duhamel reduction

- ID: `ch9_exercise_method_feynman_kac_duhamel_reduction`

- Section: 9.4 Exercises: Feynman-Kac formula for heat equations with potentials

- Kind: exercise-pattern

- Summary: Use e^{A_t}-1=integral_0^t c(B_s)e^{A_t-A_s}ds to decompose v into a heat solution plus an inhomogeneous heat solution with source c v.

- Proof idea: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Exam use: Regularity proofs for Feynman-Kac formulas with Holder f and c.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: feynman-kac, duhamel, regularity

- Source exercises: 9.4.A, 9.4.B, 9.4.C, 9.4.D, 9.4.E

### Liouville theorem via heat semigroup flattening

- ID: `ch9_exercise_method_heat_semigroup_liouville`

- Section: 9.5 Exercises: Dirichlet problem, Liouville principles, and boundary regularity

- Kind: exercise-pattern

- Summary: A bounded harmonic h satisfies h(x)=E h(x+B_t); as t grows, two Gaussian laws with fixed mean separation have vanishing total variation distance, so h(x)=h(y).

- Proof idea: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Exam use: Bounded harmonic functions on all of R^d.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: liouville, harmonic-functions, heat-semigroup

- Source exercises: 9.5.1, 9.5.2, 9.5.3, 9.5.4, 9.5.5

### Recurrent Brownian motion forces nonnegative superharmonic functions constant

- ID: `ch9_exercise_method_recurrent_superharmonic_constancy`

- Section: 9.5 Exercises: Dirichlet problem, Liouville principles, and boundary regularity

- Kind: exercise-pattern

- Summary: Nonnegative superharmonic functions yield supermartingales; in d=1,2 Brownian motion hits every small neighborhood, so optional stopping gives f(x)>=f(y) and symmetry gives equality.

- Proof idea: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Exam use: Superharmonic Liouville-type exercises in recurrent dimensions.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: superharmonic, recurrence, optional-stopping

- Source exercises: 9.5.1, 9.5.2, 9.5.3, 9.5.4, 9.5.5

### Radial superharmonic examples in high dimension

- ID: `ch9_exercise_method_radial_superharmonic_high_dimension`

- Section: 9.5 Exercises: Dirichlet problem, Liouville principles, and boundary regularity

- Kind: example-pattern

- Summary: Use the radial Laplacian g''(r)+(d-1)g'(r)/r; functions such as (1+r^2)^{-(d-2)/2} are smooth nonconstant nonnegative superharmonic for d>=3.

- Proof idea: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Exam use: Constructing counterexamples to recurrent-dimensional constancy in transient dimensions.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: radial-laplacian, superharmonic, dimension

- Source exercises: 9.5.1, 9.5.2, 9.5.3, 9.5.4, 9.5.5

### Escape probability is the nonuniqueness direction

- ID: `ch9_exercise_method_escape_probability_nonuniqueness`

- Section: 9.5 Exercises: Dirichlet problem, Liouville principles, and boundary regularity

- Kind: exercise-pattern

- Summary: When Brownian motion can avoid exiting G, q(x)=P_x(tau=infinity) is a bounded zero-boundary harmonic function; all bounded zero-boundary solutions differ by c q.

- Proof idea: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Exam use: Dirichlet problems in domains where exit is not almost sure.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: dirichlet-problem, nonuniqueness, escape-probability

- Source exercises: 9.5.1, 9.5.2, 9.5.3, 9.5.4, 9.5.5

### Flat cone boundary regularity

- ID: `ch9_exercise_method_flat_cone_regular_boundary`

- Section: 9.5 Exercises: Dirichlet problem, Liouville principles, and boundary regularity

- Kind: exercise-pattern

- Summary: Use zeros of the perpendicular Brownian coordinate and the induced Cauchy trace on the hyperplane to show Brownian motion immediately hits a flat exterior cone.

- Proof idea: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Exam use: Checking regular boundary points under weaker geometric exterior conditions.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: regular-boundary, cone-condition, brownian-trace

- Source exercises: 9.5.1, 9.5.2, 9.5.3, 9.5.4, 9.5.5

### Infinite ball occupation in recurrent dimensions

- ID: `ch9_exercise_method_recurrent_ball_occupation_infinite`

- Section: 9.6 Exercises: Green functions, occupation densities, and potential-kernel normalization

- Kind: exercise-pattern

- Summary: Use recurrence to get infinitely many returns to a ball and the strong Markov property to sum positive occupation increments.

- Proof idea: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Exam use: Occupation-time dichotomy for Brownian motion in d<=2.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: occupation-time, recurrence, strong-markov-property

- Source exercises: 9.6.A, 9.6.B, 9.6.C, 9.6.D, 9.6.E

### Gamma change of variables for transient potential kernels

- ID: `ch9_exercise_method_transient_potential_kernel_gamma`

- Section: 9.6 Exercises: Green functions, occupation densities, and potential-kernel normalization

- Kind: exercise-pattern

- Summary: For d>=3, integrate the heat kernel over time and use s=|x-y|^2/(2t) to get Gamma(d/2-1)/(2 pi^{d/2}) |x-y|^{2-d}.

- Proof idea: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Exam use: Green-function and expected occupation-density calculations.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: potential-kernel, gamma-function, transience

- Source exercises: 9.6.A, 9.6.B, 9.6.C, 9.6.D, 9.6.E

### Modified potential kernels in recurrent dimensions

- ID: `ch9_exercise_method_recurrent_modified_potential_kernel`

- Section: 9.6 Exercises: Green functions, occupation densities, and potential-kernel normalization

- Kind: exercise-pattern

- Summary: Subtract a reference heat kernel before integrating over time; in d=1 this gives -|x-y| and in d=2 gives -(1/pi)log|x-y|.

- Proof idea: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Exam use: Using potential kernels when the full-space occupation integral diverges.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: potential-kernel, recurrent-dimensions, renormalization

- Source exercises: 9.6.A, 9.6.B, 9.6.C, 9.6.D, 9.6.E

### Frullani integral for the two-dimensional log kernel

- ID: `ch9_exercise_method_frullani_log_kernel`

- Section: 9.6 Exercises: Green functions, occupation densities, and potential-kernel normalization

- Kind: exercise-pattern

- Summary: After u=1/(2t), the difference of two planar heat kernels becomes integral_0^infty (e^{-a^2u}-e^{-u})du/u=-2log a.

- Proof idea: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Exam use: Deriving the d=2 logarithmic potential kernel.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: frullani, log-kernel, dimension-two

- Source exercises: 9.6.A, 9.6.B, 9.6.C, 9.6.D, 9.6.E

### Distributional delta normalization of Green kernels

- ID: `ch9_exercise_method_distributional_delta_normalization`

- Section: 9.6 Exercises: Green functions, occupation densities, and potential-kernel normalization

- Kind: exercise-pattern

- Summary: Integrate by parts outside a small ball and let the radius shrink; the boundary flux fixes the constant so (1/2)Delta G=-delta_0.

- Proof idea: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Exam use: Checking Green-function constants and fundamental solutions.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: distributional-laplacian, green-function, flux

- Source exercises: 9.6.A, 9.6.B, 9.6.C, 9.6.D, 9.6.E

### Exit-time moment recursion

- ID: `ch9_exercise_method_exit_time_moment_recursion`

- Section: 9.7 Exercises: Poisson equation and exit-time moment recursions

- Kind: exercise-pattern

- Summary: For m_n(x)=E_x tau^n, the Markov property or Dynkin formula gives (1/2)Delta m_n=-n m_{n-1} with zero boundary values.

- Proof idea: Identify exit-time moments by applying the Poisson representation recursively: the nth moment solves a Poisson equation with source n times the previous moment.

- Exam use: Computing higher moments of Brownian exit times.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: exit-time, moment-recursion, poisson-equation

- Source exercises: 9.7.1

### Second exit-time moment Poisson system

- ID: `ch9_exercise_method_second_moment_poisson_system`

- Section: 9.7 Exercises: Poisson equation and exit-time moment recursions

- Kind: exercise-pattern

- Summary: First solve (1/2)Delta v=-1 for v=E tau; then solve (1/2)Delta w=-2v for w=E tau^2, both with zero boundary values.

- Proof idea: Identify exit-time moments by applying the Poisson representation recursively: the nth moment solves a Poisson equation with source n times the previous moment.

- Exam use: Exercise 9.7.1 and second-moment exit-time computations.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: exit-time, second-moment, poisson-equation

- Source exercises: 9.7.1

### Schrodinger weighted martingale

- ID: `ch9_exercise_method_schrodinger_weighted_martingale`

- Section: 9.8 Exercises: Schrodinger equation, gauge integrability, and exponential exit moments

- Kind: exercise-pattern

- Summary: For (1/2)Delta u+c u=0, Ito plus the finite-variation product rule makes u(B_t)exp(integral_0^t c(B_s)ds) a local martingale before exit.

- Proof idea: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Exam use: Boundary Feynman-Kac formulas for elliptic equations with potential.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: schrodinger-equation, feynman-kac, martingale

- Source exercises: 9.8.A, 9.8.B, 9.8.C, 9.8.D, 9.8.E, 9.8.F

### Gauge integrability condition

- ID: `ch9_exercise_method_gauge_integrability_condition`

- Section: 9.8 Exercises: Schrodinger equation, gauge integrability, and exponential exit moments

- Kind: criterion

- Summary: Before applying boundary Feynman-Kac with positive potential, check w(x)=E_x exp(integral_0^tau c(B_s)ds); bounded c alone does not ensure finiteness.

- Proof idea: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Exam use: Avoiding false Schrodinger Feynman-Kac representations.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: gauge, integrability, positive-potential

- Source exercises: 9.8.A, 9.8.B, 9.8.C, 9.8.D, 9.8.E, 9.8.F

### Interval eigenvalue threshold for exponential exit times

- ID: `ch9_exercise_method_interval_eigenvalue_threshold`

- Section: 9.8 Exercises: Schrodinger equation, gauge integrability, and exponential exit moments

- Kind: exercise-pattern

- Summary: For tau exiting (-a,a), solve (1/2)u''+gamma u=0 with boundary value one; finiteness holds exactly below gamma=pi^2/(8a^2).

- Proof idea: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Exam use: Explicit exponential exit-time moments and gauge blow-up examples.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: exit-time, eigenvalue, interval

- Source exercises: 9.8.A, 9.8.B, 9.8.C, 9.8.D, 9.8.E, 9.8.F

### Finite-gauge boundary Feynman-Kac uniqueness

- ID: `ch9_exercise_method_finite_gauge_boundary_feynman_kac`

- Section: 9.8 Exercises: Schrodinger equation, gauge integrability, and exponential exit moments

- Kind: exercise-pattern

- Summary: Finite bounded gauge controls the terminal exponential weight and kills the tail term, giving u(x)=E_x[f(B_tau)exp(integral_0^tau c(B_s)ds)].

- Proof idea: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Exam use: Uniqueness of bounded Schrodinger Dirichlet solutions.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: finite-gauge, dirichlet-problem, feynman-kac

- Source exercises: 9.8.A, 9.8.B, 9.8.C, 9.8.D, 9.8.E, 9.8.F

### Local exit expansion for smooth Schrodinger representations

- ID: `ch9_exercise_method_smooth_schrodinger_local_exit_expansion`

- Section: 9.8 Exercises: Schrodinger equation, gauge integrability, and exponential exit moments

- Kind: exercise-pattern

- Summary: Stop at a small ball, expand v(B_sigma) and exp(integral_0^sigma c(B_s)ds), then divide by E sigma to get (1/2)Delta v+c v=0.

- Proof idea: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Exam use: Verifying smooth Schrodinger Feynman-Kac formulas solve the PDE.

- Pitfall: Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.

- Tags: schrodinger-equation, local-exit, taylor-expansion

- Source exercises: 9.8.A, 9.8.B, 9.8.C, 9.8.D, 9.8.E, 9.8.F

## Exercise Method Cards

### 9.2 Heat equation, Brownian semigroup, and heat-kernel smoothing

- ID: `durrett_ch9_section_9_2_method_card`

- Method: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- New knowledge IDs: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

### 9.3 Inhomogeneous heat equation and Duhamel occupation formulas

- ID: `durrett_ch9_section_9_3_method_card`

- Method: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Tags: duhamel, source-term, occupation-integral, holder-regularity

- New knowledge IDs: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

### 9.4 Feynman-Kac formula for heat equations with potentials

- ID: `durrett_ch9_section_9_4_method_card`

- Method: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Tags: feynman-kac, exponential-weight, potential, regularity-reduction

- New knowledge IDs: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

### 9.5 Dirichlet problem, Liouville principles, and boundary regularity

- ID: `durrett_ch9_section_9_5_method_card`

- Method: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- New knowledge IDs: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

### 9.6 Green functions, occupation densities, and potential-kernel normalization

- ID: `durrett_ch9_section_9_6_method_card`

- Method: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- New knowledge IDs: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

### 9.7 Poisson equation and exit-time moment recursions

- ID: `durrett_ch9_section_9_7_method_card`

- Method: Identify exit-time moments by applying the Poisson representation recursively: the nth moment solves a Poisson equation with source n times the previous moment.

- Tags: poisson-equation, exit-time-moments, moment-recursion

- New knowledge IDs: ch9_exercise_method_exit_time_moment_recursion, ch9_exercise_method_second_moment_poisson_system

### 9.8 Schrodinger equation, gauge integrability, and exponential exit moments

- ID: `durrett_ch9_section_9_8_method_card`

- Method: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- New knowledge IDs: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

## Exercise Record Index

### 9.2 Heat equation, Brownian semigroup, and heat-kernel smoothing

- Exercise 9.2.A: method tags `heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness`; knowledge used `durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants`.
- Exercise 9.2.B: method tags `heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness`; knowledge used `durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants`.
- Exercise 9.2.C: method tags `heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness`; knowledge used `durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants`.
- Exercise 9.2.D: method tags `heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness`; knowledge used `durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants`.

### 9.3 Inhomogeneous heat equation and Duhamel occupation formulas

- Exercise 9.3.A: method tags `duhamel, source-term, occupation-integral, holder-regularity`; knowledge used `durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity`.
- Exercise 9.3.B: method tags `duhamel, source-term, occupation-integral, holder-regularity`; knowledge used `durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity`.
- Exercise 9.3.C: method tags `duhamel, source-term, occupation-integral, holder-regularity`; knowledge used `durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity`.
- Exercise 9.3.D: method tags `duhamel, source-term, occupation-integral, holder-regularity`; knowledge used `durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity`.
- Exercise 9.3.E: method tags `duhamel, source-term, occupation-integral, holder-regularity`; knowledge used `durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing`; new knowledge `ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity`.

### 9.4 Feynman-Kac formula for heat equations with potentials

- Exercise 9.4.A: method tags `feynman-kac, exponential-weight, potential, regularity-reduction`; knowledge used `durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat`; new knowledge `ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction`.
- Exercise 9.4.B: method tags `feynman-kac, exponential-weight, potential, regularity-reduction`; knowledge used `durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat`; new knowledge `ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction`.
- Exercise 9.4.C: method tags `feynman-kac, exponential-weight, potential, regularity-reduction`; knowledge used `durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat`; new knowledge `ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction`.
- Exercise 9.4.D: method tags `feynman-kac, exponential-weight, potential, regularity-reduction`; knowledge used `durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat`; new knowledge `ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction`.
- Exercise 9.4.E: method tags `feynman-kac, exponential-weight, potential, regularity-reduction`; knowledge used `durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat`; new knowledge `ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction`.

### 9.5 Dirichlet problem, Liouville principles, and boundary regularity

- Exercise 9.5.1: method tags `dirichlet-problem, harmonic-functions, regular-boundary, escape-probability`; knowledge used `durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition`; new knowledge `ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary`.
- Exercise 9.5.2: method tags `dirichlet-problem, harmonic-functions, regular-boundary, escape-probability`; knowledge used `durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition`; new knowledge `ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary`.
- Exercise 9.5.3: method tags `dirichlet-problem, harmonic-functions, regular-boundary, escape-probability`; knowledge used `durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition`; new knowledge `ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary`.
- Exercise 9.5.4: method tags `dirichlet-problem, harmonic-functions, regular-boundary, escape-probability`; knowledge used `durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition`; new knowledge `ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary`.
- Exercise 9.5.5: method tags `dirichlet-problem, harmonic-functions, regular-boundary, escape-probability`; knowledge used `durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition`; new knowledge `ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary`.

### 9.6 Green functions, occupation densities, and potential-kernel normalization

- Exercise 9.6.A: method tags `green-function, potential-kernel, occupation-time, distributional-laplacian`; knowledge used `durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions`; new knowledge `ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization`.
- Exercise 9.6.B: method tags `green-function, potential-kernel, occupation-time, distributional-laplacian`; knowledge used `durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions`; new knowledge `ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization`.
- Exercise 9.6.C: method tags `green-function, potential-kernel, occupation-time, distributional-laplacian`; knowledge used `durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions`; new knowledge `ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization`.
- Exercise 9.6.D: method tags `green-function, potential-kernel, occupation-time, distributional-laplacian`; knowledge used `durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions`; new knowledge `ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization`.
- Exercise 9.6.E: method tags `green-function, potential-kernel, occupation-time, distributional-laplacian`; knowledge used `durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions`; new knowledge `ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization`.

### 9.7 Poisson equation and exit-time moment recursions

- Exercise 9.7.1: method tags `poisson-equation, exit-time-moments, moment-recursion`; knowledge used `durrett_ch9_poisson_equation_representation, durrett_ch9_expected_exit_time_poisson, durrett_ch9_poisson_boundary_regular`; new knowledge `ch9_exercise_method_exit_time_moment_recursion, ch9_exercise_method_second_moment_poisson_system`.

### 9.8 Schrodinger equation, gauge integrability, and exponential exit moments

- Exercise 9.8.A: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.
- Exercise 9.8.B: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.
- Exercise 9.8.C: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.
- Exercise 9.8.D: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.
- Exercise 9.8.E: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.
- Exercise 9.8.F: method tags `schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold`; knowledge used `durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment`; new knowledge `ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion`.

# Durrett Chapter 9 Exercise LLM Viki

Source: `Probability/Exercises/Chapter9/Chapter9Exercises.tex` and compiled PDF.

These records are derived from the solved Chapter 9 exercises and verification tasks, with reusable method patterns for LLM retrieval.

## Method Cards

### 9.2 Heat equation, Brownian semigroup, and heat-kernel smoothing

- ID: `durrett_ch9_section_9_2_method_card`

- Method: Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.

- Tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- Knowledge used: durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing

- Exercise-derived knowledge: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

### 9.3 Inhomogeneous heat equation and Duhamel occupation formulas

- ID: `durrett_ch9_section_9_3_method_card`

- Method: Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.

- Tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- Exercise-derived knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

### 9.4 Feynman-Kac formula for heat equations with potentials

- ID: `durrett_ch9_section_9_4_method_card`

- Method: Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.

- Tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- Exercise-derived knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

### 9.5 Dirichlet problem, Liouville principles, and boundary regularity

- ID: `durrett_ch9_section_9_5_method_card`

- Method: Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.

- Tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- Exercise-derived knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

### 9.6 Green functions, occupation densities, and potential-kernel normalization

- ID: `durrett_ch9_section_9_6_method_card`

- Method: Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.

- Tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- Exercise-derived knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

### 9.7 Poisson equation and exit-time moment recursions

- ID: `durrett_ch9_section_9_7_method_card`

- Method: Identify exit-time moments by applying the Poisson representation recursively: the nth moment solves a Poisson equation with source n times the previous moment.

- Tags: poisson-equation, exit-time-moments, moment-recursion

- Knowledge used: durrett_ch9_poisson_equation_representation, durrett_ch9_expected_exit_time_poisson, durrett_ch9_poisson_boundary_regular

- Exercise-derived knowledge: ch9_exercise_method_exit_time_moment_recursion, ch9_exercise_method_second_moment_poisson_system

### 9.8 Schrodinger equation, gauge integrability, and exponential exit moments

- ID: `durrett_ch9_section_9_8_method_card`

- Method: Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.

- Tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- Exercise-derived knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

## New Knowledge

### Backward heat martingale template

- ID: `ch9_exercise_method_backward_heat_martingale_template`

- Kind: proof-template

- Summary: For u_t=(1/2)Delta u, apply Ito to u(t-s,B_s); the time derivative cancels the Brownian drift and leaves a local martingale.

- Use case: Section 9.2 martingale checks and any backward parabolic uniqueness argument.

- Tags: heat-equation, ito-formula, backward-time, martingale

### Bounded heat solution uniqueness by terminal martingale

- ID: `ch9_exercise_method_bounded_heat_uniqueness`

- Kind: proof-template

- Summary: Boundedness upgrades the backward local martingale to a uniformly integrable martingale; sending s up to t identifies u(t,x) with E_x f(B_t).

- Use case: Heat equation uniqueness and bounded parabolic Cauchy problems.

- Tags: heat-equation, uniqueness, uniform-integrability

### Gaussian approximate identity at t=0

- ID: `ch9_exercise_method_gaussian_approximate_identity`

- Kind: calculation-template

- Summary: Write B_t as sqrt(t)Z; bounded convergence proves E f(x_n+sqrt(t_n)Z) tends to f(x) when f is bounded continuous.

- Use case: Initial-condition verification for heat and Feynman-Kac formulas.

- Tags: heat-kernel, initial-condition, bounded-convergence

### Heat-kernel derivative majorants

- ID: `ch9_exercise_method_heat_kernel_derivative_majorants`

- Kind: regularity-template

- Summary: On t bounded away from zero, derivatives of the Gaussian kernel are polynomial times a Gaussian, giving integrable majorants for differentiating under the integral.

- Use case: Proving C^{1,2} smoothing for heat semigroups.

- Tags: heat-kernel, regularity, dominated-convergence

### Source-term martingale for inhomogeneous heat equations

- ID: `ch9_exercise_method_source_term_martingale`

- Kind: proof-template

- Summary: For u_t=(1/2)Delta u+g, add integral_0^s g(B_r)dr to u(t-s,B_s) so the drift cancels.

- Use case: Duhamel representation and source-term uniqueness.

- Tags: duhamel, source-term, martingale

### Duhamel uniqueness from bounded martingales

- ID: `ch9_exercise_method_duhamel_uniqueness`

- Kind: proof-template

- Summary: A bounded inhomogeneous heat solution with zero initial data equals E_x integral_0^t g(B_s)ds by stopping the source-term martingale at s=t.

- Use case: Identifying source-forced heat solutions and occupation integrals.

- Tags: duhamel, uniqueness, occupation-integral

### Short-time Markov-property PDE verification

- ID: `ch9_exercise_method_markov_property_pde_verification`

- Kind: calculation-template

- Summary: Use v(t+h,x)=E_x[v(t,B_h)+short-time reward], Taylor expand v(t,B_h), divide by h, and let h down to zero.

- Use case: Showing smooth Brownian representations solve heat, Poisson, and Feynman-Kac PDEs.

- Tags: markov-property, taylor-expansion, pde-verification

### Holder cancellation for singular heat-source kernels

- ID: `ch9_exercise_method_holder_cancels_kernel_singularity`

- Kind: regularity-template

- Summary: Subtract g(x) inside P_s g(x)-g(x); Holder continuity gives O(s^{alpha/2}), offsetting the small-time singularity.

- Use case: Regularity of inhomogeneous heat and potential-kernel formulas.

- Tags: holder-continuity, regularity, singular-kernel

### Exponential potential weight martingale

- ID: `ch9_exercise_method_exponential_weight_martingale`

- Kind: proof-template

- Summary: Multiply by exp(integral c(B_s)ds); the finite-variation product rule adds exactly the c u drift needed for cancellation.

- Use case: Feynman-Kac and Schrodinger martingale derivations.

- Tags: feynman-kac, exponential-weight, martingale

### Bounded Feynman-Kac uniqueness

- ID: `ch9_exercise_method_feynman_kac_bounded_uniqueness`

- Kind: proof-template

- Summary: If c and u are bounded on finite time intervals, the weighted martingale is bounded; stopping at t gives u(t,x)=E_x[f(B_t)exp(integral_0^t c(B_s)ds)].

- Use case: Parabolic PDEs with bounded multiplicative potentials.

- Tags: feynman-kac, boundedness, uniqueness

### Smooth Feynman-Kac short-time check

- ID: `ch9_exercise_method_smooth_feynman_kac_short_time_check`

- Kind: calculation-template

- Summary: Use v(t+h,x)=E_x[e^{int_0^h c(B_s)ds}v(t,B_h)], then expand the Brownian move and the exponential to get v_t=(1/2)Delta v+c v.

- Use case: Verifying smooth Feynman-Kac representations solve the PDE.

- Tags: feynman-kac, short-time, pde-verification

### Feynman-Kac smoothness by Duhamel reduction

- ID: `ch9_exercise_method_feynman_kac_duhamel_reduction`

- Kind: regularity-template

- Summary: Use e^{A_t}-1=integral_0^t c(B_s)e^{A_t-A_s}ds to decompose v into a heat solution plus an inhomogeneous heat solution with source c v.

- Use case: Regularity proofs for Feynman-Kac formulas with Holder f and c.

- Tags: feynman-kac, duhamel, regularity

### Liouville theorem via heat semigroup flattening

- ID: `ch9_exercise_method_heat_semigroup_liouville`

- Kind: proof-template

- Summary: A bounded harmonic h satisfies h(x)=E h(x+B_t); as t grows, two Gaussian laws with fixed mean separation have vanishing total variation distance, so h(x)=h(y).

- Use case: Bounded harmonic functions on all of R^d.

- Tags: liouville, harmonic-functions, heat-semigroup

### Recurrent Brownian motion forces nonnegative superharmonic functions constant

- ID: `ch9_exercise_method_recurrent_superharmonic_constancy`

- Kind: proof-template

- Summary: Nonnegative superharmonic functions yield supermartingales; in d=1,2 Brownian motion hits every small neighborhood, so optional stopping gives f(x)>=f(y) and symmetry gives equality.

- Use case: Superharmonic Liouville-type exercises in recurrent dimensions.

- Tags: superharmonic, recurrence, optional-stopping

### Radial superharmonic examples in high dimension

- ID: `ch9_exercise_method_radial_superharmonic_high_dimension`

- Kind: example-pattern

- Summary: Use the radial Laplacian g''(r)+(d-1)g'(r)/r; functions such as (1+r^2)^{-(d-2)/2} are smooth nonconstant nonnegative superharmonic for d>=3.

- Use case: Constructing counterexamples to recurrent-dimensional constancy in transient dimensions.

- Tags: radial-laplacian, superharmonic, dimension

### Escape probability is the nonuniqueness direction

- ID: `ch9_exercise_method_escape_probability_nonuniqueness`

- Kind: proof-template

- Summary: When Brownian motion can avoid exiting G, q(x)=P_x(tau=infinity) is a bounded zero-boundary harmonic function; all bounded zero-boundary solutions differ by c q.

- Use case: Dirichlet problems in domains where exit is not almost sure.

- Tags: dirichlet-problem, nonuniqueness, escape-probability

### Flat cone boundary regularity

- ID: `ch9_exercise_method_flat_cone_regular_boundary`

- Kind: proof-template

- Summary: Use zeros of the perpendicular Brownian coordinate and the induced Cauchy trace on the hyperplane to show Brownian motion immediately hits a flat exterior cone.

- Use case: Checking regular boundary points under weaker geometric exterior conditions.

- Tags: regular-boundary, cone-condition, brownian-trace

### Infinite ball occupation in recurrent dimensions

- ID: `ch9_exercise_method_recurrent_ball_occupation_infinite`

- Kind: proof-template

- Summary: Use recurrence to get infinitely many returns to a ball and the strong Markov property to sum positive occupation increments.

- Use case: Occupation-time dichotomy for Brownian motion in d<=2.

- Tags: occupation-time, recurrence, strong-markov-property

### Gamma change of variables for transient potential kernels

- ID: `ch9_exercise_method_transient_potential_kernel_gamma`

- Kind: calculation-template

- Summary: For d>=3, integrate the heat kernel over time and use s=|x-y|^2/(2t) to get Gamma(d/2-1)/(2 pi^{d/2}) |x-y|^{2-d}.

- Use case: Green-function and expected occupation-density calculations.

- Tags: potential-kernel, gamma-function, transience

### Modified potential kernels in recurrent dimensions

- ID: `ch9_exercise_method_recurrent_modified_potential_kernel`

- Kind: calculation-template

- Summary: Subtract a reference heat kernel before integrating over time; in d=1 this gives -|x-y| and in d=2 gives -(1/pi)log|x-y|.

- Use case: Using potential kernels when the full-space occupation integral diverges.

- Tags: potential-kernel, recurrent-dimensions, renormalization

### Frullani integral for the two-dimensional log kernel

- ID: `ch9_exercise_method_frullani_log_kernel`

- Kind: calculation-template

- Summary: After u=1/(2t), the difference of two planar heat kernels becomes integral_0^infty (e^{-a^2u}-e^{-u})du/u=-2log a.

- Use case: Deriving the d=2 logarithmic potential kernel.

- Tags: frullani, log-kernel, dimension-two

### Distributional delta normalization of Green kernels

- ID: `ch9_exercise_method_distributional_delta_normalization`

- Kind: proof-template

- Summary: Integrate by parts outside a small ball and let the radius shrink; the boundary flux fixes the constant so (1/2)Delta G=-delta_0.

- Use case: Checking Green-function constants and fundamental solutions.

- Tags: distributional-laplacian, green-function, flux

### Exit-time moment recursion

- ID: `ch9_exercise_method_exit_time_moment_recursion`

- Kind: proof-template

- Summary: For m_n(x)=E_x tau^n, the Markov property or Dynkin formula gives (1/2)Delta m_n=-n m_{n-1} with zero boundary values.

- Use case: Computing higher moments of Brownian exit times.

- Tags: exit-time, moment-recursion, poisson-equation

### Second exit-time moment Poisson system

- ID: `ch9_exercise_method_second_moment_poisson_system`

- Kind: calculation-template

- Summary: First solve (1/2)Delta v=-1 for v=E tau; then solve (1/2)Delta w=-2v for w=E tau^2, both with zero boundary values.

- Use case: Exercise 9.7.1 and second-moment exit-time computations.

- Tags: exit-time, second-moment, poisson-equation

### Schrodinger weighted martingale

- ID: `ch9_exercise_method_schrodinger_weighted_martingale`

- Kind: proof-template

- Summary: For (1/2)Delta u+c u=0, Ito plus the finite-variation product rule makes u(B_t)exp(integral_0^t c(B_s)ds) a local martingale before exit.

- Use case: Boundary Feynman-Kac formulas for elliptic equations with potential.

- Tags: schrodinger-equation, feynman-kac, martingale

### Gauge integrability condition

- ID: `ch9_exercise_method_gauge_integrability_condition`

- Kind: criterion

- Summary: Before applying boundary Feynman-Kac with positive potential, check w(x)=E_x exp(integral_0^tau c(B_s)ds); bounded c alone does not ensure finiteness.

- Use case: Avoiding false Schrodinger Feynman-Kac representations.

- Tags: gauge, integrability, positive-potential

### Interval eigenvalue threshold for exponential exit times

- ID: `ch9_exercise_method_interval_eigenvalue_threshold`

- Kind: calculation-template

- Summary: For tau exiting (-a,a), solve (1/2)u''+gamma u=0 with boundary value one; finiteness holds exactly below gamma=pi^2/(8a^2).

- Use case: Explicit exponential exit-time moments and gauge blow-up examples.

- Tags: exit-time, eigenvalue, interval

### Finite-gauge boundary Feynman-Kac uniqueness

- ID: `ch9_exercise_method_finite_gauge_boundary_feynman_kac`

- Kind: proof-template

- Summary: Finite bounded gauge controls the terminal exponential weight and kills the tail term, giving u(x)=E_x[f(B_tau)exp(integral_0^tau c(B_s)ds)].

- Use case: Uniqueness of bounded Schrodinger Dirichlet solutions.

- Tags: finite-gauge, dirichlet-problem, feynman-kac

### Local exit expansion for smooth Schrodinger representations

- ID: `ch9_exercise_method_smooth_schrodinger_local_exit_expansion`

- Kind: calculation-template

- Summary: Stop at a small ball, expand v(B_sigma) and exp(integral_0^sigma c(B_s)ds), then divide by E sigma to get (1/2)Delta v+c v=0.

- Use case: Verifying smooth Schrodinger Feynman-Kac formulas solve the PDE.

- Tags: schrodinger-equation, local-exit, taylor-expansion

## Exercise Records

### 9.2 Heat equation, Brownian semigroup, and heat-kernel smoothing

#### 9.2.A the backward heat martingale

- ID: `durrett_ch9_exercise_9_2_A`

- Method tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- Knowledge used: durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

#### 9.2.B uniqueness of bounded heat solutions

- ID: `durrett_ch9_exercise_9_2_B`

- Method tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- Knowledge used: durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

#### 9.2.C the initial condition for the Brownian formula

- ID: `durrett_ch9_exercise_9_2_C`

- Method tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- Knowledge used: durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

#### 9.2.D heat-kernel smoothing and the PDE

- ID: `durrett_ch9_exercise_9_2_D`

- Method tags: heat-equation, brownian-semigroup, kernel-smoothing, martingale-uniqueness

- Knowledge used: durrett_ch9_heat_backward_martingale, durrett_ch9_heat_equation_solution, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_backward_heat_martingale_template, ch9_exercise_method_bounded_heat_uniqueness, ch9_exercise_method_gaussian_approximate_identity, ch9_exercise_method_heat_kernel_derivative_majorants

### 9.3 Inhomogeneous heat equation and Duhamel occupation formulas

#### 9.3.A the source-term martingale

- ID: `durrett_ch9_exercise_9_3_A`

- Method tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

#### 9.3.B uniqueness and Duhamel's formula

- ID: `durrett_ch9_exercise_9_3_B`

- Method tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

#### 9.3.C smooth formula implies the PDE

- ID: `durrett_ch9_exercise_9_3_C`

- Method tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

#### 9.3.D initial condition

- ID: `durrett_ch9_exercise_9_3_D`

- Method tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

#### 9.3.E kernel form and regularity

- ID: `durrett_ch9_exercise_9_3_E`

- Method tags: duhamel, source-term, occupation-integral, holder-regularity

- Knowledge used: durrett_ch9_duhamel_inhomogeneous_heat, durrett_ch9_inhomogeneous_heat_regularity, durrett_ch9_heat_kernel_smoothing

- New knowledge: ch9_exercise_method_source_term_martingale, ch9_exercise_method_duhamel_uniqueness, ch9_exercise_method_markov_property_pde_verification, ch9_exercise_method_holder_cancels_kernel_singularity

### 9.4 Feynman-Kac formula for heat equations with potentials

#### 9.4.A the weighted martingale

- ID: `durrett_ch9_exercise_9_4_A`

- Method tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- New knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

#### 9.4.B uniqueness and the Feynman-Kac formula

- ID: `durrett_ch9_exercise_9_4_B`

- Method tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- New knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

#### 9.4.C a smooth Feynman-Kac formula solves the PDE

- ID: `durrett_ch9_exercise_9_4_C`

- Method tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- New knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

#### 9.4.D initial condition

- ID: `durrett_ch9_exercise_9_4_D`

- Method tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- New knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

#### 9.4.E reducing smoothness to Sections 9.2 and 9.3

- ID: `durrett_ch9_exercise_9_4_E`

- Method tags: feynman-kac, exponential-weight, potential, regularity-reduction

- Knowledge used: durrett_ch9_feynman_kac_forward, durrett_ch9_feynman_kac_smoothness, durrett_ch9_heat_equation_solution, durrett_ch9_duhamel_inhomogeneous_heat

- New knowledge: ch9_exercise_method_exponential_weight_martingale, ch9_exercise_method_feynman_kac_bounded_uniqueness, ch9_exercise_method_smooth_feynman_kac_short_time_check, ch9_exercise_method_feynman_kac_duhamel_reduction

### 9.5 Dirichlet problem, Liouville principles, and boundary regularity

#### 9.5.1 Exercise 9.5.1

- ID: `durrett_ch9_exercise_9_5_1`

- Method tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- New knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

#### 9.5.2 Exercise 9.5.2

- ID: `durrett_ch9_exercise_9_5_2`

- Method tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- New knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

#### 9.5.3 Exercise 9.5.3

- ID: `durrett_ch9_exercise_9_5_3`

- Method tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- New knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

#### 9.5.4 Exercise 9.5.4

- ID: `durrett_ch9_exercise_9_5_4`

- Method tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- New knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

#### 9.5.5 Exercise 9.5.5

- ID: `durrett_ch9_exercise_9_5_5`

- Method tags: dirichlet-problem, harmonic-functions, regular-boundary, escape-probability

- Knowledge used: durrett_ch9_dirichlet_problem_representation, durrett_ch9_mean_value_harmonicity, durrett_ch9_interior_smoothness_harmonic, durrett_ch9_regular_boundary_point, durrett_ch9_boundary_continuity_regular_points, durrett_ch9_cone_condition

- New knowledge: ch9_exercise_method_heat_semigroup_liouville, ch9_exercise_method_recurrent_superharmonic_constancy, ch9_exercise_method_radial_superharmonic_high_dimension, ch9_exercise_method_escape_probability_nonuniqueness, ch9_exercise_method_flat_cone_regular_boundary

### 9.6 Green functions, occupation densities, and potential-kernel normalization

#### 9.6.A occupation time of a ball

- ID: `durrett_ch9_exercise_9_6_A`

- Method tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- New knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

#### 9.6.B the potential kernel in $d\ge3$

- ID: `durrett_ch9_exercise_9_6_B`

- Method tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- New knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

#### 9.6.C the modified kernel in $d=1$

- ID: `durrett_ch9_exercise_9_6_C`

- Method tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- New knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

#### 9.6.D the modified kernel in $d=2$

- ID: `durrett_ch9_exercise_9_6_D`

- Method tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- New knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

#### 9.6.E distributional normalization

- ID: `durrett_ch9_exercise_9_6_E`

- Method tags: green-function, potential-kernel, occupation-time, distributional-laplacian

- Knowledge used: durrett_ch9_newtonian_potential_kernel, durrett_ch9_green_function_killed_domain, durrett_ch9_radial_harmonic_functions

- New knowledge: ch9_exercise_method_recurrent_ball_occupation_infinite, ch9_exercise_method_transient_potential_kernel_gamma, ch9_exercise_method_recurrent_modified_potential_kernel, ch9_exercise_method_frullani_log_kernel, ch9_exercise_method_distributional_delta_normalization

### 9.7 Poisson equation and exit-time moment recursions

#### 9.7.1 Exercise 9.7.1

- ID: `durrett_ch9_exercise_9_7_1`

- Method tags: poisson-equation, exit-time-moments, moment-recursion

- Knowledge used: durrett_ch9_poisson_equation_representation, durrett_ch9_expected_exit_time_poisson, durrett_ch9_poisson_boundary_regular

- New knowledge: ch9_exercise_method_exit_time_moment_recursion, ch9_exercise_method_second_moment_poisson_system

### 9.8 Schrodinger equation, gauge integrability, and exponential exit moments

#### 9.8.A the Schrodinger martingale

- ID: `durrett_ch9_exercise_9_8_A`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

#### 9.8.B why boundedness alone is not enough

- ID: `durrett_ch9_exercise_9_8_B`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

#### 9.8.C the gauge and finite-gauge uniqueness

- ID: `durrett_ch9_exercise_9_8_C`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

#### 9.8.D the smooth representation solves the PDE

- ID: `durrett_ch9_exercise_9_8_D`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

#### 9.8.E boundary condition at regular points

- ID: `durrett_ch9_exercise_9_8_E`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

#### 9.8.F exponential exit time from an interval

- ID: `durrett_ch9_exercise_9_8_F`

- Method tags: schrodinger-equation, gauge, exponential-exit-time, eigenvalue-threshold

- Knowledge used: durrett_ch9_schrodinger_martingale, durrett_ch9_schrodinger_nonuniqueness_warning, durrett_ch9_gauge_function, durrett_ch9_gauge_theorem_connected_domain, durrett_ch9_schrodinger_dirichlet_representation, durrett_ch9_schrodinger_boundary_regular, durrett_ch9_interval_exponential_exit_moment

- New knowledge: ch9_exercise_method_schrodinger_weighted_martingale, ch9_exercise_method_gauge_integrability_condition, ch9_exercise_method_interval_eigenvalue_threshold, ch9_exercise_method_finite_gauge_boundary_feynman_kac, ch9_exercise_method_smooth_schrodinger_local_exit_expansion

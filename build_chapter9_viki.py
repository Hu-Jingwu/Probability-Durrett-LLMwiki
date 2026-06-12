from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter9_Knowledge"
SOURCE = ROOT / "Probability/Textbook/Chapters/PTE-Chapter9.pdf"

CREATED = datetime.now(timezone.utc).isoformat()


def piece(pid, section, title, kind, summary, proof_idea, exam_use, pitfalls, tags, related=None):
    return {
        "id": f"durrett_ch9_{pid}",
        "source": "Rick Durrett, Probability: Theory and Examples, extracted Chapter 9 PDF",
        "source_file": str(SOURCE),
        "chapter": 9,
        "section": section,
        "title": title,
        "kind": kind,
        "summary": summary,
        "proof_idea": proof_idea,
        "exam_use": exam_use,
        "pitfalls": pitfalls,
        "tags": tags,
        "related_ids": related or [],
        "created_at": CREATED,
    }


PIECES = [
    piece(
        "ito_laplacian_martingale",
        "9.1 Martingales",
        "Ito-Laplacian martingale for Brownian motion",
        "theorem",
        "If v is C2 and the stochastic integral is square-integrable, then v(B_t)-1/2 integral_0^t Delta v(B_s) ds is a continuous martingale.",
        "Apply Ito's formula to v(B_t); the drift is exactly 1/2 Delta v and the gradient term is a martingale.",
        "The one-line engine behind harmonic functions, optional stopping, PDE uniqueness, and Green function computations.",
        "The integrability/localization condition is not decoration; without it the stochastic integral may only be local.",
        ["brownian-motion", "ito-formula", "laplacian", "martingale"],
    ),
    piece(
        "exit_time_ball_mean",
        "9.1 Martingales",
        "Mean exit time from a ball",
        "formula",
        "For d-dimensional Brownian motion started at |x|<R, the hitting time S_R of the sphere of radius R has E_x S_R=(R^2-|x|^2)/d.",
        "Stop the martingale |B_t|^2-dt at S_R wedge t and let t go to infinity.",
        "Use for expected lifetime in balls and as a quick check for Poisson-equation solutions.",
        "The dimension appears in the denominator because |B_t|^2-dt is summed over d coordinates.",
        ["exit-time", "ball", "optional-stopping"],
        ["durrett_ch9_ito_laplacian_martingale"],
    ),
    piece(
        "radial_harmonic_functions",
        "9.1 Martingales",
        "Radial harmonic test functions",
        "formula",
        "The radial functions phi(x)=log|x| in d=2 and phi(x)=|x|^(2-d) in d>=3 are harmonic off the origin.",
        "Differentiate radial functions or use the radial Laplacian formula g''(r)+(d-1)g'(r)/r.",
        "They convert annulus hitting probabilities into algebra.",
        "They are singular at zero, so stop before hitting the inner radius and localize with smooth compact modifications.",
        ["harmonic", "radial", "annulus"],
        ["durrett_ch9_ito_laplacian_martingale"],
    ),
    piece(
        "annulus_hitting_probability",
        "9.1 Martingales",
        "Annulus hitting probability",
        "formula",
        "For r<|x|<R, P_x(S_r<S_R)=[phi(R)-phi(x)]/[phi(R)-phi(r)], with phi radial harmonic as above.",
        "Optional stopping gives phi(x)=phi(r)P_x(S_r<S_R)+phi(R)P_x(S_R<S_r); solve the linear equation.",
        "This is the standard computation for recurrence in d=2 and transience in d>=3.",
        "Use the correct dimension-specific phi; the logarithmic d=2 case is a frequent source of wrong powers.",
        ["annulus", "hitting-probability", "recurrence", "transience"],
        ["durrett_ch9_radial_harmonic_functions"],
    ),
    piece(
        "two_dimensional_recurrence",
        "9.1 Martingales",
        "Two-dimensional Brownian recurrence",
        "theorem",
        "In d=2, Brownian motion hits every circle around the origin almost surely and visits every nonempty open set infinitely often.",
        "In the annulus formula, fix r and let R go to infinity; the logarithmic ratio tends to one.",
        "Use to decide whether planar Brownian motion returns to neighborhoods, not to exact points.",
        "Recurrence of neighborhoods does not mean hitting a prescribed point at positive time.",
        ["dimension-two", "recurrence", "hitting"],
        ["durrett_ch9_annulus_hitting_probability"],
    ),
    piece(
        "points_polar_in_d_ge_2",
        "9.1 Martingales",
        "Points are polar in dimensions at least two",
        "fact",
        "For d>=2, Brownian motion does not hit a fixed point at a positive time, even when started from that point.",
        "In d=2, let the inner radius shrink to zero in the annulus formula; in higher dimensions reduce or compare by projection.",
        "Prevents confusing recurrence in d=2 with point recurrence; important for punctured-domain examples.",
        "The definition of hitting zero uses t>0, so starting at zero is not a counterexample.",
        ["polar-sets", "hitting-points", "dimension"],
        ["durrett_ch9_two_dimensional_recurrence"],
    ),
    piece(
        "higher_dimensional_transience",
        "9.1 Martingales",
        "Transience in dimensions at least three",
        "theorem",
        "For d>=3, P_x(S_r<infinity)=(r/|x|)^(d-2) when |x|>r, and |B_t| tends to infinity almost surely.",
        "Let the outer radius go to infinity in the annulus formula, then use the strong Markov property over growing spheres.",
        "Use whenever a problem asks whether Brownian motion returns to bounded sets in high dimension.",
        "The limit |B_t| to infinity is almost sure but does not imply monotone radial motion.",
        ["transience", "dimension-three", "radial-process"],
        ["durrett_ch9_annulus_hitting_probability"],
    ),
    piece(
        "dvoresky_erdos_test",
        "9.1 Martingales",
        "Dvoretsky-Erdos lower envelope test",
        "theorem",
        "For d>=3 and positive decreasing g, P_0(|B_t|<=g(t)sqrt(t) infinitely often) is one or zero according as integral g(t)^(d-2) dt/t diverges or converges.",
        "This sharpens transience by testing repeated returns to shrinking multiples of sqrt(t).",
        "Useful as a recognition result for Brownian escape rates in advanced prelim-style questions.",
        "It concerns infinitely often behavior near infinity, not fixed-time Gaussian tails.",
        ["lower-envelope", "transience", "zero-one-law"],
        ["durrett_ch9_higher_dimensional_transience"],
    ),
    piece(
        "heat_backward_martingale",
        "9.2 Heat Equation",
        "Backward heat-equation martingale",
        "theorem",
        "If u_t=1/2 Delta u, then M_s=u(t-s,B_s) is a local martingale on 0<=s<=t.",
        "Apply Ito's formula to the space-time process (t-s,B_s); the time derivative cancels the Brownian drift.",
        "This is the probabilistic uniqueness mechanism for the heat equation.",
        "The backward time t-s is essential; using t+s changes the sign.",
        ["heat-equation", "space-time", "martingale"],
        ["durrett_ch9_ito_laplacian_martingale"],
    ),
    piece(
        "heat_equation_solution",
        "9.2 Heat Equation",
        "Heat equation solution by Brownian expectation",
        "theorem",
        "The bounded solution with initial condition f is v(t,x)=E_x f(B_t), equivalently convolution with the Gaussian heat kernel.",
        "Boundedness makes the backward martingale uniformly integrable, so u(t,x)=E_x u(0,B_t).",
        "Use to solve Cauchy heat problems and identify semigroup smoothing.",
        "Continuity at t=0 requires continuity of f; boundedness alone is not enough for the boundary condition.",
        ["heat-kernel", "brownian-semigroup", "uniqueness"],
        ["durrett_ch9_heat_backward_martingale"],
    ),
    piece(
        "heat_kernel_smoothing",
        "9.2 Heat Equation",
        "Gaussian heat kernel smoothing",
        "regularity",
        "For bounded continuous f, v(t,x)=integral (2 pi t)^(-d/2) exp(-|x-y|^2/(2t)) f(y) dy is C1,2 for t>0.",
        "Differentiate the Gaussian kernel under the integral for positive times.",
        "Turns probabilistic representation into an actual classical solution.",
        "The smoothing is for t>0; behavior at t=0 is controlled by the initial data.",
        ["regularity", "heat-kernel", "smoothing"],
        ["durrett_ch9_heat_equation_solution"],
    ),
    piece(
        "duhamel_inhomogeneous_heat",
        "9.3 Inhomogeneous Heat Equation",
        "Duhamel representation for inhomogeneous heat equation",
        "formula",
        "For u_t=1/2 Delta u+g with zero initial data, the bounded solution is v(t,x)=E_x integral_0^t g(B_s) ds.",
        "Ito's formula shows u(t-s,B_s)+integral_0^s g(B_r)dr is a local martingale; stop at s=t.",
        "Use for heat equations with source terms and for occupation-time interpretations.",
        "With nonzero f, add the homogeneous solution E_x f(B_t).",
        ["inhomogeneous-heat", "duhamel", "occupation-time"],
        ["durrett_ch9_heat_equation_solution"],
    ),
    piece(
        "inhomogeneous_heat_regularity",
        "9.3 Inhomogeneous Heat Equation",
        "Holder source gives C1,2 inhomogeneous solution",
        "regularity",
        "If g is Holder continuous, then v(t,x)=E_x integral_0^t g(B_s) ds is C1,2 and solves the inhomogeneous heat equation.",
        "Write v as integration of heat kernels against g and use parabolic regularity estimates.",
        "A checklist item: representation plus Holder regularity gives a classical PDE solution.",
        "Continuity of g is natural, but Holder regularity is the clean sufficient condition used here.",
        ["holder-continuity", "regularity", "inhomogeneous-heat"],
        ["durrett_ch9_duhamel_inhomogeneous_heat"],
    ),
    piece(
        "feynman_kac_forward",
        "9.4 Feynman-Kac Formula",
        "Feynman-Kac formula for the heat equation with potential",
        "theorem",
        "For u_t=1/2 Delta u+c(x)u and initial f, the bounded solution is v(t,x)=E_x[f(B_t) exp(integral_0^t c(B_s)ds)].",
        "Use Ito plus the product rule on u(t-s,B_s) exp(integral_0^s c(B_r)dr); the drift cancels.",
        "Use for heat equations with growth/decay potential and moment-generating questions for occupation integrals.",
        "Check the sign convention: the chapter's plus c u corresponds to exp(+ integral c).",
        ["feynman-kac", "potential", "heat-equation"],
        ["durrett_ch9_heat_backward_martingale"],
    ),
    piece(
        "feynman_kac_smoothness",
        "9.4 Feynman-Kac Formula",
        "Feynman-Kac smoothness via reduction",
        "proof-template",
        "If f and c are Holder continuous, the Feynman-Kac representation is C1,2 and solves the PDE.",
        "Split the representation into a heat part and an inhomogeneous heat part with source c(x)v(t,x).",
        "Use when asked to justify that a probabilistic formula is a classical solution.",
        "Boundedness gives a representation; regularity needs additional assumptions.",
        ["regularity", "feynman-kac", "holder-continuity"],
        ["durrett_ch9_feynman_kac_forward", "durrett_ch9_inhomogeneous_heat_regularity"],
    ),
    piece(
        "dirichlet_problem_representation",
        "9.5 Dirichlet Problem",
        "Dirichlet problem representation",
        "theorem",
        "For a domain G with exit time tau, any bounded harmonic solution with boundary data f must be v(x)=E_x f(B_tau).",
        "Run u(B_t) until exit, use bounded martingale convergence, and identify the terminal boundary value.",
        "The central Brownian representation for harmonic measure and boundary-value problems.",
        "The formula can fail to satisfy the boundary condition at irregular boundary points.",
        ["dirichlet-problem", "harmonic-measure", "exit-time"],
        ["durrett_ch9_ito_laplacian_martingale"],
    ),
    piece(
        "mean_value_harmonicity",
        "9.5 Dirichlet Problem",
        "Mean-value property implies harmonicity",
        "proof-template",
        "If v(x)=E_x v(B_tau_B) for every small ball B around x and v is C2, then Delta v(x)=0.",
        "Use Taylor expansion at x and the symmetry of the exit distribution from a ball.",
        "Use to move from Brownian representations to Laplace's equation without stochastic calculus.",
        "The ball must be compactly contained in the domain.",
        ["mean-value-property", "harmonic", "laplace-equation"],
        ["durrett_ch9_dirichlet_problem_representation"],
    ),
    piece(
        "interior_smoothness_harmonic",
        "9.5 Dirichlet Problem",
        "Interior smoothness of Brownian harmonic functions",
        "regularity",
        "The Brownian Dirichlet solution v(x)=E_x f(B_tau) is C-infinity inside G.",
        "Inside a ball, v equals an average over the sphere with the smooth Poisson kernel, so differentiation is allowed.",
        "Lets you assert interior classical harmonicity even with only bounded boundary data.",
        "Interior smoothness says nothing by itself about boundary continuity.",
        ["harmonic-functions", "smoothness", "poisson-kernel"],
        ["durrett_ch9_dirichlet_problem_representation"],
    ),
    piece(
        "regular_boundary_point",
        "9.5 Dirichlet Problem",
        "Regular boundary point",
        "definition",
        "A boundary point y is regular for G if Brownian motion started at y exits G immediately: P_y(tau=0)=1.",
        "Regularity is characterized probabilistically by immediate contact with the complement.",
        "Use to decide where the Brownian Dirichlet solution attains the prescribed boundary value.",
        "A boundary point can be topologically present but probabilistically invisible.",
        ["regular-boundary", "dirichlet-problem", "brownian-exit"],
    ),
    piece(
        "boundary_continuity_regular_points",
        "9.5 Dirichlet Problem",
        "Boundary continuity at regular points",
        "theorem",
        "If f is bounded continuous and y is a regular boundary point, then E_x f(B_tau) tends to f(y) as x in G tends to y.",
        "Lower semicontinuity of x -> P_x(tau<=t) plus Brownian path continuity forces exits near y with high probability.",
        "This is the precise condition for the Dirichlet representation to satisfy the boundary data.",
        "Do not claim boundary convergence at every boundary point without checking regularity.",
        ["boundary-continuity", "regular-point", "dirichlet-problem"],
        ["durrett_ch9_regular_boundary_point"],
    ),
    piece(
        "cone_condition",
        "9.5 Dirichlet Problem",
        "Cone condition for regularity",
        "criterion",
        "If the complement of G contains a cone with vertex y inside some small ball, then y is a regular boundary point.",
        "Brownian motion hits such exterior cones immediately enough to force tau=0 from the boundary.",
        "A practical geometric sufficient condition for boundary regularity.",
        "It is sufficient, not necessary; failure of a cone condition does not automatically mean irregularity.",
        ["cone-condition", "regular-boundary", "geometry"],
        ["durrett_ch9_boundary_continuity_regular_points"],
    ),
    piece(
        "punctured_domain_warning",
        "9.5 Dirichlet Problem",
        "Punctured-domain boundary warning",
        "example-pattern",
        "Thin removed sets can fail to influence Brownian exit, so a bounded harmonic representation may ignore assigned values on those sets.",
        "Use polarity of points or lines in higher dimensions to see that Brownian motion almost surely misses the thin set.",
        "Explains why Dirichlet boundary data must be paired with regularity assumptions.",
        "A discontinuity of the probabilistic solution at an irregular point is not a contradiction of uniqueness inside G.",
        ["irregular-boundary", "polar-sets", "examples"],
        ["durrett_ch9_points_polar_in_d_ge_2", "durrett_ch9_regular_boundary_point"],
    ),
    piece(
        "half_space_poisson_kernel",
        "9.5.1 Exit Distributions",
        "Half-space Poisson kernel",
        "formula",
        "For the upper half-space H, the exit distribution on the boundary has density C_d y/(|x-theta|^2+y^2)^(d/2).",
        "Check the kernel is harmonic in H, normalizes to one, and approximates boundary data as y down to zero.",
        "Use to compute Brownian exit distributions from a half-space; in d=2 it gives the Cauchy density.",
        "Track dimension conventions: the boundary variable theta lives in d-1 dimensions.",
        ["poisson-kernel", "half-space", "exit-distribution"],
        ["durrett_ch9_dirichlet_problem_representation"],
    ),
    piece(
        "ball_poisson_kernel",
        "9.5.1 Exit Distributions",
        "Unit-ball Poisson kernel",
        "formula",
        "For the unit ball D, E_x f(B_tau)=integral_{partial D} [(1-|x|^2)/|x-y|^d] f(y) pi(dy).",
        "Show the kernel is harmonic in x and reproduces the boundary data as x approaches regular boundary points.",
        "Use to solve explicit Dirichlet problems in balls.",
        "The surface measure pi is normalized to be a probability measure in the chapter's formula.",
        ["poisson-kernel", "ball", "harmonic-measure"],
        ["durrett_ch9_dirichlet_problem_representation"],
    ),
    piece(
        "newtonian_potential_kernel",
        "9.6 Green's Functions and Potential Kernels",
        "Brownian potential kernel in R^d",
        "formula",
        "The expected occupation density of Brownian motion is the potential kernel G(x,y), proportional to |x-y|^(2-d) for d>=3 and to -log|x-y| in d=2 after domain adjustment.",
        "Integrate the Gaussian transition density over time and evaluate the resulting radial integral.",
        "Use to turn occupation-time expectations into spatial integrals.",
        "In recurrent dimensions the full-space occupation integral can diverge, so constants and killed domains matter.",
        ["green-function", "potential-kernel", "occupation-density"],
    ),
    piece(
        "green_function_killed_domain",
        "9.6 Green's Functions and Potential Kernels",
        "Killed-domain Green function",
        "definition",
        "For Brownian motion killed on leaving D, G_D(x,y) is the density satisfying E_x integral_0^tau f(B_t)dt = integral_D G_D(x,y)f(y)dy.",
        "Subtract the expected potential contributed after exit from the full-space potential.",
        "The bridge between Brownian occupation times and Poisson's equation.",
        "The Green function depends on the domain and boundary killing, not only on |x-y|.",
        ["green-function", "killed-brownian-motion", "occupation-time"],
        ["durrett_ch9_newtonian_potential_kernel"],
    ),
    piece(
        "poisson_equation_representation",
        "9.7 Poisson's Equation",
        "Poisson equation representation",
        "theorem",
        "For 1/2 Delta u=-g in G with zero boundary data, any bounded solution must be v(x)=E_x integral_0^tau g(B_t)dt.",
        "The process u(B_t)+integral_0^t g(B_s)ds is a local martingale up to tau; stop and let t approach tau.",
        "Use for expected occupation times, expected exit times, and source-term boundary problems.",
        "Sign conventions vary; here the PDE is 1/2 Delta u=-g for a positive occupation formula.",
        ["poisson-equation", "occupation-time", "exit-time"],
        ["durrett_ch9_green_function_killed_domain"],
    ),
    piece(
        "expected_exit_time_poisson",
        "9.7 Poisson's Equation",
        "Expected exit time solves Poisson's equation",
        "example-pattern",
        "Taking g=1 gives v(x)=E_x tau, which solves 1/2 Delta v=-1 in G with zero boundary values at regular points.",
        "This is the Poisson representation specialized to unit source.",
        "A common prelim computation: guess radial v in a ball and verify by Laplacian and boundary values.",
        "Finite expectation needs domain control; unbounded domains may have infinite exit time.",
        ["expected-exit-time", "poisson-equation", "radial-solution"],
        ["durrett_ch9_poisson_equation_representation", "durrett_ch9_exit_time_ball_mean"],
    ),
    piece(
        "poisson_boundary_regular",
        "9.7 Poisson's Equation",
        "Poisson solution vanishes at regular boundary points",
        "theorem",
        "If G and g are bounded and y is a regular boundary point, then v(x)=E_x integral_0^tau g(B_t)dt tends to zero as x tends to y from inside G.",
        "Regularity makes tau small with high probability; boundedness controls the remaining tail.",
        "Use to verify the zero boundary condition for occupation-time solutions.",
        "Regularity and boundedness assumptions are doing real work here.",
        ["boundary-condition", "poisson-equation", "regular-point"],
        ["durrett_ch9_regular_boundary_point", "durrett_ch9_poisson_equation_representation"],
    ),
    piece(
        "green_function_half_space",
        "9.7.1 Occupation Times",
        "Half-space Green function by reflection",
        "formula",
        "For the half-space, the killed Green function equals the full-space potential at y minus the full-space potential at the reflected point y_bar.",
        "Use the reflection principle/image method so the difference vanishes on the boundary.",
        "Compute occupation times before exiting a half-space.",
        "The reflected term has the same singularity mirrored across the boundary, not at the original y.",
        ["green-function", "reflection-principle", "half-space"],
        ["durrett_ch9_green_function_killed_domain"],
    ),
    piece(
        "green_function_ball_kelvin",
        "9.7.1 Occupation Times",
        "Ball Green function by Kelvin transform",
        "formula",
        "For the unit ball in d>=3, G_D(x,y)=G(x,y)-|y|^(2-d)G(x,y/|y|^2); a logarithmic analog holds in d=2.",
        "The Kelvin-reflected singularity makes the boundary value cancel on |x|=1.",
        "Use for explicit occupation densities in balls.",
        "The formula has a singular-looking y=0 case that must be handled by a limit or separately.",
        ["green-function", "unit-ball", "kelvin-transform"],
        ["durrett_ch9_green_function_killed_domain", "durrett_ch9_ball_poisson_kernel"],
    ),
    piece(
        "schrodinger_martingale",
        "9.8 Schrodinger Equation",
        "Schrodinger boundary-value martingale",
        "theorem",
        "For 1/2 Delta u+c(x)u=0 in G, u(B_t) exp(integral_0^t c(B_s)ds) is a local martingale up to the exit time.",
        "Apply Ito's formula and the product rule; the PDE cancels the drift after weighting by the exponential potential.",
        "Foundation for boundary Feynman-Kac formulas and exponential exit-time moments.",
        "The sign of c controls integrability; positive c can make the expectation infinite.",
        ["schrodinger-equation", "feynman-kac", "local-martingale"],
        ["durrett_ch9_feynman_kac_forward"],
    ),
    piece(
        "schrodinger_nonuniqueness_warning",
        "9.8 Schrodinger Equation",
        "Positive potential can destroy bounded representation",
        "example-pattern",
        "For G=(-a,a), c=gamma>0, and boundary value 1, the ODE solution exists only away from eigenvalue obstructions and exponential exit moments can blow up.",
        "Solve 1/2 u''+gamma u=0 with boundary values and inspect zeros of cos(a sqrt(2 gamma)).",
        "Use as a warning that Feynman-Kac with positive potential needs integrability assumptions.",
        "Bounded c does not automatically imply E_x exp(integral_0^tau c(B_s)ds) is finite.",
        ["schrodinger-equation", "eigenvalues", "integrability"],
        ["durrett_ch9_schrodinger_martingale"],
    ),
    piece(
        "gauge_function",
        "9.8 Schrodinger Equation",
        "Gauge function for exponential lifetime integrability",
        "definition",
        "The gauge w(x)=E_x exp(integral_0^tau c(B_s)ds) measures whether the Schrodinger Feynman-Kac representation is finite.",
        "Local exponential exit-time bounds plus a covering argument propagate finiteness through connected domains.",
        "Check this before asserting uniqueness or boundary representations with exponential weights.",
        "Finiteness at one point and boundedness over the domain require separate hypotheses in the chapter.",
        ["gauge", "exponential-moment", "schrodinger-equation"],
        ["durrett_ch9_schrodinger_nonuniqueness_warning"],
    ),
    piece(
        "small_set_exponential_exit_bound",
        "9.8 Schrodinger Equation",
        "Small-set exponential exit bound",
        "lemma",
        "For each theta>0, sufficiently small open sets H have uniformly bounded E_x exp(theta tau_H).",
        "Use occupation-time/tail bounds for Brownian exit from small-measure sets and sum the exponential series.",
        "Technical tool that makes the gauge theorem work.",
        "Small Lebesgue measure is the key condition, not merely small diameter in the statement.",
        ["exit-time", "exponential-moment", "small-set"],
        ["durrett_ch9_gauge_function"],
    ),
    piece(
        "gauge_theorem_connected_domain",
        "9.8 Schrodinger Equation",
        "Gauge finiteness propagates on connected domains",
        "theorem",
        "If G is connected and the gauge w is not identically infinite, then w(x)<infinity for every x in G; if |G|<infinity, w is bounded.",
        "Local comparison across balls gives openness of the finite set, and connectedness plus small-set control gives closed propagation.",
        "Use to justify uniform integrability in Schrodinger uniqueness proofs.",
        "Connectedness matters; separate components need separate checks.",
        ["gauge-theorem", "connected-domain", "boundedness"],
        ["durrett_ch9_gauge_function", "durrett_ch9_small_set_exponential_exit_bound"],
    ),
    piece(
        "schrodinger_dirichlet_representation",
        "9.8 Schrodinger Equation",
        "Schrodinger Dirichlet representation",
        "theorem",
        "Under bounded connected domain, bounded continuous f and c, and finite gauge, the bounded solution is v(x)=E_x[f(B_tau) exp(integral_0^tau c(B_s)ds)].",
        "Stop the weighted martingale, use boundedness of the gauge for uniform integrability, and pass to the exit time.",
        "Use for boundary-value problems with killing or creation potentials.",
        "Without the finite-gauge assumption, the formula may be infinite or uniqueness may fail.",
        ["schrodinger-equation", "dirichlet-problem", "feynman-kac"],
        ["durrett_ch9_schrodinger_martingale", "durrett_ch9_gauge_theorem_connected_domain"],
    ),
    piece(
        "schrodinger_boundary_regular",
        "9.8 Schrodinger Equation",
        "Schrodinger boundary condition at regular points",
        "theorem",
        "At regular boundary points, the Schrodinger representation tends to the boundary value f(y).",
        "Split paths by small exit time and nearby exit location, then control the remaining event with bounded gauge.",
        "Use to finish verification of boundary data for the weighted representation.",
        "The exponential weight adds a tail-control requirement absent from the plain Dirichlet problem.",
        ["boundary-condition", "regular-point", "schrodinger-equation"],
        ["durrett_ch9_schrodinger_dirichlet_representation", "durrett_ch9_regular_boundary_point"],
    ),
    piece(
        "schrodinger_smoothness",
        "9.8 Schrodinger Equation",
        "Holder potential gives C2 Schrodinger solution",
        "regularity",
        "With the chapter's bounded-domain/gauge assumptions and Holder continuous c, the Schrodinger representation is C2 and solves 1/2 Delta v+c v=0.",
        "Reduce locally to Poisson-equation regularity with source c(x)v(x).",
        "Use to upgrade the probabilistic representation to a classical solution.",
        "Smoothness is interior; boundary regularity is a separate issue.",
        ["regularity", "holder-continuity", "schrodinger-equation"],
        ["durrett_ch9_schrodinger_dirichlet_representation", "durrett_ch9_poisson_equation_representation"],
    ),
    piece(
        "interval_exponential_exit_moment",
        "9.8 Schrodinger Equation",
        "Exponential exit moment from an interval",
        "formula",
        "For tau exiting (-a,a), E_x exp(gamma tau)=cos(x sqrt(2 gamma))/cos(a sqrt(2 gamma)) when 0<gamma<pi^2/(8a^2), and is infinite at or above the threshold.",
        "Solve the ODE 1/2 u''+gamma u=0 with boundary value one and use the gauge/uniqueness result below the first eigenvalue.",
        "A high-yield explicit computation connecting Brownian exit times with eigenvalues.",
        "The threshold is the first Dirichlet eigenvalue for the interval; at the threshold the denominator vanishes.",
        ["exit-time", "exponential-moment", "eigenvalue", "interval"],
        ["durrett_ch9_schrodinger_nonuniqueness_warning", "durrett_ch9_gauge_theorem_connected_domain"],
    ),
]


SECTION_GUIDES = [
    {
        "section": "9.1 Martingales",
        "study_goal": "Use Ito's formula and optional stopping to compute multidimensional Brownian hitting probabilities and recurrence/transience facts.",
        "must_master": ["Ito-Laplacian martingale", "radial harmonic functions", "annulus hitting", "d=2 recurrence", "d>=3 transience"],
        "prelim_angle": "Most computations reduce to choosing the right harmonic function and stopping at sphere hitting times.",
    },
    {
        "section": "9.2 Heat Equation",
        "study_goal": "Represent bounded heat-equation solutions as Brownian expectations and connect them to Gaussian kernels.",
        "must_master": ["backward martingale", "heat kernel", "initial continuity", "smoothing"],
        "prelim_angle": "A standard way to turn PDE uniqueness and existence into a martingale argument.",
    },
    {
        "section": "9.3 Inhomogeneous Heat Equation",
        "study_goal": "Handle source terms through Brownian occupation integrals.",
        "must_master": ["Duhamel formula", "source-term martingale", "Holder regularity"],
        "prelim_angle": "Recognize integral_0^t g(B_s) ds as the probabilistic form of a forcing term.",
    },
    {
        "section": "9.4 Feynman-Kac Formula",
        "study_goal": "Use exponential weights to solve heat equations with multiplicative potentials.",
        "must_master": ["weighted martingale", "sign convention", "boundedness", "Holder smoothness"],
        "prelim_angle": "Converts PDEs with c(x)u terms into expectations of exponential occupation functionals.",
    },
    {
        "section": "9.5 Dirichlet Problem",
        "study_goal": "Represent harmonic boundary-value problems with Brownian exit distributions and understand boundary regularity.",
        "must_master": ["harmonic measure", "regular boundary points", "cone condition", "Poisson kernels"],
        "prelim_angle": "Boundary behavior is often the hidden issue; regular points are the right probabilistic condition.",
    },
    {
        "section": "9.6 Green's Functions and Potential Kernels",
        "study_goal": "Interpret Green functions as Brownian occupation densities.",
        "must_master": ["potential kernel", "killed Green function", "occupation density"],
        "prelim_angle": "Green functions make expected time spent in a set into an integral kernel calculation.",
    },
    {
        "section": "9.7 Poisson's Equation",
        "study_goal": "Solve Poisson equations using occupation times and Green functions.",
        "must_master": ["Poisson representation", "expected exit time", "regular boundary zero condition", "reflection/Kelvin formulas"],
        "prelim_angle": "Expected exit times and occupation times are usually Poisson-equation problems in disguise.",
    },
    {
        "section": "9.8 Schrodinger Equation",
        "study_goal": "Solve elliptic equations with potentials using exponential weights and gauge integrability.",
        "must_master": ["weighted martingale", "gauge function", "finite-gauge theorem", "interval eigenvalue threshold"],
        "prelim_angle": "The main exam trap is assuming exponential exit-time expectations are finite without checking the gauge.",
    },
]


def write_jsonl(path: Path, rows):
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    write_jsonl(OUT / "chapter9_knowledge_pieces.jsonl", PIECES)
    write_jsonl(OUT / "chapter9_section_guides.jsonl", SECTION_GUIDES)

    manifest = {
        "name": "durrett_chapter9_multidimensional_brownian_motion_llm_viki",
        "description": "Curated LLM/Viki-style knowledge pieces for Chapter 9 of Durrett Probability: Theory and Examples.",
        "source_file": str(SOURCE),
        "created_at": CREATED,
        "piece_count": len(PIECES),
        "section_count": len(SECTION_GUIDES),
        "files": [
            "chapter9_knowledge_pieces.jsonl",
            "chapter9_section_guides.jsonl",
            "chapter9_viki.md",
            "chapter9_flashcards.tsv",
            "manifest.json",
        ],
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    md = ["# Durrett Chapter 9 LLM Viki: Multidimensional Brownian Motion\n"]
    md.append("Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter9.pdf`.\n")
    md.append("These are curated study/LLM retrieval pieces, not verbatim textbook notes.\n")
    md.append("## Section Guides\n")
    for guide in SECTION_GUIDES:
        md.append(f"### {guide['section']}\n")
        md.append(f"- Goal: {guide['study_goal']}\n")
        md.append(f"- Must master: {', '.join(guide['must_master'])}\n")
        md.append(f"- Prelim angle: {guide['prelim_angle']}\n")
    md.append("## Knowledge Pieces\n")
    for item in PIECES:
        md.append(f"### {item['title']}\n")
        md.append(f"- ID: `{item['id']}`\n")
        md.append(f"- Section: {item['section']}\n")
        md.append(f"- Kind: {item['kind']}\n")
        md.append(f"- Summary: {item['summary']}\n")
        md.append(f"- Proof idea: {item['proof_idea']}\n")
        md.append(f"- Exam use: {item['exam_use']}\n")
        md.append(f"- Pitfall: {item['pitfalls']}\n")
        md.append(f"- Tags: {', '.join(item['tags'])}\n")
    (OUT / "chapter9_viki.md").write_text("\n".join(md), encoding="utf-8")

    flash = ["id\tfront\tback\ttags"]
    for item in PIECES:
        front = f"{item['title']} ({item['section']})"
        back = f"{item['summary']} Exam use: {item['exam_use']} Pitfall: {item['pitfalls']}"
        flash.append(f"{item['id']}\t{front}\t{back}\t{','.join(item['tags'])}")
    (OUT / "chapter9_flashcards.tsv").write_text("\n".join(flash) + "\n", encoding="utf-8")

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

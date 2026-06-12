from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter3_Knowledge"
SOURCE_TEX = ROOT / "Probability/Exercises/Chapter3/Chapter3Exercises.tex"
SOURCE_PDF = ROOT / "Probability/Exercises/Chapter3/Chapter3Exercises.pdf"

CREATED = datetime.now(timezone.utc).isoformat()

SECTION_TOPICS = {
    "3.1": "De Moivre-Laplace theorem, Stirling asymptotics, and binomial normal approximation",
    "3.2": "Weak convergence, Portmanteau criteria, tightness, and continuous mapping",
    "3.3": "Characteristic functions, inversion, moments, independence, and Levy continuity",
    "3.4": "Central limit theorems, triangular arrays, Lindeberg, and normal approximations",
    "3.5": "Local limit theorems and lattice-level normal approximation",
    "3.6": "Total variation, couplings, and maximal coupling construction",
    "3.7": "Poisson processes, exponential waiting times, thinning, splitting, and uniform spacings",
    "3.8": "Stable laws, heavy tails, positive stable laws, and subordination",
    "3.9": "Infinitely divisible distributions and Levy measures",
    "3.10": "Multidimensional distributions, copulas, joint characteristic functions, and multivariate normal laws",
}

METHOD_CARDS = [
    {
        "section": "3.1",
        "method_summary": "Use Stirling's formula and product-log expansions to turn exact binomial or rare-event probabilities into normal or exponential limits.",
        "method_tags": ["stirling", "binomial", "product-limit", "normal-approximation"],
        "new_knowledge_ids": [
            "exercise_ch3_stirling_binomial_ratio_method",
            "exercise_ch3_product_to_exponential_method",
            "exercise_ch3_linear_deviation_not_clt",
        ],
    },
    {
        "section": "3.2",
        "method_summary": "Translate weak convergence into CDF continuity-point checks, bounded continuous test functions, open/closed set bounds, tightness, and continuous mappings.",
        "method_tags": ["weak-convergence", "portmanteau", "tightness", "continuous-mapping", "slutsky"],
        "new_knowledge_ids": [
            "exercise_ch3_buffer_events_for_weak_convergence",
            "exercise_ch3_subsequence_principle_for_limits",
            "exercise_ch3_tightness_by_tail_or_moment_bound",
            "exercise_ch3_converging_together_slutsky_template",
        ],
    },
    {
        "section": "3.3",
        "method_summary": "Identify distributions and limits through characteristic functions; use transform tables, Taylor expansions at zero, inversion, and factorization.",
        "method_tags": ["characteristic-functions", "levy-continuity", "moments", "inversion", "independence"],
        "new_knowledge_ids": [
            "exercise_ch3_cf_table_matching",
            "exercise_ch3_cf_taylor_moment_extraction",
            "exercise_ch3_cf_factorization_independence",
            "exercise_ch3_inversion_for_lattice_or_density",
        ],
    },
    {
        "section": "3.4",
        "method_summary": "Choose the correct normalization, verify Lindeberg or Lyapunov conditions, and reduce random-index or triangular-array sums to known CLT forms.",
        "method_tags": ["clt", "lindeberg", "lyapunov", "triangular-array", "random-sums"],
        "new_knowledge_ids": [
            "exercise_ch3_lindeberg_truncation_check",
            "exercise_ch3_lyapunov_shortcut",
            "exercise_ch3_random_index_clt_template",
            "exercise_ch3_poisson_or_multinomial_clt_scaling",
        ],
    },
    {
        "section": "3.5",
        "method_summary": "Use local limit theorem thinking when a problem asks for point probabilities or lattice-scale approximations rather than only distributional convergence.",
        "method_tags": ["local-limit", "lattice", "point-probability", "normal-density"],
        "new_knowledge_ids": [
            "exercise_ch3_local_limit_vs_global_clt",
            "exercise_ch3_lattice_span_check",
        ],
    },
    {
        "section": "3.6",
        "method_summary": "Prove total variation bounds by coupling, and prove sharpness by constructing a maximal coupling from the common mass of two measures.",
        "method_tags": ["coupling", "total-variation", "maximal-coupling", "discrete-measures"],
        "new_knowledge_ids": [
            "exercise_ch3_coupling_bounds_total_variation",
            "exercise_ch3_maximal_coupling_common_mass",
        ],
    },
    {
        "section": "3.7",
        "method_summary": "Exploit exponential survival functions, Poisson thinning/splitting, and Dirichlet uniform spacings to solve process and occupancy limits.",
        "method_tags": ["poisson-process", "exponential", "thinning", "splitting", "uniform-spacings"],
        "new_knowledge_ids": [
            "exercise_ch3_memoryless_survival_equation",
            "exercise_ch3_competing_exponentials",
            "exercise_ch3_poisson_thinning_for_infinite_server_queue",
            "exercise_ch3_poisson_splitting_occupancy",
            "exercise_ch3_dirichlet_uniform_spacings",
            "exercise_ch3_extreme_spacing_second_moment",
        ],
    },
    {
        "section": "3.8",
        "method_summary": "Read stable-law questions through scaling, regular variation, tail integrals, Laplace transforms, and conditioning on positive stable subordinators.",
        "method_tags": ["stable-laws", "heavy-tails", "regular-variation", "laplace-transform", "subordination"],
        "new_knowledge_ids": [
            "exercise_ch3_stable_no_centering_alpha_less_than_one",
            "exercise_ch3_borderline_normal_log_correction",
            "exercise_ch3_stable_fractional_moment_tail_test",
            "exercise_ch3_positive_stable_laplace_functional_equation",
            "exercise_ch3_stable_subordination_product_rule",
        ],
    },
    {
        "section": "3.9",
        "method_summary": "Use convolution roots, support diameter, symmetrized characteristic functions, and Levy-Khinchin exponent matching for infinite divisibility problems.",
        "method_tags": ["infinite-divisibility", "gamma", "levy-khinchin", "characteristic-functions", "support"],
        "new_knowledge_ids": [
            "exercise_ch3_gamma_shape_splitting",
            "exercise_ch3_bounded_infinitely_divisible_degenerate",
            "exercise_ch3_infinitely_divisible_cf_nonvanishing",
            "exercise_ch3_levy_measure_by_exponent_matching",
        ],
    },
    {
        "section": "3.10",
        "method_summary": "Recover marginals by sending coordinates to infinity, build joint laws with copulas, and prove independence or normality by multivariate characteristic functions.",
        "method_tags": ["multivariate", "marginals", "copula", "joint-characteristic-function", "multivariate-normal"],
        "new_knowledge_ids": [
            "exercise_ch3_marginals_from_joint_cdf",
            "exercise_ch3_fgm_copula_density_check",
            "exercise_ch3_mixed_partial_recovers_density",
            "exercise_ch3_joint_cf_independence_factorization",
            "exercise_ch3_multivariate_normal_diagonal_covariance",
            "exercise_ch3_cramer_wold_normal_identification",
        ],
    },
]

NEW_KNOWLEDGE = [
    {
        "id": "exercise_ch3_stirling_binomial_ratio_method",
        "title": "Stirling method for binomial ratios",
        "kind": "calculation-template",
        "summary": "Insert Stirling's formula into factorial probabilities, simplify the polynomial prefactor, and exponentiate logarithmic expansions.",
        "use_case": "Exercises in Section 3.1 involving De Moivre-Laplace or large binomial probabilities.",
        "tags": ["stirling", "binomial", "asymptotics"],
    },
    {
        "id": "exercise_ch3_product_to_exponential_method",
        "title": "Convert rare-event products to exponentials",
        "kind": "limit-template",
        "summary": "For products of factors 1+a_{n,k}, take logs and use log(1+x)=x+o(x) when the maximum factor is small.",
        "use_case": "Birthday, occupancy, no-collision, and geometric waiting-time limits.",
        "tags": ["product-limit", "rare-events", "log-expansion"],
    },
    {
        "id": "exercise_ch3_linear_deviation_not_clt",
        "title": "Linear deviations require exponential-rate estimates",
        "kind": "warning",
        "summary": "When deviations are of order n rather than sqrt(n), normal approximation is usually wrong; use Stirling or large-deviation rates.",
        "use_case": "Binomial or random-walk tail exercises before the large-deviation chapter.",
        "tags": ["large-deviation", "normal-approximation", "scale"],
    },
    {
        "id": "exercise_ch3_buffer_events_for_weak_convergence",
        "title": "Buffer events for weak convergence",
        "kind": "proof-template",
        "summary": "Compare events such as {X_n <= x} with {X <= x +/- epsilon} to pass from convergence in probability to weak convergence.",
        "use_case": "Exercises proving convergence in probability implies distributional convergence or converging-together results.",
        "tags": ["weak-convergence", "epsilon-buffer", "cdf"],
    },
    {
        "id": "exercise_ch3_subsequence_principle_for_limits",
        "title": "Subsequence principle for identifying limits",
        "kind": "proof-template",
        "summary": "Show every subsequence has a further subsequence with the same limit; then the original sequence converges.",
        "use_case": "Tightness and uniqueness arguments in weak convergence exercises.",
        "tags": ["subsequence", "tightness", "uniqueness"],
    },
    {
        "id": "exercise_ch3_tightness_by_tail_or_moment_bound",
        "title": "Tightness from tails or coercive moments",
        "kind": "criterion",
        "summary": "Control sup_n P(|X_n|>K) directly or use Markov's inequality on a function growing to infinity.",
        "use_case": "Weak convergence compactness exercises.",
        "tags": ["tightness", "markov", "moment-bound"],
    },
    {
        "id": "exercise_ch3_converging_together_slutsky_template",
        "title": "Converging together and Slutsky template",
        "kind": "proof-template",
        "summary": "If a main term has a distributional limit and the error goes to zero in probability, use tightness and buffer events to keep the same limit.",
        "use_case": "Exercises where a statistic is approximated by a simpler statistic.",
        "tags": ["slutsky", "negligible-error", "weak-convergence"],
    },
    {
        "id": "exercise_ch3_cf_table_matching",
        "title": "Characteristic-function table matching",
        "kind": "calculation-template",
        "summary": "Recognize transforms such as normal, Cauchy, gamma, Poisson, and uniform; then invoke uniqueness.",
        "use_case": "Distribution identification and transform inversion exercises in Section 3.3.",
        "tags": ["characteristic-functions", "transform-table", "uniqueness"],
    },
    {
        "id": "exercise_ch3_cf_taylor_moment_extraction",
        "title": "Extract moments from characteristic-function Taylor terms",
        "kind": "calculation-template",
        "summary": "Differentiate the characteristic function at zero or compare its Taylor expansion with 1+it EX - t^2 E X^2/2 + ... .",
        "use_case": "Moment and variance calculations from transforms.",
        "tags": ["moments", "taylor-expansion", "characteristic-functions"],
    },
    {
        "id": "exercise_ch3_cf_factorization_independence",
        "title": "Independence through characteristic-function factorization",
        "kind": "proof-template",
        "summary": "A joint characteristic function that factors into marginal characteristic functions identifies the product law.",
        "use_case": "Exercises proving independence from transforms.",
        "tags": ["independence", "joint-law", "characteristic-functions"],
    },
    {
        "id": "exercise_ch3_inversion_for_lattice_or_density",
        "title": "Use inversion to recover probabilities or densities",
        "kind": "calculation-template",
        "summary": "Apply the inversion formula in the form appropriate to densities or lattice probabilities, checking integrability when needed.",
        "use_case": "Characteristic-function inversion exercises.",
        "tags": ["inversion", "density", "lattice"],
    },
    {
        "id": "exercise_ch3_lindeberg_truncation_check",
        "title": "Lindeberg check by truncation",
        "kind": "proof-template",
        "summary": "Bound the contribution of terms exceeding epsilon times the row standard deviation; bounded or uniformly small terms often make the condition immediate.",
        "use_case": "Triangular-array CLT exercises.",
        "tags": ["lindeberg", "triangular-array", "truncation"],
    },
    {
        "id": "exercise_ch3_lyapunov_shortcut",
        "title": "Lyapunov condition as a shortcut to Lindeberg",
        "kind": "criterion",
        "summary": "Verify a higher-moment bound divided by the row variance scale; Lyapunov implies Lindeberg.",
        "use_case": "CLT exercises with available third or higher moments.",
        "tags": ["lyapunov", "clt", "moments"],
    },
    {
        "id": "exercise_ch3_random_index_clt_template",
        "title": "Random-index CLT template",
        "kind": "proof-template",
        "summary": "Condition on the random index or compare it to a deterministic equivalent, then use Slutsky once the index ratio converges.",
        "use_case": "Random sums and stopped-sum CLT exercises.",
        "tags": ["random-index", "clt", "slutsky"],
    },
    {
        "id": "exercise_ch3_poisson_or_multinomial_clt_scaling",
        "title": "Poisson and multinomial CLT scaling",
        "kind": "calculation-template",
        "summary": "Center counts by their means and scale by square roots of variances; dependence in multinomial vectors appears through covariance constraints.",
        "use_case": "Occupancy, count-vector, and Poisson approximation CLT exercises.",
        "tags": ["poisson", "multinomial", "normal-approximation"],
    },
    {
        "id": "exercise_ch3_local_limit_vs_global_clt",
        "title": "Local limit versus global CLT",
        "kind": "warning",
        "summary": "The CLT controls interval probabilities, while a local limit theorem controls individual lattice probabilities at the normal-density scale.",
        "use_case": "Point probability approximations in Section 3.5.",
        "tags": ["local-limit", "clt", "lattice"],
    },
    {
        "id": "exercise_ch3_lattice_span_check",
        "title": "Check lattice span before using a local limit theorem",
        "kind": "warning",
        "summary": "For lattice variables, the correct local approximation includes the span and only applies on reachable lattice points.",
        "use_case": "Local normal approximations for sums of integer-valued variables.",
        "tags": ["lattice", "span", "local-limit"],
    },
    {
        "id": "exercise_ch3_coupling_bounds_total_variation",
        "title": "Any coupling bounds total variation",
        "kind": "proof-template",
        "summary": "For every event A, |P(X in A)-P(Y in A)| is bounded by P(X != Y), so total variation is no larger than mismatch probability.",
        "use_case": "Exercise 3.6.1 and coupling estimates.",
        "tags": ["coupling", "total-variation", "mismatch"],
    },
    {
        "id": "exercise_ch3_maximal_coupling_common_mass",
        "title": "Maximal coupling by common mass",
        "kind": "construction-template",
        "summary": "Couple two discrete laws by first sampling from their overlap min(mu,nu), then sample residuals on disjoint supports.",
        "use_case": "Sharp total variation coupling results.",
        "tags": ["maximal-coupling", "common-mass", "discrete-law"],
    },
    {
        "id": "exercise_ch3_memoryless_survival_equation",
        "title": "Memoryless survival equation",
        "kind": "proof-template",
        "summary": "The lack-of-memory property gives G(s+t)=G(s)G(t); monotonicity and right-continuity force G(t)=exp(-lambda t).",
        "use_case": "Exercise 3.7.1 and exponential waiting-time characterization.",
        "tags": ["memoryless", "exponential", "survival-function"],
    },
    {
        "id": "exercise_ch3_competing_exponentials",
        "title": "Competing exponentials race rule",
        "kind": "calculation-template",
        "summary": "The minimum of independent exponentials has rate equal to the sum of rates, and the winning index has probability proportional to its rate.",
        "use_case": "Exercises 3.7.2 and 3.7.3.",
        "tags": ["exponential", "minimum", "race"],
    },
    {
        "id": "exercise_ch3_poisson_thinning_for_infinite_server_queue",
        "title": "Infinite-server queue by Poisson thinning",
        "kind": "calculation-template",
        "summary": "Calls of age r survive with probability 1-G(r); thinning and superposition give a Poisson number in service with mean lambda integral survival.",
        "use_case": "Exercise 3.7.4.",
        "tags": ["poisson-thinning", "queue", "tail-integral"],
    },
    {
        "id": "exercise_ch3_poisson_splitting_occupancy",
        "title": "Poisson splitting for occupancy",
        "kind": "calculation-template",
        "summary": "A Poisson number of independent categorized observations splits into independent Poisson counts in each category.",
        "use_case": "Exercise 3.7.5 and birthday/occupancy computations.",
        "tags": ["poisson-splitting", "occupancy", "independence"],
    },
    {
        "id": "exercise_ch3_dirichlet_uniform_spacings",
        "title": "Uniform spacings are Dirichlet",
        "kind": "distribution-fact",
        "summary": "The gaps between ordered uniform points, including endpoints, are exchangeable Dirichlet(1,...,1) spacings.",
        "use_case": "Exercises 3.7.7 through 3.7.9.",
        "tags": ["uniform-order-statistics", "spacings", "dirichlet"],
    },
    {
        "id": "exercise_ch3_extreme_spacing_second_moment",
        "title": "Extreme spacings by first and second moments",
        "kind": "proof-template",
        "summary": "Count gaps above a threshold, compute one- and two-gap probabilities from simplex volumes, and use variance control.",
        "use_case": "Largest and smallest uniform spacing limits.",
        "tags": ["extreme-spacing", "second-moment", "simplex-volume"],
    },
    {
        "id": "exercise_ch3_stable_no_centering_alpha_less_than_one",
        "title": "No centering for alpha less than one stable limits",
        "kind": "stable-law-fact",
        "summary": "For alpha<1, small jumps are summable in absolute value under the Levy measure, so the stable limit needs no compensating centering.",
        "use_case": "Exercises 3.8.1, 3.8.3, and 3.8.5.",
        "tags": ["stable-laws", "centering", "alpha-less-than-one"],
    },
    {
        "id": "exercise_ch3_borderline_normal_log_correction",
        "title": "Borderline normal attraction has sqrt(n log n) scale",
        "kind": "limit-template",
        "summary": "A symmetric variable with tail P(|Z|>x) like x^{-2} has infinite variance but still lies in the normal domain with a logarithmic variance correction.",
        "use_case": "Exercise 3.8.2 with p=1/2.",
        "tags": ["normal-attraction", "infinite-variance", "log-correction"],
    },
    {
        "id": "exercise_ch3_stable_fractional_moment_tail_test",
        "title": "Stable fractional moment and tail test",
        "kind": "calculation-template",
        "summary": "Use the integral representation of E|X|^p through 1-Re phi(t) to get finiteness for p<alpha and tail lower bounds to show E|X|^alpha diverges.",
        "use_case": "Exercise 3.8.4.",
        "tags": ["stable-laws", "fractional-moments", "tails"],
    },
    {
        "id": "exercise_ch3_positive_stable_laplace_functional_equation",
        "title": "Positive stable Laplace functional equation",
        "kind": "proof-template",
        "summary": "Stability gives psi(lambda)^n=psi(n^{1/alpha}lambda); continuity turns this into psi(lambda)=exp(-c lambda^alpha).",
        "use_case": "Exercise 3.8.6.",
        "tags": ["positive-stable", "laplace-transform", "functional-equation"],
    },
    {
        "id": "exercise_ch3_stable_subordination_product_rule",
        "title": "Stable subordination product rule",
        "kind": "calculation-template",
        "summary": "Condition on a positive beta-stable Y: E exp(it X Y^{1/alpha}) becomes the Laplace transform of Y at c|t|^alpha, giving index alpha beta.",
        "use_case": "Exercise 3.8.7 and normal-ratio Cauchy derivations.",
        "tags": ["subordination", "stable-laws", "cauchy"],
    },
    {
        "id": "exercise_ch3_gamma_shape_splitting",
        "title": "Gamma infinite divisibility by shape splitting",
        "kind": "calculation-template",
        "summary": "A Gamma(a,lambda) characteristic function is the nth power of the Gamma(a/n,lambda) characteristic function.",
        "use_case": "Exercise 3.9.1.",
        "tags": ["gamma", "infinite-divisibility", "convolution"],
    },
    {
        "id": "exercise_ch3_bounded_infinitely_divisible_degenerate",
        "title": "Bounded infinitely divisible laws are degenerate",
        "kind": "proof-template",
        "summary": "If a bounded law is an n-fold convolution, the summand support diameter is at most 1/n of the total diameter, forcing variance to zero.",
        "use_case": "Exercise 3.9.2.",
        "tags": ["infinite-divisibility", "bounded-support", "variance"],
    },
    {
        "id": "exercise_ch3_infinitely_divisible_cf_nonvanishing",
        "title": "Infinitely divisible characteristic functions do not vanish",
        "kind": "proof-template",
        "summary": "Symmetrize to |phi|^2, take nth convolution roots, and use continuity near zero to contradict a zero at a fixed point.",
        "use_case": "Exercise 3.9.3.",
        "tags": ["characteristic-functions", "infinite-divisibility", "nonvanishing"],
    },
    {
        "id": "exercise_ch3_levy_measure_by_exponent_matching",
        "title": "Find Levy measures by matching exponents",
        "kind": "calculation-template",
        "summary": "Compare the log characteristic function with the Levy-Khinchin integral; symmetry cancels imaginary compensation terms.",
        "use_case": "Exercise 3.9.4.",
        "tags": ["levy-measure", "levy-khinchin", "symmetric-law"],
    },
    {
        "id": "exercise_ch3_marginals_from_joint_cdf",
        "title": "Recover marginals from a joint CDF",
        "kind": "definition-use",
        "summary": "Send all non-target coordinates to infinity and use continuity from below to recover the target coordinate's distribution function.",
        "use_case": "Exercise 3.10.1.",
        "tags": ["marginals", "joint-cdf", "continuity-from-below"],
    },
    {
        "id": "exercise_ch3_fgm_copula_density_check",
        "title": "FGM-type copula density check",
        "kind": "construction-template",
        "summary": "For C(u)=prod u_i + alpha prod u_i(1-u_i), the mixed derivative is 1+alpha prod(1-2u_i), nonnegative for |alpha|<=1.",
        "use_case": "Exercise 3.10.2.",
        "tags": ["copula", "joint-distribution", "density-check"],
    },
    {
        "id": "exercise_ch3_mixed_partial_recovers_density",
        "title": "Mixed partial derivative recovers joint density",
        "kind": "calculation-template",
        "summary": "Write the CDF as an iterated integral of the density and apply the fundamental theorem of calculus successively.",
        "use_case": "Exercise 3.10.3.",
        "tags": ["joint-density", "cdf", "mixed-partial"],
    },
    {
        "id": "exercise_ch3_joint_cf_independence_factorization",
        "title": "Joint characteristic function factorization",
        "kind": "proof-template",
        "summary": "Independence gives product transforms; conversely, a product joint characteristic function matches the product law by uniqueness.",
        "use_case": "Exercise 3.10.6.",
        "tags": ["independence", "joint-characteristic-function", "uniqueness"],
    },
    {
        "id": "exercise_ch3_multivariate_normal_diagonal_covariance",
        "title": "Diagonal covariance gives independent normal coordinates",
        "kind": "normal-law-fact",
        "summary": "For a multivariate normal vector, a diagonal covariance matrix makes the characteristic function factor into one-dimensional normal transforms.",
        "use_case": "Exercise 3.10.7.",
        "tags": ["multivariate-normal", "covariance", "independence"],
    },
    {
        "id": "exercise_ch3_cramer_wold_normal_identification",
        "title": "Identify multivariate normal laws by all linear combinations",
        "kind": "proof-template",
        "summary": "If every t dot X is normal with the right mean and variance, then the joint characteristic function is the multivariate normal transform.",
        "use_case": "Exercise 3.10.8.",
        "tags": ["cramer-wold", "multivariate-normal", "characteristic-functions"],
    },
]

KNOWLEDGE_IDS_BY_SECTION = {
    "3.1": ["durrett_ch3_stirling_local_binomial", "durrett_ch3_demoivre_laplace", "durrett_ch3_product_exponential_limit"],
    "3.2": ["durrett_ch3_weak_convergence_definition", "durrett_ch3_continuous_mapping_theorem", "durrett_ch3_portmanteau_open_closed", "durrett_ch3_helly_selection_tightness"],
    "3.3": ["durrett_ch3_characteristic_function_definition", "durrett_ch3_levy_continuity_theorem", "durrett_ch3_moment_derivatives"],
    "3.4": ["durrett_ch3_iid_central_limit_theorem", "durrett_ch3_lindeberg_feller_clt", "durrett_ch3_lyapunov_condition"],
    "3.5": ["durrett_ch3_local_limit_theorem"],
    "3.6": ["durrett_ch3_total_variation_distance", "durrett_ch3_coupling_inequality"],
    "3.7": ["durrett_ch3_poisson_process", "durrett_ch3_exponential_waiting_times", "durrett_ch3_poisson_splitting"],
    "3.8": ["durrett_ch3_stable_laws", "durrett_ch3_regular_variation_stable_domain", "durrett_ch3_positive_stable_laplace_transform"],
    "3.9": ["durrett_ch3_infinite_divisibility", "durrett_ch3_levy_khinchin_formula"],
    "3.10": ["durrett_ch3_multivariate_distribution_functions", "durrett_ch3_joint_characteristic_functions", "durrett_ch3_multivariate_normal"],
}


def clean_tex(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def extract_exercises(tex: str) -> list[dict]:
    section_re = re.compile(r"\\section\*\{Section (3\.\d+): ([^}]*)\}")
    exercise_re = re.compile(r"\\(?:sub)?section\*\{Exercise (3\.\d+\.\d+)\}")

    positions = []
    for match in section_re.finditer(tex):
        positions.append((match.start(), "section", match))
    for match in exercise_re.finditer(tex):
        positions.append((match.start(), "exercise", match))
    positions.sort(key=lambda item: item[0])

    exercise_spans = []
    for idx, (pos, kind, match) in enumerate(positions):
        next_pos = positions[idx + 1][0] if idx + 1 < len(positions) else tex.find(r"\end{document}", pos)
        if kind == "section":
            continue
        else:
            exercise = match.group(1)
            section = ".".join(exercise.split(".")[:2])
            exercise_spans.append((exercise, section, pos, next_pos))

    records = []
    for exercise, section, start, end in exercise_spans:
        block = tex[start:end]
        q_marker = r"\textbf{Question.}"
        s_marker = r"\textbf{Solution.}"
        k_marker = r"\textbf{Knowledge used.}"
        if q_marker not in block or s_marker not in block:
            continue
        question_part = block.split(q_marker, 1)[1].split(s_marker, 1)[0]
        knowledge_macro_match = re.search(r"\\Knowledge\{(?P<body>.*?)\n\}", question_part, flags=re.S)
        if knowledge_macro_match:
            question = question_part[: knowledge_macro_match.start()]
            macro_body = knowledge_macro_match.group("body")
            macro_ids = re.findall(r"\\path\{([^}]*)\}", macro_body)
            knowledge_text = "; ".join(macro_ids)
        else:
            question = question_part
            macro_ids = []

        solution_part = block.split(s_marker, 1)[1]
        if k_marker in solution_part:
            solution = solution_part.split(k_marker, 1)[0]
            knowledge_text = solution_part.split(k_marker, 1)[1]
        else:
            solution = solution_part

        method_card = next(card for card in METHOD_CARDS if card["section"] == section)
        knowledge_ids = macro_ids or KNOWLEDGE_IDS_BY_SECTION.get(section, [])
        records.append(
            {
                "id": "durrett_ch3_exercise_" + exercise.replace(".", "_"),
                "exercise": exercise,
                "chapter": 3,
                "section": section,
                "section_topic": SECTION_TOPICS.get(section, ""),
                "source_tex": str(SOURCE_TEX),
                "source_pdf": str(SOURCE_PDF),
                "question_tex": clean_tex(question),
                "solution_tex": clean_tex(solution),
                "knowledge_used_text": clean_tex(knowledge_text),
                "knowledge_used_ids": knowledge_ids + method_card["new_knowledge_ids"],
                "method_summary": method_card["method_summary"],
                "method_tags": method_card["method_tags"],
                "new_knowledge_ids": method_card["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )
    return records


def method_cards() -> list[dict]:
    cards = []
    for card in METHOD_CARDS:
        section = card["section"]
        cards.append(
            {
                "id": f"durrett_ch3_section_{section.replace('.', '_')}_method_card",
                "chapter": 3,
                "section": section,
                "title": f"Chapter {section} exercise method card",
                "section_topic": SECTION_TOPICS[section],
                "method_summary": card["method_summary"],
                "method_tags": card["method_tags"],
                "new_knowledge_ids": card["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )
    return cards


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_flashcards(path: Path, cards: list[dict], knowledge: list[dict]) -> None:
    by_id = {item["id"]: item for item in knowledge}
    with path.open("w", encoding="utf-8") as handle:
        handle.write("front\tback\ttags\n")
        for card in cards:
            front = f"Chapter {card['section']} method: what is the main exercise strategy?"
            back = card["method_summary"]
            tags = ",".join(["chapter3", card["section"].replace(".", "_")] + card["method_tags"])
            handle.write(f"{front}\t{back}\t{tags}\n")
        for item in knowledge:
            front = item["title"]
            back = f"{item['summary']} Use case: {item['use_case']}"
            tags = ",".join(["chapter3", item["kind"]] + item["tags"])
            handle.write(f"{front}\t{back}\t{tags}\n")


def write_markdown(path: Path, records: list[dict], cards: list[dict], knowledge: list[dict]) -> None:
    counts_by_section: dict[str, int] = {}
    for record in records:
        counts_by_section[record["section"]] = counts_by_section.get(record["section"], 0) + 1

    lines = [
        "# Chapter 3 Exercise Viki Dataset",
        "",
        f"Source TeX: `{SOURCE_TEX}`",
        f"Source PDF: `{SOURCE_PDF}`",
        "",
        "This dataset turns the solved Chapter 3 exercises into retrieval-ready records, reusable method cards, and exercise-derived knowledge pieces.",
        "",
        "## Files",
        "",
        "- `chapter3_exercise_records.jsonl`: one record per solved exercise, including question, solution, knowledge used, and method tags.",
        "- `chapter3_exercise_method_cards.jsonl`: section-level method summaries.",
        "- `chapter3_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.",
        "- `chapter3_exercise_method_flashcards.tsv`: flashcard import file for method and new-knowledge cards.",
        "- `chapter3_exercise_viki.md`: human-readable overview.",
        "",
        "## Section Method Cards",
        "",
    ]
    for card in cards:
        count = counts_by_section.get(card["section"], 0)
        lines.extend(
            [
                f"### {card['section']} - {card['section_topic']}",
                "",
                f"Solved exercise records: {count}",
                "",
                card["method_summary"],
                "",
                "Tags: " + ", ".join(card["method_tags"]),
                "",
                "Reusable knowledge: " + ", ".join(card["new_knowledge_ids"]),
                "",
            ]
        )

    lines.extend(["## Exercise Records", ""])
    for record in records:
        lines.extend(
            [
                f"- `{record['exercise']}` ({record['section']}): {record['section_topic']}",
                f"  - Methods: {', '.join(record['method_tags'])}",
                f"  - Knowledge used: {record['knowledge_used_text']}",
            ]
        )

    lines.extend(["", "## New Exercise-Derived Knowledge", ""])
    for item in knowledge:
        lines.extend(
            [
                f"### {item['title']}",
                "",
                f"- ID: `{item['id']}`",
                f"- Kind: {item['kind']}",
                f"- Summary: {item['summary']}",
                f"- Use case: {item['use_case']}",
                f"- Tags: {', '.join(item['tags'])}",
                "",
            ]
        )

    path.write_text("\n".join(lines), encoding="utf-8")


def update_manifest(records: list[dict], cards: list[dict], knowledge: list[dict]) -> None:
    path = OUT / "manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    exercise_files = [
        "chapter3_exercise_records.jsonl",
        "chapter3_exercise_method_cards.jsonl",
        "chapter3_exercise_new_knowledge.jsonl",
        "chapter3_exercise_method_flashcards.tsv",
        "chapter3_exercise_viki.md",
    ]
    merged_files = list(dict.fromkeys(manifest.get("files", []) + exercise_files))
    manifest.update(
        {
            "exercise_source_tex": str(SOURCE_TEX),
            "exercise_source_pdf": str(SOURCE_PDF),
            "exercise_record_count": len(records),
            "exercise_method_card_count": len(cards),
            "exercise_new_knowledge_count": len(knowledge),
            "exercise_viki_created_at": CREATED,
            "files": merged_files,
        }
    )
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    tex = SOURCE_TEX.read_text(encoding="utf-8")
    records = extract_exercises(tex)
    cards = method_cards()
    knowledge = NEW_KNOWLEDGE

    write_jsonl(OUT / "chapter3_exercise_records.jsonl", records)
    write_jsonl(OUT / "chapter3_exercise_method_cards.jsonl", cards)
    write_jsonl(OUT / "chapter3_exercise_new_knowledge.jsonl", knowledge)
    write_flashcards(OUT / "chapter3_exercise_method_flashcards.tsv", cards, knowledge)
    write_markdown(OUT / "chapter3_exercise_viki.md", records, cards, knowledge)
    update_manifest(records, cards, knowledge)

    print(f"wrote {len(records)} exercise records")
    print(f"wrote {len(cards)} method cards")
    print(f"wrote {len(knowledge)} new knowledge pieces")


if __name__ == "__main__":
    main()

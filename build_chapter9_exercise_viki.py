from __future__ import annotations

import csv
import json
import re
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE_FILE = ROOT / "Probability/Textbook/Chapters/PTE-Chapter9.pdf"
SOURCE_TEX = ROOT / "Probability/Exercises/Chapter9/Chapter9Exercises.tex"
SOURCE_PDF = ROOT / "Probability/Exercises/Chapter9/Chapter9Exercises.pdf"
EXERCISE_DIR = ROOT / "Probability/LLM_Viki_Dataset/Chapter9_Exercise_Viki"
KNOWLEDGE_DIR = ROOT / "Probability/LLM_Viki_Dataset/Chapter9_Knowledge"
CREATED = datetime.now(timezone.utc).isoformat()


SECTION_METHODS = {
    "9.2": {
        "section_topic": "Heat equation, Brownian semigroup, and heat-kernel smoothing",
        "method_summary": "Run Brownian motion backward in time, use bounded martingales for uniqueness, and verify existence through Gaussian-kernel smoothing and the approximate identity at t=0.",
        "method_tags": ["heat-equation", "brownian-semigroup", "kernel-smoothing", "martingale-uniqueness"],
        "knowledge_used_ids": [
            "durrett_ch9_heat_backward_martingale",
            "durrett_ch9_heat_equation_solution",
            "durrett_ch9_heat_kernel_smoothing",
        ],
        "new_knowledge_ids": [
            "ch9_exercise_method_backward_heat_martingale_template",
            "ch9_exercise_method_bounded_heat_uniqueness",
            "ch9_exercise_method_gaussian_approximate_identity",
            "ch9_exercise_method_heat_kernel_derivative_majorants",
        ],
    },
    "9.3": {
        "section_topic": "Inhomogeneous heat equation and Duhamel occupation formulas",
        "method_summary": "Add the accumulated source term to the backward martingale, identify the unique bounded solution as a Brownian occupation integral, and use Holder regularity to control the singular small-time kernel.",
        "method_tags": ["duhamel", "source-term", "occupation-integral", "holder-regularity"],
        "knowledge_used_ids": [
            "durrett_ch9_duhamel_inhomogeneous_heat",
            "durrett_ch9_inhomogeneous_heat_regularity",
            "durrett_ch9_heat_kernel_smoothing",
        ],
        "new_knowledge_ids": [
            "ch9_exercise_method_source_term_martingale",
            "ch9_exercise_method_duhamel_uniqueness",
            "ch9_exercise_method_markov_property_pde_verification",
            "ch9_exercise_method_holder_cancels_kernel_singularity",
        ],
    },
    "9.4": {
        "section_topic": "Feynman-Kac formula for heat equations with potentials",
        "method_summary": "Multiply by the exponential potential weight, stop the weighted martingale, verify the PDE by a short-time expansion, and reduce smoothness to heat plus inhomogeneous heat regularity.",
        "method_tags": ["feynman-kac", "exponential-weight", "potential", "regularity-reduction"],
        "knowledge_used_ids": [
            "durrett_ch9_feynman_kac_forward",
            "durrett_ch9_feynman_kac_smoothness",
            "durrett_ch9_heat_equation_solution",
            "durrett_ch9_duhamel_inhomogeneous_heat",
        ],
        "new_knowledge_ids": [
            "ch9_exercise_method_exponential_weight_martingale",
            "ch9_exercise_method_feynman_kac_bounded_uniqueness",
            "ch9_exercise_method_smooth_feynman_kac_short_time_check",
            "ch9_exercise_method_feynman_kac_duhamel_reduction",
        ],
    },
    "9.5": {
        "section_topic": "Dirichlet problem, Liouville principles, and boundary regularity",
        "method_summary": "Represent harmonic functions by Brownian exit laws, use recurrence/transience to classify bounded or nonnegative harmonic objects, and isolate boundary irregularity through escape probabilities and cone conditions.",
        "method_tags": ["dirichlet-problem", "harmonic-functions", "regular-boundary", "escape-probability"],
        "knowledge_used_ids": [
            "durrett_ch9_dirichlet_problem_representation",
            "durrett_ch9_mean_value_harmonicity",
            "durrett_ch9_interior_smoothness_harmonic",
            "durrett_ch9_regular_boundary_point",
            "durrett_ch9_boundary_continuity_regular_points",
            "durrett_ch9_cone_condition",
        ],
        "new_knowledge_ids": [
            "ch9_exercise_method_heat_semigroup_liouville",
            "ch9_exercise_method_recurrent_superharmonic_constancy",
            "ch9_exercise_method_radial_superharmonic_high_dimension",
            "ch9_exercise_method_escape_probability_nonuniqueness",
            "ch9_exercise_method_flat_cone_regular_boundary",
        ],
    },
    "9.6": {
        "section_topic": "Green functions, occupation densities, and potential-kernel normalization",
        "method_summary": "Turn occupation times into integrals of transition densities, compute potential kernels by changes of variables or subtraction constants, and normalize constants through the distributional Laplacian.",
        "method_tags": ["green-function", "potential-kernel", "occupation-time", "distributional-laplacian"],
        "knowledge_used_ids": [
            "durrett_ch9_newtonian_potential_kernel",
            "durrett_ch9_green_function_killed_domain",
            "durrett_ch9_radial_harmonic_functions",
        ],
        "new_knowledge_ids": [
            "ch9_exercise_method_recurrent_ball_occupation_infinite",
            "ch9_exercise_method_transient_potential_kernel_gamma",
            "ch9_exercise_method_recurrent_modified_potential_kernel",
            "ch9_exercise_method_frullani_log_kernel",
            "ch9_exercise_method_distributional_delta_normalization",
        ],
    },
    "9.7": {
        "section_topic": "Poisson equation and exit-time moment recursions",
        "method_summary": "Identify exit-time moments by applying the Poisson representation recursively: the nth moment solves a Poisson equation with source n times the previous moment.",
        "method_tags": ["poisson-equation", "exit-time-moments", "moment-recursion"],
        "knowledge_used_ids": [
            "durrett_ch9_poisson_equation_representation",
            "durrett_ch9_expected_exit_time_poisson",
            "durrett_ch9_poisson_boundary_regular",
        ],
        "new_knowledge_ids": [
            "ch9_exercise_method_exit_time_moment_recursion",
            "ch9_exercise_method_second_moment_poisson_system",
        ],
    },
    "9.8": {
        "section_topic": "Schrodinger equation, gauge integrability, and exponential exit moments",
        "method_summary": "Use exponential weighting for elliptic equations with potential, check the gauge before applying Feynman-Kac, and detect blow-up through interval eigenvalue thresholds.",
        "method_tags": ["schrodinger-equation", "gauge", "exponential-exit-time", "eigenvalue-threshold"],
        "knowledge_used_ids": [
            "durrett_ch9_schrodinger_martingale",
            "durrett_ch9_schrodinger_nonuniqueness_warning",
            "durrett_ch9_gauge_function",
            "durrett_ch9_gauge_theorem_connected_domain",
            "durrett_ch9_schrodinger_dirichlet_representation",
            "durrett_ch9_schrodinger_boundary_regular",
            "durrett_ch9_interval_exponential_exit_moment",
        ],
        "new_knowledge_ids": [
            "ch9_exercise_method_schrodinger_weighted_martingale",
            "ch9_exercise_method_gauge_integrability_condition",
            "ch9_exercise_method_interval_eigenvalue_threshold",
            "ch9_exercise_method_finite_gauge_boundary_feynman_kac",
            "ch9_exercise_method_smooth_schrodinger_local_exit_expansion",
        ],
    },
}


NEW_KNOWLEDGE = [
    {
        "id": "ch9_exercise_method_backward_heat_martingale_template",
        "title": "Backward heat martingale template",
        "kind": "proof-template",
        "summary": "For u_t=(1/2)Delta u, apply Ito to u(t-s,B_s); the time derivative cancels the Brownian drift and leaves a local martingale.",
        "use_case": "Section 9.2 martingale checks and any backward parabolic uniqueness argument.",
        "tags": ["heat-equation", "ito-formula", "backward-time", "martingale"],
    },
    {
        "id": "ch9_exercise_method_bounded_heat_uniqueness",
        "title": "Bounded heat solution uniqueness by terminal martingale",
        "kind": "proof-template",
        "summary": "Boundedness upgrades the backward local martingale to a uniformly integrable martingale; sending s up to t identifies u(t,x) with E_x f(B_t).",
        "use_case": "Heat equation uniqueness and bounded parabolic Cauchy problems.",
        "tags": ["heat-equation", "uniqueness", "uniform-integrability"],
    },
    {
        "id": "ch9_exercise_method_gaussian_approximate_identity",
        "title": "Gaussian approximate identity at t=0",
        "kind": "calculation-template",
        "summary": "Write B_t as sqrt(t)Z; bounded convergence proves E f(x_n+sqrt(t_n)Z) tends to f(x) when f is bounded continuous.",
        "use_case": "Initial-condition verification for heat and Feynman-Kac formulas.",
        "tags": ["heat-kernel", "initial-condition", "bounded-convergence"],
    },
    {
        "id": "ch9_exercise_method_heat_kernel_derivative_majorants",
        "title": "Heat-kernel derivative majorants",
        "kind": "regularity-template",
        "summary": "On t bounded away from zero, derivatives of the Gaussian kernel are polynomial times a Gaussian, giving integrable majorants for differentiating under the integral.",
        "use_case": "Proving C^{1,2} smoothing for heat semigroups.",
        "tags": ["heat-kernel", "regularity", "dominated-convergence"],
    },
    {
        "id": "ch9_exercise_method_source_term_martingale",
        "title": "Source-term martingale for inhomogeneous heat equations",
        "kind": "proof-template",
        "summary": "For u_t=(1/2)Delta u+g, add integral_0^s g(B_r)dr to u(t-s,B_s) so the drift cancels.",
        "use_case": "Duhamel representation and source-term uniqueness.",
        "tags": ["duhamel", "source-term", "martingale"],
    },
    {
        "id": "ch9_exercise_method_duhamel_uniqueness",
        "title": "Duhamel uniqueness from bounded martingales",
        "kind": "proof-template",
        "summary": "A bounded inhomogeneous heat solution with zero initial data equals E_x integral_0^t g(B_s)ds by stopping the source-term martingale at s=t.",
        "use_case": "Identifying source-forced heat solutions and occupation integrals.",
        "tags": ["duhamel", "uniqueness", "occupation-integral"],
    },
    {
        "id": "ch9_exercise_method_markov_property_pde_verification",
        "title": "Short-time Markov-property PDE verification",
        "kind": "calculation-template",
        "summary": "Use v(t+h,x)=E_x[v(t,B_h)+short-time reward], Taylor expand v(t,B_h), divide by h, and let h down to zero.",
        "use_case": "Showing smooth Brownian representations solve heat, Poisson, and Feynman-Kac PDEs.",
        "tags": ["markov-property", "taylor-expansion", "pde-verification"],
    },
    {
        "id": "ch9_exercise_method_holder_cancels_kernel_singularity",
        "title": "Holder cancellation for singular heat-source kernels",
        "kind": "regularity-template",
        "summary": "Subtract g(x) inside P_s g(x)-g(x); Holder continuity gives O(s^{alpha/2}), offsetting the small-time singularity.",
        "use_case": "Regularity of inhomogeneous heat and potential-kernel formulas.",
        "tags": ["holder-continuity", "regularity", "singular-kernel"],
    },
    {
        "id": "ch9_exercise_method_exponential_weight_martingale",
        "title": "Exponential potential weight martingale",
        "kind": "proof-template",
        "summary": "Multiply by exp(integral c(B_s)ds); the finite-variation product rule adds exactly the c u drift needed for cancellation.",
        "use_case": "Feynman-Kac and Schrodinger martingale derivations.",
        "tags": ["feynman-kac", "exponential-weight", "martingale"],
    },
    {
        "id": "ch9_exercise_method_feynman_kac_bounded_uniqueness",
        "title": "Bounded Feynman-Kac uniqueness",
        "kind": "proof-template",
        "summary": "If c and u are bounded on finite time intervals, the weighted martingale is bounded; stopping at t gives u(t,x)=E_x[f(B_t)exp(integral_0^t c(B_s)ds)].",
        "use_case": "Parabolic PDEs with bounded multiplicative potentials.",
        "tags": ["feynman-kac", "boundedness", "uniqueness"],
    },
    {
        "id": "ch9_exercise_method_smooth_feynman_kac_short_time_check",
        "title": "Smooth Feynman-Kac short-time check",
        "kind": "calculation-template",
        "summary": "Use v(t+h,x)=E_x[e^{int_0^h c(B_s)ds}v(t,B_h)], then expand the Brownian move and the exponential to get v_t=(1/2)Delta v+c v.",
        "use_case": "Verifying smooth Feynman-Kac representations solve the PDE.",
        "tags": ["feynman-kac", "short-time", "pde-verification"],
    },
    {
        "id": "ch9_exercise_method_feynman_kac_duhamel_reduction",
        "title": "Feynman-Kac smoothness by Duhamel reduction",
        "kind": "regularity-template",
        "summary": "Use e^{A_t}-1=integral_0^t c(B_s)e^{A_t-A_s}ds to decompose v into a heat solution plus an inhomogeneous heat solution with source c v.",
        "use_case": "Regularity proofs for Feynman-Kac formulas with Holder f and c.",
        "tags": ["feynman-kac", "duhamel", "regularity"],
    },
    {
        "id": "ch9_exercise_method_heat_semigroup_liouville",
        "title": "Liouville theorem via heat semigroup flattening",
        "kind": "proof-template",
        "summary": "A bounded harmonic h satisfies h(x)=E h(x+B_t); as t grows, two Gaussian laws with fixed mean separation have vanishing total variation distance, so h(x)=h(y).",
        "use_case": "Bounded harmonic functions on all of R^d.",
        "tags": ["liouville", "harmonic-functions", "heat-semigroup"],
    },
    {
        "id": "ch9_exercise_method_recurrent_superharmonic_constancy",
        "title": "Recurrent Brownian motion forces nonnegative superharmonic functions constant",
        "kind": "proof-template",
        "summary": "Nonnegative superharmonic functions yield supermartingales; in d=1,2 Brownian motion hits every small neighborhood, so optional stopping gives f(x)>=f(y) and symmetry gives equality.",
        "use_case": "Superharmonic Liouville-type exercises in recurrent dimensions.",
        "tags": ["superharmonic", "recurrence", "optional-stopping"],
    },
    {
        "id": "ch9_exercise_method_radial_superharmonic_high_dimension",
        "title": "Radial superharmonic examples in high dimension",
        "kind": "example-pattern",
        "summary": "Use the radial Laplacian g''(r)+(d-1)g'(r)/r; functions such as (1+r^2)^{-(d-2)/2} are smooth nonconstant nonnegative superharmonic for d>=3.",
        "use_case": "Constructing counterexamples to recurrent-dimensional constancy in transient dimensions.",
        "tags": ["radial-laplacian", "superharmonic", "dimension"],
    },
    {
        "id": "ch9_exercise_method_escape_probability_nonuniqueness",
        "title": "Escape probability is the nonuniqueness direction",
        "kind": "proof-template",
        "summary": "When Brownian motion can avoid exiting G, q(x)=P_x(tau=infinity) is a bounded zero-boundary harmonic function; all bounded zero-boundary solutions differ by c q.",
        "use_case": "Dirichlet problems in domains where exit is not almost sure.",
        "tags": ["dirichlet-problem", "nonuniqueness", "escape-probability"],
    },
    {
        "id": "ch9_exercise_method_flat_cone_regular_boundary",
        "title": "Flat cone boundary regularity",
        "kind": "proof-template",
        "summary": "Use zeros of the perpendicular Brownian coordinate and the induced Cauchy trace on the hyperplane to show Brownian motion immediately hits a flat exterior cone.",
        "use_case": "Checking regular boundary points under weaker geometric exterior conditions.",
        "tags": ["regular-boundary", "cone-condition", "brownian-trace"],
    },
    {
        "id": "ch9_exercise_method_recurrent_ball_occupation_infinite",
        "title": "Infinite ball occupation in recurrent dimensions",
        "kind": "proof-template",
        "summary": "Use recurrence to get infinitely many returns to a ball and the strong Markov property to sum positive occupation increments.",
        "use_case": "Occupation-time dichotomy for Brownian motion in d<=2.",
        "tags": ["occupation-time", "recurrence", "strong-markov-property"],
    },
    {
        "id": "ch9_exercise_method_transient_potential_kernel_gamma",
        "title": "Gamma change of variables for transient potential kernels",
        "kind": "calculation-template",
        "summary": "For d>=3, integrate the heat kernel over time and use s=|x-y|^2/(2t) to get Gamma(d/2-1)/(2 pi^{d/2}) |x-y|^{2-d}.",
        "use_case": "Green-function and expected occupation-density calculations.",
        "tags": ["potential-kernel", "gamma-function", "transience"],
    },
    {
        "id": "ch9_exercise_method_recurrent_modified_potential_kernel",
        "title": "Modified potential kernels in recurrent dimensions",
        "kind": "calculation-template",
        "summary": "Subtract a reference heat kernel before integrating over time; in d=1 this gives -|x-y| and in d=2 gives -(1/pi)log|x-y|.",
        "use_case": "Using potential kernels when the full-space occupation integral diverges.",
        "tags": ["potential-kernel", "recurrent-dimensions", "renormalization"],
    },
    {
        "id": "ch9_exercise_method_frullani_log_kernel",
        "title": "Frullani integral for the two-dimensional log kernel",
        "kind": "calculation-template",
        "summary": "After u=1/(2t), the difference of two planar heat kernels becomes integral_0^infty (e^{-a^2u}-e^{-u})du/u=-2log a.",
        "use_case": "Deriving the d=2 logarithmic potential kernel.",
        "tags": ["frullani", "log-kernel", "dimension-two"],
    },
    {
        "id": "ch9_exercise_method_distributional_delta_normalization",
        "title": "Distributional delta normalization of Green kernels",
        "kind": "proof-template",
        "summary": "Integrate by parts outside a small ball and let the radius shrink; the boundary flux fixes the constant so (1/2)Delta G=-delta_0.",
        "use_case": "Checking Green-function constants and fundamental solutions.",
        "tags": ["distributional-laplacian", "green-function", "flux"],
    },
    {
        "id": "ch9_exercise_method_exit_time_moment_recursion",
        "title": "Exit-time moment recursion",
        "kind": "proof-template",
        "summary": "For m_n(x)=E_x tau^n, the Markov property or Dynkin formula gives (1/2)Delta m_n=-n m_{n-1} with zero boundary values.",
        "use_case": "Computing higher moments of Brownian exit times.",
        "tags": ["exit-time", "moment-recursion", "poisson-equation"],
    },
    {
        "id": "ch9_exercise_method_second_moment_poisson_system",
        "title": "Second exit-time moment Poisson system",
        "kind": "calculation-template",
        "summary": "First solve (1/2)Delta v=-1 for v=E tau; then solve (1/2)Delta w=-2v for w=E tau^2, both with zero boundary values.",
        "use_case": "Exercise 9.7.1 and second-moment exit-time computations.",
        "tags": ["exit-time", "second-moment", "poisson-equation"],
    },
    {
        "id": "ch9_exercise_method_schrodinger_weighted_martingale",
        "title": "Schrodinger weighted martingale",
        "kind": "proof-template",
        "summary": "For (1/2)Delta u+c u=0, Ito plus the finite-variation product rule makes u(B_t)exp(integral_0^t c(B_s)ds) a local martingale before exit.",
        "use_case": "Boundary Feynman-Kac formulas for elliptic equations with potential.",
        "tags": ["schrodinger-equation", "feynman-kac", "martingale"],
    },
    {
        "id": "ch9_exercise_method_gauge_integrability_condition",
        "title": "Gauge integrability condition",
        "kind": "criterion",
        "summary": "Before applying boundary Feynman-Kac with positive potential, check w(x)=E_x exp(integral_0^tau c(B_s)ds); bounded c alone does not ensure finiteness.",
        "use_case": "Avoiding false Schrodinger Feynman-Kac representations.",
        "tags": ["gauge", "integrability", "positive-potential"],
    },
    {
        "id": "ch9_exercise_method_interval_eigenvalue_threshold",
        "title": "Interval eigenvalue threshold for exponential exit times",
        "kind": "calculation-template",
        "summary": "For tau exiting (-a,a), solve (1/2)u''+gamma u=0 with boundary value one; finiteness holds exactly below gamma=pi^2/(8a^2).",
        "use_case": "Explicit exponential exit-time moments and gauge blow-up examples.",
        "tags": ["exit-time", "eigenvalue", "interval"],
    },
    {
        "id": "ch9_exercise_method_finite_gauge_boundary_feynman_kac",
        "title": "Finite-gauge boundary Feynman-Kac uniqueness",
        "kind": "proof-template",
        "summary": "Finite bounded gauge controls the terminal exponential weight and kills the tail term, giving u(x)=E_x[f(B_tau)exp(integral_0^tau c(B_s)ds)].",
        "use_case": "Uniqueness of bounded Schrodinger Dirichlet solutions.",
        "tags": ["finite-gauge", "dirichlet-problem", "feynman-kac"],
    },
    {
        "id": "ch9_exercise_method_smooth_schrodinger_local_exit_expansion",
        "title": "Local exit expansion for smooth Schrodinger representations",
        "kind": "calculation-template",
        "summary": "Stop at a small ball, expand v(B_sigma) and exp(integral_0^sigma c(B_s)ds), then divide by E sigma to get (1/2)Delta v+c v=0.",
        "use_case": "Verifying smooth Schrodinger Feynman-Kac formulas solve the PDE.",
        "tags": ["schrodinger-equation", "local-exit", "taylor-expansion"],
    },
]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def clean_tex(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def extract_exercises(tex: str) -> list[dict]:
    pattern = re.compile(
        r"\\section\*\{Section (?P<section>9\.\d+) Exercises\}|"
        r"\\subsection\*\{Exercise (?P<exercise>9\.\d+(?:\.[0-9]+|\.[A-Z]))(?:: (?P<title>[^}]+))?\}",
    )
    matches = list(pattern.finditer(tex))
    records = []
    current_section = None
    for idx, match in enumerate(matches):
        if match.group("section"):
            current_section = match.group("section")
            continue
        exercise = match.group("exercise")
        title = match.group("title") or f"Exercise {exercise}"
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else tex.find(r"\end{document}", start)
        body = tex[start:end]
        q_match = re.search(
            r"\\noindent\\textbf\{(?:Problem|Question)\.\}\s*(?P<question>.*?)"
            r"\\noindent\\textbf\{Solution\.\}\s*(?P<solution>.*)",
            body,
            flags=re.S,
        )
        if not q_match:
            continue
        section = current_section or ".".join(exercise.split(".")[:2])
        records.append(
            {
                "exercise": exercise,
                "title": clean_tex(title),
                "section": section,
                "question_tex": clean_tex(q_match.group("question")),
                "solution_tex": clean_tex(q_match.group("solution")),
            }
        )
    return records


def exercise_id(exercise: str) -> str:
    return "durrett_ch9_exercise_" + exercise.replace(".", "_")


def make_exercise_records() -> list[dict]:
    tex = SOURCE_TEX.read_text(encoding="utf-8")
    extracted = extract_exercises(tex)
    records = []
    for item in extracted:
        section = item["section"]
        method = SECTION_METHODS[section]
        records.append(
            {
                "id": exercise_id(item["exercise"]),
                "exercise": item["exercise"],
                "chapter": 9,
                "section": section,
                "section_topic": method["section_topic"],
                "title": item["title"],
                "source_tex": str(SOURCE_TEX),
                "source_pdf": str(SOURCE_PDF),
                "question_tex": item["question_tex"],
                "solution_tex": item["solution_tex"],
                "knowledge_used_ids": method["knowledge_used_ids"],
                "method_summary": method["method_summary"],
                "method_tags": method["method_tags"],
                "new_knowledge_ids": method["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )
    return records


def make_method_cards() -> list[dict]:
    cards = []
    for section, method in SECTION_METHODS.items():
        cards.append(
            {
                "id": f"durrett_ch9_section_{section.replace('.', '_')}_method_card",
                "chapter": 9,
                "section": section,
                "title": f"Chapter {section} exercise method card",
                "section_topic": method["section_topic"],
                "method_summary": method["method_summary"],
                "method_tags": method["method_tags"],
                "knowledge_used_ids": method["knowledge_used_ids"],
                "new_knowledge_ids": method["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )
    return cards


def write_flashcards(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["id", "front", "back", "tags"])
        for row in rows:
            writer.writerow(
                [
                    row["id"],
                    f"{row['title']} ({row['kind']})",
                    f"{row['summary']} Use case: {row.get('use_case', '')}",
                    ",".join(row.get("tags", [])),
                ]
            )


def make_exercise_markdown(
    path: Path,
    exercise_records: list[dict],
    method_cards: list[dict],
    new_knowledge: list[dict],
) -> None:
    lines = [
        "# Durrett Chapter 9 Exercise LLM Viki",
        "",
        "Source: `Probability/Exercises/Chapter9/Chapter9Exercises.tex` and compiled PDF.",
        "",
        "These records are derived from the solved Chapter 9 exercises and verification tasks, with reusable method patterns for LLM retrieval.",
        "",
        "## Method Cards",
        "",
    ]
    for card in method_cards:
        lines.extend(
            [
                f"### {card['section']} {card['section_topic']}",
                "",
                f"- ID: `{card['id']}`",
                "",
                f"- Method: {card['method_summary']}",
                "",
                f"- Tags: {', '.join(card['method_tags'])}",
                "",
                f"- Knowledge used: {', '.join(card['knowledge_used_ids'])}",
                "",
                f"- Exercise-derived knowledge: {', '.join(card['new_knowledge_ids'])}",
                "",
            ]
        )

    lines.extend(["## New Knowledge", ""])
    for item in new_knowledge:
        lines.extend(
            [
                f"### {item['title']}",
                "",
                f"- ID: `{item['id']}`",
                "",
                f"- Kind: {item['kind']}",
                "",
                f"- Summary: {item['summary']}",
                "",
                f"- Use case: {item['use_case']}",
                "",
                f"- Tags: {', '.join(item['tags'])}",
                "",
            ]
        )

    by_section: dict[str, list[dict]] = defaultdict(list)
    for record in exercise_records:
        by_section[record["section"]].append(record)

    lines.extend(["## Exercise Records", ""])
    for section in sorted(by_section):
        topic = by_section[section][0]["section_topic"]
        lines.extend([f"### {section} {topic}", ""])
        for record in by_section[section]:
            lines.extend(
                [
                    f"#### {record['exercise']} {record['title']}",
                    "",
                    f"- ID: `{record['id']}`",
                    "",
                    f"- Method tags: {', '.join(record['method_tags'])}",
                    "",
                    f"- Knowledge used: {', '.join(record['knowledge_used_ids'])}",
                    "",
                    f"- New knowledge: {', '.join(record['new_knowledge_ids'])}",
                    "",
                ]
            )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_exercise_viki() -> tuple[list[dict], list[dict], list[dict]]:
    EXERCISE_DIR.mkdir(parents=True, exist_ok=True)
    exercise_records = make_exercise_records()
    method_cards = make_method_cards()
    new_knowledge = [dict(item, created_at=CREATED) for item in NEW_KNOWLEDGE]

    write_jsonl(EXERCISE_DIR / "chapter9_exercise_records.jsonl", exercise_records)
    write_jsonl(EXERCISE_DIR / "chapter9_exercise_method_cards.jsonl", method_cards)
    write_jsonl(EXERCISE_DIR / "chapter9_exercise_new_knowledge.jsonl", new_knowledge)
    write_flashcards(EXERCISE_DIR / "chapter9_exercise_method_flashcards.tsv", new_knowledge)
    make_exercise_markdown(
        EXERCISE_DIR / "chapter9_exercise_viki.md",
        exercise_records,
        method_cards,
        new_knowledge,
    )

    manifest = {
        "name": "durrett_chapter9_exercise_viki",
        "description": "LLM/Viki exercise dataset built from solved Durrett Chapter 9 exercises and verification tasks, including questions, solutions, methods, and reusable knowledge pieces.",
        "created_at": CREATED,
        "source_tex": str(SOURCE_TEX),
        "source_pdf": str(SOURCE_PDF),
        "exercise_record_count": len(exercise_records),
        "method_card_count": len(method_cards),
        "new_knowledge_count": len(new_knowledge),
        "files": [
            "chapter9_exercise_records.jsonl",
            "chapter9_exercise_method_cards.jsonl",
            "chapter9_exercise_new_knowledge.jsonl",
            "chapter9_exercise_method_flashcards.tsv",
            "chapter9_exercise_viki.md",
            "manifest.json",
        ],
    }
    (EXERCISE_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return exercise_records, method_cards, new_knowledge


def normalize_kind(kind: str) -> str:
    if kind in {"proof-template", "calculation-template", "regularity-template"}:
        return "exercise-pattern"
    if kind == "example-pattern":
        return "example-pattern"
    if kind == "criterion":
        return "criterion"
    return kind


def back_text(piece: dict) -> str:
    parts = [piece.get("summary", "")]
    if piece.get("exam_use"):
        parts.append(f"Exam use: {piece['exam_use']}")
    if piece.get("pitfalls"):
        parts.append(f"Pitfall: {piece['pitfalls']}")
    return " ".join(part for part in parts if part)


def write_knowledge_flashcards(path: Path, pieces: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["id", "front", "back", "tags"])
        for piece in pieces:
            writer.writerow(
                [
                    piece["id"],
                    f"{piece['title']} ({piece['section']})",
                    back_text(piece),
                    ",".join(piece.get("tags", [])),
                ]
            )


def make_unified_markdown(
    path: Path,
    section_guides: list[dict],
    pieces: list[dict],
    method_cards: list[dict],
    exercise_records: list[dict],
) -> None:
    lines = [
        "# Durrett Chapter 9 LLM Viki: Multidimensional Brownian Motion",
        "",
        "Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter9.pdf`.",
        "",
        "This unified Chapter 9 knowledge base includes textbook knowledge pieces plus exercise-derived method patterns from the solved Chapter 9 exercises.",
        "",
        "Exercise source: `Probability/Exercises/Chapter9/Chapter9Exercises.tex` and `Probability/Exercises/Chapter9/Chapter9Exercises.pdf`.",
        "",
        "These are curated study/LLM retrieval pieces, not verbatim textbook notes.",
        "",
        "## Section Guides",
        "",
    ]
    for guide in section_guides:
        lines.extend(
            [
                f"### {guide['section']}",
                "",
                f"- Goal: {guide.get('study_goal', guide.get('goal', ''))}",
                "",
                f"- Must master: {', '.join(guide.get('must_master', []))}",
                "",
                f"- Prelim angle: {guide.get('prelim_angle', '')}",
                "",
            ]
        )

    lines.extend(["## Knowledge Pieces", ""])
    for piece in pieces:
        lines.extend(
            [
                f"### {piece['title']}",
                "",
                f"- ID: `{piece['id']}`",
                "",
                f"- Section: {piece['section']}",
                "",
                f"- Kind: {piece['kind']}",
                "",
                f"- Summary: {piece['summary']}",
                "",
                f"- Proof idea: {piece.get('proof_idea', '')}",
                "",
                f"- Exam use: {piece.get('exam_use', '')}",
                "",
                f"- Pitfall: {piece.get('pitfalls', '')}",
                "",
                f"- Tags: {', '.join(piece.get('tags', []))}",
                "",
            ]
        )
        if piece.get("source_exercises"):
            lines.extend([f"- Source exercises: {', '.join(piece['source_exercises'])}", ""])

    lines.extend(["## Exercise Method Cards", ""])
    for card in method_cards:
        lines.extend(
            [
                f"### {card['section']} {card['section_topic']}",
                "",
                f"- ID: `{card['id']}`",
                "",
                f"- Method: {card['method_summary']}",
                "",
                f"- Tags: {', '.join(card['method_tags'])}",
                "",
                f"- New knowledge IDs: {', '.join(card['new_knowledge_ids'])}",
                "",
            ]
        )

    by_section: dict[str, list[dict]] = defaultdict(list)
    for record in exercise_records:
        by_section[record["section"]].append(record)
    lines.extend(["## Exercise Record Index", ""])
    for section in sorted(by_section):
        topic = by_section[section][0]["section_topic"]
        lines.extend([f"### {section} {topic}", ""])
        for record in by_section[section]:
            lines.append(
                f"- Exercise {record['exercise']}: method tags `"
                + ", ".join(record.get("method_tags", []))
                + "`; knowledge used `"
                + ", ".join(record.get("knowledge_used_ids", []))
                + "`; new knowledge `"
                + ", ".join(record.get("new_knowledge_ids", []))
                + "`."
            )
        lines.append("")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def copy_exercise_artifacts() -> None:
    for name in [
        "chapter9_exercise_records.jsonl",
        "chapter9_exercise_method_cards.jsonl",
        "chapter9_exercise_new_knowledge.jsonl",
        "chapter9_exercise_method_flashcards.tsv",
        "chapter9_exercise_viki.md",
    ]:
        shutil.copy2(EXERCISE_DIR / name, KNOWLEDGE_DIR / name)


def merge_into_chapter_knowledge(
    exercise_records: list[dict],
    method_cards: list[dict],
    new_knowledge: list[dict],
) -> None:
    KNOWLEDGE_DIR.mkdir(parents=True, exist_ok=True)
    current_pieces = read_jsonl(KNOWLEDGE_DIR / "chapter9_knowledge_pieces.jsonl")
    textbook_pieces = [
        piece for piece in current_pieces if not piece["id"].startswith("ch9_exercise_method_")
    ]
    write_jsonl(KNOWLEDGE_DIR / "chapter9_textbook_knowledge_pieces.jsonl", textbook_pieces)
    section_guides = read_jsonl(KNOWLEDGE_DIR / "chapter9_section_guides.jsonl")
    copy_exercise_artifacts()

    id_to_card: dict[str, dict] = {}
    for card in method_cards:
        for knowledge_id in card.get("new_knowledge_ids", []):
            id_to_card[knowledge_id] = card

    id_to_exercises: dict[str, set[str]] = defaultdict(set)
    id_to_related: dict[str, set[str]] = defaultdict(set)
    for record in exercise_records:
        for knowledge_id in record.get("new_knowledge_ids", []):
            id_to_exercises[knowledge_id].add(record["exercise"])
            id_to_related[knowledge_id].update(record.get("knowledge_used_ids", []))

    exercise_pieces = []
    for item in new_knowledge:
        card = id_to_card[item["id"]]
        exercise_pieces.append(
            {
                "id": item["id"],
                "source": "Solved Durrett Chapter 9 exercises and exercise viki records",
                "source_file": str(SOURCE_TEX),
                "source_pdf": str(SOURCE_PDF),
                "chapter": 9,
                "section": f"{card['section']} Exercises: {card['section_topic']}",
                "title": item["title"],
                "kind": normalize_kind(item.get("kind", "exercise-pattern")),
                "summary": item["summary"],
                "proof_idea": card["method_summary"],
                "exam_use": item.get("use_case", ""),
                "pitfalls": "Check boundedness, regularity, exit-time finiteness, boundary regularity, and gauge hypotheses before reusing Chapter 9 Brownian/PDE patterns.",
                "tags": item.get("tags", []),
                "related_ids": sorted(id_to_related[item["id"]]),
                "source_exercises": sorted(id_to_exercises[item["id"]]),
                "created_at": item.get("created_at", CREATED),
                "merged_at": CREATED,
            }
        )

    combined_pieces = textbook_pieces + exercise_pieces
    write_jsonl(KNOWLEDGE_DIR / "chapter9_knowledge_pieces.jsonl", combined_pieces)
    write_knowledge_flashcards(KNOWLEDGE_DIR / "chapter9_flashcards.tsv", combined_pieces)
    make_unified_markdown(
        KNOWLEDGE_DIR / "chapter9_viki.md",
        section_guides,
        combined_pieces,
        method_cards,
        exercise_records,
    )

    manifest = {
        "name": "durrett_chapter9_multidimensional_brownian_motion_llm_viki",
        "description": "Unified LLM/Viki-style knowledge base for Chapter 9 of Durrett Probability: Theory and Examples, including textbook knowledge pieces and exercise-derived Brownian/PDE method patterns.",
        "source_file": str(SOURCE_FILE),
        "source_tex": str(SOURCE_TEX),
        "source_pdf": str(SOURCE_PDF),
        "created_at": CREATED,
        "piece_count": len(combined_pieces),
        "textbook_piece_count": len(textbook_pieces),
        "exercise_derived_piece_count": len(exercise_pieces),
        "section_count": len(section_guides),
        "exercise_record_count": len(exercise_records),
        "method_card_count": len(method_cards),
        "files": [
            "chapter9_knowledge_pieces.jsonl",
            "chapter9_textbook_knowledge_pieces.jsonl",
            "chapter9_section_guides.jsonl",
            "chapter9_viki.md",
            "chapter9_flashcards.tsv",
            "chapter9_exercise_records.jsonl",
            "chapter9_exercise_method_cards.jsonl",
            "chapter9_exercise_new_knowledge.jsonl",
            "chapter9_exercise_method_flashcards.tsv",
            "chapter9_exercise_viki.md",
            "manifest.json",
        ],
    }
    (KNOWLEDGE_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    exercise_records, method_cards, new_knowledge = build_exercise_viki()
    merge_into_chapter_knowledge(exercise_records, method_cards, new_knowledge)
    print(
        json.dumps(
            {
                "exercise_records": len(exercise_records),
                "method_cards": len(method_cards),
                "new_knowledge": len(new_knowledge),
                "chapter9_total_pieces": len(read_jsonl(KNOWLEDGE_DIR / "chapter9_knowledge_pieces.jsonl")),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEX = ROOT / "Probability/Exercises/Chapter7/Chapter7Exercises.tex"
PDF = ROOT / "Probability/Exercises/Chapter7/Chapter7Exercises.pdf"
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter7_Exercise_Viki"
CREATED = datetime.now(timezone.utc).isoformat()


SECTION_METHODS = {
    "7.1": {
        "section_topic": "Brownian construction, Gaussian calculations, path roughness, and quadratic variation",
        "method_summary": "Reduce finite-dimensional Brownian questions to independent Gaussian increments; use rotational normal geometry, Gaussian linear functionals, small-increment estimates, and Borel-Cantelli for path regularity.",
        "method_tags": ["brownian-definition", "gaussian-increments", "holder", "quadratic-variation"],
        "new_knowledge_ids": [
            "exercise_method_ch7_gaussian_wedge_probability",
            "exercise_method_ch7_increment_expansion_moments",
            "exercise_method_ch7_brownian_integral_gaussian",
            "exercise_method_ch7_countable_coordinate_sigma_field",
            "exercise_method_ch7_k_increment_holder_obstruction",
            "exercise_method_ch7_dyadic_quadratic_variation_borel_cantelli",
        ],
    },
    "7.2": {
        "section_topic": "Markov property, Blumenthal 0-1 law, immediate behavior, and recurrence patterns",
        "method_summary": "Condition on Brownian position at a deterministic time, translate future hitting events into fresh Brownian probabilities, and use germ 0-1 laws to upgrade positive-probability local behavior to almost sure behavior.",
        "method_tags": ["markov-property", "blumenthal", "germ-field", "recurrence"],
        "new_knowledge_ids": [
            "exercise_method_ch7_markov_conditioning_hitting_survival",
            "exercise_method_ch7_last_zero_markov_decomposition",
            "exercise_method_ch7_dense_local_maxima_from_immediate_crossing",
            "exercise_method_ch7_germ_limsup_constant",
            "exercise_method_ch7_sqrt_time_not_holder_half",
        ],
    },
    "7.3": {
        "section_topic": "Stopping-time closure and stopped sigma-fields",
        "method_summary": "Prove stopping-time claims by rewriting events with countable unions over rational times, use open/closed hitting-time facts, and apply the definition of F_S through restrictions to {S <= t}.",
        "method_tags": ["stopping-times", "stopped-sigma-field", "rational-time", "closure-properties"],
        "new_knowledge_ids": [
            "exercise_method_ch7_fsigma_hitting_time",
            "exercise_method_ch7_sum_stopping_time_rational_split",
            "exercise_method_ch7_sup_inf_stopping_times",
            "exercise_method_ch7_stopped_event_restriction",
            "exercise_method_ch7_compare_stopping_times_in_stopped_fields",
            "exercise_method_ch7_meet_stopped_sigma_field",
        ],
    },
    "7.4": {
        "section_topic": "Brownian path properties, reflection, hitting-time densities, and arcsine-type laws",
        "method_summary": "Combine strong Markov, reflection, hitting-time densities, and conditioning at fixed times to compute distributions of returns, maxima, endpoints, and zero-set events.",
        "method_tags": ["reflection-principle", "hitting-times", "cauchy", "zero-set", "arcsine"],
        "new_knowledge_ids": [
            "exercise_method_ch7_planar_hitting_cauchy",
            "exercise_method_ch7_return_time_density_mixture",
            "exercise_method_ch7_reflected_endpoint_subdensity",
            "exercise_method_ch7_joint_max_endpoint_density",
            "exercise_method_ch7_zero_interval_arccos_integral",
        ],
    },
    "7.5": {
        "section_topic": "Brownian martingales, optional stopping, exit transforms, and moment computations",
        "method_summary": "Choose martingales tailored to the target: cosh/exponential martingales for Laplace transforms, heat-polynomial martingales for exit moments, and maximal inequalities for almost-sure growth bounds.",
        "method_tags": ["martingales", "optional-stopping", "laplace-transform", "exit-times", "polynomial-martingales"],
        "new_knowledge_ids": [
            "exercise_method_ch7_cosh_martingale_exit_laplace",
            "exercise_method_ch7_drift_hitting_exponential_martingale",
            "exercise_method_ch7_interval_exit_laplace_linear_system",
            "exercise_method_ch7_cauchy_schwarz_exit_moment_comparison",
            "exercise_method_ch7_sixth_degree_exit_moment",
            "exercise_method_ch7_exponential_square_maximal_borel_cantelli",
        ],
    },
    "7.6": {
        "section_topic": "Ito formula, stochastic integral martingales, and Brownian moment/radial identities",
        "method_summary": "Apply one-dimensional, time-space, and multidimensional Ito formulas; identify drift terms, turn zero drift into martingales, and take expectations to get moment recursions.",
        "method_tags": ["ito-formula", "stochastic-integral", "moments", "radial-process", "bessel"],
        "new_knowledge_ids": [
            "exercise_method_ch7_ito_affine_martingale_characterization",
            "exercise_method_ch7_cubic_ito_martingales",
            "exercise_method_ch7_even_moment_ito_recursion",
            "exercise_method_ch7_radial_ito_bessel_form",
            "exercise_method_ch7_squared_norm_ito_dimension_drift",
        ],
    },
}


NEW_KNOWLEDGE = [
    {
        "id": "exercise_method_ch7_gaussian_wedge_probability",
        "title": "Two-time Brownian sign probability by Gaussian wedge angle",
        "kind": "calculation-template",
        "summary": "Write B_t as B_s plus an independent increment, standardize to a rotationally symmetric bivariate normal, and compute the sector angle cut out by the two half-planes.",
        "use_case": "Exercise 7.1.1; probabilities involving signs of correlated Brownian values.",
        "tags": ["brownian", "gaussian-geometry", "sign-probability"],
    },
    {
        "id": "exercise_method_ch7_increment_expansion_moments",
        "title": "Brownian polynomial moments by independent increment expansion",
        "kind": "calculation-template",
        "summary": "Represent B_1, B_2, B_3 through independent unit Gaussian increments, expand the polynomial, and discard terms with centered odd factors.",
        "use_case": "Exercise 7.1.2; low-order Brownian moment computations.",
        "tags": ["brownian-moments", "independent-increments", "gaussian"],
    },
    {
        "id": "exercise_method_ch7_brownian_integral_gaussian",
        "title": "Deterministic Brownian integrals are Gaussian",
        "kind": "calculation-template",
        "summary": "Approximate an integral of B_s against deterministic ds by Riemann sums; each sum is Gaussian, and the variance is the double integral of r wedge s.",
        "use_case": "Exercise 7.1.3; integrated Brownian motion and Gaussian linear functionals.",
        "tags": ["gaussian-process", "brownian-integral", "covariance"],
    },
    {
        "id": "exercise_method_ch7_countable_coordinate_sigma_field",
        "title": "Events in raw path sigma-field depend on countably many coordinates",
        "kind": "proof-template",
        "summary": "Show the class of events depending on a countable coordinate list is a sigma-field containing all finite-dimensional cylinders.",
        "use_case": "Exercise 7.1.4; path-space measurability and cylinder sigma-fields.",
        "tags": ["path-space", "sigma-field", "coordinates"],
    },
    {
        "id": "exercise_method_ch7_k_increment_holder_obstruction",
        "title": "K-increment obstruction to Brownian Holder regularity",
        "kind": "proof-template",
        "summary": "If a Holder point exists, a nearby block of k Gaussian increments must all be unusually small; union bound gives probability O(n^{1+k(1/2-gamma)}).",
        "use_case": "Exercise 7.1.5; proving no Holder points above exponent 1/2.",
        "tags": ["holder", "small-increments", "brownian-roughness"],
    },
    {
        "id": "exercise_method_ch7_dyadic_quadratic_variation_borel_cantelli",
        "title": "Dyadic quadratic variation by L2 plus Borel-Cantelli",
        "kind": "proof-template",
        "summary": "Compute variance of the dyadic squared-increment sum as 2t^2 2^{-n}, apply Chebyshev, and sum over n to get almost sure convergence.",
        "use_case": "Exercise 7.1.6; Brownian quadratic variation along dyadic partitions.",
        "tags": ["quadratic-variation", "borel-cantelli", "chebyshev"],
    },
    {
        "id": "exercise_method_ch7_markov_conditioning_hitting_survival",
        "title": "Deterministic-time Markov conditioning for hitting survival",
        "kind": "proof-template",
        "summary": "Condition on B_s=y, replace the future event by a hitting probability for Brownian motion started at y, and integrate against the transition density.",
        "use_case": "Exercises 7.2.1 and 7.2.2; return-time and last-zero decompositions.",
        "tags": ["markov-property", "hitting-time", "transition-density"],
    },
    {
        "id": "exercise_method_ch7_last_zero_markov_decomposition",
        "title": "Last-zero event as no future hit after conditioning",
        "kind": "calculation-template",
        "summary": "The event L <= t is equivalent to no zero in (t,1]; after conditioning on B_t, this becomes P_y(T_0 > 1-t).",
        "use_case": "Exercise 7.2.2 and arcsine-law calculations.",
        "tags": ["last-zero", "markov-property", "survival-probability"],
    },
    {
        "id": "exercise_method_ch7_dense_local_maxima_from_immediate_crossing",
        "title": "Dense local maxima from immediate two-sided crossing",
        "kind": "proof-template",
        "summary": "Take shrinking deterministic intervals, use continuity to get a maximum, and use immediate crossing forward and backward to rule out endpoints.",
        "use_case": "Exercise 7.2.3; path-local extremum arguments.",
        "tags": ["local-maxima", "immediate-crossing", "brownian-paths"],
    },
    {
        "id": "exercise_method_ch7_germ_limsup_constant",
        "title": "Germ-field limsup constants via Blumenthal 0-1",
        "kind": "proof-template",
        "summary": "For a small-time limsup L, events {L <= r} lie in the germ sigma-field; 0-1 probabilities force L to be almost surely constant.",
        "use_case": "Exercise 7.2.4(i); local Brownian growth rates.",
        "tags": ["blumenthal", "limsup", "germ-field"],
    },
    {
        "id": "exercise_method_ch7_sqrt_time_not_holder_half",
        "title": "Brownian paths are not 1/2-Holder at a fixed time",
        "kind": "proof-template",
        "summary": "Use B_delta/sqrt(delta) standard normal to get positive probability of arbitrarily large normalized values, then apply Blumenthal 0-1.",
        "use_case": "Exercise 7.2.4(ii); critical Brownian Holder exponent.",
        "tags": ["holder", "blumenthal", "sqrt-time"],
    },
    {
        "id": "exercise_method_ch7_fsigma_hitting_time",
        "title": "F-sigma hitting times as infima of closed hitting times",
        "kind": "proof-template",
        "summary": "Write the F-sigma set as a countable union of closed sets, use closed-set hitting times, and express {inf T_n < t} as a countable union.",
        "use_case": "Exercise 7.3.1; proving first-entry times are stopping times.",
        "tags": ["stopping-time", "hitting-time", "f-sigma"],
    },
    {
        "id": "exercise_method_ch7_sum_stopping_time_rational_split",
        "title": "Sum of stopping times via rational split",
        "kind": "proof-template",
        "summary": "Write {S+T<t} as the union over rational q<t of {S<q} cap {T<t-q}.",
        "use_case": "Exercise 7.3.2; closure properties for stopping times.",
        "tags": ["stopping-time", "rationals", "closure"],
    },
    {
        "id": "exercise_method_ch7_sup_inf_stopping_times",
        "title": "Supremum and infimum of stopping times",
        "kind": "proof-template",
        "summary": "Use {inf T_n<t}=union {T_n<t} and {sup T_n<=t}=intersection {T_n<=t}, then build liminf and limsup from sup/inf combinations.",
        "use_case": "Exercise 7.3.3; stopping-time sequence operations.",
        "tags": ["stopping-time", "supremum", "infimum"],
    },
    {
        "id": "exercise_method_ch7_stopped_event_restriction",
        "title": "Use F_S by restricting to {S <= t}",
        "kind": "proof-template",
        "summary": "To prove an event-defined random time is a stopping time, intersect the event A in F_S with {S <= t} and use the definition of F_S.",
        "use_case": "Exercise 7.3.4; killing a stopping time on an event.",
        "tags": ["stopped-sigma-field", "stopping-time", "restriction"],
    },
    {
        "id": "exercise_method_ch7_compare_stopping_times_in_stopped_fields",
        "title": "Comparison events for stopping times are known at either time",
        "kind": "proof-template",
        "summary": "Represent {S<T} or {S>T} on {S<t} using countable rational cuts, then repeat with S and T interchanged.",
        "use_case": "Exercise 7.3.5; stopped sigma-field comparison events.",
        "tags": ["stopped-sigma-field", "rational-cuts", "comparison"],
    },
    {
        "id": "exercise_method_ch7_meet_stopped_sigma_field",
        "title": "Stopped sigma-field at S wedge T",
        "kind": "proof-template",
        "summary": "Use S wedge T <= S,T for one inclusion; for the reverse, decompose A cap {S wedge T <= t} into the union of A cap {S <= t} and A cap {T <= t}.",
        "use_case": "Exercise 7.3.6; identities among stopped sigma-fields.",
        "tags": ["stopped-sigma-field", "minimum", "filtration"],
    },
    {
        "id": "exercise_method_ch7_planar_hitting_cauchy",
        "title": "Planar Brownian level hitting gives Cauchy law",
        "kind": "calculation-template",
        "summary": "Condition the first coordinate on the second-coordinate hitting time, then use the hitting-time Laplace transform to get characteristic function exp(-a|u|).",
        "use_case": "Exercise 7.4.1; Cauchy distribution from Brownian hitting.",
        "tags": ["cauchy", "planar-brownian", "hitting-time"],
    },
    {
        "id": "exercise_method_ch7_return_time_density_mixture",
        "title": "Return-time density by mixing first-hit densities",
        "kind": "calculation-template",
        "summary": "Condition on B_1=y and integrate the first-hitting density from y to 0 against the N(0,1) density.",
        "use_case": "Exercise 7.4.2; density of the next zero after time 1.",
        "tags": ["return-time", "density", "markov-property"],
    },
    {
        "id": "exercise_method_ch7_reflected_endpoint_subdensity",
        "title": "Endpoint subdensity after barrier crossing",
        "kind": "calculation-template",
        "summary": "Reflect paths after the first hit of level a to identify P(T_a<t, B_t in dx) below a with the free Brownian density at 2a-x.",
        "use_case": "Exercise 7.4.3(a,b); reflection-principle refinements.",
        "tags": ["reflection-principle", "subdensity", "barrier"],
    },
    {
        "id": "exercise_method_ch7_joint_max_endpoint_density",
        "title": "Joint density of Brownian maximum and endpoint",
        "kind": "calculation-template",
        "summary": "Use {M_t>a}={T_a<t}, write the reflected endpoint subdensity, and differentiate the tail probability in the maximum level a.",
        "use_case": "Exercise 7.4.3(c); Brownian maximum-endpoint joint law.",
        "tags": ["maximum", "joint-density", "reflection"],
    },
    {
        "id": "exercise_method_ch7_zero_interval_arccos_integral",
        "title": "Zero-in-interval probability by hitting-time density integral",
        "kind": "calculation-template",
        "summary": "Condition on B_s, integrate the first-hit density over [0,t-s], swap integrals, and use u=sqrt(r/s) to get an arccos formula.",
        "use_case": "Exercise 7.4.4; zero-set interval probabilities.",
        "tags": ["zero-set", "hitting-density", "arccos"],
    },
    {
        "id": "exercise_method_ch7_cosh_martingale_exit_laplace",
        "title": "Cosh martingale for symmetric interval exit Laplace transforms",
        "kind": "calculation-template",
        "summary": "Average the plus and minus exponential Brownian martingales to get e^{-lambda t} cosh(sqrt(2lambda) B_t), then stop at +/-a.",
        "use_case": "Exercise 7.5.1; symmetric two-sided exit transform.",
        "tags": ["cosh", "exponential-martingale", "exit-time"],
    },
    {
        "id": "exercise_method_ch7_drift_hitting_exponential_martingale",
        "title": "Drifted Brownian hitting via exponential martingale",
        "kind": "calculation-template",
        "summary": "Choose theta solving theta^2/2 - b theta = lambda, stop exp(theta B_t - theta^2 t/2) at the linear boundary hitting time, and let the cutoff go to infinity.",
        "use_case": "Exercise 7.5.2; Brownian motion with drift hitting a level.",
        "tags": ["drift", "hitting-time", "exponential-martingale"],
    },
    {
        "id": "exercise_method_ch7_interval_exit_laplace_linear_system",
        "title": "Interval exit Laplace transforms from strong Markov linear equations",
        "kind": "calculation-template",
        "summary": "Decompose one-sided hitting transforms by whether the interval exit occurs at a or b, then solve the two equations using exp(-sqrt(2lambda) distance).",
        "use_case": "Exercise 7.5.3; killed Brownian exit transforms.",
        "tags": ["strong-markov", "laplace-transform", "linear-system"],
    },
    {
        "id": "exercise_method_ch7_cauchy_schwarz_exit_moment_comparison",
        "title": "Exit-moment comparison using Cauchy-Schwarz",
        "kind": "inequality-template",
        "summary": "Stop the fourth-degree Brownian polynomial martingale, then bound E(T B_T^2) by sqrt(E T^2) sqrt(E B_T^4).",
        "use_case": "Exercise 7.5.4; nonsymmetric interval exit moments.",
        "tags": ["cauchy-schwarz", "exit-time", "polynomial-martingale"],
    },
    {
        "id": "exercise_method_ch7_sixth_degree_exit_moment",
        "title": "Sixth-degree heat polynomial for third exit-time moment",
        "kind": "calculation-template",
        "summary": "Solve u_t+u_xx/2=0 for x^6-c1 t x^4+c2 t^2 x^2-c3 t^3, stop at +/-a, and insert lower exit moments.",
        "use_case": "Exercise 7.5.5; higher moments of symmetric Brownian exit times.",
        "tags": ["polynomial-martingale", "exit-time-moments", "heat-equation"],
    },
    {
        "id": "exercise_method_ch7_exponential_square_maximal_borel_cantelli",
        "title": "Exponential-square martingale plus maximal inequality",
        "kind": "proof-template",
        "summary": "Use (1+t)^(-1/2) exp(B_t^2/(2(1+t))) as a positive martingale, apply Doob over exponential time blocks, and sum probabilities.",
        "use_case": "Exercise 7.5.6; almost-sure Brownian growth upper bounds.",
        "tags": ["maximal-inequality", "borel-cantelli", "growth-bound"],
    },
    {
        "id": "exercise_method_ch7_ito_affine_martingale_characterization",
        "title": "Ito drift test for f(B_t) martingales",
        "kind": "proof-template",
        "summary": "Ito's formula shows f(B_t) has drift (1/2)f''(B_t)dt; martingality forces the finite-variation drift to vanish, hence f''=0.",
        "use_case": "Exercise 7.6.1; characterizing functions of Brownian motion that are martingales.",
        "tags": ["ito-formula", "martingale", "affine"],
    },
    {
        "id": "exercise_method_ch7_cubic_ito_martingales",
        "title": "Cubic Brownian martingales from Ito formula",
        "kind": "calculation-template",
        "summary": "Use u(t,x)=x^3-3tx for a time-space martingale, or apply Ito to x^3 and subtract the drift integral.",
        "use_case": "Exercise 7.6.2; polynomial Brownian martingales.",
        "tags": ["ito-formula", "cubic", "polynomial-martingale"],
    },
    {
        "id": "exercise_method_ch7_even_moment_ito_recursion",
        "title": "Even Brownian moments by Ito recursion",
        "kind": "calculation-template",
        "summary": "Apply Ito to x^{2k}, take expectations, and solve beta_{2k}'(t)=k(2k-1) beta_{2k-2}(t) with beta_0=1.",
        "use_case": "Exercise 7.6.3; deriving Gaussian even moments.",
        "tags": ["moments", "ito-formula", "gaussian"],
    },
    {
        "id": "exercise_method_ch7_radial_ito_bessel_form",
        "title": "Radial Brownian Ito formula and Bessel drift",
        "kind": "calculation-template",
        "summary": "Approximate |x| near 0, use gradient x/|x| and Laplacian (d-1)/|x| away from 0, and identify the radial martingale part.",
        "use_case": "Exercise 7.6.4; radial Brownian motion and Bessel processes.",
        "tags": ["radial-process", "bessel", "multidimensional-ito"],
    },
    {
        "id": "exercise_method_ch7_squared_norm_ito_dimension_drift",
        "title": "Squared Brownian norm has dimension drift",
        "kind": "calculation-template",
        "summary": "Apply multidimensional Ito to |x|^2; the martingale part is 2 sum_i int B_s^i dB_s^i and the drift is d t.",
        "use_case": "Exercise 7.6.5; computing E|B_t|^2 in R^d.",
        "tags": ["multidimensional-ito", "second-moment", "dimension"],
    },
]


def section_key(exercise: str) -> str:
    parts = exercise.split(".")
    return ".".join(parts[:2])


def parse_exercises(tex: str):
    pattern = re.compile(r"\\section\*\{Exercise ([0-9]+\.[0-9]+\.[0-9]+)\}")
    matches = list(pattern.finditer(tex))
    records = []
    for i, match in enumerate(matches):
        exercise = match.group(1)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else tex.find(r"\end{document}", start)
        block = tex[start:end].strip()
        q_match = re.search(
            r"\\noindent\\textbf\{Question\.\}(.*?)(?=\\Knowledge\{)",
            block,
            flags=re.S,
        )
        k_match = re.search(
            r"\\Knowledge\{(.*?)\}\s*\\noindent\\textbf\{Solution\.\}",
            block,
            flags=re.S,
        )
        s_match = re.search(
            r"\\noindent\\textbf\{Solution\.\}(.*)",
            block,
            flags=re.S,
        )
        question = q_match.group(1).strip() if q_match else ""
        knowledge_tex = k_match.group(1).strip() if k_match else ""
        solution = s_match.group(1).strip() if s_match else ""
        knowledge_ids = re.findall(r"durrett_ch7_[A-Za-z0-9_]+", knowledge_tex)
        sec = section_key(exercise)
        meta = SECTION_METHODS.get(sec, {})
        records.append(
            {
                "id": f"durrett_ch7_exercise_{exercise.replace('.', '_')}",
                "exercise": exercise,
                "chapter": 7,
                "section": sec,
                "section_topic": meta.get("section_topic"),
                "source_tex": str(TEX),
                "source_pdf": str(PDF),
                "question_tex": question,
                "solution_tex": solution,
                "knowledge_used_ids": knowledge_ids,
                "method_summary": meta.get("method_summary"),
                "method_tags": meta.get("method_tags", []),
                "new_knowledge_ids": meta.get("new_knowledge_ids", []),
                "created_at": CREATED,
            }
        )
    return records


def write_jsonl(path: Path, rows):
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")


def main():
    tex = TEX.read_text(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)

    exercise_records = parse_exercises(tex)

    method_cards = []
    for sec, meta in SECTION_METHODS.items():
        method_cards.append(
            {
                "id": f"durrett_ch7_section_{sec.replace('.', '_')}_method_card",
                "chapter": 7,
                "section": sec,
                "title": f"Chapter {sec} exercise method card",
                "section_topic": meta["section_topic"],
                "method_summary": meta["method_summary"],
                "method_tags": meta["method_tags"],
                "new_knowledge_ids": meta["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )

    write_jsonl(OUT / "chapter7_exercise_records.jsonl", exercise_records)
    write_jsonl(OUT / "chapter7_exercise_method_cards.jsonl", method_cards)
    write_jsonl(OUT / "chapter7_exercise_new_knowledge.jsonl", NEW_KNOWLEDGE)

    flashcards = ["id\tfront\tback\ttags"]
    for item in NEW_KNOWLEDGE:
        flashcards.append(
            f"{item['id']}\t{item['title']}\t{item['summary']} Use case: {item['use_case']}\t{','.join(item['tags'])}"
        )
    (OUT / "chapter7_exercise_method_flashcards.tsv").write_text("\n".join(flashcards) + "\n", encoding="utf-8")

    md = [
        "# Chapter 7 Exercise Viki Dataset",
        "",
        f"Source TeX: `{TEX}`",
        f"Source PDF: `{PDF}`",
        "",
        "This dataset turns the solved Chapter 7 Brownian motion exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.",
        "",
        "## Files",
        "",
        "- `chapter7_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.",
        "- `chapter7_exercise_method_cards.jsonl`: section-level method summaries.",
        "- `chapter7_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.",
        "- `chapter7_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.",
        "- `chapter7_exercise_viki.md`: human-readable overview.",
        "- `manifest.json`: dataset metadata.",
        "",
        "## Section Method Cards",
        "",
    ]
    for card in method_cards:
        md.extend(
            [
                f"### {card['section']} - {card['section_topic']}",
                "",
                card["method_summary"],
                "",
                f"Tags: {', '.join(card['method_tags'])}",
                "",
            ]
        )
    md.extend(["## New Knowledge Pieces", ""])
    for item in NEW_KNOWLEDGE:
        md.extend(
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
    (OUT / "chapter7_exercise_viki.md").write_text("\n".join(md), encoding="utf-8")

    manifest = {
        "name": "durrett_chapter7_exercise_viki",
        "description": "LLM/Viki exercise dataset built from solved Durrett Chapter 7 Brownian motion exercises, including questions, solutions, methods, and new reusable knowledge pieces.",
        "created_at": CREATED,
        "source_tex": str(TEX),
        "source_pdf": str(PDF),
        "exercise_record_count": len(exercise_records),
        "method_card_count": len(method_cards),
        "new_knowledge_count": len(NEW_KNOWLEDGE),
        "files": [
            "chapter7_exercise_records.jsonl",
            "chapter7_exercise_method_cards.jsonl",
            "chapter7_exercise_new_knowledge.jsonl",
            "chapter7_exercise_method_flashcards.tsv",
            "chapter7_exercise_viki.md",
            "manifest.json",
        ],
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()

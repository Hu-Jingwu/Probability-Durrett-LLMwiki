from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEX = ROOT / "Chapter1Exercises.tex"
PDF = ROOT / "Chapter1Exercises.pdf"
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter1_Exercise_Viki"
CREATED = datetime.now(timezone.utc).isoformat()


SECTION_METHODS = {
    "1.1": {
        "section_topic": "Probability spaces, sigma-fields, generators, and set algebras",
        "method_summary": "Prove structural set properties directly from closure rules; use generators/countable bases; build counterexamples by violating finite or countable closure.",
        "method_tags": ["sigma-field", "generator", "set-counterexample", "measure-foundations"],
        "new_knowledge_ids": [
            "exercise_method_countable_cocountable_measure",
            "exercise_method_borel_generated_by_half_open_rectangles",
            "exercise_method_increasing_sigma_fields_not_sigma_field",
            "exercise_method_asymptotic_density_block_counterexample",
        ],
    },
    "1.2": {
        "section_topic": "Distributions, normal tails, transformations, and density calculations",
        "method_summary": "Convert distribution questions into CDF/event identities; use jumps for discontinuities; use inverse transformations and normal-tail bounds for explicit calculations.",
        "method_tags": ["cdf", "density-transform", "normal-tail", "probability-integral-transform"],
        "new_knowledge_ids": [
            "exercise_method_piecewise_random_variable_measurability",
            "exercise_method_countable_cdf_discontinuities",
            "exercise_method_density_change_of_variables",
            "exercise_method_square_transform_density",
        ],
    },
    "1.3": {
        "section_topic": "Measurability, generated sigma-fields, semicontinuity, and sigma(X) factorization",
        "method_summary": "Check inverse images on generating classes; express measurability through countable rational cuts; prove closure under limits and construct Borel representatives.",
        "method_tags": ["measurability", "generators", "semicontinuity", "sigma-x-factorization"],
        "new_knowledge_ids": [
            "exercise_method_rational_cut_sum_measurability",
            "exercise_method_closed_sublevel_semicontinuity",
            "exercise_method_oscillation_discontinuity_set",
            "exercise_method_constructive_sigma_x_representation",
        ],
    },
    "1.4": {
        "section_topic": "Lebesgue integration construction and approximation",
        "method_summary": "Approximate integrable functions by simple, step, and continuous functions; use monotone simple approximations and reduction to step functions for oscillatory integrals.",
        "method_tags": ["lebesgue-integral", "simple-approximation", "l1-approximation", "riemann-lebesgue"],
        "new_knowledge_ids": [
            "exercise_method_zero_integral_nonnegative",
            "exercise_method_dyadic_lower_integral_approximation",
            "exercise_method_l1_continuous_approximation",
            "exercise_method_riemann_lebesgue_step_reduction",
        ],
    },
    "1.5": {
        "section_topic": "Lp inequalities, convergence theorems, and absolute continuity of the integral",
        "method_summary": "Use Holder/Minkowski, monotone convergence, dominated convergence, and truncation to prove norm, series, and continuity properties.",
        "method_tags": ["lp", "holder", "minkowski", "mct", "dct", "absolute-continuity"],
        "new_knowledge_ids": [
            "exercise_method_essential_supremum_bound",
            "exercise_method_lp_to_l_infty_limit",
            "exercise_method_density_of_simple_functions_in_lp",
            "exercise_method_absolute_summability_exchange",
        ],
    },
    "1.6": {
        "section_topic": "Expectation, Jensen/Chebyshev, moment bounds, and expectation limits",
        "method_summary": "Translate integral tools into expectation language; use extremal two-point distributions for sharpness, Jensen/Cauchy-Schwarz for inequalities, and MCT/DCT for limits.",
        "method_tags": ["expectation", "jensen", "chebyshev", "moment-bound", "mct", "dct"],
        "new_knowledge_ids": [
            "exercise_method_strict_jensen_equality",
            "exercise_method_two_point_extremizers",
            "exercise_method_paley_zygmund_basic",
            "exercise_method_expectation_tail_truncation",
            "exercise_method_inclusion_exclusion_indicators",
        ],
    },
    "1.7": {
        "section_topic": "Product measures, Fubini/Tonelli, layer-cake formulas, and Stieltjes integration",
        "method_summary": "Turn integrals into product-measure regions; use sections and Tonelli to swap order; interpret Stieltjes integrals geometrically.",
        "method_tags": ["fubini", "tonelli", "product-measure", "layer-cake", "stieltjes"],
        "new_knowledge_ids": [
            "exercise_method_layer_cake_formula",
            "exercise_method_stieltjes_integration_by_parts_with_jumps",
            "exercise_method_interval_sliding_fubini",
            "exercise_method_sine_integral_fubini",
        ],
    },
}


NEW_KNOWLEDGE = [
    {
        "id": "exercise_method_countable_cocountable_measure",
        "title": "Countable/co-countable probability measure",
        "kind": "exercise-derived-method",
        "summary": "To verify the countable/co-countable construction, split disjoint families into the cases where all sets are countable or exactly one set is co-countable.",
        "use_case": "Exercise 1.1.1 and any probability-space verification on unusual sigma-fields.",
        "tags": ["probability-space", "countable-additivity", "co-countable"],
    },
    {
        "id": "exercise_method_borel_generated_by_half_open_rectangles",
        "title": "Borel sigma-field from half-open rectangles",
        "kind": "exercise-derived-method",
        "summary": "Show half-open rectangles are Borel, then express rational open rectangles as countable unions of half-open rectangles; use the countable rational base.",
        "use_case": "Exercises 1.1.2 and 1.1.3; product-measure generation arguments.",
        "tags": ["borel", "generator", "rectangles"],
    },
    {
        "id": "exercise_method_increasing_sigma_fields_not_sigma_field",
        "title": "Increasing union of sigma-fields can fail countable closure",
        "kind": "counterexample-template",
        "summary": "Use finite initial-coordinate sigma-fields on N; their union contains every finite set but misses an infinite non-cofinite set such as the evens.",
        "use_case": "Exercise 1.1.4; distinguishing algebras from sigma-fields.",
        "tags": ["sigma-field", "algebra", "counterexample"],
    },
    {
        "id": "exercise_method_asymptotic_density_block_counterexample",
        "title": "Block construction for asymptotic density counterexamples",
        "kind": "counterexample-template",
        "summary": "Use rapidly growing blocks so the latest block dominates all previous blocks; alternate behavior by blocks to destroy the density of intersections.",
        "use_case": "Exercise 1.1.5 and density/limit counterexamples.",
        "tags": ["asymptotic-density", "counterexample", "blocks"],
    },
    {
        "id": "exercise_method_piecewise_random_variable_measurability",
        "title": "Piecewise random variable measurability",
        "kind": "proof-template",
        "summary": "For Z = X on A and Y on A^c, write {Z <= x} as (A cap {X <= x}) union (A^c cap {Y <= x}).",
        "use_case": "Exercise 1.2.1; patching random variables on measurable events.",
        "tags": ["measurability", "piecewise", "random-variable"],
    },
    {
        "id": "exercise_method_countable_cdf_discontinuities",
        "title": "Countability of CDF jumps",
        "kind": "proof-template",
        "summary": "Group jumps by size bigger than 1/m inside bounded intervals; each group is finite because total CDF increase is at most one.",
        "use_case": "Exercise 1.2.3; monotone-function discontinuity arguments.",
        "tags": ["cdf", "jumps", "countability"],
    },
    {
        "id": "exercise_method_density_change_of_variables",
        "title": "Monotone density change of variables",
        "kind": "calculation-template",
        "summary": "For Y=g(X) with g increasing, compute F_Y(y)=P(X <= g^{-1}(y)) and differentiate to get f_X(g^{-1}(y))/g'(g^{-1}(y)).",
        "use_case": "Exercises 1.2.5 and 1.2.6; lognormal and affine density transforms.",
        "tags": ["density", "change-of-variables", "cdf"],
    },
    {
        "id": "exercise_method_square_transform_density",
        "title": "Density of a square transform",
        "kind": "calculation-template",
        "summary": "For Y=X^2, use F_Y(y)=P(-sqrt(y)<=X<=sqrt(y)) and differentiate to get [f(sqrt(y))+f(-sqrt(y))]/(2sqrt(y)).",
        "use_case": "Exercise 1.2.7; chi-square with one degree of freedom.",
        "tags": ["density", "chi-square", "transformation"],
    },
    {
        "id": "exercise_method_rational_cut_sum_measurability",
        "title": "Rational cut proof for sum measurability",
        "kind": "proof-template",
        "summary": "Write {X+Y<x} as the countable union over q in Q of {X<q} cap {Y<x-q}.",
        "use_case": "Exercise 1.3.2; direct measurability of sums.",
        "tags": ["measurability", "rationals", "sum"],
    },
    {
        "id": "exercise_method_closed_sublevel_semicontinuity",
        "title": "Lower semicontinuity via closed sublevel sets",
        "kind": "proof-template",
        "summary": "A function is lower semicontinuous iff all sets {f <= a} are closed; sequential closure proves one direction and contradiction via subsequences proves the other.",
        "use_case": "Exercise 1.3.5; proving semicontinuous functions are measurable.",
        "tags": ["semicontinuity", "closed-sets", "measurability"],
    },
    {
        "id": "exercise_method_oscillation_discontinuity_set",
        "title": "Discontinuity set from upper and lower local envelopes",
        "kind": "proof-template",
        "summary": "Define local sup and inf over balls, take limits as radius decreases, and identify discontinuities as the set where the limiting envelopes differ.",
        "use_case": "Exercise 1.3.6; measurability of discontinuity sets.",
        "tags": ["discontinuity", "oscillation", "measurability"],
    },
    {
        "id": "exercise_method_constructive_sigma_x_representation",
        "title": "Constructive representation of sigma(X)-measurable functions",
        "kind": "proof-template",
        "summary": "Quantize Y into dyadic bins, represent each bin as {X in B}, build Borel simple functions f_n, then take a measurable pointwise limit f with Y=f(X).",
        "use_case": "Exercises 1.3.8 and 1.3.9; conditional-expectation foundations.",
        "tags": ["sigma-x", "factorization", "dyadic-approximation"],
    },
    {
        "id": "exercise_method_zero_integral_nonnegative",
        "title": "Zero integral of nonnegative function implies zero a.e.",
        "kind": "proof-template",
        "summary": "Use sets {f > 1/n}; each has zero measure because integral dominates (1/n) times its measure, and their union is {f>0}.",
        "use_case": "Exercise 1.4.1; null-set proofs.",
        "tags": ["nonnegative", "zero-integral", "a-e"],
    },
    {
        "id": "exercise_method_dyadic_lower_integral_approximation",
        "title": "Dyadic lower simple approximations",
        "kind": "calculation-template",
        "summary": "Approximate f>=0 by 2^{-n} floor(2^n f); the approximants increase to f and their integrals give monotone sums over dyadic level sets.",
        "use_case": "Exercise 1.4.2 and simple-function approximation.",
        "tags": ["dyadic", "simple-functions", "mct"],
    },
    {
        "id": "exercise_method_l1_continuous_approximation",
        "title": "L1 approximation by continuous functions",
        "kind": "proof-template",
        "summary": "Approximate an integrable function by simple functions, approximate measurable sets by finite interval unions, then round step-function corners.",
        "use_case": "Exercise 1.4.3; density of nice functions in L1 on R.",
        "tags": ["l1", "approximation", "continuous-functions"],
    },
    {
        "id": "exercise_method_riemann_lebesgue_step_reduction",
        "title": "Riemann-Lebesgue by step-function reduction",
        "kind": "proof-template",
        "summary": "Prove oscillatory integral decay for interval indicators explicitly, then approximate any L1 function by a step function.",
        "use_case": "Exercise 1.4.4; oscillatory integral estimates.",
        "tags": ["riemann-lebesgue", "step-functions", "oscillation"],
    },
    {
        "id": "exercise_method_essential_supremum_bound",
        "title": "Essential supremum bounds integrals",
        "kind": "proof-template",
        "summary": "If |g| <= ||g||_infty a.e., then |fg| <= ||g||_infty |f| and integration gives the L1-Linfty Holder endpoint.",
        "use_case": "Exercise 1.5.1; endpoint Holder inequalities.",
        "tags": ["essential-supremum", "holder", "linfty"],
    },
    {
        "id": "exercise_method_lp_to_l_infty_limit",
        "title": "Lp norms converge to Linfty on probability spaces",
        "kind": "proof-template",
        "summary": "Upper bound by essential supremum; lower bound using sets where |f| exceeds M-epsilon and their positive probability.",
        "use_case": "Exercise 1.5.2; norm comparisons.",
        "tags": ["lp", "linfty", "probability-space"],
    },
    {
        "id": "exercise_method_density_of_simple_functions_in_lp",
        "title": "Simple functions are dense in Lp",
        "kind": "proof-template",
        "summary": "Use pointwise simple approximations bounded by |f|, then dominated convergence on |phi_n-f|^p.",
        "use_case": "Exercise 1.5.9; Lp approximation.",
        "tags": ["lp", "simple-functions", "dct"],
    },
    {
        "id": "exercise_method_absolute_summability_exchange",
        "title": "Exchange integral and absolutely summable series",
        "kind": "proof-template",
        "summary": "If sum integral |f_n| is finite, then H=sum |f_n| is integrable; dominated convergence applies to partial sums.",
        "use_case": "Exercise 1.5.10 and 1.7.1 corollary.",
        "tags": ["series", "dct", "absolute-convergence"],
    },
    {
        "id": "exercise_method_strict_jensen_equality",
        "title": "Equality case in strict Jensen",
        "kind": "proof-template",
        "summary": "For strictly convex phi, equality in Jensen forces the random variable to be almost surely constant at its mean.",
        "use_case": "Exercise 1.6.1; strict convexity equality cases.",
        "tags": ["jensen", "strict-convexity", "equality-case"],
    },
    {
        "id": "exercise_method_two_point_extremizers",
        "title": "Two-point distributions as Chebyshev extremizers",
        "kind": "counterexample-template",
        "summary": "To prove sharpness of moment/tail inequalities, place small mass at boundary points and the rest at a value chosen to match moments.",
        "use_case": "Exercises 1.6.3, 1.6.4, and 1.6.5.",
        "tags": ["chebyshev", "sharpness", "two-point"],
    },
    {
        "id": "exercise_method_paley_zygmund_basic",
        "title": "Cauchy-Schwarz lower bound for positive probability",
        "kind": "inequality-template",
        "summary": "For Y>=0, Cauchy-Schwarz applied to Y*1_{Y>0} yields P(Y>0) >= (EY)^2/EY^2.",
        "use_case": "Exercise 1.6.6; basic Paley-Zygmund-style estimates.",
        "tags": ["cauchy-schwarz", "lower-bound", "paley-zygmund"],
    },
    {
        "id": "exercise_method_expectation_tail_truncation",
        "title": "Tail truncation for expectation limits",
        "kind": "proof-template",
        "summary": "Control small or large tails by splitting the event and using continuity of probability plus elementary bounds on the integrand.",
        "use_case": "Exercise 1.6.14; limits involving y E(1/X; X>y).",
        "tags": ["tail", "truncation", "expectation"],
    },
    {
        "id": "exercise_method_inclusion_exclusion_indicators",
        "title": "Indicator expansion for inclusion-exclusion and Bonferroni",
        "kind": "proof-template",
        "summary": "Use 1_union = 1 - product_i(1-1_Ai), expand, and take expectations; partial alternating sums give Bonferroni bounds.",
        "use_case": "Exercises 1.6.9 and 1.6.10.",
        "tags": ["inclusion-exclusion", "bonferroni", "indicators"],
    },
    {
        "id": "exercise_method_layer_cake_formula",
        "title": "Layer-cake formula via product sets",
        "kind": "proof-template",
        "summary": "Represent g(x) as the vertical length of {(x,y):0 <= y < g(x)} and apply Tonelli to integrate sections.",
        "use_case": "Exercise 1.7.2; tail integrals for nonnegative functions.",
        "tags": ["layer-cake", "tonelli", "tail-integral"],
    },
    {
        "id": "exercise_method_stieltjes_integration_by_parts_with_jumps",
        "title": "Stieltjes integration by parts with jump correction",
        "kind": "proof-template",
        "summary": "Interpret Stieltjes integrals as product-measure masses of order regions; the diagonal overlap contributes the product of jump masses.",
        "use_case": "Exercise 1.7.3.",
        "tags": ["stieltjes", "integration-by-parts", "jumps"],
    },
    {
        "id": "exercise_method_interval_sliding_fubini",
        "title": "Sliding interval Fubini identity",
        "kind": "calculation-template",
        "summary": "Write F(x+c)-F(x) as mu((x,x+c]), swap integrals, and observe each fixed t is counted for exactly c units of x.",
        "use_case": "Exercise 1.7.4.",
        "tags": ["fubini", "distribution-function", "sliding-window"],
    },
    {
        "id": "exercise_method_sine_integral_fubini",
        "title": "Sine integral via Fubini",
        "kind": "calculation-template",
        "summary": "Represent sin(x)/x as an integral of e^{-xy} sin(x), integrate in x first, and bound the remaining exponentially damped tails.",
        "use_case": "Exercise 1.7.5.",
        "tags": ["fubini", "sine-integral", "oscillatory-integral"],
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
        knowledge_ids = re.findall(r"durrett_ch1_[A-Za-z0-9_]+", knowledge_tex)
        sec = section_key(exercise)
        meta = SECTION_METHODS.get(sec, {})
        records.append(
            {
                "id": f"durrett_ch1_exercise_{exercise.replace('.', '_')}",
                "exercise": exercise,
                "chapter": 1,
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
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    tex = TEX.read_text(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)

    exercise_records = parse_exercises(tex)

    method_cards = []
    for sec, meta in SECTION_METHODS.items():
        method_cards.append(
            {
                "id": f"durrett_ch1_section_{sec.replace('.', '_')}_method_card",
                "chapter": 1,
                "section": sec,
                "title": f"Chapter {sec} exercise method card",
                "section_topic": meta["section_topic"],
                "method_summary": meta["method_summary"],
                "method_tags": meta["method_tags"],
                "new_knowledge_ids": meta["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )

    write_jsonl(OUT / "chapter1_exercise_records.jsonl", exercise_records)
    write_jsonl(OUT / "chapter1_exercise_method_cards.jsonl", method_cards)
    write_jsonl(OUT / "chapter1_exercise_new_knowledge.jsonl", NEW_KNOWLEDGE)

    flashcards = ["id\tfront\tback\ttags"]
    for item in NEW_KNOWLEDGE:
        flashcards.append(
            f"{item['id']}\t{item['title']}\t{item['summary']} Use case: {item['use_case']}\t{','.join(item['tags'])}"
        )
    (OUT / "chapter1_exercise_method_flashcards.tsv").write_text("\n".join(flashcards) + "\n", encoding="utf-8")

    md = [
        "# Chapter 1 Exercise Viki Dataset",
        "",
        f"Source TeX: `{TEX}`",
        f"Source PDF: `{PDF}`",
        "",
        "This dataset turns the solved Chapter 1 exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.",
        "",
        "## Files",
        "",
        "- `chapter1_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.",
        "- `chapter1_exercise_method_cards.jsonl`: section-level method summaries.",
        "- `chapter1_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.",
        "- `chapter1_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.",
        "- `chapter1_exercise_viki.md`: human-readable overview.",
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
    (OUT / "chapter1_exercise_viki.md").write_text("\n".join(md), encoding="utf-8")

    manifest = {
        "name": "durrett_chapter1_exercise_viki",
        "description": "LLM/Viki exercise dataset built from solved Durrett Chapter 1 exercises, including questions, solutions, methods, and new reusable knowledge pieces.",
        "created_at": CREATED,
        "source_tex": str(TEX),
        "source_pdf": str(PDF),
        "exercise_record_count": len(exercise_records),
        "method_card_count": len(method_cards),
        "new_knowledge_count": len(NEW_KNOWLEDGE),
        "files": [
            "chapter1_exercise_records.jsonl",
            "chapter1_exercise_method_cards.jsonl",
            "chapter1_exercise_new_knowledge.jsonl",
            "chapter1_exercise_method_flashcards.tsv",
            "chapter1_exercise_viki.md",
            "manifest.json",
        ],
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

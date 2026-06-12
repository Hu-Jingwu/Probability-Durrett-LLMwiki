from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter6_Knowledge"
SOURCE_FILE = ROOT / "Probability/Textbook/Chapters/PTE-Chapter6.pdf"
SOURCE_TEX = ROOT / "Probability/Exercises/Chapter6/Chapter6Exercises.tex"
SOURCE_PDF = ROOT / "Probability/Exercises/Chapter6/Chapter6Exercises.pdf"

CREATED = datetime.now(timezone.utc).isoformat()


SECTION_METHODS = {
    "6.1": {
        "section_topic": "Stationarity, invariant events, ergodicity, and measure-preserving examples",
        "method_summary": "Convert stationary processes to shift or measure-preserving models; prove invariance through pullbacks; use density, factor maps, random phases, and branch decompositions for examples.",
        "method_tags": ["stationarity", "invariant-events", "ergodicity", "shift-model", "measure-preserving"],
        "new_knowledge_ids": [
            "ch6_exercise_method_invariant_sigma_field_measurable_functions",
            "ch6_exercise_method_almost_invariant_strictification",
            "ch6_exercise_method_direct_irrational_rotation_ergodicity",
            "ch6_exercise_method_two_sided_stationary_extension",
            "ch6_exercise_method_factor_stationarity_ergodicity",
            "ch6_exercise_method_random_phase_iid_blocks",
            "ch6_exercise_method_gauss_map_invariant_density",
        ],
    },
    "6.2": {
        "section_topic": "Birkhoff upgrades, moving observables, and maximal inequalities",
        "method_summary": "Upgrade Birkhoff convergence by truncation and Jensen; compare moving functions to a fixed limit using tail suprema or Cesaro L1 bounds; derive maximal inequalities by centering with a threshold.",
        "method_tags": ["birkhoff", "lp-convergence", "truncation", "moving-observable", "maximal-inequality"],
        "new_knowledge_ids": [
            "ch6_exercise_method_lp_upgrade_by_truncation",
            "ch6_exercise_method_moving_observable_ergodic_average",
            "ch6_exercise_method_wiener_maximal_from_maximal_ergodic",
        ],
    },
    "6.3": {
        "section_topic": "Range growth, recurrence, cycle tricks, and stationary renewal bias",
        "method_summary": "Count range by last visits, identify escape probability through range growth, and use two-sided stationarity to turn return cycles into occupation and waiting-time identities.",
        "method_tags": ["recurrence", "range", "last-visit", "cycle-trick", "stationary-renewal"],
        "new_knowledge_ids": [
            "ch6_exercise_method_range_last_visit_counting",
            "ch6_exercise_method_positive_drift_escape_probability",
            "ch6_exercise_method_cycle_trick_occupation_ratio",
            "ch6_exercise_method_stationary_renewal_waiting_bias",
        ],
    },
    "6.5": {
        "section_topic": "Applications of subadditivity to LCS, LIS, Poisson paths, and branching",
        "method_summary": "Check deterministic subadditivity rates, use first-moment bounds for subsequence problems, exploit Poisson greedy paths, and build exponential martingales for branching-process speed bounds.",
        "method_tags": ["subadditivity", "first-moment", "poissonization", "branching-martingale", "large-deviations"],
        "new_knowledge_ids": [
            "ch6_exercise_method_arbitrarily_slow_subadditive_convergence",
            "ch6_exercise_method_lcs_first_moment_bounds",
            "ch6_exercise_method_poisson_greedy_increasing_path_lower_bound",
            "ch6_exercise_method_permutation_lis_first_moment_upper_bound",
            "ch6_exercise_method_branching_laplace_martingale_bound",
        ],
    },
}


NEW_KNOWLEDGE = [
    {
        "id": "ch6_exercise_method_invariant_sigma_field_measurable_functions",
        "title": "Invariant sigma-field and invariant random variables",
        "kind": "exercise-derived-method",
        "summary": "Show invariant events form a sigma-field by pullback closure; prove an I-measurable random variable is invariant by checking rational cuts, and conversely use invariant inverse images.",
        "use_case": "Exercise 6.1.1; identifying E(X|I) and invariant limits.",
        "tags": ["invariant-sigma-field", "measurability", "rational-cuts"],
    },
    {
        "id": "ch6_exercise_method_almost_invariant_strictification",
        "title": "Strict representative for almost invariant sets",
        "kind": "proof-template",
        "summary": "From an almost invariant set, form a forward pullback union B and then C=intersection phi^{-n}B; C is strictly invariant and differs only by a null set.",
        "use_case": "Exercise 6.1.2; replacing mod-null invariance by exact invariance.",
        "tags": ["almost-invariant", "strict-invariance", "null-sets"],
    },
    {
        "id": "ch6_exercise_method_direct_irrational_rotation_ergodicity",
        "title": "Direct density proof of irrational rotation ergodicity",
        "kind": "proof-template",
        "summary": "Use pigeonhole gaps to prove the irrational orbit is dense, approximate positive-measure sets by high-density intervals, and contradict coexistence of invariant A and A^c with positive measure.",
        "use_case": "Exercise 6.1.3; proving ergodicity without Fourier series.",
        "tags": ["irrational-rotation", "density-points", "ergodicity"],
    },
    {
        "id": "ch6_exercise_method_two_sided_stationary_extension",
        "title": "Two-sided extension of a stationary sequence",
        "kind": "construction",
        "summary": "Define finite-dimensional laws on integer-indexed coordinates by shifting all indices into the nonnegative side, then use stationarity for consistency and Kolmogorov extension.",
        "use_case": "Exercise 6.1.4; return-time and cycle arguments needing negative times.",
        "tags": ["stationary-process", "two-sided", "kolmogorov-extension"],
    },
    {
        "id": "ch6_exercise_method_factor_stationarity_ergodicity",
        "title": "Stationarity and ergodicity pass to factors",
        "kind": "proof-template",
        "summary": "For Y_k=g(X_k,X_{k+1},...), stationarity follows from shifted future laws; invariant events for Y pull back to invariant events for X, so ergodicity passes to Y.",
        "use_case": "Exercise 6.1.5; creating stationary derived processes.",
        "tags": ["factor-map", "stationarity", "ergodicity"],
    },
    {
        "id": "ch6_exercise_method_random_phase_iid_blocks",
        "title": "Random phase makes iid blocks stationary and ergodic",
        "kind": "construction",
        "summary": "Concatenate iid blocks and start at an independent uniform phase; one-step shifts rotate the phase and occasionally shift the iid block sequence, giving stationarity and ergodicity.",
        "use_case": "Exercise 6.1.6; block constructions with stationary output.",
        "tags": ["iid-blocks", "random-phase", "ergodicity"],
    },
    {
        "id": "ch6_exercise_method_gauss_map_invariant_density",
        "title": "Gauss map invariant density by branch telescoping",
        "kind": "calculation-template",
        "summary": "For phi(x)=1/x-floor(1/x), split into branches x=1/(k+y); the transformed density sum telescopes to 1/(1+y).",
        "use_case": "Exercise 6.1.7; verifying the continued-fraction invariant measure.",
        "tags": ["continued-fractions", "gauss-map", "invariant-density"],
    },
    {
        "id": "ch6_exercise_method_lp_upgrade_by_truncation",
        "title": "Lp upgrade of Birkhoff by truncation",
        "kind": "proof-template",
        "summary": "Prove Lp convergence for bounded observables by bounded convergence, then truncate X and control the tail using Jensen plus Lp contraction of conditional expectation.",
        "use_case": "Exercise 6.2.1; upgrading ergodic averages from L1 to Lp.",
        "tags": ["birkhoff", "lp", "truncation", "jensen"],
    },
    {
        "id": "ch6_exercise_method_moving_observable_ergodic_average",
        "title": "Moving observable ergodic average",
        "kind": "proof-template",
        "summary": "Decompose averages of g_m(phi^m) into the fixed g average plus errors; control a.s. errors by tail suprema and L1 errors by Cesaro means.",
        "use_case": "Exercise 6.2.2; triangular or time-varying observables in ergodic averages.",
        "tags": ["moving-observable", "tail-supremum", "cesaro", "birkhoff"],
    },
    {
        "id": "ch6_exercise_method_wiener_maximal_from_maximal_ergodic",
        "title": "Wiener maximal inequality from maximal ergodic lemma",
        "kind": "proof-template",
        "summary": "Apply the maximal ergodic lemma to Y=X-alpha so the positivity event of the shifted partial sums is exactly {max S_j/j > alpha}.",
        "use_case": "Exercise 6.2.3; deriving maximal probability bounds for ergodic averages.",
        "tags": ["maximal-ergodic-lemma", "wiener-inequality", "threshold-shift"],
    },
    {
        "id": "ch6_exercise_method_range_last_visit_counting",
        "title": "Range expectation by last-visit decomposition",
        "kind": "calculation-template",
        "summary": "Count each visited site by its last visit time; stationarity makes the probability of no future revisit over n-m steps equal to g_{n-m}.",
        "use_case": "Exercise 6.3.1; expected range identities for stationary-increment walks.",
        "tags": ["range", "last-visit", "stationary-increments"],
    },
    {
        "id": "ch6_exercise_method_positive_drift_escape_probability",
        "title": "Positive drift escape probability from range growth",
        "kind": "proof-template",
        "summary": "With ergodic integer increments bounded above by one and positive mean, the range grows at the same rate as the running maximum; Theorem 6.3.1 identifies the rate with P(escape).",
        "use_case": "Exercise 6.3.2; recurrence/escape probabilities under stationary increments.",
        "tags": ["positive-drift", "escape-probability", "range-growth"],
    },
    {
        "id": "ch6_exercise_method_cycle_trick_occupation_ratio",
        "title": "Cycle trick occupation ratio",
        "kind": "proof-template",
        "summary": "Use a two-sided stationary version and partition by the last visit to A before time 0; expected B-occupation in an A-cycle equals P(X0 in B)/P(X0 in A).",
        "use_case": "Exercise 6.3.3; constructing stationary measures from excursions.",
        "tags": ["cycle-trick", "occupation-time", "two-sided-stationarity"],
    },
    {
        "id": "ch6_exercise_method_stationary_renewal_waiting_bias",
        "title": "Stationary renewal first-waiting bias",
        "kind": "calculation-template",
        "summary": "Under conditioning on a renewal at time 0, stationarity of return gaps gives P(T=n)=Pbar(T>=n)/Ebar T for the waiting time seen from a stationary time.",
        "use_case": "Exercise 6.3.4; inspection-paradox and stationary renewal calculations.",
        "tags": ["renewal", "waiting-time", "kac", "stationary-bias"],
    },
    {
        "id": "ch6_exercise_method_arbitrarily_slow_subadditive_convergence",
        "title": "Arbitrarily slow deterministic subadditive convergence",
        "kind": "counterexample-template",
        "summary": "Set X_{m,m+k}=f(k) with f(k)/k decreasing; subadditivity follows by comparing both pieces to f(n)/n, so the expectation convergence can be as slow as f(n)/n.",
        "use_case": "Exercise 6.5.1; understanding limits of Fekete-type convergence rates.",
        "tags": ["subadditivity", "slow-convergence", "fekete"],
    },
    {
        "id": "ch6_exercise_method_lcs_first_moment_bounds",
        "title": "Longest common subsequence first-moment bounds",
        "kind": "calculation-template",
        "summary": "Compute small-n expectations for lower bounds and bound P(L_n >= K) by the expected number of matching index-pair subsequences, binom(n,K)^2 2^{-K}.",
        "use_case": "Exercise 6.5.2; bounding LCS constants.",
        "tags": ["longest-common-subsequence", "first-moment", "entropy-bound"],
    },
    {
        "id": "ch6_exercise_method_poisson_greedy_increasing_path_lower_bound",
        "title": "Poisson greedy path lower bound",
        "kind": "calculation-template",
        "summary": "Choose successive Poisson points minimizing x+y in the northeast quadrant; the increment sum has tail exp(-t^2/2), giving mean coordinate step sqrt(pi/8) and gamma >= sqrt(8/pi).",
        "use_case": "Exercise 6.5.3; lower bounds for Hammersley's increasing path constant.",
        "tags": ["poisson-process", "greedy-path", "lis-lower-bound"],
    },
    {
        "id": "ch6_exercise_method_permutation_lis_first_moment_upper_bound",
        "title": "Permutation LIS upper bound by first moment",
        "kind": "calculation-template",
        "summary": "For a fixed k-subset of indices, the values are increasing with probability 1/k!, so E J_k^n=binom(n,k)/k!; Stirling with k~alpha sqrt(n) gives gamma <= e.",
        "use_case": "Exercise 6.5.4; upper bounds for longest increasing subsequences.",
        "tags": ["random-permutation", "lis", "first-moment", "stirling"],
    },
    {
        "id": "ch6_exercise_method_branching_laplace_martingale_bound",
        "title": "Branching Laplace martingale speed bound",
        "kind": "proof-template",
        "summary": "Normalize the generation-n Laplace sum by (mu phi(theta))^n to get a nonnegative martingale; Markov's inequality bounds early birth events when exp(-theta a)/(mu phi(theta))>1.",
        "use_case": "Exercise 6.5.5; age-dependent branching speed upper-tail bounds.",
        "tags": ["branching-process", "laplace-transform", "martingale", "large-deviations"],
    },
]


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def clean_tex(text: str) -> str:
    return text.strip()


def section_of_exercise(exercise: str) -> str:
    parts = exercise.split(".")
    return ".".join(parts[:2])


def parse_exercises() -> list[dict]:
    text = SOURCE_TEX.read_text(encoding="utf-8")
    parts = re.split(r"\\section\*\{Exercise ([0-9.]+)\}", text)
    records = []
    for exercise, body in zip(parts[1::2], parts[2::2]):
        body = body.split(r"\section*{Exercise", 1)[0].rsplit(r"\end{document}", 1)[0]
        q_match = re.search(
            r"\\noindent\\textbf\{Question\.\}\s*(.*?)\s*\\Knowledge\{",
            body,
            flags=re.S,
        )
        k_match = re.search(
            r"\\Knowledge\{\s*(.*?)\s*\}\s*\\noindent\\textbf\{Solution\.\}",
            body,
            flags=re.S,
        )
        s_match = re.search(
            r"\\noindent\\textbf\{Solution\.\}\s*(.*)",
            body,
            flags=re.S,
        )
        if not (q_match and k_match and s_match):
            raise ValueError(f"Could not parse exercise {exercise}")
        section = section_of_exercise(exercise)
        method = SECTION_METHODS[section]
        knowledge_ids = re.findall(r"\\path\{([^}]+)\}", k_match.group(1))
        records.append(
            {
                "id": f"durrett_ch6_exercise_{exercise.replace('.', '_')}",
                "exercise": exercise,
                "chapter": 6,
                "section": section,
                "section_topic": method["section_topic"],
                "source_tex": str(SOURCE_TEX),
                "source_pdf": str(SOURCE_PDF),
                "question_tex": clean_tex(q_match.group(1)),
                "solution_tex": clean_tex(s_match.group(1)),
                "knowledge_used_ids": knowledge_ids,
                "method_summary": method["method_summary"],
                "method_tags": method["method_tags"],
                "new_knowledge_ids": method["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )
    return records


def method_cards() -> list[dict]:
    cards = []
    for section, method in SECTION_METHODS.items():
        cards.append(
            {
                "id": f"durrett_ch6_section_{section.replace('.', '_')}_method_card",
                "chapter": 6,
                "section": section,
                "title": f"Chapter {section} exercise method card",
                "section_topic": method["section_topic"],
                "method_summary": method["method_summary"],
                "method_tags": method["method_tags"],
                "new_knowledge_ids": method["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )
    return cards


def normalize_kind(kind: str) -> str:
    if kind == "exercise-derived-method":
        return "exercise-pattern"
    return kind


def exercise_pieces(new_knowledge: list[dict], cards: list[dict], records: list[dict]) -> list[dict]:
    id_to_card = {}
    for card in cards:
        for kid in card["new_knowledge_ids"]:
            id_to_card[kid] = card

    id_to_exercises: dict[str, set[str]] = defaultdict(set)
    id_to_related: dict[str, set[str]] = defaultdict(set)
    for record in records:
        for kid in record["new_knowledge_ids"]:
            id_to_exercises[kid].add(record["exercise"])
            id_to_related[kid].update(record["knowledge_used_ids"])

    pieces = []
    for item in new_knowledge:
        card = id_to_card[item["id"]]
        pieces.append(
            {
                "id": item["id"],
                "source": "Solved Durrett Chapter 6 exercises and exercise viki records",
                "source_file": str(SOURCE_TEX),
                "source_pdf": str(SOURCE_PDF),
                "chapter": 6,
                "section": f"{card['section']} Exercises: {card['section_topic']}",
                "title": item["title"],
                "kind": normalize_kind(item["kind"]),
                "summary": item["summary"],
                "proof_idea": card["method_summary"],
                "exam_use": item["use_case"],
                "pitfalls": "Check stationarity, ergodicity, integrability, and indexing hypotheses before reusing the pattern.",
                "tags": item["tags"],
                "related_ids": sorted(id_to_related[item["id"]]),
                "source_exercises": sorted(id_to_exercises[item["id"]]),
                "created_at": item.get("created_at", CREATED),
                "merged_at": CREATED,
            }
        )
    return pieces


def back_text(piece: dict) -> str:
    parts = [piece.get("summary", "")]
    if piece.get("exam_use"):
        parts.append(f"Exam use: {piece['exam_use']}")
    if piece.get("pitfalls"):
        parts.append(f"Pitfall: {piece['pitfalls']}")
    return " ".join(part for part in parts if part)


def write_flashcards(path: Path, pieces: list[dict]) -> None:
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


def write_method_flashcards(path: Path, new_knowledge: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["id", "front", "back", "tags"])
        for item in new_knowledge:
            writer.writerow(
                [
                    item["id"],
                    item["title"],
                    f"{item['summary']} Use case: {item['use_case']}",
                    ",".join(item["tags"]),
                ]
            )


def write_exercise_viki(path: Path, records: list[dict], cards: list[dict], new_knowledge: list[dict]) -> None:
    lines = [
        "# Chapter 6 Exercise Viki Dataset",
        "",
        f"Source TeX: `{SOURCE_TEX}`",
        f"Source PDF: `{SOURCE_PDF}`",
        "",
        "This dataset turns the solved Chapter 6 exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.",
        "",
        "## Files",
        "",
        "- `chapter6_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.",
        "- `chapter6_exercise_method_cards.jsonl`: section-level method summaries.",
        "- `chapter6_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.",
        "- `chapter6_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.",
        "- `chapter6_exercise_viki.md`: human-readable overview.",
        "- `manifest.json`: dataset metadata.",
        "",
        "## Section Method Cards",
        "",
    ]
    for card in cards:
        lines.extend(
            [
                f"### {card['section']} - {card['section_topic']}",
                "",
                card["method_summary"],
                "",
                f"Tags: {', '.join(card['method_tags'])}",
                "",
            ]
        )

    lines.extend(["## New Knowledge Pieces", ""])
    for item in new_knowledge:
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

    by_section: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        by_section[record["section"]].append(record)

    lines.extend(["## Exercise Record Index", ""])
    for section in sorted(by_section):
        topic = by_section[section][0]["section_topic"]
        lines.extend([f"### {section} - {topic}", ""])
        for record in by_section[section]:
            lines.append(
                f"- Exercise {record['exercise']}: method tags `{', '.join(record['method_tags'])}`; "
                f"knowledge used `{', '.join(record['knowledge_used_ids'])}`; "
                f"new knowledge `{', '.join(record['new_knowledge_ids'])}`."
            )
        lines.append("")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_unified_markdown(path: Path, section_guides: list[dict], pieces: list[dict], cards: list[dict], records: list[dict]) -> None:
    lines = [
        "# Durrett Chapter 6 LLM Viki: Ergodic Theorems",
        "",
        "Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter6.pdf`.",
        "",
        "This unified Chapter 6 knowledge base includes textbook knowledge pieces plus exercise-derived method patterns from the solved Chapter 6 exercises.",
        "",
        "Exercise source: `Probability/Exercises/Chapter6/Chapter6Exercises.tex` and `Probability/Exercises/Chapter6/Chapter6Exercises.pdf`.",
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
                f"- Goal: {guide['study_goal']}",
                "",
                f"- Must master: {', '.join(guide['must_master'])}",
                "",
                f"- Prelim angle: {guide['prelim_angle']}",
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
    for card in cards:
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

    lines.extend(["## Exercise Record Index", ""])
    for record in records:
        lines.append(
            f"- Exercise {record['exercise']}: method tags `{', '.join(record['method_tags'])}`; "
            f"knowledge used `{', '.join(record['knowledge_used_ids'])}`."
        )

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    records = parse_exercises()
    cards = method_cards()
    new_knowledge = [{**item, "created_at": CREATED} for item in NEW_KNOWLEDGE]

    write_jsonl(OUT / "chapter6_exercise_records.jsonl", records)
    write_jsonl(OUT / "chapter6_exercise_method_cards.jsonl", cards)
    write_jsonl(OUT / "chapter6_exercise_new_knowledge.jsonl", new_knowledge)
    write_method_flashcards(OUT / "chapter6_exercise_method_flashcards.tsv", new_knowledge)
    write_exercise_viki(OUT / "chapter6_exercise_viki.md", records, cards, new_knowledge)

    current_pieces = read_jsonl(OUT / "chapter6_knowledge_pieces.jsonl")
    textbook_pieces = [
        piece for piece in current_pieces if not piece["id"].startswith("ch6_exercise_method_")
    ]
    write_jsonl(OUT / "chapter6_textbook_knowledge_pieces.jsonl", textbook_pieces)

    exercise_derived_pieces = exercise_pieces(new_knowledge, cards, records)
    combined_pieces = textbook_pieces + exercise_derived_pieces
    section_guides = read_jsonl(OUT / "chapter6_section_guides.jsonl")

    write_jsonl(OUT / "chapter6_knowledge_pieces.jsonl", combined_pieces)
    write_flashcards(OUT / "chapter6_flashcards.tsv", combined_pieces)
    write_unified_markdown(OUT / "chapter6_viki.md", section_guides, combined_pieces, cards, records)

    manifest = {
        "name": "durrett_chapter6_ergodic_theorems_llm_viki",
        "description": "Unified LLM/Viki-style knowledge base for Chapter 6 of Durrett Probability: Theory and Examples, including textbook knowledge pieces and exercise-derived method patterns.",
        "source_file": str(SOURCE_FILE),
        "source_tex": str(SOURCE_TEX),
        "source_pdf": str(SOURCE_PDF),
        "created_at": CREATED,
        "piece_count": len(combined_pieces),
        "textbook_piece_count": len(textbook_pieces),
        "exercise_derived_piece_count": len(exercise_derived_pieces),
        "section_count": len(section_guides),
        "exercise_record_count": len(records),
        "method_card_count": len(cards),
        "files": [
            "chapter6_knowledge_pieces.jsonl",
            "chapter6_textbook_knowledge_pieces.jsonl",
            "chapter6_section_guides.jsonl",
            "chapter6_viki.md",
            "chapter6_flashcards.tsv",
            "chapter6_exercise_records.jsonl",
            "chapter6_exercise_method_cards.jsonl",
            "chapter6_exercise_new_knowledge.jsonl",
            "chapter6_exercise_method_flashcards.tsv",
            "chapter6_exercise_viki.md",
            "manifest.json",
        ],
    }
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

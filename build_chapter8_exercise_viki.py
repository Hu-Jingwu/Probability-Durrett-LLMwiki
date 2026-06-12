from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEX = ROOT / "Probability/Exercises/Chapter8/Chapter8Exercises.tex"
PDF = ROOT / "Probability/Exercises/Chapter8/Chapter8Exercises.pdf"
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter8_Knowledge"
CREATED = datetime.now(timezone.utc).isoformat()


SECTION_METHODS = {
    "8.1": {
        "section_topic": "Donsker embedding, random-walk path functionals, and Brownian transfer",
        "method_summary": "Condition on the Skorokhod embedding interval for Brownian exit-time estimates; use Donsker plus continuous mapping for range, maximum, and occupation-type walk functionals.",
        "method_tags": ["donsker", "skorokhod-embedding", "brownian-exit-time", "continuous-mapping", "random-walk-range"],
        "new_knowledge_ids": [
            "exercise_method_conditional_exit_time_moment_transfer",
            "exercise_method_random_walk_range_via_donsker",
        ],
    },
    "8.3": {
        "section_topic": "Stationary sequence CLTs and martingale/coboundary approximation",
        "method_summary": "Center the statistic, verify finite dependence or projective summability, compute long-run variance from covariances, and identify the martingale approximation term from the proof.",
        "method_tags": ["stationary-clt", "m-dependent", "long-run-variance", "martingale-approximation", "head-runs"],
        "new_knowledge_ids": [
            "exercise_method_head_run_long_run_variance",
            "exercise_method_gordin_y0_computation",
        ],
    },
    "8.4": {
        "section_topic": "Brownian bridge, empirical-process limits, and pinned Brownian calculations",
        "method_summary": "Represent the bridge as Brownian motion pinned at time one; compute bridge probabilities by conditioning transition densities, and prove bridge Markov/martingale properties from its transition kernel.",
        "method_tags": ["brownian-bridge", "pinned-brownian-motion", "reflection-principle", "transition-density", "martingale"],
        "new_knowledge_ids": [
            "exercise_method_bridge_tail_conditioned_reflection",
            "exercise_method_bridge_time_change_covariance",
            "exercise_method_bridge_markov_kernel_cancellation",
            "exercise_method_bridge_remaining_time_martingale",
        ],
    },
    "8.5": {
        "section_topic": "Laws of the iterated logarithm and Strassen limit sets",
        "method_summary": "Use tail sums and Borel-Cantelli to show heavy-tailed jumps break LIL scaling; use continuous endpoint evaluation of Strassen's functional limit set for scalar limit points.",
        "method_tags": ["lil", "borel-cantelli", "heavy-tail", "strassen", "functional-lil"],
        "new_knowledge_ids": [
            "exercise_method_heavy_tail_jump_obstruction_lil",
            "exercise_method_strassen_endpoint_limit_set",
        ],
    },
}


NEW_KNOWLEDGE = [
    {
        "id": "exercise_method_conditional_exit_time_moment_transfer",
        "title": "Conditional exit-time moment transfer",
        "kind": "exercise-derived-method",
        "summary": "When a Skorokhod embedding is a mixture of Brownian exits from intervals, apply exit-time estimates conditionally on the random interval and then integrate over the mixing law.",
        "use_case": "Exercise 8.1.1; transferring Exercise 7.5.4 bounds to the random time T_{U,V}.",
        "tags": ["skorokhod-embedding", "brownian-exit-time", "conditioning", "moment-bound"],
    },
    {
        "id": "exercise_method_random_walk_range_via_donsker",
        "title": "Random-walk range via Donsker",
        "kind": "calculation-template",
        "summary": "For one-dimensional nearest-neighbor walks, visited sites form the interval between running min and max; divide by sqrt(n), apply Donsker to the continuous range functional, and drop the 1/sqrt(n) endpoint correction.",
        "use_case": "Exercise 8.1.2 and random-walk range asymptotics.",
        "tags": ["donsker", "range", "continuous-mapping", "simple-random-walk"],
    },
    {
        "id": "exercise_method_head_run_long_run_variance",
        "title": "Head-run CLT variance from 1-dependence",
        "kind": "calculation-template",
        "summary": "For indicators of the pattern HT in fair coin flips, center by mu=1/4 and compute long-run variance as Var(eta_0)+2 Cov(eta_0,eta_1)=1/16 because adjacent HT events are mutually exclusive.",
        "use_case": "Exercise 8.3.1; finite-dependence stationary CLT computations.",
        "tags": ["stationary-clt", "m-dependent", "long-run-variance", "pattern-counting"],
    },
    {
        "id": "exercise_method_gordin_y0_computation",
        "title": "Computing Gordin's Y0 in finite-dependence examples",
        "kind": "proof-template",
        "summary": "Use Y0=sum_j>=0(E(X_j|F_0)-E(X_j|F_{-1})); finite dependence kills all but finitely many terms, leaving explicit conditional expectations.",
        "use_case": "Exercise 8.3.1 and martingale approximation examples.",
        "tags": ["gordin", "martingale-approximation", "conditional-expectation", "stationary-clt"],
    },
    {
        "id": "exercise_method_bridge_tail_conditioned_reflection",
        "title": "One-sided Brownian bridge tail by conditioned reflection",
        "kind": "proof-template",
        "summary": "Compute P(max bridge > b) by viewing the bridge as Brownian motion conditioned on B_1=0 and using the reflected Brownian density on {T_b<1}.",
        "use_case": "Exercise 8.4.1; bridge extrema and Kolmogorov-Smirnov limit calculations.",
        "tags": ["brownian-bridge", "reflection-principle", "conditional-density", "tail"],
    },
    {
        "id": "exercise_method_bridge_time_change_covariance",
        "title": "Brownian bridge from time-changed Brownian motion",
        "kind": "construction",
        "summary": "To prove X_t=(1-t)B(t/(1-t)) is a bridge, show it is centered Gaussian with covariance s(1-t) for s<=t and continuous extension X_1=0.",
        "use_case": "Exercise 8.4.2; recognizing Gaussian process identities.",
        "tags": ["brownian-bridge", "time-change", "gaussian-process", "covariance"],
    },
    {
        "id": "exercise_method_bridge_markov_kernel_cancellation",
        "title": "Brownian bridge Markov kernel by density cancellation",
        "kind": "proof-template",
        "summary": "Write pinned finite-dimensional densities as products of Brownian transition densities ending at zero; divide joint densities so all pre-s factors cancel, leaving a kernel depending only on the present state.",
        "use_case": "Exercise 8.4.3; proving Markov property for conditioned Gaussian processes.",
        "tags": ["brownian-bridge", "markov-property", "transition-density", "conditioning"],
    },
    {
        "id": "exercise_method_bridge_remaining_time_martingale",
        "title": "Bridge divided by remaining time is a martingale",
        "kind": "proof-template",
        "summary": "Use E(B_t^0|B_s^0)=((1-t)/(1-s))B_s^0 to show B_t^0/(1-t) is a martingale; L2 norms grow like t/(1-t), so it is not L2 bounded.",
        "use_case": "Exercise 8.4.4; bridge martingales and terminal singularity checks.",
        "tags": ["brownian-bridge", "martingale", "l2-boundedness", "transition-kernel"],
    },
    {
        "id": "exercise_method_heavy_tail_jump_obstruction_lil",
        "title": "Heavy-tailed jumps obstruct LIL scaling",
        "kind": "proof-template",
        "summary": "If E|X|^alpha is infinite with alpha<2, tail sums at scale n^{1/alpha} diverge; Borel-Cantelli gives infinitely many huge increments, forcing adjacent partial sums above sqrt(n log log n) scale.",
        "use_case": "Exercise 8.5.1 and necessity intuition for finite variance in LIL.",
        "tags": ["lil", "heavy-tail", "borel-cantelli", "large-jumps"],
    },
    {
        "id": "exercise_method_strassen_endpoint_limit_set",
        "title": "Scalar LIL limit set from Strassen endpoint evaluation",
        "kind": "proof-template",
        "summary": "Apply the continuous map f -> f(1) to Strassen's compact LIL limit set; Cauchy-Schwarz bounds endpoints by [-1,1], and linear functions f(t)=at realize every endpoint.",
        "use_case": "Exercise 8.5.2; deriving scalar limsup/limit-set results from functional LIL.",
        "tags": ["strassen", "functional-lil", "endpoint-map", "limit-set"],
    },
]


def write_jsonl(path: Path, rows):
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def extract_exercise_blocks(tex: str):
    pattern = re.compile(
        r"\\section\*\{Exercise ([0-9]+\.[0-9]+\.[0-9]+)\}(.*?)(?=\\section\*\{|\\end\{document\})",
        re.S,
    )
    for match in pattern.finditer(tex):
        exercise = match.group(1)
        block = match.group(2)
        q_match = re.search(r"\\noindent\\textbf\{Question\.\}(.*?)(?=\\Knowledge\{)", block, re.S)
        k_match = re.search(r"\\Knowledge\{(.*?)\}\s*\\noindent\\textbf\{Solution\.\}", block, re.S)
        s_match = re.search(r"\\noindent\\textbf\{Solution\.\}(.*)", block, re.S)
        if not (q_match and k_match and s_match):
            raise ValueError(f"Could not parse exercise {exercise}")
        question = q_match.group(1).strip()
        solution = s_match.group(1).strip()
        knowledge_ids = re.findall(r"\\path\{([^}]+)\}", k_match.group(1))
        yield exercise, question, solution, knowledge_ids


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    tex = TEX.read_text(encoding="utf-8")

    exercise_records = []
    for exercise, question, solution, knowledge_ids in extract_exercise_blocks(tex):
        section = ".".join(exercise.split(".")[:2])
        meta = SECTION_METHODS[section]
        exercise_records.append(
            {
                "id": f"durrett_ch8_exercise_{exercise.replace('.', '_')}",
                "exercise": exercise,
                "chapter": 8,
                "section": section,
                "section_topic": meta["section_topic"],
                "source_tex": str(TEX),
                "source_pdf": str(PDF),
                "question_tex": question,
                "solution_tex": solution,
                "knowledge_used_ids": knowledge_ids,
                "method_summary": meta["method_summary"],
                "method_tags": meta["method_tags"],
                "new_knowledge_ids": meta["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )

    method_cards = []
    for section, meta in SECTION_METHODS.items():
        method_cards.append(
            {
                "id": f"durrett_ch8_section_{section.replace('.', '_')}_method_card",
                "chapter": 8,
                "section": section,
                "title": f"Chapter {section} exercise method card",
                "section_topic": meta["section_topic"],
                "method_summary": meta["method_summary"],
                "method_tags": meta["method_tags"],
                "new_knowledge_ids": meta["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )

    write_jsonl(OUT / "chapter8_exercise_records.jsonl", exercise_records)
    write_jsonl(OUT / "chapter8_exercise_method_cards.jsonl", method_cards)
    write_jsonl(OUT / "chapter8_exercise_new_knowledge.jsonl", NEW_KNOWLEDGE)

    flashcards = ["id\tfront\tback\ttags"]
    for item in NEW_KNOWLEDGE:
        flashcards.append(
            f"{item['id']}\t{item['title']}\t{item['summary']} Use case: {item['use_case']}\t{','.join(item['tags'])}"
        )
    (OUT / "chapter8_exercise_method_flashcards.tsv").write_text("\n".join(flashcards) + "\n", encoding="utf-8")

    md = [
        "# Chapter 8 Exercise Viki Dataset",
        "",
        f"Source TeX: `{TEX}`",
        f"Source PDF: `{PDF}`",
        "",
        "This dataset turns the solved Chapter 8 exercises into retrieval-ready records, reusable method cards, and new exercise-derived knowledge pieces.",
        "",
        "## Files",
        "",
        "- `chapter8_exercise_records.jsonl`: one record per solved exercise, including question, solution, viki IDs used, and method tags.",
        "- `chapter8_exercise_method_cards.jsonl`: section-level method summaries.",
        "- `chapter8_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.",
        "- `chapter8_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.",
        "- `chapter8_exercise_viki.md`: human-readable overview.",
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
    (OUT / "chapter8_exercise_viki.md").write_text("\n".join(md), encoding="utf-8")

    existing_manifest_path = OUT / "manifest.json"
    existing_manifest = json.loads(existing_manifest_path.read_text(encoding="utf-8"))
    existing_files = list(existing_manifest.get("files", []))
    exercise_files = [
        "chapter8_exercise_records.jsonl",
        "chapter8_exercise_method_cards.jsonl",
        "chapter8_exercise_new_knowledge.jsonl",
        "chapter8_exercise_method_flashcards.tsv",
        "chapter8_exercise_viki.md",
    ]
    for file_name in exercise_files:
        if file_name not in existing_files:
            existing_files.append(file_name)

    existing_manifest.update(
        {
            "updated_at": CREATED,
            "exercise_record_count": len(exercise_records),
            "exercise_method_card_count": len(method_cards),
            "exercise_new_knowledge_count": len(NEW_KNOWLEDGE),
            "source_exercise_tex": str(TEX),
            "source_exercise_pdf": str(PDF),
            "files": existing_files,
        }
    )
    existing_manifest_path.write_text(json.dumps(existing_manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps(existing_manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEX = ROOT / "Probability/Exercises/Chapter5/Chapter5Exercises.tex"
PDF = ROOT / "Probability/Exercises/Chapter5/Chapter5Exercises.pdf"
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter5_Knowledge"
CREATED = datetime.now(timezone.utc).isoformat()


SECTION_METHODS = {
    "5.1": {
        "section_topic": "Markov-chain examples and transition kernels",
        "method_summary": "Identify the state variable that makes the future depend only on the present; compute transition probabilities by conditioning on the next independent draw, offspring, ball swap, or allele sample.",
        "method_tags": ["markov-property", "transition-kernel", "example-models", "state-choice"],
        "new_knowledge_ids": [
            "exercise_ch5_state_sufficiency_test",
            "exercise_ch5_transition_from_one_step_mechanism",
            "exercise_ch5_hidden_parameter_predictive_markov",
            "exercise_ch5_mendelian_pair_transition",
        ],
    },
    "5.2": {
        "section_topic": "Markov property, stopping, hitting, exit, and martingale equations",
        "method_summary": "Use conditional independence from the Markov property, decompose at first hitting times, and solve finite exit or expected-time problems through harmonic and Poisson equations.",
        "method_tags": ["strong-markov", "hitting-time", "harmonic-equation", "martingale"],
        "new_knowledge_ids": [
            "exercise_ch5_conditional_independence_past_future",
            "exercise_ch5_first_entrance_decomposition",
            "exercise_ch5_exit_probability_dirichlet_problem",
            "exercise_ch5_expected_hitting_time_poisson_equation",
            "exercise_ch5_absorption_probability_martingale",
        ],
    },
    "5.3": {
        "section_topic": "Recurrence, transience, birth-death tests, and Lyapunov criteria",
        "method_summary": "Classify recurrence through return sums, finite closed classes, scale functions, and Foster-Lyapunov supermartingales; use asymptotic product tests for birth-death boundaries.",
        "method_tags": ["recurrence", "transience", "birth-death", "lyapunov", "scale-function"],
        "new_knowledge_ids": [
            "exercise_ch5_excursion_iid_cycles",
            "exercise_ch5_birth_death_log_product_test",
            "exercise_ch5_lyapunov_to_zero_transience",
            "exercise_ch5_power_lyapunov_birth_death",
            "exercise_ch5_superharmonic_liouville_chain",
        ],
    },
    "5.4": {
        "section_topic": "Random-walk recurrence and harmonic-function consequences",
        "method_summary": "Use ladder variables, recurrence alternatives, and random-walk visits to convert path behavior into Liouville theorems for superharmonic or bounded harmonic functions.",
        "method_tags": ["random-walk", "ladder-variables", "liouville", "harmonic-functions"],
        "new_knowledge_ids": [
            "exercise_ch5_one_dimensional_random_walk_alternatives",
            "exercise_ch5_ladder_epoch_geometric_regeneration",
            "exercise_ch5_recurrent_walk_superharmonic_liouville",
            "exercise_ch5_bounded_harmonic_tail_zero_one",
        ],
    },
    "5.5": {
        "section_topic": "Stationary measures, reversibility, cycle formula, and positive recurrence",
        "method_summary": "Find invariant laws using detailed balance, cycle occupation measures, return-time identities, and drift/regeneration arguments for queues.",
        "method_tags": ["stationary-distribution", "detailed-balance", "cycle-trick", "positive-recurrence"],
        "new_knowledge_ids": [
            "exercise_ch5_hypergeometric_detailed_balance",
            "exercise_ch5_cycle_measure_hitting_ratio",
            "exercise_ch5_stationary_measure_uniqueness_scaling",
            "exercise_ch5_poisson_thinning_stationarity",
            "exercise_ch5_reflected_walk_idle_fraction",
        ],
    },
    "5.6": {
        "section_topic": "Convergence to stationarity, coupling rates, and regenerative limit theorems",
        "method_summary": "Prove convergence by coupling, obtain finite-state exponential rates through uniform block coupling, and use regenerative cycles for additive LLNs, CLTs, and ratio limits.",
        "method_tags": ["coupling", "ergodic-theorem", "regeneration", "ratio-limit", "clt"],
        "new_knowledge_ids": [
            "exercise_ch5_two_state_affine_recursion",
            "exercise_ch5_finite_aperiodic_uniform_power",
            "exercise_ch5_block_coupling_exponential_rate",
            "exercise_ch5_regenerative_additive_functional_lln",
            "exercise_ch5_regenerative_additive_functional_clt",
            "exercise_ch5_recurrent_ratio_limit_cycles",
        ],
    },
    "5.8": {
        "section_topic": "Harris chains, split-chain atoms, GI/G/1 queues, and continuous-state recurrence",
        "method_summary": "Reduce Harris-chain questions to the split-chain atom, transfer countable-state return and stationary-measure arguments, and analyze reflected random walks by drift and path reversal.",
        "method_tags": ["harris-chain", "split-chain", "atom", "gig1", "reflected-random-walk"],
        "new_knowledge_ids": [
            "exercise_ch5_split_atom_return_sum",
            "exercise_ch5_harris_stationarity_implies_recurrence",
            "exercise_ch5_harris_small_set_choice_invariance",
            "exercise_ch5_gig1_drift_classification",
            "exercise_ch5_reflection_maximum_representation",
            "exercise_ch5_multiplicative_ou_log_recursion",
        ],
    },
}


NEW_KNOWLEDGE = [
    {
        "id": "exercise_ch5_state_sufficiency_test",
        "title": "State sufficiency test for the Markov property",
        "kind": "diagnostic-template",
        "summary": "A proposed process is Markov only if the retained state contains all information needed to compute the next-step law; record maxima fail when the current walk location is omitted.",
        "use_case": "Exercises 5.1.1, 5.1.2, 5.1.3, and other state-selection problems.",
        "tags": ["markov-property", "state-choice", "counterexample"],
    },
    {
        "id": "exercise_ch5_transition_from_one_step_mechanism",
        "title": "Compute transitions from the one-step mechanism",
        "kind": "calculation-template",
        "summary": "Given the present state, enumerate the next independent draw, swap, birth, or arrival and translate the possible outcomes into transition probabilities.",
        "use_case": "Coupon, pair-chain, Bernoulli-Laplace, Wright-Fisher, and queue transition computations.",
        "tags": ["transition-matrix", "conditioning", "examples"],
    },
    {
        "id": "exercise_ch5_hidden_parameter_predictive_markov",
        "title": "Bayesian predictive state for hidden-parameter chains",
        "kind": "calculation-template",
        "summary": "When a hidden parameter is shared across trials, update its posterior from a sufficient statistic and use the posterior mean as the next-step predictive probability.",
        "use_case": "Exercise 5.1.6 and temporally inhomogeneous Markov chains from exchangeable coin flips.",
        "tags": ["bayesian-update", "sufficient-statistic", "inhomogeneous-markov"],
    },
    {
        "id": "exercise_ch5_mendelian_pair_transition",
        "title": "Mendelian pair transition matrix",
        "kind": "calculation-template",
        "summary": "For unordered genotype-pair states, compute one-offspring genotype probabilities (p,q,r) and map two independent offspring to probabilities p^2, 2pq, 2pr, q^2, 2qr, r^2.",
        "use_case": "Brother-sister mating transition and absorption computations.",
        "tags": ["genetics", "transition-matrix", "mendelian"],
    },
    {
        "id": "exercise_ch5_conditional_independence_past_future",
        "title": "Past and future conditional independence",
        "kind": "proof-template",
        "summary": "For A in the past and B in the future, condition first on the present sigma-field; the Markov property turns E(1_B|F_n) into a function of X_n.",
        "use_case": "Exercise 5.2.1 and conditional independence arguments.",
        "tags": ["markov-property", "conditional-independence", "tower-property"],
    },
    {
        "id": "exercise_ch5_first_entrance_decomposition",
        "title": "First entrance decomposition",
        "kind": "proof-template",
        "summary": "Partition {X_n=y} by the first positive hitting time T_y=m, then restart from y by the strong Markov property to get p^n(x,y)=sum_m P_x(T_y=m)p^{n-m}(y,y).",
        "use_case": "Exercise 5.2.4 and renewal decompositions for Markov chains.",
        "tags": ["hitting-time", "strong-markov", "decomposition"],
    },
    {
        "id": "exercise_ch5_exit_probability_dirichlet_problem",
        "title": "Exit probabilities solve the Dirichlet problem",
        "kind": "proof-template",
        "summary": "An exit probability h(x)=P_x(V_A<V_B) is harmonic off A union B with boundary values 1 and 0; optional stopping at the exit time proves uniqueness on finite domains.",
        "use_case": "Exercises 5.2.7 and 5.2.8.",
        "tags": ["dirichlet-problem", "harmonic", "optional-stopping"],
    },
    {
        "id": "exercise_ch5_expected_hitting_time_poisson_equation",
        "title": "Expected hitting times solve a Poisson equation",
        "kind": "proof-template",
        "summary": "For g(x)=E_x V_A, first-step analysis gives g=1+Pg off A and g=0 on A; the process g(X_{n∧V_A})+n∧V_A is the uniqueness martingale.",
        "use_case": "Exercises 5.2.11, 5.2.12, and 5.2.13.",
        "tags": ["expected-hitting-time", "poisson-equation", "martingale"],
    },
    {
        "id": "exercise_ch5_absorption_probability_martingale",
        "title": "Absorption probability from martingale value",
        "kind": "calculation-template",
        "summary": "If a bounded martingale is stopped on two absorbing boundary values, the starting value equals the boundary-weighted absorption probability.",
        "use_case": "Exercises 5.2.8, 5.2.9, and 5.2.10.",
        "tags": ["martingale", "absorption", "optional-stopping"],
    },
    {
        "id": "exercise_ch5_excursion_iid_cycles",
        "title": "Iid excursions between recurrent returns",
        "kind": "regeneration-template",
        "summary": "At successive return times to a recurrent state, the strong Markov property makes the interarrival times and path excursions iid.",
        "use_case": "Exercise 5.3.1 and regenerative proofs in Sections 5.5 and 5.6.",
        "tags": ["excursions", "regeneration", "strong-markov"],
    },
    {
        "id": "exercise_ch5_birth_death_log_product_test",
        "title": "Birth-death recurrence by log product asymptotics",
        "kind": "asymptotic-template",
        "summary": "Use log(q_j/p_j) expansions to decide divergence of the birth-death scale sum; for p_j=1/2+C/j the threshold is C=1/4.",
        "use_case": "Exercise 5.3.4 and nearest-neighbor recurrence boundaries.",
        "tags": ["birth-death", "recurrence", "asymptotics"],
    },
    {
        "id": "exercise_ch5_lyapunov_to_zero_transience",
        "title": "Lyapunov function tending to zero proves transience",
        "kind": "criterion",
        "summary": "A positive superharmonic function outside a finite set that tends to zero at infinity contradicts recurrent return to that finite set, hence implies transience in irreducible chains.",
        "use_case": "Exercise 5.3.5 and outward-drift birth-death chains.",
        "tags": ["lyapunov", "transience", "supermartingale"],
    },
    {
        "id": "exercise_ch5_power_lyapunov_birth_death",
        "title": "Power Lyapunov functions for near-critical birth-death chains",
        "kind": "calculation-template",
        "summary": "For p_j-1/2~C/j, Taylor expand E_j X_1^alpha-j^alpha; choosing alpha on the correct side of 1-4C gives recurrence or transience.",
        "use_case": "Exercise 5.3.6.",
        "tags": ["birth-death", "lyapunov", "taylor-expansion"],
    },
    {
        "id": "exercise_ch5_superharmonic_liouville_chain",
        "title": "Recurrent irreducible chains have only constant nonnegative superharmonic functions",
        "kind": "liouville-template",
        "summary": "Stop a nonnegative supermartingale f(X_n) at the hitting time of another state; recurrence forces f(x)>=f(y) and symmetry gives equality.",
        "use_case": "Exercise 5.3.7 and Liouville-type arguments.",
        "tags": ["superharmonic", "recurrence", "liouville"],
    },
    {
        "id": "exercise_ch5_one_dimensional_random_walk_alternatives",
        "title": "Four alternatives for one-dimensional random walks",
        "kind": "classification-template",
        "summary": "Tail zero-one laws and ladder behavior force a one-dimensional random walk to be identically zero, drift to +infinity, drift to -infinity, or oscillate unboundedly both ways.",
        "use_case": "Exercise 5.4.1.",
        "tags": ["random-walk", "zero-one-law", "classification"],
    },
    {
        "id": "exercise_ch5_ladder_epoch_geometric_regeneration",
        "title": "Ascending ladder epochs regenerate record highs",
        "kind": "regeneration-template",
        "summary": "Successive strict ascending ladder epochs repeat the same trial by the strong Markov property; if the first ladder time is defective, only finitely many records occur, otherwise records go to infinity.",
        "use_case": "Exercise 5.4.2.",
        "tags": ["ladder-variables", "records", "random-walk"],
    },
    {
        "id": "exercise_ch5_recurrent_walk_superharmonic_liouville",
        "title": "Recurrent random walk implies nonnegative superharmonic Liouville",
        "kind": "liouville-template",
        "summary": "For recurrent walks in dimensions one and two, f(S_n) is a nonnegative supermartingale and recurrent visits to neighborhoods force all superharmonic values to agree.",
        "use_case": "Exercise 5.4.3.",
        "tags": ["superharmonic", "random-walk", "liouville"],
    },
    {
        "id": "exercise_ch5_bounded_harmonic_tail_zero_one",
        "title": "Bounded harmonic functions via tail zero-one law",
        "kind": "proof-template",
        "summary": "For a bounded harmonic h, h(S_n) is a bounded martingale; its limit is invariant under finite permutations of iid increments, so Hewitt-Savage forces constancy.",
        "use_case": "Exercise 5.4.4.",
        "tags": ["harmonic", "hewitt-savage", "martingale"],
    },
    {
        "id": "exercise_ch5_hypergeometric_detailed_balance",
        "title": "Hypergeometric stationary law for Bernoulli-Laplace",
        "kind": "calculation-template",
        "summary": "The Bernoulli-Laplace diffusion has stationary distribution proportional to binomial choices of black and white balls in the left urn; adjacent detailed balance verifies it.",
        "use_case": "Exercise 5.5.1.",
        "tags": ["bernoulli-laplace", "hypergeometric", "detailed-balance"],
    },
    {
        "id": "exercise_ch5_cycle_measure_hitting_ratio",
        "title": "Cycle occupation measure as a hitting-probability ratio",
        "kind": "formula",
        "summary": "For recurrent x and y in the same class, expected visits to y during one x-cycle equal P_x(T_y<T_x)/P_y(T_x<T_y).",
        "use_case": "Exercise 5.5.2.",
        "tags": ["cycle-trick", "hitting-probability", "stationary-measure"],
    },
    {
        "id": "exercise_ch5_stationary_measure_uniqueness_scaling",
        "title": "Use normalization to compare stationary measures",
        "kind": "proof-template",
        "summary": "In an irreducible recurrent chain, all stationary measures are scalar multiples; evaluate at one state to determine the scalar.",
        "use_case": "Exercises 5.5.3 and 5.5.5.",
        "tags": ["stationary-measure", "uniqueness", "normalization"],
    },
    {
        "id": "exercise_ch5_poisson_thinning_stationarity",
        "title": "Poisson thinning gives M/M/infinity stationarity",
        "kind": "calculation-template",
        "summary": "If X is Poisson(theta), Bernoulli thinning with survival p gives Poisson(p theta), and adding independent Poisson(lambda) arrivals gives Poisson(p theta+lambda).",
        "use_case": "Exercise 5.5.8.",
        "tags": ["poisson", "thinning", "queue"],
    },
    {
        "id": "exercise_ch5_reflected_walk_idle_fraction",
        "title": "Idle fraction from reflected random-walk regulator",
        "kind": "queue-template",
        "summary": "For a stable reflected walk, the regulator increments exactly when the queue is empty and the raw increment is -1; dividing the reflection identity by n gives the long-run idle frequency.",
        "use_case": "Exercise 5.5.7 and M/G/1 stationary mass at zero.",
        "tags": ["reflected-random-walk", "queue", "stationarity"],
    },
    {
        "id": "exercise_ch5_two_state_affine_recursion",
        "title": "Two-state chain convergence via affine recursion",
        "kind": "calculation-template",
        "summary": "Track one coordinate probability q_n; the recursion q_{n+1}=beta+(1-alpha-beta)q_n solves explicitly around its stationary fixed point.",
        "use_case": "Exercise 5.6.1.",
        "tags": ["two-state-chain", "stationary-distribution", "recursion"],
    },
    {
        "id": "exercise_ch5_finite_aperiodic_uniform_power",
        "title": "Finite irreducible aperiodic chains have a positive matrix power",
        "kind": "proof-template",
        "summary": "Use a path from x to y plus sufficiently long return loops at y; finiteness lets one choose a common power m for all pairs.",
        "use_case": "Exercise 5.6.2.",
        "tags": ["finite-chain", "aperiodic", "positive-power"],
    },
    {
        "id": "exercise_ch5_block_coupling_exponential_rate",
        "title": "Uniform block coupling gives exponential convergence",
        "kind": "coupling-template",
        "summary": "If an m-step transition has a uniformly positive chance to send all states to one common state, coupling attempts in independent blocks have geometric tails.",
        "use_case": "Exercise 5.6.3 and finite-state mixing estimates.",
        "tags": ["coupling", "exponential-rate", "finite-chain"],
    },
    {
        "id": "exercise_ch5_regenerative_additive_functional_lln",
        "title": "Regenerative LLN for additive functionals",
        "kind": "limit-template",
        "summary": "Split the path into iid return cycles; reward sums divided by elapsed time converge to expected cycle reward divided by expected cycle length, which equals the stationary average.",
        "use_case": "Exercise 5.6.5.",
        "tags": ["regeneration", "ergodic-theorem", "lln"],
    },
    {
        "id": "exercise_ch5_regenerative_additive_functional_clt",
        "title": "Regenerative CLT for additive functionals",
        "kind": "limit-template",
        "summary": "Apply the iid CLT to centered cycle rewards and random-index by the number of completed cycles; show incomplete-cycle rewards are negligible on sqrt(n) scale.",
        "use_case": "Exercise 5.6.6.",
        "tags": ["regeneration", "clt", "random-index"],
    },
    {
        "id": "exercise_ch5_recurrent_ratio_limit_cycles",
        "title": "Ratio limits from recurrent cycles",
        "kind": "limit-template",
        "summary": "Count visits to z per completed y-cycle and divide by visits to y; the strong law gives the stationary-measure ratio m(z)/m(y).",
        "use_case": "Exercises 5.6.7 and 5.6.8.",
        "tags": ["ratio-limit", "recurrent-chain", "cycle-measure"],
    },
    {
        "id": "exercise_ch5_split_atom_return_sum",
        "title": "Split-chain recurrence is return-sum divergence at the atom",
        "kind": "criterion",
        "summary": "For the artificial atom alpha, the countable-state return criterion applies: recurrence is equivalent to divergence of sum_n pbar^n(alpha,alpha).",
        "use_case": "Exercise 5.8.1.",
        "tags": ["harris-chain", "split-chain", "recurrence"],
    },
    {
        "id": "exercise_ch5_harris_stationarity_implies_recurrence",
        "title": "Stationary distribution forces Harris recurrence",
        "kind": "proof-template",
        "summary": "Lift a stationary distribution to the split chain; positive stationary mass at alpha forces an infinite expected number of alpha visits, hence recurrence.",
        "use_case": "Exercise 5.8.3.",
        "tags": ["harris-chain", "stationarity", "recurrence"],
    },
    {
        "id": "exercise_ch5_harris_small_set_choice_invariance",
        "title": "Harris recurrence does not depend on the small-set pair",
        "kind": "proof-template",
        "summary": "If another Harris set A' is reachable, it has positive lambda measure for the original split chain; Theorem 5.8.8 makes visits to A' occur infinitely often.",
        "use_case": "Exercise 5.8.4.",
        "tags": ["harris-chain", "small-set", "invariance"],
    },
    {
        "id": "exercise_ch5_gig1_drift_classification",
        "title": "GI/G/1 drift classification",
        "kind": "queue-template",
        "summary": "Compare the reflected workload with the raw random walk until the first negative passage: positive drift gives transience, nonpositive drift gives recurrence, negative drift gives positive recurrence.",
        "use_case": "Exercise 5.8.5.",
        "tags": ["gig1", "queue", "drift"],
    },
    {
        "id": "exercise_ch5_reflection_maximum_representation",
        "title": "Reflected random walk equals reversed maximum in law",
        "kind": "identity-template",
        "summary": "The reflected workload satisfies W_n=S_n-min_{j<=n}S_j, which by reversing increments has the same law as the maximum of a length-n random walk.",
        "use_case": "Exercise 5.8.6.",
        "tags": ["reflected-random-walk", "path-reversal", "maximum"],
    },
    {
        "id": "exercise_ch5_multiplicative_ou_log_recursion",
        "title": "Multiplicative variance O.U. becomes stable on log scale",
        "kind": "classification-template",
        "summary": "For Y_{n+1}=beta sqrt(|Y_n|) Z_{n+1}, log|Y_n| follows an AR(1) recursion with coefficient 1/2, yielding a nonzero positive recurrent Harris class plus an absorbing zero.",
        "use_case": "Exercise 5.8.7.",
        "tags": ["ornstein-uhlenbeck", "log-recursion", "harris-chain"],
    },
]


def section_key(exercise: str) -> str:
    return ".".join(exercise.split(".")[:2])


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
        knowledge_used_ids = re.findall(r"durrett_ch\d+_[A-Za-z0-9_]+", knowledge_tex)
        sec = section_key(exercise)
        meta = SECTION_METHODS.get(sec, {})
        new_knowledge_ids = meta.get("new_knowledge_ids", [])
        records.append(
            {
                "id": f"durrett_ch5_exercise_{exercise.replace('.', '_')}",
                "exercise": exercise,
                "chapter": 5,
                "section": sec,
                "section_topic": meta.get("section_topic"),
                "source_tex": str(TEX),
                "source_pdf": str(PDF),
                "question_tex": question,
                "solution_tex": solution,
                "knowledge_used_text": "; ".join(knowledge_used_ids + new_knowledge_ids),
                "knowledge_used_ids": knowledge_used_ids + new_knowledge_ids,
                "textbook_knowledge_used_ids": knowledge_used_ids,
                "method_summary": meta.get("method_summary"),
                "method_tags": meta.get("method_tags", []),
                "new_knowledge_ids": new_knowledge_ids,
                "created_at": CREATED,
            }
        )
    return records


def write_jsonl(path: Path, rows):
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def update_manifest(exercise_records, method_cards):
    manifest_path = OUT / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    else:
        manifest = {
            "name": "durrett_chapter5_markov_chains_llm_viki",
            "description": "Curated LLM/Viki-style knowledge pieces for Chapter 5 of Durrett Probability: Theory and Examples.",
            "files": [],
        }

    exercise_files = [
        "chapter5_exercise_records.jsonl",
        "chapter5_exercise_method_cards.jsonl",
        "chapter5_exercise_new_knowledge.jsonl",
        "chapter5_exercise_method_flashcards.tsv",
        "chapter5_exercise_viki.md",
    ]
    files = manifest.get("files", [])
    for file_name in exercise_files:
        if file_name not in files:
            files.append(file_name)
    manifest["files"] = files
    manifest["exercise_source_tex"] = str(TEX)
    manifest["exercise_source_pdf"] = str(PDF)
    manifest["exercise_record_count"] = len(exercise_records)
    manifest["exercise_method_card_count"] = len(method_cards)
    manifest["exercise_new_knowledge_count"] = len(NEW_KNOWLEDGE)
    manifest["exercise_viki_created_at"] = CREATED
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


def main():
    tex = TEX.read_text(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)

    exercise_records = parse_exercises(tex)
    method_cards = []
    for sec, meta in SECTION_METHODS.items():
        method_cards.append(
            {
                "id": f"durrett_ch5_section_{sec.replace('.', '_')}_method_card",
                "chapter": 5,
                "section": sec,
                "title": f"Chapter {sec} exercise method card",
                "section_topic": meta["section_topic"],
                "method_summary": meta["method_summary"],
                "method_tags": meta["method_tags"],
                "new_knowledge_ids": meta["new_knowledge_ids"],
                "created_at": CREATED,
            }
        )

    write_jsonl(OUT / "chapter5_exercise_records.jsonl", exercise_records)
    write_jsonl(OUT / "chapter5_exercise_method_cards.jsonl", method_cards)
    write_jsonl(OUT / "chapter5_exercise_new_knowledge.jsonl", NEW_KNOWLEDGE)

    flashcards = ["id\tfront\tback\ttags"]
    for item in NEW_KNOWLEDGE:
        flashcards.append(
            f"{item['id']}\t{item['title']}\t{item['summary']} Use case: {item['use_case']}\t{','.join(item['tags'])}"
        )
    (OUT / "chapter5_exercise_method_flashcards.tsv").write_text("\n".join(flashcards) + "\n", encoding="utf-8")

    md = [
        "# Chapter 5 Exercise Viki Dataset",
        "",
        f"Source TeX: `{TEX}`",
        f"Source PDF: `{PDF}`",
        "",
        "This dataset turns the solved Chapter 5 exercises into retrieval-ready records, reusable method cards, and exercise-derived knowledge pieces.",
        "",
        "Solved sections currently included: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, and 5.8.",
        "",
        "## Files",
        "",
        "- `chapter5_exercise_records.jsonl`: one record per solved exercise, including question, solution, Viki IDs used, and method tags.",
        "- `chapter5_exercise_method_cards.jsonl`: section-level method summaries.",
        "- `chapter5_exercise_new_knowledge.jsonl`: reusable proof/calculation/classification patterns extracted from the exercises.",
        "- `chapter5_exercise_method_flashcards.tsv`: flashcard import file for the new method cards.",
        "- `chapter5_exercise_viki.md`: human-readable overview.",
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
    (OUT / "chapter5_exercise_viki.md").write_text("\n".join(md), encoding="utf-8")

    manifest = update_manifest(exercise_records, method_cards)
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

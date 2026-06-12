from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter4_Knowledge"
SOURCE_TEX = ROOT / "Probability/Exercises/Chapter4/Chapter4Exercises.tex"
SOURCE_PDF = ROOT / "Probability/Exercises/Chapter4/Chapter4Exercises.pdf"

CREATED = datetime.now(timezone.utc).isoformat()


SECTION_TOPICS = {
    "4.1": "Conditional expectation, conditioning identities, and L2 projection",
    "4.2": "Martingales, submartingales, supermartingales, transforms, and upcrossings",
    "4.3": "Examples of martingales, likelihood-ratio martingales, and branching processes",
    "4.4": "Doob inequalities, optional sampling, maximal bounds, and martingale SLLN",
    "4.6": "Uniform integrability, Levy theorems, posterior limits, and martingale convergence",
    "4.7": "Backward martingales, exchangeability, and U-statistic limits",
    "4.8": "Optional stopping applications, Wald identities, random walks, and ruin estimates",
    "4.9": "Renewal equations and generating functions for random-walk return times",
}


METHOD_CARDS = [
    {
        "section": "4.1",
        "method_summary": "Compute conditional expectations by testing against the conditioning sigma-field, then use projection, Jensen, conditioning on partitions, and variance decomposition to simplify identities.",
        "method_tags": ["conditional-expectation", "projection", "jensen", "variance-decomposition"],
        "new_knowledge_ids": [
            "exercise_ch4_conditional_bayes_by_indicator",
            "exercise_ch4_conditional_inequality_from_pointwise_bound",
            "exercise_ch4_l2_projection_pythagorean_conditioning",
            "exercise_ch4_total_variance_random_sum",
            "exercise_ch4_distribution_preserving_conditional_expectation",
        ],
    },
    {
        "section": "4.2",
        "method_summary": "Check martingale type by conditioning one step ahead; use predictable transforms, stopped processes, upcrossing counts, and product decompositions to prove convergence or construct examples.",
        "method_tags": ["martingale", "predictable-transform", "stopping", "upcrossing", "convergence"],
        "new_knowledge_ids": [
            "exercise_ch4_natural_filtration_martingale_reduction",
            "exercise_ch4_deterministic_submartingale_square_supermartingale",
            "exercise_ch4_stopped_upcrossing_localization",
            "exercise_ch4_product_martingale_limit_zero",
            "exercise_ch4_dubins_upcrossing_switching",
        ],
    },
    {
        "section": "4.3",
        "method_summary": "Use concrete martingale examples to isolate hypotheses: likelihood-ratio processes give martingales, additive error bounds give convergence, and branching recursions reduce to fixed-point equations.",
        "method_tags": ["examples", "likelihood-ratio", "radon-nikodym", "branching-process", "counterexample"],
        "new_knowledge_ids": [
            "exercise_ch4_bounded_increment_nonmartingale_counterexample",
            "exercise_ch4_additive_error_supermartingale_convergence",
            "exercise_ch4_partition_rn_derivative_martingale",
            "exercise_ch4_bernoulli_product_hellinger_criterion",
            "exercise_ch4_branching_fixed_point_extinction",
        ],
    },
    {
        "section": "4.4",
        "method_summary": "Apply optional sampling and Doob inequalities to stopped martingales; combine orthogonal increments, quadratic martingales, and Kronecker normalization for L2 and strong-law estimates.",
        "method_tags": ["doob-inequality", "optional-sampling", "quadratic-martingale", "orthogonal-increments", "strong-law"],
        "new_knowledge_ids": [
            "exercise_ch4_optional_sampling_between_stopping_times",
            "exercise_ch4_doob_l1_log_maximal_bound",
            "exercise_ch4_stopped_quadratic_martingale_exit_bound",
            "exercise_ch4_martingale_increment_orthogonality_sum",
            "exercise_ch4_kronecker_martingale_normalization",
        ],
    },
    {
        "section": "4.6",
        "method_summary": "Recognize when convergence is upgraded by uniform integrability; use Levy upward and zero-one laws to turn conditioning on growing sigma-fields into posterior consistency or absorbing-state conclusions.",
        "method_tags": ["uniform-integrability", "levy-upward", "zero-one-law", "posterior-consistency", "bounded-martingale"],
        "new_knowledge_ids": [
            "exercise_ch4_posterior_consistency_by_levy_upward",
            "exercise_ch4_dyadic_conditional_expectation_approximation",
            "exercise_ch4_levy_zero_one_absorption_or_escape",
            "exercise_ch4_bounded_martingale_binary_limit",
        ],
    },
    {
        "section": "4.7",
        "method_summary": "Use backward martingale convergence for tail-like sigma-fields, then exploit exchangeability to replace conditional laws by finite-population hypergeometric formulas.",
        "method_tags": ["backward-martingale", "exchangeability", "hypergeometric", "u-statistic", "covariance"],
        "new_knowledge_ids": [
            "exercise_ch4_backward_lp_convergence_ui",
            "exercise_ch4_backward_conditional_dct",
            "exercise_ch4_exchangeable_hypergeometric_conditioning",
            "exercise_ch4_exchangeable_pair_covariance_positive",
            "exercise_ch4_u_statistic_pair_square_limit",
        ],
    },
    {
        "section": "4.8",
        "method_summary": "Choose a martingale matched to the target functional, stop it at bounded levels, justify optional stopping, and pass limits to obtain hitting probabilities, Wald identities, and ruin bounds.",
        "method_tags": ["optional-stopping", "random-walk", "wald-identity", "gambler-ruin", "exponential-martingale"],
        "new_knowledge_ids": [
            "exercise_ch4_optional_stopping_ui_conditional_form",
            "exercise_ch4_supermartingale_maximal_bound",
            "exercise_ch4_wald_second_equation_stopped_l2",
            "exercise_ch4_gambler_ruin_variance_generation",
            "exercise_ch4_exponential_martingale_ruin_adjustment",
            "exercise_ch4_fourth_moment_exit_time",
        ],
    },
    {
        "section": "4.9",
        "method_summary": "Encode first-return decompositions as renewal equations and solve them with generating functions; singular behavior at one reveals recurrence and return-time means.",
        "method_tags": ["renewal-equation", "generating-functions", "return-time", "random-walk"],
        "new_knowledge_ids": [
            "exercise_ch4_return_time_renewal_generating_function",
        ],
    },
]


NEW_KNOWLEDGE = [
    {
        "id": "exercise_ch4_conditional_bayes_by_indicator",
        "title": "Conditional Bayes rule from indicator tests",
        "kind": "calculation-template",
        "summary": "To identify E[X | H] on a partition or sub-sigma-field, multiply by indicators of conditioning events and match integrals.",
        "use_case": "Section 4.1 exercises involving conditional probabilities, finite partitions, and conditional densities.",
        "tags": ["conditional-expectation", "indicator-test", "bayes"],
    },
    {
        "id": "exercise_ch4_conditional_inequality_from_pointwise_bound",
        "title": "Transfer pointwise inequalities through conditioning",
        "kind": "proof-template",
        "summary": "If an inequality holds after multiplying by every nonnegative H-measurable test function, it holds for the conditional expectations.",
        "use_case": "Conditional Jensen, conditional Markov bounds, and monotonicity arguments in Section 4.1.",
        "tags": ["conditional-expectation", "inequality", "test-functions"],
    },
    {
        "id": "exercise_ch4_l2_projection_pythagorean_conditioning",
        "title": "L2 projection Pythagorean identity for conditioning",
        "kind": "proof-template",
        "summary": "Use E[(X-E[X|H])Z]=0 for H-measurable Z to split squared errors and prove best-approximation identities.",
        "use_case": "Projection and regression-style conditional expectation exercises.",
        "tags": ["l2-projection", "orthogonality", "conditional-expectation"],
    },
    {
        "id": "exercise_ch4_total_variance_random_sum",
        "title": "Random-sum variance by conditioning on the count",
        "kind": "calculation-template",
        "summary": "Condition on N to compute E[S_N | N] and Var(S_N | N), then add conditional variance plus variance of the conditional mean.",
        "use_case": "Random sums and total-variance exercises in Section 4.1.",
        "tags": ["random-sum", "total-variance", "conditioning"],
    },
    {
        "id": "exercise_ch4_distribution_preserving_conditional_expectation",
        "title": "Conditional expectation can preserve distribution only under rigidity",
        "kind": "warning",
        "summary": "If E[X|H] has the same distribution as X and Jensen is tight for a strictly convex function, then X must already be H-measurable.",
        "use_case": "Exercises where conditioning appears not to reduce randomness.",
        "tags": ["jensen", "rigidity", "conditional-expectation"],
    },
    {
        "id": "exercise_ch4_natural_filtration_martingale_reduction",
        "title": "One-step martingale check in the natural filtration",
        "kind": "proof-template",
        "summary": "For processes built from independent increments, reduce E[X_{n+1}|F_n] to a deterministic function of the current state and one new increment.",
        "use_case": "Section 4.2 martingale, submartingale, and supermartingale verification.",
        "tags": ["martingale", "natural-filtration", "independent-increments"],
    },
    {
        "id": "exercise_ch4_deterministic_submartingale_square_supermartingale",
        "title": "Deterministic martingale-type checks reduce to monotonicity",
        "kind": "calculation-template",
        "summary": "A deterministic adapted process is a submartingale or supermartingale exactly when the underlying sequence is monotone in the corresponding direction.",
        "use_case": "Exercises testing definitions on simple deterministic examples.",
        "tags": ["submartingale", "supermartingale", "deterministic-process"],
    },
    {
        "id": "exercise_ch4_stopped_upcrossing_localization",
        "title": "Localize upcrossing arguments by stopping at bounded levels",
        "kind": "proof-template",
        "summary": "Stop a process before it leaves a bounded range so optional inequalities apply, then let the stopping level increase.",
        "use_case": "Upcrossing and convergence exercises where integrability or boundedness needs to be restored.",
        "tags": ["upcrossing", "stopping", "localization"],
    },
    {
        "id": "exercise_ch4_product_martingale_limit_zero",
        "title": "Product martingales may converge to zero by logarithms",
        "kind": "calculation-template",
        "summary": "For products of independent mean-one factors, examine log factors; a negative accumulated log drift can force almost-sure convergence to zero.",
        "use_case": "Multiplicative martingales and examples where mean is not preserved at the limit.",
        "tags": ["product-martingale", "log-transform", "almost-sure-limit"],
    },
    {
        "id": "exercise_ch4_dubins_upcrossing_switching",
        "title": "Dubins-style switching creates many upcrossings",
        "kind": "construction-template",
        "summary": "Alternate between betting strategies active below one level and above another to convert repeated upcrossings into predictable-transform gains.",
        "use_case": "Exercises connecting upcrossing inequalities with gambling interpretations.",
        "tags": ["upcrossing", "predictable-transform", "gambling"],
    },
    {
        "id": "exercise_ch4_bounded_increment_nonmartingale_counterexample",
        "title": "Bounded increments alone do not make a martingale",
        "kind": "counterexample-template",
        "summary": "Construct an adapted process with bounded steps but nonzero conditional drift to show martingale conclusions need a true drift condition.",
        "use_case": "Section 4.3 exercises checking the exact hypotheses of martingale theorems.",
        "tags": ["counterexample", "bounded-increments", "conditional-drift"],
    },
    {
        "id": "exercise_ch4_additive_error_supermartingale_convergence",
        "title": "Summable additive errors preserve convergence",
        "kind": "proof-template",
        "summary": "Add the tail sum of the error sequence to a near-supermartingale to obtain a genuine supermartingale with the same limiting behavior.",
        "use_case": "Almost-supermartingale convergence arguments.",
        "tags": ["supermartingale", "summable-errors", "convergence"],
    },
    {
        "id": "exercise_ch4_partition_rn_derivative_martingale",
        "title": "Partition likelihood ratios form martingales",
        "kind": "calculation-template",
        "summary": "On a refining finite partition, the ratio Q(A)/P(A) on the cell containing omega is the conditional expectation of dQ/dP.",
        "use_case": "Radon-Nikodym and likelihood-ratio martingale exercises.",
        "tags": ["radon-nikodym", "likelihood-ratio", "partition"],
    },
    {
        "id": "exercise_ch4_bernoulli_product_hellinger_criterion",
        "title": "Bernoulli product likelihood ratios and Hellinger sums",
        "kind": "criterion",
        "summary": "For product Bernoulli laws, square-root likelihood overlaps factor, and convergence or singularity is controlled by a summable squared parameter distance.",
        "use_case": "Exercises comparing infinite product measures.",
        "tags": ["bernoulli-product", "hellinger", "absolute-continuity"],
    },
    {
        "id": "exercise_ch4_branching_fixed_point_extinction",
        "title": "Branching extinction probabilities are fixed points",
        "kind": "calculation-template",
        "summary": "Condition on the first generation to get q = f(q), where f is the offspring generating function; choose the minimal fixed point in [0,1].",
        "use_case": "Branching-process extinction and survival exercises.",
        "tags": ["branching-process", "generating-function", "fixed-point"],
    },
    {
        "id": "exercise_ch4_optional_sampling_between_stopping_times",
        "title": "Optional sampling between two stopping times",
        "kind": "proof-template",
        "summary": "Apply optional sampling to stopped processes at bounded approximations of S and T, then pass to limits using the available integrability control.",
        "use_case": "Section 4.4 exercises with E[M_T | F_S] and S <= T.",
        "tags": ["optional-sampling", "stopping-times", "conditioning"],
    },
    {
        "id": "exercise_ch4_doob_l1_log_maximal_bound",
        "title": "Doob L1 logarithmic maximal bound",
        "kind": "inequality-template",
        "summary": "Integrate the weak L1 maximal inequality over levels and split at a scale where the integral of min(1, X/lambda) is finite.",
        "use_case": "Maximal estimates for nonnegative submartingales without Lp control for p>1.",
        "tags": ["doob-inequality", "maximal-bound", "logarithmic-moment"],
    },
    {
        "id": "exercise_ch4_stopped_quadratic_martingale_exit_bound",
        "title": "Quadratic martingale exit bounds",
        "kind": "calculation-template",
        "summary": "For a martingale with controlled conditional variances, stop M_n^2 minus accumulated variance at the exit time and compare with the boundary size.",
        "use_case": "Exit probability and maximal L2 exercises.",
        "tags": ["quadratic-martingale", "exit-time", "variance-bound"],
    },
    {
        "id": "exercise_ch4_martingale_increment_orthogonality_sum",
        "title": "Martingale increments are orthogonal in L2",
        "kind": "proof-template",
        "summary": "For i<j, E[D_iD_j]=E[D_i E[D_j|F_{j-1}]]=0, so variances of martingale sums add.",
        "use_case": "L2 convergence, square-function, and maximal inequality exercises.",
        "tags": ["orthogonality", "martingale-differences", "l2"],
    },
    {
        "id": "exercise_ch4_kronecker_martingale_normalization",
        "title": "Kronecker normalization for martingale sums",
        "kind": "proof-template",
        "summary": "Show a weighted martingale series converges in L2 or a.s., then apply Kronecker's lemma to get normalized partial-sum convergence.",
        "use_case": "Martingale strong laws and weighted-average exercises.",
        "tags": ["kronecker-lemma", "strong-law", "martingale-series"],
    },
    {
        "id": "exercise_ch4_posterior_consistency_by_levy_upward",
        "title": "Posterior consistency from Levy upward theorem",
        "kind": "proof-template",
        "summary": "Write a posterior probability as E[1_A | F_n]; as observations accumulate and generate A, Levy upward convergence sends it to 1_A.",
        "use_case": "Bayesian consistency and statistical identification exercises.",
        "tags": ["levy-upward", "posterior", "conditional-probability"],
    },
    {
        "id": "exercise_ch4_dyadic_conditional_expectation_approximation",
        "title": "Dyadic conditional expectations approximate the full variable",
        "kind": "construction-template",
        "summary": "Condition on increasingly fine dyadic sigma-fields; the generated sigma-field is the Borel information, so Levy upward gives convergence.",
        "use_case": "Exercises approximating a variable by finite-information conditional expectations.",
        "tags": ["dyadic", "conditional-expectation", "levy-upward"],
    },
    {
        "id": "exercise_ch4_levy_zero_one_absorption_or_escape",
        "title": "Levy zero-one law forces absorption or escape events",
        "kind": "proof-template",
        "summary": "If conditional probabilities of a tail event stay bounded away from the event indicator, Levy's zero-one law gives a contradiction.",
        "use_case": "Random-walk, branching, or Markov-chain exercises with eventual absorption events.",
        "tags": ["levy-zero-one", "tail-event", "absorption"],
    },
    {
        "id": "exercise_ch4_bounded_martingale_binary_limit",
        "title": "Bounded martingales with binary absorbing limits",
        "kind": "proof-template",
        "summary": "A bounded martingale converges a.s.; if the dynamics force every limit to be 0 or 1, the starting value is the probability of limiting at 1.",
        "use_case": "Urn, posterior, and absorbing-state martingale exercises.",
        "tags": ["bounded-martingale", "absorbing-state", "limit"],
    },
    {
        "id": "exercise_ch4_backward_lp_convergence_ui",
        "title": "Backward martingale Lp convergence by uniform integrability",
        "kind": "proof-template",
        "summary": "For p>1, boundedness in Lp gives uniform integrability, so backward martingale convergence improves to L1 and often Lp convergence.",
        "use_case": "Backward conditional expectation exercises in Section 4.7.",
        "tags": ["backward-martingale", "lp", "uniform-integrability"],
    },
    {
        "id": "exercise_ch4_backward_conditional_dct",
        "title": "Pass limits inside backward conditional expectations carefully",
        "kind": "warning",
        "summary": "Use domination or uniform integrability before interchanging conditional expectation limits with ordinary limits.",
        "use_case": "Backward martingale convergence exercises involving approximating functions.",
        "tags": ["conditional-dct", "backward-martingale", "uniform-integrability"],
    },
    {
        "id": "exercise_ch4_exchangeable_hypergeometric_conditioning",
        "title": "Exchangeability turns conditioning into hypergeometric sampling",
        "kind": "calculation-template",
        "summary": "Given the unordered multiset or the total number of successes, exchangeability makes a fixed subcollection have the finite-population hypergeometric law.",
        "use_case": "Exchangeable Bernoulli and finite-sample conditional probability exercises.",
        "tags": ["exchangeability", "hypergeometric", "conditioning"],
    },
    {
        "id": "exercise_ch4_exchangeable_pair_covariance_positive",
        "title": "Exchangeable pair covariance constraints",
        "kind": "calculation-template",
        "summary": "Use Var(sum X_i) >= 0 to derive lower bounds on pair covariances and identify the limiting covariance structure.",
        "use_case": "Exchangeability exercises about correlations and de Finetti-style limits.",
        "tags": ["exchangeability", "covariance", "variance"],
    },
    {
        "id": "exercise_ch4_u_statistic_pair_square_limit",
        "title": "U-statistic square limits by pair classification",
        "kind": "calculation-template",
        "summary": "Expand the square of the U-statistic and classify pairs by overlap pattern; only non-negligible classes contribute in the limit.",
        "use_case": "U-statistic convergence exercises under exchangeability or iid assumptions.",
        "tags": ["u-statistic", "second-moment", "pair-counting"],
    },
    {
        "id": "exercise_ch4_optional_stopping_ui_conditional_form",
        "title": "Optional stopping with a conditional target",
        "kind": "proof-template",
        "summary": "Stop at T wedge n, prove uniform integrability or boundedness, and pass to E[M_T | F_S]=M_S.",
        "use_case": "Random-walk and stopping-time exercises with conditional versions of optional stopping.",
        "tags": ["optional-stopping", "uniform-integrability", "conditioning"],
    },
    {
        "id": "exercise_ch4_supermartingale_maximal_bound",
        "title": "Maximal bounds for nonnegative supermartingales",
        "kind": "inequality-template",
        "summary": "Stop at the first crossing of a level and use the supermartingale property to bound the crossing probability by the initial mean divided by the level.",
        "use_case": "Ruin, hitting, and overshoot probability estimates.",
        "tags": ["supermartingale", "maximal-bound", "hitting-time"],
    },
    {
        "id": "exercise_ch4_wald_second_equation_stopped_l2",
        "title": "Wald's second equation from a stopped square martingale",
        "kind": "calculation-template",
        "summary": "For centered iid increments, S_n^2 - n sigma^2 is a martingale; optional stopping gives E[S_T^2]=sigma^2 E[T] when justified.",
        "use_case": "Expected duration and variance identities for stopped random walks.",
        "tags": ["wald-identity", "square-martingale", "random-walk"],
    },
    {
        "id": "exercise_ch4_gambler_ruin_variance_generation",
        "title": "Generate gambler's ruin moments from martingales",
        "kind": "calculation-template",
        "summary": "Use S_n, S_n^2-n, and higher polynomial martingales stopped at ruin boundaries to solve for hitting probabilities and time moments.",
        "use_case": "Gambler's ruin expected time and variance exercises.",
        "tags": ["gambler-ruin", "polynomial-martingales", "moments"],
    },
    {
        "id": "exercise_ch4_exponential_martingale_ruin_adjustment",
        "title": "Exponential martingale ruin adjustment",
        "kind": "calculation-template",
        "summary": "Find theta with E exp(theta X)=1, stop exp(theta S_n) at a hitting time, and use boundary values to estimate ruin probabilities.",
        "use_case": "Insurance risk, random-walk ruin, and Lundberg-type inequalities.",
        "tags": ["exponential-martingale", "ruin-probability", "adjustment-coefficient"],
    },
    {
        "id": "exercise_ch4_fourth_moment_exit_time",
        "title": "Fourth-moment martingales bound exit-time moments",
        "kind": "calculation-template",
        "summary": "Construct a polynomial martingale involving S_n^4, S_n^2, and n; stopping it at an exit time produces second-moment bounds for T.",
        "use_case": "Random-walk exit-time variance and higher-moment exercises.",
        "tags": ["fourth-moment", "exit-time", "polynomial-martingale"],
    },
    {
        "id": "exercise_ch4_return_time_renewal_generating_function",
        "title": "Return-time renewal equations via generating functions",
        "kind": "calculation-template",
        "summary": "Decompose visits into first return plus future visits, obtaining U(s)=1/(1-F(s)); analyze F(s) near s=1 to read recurrence and expected return time.",
        "use_case": "Section 4.9 random-walk return-time exercise.",
        "tags": ["renewal-equation", "generating-functions", "return-time"],
    },
]


def clean_tex(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def extract_exercises(tex: str) -> list[dict]:
    exercise_re = re.compile(r"\\section\*\{Exercise (4\.\d+\.\d+)\}")
    matches = list(exercise_re.finditer(tex))
    end_document = tex.find(r"\end{document}")

    records = []
    for idx, match in enumerate(matches):
        exercise = match.group(1)
        section = ".".join(exercise.split(".")[:2])
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else end_document
        block = tex[start:end]

        q_marker = r"\textbf{Question.}"
        s_marker = r"\textbf{Solution.}"
        if q_marker not in block or s_marker not in block:
            continue

        question_part = block.split(q_marker, 1)[1].split(s_marker, 1)[0]
        knowledge_macro_match = re.search(r"\\Knowledge\{(?P<body>.*?)\n\}", question_part, flags=re.S)
        if knowledge_macro_match:
            question = question_part[: knowledge_macro_match.start()]
            macro_body = knowledge_macro_match.group("body")
            knowledge_ids = re.findall(r"\\path\{([^}]*)\}", macro_body)
            knowledge_text = "; ".join(knowledge_ids)
        else:
            question = question_part
            knowledge_ids = []
            knowledge_text = ""

        solution = block.split(s_marker, 1)[1]
        method_card = next(card for card in METHOD_CARDS if card["section"] == section)
        records.append(
            {
                "id": "durrett_ch4_exercise_" + exercise.replace(".", "_"),
                "exercise": exercise,
                "chapter": 4,
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
                "id": f"durrett_ch4_section_{section.replace('.', '_')}_method_card",
                "chapter": 4,
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
    with path.open("w", encoding="utf-8") as handle:
        handle.write("front\tback\ttags\n")
        for card in cards:
            front = f"Chapter {card['section']} method: what is the main exercise strategy?"
            back = card["method_summary"]
            tags = ",".join(["chapter4", card["section"].replace(".", "_")] + card["method_tags"])
            handle.write(f"{front}\t{back}\t{tags}\n")
        for item in knowledge:
            front = item["title"]
            back = f"{item['summary']} Use case: {item['use_case']}"
            tags = ",".join(["chapter4", item["kind"]] + item["tags"])
            handle.write(f"{front}\t{back}\t{tags}\n")


def write_markdown(path: Path, records: list[dict], cards: list[dict], knowledge: list[dict]) -> None:
    counts_by_section: dict[str, int] = {}
    for record in records:
        counts_by_section[record["section"]] = counts_by_section.get(record["section"], 0) + 1

    lines = [
        "# Chapter 4 Exercise Viki Dataset",
        "",
        f"Source TeX: `{SOURCE_TEX}`",
        f"Source PDF: `{SOURCE_PDF}`",
        "",
        "This dataset turns the solved Chapter 4 exercises into retrieval-ready records, reusable method cards, and exercise-derived knowledge pieces.",
        "",
        "## Files",
        "",
        "- `chapter4_exercise_records.jsonl`: one record per solved exercise, including question, solution, knowledge used, and method tags.",
        "- `chapter4_exercise_method_cards.jsonl`: section-level method summaries.",
        "- `chapter4_exercise_new_knowledge.jsonl`: reusable proof/calculation/counterexample patterns extracted from the exercises.",
        "- `chapter4_exercise_method_flashcards.tsv`: flashcard import file for method and new-knowledge cards.",
        "- `chapter4_exercise_viki.md`: human-readable overview.",
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
        "chapter4_exercise_records.jsonl",
        "chapter4_exercise_method_cards.jsonl",
        "chapter4_exercise_new_knowledge.jsonl",
        "chapter4_exercise_method_flashcards.tsv",
        "chapter4_exercise_viki.md",
    ]
    merged_files = list(dict.fromkeys(manifest.get("files", []) + exercise_files))
    manifest.update(
        {
            "exercise_source_tex": str(SOURCE_TEX),
            "exercise_source_pdf": str(SOURCE_PDF),
            "exercise_record_count": len(records),
            "exercise_method_card_count": len(cards),
            "exercise_new_knowledge_count": len(knowledge),
            "exercise_sections": sorted(counts_by_section(records)),
            "exercise_viki_created_at": CREATED,
            "files": merged_files,
        }
    )
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def counts_by_section(records: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for record in records:
        counts[record["section"]] = counts.get(record["section"], 0) + 1
    return counts


def main() -> None:
    tex = SOURCE_TEX.read_text(encoding="utf-8")
    records = extract_exercises(tex)
    cards = method_cards()
    knowledge = NEW_KNOWLEDGE

    write_jsonl(OUT / "chapter4_exercise_records.jsonl", records)
    write_jsonl(OUT / "chapter4_exercise_method_cards.jsonl", cards)
    write_jsonl(OUT / "chapter4_exercise_new_knowledge.jsonl", knowledge)
    write_flashcards(OUT / "chapter4_exercise_method_flashcards.tsv", cards, knowledge)
    write_markdown(OUT / "chapter4_exercise_viki.md", records, cards, knowledge)
    update_manifest(records, cards, knowledge)

    print(f"wrote {len(records)} exercise records")
    print(f"wrote {len(cards)} method cards")
    print(f"wrote {len(knowledge)} new knowledge pieces")


if __name__ == "__main__":
    main()

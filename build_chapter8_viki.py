from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter8_Knowledge"
SOURCE = ROOT / "Probability/Textbook/Chapters/PTE-Chapter8.pdf"

CREATED = datetime.now(timezone.utc).isoformat()


def piece(pid, section, title, kind, summary, proof_idea, exam_use, pitfalls, tags, related=None):
    return {
        "id": f"durrett_ch8_{pid}",
        "source": "Rick Durrett, Probability: Theory and Examples, extracted Chapter 8 PDF",
        "source_file": str(SOURCE),
        "chapter": 8,
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
        "skorokhod_embedding_mean_zero",
        "8.1 Donsker's Theorem",
        "Skorokhod embedding for one mean-zero variable",
        "theorem",
        "If X has mean 0 and finite second moment, then Brownian motion can be stopped at a time T with B_T distributed as X and E T = E X^2.",
        "Represent the law of X as a mixture of two-point mean-zero laws, then use Brownian first exits from intervals (u,v).",
        "Turns random-walk increments into Brownian increments with matching variance, making Brownian path results available for sums.",
        "The random interval used in the construction is external randomness; conditioning is what preserves the stopping-time calculations.",
        ["skorokhod-embedding", "brownian-motion", "stopping-time", "finite-variance"],
    ),
    piece(
        "embedded_random_walk",
        "8.1 Donsker's Theorem",
        "Embedding iid sums in Brownian motion",
        "construction",
        "For iid mean-zero variance-one increments, one can choose increasing stopping times T_n so that S_n has the same finite-dimensional law as B(T_n), with iid gaps T_n-T_{n-1}.",
        "Restart Brownian motion after each stopping time and apply the one-step Skorokhod embedding to each increment.",
        "Useful for proving CLT and invariance principles by comparing S_n to Brownian motion at random times.",
        "The equality is in distribution for the embedded walk, not necessarily pathwise equality with a preexisting walk.",
        ["random-walk", "embedding", "iid", "brownian-scaling"],
        ["durrett_ch8_skorokhod_embedding_mean_zero"],
    ),
    piece(
        "clt_from_embedding",
        "8.1 Donsker's Theorem",
        "Central limit theorem via random times",
        "proof-template",
        "Since S_n/sqrt(n) has the same law as B(T_n)/sqrt(n) and T_n/n converges in probability to 1, S_n/sqrt(n) converges to a standard normal variable.",
        "Use the weak law on the iid stopping-time gaps and Brownian continuity near time 1, then apply converging together.",
        "A clean proof strategy when Brownian embedding is available and finite variance is assumed.",
        "One still needs tight control of B(t) near t=1; T_n/n -> 1 alone is not a distributional identity.",
        ["clt", "brownian-motion", "converging-together", "weak-law"],
        ["durrett_ch8_embedded_random_walk"],
    ),
    piece(
        "donsker_invariance_principle",
        "8.1 Donsker's Theorem",
        "Donsker invariance principle",
        "theorem",
        "The linearly interpolated process S(n t)/sqrt(n), built from iid mean-zero variance-one increments, converges weakly in C[0,1] to standard Brownian motion.",
        "Show the embedded Brownian time change is uniformly close to deterministic time on [0,1], then use uniform continuity of Brownian paths.",
        "This is the main transfer principle from random walks to Brownian motion for maxima, hitting times, occupations, and path functionals.",
        "The topology matters: the statement is process-level weak convergence, not only convergence of each fixed time.",
        ["donsker", "invariance-principle", "functional-clt", "c0-1"],
        ["durrett_ch8_clt_from_embedding"],
    ),
    piece(
        "continuous_functional_transfer",
        "8.1 Donsker's Theorem",
        "Continuous functional transfer from Donsker",
        "theorem",
        "If a functional on C[0,1] is continuous at Brownian paths with probability one, then applying it to the rescaled random walk converges to applying it to Brownian motion.",
        "Combine Donsker's theorem with the continuous mapping theorem, allowing discontinuities on Brownian-null path sets.",
        "The default method for deriving asymptotics of path statistics from random-walk convergence.",
        "Many natural functionals are not everywhere continuous; check Brownian almost-sure continuity rather than ordinary continuity only.",
        ["continuous-mapping", "path-functional", "brownian-motion", "donsker"],
        ["durrett_ch8_donsker_invariance_principle"],
    ),
    piece(
        "maximum_functional",
        "8.1 Donsker's Theorem",
        "Random-walk maximum limit",
        "example-pattern",
        "The normalized maximum max_{m<=n} S_m/sqrt(n) converges to max_{0<=t<=1} B_t, whose tail is 2 P(B_1 >= a).",
        "Apply Donsker to the continuous maximum functional and use the Brownian reflection principle for the distribution.",
        "Recognize maximum and boundary-crossing limits as Brownian supremum problems.",
        "The reflection-principle tail formula is for a nonnegative barrier and Brownian motion starting at 0.",
        ["maximum", "reflection-principle", "brownian-supremum", "random-walk"],
        ["durrett_ch8_continuous_functional_transfer"],
    ),
    piece(
        "last_zero_arcsine",
        "8.1 Donsker's Theorem",
        "Last zero before time n",
        "example-pattern",
        "The last sign-change or zero time of a centered finite-variance walk, divided by n, converges to the Brownian last-zero time, which has the arcsine law.",
        "Show the last-zero functional is continuous at Brownian paths almost surely, then invoke Donsker.",
        "Transfers the arcsine law beyond simple symmetric walks.",
        "The functional is discontinuous at some deterministic paths, so the Brownian null-set condition is the key point.",
        ["arcsine-law", "last-zero", "donsker", "brownian-zero-set"],
        ["durrett_ch8_continuous_functional_transfer"],
    ),
    piece(
        "occupation_time_halfline",
        "8.1 Donsker's Theorem",
        "Occupation time of a half-line",
        "example-pattern",
        "The fraction of times a centered finite-variance walk spends above a sqrt(n) threshold converges to the Brownian occupation time above that threshold.",
        "Apply Donsker to the occupation functional and use that Brownian paths spend zero Lebesgue time at any fixed level.",
        "Use for random-walk occupation proportions and arcsine-type limits.",
        "Discrete-time counts require a small interpolation comparison; do not identify them blindly with continuous occupation time.",
        ["occupation-time", "arcsine-law", "brownian-motion", "invariance-principle"],
        ["durrett_ch8_continuous_functional_transfer"],
    ),
    piece(
        "martingale_sk_embedding",
        "8.2 CLTs for Martingales",
        "Embedding square-integrable martingales",
        "theorem",
        "A square-integrable martingale can be represented in distribution as Brownian motion sampled at increasing stopping times whose conditional expected increments match conditional variances.",
        "Embed each martingale difference conditionally using a Brownian first-exit construction after the previous stopping time.",
        "Provides the Brownian-time-change route to martingale CLTs.",
        "The conditional variance process, not deterministic time, controls the Brownian clock.",
        ["martingale", "skorokhod-embedding", "conditional-variance", "brownian-motion"],
    ),
    piece(
        "martingale_convergence_variance_sum",
        "8.2 CLTs for Martingales",
        "Martingale convergence from finite quadratic variation",
        "theorem",
        "A square-integrable martingale with finite total conditional variance has an almost sure finite limit.",
        "Use L2 boundedness, Doob convergence ideas, and the sum of conditional second moments.",
        "A standard way to separate negligible martingale tails from the main CLT-scale variance.",
        "Finite expected total variance is stronger than merely having bounded increments.",
        ["martingale-convergence", "quadratic-variation", "l2"],
    ),
    piece(
        "martingale_fclt_random_clock",
        "8.2 CLTs for Martingales",
        "Martingale functional CLT by random clock",
        "theorem",
        "For a martingale-difference array, if the embedded Brownian clock converges to deterministic time and large jumps vanish, the interpolated martingale converges to Brownian motion.",
        "Use Skorokhod embedding, control the random time change, and prove the embedded path is close to Brownian motion.",
        "The process-level version of the martingale CLT; use when partial-sum paths rather than only final sums appear.",
        "The theorem needs both variance-clock convergence and a Lindeberg-type no-large-jumps condition.",
        ["martingale-fclt", "random-clock", "lindeberg", "brownian-motion"],
        ["durrett_ch8_martingale_sk_embedding"],
    ),
    piece(
        "martingale_lindeberg_feller",
        "8.2 CLTs for Martingales",
        "Lindeberg-Feller condition for martingales",
        "theorem",
        "A martingale-difference array has a normal limit when its conditional variances converge to 1 and its conditional large-jump contribution vanishes.",
        "Truncate the array, embed the truncated martingale, and show the discarded part is negligible.",
        "High-yield theorem for dependent CLTs where conditional means are zero.",
        "Ordinary variance convergence is not enough; the conditional variance process must stabilize.",
        ["martingale-clt", "lindeberg-condition", "conditional-variance", "triangular-array"],
        ["durrett_ch8_martingale_fclt_random_clock"],
    ),
    piece(
        "martingale_clt_final_form",
        "8.2 CLTs for Martingales",
        "Martingale central limit theorem",
        "theorem",
        "A martingale-difference sequence normalized by its variance has a normal limit under conditional variance convergence and conditional Lindeberg conditions.",
        "Reduce the sequence to a triangular array and apply the martingale Lindeberg-Feller theorem.",
        "Use for sums of dependent variables after decomposing them into martingale differences.",
        "Verify the filtration and conditional mean-zero property before applying the theorem.",
        ["martingale-clt", "normal-limit", "filtration", "conditional-lindeberg"],
        ["durrett_ch8_martingale_lindeberg_feller"],
    ),
    piece(
        "stationary_coboundary_clt",
        "8.3 CLTs for Stationary Sequences",
        "Stationary sequence CLT through martingale approximation",
        "theorem",
        "For an ergodic stationary square-integrable sequence, a CLT can be proved when the partial sums are well approximated by a martingale with stationary differences.",
        "Decompose X_n into a martingale difference plus a small coboundary or negligible remainder, then apply the martingale CLT.",
        "Main strategy for dependent stationary sequences on prelim-style problems.",
        "Ergodicity and square integrability do not by themselves guarantee a CLT; the approximation condition matters.",
        ["stationary-sequence", "martingale-approximation", "ergodic", "clt"],
    ),
    piece(
        "projective_stationary_clt",
        "8.3 CLTs for Stationary Sequences",
        "Projective criterion for stationary CLT",
        "criterion",
        "If conditional projections of future partial sums are summable or suitably controlled, stationary centered sequences satisfy a CLT with variance from the martingale approximation.",
        "Use conditional expectations relative to the natural filtration to build martingale differences and bound the error.",
        "A practical check for dependent sequences where conditioning on the past becomes small.",
        "Do not replace the projective condition by ordinary covariance decay unless a theorem justifies it.",
        ["projective-criterion", "stationary", "conditional-expectation", "clt"],
        ["durrett_ch8_stationary_coboundary_clt"],
    ),
    piece(
        "m_dependent_clt",
        "8.3 CLTs for Stationary Sequences",
        "M-dependent stationary CLT",
        "example-pattern",
        "For a centered stationary M-dependent sequence, the normalized sum has a normal limit with long-run variance sigma^2 = E X_0^2 + 2 sum_{k=1}^M E X_0 X_k.",
        "Group variables into blocks or use the stationary martingale approximation theorem; dependence disappears past lag M.",
        "Fast recognition pattern for finite-range dependence problems.",
        "The limiting variance can be zero; in that case the usual nondegenerate normal limit collapses.",
        ["m-dependent", "stationary", "long-run-variance", "clt"],
        ["durrett_ch8_stationary_coboundary_clt"],
    ),
    piece(
        "markov_chain_poisson_equation_clt",
        "8.3 CLTs for Stationary Sequences",
        "Markov-chain CLT via Poisson equation",
        "example-pattern",
        "For a stationary ergodic Markov chain, additive functionals can satisfy a CLT when f is represented through a solution of a Poisson equation, producing a martingale plus a telescoping error.",
        "Write f = g - P g plus a martingale increment, then show the boundary terms are negligible after sqrt(n) scaling.",
        "Use when a dependent sum is generated by a Markov transition kernel.",
        "Stationarity or a controlled initial distribution is needed; starting far from equilibrium can add transient terms.",
        ["markov-chain", "poisson-equation", "additive-functional", "martingale-approximation"],
        ["durrett_ch8_stationary_coboundary_clt"],
    ),
    piece(
        "moving_average_clt",
        "8.3 CLTs for Stationary Sequences",
        "Moving-average process CLT",
        "example-pattern",
        "Linear moving averages of iid innovations satisfy CLTs under coefficient conditions that make the process square integrable and approximable by finite-dependent truncations.",
        "Approximate the infinite moving average by an M-dependent one and control the L2 error of the remainder.",
        "A standard dependent but explicit model where long-run variance can often be computed.",
        "Absolute or square summability assumptions on coefficients are not cosmetic; they justify truncation and variance formulas.",
        ["moving-average", "linear-process", "m-dependent-approximation", "clt"],
        ["durrett_ch8_m_dependent_clt"],
    ),
    piece(
        "mixing_covariance_inequality",
        "8.3.1 Mixing Properties",
        "Mixing covariance inequality",
        "lemma",
        "Mixing coefficients bound covariances between variables measurable with respect to separated sigma-fields, with Holder exponents controlling integrability.",
        "Approximate indicators and apply Holder-type bounds using the distance between joint and product probabilities.",
        "Converts abstract mixing assumptions into summable covariance or projection bounds for CLTs.",
        "Check the exact mixing coefficient and exponent relation; different texts use different normalizations.",
        ["mixing", "covariance-bound", "holder", "dependence"],
    ),
    piece(
        "strong_mixing_stationary_clt",
        "8.3.1 Mixing Properties",
        "Strong-mixing stationary CLT",
        "theorem",
        "A centered ergodic stationary sequence satisfying suitable moment and summable mixing conditions obeys a CLT with long-run variance given by the covariance series.",
        "Use the mixing covariance inequality to verify the projective or martingale-approximation criterion.",
        "Use for dependent sequences when decay of dependence is given quantitatively.",
        "Moment assumptions and summability rates are paired; weakening one often requires strengthening the other.",
        ["strong-mixing", "stationary-clt", "long-run-variance", "covariance-series"],
        ["durrett_ch8_mixing_covariance_inequality"],
    ),
    piece(
        "glivenko_cantelli_uniform",
        "8.4 Empirical Distributions, Brownian Bridge",
        "Glivenko-Cantelli theorem",
        "theorem",
        "The empirical distribution function F_n converges uniformly almost surely to the true distribution function F.",
        "Reduce to the uniform distribution by the probability integral transform, then control finitely many grid intervals and use monotonicity.",
        "The baseline consistency result for empirical CDFs before studying sqrt(n) fluctuations.",
        "Pointwise LLN is not enough; the theorem gives uniform convergence over all x.",
        ["empirical-distribution", "glivenko-cantelli", "uniform-convergence", "cdf"],
    ),
    piece(
        "empirical_process_bridge",
        "8.4 Empirical Distributions, Brownian Bridge",
        "Empirical process convergence to Brownian bridge",
        "theorem",
        "For uniform samples, sqrt(n)(F_n(t)-t) converges as a process to the Brownian bridge B_t - t B_1.",
        "Represent F_n through uniform order statistics or multinomial increments and apply Donsker with the endpoint pinned.",
        "Foundation for Kolmogorov-Smirnov statistics and distribution-free empirical-process limits.",
        "The limit is a bridge, not free Brownian motion, because the empirical CDF is pinned at 0 and 1.",
        ["empirical-process", "brownian-bridge", "donsker", "uniform-order-statistics"],
    ),
    piece(
        "kolmogorov_smirnov_limit",
        "8.4 Empirical Distributions, Brownian Bridge",
        "Kolmogorov-Smirnov statistic limit",
        "theorem",
        "The statistic D_n = sqrt(n) sup_x |F_n(x)-F(x)| converges to sup_{0<=t<=1} |B_t - t B_1| for continuous F.",
        "Use the probability integral transform and the continuous mapping theorem applied to the empirical process.",
        "Identifies the asymptotic null distribution of the Kolmogorov-Smirnov goodness-of-fit statistic.",
        "Continuity of F gives distribution-free uniformization; atoms require separate handling.",
        ["kolmogorov-smirnov", "brownian-bridge", "empirical-cdf", "supremum"],
        ["durrett_ch8_empirical_process_bridge"],
    ),
    piece(
        "brownian_bridge_conditioning",
        "8.4 Empirical Distributions, Brownian Bridge",
        "Brownian bridge as pinned Brownian motion",
        "construction",
        "The Brownian bridge has the same law as B_t - t B_1 on [0,1], equivalently Brownian motion conditioned to return to 0 at time 1.",
        "Compute Gaussian means and covariances, or use Markov transition densities and conditioning on B_1=0.",
        "Use to compute bridge covariance, Markov transition laws, and empirical-process limits.",
        "Conditioning on an event of probability zero is shorthand for a regular conditional or limiting density argument.",
        ["brownian-bridge", "gaussian-process", "conditioning", "empirical-process"],
        ["durrett_ch8_empirical_process_bridge"],
    ),
    piece(
        "kolmogorov_distribution_method",
        "8.4 Empirical Distributions, Brownian Bridge",
        "Kolmogorov distribution by killed Brownian motion",
        "proof-template",
        "The distribution of sup |Brownian bridge| can be computed from Brownian motion killed on exiting an interval and then pinned at time 1.",
        "Use reflection or eigenfunction expansions for Brownian transition densities with absorbing barriers, then condition to form the bridge.",
        "Useful when an exam asks not just for the KS limit but for its explicit distribution.",
        "Keep straight whether the boundary event is one-sided or two-sided; the formulas differ.",
        ["kolmogorov-distribution", "killed-brownian-motion", "brownian-bridge", "reflection-principle"],
        ["durrett_ch8_kolmogorov_smirnov_limit"],
    ),
    piece(
        "brownian_lil",
        "8.5 Laws of the Iterated Logarithm",
        "Law of the iterated logarithm for Brownian motion",
        "theorem",
        "Brownian motion satisfies limsup_{t->infty} B_t / sqrt(2 t log log t) = 1 almost surely, with the corresponding liminf equal to -1.",
        "Prove upper and lower bounds on a geometric time grid using Gaussian tails, Borel-Cantelli, and control between grid points.",
        "The Brownian template for LILs of partial sums after embedding or invariance principles.",
        "The log log term is meaningful only in the eventual range where it is positive; constants are sharp.",
        ["lil", "brownian-motion", "borel-cantelli", "gaussian-tail"],
    ),
    piece(
        "iid_lil",
        "8.5 Laws of the Iterated Logarithm",
        "Law of the iterated logarithm for iid sums",
        "theorem",
        "For iid mean-zero finite-variance increments with variance sigma^2, limsup S_n / sqrt(2 sigma^2 n log log n) = 1 almost surely, and the liminf is -1.",
        "Embed the random walk in Brownian motion and show the random clock is close enough to n for Brownian LIL scaling.",
        "Use when a problem asks for sharp almost-sure fluctuation size of partial sums.",
        "A CLT-scale heuristic is too small for limsup behavior; LIL has an extra sqrt(log log n) factor.",
        ["lil", "iid", "random-walk", "finite-variance"],
        ["durrett_ch8_brownian_lil"],
    ),
    piece(
        "strassen_invariance_principle",
        "8.5 Laws of the Iterated Logarithm",
        "Strassen invariance principle",
        "theorem",
        "The set of subsequential limit points of suitably LIL-rescaled partial-sum paths is the unit ball of absolutely continuous functions with square-integrable derivative.",
        "Use strong approximation ideas to transfer Brownian compact LIL behavior to partial sums.",
        "A functional strengthening of the scalar LIL; it describes the whole path shape, not just limsup constants.",
        "The limit set is deterministic and compact in path space; it is not a single limiting process.",
        ["strassen", "functional-lil", "invariance-principle", "path-limit-set"],
        ["durrett_ch8_iid_lil"],
    ),
]


SECTION_GUIDES = [
    {
        "section": "8.1 Donsker's Theorem",
        "study_goal": "Use Skorokhod embedding to derive CLT, Donsker convergence, and random-walk path-functional limits.",
        "must_master": ["Skorokhod embedding", "Brownian random clock", "Donsker theorem", "continuous mapping for path functionals", "maxima and occupation examples"],
        "prelim_angle": "Most useful when a random-walk statistic can be rewritten as a Brownian functional in the limit.",
    },
    {
        "section": "8.2 CLTs for Martingales",
        "study_goal": "Prove normal and functional limits for martingale arrays using conditional variances and Lindeberg controls.",
        "must_master": ["martingale embedding", "conditional variance clock", "martingale Lindeberg condition", "martingale CLT"],
        "prelim_angle": "High-yield for dependent sums once the summands have conditional mean zero.",
    },
    {
        "section": "8.3 CLTs for Stationary Sequences",
        "study_goal": "Reduce dependent stationary CLTs to martingale approximations, finite dependence, Markov-chain decompositions, or mixing estimates.",
        "must_master": ["martingale approximation", "projective criteria", "M-dependent variance", "Poisson equation", "mixing covariance bounds"],
        "prelim_angle": "A toolkit for deciding when dependence is weak enough for a normal limit and how to compute long-run variance.",
    },
    {
        "section": "8.4 Empirical Distributions, Brownian Bridge",
        "study_goal": "Move from empirical CDF consistency to sqrt(n) empirical-process fluctuations and Brownian bridge limits.",
        "must_master": ["Glivenko-Cantelli", "empirical process", "Brownian bridge", "Kolmogorov-Smirnov statistic", "killed Brownian density method"],
        "prelim_angle": "Connects iid samples, CDF transforms, and Brownian bridge limits used in goodness-of-fit theory.",
    },
    {
        "section": "8.5 Laws of the Iterated Logarithm",
        "study_goal": "Understand sharp almost-sure fluctuation scales for Brownian motion and iid random walks.",
        "must_master": ["Brownian LIL", "iid LIL", "Borel-Cantelli tail bounds", "Strassen functional LIL"],
        "prelim_angle": "Use for questions about almost-sure limsup behavior rather than distributional limits.",
    },
]


def write_jsonl(path: Path, rows):
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    write_jsonl(OUT / "chapter8_knowledge_pieces.jsonl", PIECES)
    write_jsonl(OUT / "chapter8_section_guides.jsonl", SECTION_GUIDES)

    manifest = {
        "name": "durrett_chapter8_applications_to_random_walk_llm_viki",
        "description": "Curated LLM/Viki-style knowledge pieces for Chapter 8 of Durrett Probability: Theory and Examples.",
        "source_file": str(SOURCE),
        "created_at": CREATED,
        "piece_count": len(PIECES),
        "section_count": len(SECTION_GUIDES),
        "files": [
            "chapter8_knowledge_pieces.jsonl",
            "chapter8_section_guides.jsonl",
            "chapter8_viki.md",
            "chapter8_flashcards.tsv",
            "manifest.json",
        ],
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    md = ["# Durrett Chapter 8 LLM Viki: Applications to Random Walk\n"]
    md.append("Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter8.pdf`.\n")
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
    (OUT / "chapter8_viki.md").write_text("\n".join(md), encoding="utf-8")

    flash = ["id\tfront\tback\ttags"]
    for item in PIECES:
        front = f"{item['title']} ({item['section']})"
        back = f"{item['summary']} Exam use: {item['exam_use']} Pitfall: {item['pitfalls']}"
        flash.append(f"{item['id']}\t{front}\t{back}\t{','.join(item['tags'])}")
    (OUT / "chapter8_flashcards.tsv").write_text("\n".join(flash) + "\n", encoding="utf-8")

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

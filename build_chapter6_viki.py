from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter6_Knowledge"
SOURCE = ROOT / "Probability/Textbook/Chapters/PTE-Chapter6.pdf"

CREATED = datetime.now(timezone.utc).isoformat()


def piece(pid, section, title, kind, summary, proof_idea, exam_use, pitfalls, tags, related=None):
    return {
        "id": f"durrett_ch6_{pid}",
        "source": "Rick Durrett, Probability: Theory and Examples, extracted Chapter 6 PDF",
        "source_file": str(SOURCE),
        "chapter": 6,
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
        "stationary_sequence_definition",
        "6.1 Definitions and Examples",
        "Stationary sequence",
        "definition",
        "A sequence X_0, X_1, ... is stationary when each shifted finite block has the same law as the original block.",
        "Check equality of all finite-dimensional distributions after shifting by k.",
        "Use as the entry point for ergodic averages, stationary Markov chains, rotations, and stationary increments.",
        "Stationarity is distributional, not pathwise equality; it does not imply independence.",
        ["stationarity", "finite-dimensional-laws", "shift"],
    ),
    piece(
        "measure_preserving_shift_model",
        "6.1 Definitions and Examples",
        "Measure-preserving transformation model",
        "construction",
        "Every stationary sequence on a nice state space can be represented as X_n(omega)=X(phi^n omega) for a measure-preserving map phi.",
        "Put the stationary law on sequence space and let phi be the left shift; stationarity makes the shift preserve probability.",
        "Lets all ergodic-theorem statements be proved for one abstract dynamical system.",
        "The representation changes the sample space; it preserves laws but not necessarily the user's original probability space.",
        ["measure-preserving", "shift-space", "stationary-process"],
        ["durrett_ch6_stationary_sequence_definition"],
    ),
    piece(
        "invariant_sigma_field",
        "6.1 Definitions and Examples",
        "Invariant events and invariant sigma-field",
        "definition",
        "An event A is invariant if phi^{-1}A=A up to null sets; the invariant events form the sigma-field I.",
        "Closure under complements and countable unions follows from pulling sets back through phi^{-1}.",
        "The limit in Birkhoff's theorem is the conditional expectation onto I.",
        "Invariant means unchanged under the transformation, not merely high probability overlap after one shift.",
        ["invariant-events", "sigma-field", "conditional-expectation"],
    ),
    piece(
        "ergodicity_definition",
        "6.1 Definitions and Examples",
        "Ergodicity",
        "definition",
        "A measure-preserving transformation is ergodic when every invariant event has probability 0 or 1.",
        "Interpret nonergodicity as the ability to split the space into invariant pieces of positive probability.",
        "Use ergodicity to turn Birkhoff limits E(X|I) into constants EX.",
        "Ergodic is stronger than stationary and different from independent; periodic examples can be stationary but not mixing.",
        ["ergodicity", "invariant-events", "0-1-law"],
        ["durrett_ch6_invariant_sigma_field"],
    ),
    piece(
        "iid_shift_ergodic",
        "6.1 Definitions and Examples",
        "IID shifts are ergodic",
        "example-pattern",
        "For an iid sequence, invariant shift events lie in the tail sigma-field, so Kolmogorov's 0-1 law implies ergodicity.",
        "Iterate shift invariance to show A is measurable with respect to sigma(X_n, X_{n+1}, ...), then intersect over n.",
        "Explains why Birkhoff's theorem recovers the strong law for iid sequences.",
        "The tail sigma-field argument uses iid independence; it is not automatic for every stationary sequence.",
        ["iid", "tail-sigma-field", "ergodic"],
        ["durrett_ch6_ergodicity_definition"],
    ),
    piece(
        "stationary_markov_chain_ergodic",
        "6.1 Definitions and Examples",
        "Stationary Markov chain ergodicity criterion",
        "theorem",
        "A countable-state Markov chain started in a positive stationary distribution is ergodic exactly when the chain is irreducible.",
        "Closed irreducible classes give invariant events; conversely the Markov property and recurrence force invariant probabilities to be constant.",
        "Use for time averages of irreducible positive recurrent chains.",
        "Irreducibility makes I trivial, but periodic chains may still have a nontrivial tail sigma-field.",
        ["markov-chains", "irreducibility", "stationary-distribution"],
        ["durrett_ch6_ergodicity_definition"],
    ),
    piece(
        "circle_rotation_ergodicity",
        "6.1 Definitions and Examples",
        "Circle rotation ergodicity",
        "example-pattern",
        "Rotation x -> x+theta mod 1 is ergodic under Lebesgue measure when theta is irrational and not ergodic when theta is rational.",
        "For irrational theta, Fourier coefficients of an invariant L2 function satisfy c_k(e^{2 pi i k theta}-1)=0, forcing all nonconstant coefficients to vanish.",
        "The canonical deterministic example where ergodic averages behave like probabilistic averages.",
        "Rational rotations have finite orbits and many invariant unions of orbit slices.",
        ["circle-rotation", "fourier-series", "irrational"],
        ["durrett_ch6_ergodicity_definition"],
    ),
    piece(
        "functions_of_stationary_processes",
        "6.1 Definitions and Examples",
        "Functions of stationary processes",
        "fact",
        "Measurable functions of the future of a stationary process form another stationary process; ergodicity is inherited under such factors.",
        "Write Y_k=g(X_k,X_{k+1},...) and compare shifted finite-dimensional distributions.",
        "Useful for creating stationary indicator, block, or return-time processes.",
        "The function must be applied in a shift-compatible way; arbitrary time-dependent functions can destroy stationarity.",
        ["stationary-factors", "measurable-functions", "ergodicity"],
        ["durrett_ch6_stationary_sequence_definition"],
    ),
    piece(
        "birkhoff_ergodic_theorem",
        "6.2 Birkhoff's Ergodic Theorem",
        "Birkhoff ergodic theorem",
        "theorem",
        "For X in L1, the time averages n^{-1} sum_{m<n} X(phi^m omega) converge almost surely and in L1 to E(X|I).",
        "Subtract E(X|I), use the maximal ergodic lemma to rule out positive limsup and negative liminf, then truncate for L1 convergence.",
        "Main tool for replacing long-run empirical averages by conditional or ordinary means.",
        "Without ergodicity the limit is random: it is E(X|I), not necessarily EX.",
        ["birkhoff", "ergodic-theorem", "time-averages"],
        ["durrett_ch6_invariant_sigma_field"],
    ),
    piece(
        "maximal_ergodic_lemma",
        "6.2 Birkhoff's Ergodic Theorem",
        "Maximal ergodic lemma",
        "lemma",
        "For partial sums S_k of X along a measure-preserving orbit and M_k=max(0,S_1,...,S_k), one has E(X; M_k>0) >= 0.",
        "Compare X(omega)+M_k(phi omega) with each S_j(omega), integrate, and use measure preservation.",
        "The key technical inequality behind Birkhoff's pointwise convergence proof.",
        "It is an integration inequality, not a direct maximal probability bound; track the set {M_k>0}.",
        ["maximal-ergodic-lemma", "partial-sums", "birkhoff-proof"],
        ["durrett_ch6_birkhoff_ergodic_theorem"],
    ),
    piece(
        "strong_law_from_birkhoff",
        "6.2 Birkhoff's Ergodic Theorem",
        "Strong law as an ergodic theorem",
        "example-pattern",
        "For iid X_m in L1, Birkhoff gives n^{-1} sum_{m<n} X_m -> E X_0 almost surely and in L1.",
        "The iid shift is ergodic, so E(X_0|I)=E X_0.",
        "Use as a conceptual shortcut from Chapter 2 LLNs to general stationary sequences.",
        "The theorem needs integrability; for nonintegrable iid variables this conclusion can fail.",
        ["strong-law", "iid", "birkhoff"],
        ["durrett_ch6_iid_shift_ergodic", "durrett_ch6_birkhoff_ergodic_theorem"],
    ),
    piece(
        "markov_chain_time_average",
        "6.2 Birkhoff's Ergodic Theorem",
        "Stationary Markov chain time averages",
        "corollary",
        "For an irreducible countable-state Markov chain started from its stationary distribution pi, n^{-1} sum_{m<n} f(X_m) -> sum_x f(x) pi(x) for pi-integrable f.",
        "Apply Birkhoff to f(X_0) and use the irreducible stationary chain's ergodicity.",
        "Recovers the long-run frequency and reward law for positive recurrent Markov chains.",
        "The statement is under stationarity; nonstationary initial laws need an additional argument.",
        ["markov-chains", "time-averages", "stationary-distribution"],
        ["durrett_ch6_stationary_markov_chain_ergodic", "durrett_ch6_birkhoff_ergodic_theorem"],
    ),
    piece(
        "weyl_equidistribution",
        "6.2 Birkhoff's Ergodic Theorem",
        "Weyl equidistribution from irrational rotation",
        "theorem",
        "For irrational theta, the orbit x+n theta mod 1 visits every interval [a,b) with limiting frequency b-a for every starting x.",
        "Apply Birkhoff to interval indicators, then remove the exceptional set by approximating intervals from inside and using density.",
        "Use for deterministic averaging and number-theoretic distribution mod 1.",
        "Birkhoff first gives almost-every starting point; the interval theorem needs extra work for every x.",
        ["equidistribution", "irrational-rotation", "intervals"],
        ["durrett_ch6_circle_rotation_ergodicity", "durrett_ch6_birkhoff_ergodic_theorem"],
    ),
    piece(
        "benford_law_powers",
        "6.2 Birkhoff's Ergodic Theorem",
        "Benford law for powers",
        "example-pattern",
        "If log_10 2 is irrational, the first digit of 2^m has limiting frequency log_10((k+1)/k) for digit k.",
        "First digits correspond to fractional parts of m log_10 2 lying in [log_10 k, log_10(k+1)).",
        "A memorable application of equidistribution to leading-digit asymptotics.",
        "Benford frequencies describe a limiting distribution, not exact finite-sample frequencies.",
        ["benford-law", "equidistribution", "first-digits"],
        ["durrett_ch6_weyl_equidistribution"],
    ),
    piece(
        "lp_upgrade_birkhoff",
        "6.2 Birkhoff's Ergodic Theorem",
        "Lp convergence upgrade",
        "exercise-pattern",
        "If X is in Lp for p>1, the Birkhoff averages converge in Lp as well as almost surely.",
        "Use maximal or domination arguments for the averages and uniform integrability of powers.",
        "Useful when a problem asks for convergence in norm rather than only almost surely.",
        "Do not infer Lp convergence from L1 convergence without an Lp bound or uniform integrability.",
        ["lp-convergence", "uniform-integrability", "birkhoff"],
        ["durrett_ch6_birkhoff_ergodic_theorem"],
    ),
    piece(
        "range_growth_stationary_increments",
        "6.3 Recurrence",
        "Range growth for stationary increments",
        "theorem",
        "For a stationary-increment walk S_n, the range R_n=|{S_1,...,S_n}| satisfies R_n/n -> E(1_A|I), where A is the event of never returning to 0 after time 0.",
        "Bound R_n below by future-noncollision indicators and above by finite-window noncollision indicators, then apply Birkhoff and monotone convergence.",
        "Connects recurrence questions to an ergodic average of escape events.",
        "The limit is conditional on I; only in ergodic cases does it reduce to P(A).",
        ["range", "stationary-increments", "recurrence"],
        ["durrett_ch6_birkhoff_ergodic_theorem"],
    ),
    piece(
        "zero_drift_integer_recurrence",
        "6.3 Recurrence",
        "Zero conditional drift implies recurrence on Z",
        "theorem",
        "For stationary integer-valued increments with E|X_1|<infinity and E(X_1|I)=0, the walk returns to 0 infinitely often almost surely.",
        "Birkhoff gives S_n/n -> 0, so the range is sublinear; the range theorem forces escape probability zero, and stationarity then gives infinitely many returns.",
        "Generalizes the Chung-Fuchs recurrence intuition beyond iid increments.",
        "The condition is E(X_1|I)=0, not merely EX_1=0; mixtures of positive and negative drifts are counterexamples.",
        ["recurrence", "zero-drift", "stationary-increments"],
        ["durrett_ch6_range_growth_stationary_increments"],
    ),
    piece(
        "stationary_return_times_kac",
        "6.3 Recurrence",
        "Kac return-time theorem",
        "theorem",
        "For a stationary process that hits A almost surely, the successive return gaps to A are stationary under P(.|X_0 in A), and E(T_1|X_0 in A)=1/P(X_0 in A).",
        "Embed the process two-sided, decompose by the last visit before time 0, and sum tail probabilities of the first return.",
        "Turns visits to a set into regenerative cycles and recovers mean return time 1/pi(x) for Markov chains.",
        "Conditioning on X_0 in A is essential; the first waiting time from an arbitrary stationary time has a length-biased flavor.",
        ["kac", "return-times", "stationary-processes"],
    ),
    piece(
        "cycle_trick_stationary_measure",
        "6.3 Recurrence",
        "Cycle trick for stationary measures",
        "exercise-pattern",
        "Expected occupation of B during a return cycle to A equals P(X_0 in B)/P(X_0 in A) when A and B are disjoint and A is recurrent.",
        "Sum indicators over the cycle and use stationarity to convert cycle occupation counts into one-time probabilities.",
        "Useful for constructing stationary measures of Markov chains from excursions.",
        "The denominator is the stationary mass of A; the formula is not a conditional probability of hitting B before returning.",
        ["cycle-trick", "occupation-times", "stationary-measure"],
        ["durrett_ch6_stationary_return_times_kac"],
    ),
    piece(
        "stationary_renewal_waiting_time",
        "6.3 Recurrence",
        "Stationary renewal waiting-time bias",
        "exercise-pattern",
        "For a stationary {0,1} process conditioned on X_0=1, the first return law satisfies Pbar(T_1=n)=Pbar(T_1>=n)/Ebar T_1 in the iid-gap renewal case.",
        "Count which positions inside a renewal interval can serve as the stationary origin.",
        "Explains inspection-paradox corrections in stationary renewal processes.",
        "The distribution seen from a stationary time differs from the raw interarrival distribution.",
        ["renewal", "return-time", "inspection-paradox"],
        ["durrett_ch6_stationary_return_times_kac"],
    ),
    piece(
        "subadditive_ergodic_theorem",
        "6.4 A Subadditive Ergodic Theorem",
        "Subadditive ergodic theorem",
        "theorem",
        "For a stationary subadditive array X_{m,n} with integrability and a linear lower expectation bound, X_{0,n}/n converges almost surely and in L1 to a limit with mean inf_m E X_{0,m}/m.",
        "Use Fekete's lemma for expectations, Birkhoff on block increments for the limsup, then a covering argument for the liminf.",
        "The main tool for limits of optimal costs, passage times, longest subsequences, and products.",
        "Check the exact stationarity assumptions; Liggett's version is weaker than Kingman's original in useful applications.",
        ["subadditive-ergodic-theorem", "kingman", "liggett"],
    ),
    piece(
        "fekete_expectation_step",
        "6.4 A Subadditive Ergodic Theorem",
        "Fekete step for expected subadditive arrays",
        "proof-template",
        "If a_n=E X_{0,n} and a_m+a_{n-m}>=a_n, then a_n/n converges to inf_m a_m/m.",
        "Write n=km+r, iterate subadditivity, divide by n, and let n grow with fixed m.",
        "Use whenever the deterministic expectation part of a subadditive theorem appears.",
        "The inequality direction is easy to mix up because the array convention is X_{0,m}+X_{m,n}>=X_{0,n}.",
        ["fekete", "expectations", "subadditivity"],
        ["durrett_ch6_subadditive_ergodic_theorem"],
    ),
    piece(
        "birkhoff_as_additive_case",
        "6.4 A Subadditive Ergodic Theorem",
        "Birkhoff as the additive special case",
        "example-pattern",
        "If X_{m,n}=xi_{m+1}+...+xi_n for a stationary integrable sequence, then the subadditive theorem reduces to Birkhoff.",
        "The subadditive inequality becomes equality, and block stationarity is inherited from the xi sequence.",
        "A quick consistency check for the hypotheses of the subadditive theorem.",
        "Do not lose the indexing: X_{m,n} covers increments after m through n.",
        ["additive-case", "stationary-sequence", "birkhoff"],
        ["durrett_ch6_subadditive_ergodic_theorem", "durrett_ch6_birkhoff_ergodic_theorem"],
    ),
    piece(
        "range_subadditive_example",
        "6.4 A Subadditive Ergodic Theorem",
        "Range as a subadditive example",
        "example-pattern",
        "The number of distinct sites visited between times m+1 and n is subadditive, so the normalized range has an almost sure and L1 limit.",
        "The union of sites in two adjacent time intervals covers the sites in the whole interval, giving X_{0,m}+X_{m,n}>=X_{0,n}.",
        "Provides a second route to existence of range-growth rates even when the rate is not identified.",
        "The theorem gives existence of the limit, not the recurrence classification by itself.",
        ["range", "random-walk", "subadditivity"],
        ["durrett_ch6_subadditive_ergodic_theorem"],
    ),
    piece(
        "longest_common_subsequence_limit",
        "6.4 A Subadditive Ergodic Theorem",
        "Longest common subsequence limit",
        "example-pattern",
        "For two ergodic stationary sequences, the longest common subsequence length L_{0,n} satisfies L_{0,n}/n -> gamma, where gamma=sup_m E L_{0,m}/m.",
        "Use superadditivity of L over adjacent blocks, or subadditivity of -L, and apply the subadditive ergodic theorem.",
        "Recognize optimization lengths as candidates for subadditive limits.",
        "The theorem proves existence of gamma but usually not its numerical value.",
        ["longest-common-subsequence", "superadditivity", "ergodic-limit"],
        ["durrett_ch6_subadditive_ergodic_theorem"],
    ),
    piece(
        "random_matrix_products",
        "6.5 Applications",
        "Products of positive random matrices",
        "application",
        "For stationary positive matrices with integrable log entries, n^{-1} log of product entries converges almost surely to a common growth rate.",
        "Take minus logs of positive product entries to create a subadditive array; compare entries and norms to transfer the limit.",
        "A probability route to Lyapunov-exponent-type limits.",
        "Strict positivity and log-integrability matter; zeros or heavy tails can break the logarithmic comparison.",
        ["random-matrices", "lyapunov-exponent", "subadditivity"],
        ["durrett_ch6_subadditive_ergodic_theorem"],
    ),
    piece(
        "increasing_subsequence_permutation",
        "6.5 Applications",
        "Increasing subsequences in random permutations",
        "application",
        "Poissonizing random permutations and applying subadditivity shows the longest increasing subsequence has an n^{1/2} order limit constant.",
        "Represent permutations by Poisson points in squares, use superadditivity of increasing paths, then de-Poissonize with the Poisson count law.",
        "A classic example of turning a combinatorial optimization problem into an ergodic limit.",
        "The subadditive argument gives the existence of the constant; identifying it as 2 requires deeper work.",
        ["random-permutations", "longest-increasing-subsequence", "poissonization"],
        ["durrett_ch6_subadditive_ergodic_theorem"],
    ),
    piece(
        "poisson_square_time_change",
        "6.5 Applications",
        "Poisson square time change",
        "lemma",
        "If tau(n) is the side length of the square containing the first n points of a rate-one planar Poisson process, then tau(n)/sqrt(n) -> 1 almost surely.",
        "The number of points in the square of side sqrt(n) is a sum of independent mean-one Poisson increments, so the strong law controls the inverse time.",
        "Used to pass from Poissonized increasing paths back to fixed-size random permutations.",
        "The scale is sqrt(n) because the square area is t^2.",
        ["poisson-process", "time-change", "permutation"],
        ["durrett_ch6_increasing_subsequence_permutation"],
    ),
    piece(
        "first_passage_percolation_time_constant",
        "6.5 Applications",
        "First-passage percolation time constant",
        "application",
        "For iid nonnegative edge passage times on Z^d with suitable integrability, t(0,nu)/n converges almost surely to a deterministic time constant.",
        "Passage times satisfy t(0,nu)<=t(0,mu)+t(mu,nu), so X_{m,n}=t(mu,nu) is subadditive; tail triviality makes the limit constant.",
        "Core template for metric growth models and random media.",
        "Finite mean of one edge is sufficient in the simple statement but can be weakened; without integrability the limit may be infinite.",
        ["first-passage-percolation", "time-constant", "random-media"],
        ["durrett_ch6_subadditive_ergodic_theorem"],
    ),
    piece(
        "fpp_integrability_min_condition",
        "6.5 Applications",
        "First-passage percolation integrability condition",
        "criterion",
        "A weaker useful condition is that the minimum of 2d independent edge times has finite mean, equivalently integral_0^infty (1-F(x))^{2d} dx < infinity.",
        "Use disjoint neighboring paths to dominate one-step passage times by minima of several edge variables.",
        "Helps check when a finite time constant exists for heavy-tailed edge weights.",
        "This condition concerns the minimum of several edges, not the edge variable itself.",
        ["first-passage-percolation", "integrability", "heavy-tails"],
        ["durrett_ch6_first_passage_percolation_time_constant"],
    ),
    piece(
        "age_dependent_branching_speed",
        "6.5 Applications",
        "Age-dependent branching process speed",
        "application",
        "In an age-dependent branching process with no extinction at birth and finite lifetimes, the first birth time in generation n divided by n converges almost surely.",
        "Define X_{m,n} as the additional time from the first generation-m individual to a generation-n descendant and apply Liggett's subadditive theorem.",
        "Shows why the weaker Liggett hypotheses are useful beyond Kingman's original stationary-array assumptions.",
        "The stronger all-triples subadditivity can fail because the fastest later descendant need not descend from the fastest earlier individual.",
        ["branching-process", "subadditivity", "growth-speed"],
        ["durrett_ch6_subadditive_ergodic_theorem"],
    ),
    piece(
        "branching_speed_large_deviation_formula",
        "6.5 Applications",
        "Branching speed via lifetime large deviations",
        "formula",
        "For mean offspring mu and lifetime sums with rate c(a), the asymptotic earliest-generation speed is gamma=inf{a: log mu - c(a)>0}.",
        "Compare expected counts of generation-n individuals born by time an with branching-process survival when the count grows supercritically.",
        "Connects subadditive limits with large-deviation rate functions.",
        "The subadditive theorem gives existence; this formula requires additional branching and large-deviation analysis.",
        ["branching-process", "large-deviations", "speed"],
        ["durrett_ch6_age_dependent_branching_speed"],
    ),
]


SECTION_GUIDES = [
    {
        "section": "6.1 Definitions and Examples",
        "study_goal": "Translate stationary sequences into measure-preserving dynamical systems and identify ergodic examples.",
        "must_master": ["stationarity", "measure-preserving maps", "invariant sigma-field", "ergodicity", "iid shifts", "stationary Markov chains", "irrational rotations"],
        "prelim_angle": "Most Chapter 6 problems start by checking whether the invariant sigma-field is trivial.",
    },
    {
        "section": "6.2 Birkhoff's Ergodic Theorem",
        "study_goal": "Use Birkhoff's theorem to turn long-run averages into conditional expectations or constants.",
        "must_master": ["Birkhoff theorem", "maximal ergodic lemma", "SLLN as a special case", "Markov chain averages", "equidistribution"],
        "prelim_angle": "This is the high-yield theorem for time averages of dependent stationary data.",
    },
    {
        "section": "6.3 Recurrence",
        "study_goal": "Apply ergodic averages to range growth, recurrence of stationary-increment walks, and return cycles.",
        "must_master": ["range theorem", "zero conditional drift recurrence", "Kac return-time theorem", "cycle trick"],
        "prelim_angle": "Good recurrence problems often ask you to identify escape probability or mean return time from stationarity.",
    },
    {
        "section": "6.4 A Subadditive Ergodic Theorem",
        "study_goal": "Recognize subadditive arrays and prove normalized optimal costs have limits.",
        "must_master": ["subadditive array hypotheses", "Fekete expectation step", "ergodic constant case", "range and LCS examples"],
        "prelim_angle": "Use when the quantity is an optimal path length, cost, passage time, or negative of a superadditive reward.",
    },
    {
        "section": "6.5 Applications",
        "study_goal": "See the subadditive theorem in random matrices, random permutations, first-passage percolation, and branching processes.",
        "must_master": ["random matrix products", "Poissonization", "FPP time constant", "integrability checks", "branching-process speed"],
        "prelim_angle": "Applications usually reduce to checking subadditivity plus stationarity and then interpreting the constant.",
    },
]


def write_jsonl(path: Path, rows):
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    write_jsonl(OUT / "chapter6_knowledge_pieces.jsonl", PIECES)
    write_jsonl(OUT / "chapter6_section_guides.jsonl", SECTION_GUIDES)

    manifest = {
        "name": "durrett_chapter6_ergodic_theorems_llm_viki",
        "description": "Curated LLM/Viki-style knowledge pieces for Chapter 6 of Durrett Probability: Theory and Examples.",
        "source_file": str(SOURCE),
        "created_at": CREATED,
        "piece_count": len(PIECES),
        "section_count": len(SECTION_GUIDES),
        "files": [
            "chapter6_knowledge_pieces.jsonl",
            "chapter6_section_guides.jsonl",
            "chapter6_viki.md",
            "chapter6_flashcards.tsv",
            "manifest.json",
        ],
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    md = ["# Durrett Chapter 6 LLM Viki: Ergodic Theorems\n"]
    md.append("Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter6.pdf`.\n")
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
    (OUT / "chapter6_viki.md").write_text("\n".join(md), encoding="utf-8")

    flash = ["id\tfront\tback\ttags"]
    for item in PIECES:
        front = f"{item['title']} ({item['section']})"
        back = f"{item['summary']} Exam use: {item['exam_use']} Pitfall: {item['pitfalls']}"
        flash.append(f"{item['id']}\t{front}\t{back}\t{','.join(item['tags'])}")
    (OUT / "chapter6_flashcards.tsv").write_text("\n".join(flash) + "\n", encoding="utf-8")

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

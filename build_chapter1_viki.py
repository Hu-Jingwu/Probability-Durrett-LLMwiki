from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Probability/LLM_Viki_Dataset/Chapter1_Knowledge"
SOURCE = ROOT / "Probability/Textbook/Chapters/PTE-Chapter1.pdf"


CREATED = datetime.now(timezone.utc).isoformat()


def piece(pid, section, title, kind, summary, proof_idea, exam_use, pitfalls, tags, related=None):
    return {
        "id": f"durrett_ch1_{pid}",
        "source": "Rick Durrett, Probability: Theory and Examples, extracted Chapter 1 PDF",
        "source_file": str(SOURCE),
        "chapter": 1,
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
        "probability_space",
        "1.1 Probability Spaces",
        "Probability space",
        "definition",
        "A probability model is a triple (Omega, F, P): outcomes, a sigma-field of events, and a countably additive probability measure with total mass 1.",
        "Most elementary probability identities are consequences of complement closure, countable union closure, and countable additivity.",
        "Use this as the opening language for proofs involving events, limsup/liminf events, and Borel-Cantelli later in Chapter 2.",
        "Do not treat arbitrary subsets as events unless F is the full power set; measurability is part of the model.",
        ["probability-space", "sigma-field", "measure"],
    ),
    piece(
        "sigma_field",
        "1.1 Probability Spaces",
        "Sigma-field closure rules",
        "definition",
        "A sigma-field is closed under complements and countable unions, hence also under countable intersections and finite set operations.",
        "Use De Morgan's laws to derive intersection closure from complement and union closure.",
        "When proving a random object is measurable, show that a convenient generating class of inverse images lies in F.",
        "A countable union is allowed; an arbitrary uncountable union need not be in the sigma-field.",
        ["sigma-field", "closure", "measurability"],
        ["durrett_ch1_measurability_generator"],
    ),
    piece(
        "measure_continuity",
        "1.1 Probability Spaces",
        "Continuity of measure",
        "theorem",
        "For increasing events A_n, P(union A_n) is the limit of P(A_n). For decreasing events A_n with finite first measure, P(intersection A_n) is the limit of P(A_n).",
        "Write increasing differences as disjoint pieces; for decreasing sets apply the increasing result to complements or differences.",
        "Essential for limits of events, almost sure convergence criteria, and first Borel-Cantelli arguments.",
        "For decreasing continuity, the finite-measure condition matters for general measures; it is automatic under probability measures.",
        ["continuity-from-below", "continuity-from-above", "events"],
    ),
    piece(
        "discrete_probability_space",
        "1.1 Probability Spaces",
        "Discrete probability spaces",
        "example",
        "On a countable sample space, assign nonnegative masses p(omega) summing to 1, and define P(A) as the sum over omega in A.",
        "Countable additivity reduces to rearranging nonnegative series.",
        "Useful for checking intuition before proving the analogous statement for general measures.",
        "If the sample space is uncountable, point masses need not determine the whole law.",
        ["discrete", "mass-function", "countable"],
    ),
    piece(
        "stieltjes_measure",
        "1.1 Probability Spaces",
        "Stieltjes measures from distribution-like functions",
        "theorem",
        "A nondecreasing right-continuous function with suitable limits defines a unique measure on the Borel line via interval increments.",
        "First define the measure on intervals, verify finite additivity and continuity, then extend to the generated sigma-field.",
        "This is the bridge from CDFs to probability measures on R.",
        "Right-continuity is not cosmetic; it pins down the measure on half-infinite intervals and atoms.",
        ["stieltjes", "cdf", "borel-measure"],
        ["durrett_ch1_distribution_function"],
    ),
    piece(
        "semialgebra_extension",
        "1.1 Probability Spaces",
        "Extension from semialgebras",
        "proof-template",
        "A measure-like set function on a semialgebra can be extended when it has the right countable additivity/continuity behavior on the generating class.",
        "Pass from semialgebra pieces to finite disjoint unions, then use approximation and countable additivity to extend.",
        "Explains why specifying probabilities on intervals or rectangles is enough in many probability models.",
        "Do not assume every finitely additive premeasure extends; the countable condition is the serious part.",
        ["semialgebra", "extension", "premeasure"],
    ),
    piece(
        "product_distribution_function",
        "1.1 Probability Spaces",
        "Multidimensional distribution functions",
        "theorem",
        "A function on R^d satisfying monotonicity over rectangles, right-continuity, and correct limits defines a probability measure on Borel R^d.",
        "Use rectangle increments and an extension theorem from a semialgebra of rectangles.",
        "This underlies joint distributions and later independence statements.",
        "Coordinatewise monotonicity alone is not enough; rectangle probabilities must be nonnegative.",
        ["joint-distribution", "rectangles", "borel-rd"],
    ),
    piece(
        "distribution_function",
        "1.2 Distributions",
        "Distribution function properties",
        "theorem",
        "A CDF is nondecreasing, right-continuous, tends to 0 at -infinity, and tends to 1 at +infinity.",
        "Monotonicity follows from event inclusion; right-continuity follows from continuity of probability for decreasing events.",
        "Use these properties to test whether a proposed function can be a CDF.",
        "Left-continuity is generally false; jumps represent atoms.",
        ["cdf", "distribution", "right-continuity"],
    ),
    piece(
        "cdf_to_law",
        "1.2 Distributions",
        "Every valid CDF determines a law",
        "theorem",
        "Any function with the standard CDF properties is the distribution function of a unique probability measure on R.",
        "Construct a Stieltjes measure and check that its half-line values match the function.",
        "Lets you prove convergence claims by identifying limiting CDFs, provided the limit is a valid CDF at continuity points.",
        "A pointwise limit of CDFs may fail to be a CDF if total mass escapes to infinity.",
        ["cdf", "law", "tightness"],
        ["durrett_ch1_stieltjes_measure"],
    ),
    piece(
        "atoms_jumps",
        "1.2 Distributions",
        "Atoms are jumps of the CDF",
        "fact",
        "For a real random variable, P(X = x) equals the jump F(x) - F(x-) of its distribution function.",
        "Compare events {X <= x} and {X < x}; use monotone convergence from below for F(x-).",
        "Useful for mixed discrete-continuous examples and for proving a CDF has at most countably many discontinuities.",
        "A continuous CDF does not imply a density exists; the Cantor distribution is the standard warning.",
        ["atom", "cdf-jump", "discontinuity"],
    ),
    piece(
        "normal_tail_bound",
        "1.2 Distributions",
        "Standard normal tail estimate",
        "inequality",
        "The standard normal upper tail has exponential decay comparable to phi(x)/x for positive x.",
        "Integrate the normal density and compare using monotonicity or one integration-by-parts style bound.",
        "Appears in Brownian motion, LIL-style bounds, and CLT error estimates.",
        "Keep track of whether a bound is one-sided or two-sided; prelim solutions often lose constants harmlessly but not exponents.",
        ["normal", "tail-bound", "inequality"],
    ),
    piece(
        "probability_integral_transform",
        "1.2 Distributions",
        "Probability integral transform",
        "fact",
        "If X has a continuous CDF F, then F(X) is uniform on (0,1) under suitable strictness/continuity conditions.",
        "Compute P(F(X) <= u) by translating through quantiles; handle flat parts carefully.",
        "Useful for constructing random variables from uniform variables and for distribution transformations.",
        "Continuity alone needs care when F has flat intervals; use generalized inverses for the clean general statement.",
        ["cdf-transform", "uniform", "quantile"],
    ),
    piece(
        "measurable_map",
        "1.3 Random Variables",
        "Random variables as measurable maps",
        "definition",
        "A random variable is a measurable map from the sample space to a measurable state space.",
        "Check inverse images of measurable target sets.",
        "This is the language needed for sigma(X), conditional expectation, and stochastic processes.",
        "Do not confuse a random variable with its distribution; different variables may have the same law.",
        ["random-variable", "measurable-map", "law"],
    ),
    piece(
        "measurability_generator",
        "1.3 Random Variables",
        "Checking measurability on generators",
        "theorem",
        "To prove X is measurable into a generated sigma-field, it is enough to check inverse images of a generating class.",
        "The inverse-image operation preserves complements and countable unions, so the checked class expands to a sigma-field.",
        "Use half-lines for real variables and rectangles for vector-valued variables.",
        "The generator must actually generate the target sigma-field; checking too small a class proves too little.",
        ["measurability", "generator", "inverse-image"],
        ["durrett_ch1_sigma_field"],
    ),
    piece(
        "composition_measurable",
        "1.3 Random Variables",
        "Composition of measurable maps",
        "theorem",
        "If X is measurable and f is measurable, then f(X) is measurable.",
        "Inverse images compose: {f(X) in A} equals {X in f^{-1}(A)}.",
        "Use this to justify transformations such as X^2, exp(X), indicators, vectors, sums, limsup, and liminf.",
        "Continuity is sufficient for Borel measurability, but not necessary.",
        ["composition", "transformation", "measurable"],
    ),
    piece(
        "measurable_arithmetic",
        "1.3 Random Variables",
        "Arithmetic of random variables",
        "theorem",
        "Finite sums, products, maxima, minima, and continuous functions of random variables are random variables.",
        "View (X,Y) as a measurable vector and compose with continuous maps such as addition or multiplication.",
        "Often needed before taking expectations of constructed quantities.",
        "Do not use arithmetic closure for extended real expressions without checking undefined forms like infinity minus infinity.",
        ["arithmetic", "measurable", "random-variables"],
    ),
    piece(
        "limits_measurable",
        "1.3 Random Variables",
        "Limits preserve measurability",
        "theorem",
        "Supremum, infimum, limsup, liminf, and pointwise limits of measurable real functions are measurable.",
        "Express events such as {sup X_n <= a} or {limsup X_n < a} using countable unions/intersections of measurable events.",
        "Crucial for defining almost sure convergence and stopping-time events.",
        "The countability of the sequence matters; arbitrary suprema over uncountable families can fail measurability.",
        ["limsup", "liminf", "measurability", "countability"],
    ),
    piece(
        "sigma_x_factorization",
        "1.3 Random Variables",
        "Functions measurable with respect to sigma(X)",
        "fact",
        "A random variable Y is sigma(X)-measurable exactly when it can be represented as a measurable function of X.",
        "Approximate Y by simple functions and show each sigma(X)-measurable indicator factors through X.",
        "This is a foundation for conditional expectation as a function of observed information.",
        "The representing function is only determined up to the distribution of X, not necessarily pointwise everywhere.",
        ["sigma-x", "factorization", "conditional-expectation"],
    ),
    piece(
        "simple_functions",
        "1.4 Integration",
        "Simple functions",
        "definition",
        "A simple function takes finitely many values and is the starting point for defining the Lebesgue integral.",
        "Define the integral as the sum of value times measure over level sets, then extend by monotone approximation.",
        "When stuck on an integral proof, first prove it for indicators, then simple functions, then limits.",
        "Representations of a simple function are not unique; use canonical level sets to avoid ambiguity.",
        ["simple-function", "lebesgue-integral", "proof-template"],
    ),
    piece(
        "nonnegative_integral",
        "1.4 Integration",
        "Integral of a nonnegative function",
        "definition",
        "The integral of a nonnegative measurable function is the supremum of integrals of simple functions bounded above by it.",
        "Approximate from below by simple functions and use monotone behavior.",
        "This definition makes monotone convergence natural rather than surprising.",
        "The value may be infinite; do not subtract two infinite nonnegative integrals.",
        ["nonnegative-integral", "approximation", "mct"],
    ),
    piece(
        "integrable_function",
        "1.4 Integration",
        "Integrable signed functions",
        "definition",
        "A signed measurable function is integrable when the integrals of its positive and negative parts are finite, equivalently the integral of its absolute value is finite.",
        "Define integral as integral of positive part minus integral of negative part.",
        "Before using linearity or dominated convergence, check integrability conditions.",
        "Finite positive and negative parts are needed; infinity minus infinity is not an acceptable value.",
        ["integrability", "positive-part", "negative-part"],
    ),
    piece(
        "integral_linearity",
        "1.4 Integration",
        "Linearity and order properties of the integral",
        "theorem",
        "For integrable functions, the integral is linear, monotone, and respects almost-everywhere equality.",
        "Prove first for simple functions, extend to nonnegative functions, then signed integrable functions.",
        "Use to split expectations, compare nonnegative variables, and justify replacing variables by a.s. equal versions.",
        "Linearity can fail as a finite statement if one side involves undefined infinities.",
        ["linearity", "monotonicity", "almost-everywhere"],
    ),
    piece(
        "jensen_integral",
        "1.5 Properties of the Integral",
        "Jensen's inequality for integrals",
        "inequality",
        "For a convex function phi and a probability measure, phi(integral f) is at most integral phi(f), assuming the quantities are defined.",
        "Use a supporting line to the convex function at the mean.",
        "Prelim workhorse for Lp comparisons, moment generating bounds, and conditional Jensen later.",
        "Convexity direction matters; strict equality often encodes almost sure constancy under strict convexity.",
        ["jensen", "convexity", "inequality"],
    ),
    piece(
        "holder_integral",
        "1.5 Properties of the Integral",
        "Holder's inequality",
        "inequality",
        "If p and q are conjugate exponents, the integral of |fg| is bounded by the Lp norm of f times the Lq norm of g.",
        "Normalize the functions and apply Young's inequality; handle zero norms separately.",
        "Used for moment interpolation, uniform integrability checks, and bounding expectations of products.",
        "Remember the endpoint cases need separate interpretation.",
        ["holder", "lp", "inequality"],
    ),
    piece(
        "minkowski",
        "1.5 Properties of the Integral",
        "Minkowski's inequality",
        "inequality",
        "The Lp norm satisfies the triangle inequality for p at least 1.",
        "Apply Holder to |f+g|^p split as |f+g|^{p-1}|f| plus the analogous term for g.",
        "Use to prove Lp spaces are normed and to control sums of random variables in Lp.",
        "For p below 1 this is not a norm inequality.",
        ["minkowski", "lp", "triangle-inequality"],
        ["durrett_ch1_holder_integral"],
    ),
    piece(
        "bounded_convergence",
        "1.5 Properties of the Integral",
        "Bounded convergence theorem",
        "theorem",
        "On a finite-measure space, uniformly bounded functions converging pointwise have integrals converging to the integral of the limit.",
        "Reduce to dominated convergence with a constant dominating function, or prove using finite measure and small exceptional sets.",
        "Useful for probability spaces when random variables are uniformly bounded.",
        "Finite measure is essential; bounded pointwise convergence on an infinite measure space need not preserve integrals.",
        ["bounded-convergence", "finite-measure", "limit"],
    ),
    piece(
        "fatou_integral",
        "1.5 Properties of the Integral",
        "Fatou's lemma",
        "theorem",
        "For nonnegative functions, the integral of the liminf is at most the liminf of the integrals.",
        "Let g_n be the infimum over the tail; g_n increases to the liminf and monotone convergence applies.",
        "Use for lower semicontinuity of expectations and to prove integrability of a limit from bounded expectations.",
        "Fatou gives an inequality, not usually equality.",
        ["fatou", "liminf", "nonnegative"],
    ),
    piece(
        "monotone_convergence",
        "1.5 Properties of the Integral",
        "Monotone convergence theorem",
        "theorem",
        "If nonnegative measurable functions increase pointwise to f, then their integrals increase to the integral of f.",
        "The lower approximation definition of the integral makes the result direct.",
        "Use for exchanging sums and expectations of nonnegative random variables.",
        "The monotone direction and nonnegativity are not optional unless you shift or dominate carefully.",
        ["mct", "monotone-convergence", "nonnegative"],
    ),
    piece(
        "dominated_convergence",
        "1.5 Properties of the Integral",
        "Dominated convergence theorem",
        "theorem",
        "If f_n converges pointwise a.e. to f and |f_n| is bounded by an integrable g, then integrals of f_n converge to the integral of f.",
        "Apply Fatou to g + f_n and g - f_n, or to |f_n - f| after a standard argument.",
        "The main theorem for passing limits through expectations under a uniform integrable bound.",
        "Pointwise boundedness is not enough; the dominating function must be integrable and independent of n.",
        ["dct", "dominated-convergence", "limit"],
    ),
    piece(
        "expectation_as_integral",
        "1.6 Expected Value",
        "Expected value as Lebesgue integral",
        "definition",
        "Expectation is the integral of a random variable with respect to the probability measure.",
        "All integral theorems transfer directly to expectations.",
        "This unifies discrete sums, density integrals, and abstract random variables.",
        "An expectation can be undefined if positive and negative parts are both infinite.",
        ["expectation", "lebesgue-integral", "random-variable"],
    ),
    piece(
        "expectation_linearity",
        "1.6 Expected Value",
        "Linearity and monotonicity of expectation",
        "theorem",
        "Expectation is linear for integrable random variables and monotone for ordered random variables.",
        "Apply integral linearity and monotonicity.",
        "Use constantly in variance, covariance, martingale, and conditioning calculations.",
        "Linearity does not require independence; product factorization does.",
        ["expectation", "linearity", "monotonicity"],
    ),
    piece(
        "markov_chebyshev",
        "1.6 Expected Value",
        "Markov and Chebyshev inequalities",
        "inequality",
        "Markov bounds the probability of a nonnegative variable exceeding a threshold by its expectation over the threshold; Chebyshev applies this to powers or centered moments.",
        "Use the indicator inequality a 1_{X >= a} <= X for Markov, then specialize with nonnegative functions.",
        "Core tool for convergence in probability, LLN proofs, and variance bounds.",
        "Check nonnegativity and choose the right moment; a weak moment gives a weak tail bound.",
        ["markov-inequality", "chebyshev", "tail-bound"],
    ),
    piece(
        "expectation_limit_theorems",
        "1.6 Expected Value",
        "Limit theorems for expectation",
        "theorem-card",
        "Fatou, monotone convergence, dominated convergence, and bounded convergence all have expectation versions.",
        "Translate each integral theorem to the probability space.",
        "A prelim proof often hinges on naming exactly the right convergence theorem and verifying its hypotheses.",
        "Do not cite dominated convergence when you only have bounded expectations; that is a uniform integrability issue, not automatic domination.",
        ["expectation", "fatou", "mct", "dct"],
    ),
    piece(
        "change_of_variables",
        "1.6 Expected Value",
        "Change of variables formula",
        "theorem",
        "If X has law mu and f is measurable, then E[f(X)] equals the integral of f with respect to mu, when the positive or integrable conditions hold.",
        "Prove for indicators, extend to simple functions, nonnegative functions, and signed integrable functions.",
        "Lets you compute expectations using the distribution rather than the underlying sample space.",
        "Do not assume a density exists; the law may be discrete, continuous, singular, or mixed.",
        ["change-of-variables", "law", "expectation"],
    ),
    piece(
        "tail_sum_nonnegative",
        "1.6 Expected Value",
        "Tail integral and nonnegative expectations",
        "formula",
        "For nonnegative random variables, expectations can often be computed or bounded through tail probabilities.",
        "Write X as an integral of indicators {X > t} and apply Fubini/Tonelli.",
        "Important for moment bounds, heavy-tail examples, and Borel-Cantelli estimates.",
        "Mind strict versus non-strict inequalities only at atoms; the integral is unaffected in many continuous-parameter formulas.",
        ["tail-integral", "nonnegative", "fubini"],
        ["durrett_ch1_fubini_tonelli"],
    ),
    piece(
        "common_distributions_expectations",
        "1.6 Expected Value",
        "Common expectation computations",
        "example-bank",
        "Chapter 1 reviews expectations for exponential, normal, Bernoulli, Poisson, and geometric distributions.",
        "Use densities or mass functions plus the change-of-variables formula; use series identities for discrete distributions.",
        "These examples are quick diagnostic checks for later characteristic-function and limit problems.",
        "Parameterization varies, especially for geometric distributions; state your convention.",
        ["common-distributions", "expectation", "examples"],
    ),
    piece(
        "inclusion_exclusion",
        "1.6 Expected Value",
        "Inclusion-exclusion and Bonferroni",
        "formula",
        "The probability of a finite union can be expanded by alternating sums of intersection probabilities, with Bonferroni inequalities for truncations.",
        "Apply expectation to sums/products of indicator variables.",
        "Useful for event-counting, occupancy-style estimates, and bounding union probabilities more sharply than the union bound.",
        "The exact formula is finite; infinite versions require additional limiting arguments.",
        ["inclusion-exclusion", "bonferroni", "indicators"],
    ),
    piece(
        "product_measure",
        "1.7 Product Measures, Fubini's Theorem",
        "Product measures",
        "definition",
        "Given measure spaces, the product measure is the unique measure on the product sigma-field that agrees with products of measures on measurable rectangles.",
        "Define on rectangles, verify premeasure properties, and extend.",
        "The measure-theoretic basis for joint distributions and independence.",
        "A set in the product sigma-field can be much more complicated than a rectangle.",
        ["product-measure", "rectangles", "joint-law"],
    ),
    piece(
        "sections_measurable",
        "1.7 Product Measures, Fubini's Theorem",
        "Measurable sections",
        "lemma",
        "For a measurable set in a product space, its x-section is measurable in the second space, and section measures are measurable functions of x.",
        "Prove first for rectangles, then close the class under monotone operations.",
        "This is the technical engine behind Fubini and Tonelli.",
        "Do not assume section results for nonmeasurable product subsets.",
        ["sections", "product-space", "measurability"],
    ),
    piece(
        "fubini_tonelli",
        "1.7 Product Measures, Fubini's Theorem",
        "Fubini and Tonelli theorem",
        "theorem",
        "For nonnegative functions, iterated integrals and the product integral agree. For signed functions, the same holds when the absolute integral is finite.",
        "Prove by indicators, simple functions, monotone convergence, then signed decomposition under integrability.",
        "Use to exchange sums/integrals/expectations and compute expectations by conditioning-like iterated integration.",
        "Tonelli handles nonnegative functions even with infinite value; Fubini for signed functions needs integrability.",
        ["fubini", "tonelli", "iterated-integral"],
    ),
    piece(
        "independence_preview",
        "1.7 Product Measures, Fubini's Theorem",
        "Product measures as preview of independence",
        "concept-link",
        "When a joint law factors as a product measure, the coordinates behave independently.",
        "Rectangular probabilities factor, and extension carries this to generated sigma-fields.",
        "This prepares for Chapter 2 independence and for computing expectations of products.",
        "Independence is a statement about the joint law, not merely about marginal distributions.",
        ["product-law", "independence", "joint-distribution"],
    ),
]


SECTION_GUIDES = [
    {
        "section": "1.1 Probability Spaces",
        "study_goal": "Speak fluently about events, sigma-fields, probability measures, and extension from simple generating classes.",
        "must_master": ["probability space", "sigma-field", "continuity of measure", "Stieltjes measure", "semialgebra extension"],
        "prelim_angle": "Often appears as proof scaffolding inside convergence, Borel-Cantelli, and distribution problems rather than as a standalone question.",
    },
    {
        "section": "1.2 Distributions",
        "study_goal": "Move between laws, CDFs, densities/mass functions, atoms, and transformations.",
        "must_master": ["CDF properties", "valid CDF to law", "atoms as jumps", "normal tail bounds"],
        "prelim_angle": "Directly relevant to tightness, weak convergence, and characteristic-function problems.",
    },
    {
        "section": "1.3 Random Variables",
        "study_goal": "Prove measurability quickly using generators and closure under limits/composition.",
        "must_master": ["measurable maps", "generator checking", "arithmetic and limits of random variables", "sigma(X) factorization"],
        "prelim_angle": "Needed whenever an exam asks you to justify conditional expectation, filtrations, or convergence events.",
    },
    {
        "section": "1.4 Integration",
        "study_goal": "Understand Lebesgue integral construction enough to know why the limit theorems work.",
        "must_master": ["simple functions", "nonnegative integral", "positive/negative parts", "linearity"],
        "prelim_angle": "Usually supports expectation proofs; less often tested as pure integration construction.",
    },
    {
        "section": "1.5 Properties of the Integral",
        "study_goal": "Use Jensen, Holder, Minkowski, Fatou, MCT, DCT, and bounded convergence with exact hypotheses.",
        "must_master": ["Jensen", "Holder", "Minkowski", "Fatou", "MCT", "DCT"],
        "prelim_angle": "High-frequency toolkit for bounding probabilities and passing limits under expectations.",
    },
    {
        "section": "1.6 Expected Value",
        "study_goal": "Treat expectation as integration and deploy inequalities/change-of-variables confidently.",
        "must_master": ["linearity", "Markov/Chebyshev", "expectation limit theorems", "change of variables", "tail integral"],
        "prelim_angle": "Central to LLN, CLT, martingale, and random-series problems.",
    },
    {
        "section": "1.7 Product Measures, Fubini's Theorem",
        "study_goal": "Know when iterated integration is legal and how product measures support joint distributions.",
        "must_master": ["product measure", "sections", "Fubini/Tonelli", "product laws"],
        "prelim_angle": "Used in expectation swaps, independence calculations, and conditioning foundations.",
    },
]


def write_jsonl(path: Path, rows):
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    write_jsonl(OUT / "chapter1_knowledge_pieces.jsonl", PIECES)
    write_jsonl(OUT / "chapter1_section_guides.jsonl", SECTION_GUIDES)

    manifest = {
        "name": "durrett_chapter1_probability_foundations_llm_viki",
        "description": "Curated LLM/Viki-style knowledge pieces for Chapter 1 of Durrett Probability: Theory and Examples.",
        "source_file": str(SOURCE),
        "created_at": CREATED,
        "piece_count": len(PIECES),
        "section_count": len(SECTION_GUIDES),
        "files": [
            "chapter1_knowledge_pieces.jsonl",
            "chapter1_section_guides.jsonl",
            "chapter1_viki.md",
            "chapter1_flashcards.tsv",
            "manifest.json",
        ],
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    md = ["# Durrett Chapter 1 LLM Viki: Probability Foundations\n"]
    md.append("Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter1.pdf`.\n")
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
    (OUT / "chapter1_viki.md").write_text("\n".join(md), encoding="utf-8")

    flash = ["id\tfront\tback\ttags"]
    for item in PIECES:
        front = f"{item['title']} ({item['section']})"
        back = f"{item['summary']} Exam use: {item['exam_use']} Pitfall: {item['pitfalls']}"
        flash.append(f"{item['id']}\t{front}\t{back}\t{','.join(item['tags'])}")
    (OUT / "chapter1_flashcards.tsv").write_text("\n".join(flash) + "\n", encoding="utf-8")

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

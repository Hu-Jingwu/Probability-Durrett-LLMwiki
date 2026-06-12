# Durrett Chapter 5 LLM Viki: Markov Chains

Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter5.pdf`.

These are curated study/LLM retrieval pieces, not verbatim textbook notes.

## Section Guides

### 5.1 Examples

- Goal: Recognize Markov structure in standard models and compute their transition probabilities.

- Must master: Markov property, transition matrix, random walk, branching process, Ehrenfest, Wright-Fisher, M/G/1 queue

- Prelim angle: Many exam problems start by asking whether a process is Markov and what its transition law is.

### 5.2 Construction, Markov Properties

- Goal: Use kernels, path-space construction, Markov property, Chapman-Kolmogorov, and strong Markov property.

- Must master: transition kernels, finite-dimensional distributions, shifted Markov property, Chapman-Kolmogorov, strong Markov property, hitting times

- Prelim angle: Strong Markov arguments power almost every hitting-time and recurrence calculation.

### 5.3 Recurrence and Transience

- Goal: Classify states and classes using visits, communication, closed classes, and Lyapunov/scale tools.

- Must master: recurrent vs transient, communication classes, decomposition theorem, Foster criterion, birth-death scale functions

- Prelim angle: Expect problems asking whether a chain returns, escapes, or has recurrent classes.

### 5.4 Recurrence of Random Walks Starred Section

- Goal: Understand dimension-dependent random-walk recurrence through Green functions, limits, and Fourier criteria.

- Must master: Green-function sums, simple random walk by dimension, Chung-Fuchs, Fourier recurrence tests

- Prelim angle: The d<=2 versus d>=3 classification is very high-yield, even if the starred Fourier details are less tested.

### 5.5 Stationary Measures

- Goal: Construct and identify invariant measures, stationary distributions, reversibility, and positive recurrence.

- Must master: stationary measure, detailed balance, cycle condition, return-cycle occupation measure, positive recurrence, mean return time

- Prelim angle: Equilibrium computations usually reduce to detailed balance, normalization, or mean return times.

### 5.6 Asymptotic Behavior

- Goal: Connect recurrence and stationarity to long-run transition probabilities and ergodic averages.

- Must master: renewal limits, period, aperiodic convergence, coupling, additive functional LLN

- Prelim angle: Use irreducible + positive recurrent + aperiodic as the main convergence-to-stationarity checklist.

### 5.7 Periodicity, Tail Sigma-Field Starred Section

- Goal: Handle periodic chains by cyclic classes and understand tail-event zero-one behavior.

- Must master: cyclic classes, periodic convergence, tail sigma-field, coupling zero-one arguments

- Prelim angle: Periodicity is the standard hidden reason a stationary chain does not have ordinary p^n convergence.

### 5.8 General State Space Starred Section

- Goal: Translate countable-state recurrence, stationarity, and convergence to Harris chains.

- Must master: Harris recurrence, small sets, split chain, sigma-finite invariant measure, Harris convergence, GI/G/1 queue

- Prelim angle: Useful for advanced problems with continuous state spaces or queueing recursions.

## Knowledge Pieces

### Countable-state Markov property

- ID: `durrett_ch5_markov_property_countable`

- Section: 5.1 Examples

- Kind: definition

- Summary: A temporally homogeneous countable-state Markov chain satisfies P(X_{n+1}=j | X_n=i, past)=P(X_{n+1}=j | X_n=i)=p(i,j).

- Proof idea: The current state is a sufficient statistic for predicting the next state, so the transition matrix contains all one-step dynamics.

- Exam use: Use this as the first diagnostic for deciding whether a proposed process is Markov and for computing transition probabilities.

- Pitfall: A function of a Markov chain need not be Markov unless the retained state contains enough information.

- Tags: markov-property, transition-matrix, countable-state

### Random walk as a Markov chain

- ID: `durrett_ch5_random_walk_chain`

- Section: 5.1 Examples

- Kind: example-pattern

- Summary: If X_n=X_0+xi_1+...+xi_n with iid increments on Z^d, then p(i,j)=mu({j-i}).

- Proof idea: Condition on X_n; the next state is obtained by adding the independent increment xi_{n+1}.

- Exam use: Use whenever increments are independent and stationary; transition probabilities depend only on displacement.

- Pitfall: A random walk often has no finite equilibrium on infinite groups even though it is Markov.

- Tags: random-walk, increments, translation-invariance

### Branching process transition kernel

- ID: `durrett_ch5_branching_process_chain`

- Section: 5.1 Examples

- Kind: example-pattern

- Summary: For a Galton-Watson process, p(i,j)=P(xi_1+...+xi_i=j), where each current individual independently produces offspring.

- Proof idea: Given X_n=i, the next generation is the sum of i iid offspring counts.

- Exam use: Recognize absorbing extinction state 0 and use generating functions for transition calculations.

- Pitfall: The process is Markov in the population size, but it typically does not converge to a nontrivial equilibrium.

- Tags: branching-process, offspring, absorbing-state

### Ehrenfest urn chain

- ID: `durrett_ch5_ehrenfest_chain`

- Section: 5.1 Examples

- Kind: example-pattern

- Summary: With r balls and state k equal to the number in the first urn, p(k,k+1)=(r-k)/r and p(k,k-1)=k/r.

- Proof idea: One randomly selected ball changes urns, increasing or decreasing k according to which urn the ball came from.

- Exam use: A canonical finite birth-death chain for reversibility, stationary distributions, and periodicity.

- Pitfall: The chain alternates parity, so convergence of p^n(k,j) must account for period 2 unless laziness is added.

- Tags: ehrenfest, birth-death, finite-chain, periodicity

### Wright-Fisher transition law

- ID: `durrett_ch5_wright_fisher_chain`

- Section: 5.1 Examples

- Kind: example-pattern

- Summary: In a population of N genes, the number of A alleles has binomial transition p(i,j)=C(N,j) rho_i^j(1-rho_i)^{N-j}; without mutation rho_i=i/N, with mutation rho_i=(i/N)(1-u)+((N-i)/N)v.

- Proof idea: The next generation is sampled with replacement from the current generation, with mutation modifying the success probability.

- Exam use: Use for absorption/fixation problems, martingale hitting probabilities, and finite-chain equilibrium with mutation.

- Pitfall: Without mutation, 0 and N are absorbing; with positive mutation rates they are not.

- Tags: wright-fisher, binomial-transition, mutation, absorption

### M/G/1 embedded queue chain

- ID: `durrett_ch5_mg1_queue_chain`

- Section: 5.1 Examples

- Kind: example-pattern

- Summary: At service-start epochs, X_{n+1}=(X_n+xi_{n+1})^+, where P(xi=k-1)=a_k and a_k is the chance k arrivals occur during one service time.

- Proof idea: Between service starts, arrivals during the service time add customers while the served customer leaves; the positive part handles an empty queue.

- Exam use: Use drift E xi=mean arrivals per service minus 1 to classify recurrence and stability.

- Pitfall: Do not confuse the continuous-time queue with the embedded discrete chain at service-start times.

- Tags: queue, mg1, reflected-random-walk, drift

### General transition probability

- ID: `durrett_ch5_general_transition_probability`

- Section: 5.2 Construction, Markov Properties

- Kind: definition

- Summary: On a measurable state space, p(x,A) is a transition probability when A -> p(x,A) is a probability measure and x -> p(x,A) is measurable.

- Proof idea: The two requirements make integration over paths well-defined and allow conditioning on X_n.

- Exam use: Use this language for chains beyond countable state spaces, including queues and continuous densities.

- Pitfall: For general spaces, p(x,y) is usually not a number; the kernel is p(x,A).

- Tags: transition-kernel, measurable-space, general-state-space

### Finite-dimensional construction of a chain

- ID: `durrett_ch5_finite_dimensional_construction`

- Section: 5.2 Construction, Markov Properties

- Kind: construction

- Summary: Given initial law mu and kernel p, the finite-dimensional laws are iterated integrals mu(dx_0)p(x_0,dx_1)...p(x_{n-1},dx_n).

- Proof idea: The consistency of these marginals lets the extension theorem create a path-space process.

- Exam use: Justifies statements that a Markov chain with a specified initial distribution and transition kernel exists.

- Pitfall: The formula gives path probabilities only for measurable cylinder events, then extension supplies the full path law.

- Tags: construction, finite-dimensional-distributions, path-space

### Transition operator notation

- ID: `durrett_ch5_expectation_operator_notation`

- Section: 5.2 Construction, Markov Properties

- Kind: notation

- Summary: For bounded measurable f, Pf(x)=E_x f(X_1)=integral f(y)p(x,dy); iterates P^n describe n-step expectations.

- Proof idea: Integrating one step at a time turns the transition kernel into a linear operator.

- Exam use: Useful for harmonic equations, hitting probabilities, expected hitting times, and martingale checks.

- Pitfall: The same symbol p may denote a kernel or a matrix; P as an operator acts on functions.

- Tags: transition-operator, expectation, harmonic-functions

### Markov property with path shifts

- ID: `durrett_ch5_markov_property_shift`

- Section: 5.2 Construction, Markov Properties

- Kind: theorem

- Summary: For bounded future functionals Y, E_x[Y o theta_n | F_n]=E_{X_n}Y.

- Proof idea: Check cylinder future events, extend by a monotone-class argument, and use the construction formula.

- Exam use: Transforms future-path questions after time n into a fresh chain started at X_n.

- Pitfall: The future functional must be evaluated on the shifted path; forgetting the shift changes the event.

- Tags: markov-property, shift-operator, monotone-class

### Chapman-Kolmogorov equations

- ID: `durrett_ch5_chapman_kolmogorov`

- Section: 5.2 Construction, Markov Properties

- Kind: theorem

- Summary: The n-step kernels satisfy p^{m+n}(x,z)=sum_y p^m(x,y)p^n(y,z) in countable spaces, with the analogous integral formula in general spaces.

- Proof idea: Condition on the state at the intermediate time m and apply the Markov property.

- Exam use: Compute multi-step transitions, prove communication, and derive renewal decompositions for return probabilities.

- Pitfall: For general spaces, replace sums over y by integration against p^m(x,dy).

- Tags: chapman-kolmogorov, n-step-transition, semigroup

### Strong Markov property

- ID: `durrett_ch5_strong_markov_property`

- Section: 5.2 Construction, Markov Properties

- Kind: theorem

- Summary: At a stopping time T, the post-T process behaves like a fresh chain started from X_T on the event T<infinity.

- Proof idea: Approximate the stopping time by its atoms {T=n}, apply the ordinary Markov property on each atom, and sum.

- Exam use: The main engine for hitting-time decompositions, renewal arguments, recurrence proofs, and reflection arguments.

- Pitfall: T must be a stopping time; optional-looking random times that see the future do not qualify.

- Tags: strong-markov, stopping-time, hitting-times

### Hitting and return time decomposition

- ID: `durrett_ch5_hitting_return_decomposition`

- Section: 5.2 Construction, Markov Properties

- Kind: proof-template

- Summary: Events involving visits to a state or set can be decomposed at the first hitting time and restarted by the strong Markov property.

- Proof idea: Split according to T_y=k or T_A=k, then apply the strong Markov property to the shifted future.

- Exam use: Use for equations like P_x(T_z<infinity) >= P_x(T_y<infinity)P_y(T_z<infinity) and for first-step analysis.

- Pitfall: Use T_y=inf{n>=1:X_n=y} for returns and V_A=inf{n>=0:X_n in A} for entrance; the indexing matters.

- Tags: hitting-time, return-time, first-step-analysis

### Reflection principle for symmetric random walk

- ID: `durrett_ch5_reflection_principle`

- Section: 5.2 Construction, Markov Properties

- Kind: theorem

- Summary: For one-dimensional simple symmetric random walk, paths crossing a level can be reflected after the first hitting time to convert maximum events into endpoint events.

- Proof idea: Stop at the first hit of the barrier and flip the signs of all later increments, giving a bijection of path sets.

- Exam use: Fast route to distributions of maxima and hitting probabilities for simple random walk.

- Pitfall: The clean reflection bijection uses symmetry and nearest-neighbor increments; it does not transfer unchanged to arbitrary walks.

- Tags: reflection-principle, simple-random-walk, maximum

### Expected visits criterion

- ID: `durrett_ch5_recurrence_visit_criterion`

- Section: 5.3 Recurrence and Transience

- Kind: theorem

- Summary: A state y is recurrent iff E_y N(y)=sum_n p^n(y,y)=infinity; if transient this expected visit count is finite.

- Proof idea: After each return to y, the strong Markov property restarts the process, so the number of returns has a geometric structure.

- Exam use: Use Green-function sums to classify states, especially for random walks.

- Pitfall: The criterion is for visits starting from y; from another x, accessibility must be handled separately.

- Tags: recurrence, transience, green-function, return-count

### Recurrence transfers through communication

- ID: `durrett_ch5_communication_recurrence_transfer`

- Section: 5.3 Recurrence and Transience

- Kind: theorem

- Summary: If x is recurrent and rho_xy>0, then y is recurrent and rho_yx=1.

- Proof idea: A recurrent x is visited infinitely often; successful excursions from x to y eventually occur, and returning to x forces y to communicate back.

- Exam use: Shows recurrence is a class property inside communicating classes.

- Pitfall: Accessibility in only one direction is not symmetric unless recurrence is known.

- Tags: communication, recurrence-class, irreducibility

### Finite closed classes contain recurrent states

- ID: `durrett_ch5_finite_closed_recurrent_class`

- Section: 5.3 Recurrence and Transience

- Kind: theorem

- Summary: Every finite closed set contains a recurrent state; if the finite closed set is irreducible, all its states are recurrent.

- Proof idea: A chain trapped in a finite set must visit at least one state infinitely often, then recurrence transfers through communication.

- Exam use: Use to classify finite Markov chains and prove absorbing/recurrent structure.

- Pitfall: The set must be closed; otherwise the chain can leave and never return.

- Tags: finite-chain, closed-class, recurrence

### Decomposition theorem

- ID: `durrett_ch5_decomposition_theorem`

- Section: 5.3 Recurrence and Transience

- Kind: theorem

- Summary: The recurrent states split into disjoint irreducible closed classes, while every transient state is visited only finitely often almost surely.

- Proof idea: Use communication equivalence for recurrent states and the finite expected visits criterion for transients.

- Exam use: Organizes the long-run behavior of countable chains before stationary distributions enter.

- Pitfall: Closed recurrent classes need not be finite; irreducibility is within each class, not necessarily the whole state space.

- Tags: decomposition, recurrent-classes, transient-states

### Foster-type recurrence criterion

- ID: `durrett_ch5_foster_supermartingale_recurrence`

- Section: 5.3 Recurrence and Transience

- Kind: criterion

- Summary: For an irreducible chain, a nonnegative function phi with E_x phi(X_1)<=phi(x) off a finite set and phi(x)->infinity can force recurrence.

- Proof idea: Stop phi(X_n) on leaving large finite regions and use optional-stopping/supermartingale estimates to prevent escape to infinity.

- Exam use: A powerful recurrence test for birth-death chains, queues, and chains with inward drift.

- Pitfall: Check the direction of drift carefully; superharmonic behavior outside a finite set is the recurrence signal.

- Tags: foster-criterion, supermartingale, lyapunov, recurrence

### Birth-death scale function

- ID: `durrett_ch5_birth_death_scale_function`

- Section: 5.3 Recurrence and Transience

- Kind: formula

- Summary: For a birth-death chain, harmonic scale functions solve p_x h(x+1)+q_x h(x-1)=h(x) and give explicit two-sided hitting probabilities.

- Proof idea: Rewrite the harmonic equation in first differences so ratios telescope as products q_i/p_i.

- Exam use: Use for gambler's ruin probabilities and recurrence tests on {0,1,2,...}.

- Pitfall: Boundary conventions at 0 matter; write the model's p_0 and q_0 before applying formulas.

- Tags: birth-death, scale-function, hitting-probability

### Birth-death recurrence test

- ID: `durrett_ch5_birth_death_recurrence_test`

- Section: 5.3 Recurrence and Transience

- Kind: criterion

- Summary: For a birth-death chain on nonnegative integers, recurrence of 0 is determined by divergence of the scale sum built from products q_i/p_i.

- Proof idea: Let the upper boundary M tend to infinity in the two-sided hitting formula.

- Exam use: High-yield test for nearest-neighbor chains with state-dependent drift.

- Pitfall: Small asymptotic drift terms such as C/j can decide the boundary between recurrence and transience.

- Tags: birth-death, recurrence-test, scale-sum

### Recurrent values form a closed subgroup

- ID: `durrett_ch5_random_walk_recurrent_values`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: For a random walk on R^d, the set of recurrent values is either empty or a closed subgroup of R^d.

- Proof idea: Use independence and translation invariance to show the set is closed under differences and limits.

- Exam use: Clarifies what recurrence can mean outside lattice state spaces.

- Pitfall: Returning near a value is a topological notion in R^d, not necessarily exact equality.

- Tags: random-walk, recurrent-values, closed-subgroup

### Equivalent random-walk recurrence criteria

- ID: `durrett_ch5_random_walk_recurrence_equivalences`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: For random walks, recurrence can be characterized by infinitely many visits to neighborhoods, divergence of occupation sums, and Green-function criteria.

- Proof idea: Relate neighborhood visits to the Markov property and use zero-one/renewal arguments.

- Exam use: Choose the criterion that matches the data: local probabilities, characteristic functions, or limit theorems.

- Pitfall: The exact form differs between lattice and nonlattice settings; keep the state-space topology visible.

- Tags: random-walk, recurrence-criteria, green-function

### Simple random walk recurrence by dimension

- ID: `durrett_ch5_simple_random_walk_dimension`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: Simple random walk is recurrent in dimensions 1 and 2 and transient in dimensions 3 and higher.

- Proof idea: Estimate the return probabilities: they behave like n^{-d/2}, whose series diverges for d<=2 and converges for d>=3.

- Exam use: A central classification result and a common comparison model for Markov-chain recurrence.

- Pitfall: Parity affects exact return times but not the convergence/divergence classification.

- Tags: simple-random-walk, dimension, recurrence, transience

### Chung-Fuchs one-dimensional recurrence pattern

- ID: `durrett_ch5_chung_fuchs_one_dimension`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: In one dimension, centered weak-law behavior is the key condition behind recurrence for broad random walks.

- Proof idea: Use truncation and characteristic-function/Fourier criteria to control occupation near the origin.

- Exam use: Use when increments are not nearest-neighbor but have no drift on the natural scale.

- Pitfall: Nonzero drift typically pushes the walk to infinity and destroys recurrence.

- Tags: chung-fuchs, one-dimensional-random-walk, drift

### Two-dimensional normal-limit recurrence

- ID: `durrett_ch5_two_dimensional_normal_recurrence`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: A two-dimensional random walk with S_n/sqrt(n) converging to a nondegenerate normal law is recurrent.

- Proof idea: Use the local/weak normal approximation to show enough mass returns to fixed neighborhoods for the occupation sum to diverge.

- Exam use: Recognize recurrence for centered finite-variance planar walks.

- Pitfall: A degenerate limiting covariance needs separate lower-dimensional analysis.

- Tags: two-dimensional-random-walk, normal-limit, recurrence

### Fourier recurrence criterion

- ID: `durrett_ch5_fourier_recurrence_criterion`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: criterion

- Summary: Random-walk recurrence can be tested through integrals involving 1/(1-phi(t)), where phi is the increment characteristic function.

- Proof idea: Parseval-type identities convert occupation sums into Fourier integrals over powers of phi.

- Exam use: Useful for non-nearest-neighbor walks and for proving no truly three-dimensional walk is recurrent.

- Pitfall: The singularity near t=0 is decisive; away from zero the integral is usually harmless.

- Tags: fourier, characteristic-functions, recurrence

### No truly three-dimensional recurrent random walk

- ID: `durrett_ch5_no_truly_three_dimensional_recurrence`

- Section: 5.4 Recurrence of Random Walks Starred Section

- Kind: theorem

- Summary: A random walk with genuinely three-dimensional increment support cannot be recurrent.

- Proof idea: Near the origin, the Fourier denominator behaves too singularly in dimension 3 for recurrence-compatible divergence.

- Exam use: Use as a broad transience result beyond simple random walk.

- Pitfall: If the walk actually lives in a lower-dimensional subgroup, reduce the dimension before applying the theorem.

- Tags: three-dimensional, random-walk, transience, fourier

### Stationary measures and distributions

- ID: `durrett_ch5_stationary_measure_definition`

- Section: 5.5 Stationary Measures

- Kind: definition

- Summary: A measure mu is stationary when mu p=mu; if mu(S)=1 it is a stationary distribution.

- Proof idea: Stationarity says one transition step leaves the law unchanged.

- Exam use: Find equilibria, normalize invariant measures, and connect long-run proportions to return times.

- Pitfall: An infinite stationary measure need not be a probability distribution and does not by itself imply equilibrium probabilities.

- Tags: stationary-measure, invariant-measure, equilibrium

### Reversibility and detailed balance

- ID: `durrett_ch5_reversibility_detailed_balance`

- Section: 5.5 Stationary Measures

- Kind: criterion

- Summary: If mu(x)p(x,y)=mu(y)p(y,x) for all x,y, then mu is stationary and the chain is reversible under mu.

- Proof idea: Sum the detailed-balance identity over x to get stationarity; path probabilities are unchanged by time reversal.

- Exam use: The fastest way to find stationary distributions for birth-death, Ehrenfest, and many urn chains.

- Pitfall: Detailed balance is sufficient but not necessary for stationarity unless reversibility is required.

- Tags: reversibility, detailed-balance, stationary-distribution

### Kolmogorov cycle condition

- ID: `durrett_ch5_kolmogorov_cycle_condition`

- Section: 5.5 Stationary Measures

- Kind: theorem

- Summary: For an irreducible chain, reversibility is characterized by equality of transition-probability products around every directed cycle and its reverse.

- Proof idea: Multiply detailed-balance equations around a cycle for necessity; construct ratios along paths for sufficiency.

- Exam use: Use to test whether a proposed chain can be reversible without solving for pi first.

- Pitfall: The condition is about all cycles; checking only two-state moves can miss circulation.

- Tags: kolmogorov-cycle, reversibility, cycles

### Stationary measure from one recurrent cycle

- ID: `durrett_ch5_stationary_measure_from_returns`

- Section: 5.5 Stationary Measures

- Kind: theorem

- Summary: If x is recurrent and T_x is the first positive return time, then expected occupation counts before T_x define a stationary measure with mass 1 at x.

- Proof idea: Use the strong Markov property to balance expected exits and entries over a regenerative cycle.

- Exam use: Construct invariant measures for recurrent irreducible chains without guessing.

- Pitfall: The measure may have infinite total mass when the chain is null recurrent.

- Tags: occupation-measure, regeneration, stationary-measure, return-time

### Uniqueness of stationary measure in irreducible recurrent chains

- ID: `durrett_ch5_stationary_measure_uniqueness_recurrent`

- Section: 5.5 Stationary Measures

- Kind: theorem

- Summary: For an irreducible recurrent countable chain, the stationary measure is unique up to constant multiples.

- Proof idea: Compare any invariant measure with the regenerative occupation measure normalized at one state.

- Exam use: Lets you identify all invariant measures once one candidate is found.

- Pitfall: Uniqueness up to scale does not mean a stationary distribution exists; total mass may be infinite.

- Tags: irreducible, recurrent, stationary-measure, uniqueness

### Stationary probability and mean return time

- ID: `durrett_ch5_positive_recurrence_return_time`

- Section: 5.5 Stationary Measures

- Kind: theorem

- Summary: For an irreducible chain with stationary distribution pi, pi(y)=1/E_y T_y, so states with finite mean return time are positive recurrent.

- Proof idea: Apply the regenerative stationary measure over one return cycle and normalize by its total expected length.

- Exam use: Compute stationary probabilities through expected return times and classify positive versus null recurrence.

- Pitfall: Recurrence only says T_y is finite almost surely; positive recurrence requires finite expectation.

- Tags: positive-recurrence, mean-return-time, stationary-distribution

### Positive recurrence equivalences

- ID: `durrett_ch5_positive_recurrence_equivalences`

- Section: 5.5 Stationary Measures

- Kind: theorem

- Summary: For an irreducible chain, existence of a stationary distribution, finite mean return times, and positive recurrence are equivalent.

- Proof idea: Normalize the recurrent-cycle stationary measure when its total mass is finite; conversely use stationarity to derive finite return times.

- Exam use: A standard checklist for proving an irreducible chain has an equilibrium law.

- Pitfall: In infinite state spaces, irreducible recurrent chains can be null recurrent and fail to have a stationary distribution.

- Tags: positive-recurrence, stationary-distribution, return-times

### Birth-death stationary distribution

- ID: `durrett_ch5_birth_death_stationary_distribution`

- Section: 5.5 Stationary Measures

- Kind: formula

- Summary: For birth-death chains, detailed balance gives pi(x) proportional to products of birth rates divided by death rates, if the normalizing sum is finite.

- Proof idea: Solve pi(x)p_x=pi(x+1)q_{x+1} recursively and normalize.

- Exam use: Fast equilibrium computation for queues, Ehrenfest-type chains, and one-dimensional population models.

- Pitfall: The unnormalized weights may define an invariant measure even when their sum diverges.

- Tags: birth-death, stationary-distribution, detailed-balance

### M/G/1 stability and stationarity

- ID: `durrett_ch5_mg1_stability_stationarity`

- Section: 5.5 Stationary Measures

- Kind: example-pattern

- Summary: For the embedded M/G/1 queue, stability/positive recurrence occurs when the mean number of arrivals during one service time is less than 1.

- Proof idea: Compare the reflected queue length to a random walk with drift E xi=mu-1 and use recurrence/return-time arguments.

- Exam use: Use drift less than zero as the queue stability condition.

- Pitfall: Recurrence and stationary behavior fail at or above critical load in different ways; do not treat mu=1 as stable.

- Tags: mg1, queue-stability, positive-recurrence, drift

### Renewal limit for return probabilities

- ID: `durrett_ch5_renewal_limit_return_probabilities`

- Section: 5.6 Asymptotic Behavior

- Kind: theorem

- Summary: If y is recurrent, then p^n(y,y) has asymptotics governed by the renewal theorem for the return-time distribution; positive recurrence gives limits tied to 1/E_y T_y.

- Proof idea: Decompose visits to y into renewals generated by successive return times.

- Exam use: Explains why return-time periods and mean cycle lengths control long-run transition probabilities.

- Pitfall: Periodicity can force p^n(y,y)=0 on many n, so limits may only exist along arithmetic subsequences.

- Tags: renewal-theorem, return-probabilities, asymptotics

### Period of a state

- ID: `durrett_ch5_period_definition`

- Section: 5.6 Asymptotic Behavior

- Kind: definition

- Summary: The period of state x is the greatest common divisor of {n>=1:p^n(x,x)>0}; irreducible communicating states share the same period.

- Proof idea: Use concatenation of paths and communication to transfer possible return-time arithmetic between states.

- Exam use: Check whether convergence to stationarity can hold at every time or only along residue classes.

- Pitfall: A chain can be irreducible and positive recurrent but still fail ordinary convergence because of period greater than 1.

- Tags: periodicity, aperiodic, irreducibility

### Aperiodic convergence theorem

- ID: `durrett_ch5_aperiodic_convergence_theorem`

- Section: 5.6 Asymptotic Behavior

- Kind: theorem

- Summary: If a countable chain is irreducible, aperiodic, and has stationary distribution pi, then p^n(x,y) -> pi(y).

- Proof idea: Couple two independent chains through the product chain and show they meet with probability tending to one.

- Exam use: Main equilibrium convergence theorem for prelim Markov-chain problems.

- Pitfall: Irreducible and stationary are not enough; without aperiodicity the raw n-step probabilities may oscillate.

- Tags: convergence-to-stationarity, aperiodic, coupling, positive-recurrence

### Coupling bound for convergence

- ID: `durrett_ch5_coupling_for_finite_chains`

- Section: 5.6 Asymptotic Behavior

- Kind: proof-template

- Summary: If two copies of a Markov chain are run together after meeting, then total variation distance is bounded by the probability their coupling time exceeds n.

- Proof idea: Construct the product chain, make the two coordinates coalesce at the diagonal, and compare events before and after meeting.

- Exam use: Use for finite irreducible aperiodic chains and for quantitative convergence estimates.

- Pitfall: The coupling must preserve the correct marginal transition law for each coordinate.

- Tags: coupling, total-variation, mixing

### Strong law for additive functionals

- ID: `durrett_ch5_additive_functional_lln`

- Section: 5.6 Asymptotic Behavior

- Kind: theorem

- Summary: For an irreducible positive recurrent chain with stationary law pi, time averages of suitable f(X_n) converge to sum_x pi(x)f(x).

- Proof idea: Break the path into regenerative cycles between visits to a reference state and apply iid cycle laws.

- Exam use: Use to turn long-run sample averages into stationary expectations.

- Pitfall: Integrability under pi is essential; positive recurrence alone does not control arbitrary unbounded rewards.

- Tags: ergodic-theorem, additive-functional, time-average

### Periodic cyclic classes

- ID: `durrett_ch5_periodic_convergence_classes`

- Section: 5.7 Periodicity, Tail Sigma-Field Starred Section

- Kind: theorem

- Summary: For an irreducible recurrent chain of period d, the state space splits into d cyclic classes and the d-step chain on each class is aperiodic.

- Proof idea: Group states according to hitting-time residues modulo d and use the gcd definition of period.

- Exam use: Use to repair convergence statements for periodic chains by passing to subsequences n congruent to r mod d.

- Pitfall: The stationary distribution is still a distribution on all states, but mass is visited cyclically rather than approached at all times.

- Tags: periodicity, cyclic-classes, periodic-convergence

### Periodic convergence theorem

- ID: `durrett_ch5_periodic_convergence_theorem`

- Section: 5.7 Periodicity, Tail Sigma-Field Starred Section

- Kind: theorem

- Summary: For irreducible positive recurrent chains with period d, p^n(x,y) converges along the compatible residue class to d*pi(y) and is zero on incompatible residues.

- Proof idea: Apply the aperiodic convergence theorem to the d-step chain on the cyclic class containing y.

- Exam use: Use when examples such as simple random walk on bipartite graphs oscillate forever.

- Pitfall: The factor d appears because the d-step chain's stationary law is pi restricted to one cyclic class and renormalized.

- Tags: periodic-convergence, cyclic-classes, stationary-distribution

### Tail sigma-field triviality via coupling

- ID: `durrett_ch5_tail_sigma_field_triviality_pattern`

- Section: 5.7 Periodicity, Tail Sigma-Field Starred Section

- Kind: proof-template

- Summary: For suitable irreducible recurrent chains, tail events have probability 0 or 1 because coupled copies eventually share the same future behavior.

- Proof idea: Represent two copies, couple them after a meeting or cyclic alignment, and observe that tail events are unchanged by finite initial segments.

- Exam use: Use for zero-one laws about eventual behavior of recurrent Markov chains and simple random walk.

- Pitfall: Tail events are not the same as invariant events at a fixed time; they ignore every finite prefix.

- Tags: tail-sigma-field, zero-one-law, coupling

### Harris recurrence

- ID: `durrett_ch5_harris_recurrence`

- Section: 5.8 General State Space Starred Section

- Kind: definition

- Summary: A general-state Markov chain is Harris recurrent when it repeatedly hits every set of positive reference measure from relevant starting points.

- Proof idea: A reference measure replaces countable-state point accessibility, letting recurrence be stated for measurable sets.

- Exam use: Use as the general-state analogue of irreducible recurrence.

- Pitfall: In continuous spaces, single points often have probability zero, so point-return definitions are too strong or meaningless.

- Tags: harris-recurrence, general-state-space, reference-measure

### Small sets and split-chain idea

- ID: `durrett_ch5_small_set_split_chain`

- Section: 5.8 General State Space Starred Section

- Kind: construction

- Summary: A small set has a minorization that lets one split transitions into regeneration attempts and residual motion.

- Proof idea: Use the minorization to add an artificial atom, reducing parts of the general-state chain to countable-style regeneration.

- Exam use: The conceptual bridge from countable recurrent-chain proofs to Harris-chain stationary and convergence theorems.

- Pitfall: Minorization is a structural condition; it is not just positive probability of hitting a set.

- Tags: small-set, minorization, split-chain, regeneration

### Stationary measure for recurrent Harris chains

- ID: `durrett_ch5_harris_stationary_measure`

- Section: 5.8 General State Space Starred Section

- Kind: theorem

- Summary: In the recurrent Harris setting, there is a sigma-finite stationary measure, and it is unique up to scale under the appropriate irreducibility assumptions.

- Proof idea: Construct a regenerative stationary measure using the split chain and then project back to the original chain.

- Exam use: Generalizes countable-state invariant-measure construction to continuous state spaces.

- Pitfall: Sigma-finite stationary measure is not automatically a stationary distribution; total mass decides positive recurrence.

- Tags: harris-chain, stationary-measure, sigma-finite, regeneration

### Aperiodic Harris convergence theorem

- ID: `durrett_ch5_harris_convergence_theorem`

- Section: 5.8 General State Space Starred Section

- Kind: theorem

- Summary: An aperiodic positive recurrent Harris chain with stationary distribution converges to that stationary distribution in total variation from suitable starting laws.

- Proof idea: Use split-chain regeneration and coupling, paralleling the countable-state aperiodic convergence proof.

- Exam use: Use for continuous-state Markov models where transition densities make pointwise matrix methods unavailable.

- Pitfall: The theorem requires Harris recurrence and aperiodicity; a stationary density alone may not give convergence from every start.

- Tags: harris-chain, total-variation, convergence, aperiodic

### GI/G/1 queue as a reflected random walk

- ID: `durrett_ch5_gig1_queue_storage_model`

- Section: 5.8 General State Space Starred Section

- Kind: example-pattern

- Summary: The waiting-time recursion W_{n+1}=(W_n+eta_n-zeta_n)^+ is a general-state Markov chain and storage model.

- Proof idea: Service requirements add workload and interarrival times subtract available service time, with reflection at zero.

- Exam use: Use drift E eta < E zeta for stability and Harris-chain tools for stationary waiting-time distributions.

- Pitfall: The embedded workload is continuous-state, so countable transition-matrix formulas do not apply directly.

- Tags: gig1, storage-model, reflected-random-walk, harris-chain

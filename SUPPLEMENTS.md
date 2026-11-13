# Targeted supplementary subjects and resources

## Selection policy

Use an identified diagnostic or proof gap to choose a specific subject and then
one resource. Prefer the learner's owned physical books when they address it;
lectures or another explanation can be a better fit for a particular obstacle.
Assign exact sections, lecture segments, and exercises when reaching the unit,
after verifying them. No additional complete course or book is automatically
required. See [ASSESSMENT.md](ASSESSMENT.md) for diagnostic and exercise selection.

The learner is open to purchasing a useful physical book. Recommend a purchase
with its learning purpose and overlap with owned material, but do not assume a
purchase or add it to the owned-book inventory. New resources below are options.
Digital links are to authors, publishers, or institutions that provide or link
the material legitimately. Check editions and current access when assigning it;
online access is not inferred from a third-party PDF search result.

## Owned references by subject

| Subject or diagnosed gap | Owned starting point | Intended use |
|---|---|---|
| Proofs, quantifiers, induction, relations | Eccles; Epp; Fletcher and Patty; Pinter for sets | Choose focused prerequisites and exercises, not another full foundations sequence |
| Linear algebra | Anton and Rorres, ninth edition | Subspaces, symmetry, PSD, inner products, spectral and variational reasoning as available; verify exact coverage |
| Basic probability/statistics | Epp and Triola, third edition | Check actual coverage; do not assume a statistics text covers all probability needed for random-graph proofs |
| Graph algorithms | CLRS, fourth edition; van Steen | Algorithm assumptions, correctness, and applied graph context under the task-specific disclosure rules |
| Numerical reasoning | Chapra and Canale, sixth edition; Dubin or Hassani selectively | Conditioning, residuals, sparse/dense representations, and numerical-versus-mathematical error |
| Oscillators and circuits | Taylor, Chapter 11; Barnaal; Griffiths for targeted context | Equations, units, conservation, and boundary assumptions |
| Random walks and physical interpretation | Sethna; Anton and Rorres where applicable | Locate actual relevant sections; bridge gaps without assuming complete Markov-chain coverage |
| Analysis and inequalities | Pugh; Rudin; Strauss for diffusion/boundaries | A particular proof's norms, limits, inequality, or evolution equation rather than an additional full analysis curriculum |
| Algebra and topology | Beachy and Blair; Gamelin and Greene; other owned geometry texts as needed | Prerequisites for actual graph constructions or topological arguments |
| Domain models | Kleppmann, OSTEP, TCP/IP Illustrated; Rios where relevant | Interpret dependency, data, network, or systems assumptions without replacing graph reasoning |

The personal inventory at `/home/eruzek/git/library/books.csv` remains separate.
This menu does not claim that each starting point contains every listed topic.

## Proofs and discrete mathematics: lecture alternative

[MIT 6.042J, Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/)
provides institution-hosted material on proofs, discrete structures, counting,
and discrete probability, with access to its open textbook and learning resources.
Use a relevant segment when it addresses a diagnosed gap in the early units or
before random graphs. Existing Eccles/Epp may already suffice. Choose problems
and explanations so an accompanying solution does not reveal a current exercise.

## Linear algebra: lecture alternative

[MIT 18.06, Gilbert Strang's Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
provides lectures, assignments, and exams alongside matrix, eigenvalue, and
positive-definiteness material. Use targeted lectures to support Anton-Rorres
and the graph/physics bridge. Check actual lecture coverage before assigning a
variational argument; not every advanced Chung prerequisite is assumed covered.

## Probability: a possible physical-book addition

**Joseph K. Blitzstein and Jessica Hwang, Introduction to Probability, second
edition** is a candidate purchase if diagnostics show that existing probability
references leave important gaps. Its role would be a coherent probability
foundation for random graphs and later walks, not another graph theory text.
The [publisher's print listing](https://www.routledge.com/Introduction-to-Probability--Second-Edition/Blitzstein-Hwang/p/book/9781138369917)
identifies the edition; [Harvard Stat 110](https://stat110.hsites.harvard.edu/)
links the authors' authorized free online version, print options, and lecture
videos. Try a relevant explanation before deciding whether to buy it.

Select material on the actual prerequisite gap: counting/probability models,
conditional probability and independence, random variables, expectation/variance,
or elementary bounds. Exact sections and exercises are chosen and verified when
needed. Prefer this book/course pairing if it fits; an alternative is
[MIT 6.041SC, Probabilistic Systems Analysis and Applied Probability](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/),
which supplies lectures and independent-study practice. These are alternatives,
not parallel course assignments. Keep linked solutions separate from independent
practice and quiz attempts.

## Finite-state chains: a targeted later reference

**David A. Levin and Yuval Peres, Markov Chains and Mixing Times, second edition,
with contributions by Elizabeth L. Wilmer** can fill an actual finite-state or
convergence gap. The [author's university page](https://pages.uoregon.edu/dlevin/MARKOV/)
provides a legitimate second-edition PDF, errata, and purchase links.
Use selected introductory portions before choosing later mixing material;
this is not a replacement for first-course probability or a required fourth
core book. Consider a physical purchase only if sustained use justifies it.

Diagnose transition conventions, stationary distributions, reversibility,
irreducibility, periodicity, and convergence distinctions before Chung's walk
work. Supplement owned sources only for the gaps they actually leave. Verify
the exact statement and section before making an assignment.

## Spectral explanations and applications

For a spectral explanation or application, [Daniel Spielman's Yale course
materials](https://www.cs.yale.edu/homes/spielman/462/462schedule.html) link
lecture notes and an author-provided book draft. Use a verified relevant passage
to support Chung, the variational bridge, or a physical-network example. Compare
operator conventions explicitly; these materials do not replace assigned Chung
sections or require using the course's implementation language.

## Assignment and review record

Use the relevant lab notes rather than another progress system. Record the
diagnostic gap, selected resource and verified segment, expected learning
evidence, effort estimate, attempts, assistance, actual outcome, and remaining
questions. Use one focused resource first; add another only with a clear reason.
Full Diestel and Chung coverage remains as mapped in [COVERAGE.md](COVERAGE.md).

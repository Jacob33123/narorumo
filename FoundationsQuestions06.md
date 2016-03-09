# One #
Let Σ be a finite alphabet. Prove that Σ∗ is a countable set.

# Two #
Let δ be the transition function of a deterministic finite-state automaton M = (Q, Σ, δ, q0 , F ): δ : Q × Σ → Q.

Consider the extension δ-hat : Q × Σ∗ → Q, of δ, defined by δ-hat(q, epsilon) = q, for a ∈ Σ. δ-hat(q, aw) = δ-hat(δ(q, a), w).
  * Prove that δ(q, a) = δ(q, a) for all q ∈ Q, a ∈ Σ.
  * Prove by induction on strings that for each pair of strings x, y ∈ Σ∗ and state q ∈ Q, δ-hat(q, xy) = δ-hat(δ-hat(q, x), y).

# Three #
Let Σ be an alphabet. For a ∈ Σ, let #a : Σ∗ → N be the function that gives the number of times the character a occurs in the input string.
  * Prove that L = {w ∈ {a, b}∗ | #a (w) = #b (w)} is not regular.
  * Show that L is context-free. (You need not prove that your construction yields L.)

# Four #
  * Show that the class of context-free languages is closed under set union.
  * Show that the class of context-free languages is not closed under set intersection.

# Five #
Let LCFL = { M | M a Turing machine that accepts a context-free language }.
Prove that LCFL is undecidable. Your proof can not make use of Rice’s
Theorem. [Hint: use a reduction argument.]

# Six #
Let ADFA = { M, w | M a deterministic finite-state automaton that accepts string w }
  * Outline a proof that ADFA is decidable in polynomial time.
  * Prove that ADFA is not accepted by a finite-state automaton.

# Seven #
Let a “funny graph” be a finite directed-graph where each vertex is either “square” or “circular” (but not both), and each edge is between a square vertex and a circular vertex (in either order). Prove that the following problem is NP-complete.

Given a funny graph, is there a way to color the circular vertices red or green, so that every square vertex either has an out-edge to a green vertex, or an in-edge from a red vertex.
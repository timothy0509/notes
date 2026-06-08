---
tags:
  - math
  - module-2
  - extended-part
  - induction
  - foundation-knowledge
---

# Mathematical Induction

## First Principle of Mathematical Induction

To prove a proposition $P(n)$ for all positive integers $n$:

1. **Base case**: Show $P(1)$ is true
2. **Inductive step**: Assume $P(k)$ is true for some $k \ge 1$, then prove $P(k+1)$ is true

If both steps hold, $P(n)$ is true for all $n \in \mathbb{Z}^+$.

## Standard Worked Pattern

> **Prove**: $\displaystyle \sum_{r=1}^{n} f(r) = g(n)$

**Step 1 — Base case ($n=1$):**
LHS $= f(1)$, RHS $= g(1)$ — verify equality.

**Step 2 — Inductive hypothesis:**
Assume for $n=k$:
$$
\sum_{r=1}^{k} f(r) = g(k)
$$

**Step 3 — Inductive step ($k \to k+1$):**
$$
\sum_{r=1}^{k+1} f(r) = \sum_{r=1}^{k} f(r) + f(k+1) = g(k) + f(k+1)
$$
Show $g(k) + f(k+1) = g(k+1)$ using algebraic manipulation.

**Step 4 — Conclusion:**
By the principle of mathematical induction, $P(n)$ is true for all $n \in \mathbb{Z}^+$.

## Example

Prove $\displaystyle \sum_{r=1}^{n} r = \frac{n(n+1)}{2}$.

**Base ($n=1$):** $1 = \frac{1(2)}{2}$ ✓

**Assume true for $n=k$:** $\displaystyle \sum_{r=1}^{k} r = \frac{k(k+1)}{2}$

**For $n=k+1$:**
$$
\sum_{r=1}^{k+1} r = \frac{k(k+1)}{2} + (k+1) = \frac{(k+1)(k+2)}{2}
$$

**Conclusion:** True for all $n \in \mathbb{Z}^+$ by induction.

## Remarks

- Only summation of finite sequences is required (inequalities are **not** required)
- Can also prove divisibility and other algebraic propositions

## Related Topics

- [[The Binomial Theorem]]
- [[Limits]]

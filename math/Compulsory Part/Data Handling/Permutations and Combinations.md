---
tags:
  - math
  - compulsory-part
  - data-handling
  - counting
---

# Permutations and Combinations

## Counting Principles

| Rule | Statement |
| ---- | --------- |
| **Addition Rule** | If event $A$ can occur in $m$ ways and event $B$ in $n$ ways, and they cannot occur together, then there are $m + n$ ways for $A$ or $B$ to occur |
| **Multiplication Rule** | If event $A$ can occur in $m$ ways and event $B$ in $n$ ways, then there are $m \times n$ ways for $A$ and $B$ to occur in sequence |

## Permutations ($nPr$)

The number of ways to arrange $r$ distinct objects chosen from $n$ distinct objects:

$$
P^n_r = \frac{n!}{(n-r)!}
$$

- Order **matters**
- No repetition

Special case: $P^n_n = n!$ (arranging all $n$ objects)

Problems include arrangements where particular objects must be next to each other (treat as a single object).

## Combinations ($nCr$)

The number of ways to choose $r$ distinct objects from $n$ distinct objects:

$$
C^n_r = \binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

- Order does **not** matter
- No repetition

Relationship:
$$
P^n_r = r! \times C^n_r
$$

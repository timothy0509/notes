---
tags:
  - math
  - module-1
  - extended-part
  - foundation-knowledge
  - binomial
  - algebra
---

# Binomial Expansion

## Binomial Theorem

$$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$

where $n$ is a positive integer and $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.

## Summation Notation (Σ)

$$\sum_{k=0}^n \binom{n}{k} a^{n-k} b^k = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \cdots + \binom{n}{n}b^n$$

Properties:

| Property | Expression |
|---|---|
| Symmetry | $\binom{n}{k} = \binom{n}{n-k}$ |
| Pascal's rule | $\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$ |

## Special Cases

- $(1+x)^n = \sum_{k=0}^n \binom{n}{k} x^k$

## Not Required

- Expansion of trinomials
- Greatest coefficient / greatest term
- Properties of binomial coefficients
- Numerical approximation

## Related

- [[Permutations and Combinations (CP)]]

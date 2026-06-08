---
tags:
  - math
  - module-1
  - extended-part
  - statistics
  - distribution
  - poisson
---

# The Poisson Distribution

## Definition

$X \sim \text{Poisson}(\lambda)$ models the number of events occurring in a fixed interval of time/space, where events occur independently at a constant average rate $\lambda > 0$.

$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \ldots$$

### Properties

| Property | Value |
|---|---|
| Mean | $E[X] = \lambda$ |
| Variance | $Var(X) = \lambda$ |

Proofs of mean and variance are **not required**.

## Notes

- Mean = variance = $\lambda$
- Used for rare events over a large number of trials (approximation to binomial when $n$ large, $p$ small, $\lambda = np$)

## Related

- [[The Binomial Distribution]]
- [[Applications of Binomial and Poisson Distributions]]
- [[Probability Distribution, Expectation and Variance]]

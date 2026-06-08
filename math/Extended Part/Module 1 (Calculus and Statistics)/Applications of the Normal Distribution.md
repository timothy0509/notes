---
tags:
  - math
  - module-1
  - extended-part
  - statistics
  - normal
  - applications
---

# Applications of the Normal Distribution

## Finding Probabilities

Given $X \sim N(\mu, \sigma^2)$:

| Probability | Method |
|---|---|
| $P(X > x_1)$ | Standardise: $Z = \frac{x_1 - \mu}{\sigma}$, then $P(Z > z)$ |
| $P(X < x_2)$ | Standardise, then $P(Z < z)$ |
| $P(x_1 < X < x_2)$ | Standardise both, then $P(z_1 < Z < z_2)$ |

## Finding $x$ Given Probability

Given $P(X > x) = \alpha$ (or similar):

1. Find $z$ such that $P(Z > z) = \alpha$ from standard normal table
2. Solve $x = \mu + z\sigma$

Similarly for $P(X < x)$ and $P(x_1 < X < x_2)$.

## Problems

Typical applications: heights, test scores, measurement errors, quality control limits.

## Related

- [[Standardisation of a Normal Variable]]
- [[Basic Definition and Properties of the Normal Distribution]]

---
tags:
  - math
  - module-1
  - extended-part
  - statistics
  - distribution
  - binomial
  - bernoulli
---

# The Binomial Distribution

## Bernoulli Distribution

A single trial with two outcomes: success (prob $p$) and failure (prob $q = 1-p$).

$$X \sim \text{Bernoulli}(p)$$

| Property | Value |
|---|---|
| Mean | $p$ |
| Variance | $p(1-p)$ |

## Binomial Distribution

$X \sim B(n, p)$: number of successes in $n$ independent Bernoulli trials with constant $p$.

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$

### Properties

| Property | Value |
|---|---|
| Mean | $E[X] = np$ |
| Variance | $Var(X) = np(1-p)$ |

Proofs of mean and variance are **not required**.

## Related

- [[Probability Distribution, Expectation and Variance]]
- [[The Poisson Distribution]]
- [[Applications of Binomial and Poisson Distributions]]

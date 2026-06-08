---
tags:
  - math
  - module-1
  - extended-part
  - statistics
  - probability-distribution
  - expectation
  - variance
---

# Probability Distribution, Expectation and Variance

## Discrete Probability Distribution

Represented by:

- **Table**: $x$ with corresponding $P(X=x)$
- **Graph**: bar chart of probabilities
- **Formula**: $P(X=x) = f(x)$

Properties: $0 \le P(X=x) \le 1$ and $\sum_x P(X=x) = 1$.

## Expectation

$$E[X] = \sum x\,P(X=x)$$

For a function $g(X)$:

$$E[g(X)] = \sum g(x)\,P(X=x)$$

### Properties

| Property | Formula |
|---|---|
| Linearity | $E[aX + b] = aE[X] + b$ |

## Variance

$$Var(X) = E[(X-\mu)^2] = E[X^2] - (E[X])^2$$

where $\mu = E[X]$.

### Properties

| Property | Formula |
|---|---|
| Scaling | $Var(aX + b) = a^2\,Var(X)$ |

## Related

- [[Discrete Random Variables]]
- [[The Binomial Distribution]]
- [[The Poisson Distribution]]
- [[Basic Definition and Properties of the Normal Distribution]]

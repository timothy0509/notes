---
tags:
  - math
  - module-1
  - extended-part
  - statistics
  - distribution
  - binomial
  - poisson
  - applications
---

# Applications of Binomial and Poisson Distributions

## Binomial Applications

Situations with:
- Fixed number $n$ of independent trials
- Each trial: success/failure
- Constant probability $p$

Examples: quality control (defective items), survey responses, free-throw shooting.

## Poisson Applications

Situations with:
- Events occurring independently over time/space
- Constant average rate $\lambda$

Examples: number of calls at a call centre per hour, number of accidents per day, number of typing errors per page, number of customers arriving at a queue.

## Poisson Approximation to Binomial

When $n$ is large and $p$ is small:

$$B(n, p) \approx \text{Poisson}(\lambda = np)$$

### Guidelines

- $n \ge 50$ and $p \le 0.1$: approximation is reasonable
- $n \ge 100$ and $np \le 10$: approximation is good

## Related

- [[The Binomial Distribution]]
- [[The Poisson Distribution]]

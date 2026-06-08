---
tags:
  - math
  - module-1
  - extended-part
  - statistics
  - sampling
  - central-limit-theorem
  - estimation
---

# Sampling Distribution and Point Estimates

## Population vs Sample

| Term | Definition |
|---|---|
| Population parameter | A numerical characteristic of the population (e.g. $\mu$, $\sigma^2$) |
| Sample statistic | A numerical characteristic computed from a sample (e.g. $\bar{x}$, $s^2$) |

Population variance: $\sigma^2 = \frac{\sum_{i=1}^N (x_i - \mu)^2}{N}$

## Sampling Distribution of the Sample Mean $\bar{X}$

For a random sample of size $n$ from a population with mean $\mu$ and variance $\sigma^2$:

$$E[\bar{X}] = \mu, \quad Var(\bar{X}) = \frac{\sigma^2}{n}$$

If $X \sim N(\mu, \sigma^2)$, then $\bar{X} \sim N\!\left(\mu, \frac{\sigma^2}{n}\right)$ (proof not required).

## Central Limit Theorem (CLT)

For a sufficiently large sample size $n$ (usually $n \ge 30$), the sampling distribution of $\bar{X}$ is approximately normal regardless of the population distribution:

$$\bar{X} \;\dot{\sim}\; N\!\left(\mu, \frac{\sigma^2}{n}\right)$$

## Point Estimates

| Parameter | Estimator | Formula |
|---|---|---|
| Population mean $\mu$ | Sample mean $\bar{x}$ | $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$ |
| Population variance $\sigma^2$ | Sample variance $s^2$ | $s^2 = \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n-1}$ |

### Unbiased Estimator

An estimator $\hat{\theta}$ is unbiased for $\theta$ if $E[\hat{\theta}] = \theta$.

- $\bar{X}$ is an unbiased estimator of $\mu$: $E[\bar{X}] = \mu$
- $S^2$ is an unbiased estimator of $\sigma^2$: $E[S^2] = \sigma^2$

## Related

- [[Confidence Interval for a Population Mean]]
- [[Basic Definition and Properties of the Normal Distribution]]

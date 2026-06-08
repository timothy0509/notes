---
tags:
  - math
  - module-1
  - extended-part
  - statistics
  - confidence-interval
  - estimation
  - inference
---

# Confidence Interval for a Population Mean

## Concept

A $100(1-\alpha)\%$ confidence interval estimates the range in which the population mean $\mu$ lies, based on sample data.

- $1-\alpha$ is the **confidence level**
- $\alpha$ is the **significance level**

## Known Variance

For a normal population with known variance $\sigma^2$, based on a random sample of size $n$:

$$\left(\bar{x} - z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}},\; \bar{x} + z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}\right)$$

where $z_{\alpha/2}$ is the upper $\alpha/2$ critical value of $N(0,1)$.

## Unknown Variance (Large Sample)

When sample size $n$ is sufficiently large, use sample standard deviation $s$:

$$\left(\bar{x} - z_{\alpha/2} \cdot \frac{s}{\sqrt{n}},\; \bar{x} + z_{\alpha/2} \cdot \frac{s}{\sqrt{n}}\right)$$

## Common Critical Values

| Confidence Level | $\alpha$ | $z_{\alpha/2}$ |
|---|---|---|
| 90% | 0.10 | 1.645 |
| 95% | 0.05 | 1.960 |
| 99% | 0.01 | 2.576 |

## Related

- [[Sampling Distribution and Point Estimates]]
- [[Standardisation of a Normal Variable]]

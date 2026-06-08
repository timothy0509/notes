---
tags:
  - math
  - compulsory-part
  - data-handling
  - statistics
---

# Measures of Dispersion

## Range and Inter-Quartile Range

| Measure | Definition |
| ------- | ---------- |
| Range | Largest value $-$ smallest value |
| Inter-quartile range (IQR) | $Q_3 - Q_1$ |

- $Q_1$: lower quartile (median of lower half)
- $Q_3$: upper quartile (median of upper half)

## Box-and-Whisker Diagram

Displays minimum, $Q_1$, median, $Q_3$, and maximum. Used to compare distributions of different data sets.

## Standard Deviation

For **ungrouped** data ($N$ items, mean $\mu$):
$$
\sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}}
$$

For **grouped** data (with class marks $x_i$, frequencies $f_i$):
$$
\sigma = \sqrt{\frac{\sum f_i (x_i - \mu)^2}{\sum f_i}}
$$

**Variance**: $\sigma^2$ (square of standard deviation)

## Comparing Dispersions

- Use **range** or **IQR** when data has extreme values
- Use **standard deviation** for more precise comparison when data is roughly symmetric

## Standard Scores and Normal Distribution

### Standard Score ($z$-score)

$$
z = \frac{x - \mu}{\sigma}
$$

Measures how many standard deviations a value is above or below the mean.

### Normal Distribution

- Bell-shaped, symmetrical about the mean
- Mean $=$ mode $=$ median
- Area under the curve $= 1$
- Empirical rule:
  - $\mu \pm \sigma$: $\approx 68\%$ of data
  - $\mu \pm 2\sigma$: $\approx 95\%$ of data
  - $\mu \pm 3\sigma$: $\approx 99.7\%$ of data

## Effect of Operations on Dispersion

| Operation on data | Effect on dispersion |
| ----------------- | -------------------- |
| Add a constant $k$ to every item | No change |
| Multiply every item by a constant $k$ | Dispersion multiplied by $|k|$ (SD $\times |k|$, variance $\times k^2$) |

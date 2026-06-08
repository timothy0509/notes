---
tags:
  - math
  - compulsory-part
  - number-algebra
  - exponential
  - logarithmic
---

# Exponential and Logarithmic Functions

## Rational Indices
$$a^{\frac{m}{n}} = \sqrt[n]{a^m}, \qquad a^{-\frac{m}{n}} = \frac{1}{a^{\frac{m}{n}}}$$

## Laws of Rational Indices
| Law | Expression |
|-----|------------|
| Product | $a^p a^q = a^{p+q}$ |
| Quotient | $\dfrac{a^p}{a^q} = a^{p-q}$ |
| Power | $(a^p)^q = a^{pq}$ |
| Power of product | $a^p b^p = (ab)^p$ |
| Power of quotient | $\dfrac{a^p}{b^p} = \left(\dfrac{a}{b}\right)^p$ |

## Definition of Logarithms
$$y = \log_a x \iff a^y = x \quad (a>0, a\neq1, x>0)$$

## Properties of Logarithms
| Property | Formula |
|----------|--------|
| Basic | $\log_a 1 = 0$, $\log_a a = 1$ |
| Product | $\log_a MN = \log_a M + \log_a N$ |
| Quotient | $\log_a \dfrac{M}{N} = \log_a M - \log_a N$ |
| Power | $\log_a M^k = k\log_a M$ |
| Change of Base | $\log_b N = \dfrac{\log_a N}{\log_a b}$ |

## Graphs of Exponential and Logarithmic Functions
- $f(x)=a^x$: domain $\mathbb{R}$, increases for $a>1$, decreases for $0<a<1$
- $f(x)=\log_a x$: domain $x>0$, symmetric to $y=a^x$ about $y=x$
- No $x$-intercept for $y=a^x$; $y$-intercept at $(0,1)$
- $y=\log_a x$: $x$-intercept at $(1,0)$, no $y$-intercept

## Solving Exponential and Logarithmic Equations
Use laws of indices and properties of logarithms.
Equations transformable to quadratics (e.g. $4^x-3\cdot2^x-4=0$) covered in [[More about Equations]].

## Applications
- Richter scale (earthquake intensity): $M = \log_{10}\frac{I}{I_0}$
- Decibels (sound intensity): $L = 10\log_{10}\frac{I}{I_0}$

## Historical Development
Logarithms developed by John Napier (17th century). Led to slide rules and logarithmic tables as calculation tools.

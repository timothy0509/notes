---
tags:
  - math
  - module-1
  - extended-part
  - foundation-knowledge
  - exponential
  - logarithmic
  - calculus
---

# Exponential and Logarithmic Functions

## Definition of $e$

$$e = \lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n \approx 2.71828\ldots$$

## Exponential Series

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots = \sum_{n=0}^\infty \frac{x^n}{n!}$$

## Functions $y = e^x$ and $y = \ln x$

| Property | $y = e^x$ | $y = \ln x$ |
|---|---|---|
| Domain | $\mathbb{R}$ | $x > 0$ |
| Range | $y > 0$ | $\mathbb{R}$ |
| Intercept | $(0, 1)$ | $(1, 0)$ |
| Asymptote | $y = 0$ (horizontal) | $x = 0$ (vertical) |
| Monotonicity | Strictly increasing | Strictly increasing |

Relations: $\ln(e^x) = x$, $e^{\ln x} = x$ — they are inverse functions.

## Applications

### Compound Interest

$$A = Pe^{rt}$$

where $A$ = final amount, $P$ = principal, $r$ = annual rate, $t$ = time in years (continuous compounding).

### Population Growth / Radioactive Decay

$$N(t) = N_0 e^{kt}$$

- $k > 0$: growth
- $k < 0$: decay (half-life $t_{1/2} = \ln 2 / |k|$)

## Linearisation of Non-linear Relations

Transform $y = k a^x$ and $y = k[f(x)]^n$ into linear form.

### $y = k a^x$

Take natural logs: $\ln y = \ln k + x \ln a$.

Let $Y = \ln y$, $X = x$, $A = \ln a$, $B = \ln k$:

$$Y = AX + B \quad \text{(linear)}$$

### $y = k[f(x)]^n$

Take natural logs: $\ln y = \ln k + n \ln[f(x)]$.

Let $Y = \ln y$, $X = \ln[f(x)]$, slope $= n$, intercept $= \ln k$:

$$Y = nX + \ln k \quad \text{(linear)}$$

Plot the transformed data, read slope and intercept to find constants.

## Related

- [[Exponential and Logarithmic Functions (CP)]]
- [[Derivative of a Function]]

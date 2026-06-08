---
tags:
  - math
  - module-2
  - extended-part
  - calculus
  - differentiation
---

# Differentiation

## Derivative from First Principles

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

| Function | Derivative |
|----------|-----------|
| $C$ (constant) | $0$ |
| $x^n$ ($n$ positive integer) | $nx^{n-1}$ |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $\frac{1}{x}$ |

## Differentiation Rules

| Rule | Formula |
|------|---------|
| Addition | $\frac{d}{dx}(u+v) = \frac{du}{dx} + \frac{dv}{dx}$ |
| Product | $\frac{d}{dx}(uv) = v\frac{du}{dx} + u\frac{dv}{dx}$ |
| Quotient | $\frac{d}{dx}\left(\frac{u}{v}\right) = \frac{v\frac{du}{dx} - u\frac{dv}{dx}}{v^2}$ |
| Chain | $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$ |

## Derivatives of Elementary Functions

$$
\frac{d}{dx}(\tan x) = \sec^2 x, \quad
\frac{d}{dx}(\sec x) = \sec x \tan x, \quad
\frac{d}{dx}(\csc x) = -\csc x \cot x, \quad
\frac{d}{dx}(\cot x) = -\csc^2 x
$$

$$
\frac{d}{dx}(\ln|x|) = \frac{1}{x}, \quad
\frac{d}{dx}(a^x) = a^x \ln a, \quad
\frac{d}{dx}(\log_a x) = \frac{1}{x \ln a}
$$

## Implicit Differentiation

For equations where $y$ is not explicitly solved for, differentiate both sides with respect to $x$ and solve for $\frac{dy}{dx}$.

## Logarithmic Differentiation

Take $\ln$ of both sides, differentiate implicitly, then solve for $\frac{dy}{dx}$. Useful for functions of the form $y = [f(x)]^{g(x)}$ or products of many factors.

## Second Derivative and Concavity

$$
f''(x) = \frac{d}{dx}(f'(x)) = \frac{d^2y}{dx^2}
$$

| $f''(x)$ | Concavity |
|----------|-----------|
| $f''(x) > 0$ | Concave up |
| $f''(x) < 0$ | Concave down |

**Second Derivative Test:** If $f'(c) = 0$ and $f''(c) < 0$, then $c$ is a local max; if $f''(c) > 0$, then $c$ is a local min.

## Related Topics

- [[Limits]]
- [[Applications of Differentiation]]
- [[Introduction to e]]
